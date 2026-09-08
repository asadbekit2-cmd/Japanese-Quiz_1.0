/* ===================== JLPT N3 — O'yin dvigateli ===================== */
(function () {
  "use strict";
  const META = window.JLPT_META || { levels: [], levelsCount: 15 };
  const TESTS = window.JLPT_TESTS || {};
  const getTest = id => TESTS[id] || TESTS[String(id)] || null;
  const isReady = id => !!getTest(id);

  const TYPE_UZ = {
    kanji_reading: "Kanji o'qilishi", orthography: "Yozuv (kanji)", context: "Kontekst",
    paraphrase: "Sinonim", usage: "Qo'llanish", grammar_form: "Grammatik shakl",
    sentence_order: "Gap tuzish", text_grammar: "Matn grammatikasi"
  };

  /* ======= EXAM MODE metadata ======= */
  const EXAM_PROB = {
    kanji_reading:  { no:"問題1", name:"漢字読み",      bigSec:"文字・語彙", color:"vocab",   count:8  },
    orthography:    { no:"問題2", name:"表記",          bigSec:"文字・語彙", color:"vocab",   count:6  },
    context:        { no:"問題3", name:"文脈規定",      bigSec:"文字・語彙", color:"vocab",   count:11 },
    paraphrase:     { no:"問題4", name:"言い換え類義",   bigSec:"文字・語彙", color:"vocab",   count:5  },
    usage:          { no:"問題5", name:"用法",          bigSec:"文字・語彙", color:"vocab",   count:5  },
    grammar_form:   { no:"問題1", name:"文法形式の判断", bigSec:"文法",      color:"grammar", count:13 },
    sentence_order: { no:"問題2", name:"文の組み立て",  bigSec:"文法",      color:"grammar", count:5  },
    text_grammar:   { no:"問題3", name:"文章の文法",    bigSec:"文法",      color:"grammar", count:5  }
  };

  /* ---------- saqlash ---------- */
  const SKEY = "jlpt_n3_game_v1";
  const def = () => ({ unlocked: 1, stars: {}, best: {}, xp: 0, streak: 0, lastDay: null, srs: {} });
  let S = load();
  function load() { try { return Object.assign(def(), JSON.parse(localStorage.getItem(SKEY)) || {}); } catch (e) { return def(); } }
  function save() { try { localStorage.setItem(SKEY, JSON.stringify(S)); } catch (e) {} }

  function touchStreak() {
    const today = new Date().toISOString().slice(0, 10);
    if (S.lastDay === today) return;
    const y = new Date(Date.now() - 864e5).toISOString().slice(0, 10);
    S.streak = (S.lastDay === y) ? (S.streak + 1) : 1;
    S.lastDay = today; save();
  }

  /* ---------- savollar indeksi (SRS uchun) ---------- */
  const QINDEX = {}; // qid -> {q, type, instruction_jp, instruction_uz, sectionName, levelId, problem}
  function buildIndex() {
    Object.keys(TESTS).forEach(k => {
      const t = TESTS[k]; if (!t) return;
      t.sections.forEach(sec => sec.problems.forEach(pr => pr.questions.forEach(q => {
        QINDEX[q.id] = { q, type: pr.type, instruction_jp: pr.instruction_jp, instruction_uz: pr.instruction_uz,
          sectionName: sec.name_jp, levelId: t.id, problem: pr };
      })));
    });
  }

  /* ---------- DOM yordamchilar ---------- */
  const $ = s => document.querySelector(s);
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const esc = s => (window.Furigana ? Furigana.escapeHtml(s) : String(s || ""));
  function show(id) { document.querySelectorAll(".screen").forEach(s => s.classList.remove("active")); $("#" + id).classList.add("active"); }
  function toast(msg) { const t = $("#toast"); t.textContent = msg; t.classList.add("show"); clearTimeout(t._t); t._t = setTimeout(() => t.classList.remove("show"), 2200); }

  /* ---------- furigana + tarjima ---------- */
  let furiOn = true;   // kanji o'qilishi doim ko'rinib tursin
  let trOn = false;    // tarjima ko'rsatish holati
  if (window.Furigana) { Furigana.init(); Furigana.onReady(function (ok) { if (ok && furiOn && Q) { const it = Q.queue[Q.idx]; if (it) renderByType(it, it.q); } }); }
  function jp(text, skip) { return (furiOn && window.Furigana && Furigana.available()) ? Furigana.toRuby(text, skip) : esc(text); }

  /* ===================== HOME ===================== */
  function renderHome() {
    $("#hud-xp").textContent = S.xp;
    $("#hud-streak").textContent = S.streak;
    const done = Object.keys(S.stars).length;
    $("#po-fill").style.width = (done / META.levelsCount * 100) + "%";
    $("#po-label").textContent = done + " / " + META.levelsCount + " bosqich";
    $("#review-count").textContent = dueCount() + " ta";

    const map = $("#level-map"); map.innerHTML = "";
    META.levels.forEach(lv => {
      const ready = isReady(lv.id);
      const stars = S.stars[lv.id] || 0;
      const node = el("div", "level");
      if (!ready) node.classList.add("soon");
      else if (stars > 0) node.classList.add("done");
      else node.classList.add("current");

      let badge = "";
      if (!ready) badge = "🛠";
      else if (stars > 0) badge = "✓";

      // Tur tugmalari (8 ta) — qisqa belgilar
      const TYPE_CHIPS = [
        { type:"kanji_reading",  label:"漢", cls:"voc"  },
        { type:"orthography",    label:"表", cls:"voc"  },
        { type:"context",        label:"文脈", cls:"voc"  },
        { type:"paraphrase",     label:"類", cls:"voc"  },
        { type:"usage",          label:"用", cls:"voc"  },
        { type:"grammar_form",   label:"文法", cls:"gram" },
        { type:"sentence_order", label:"★",  cls:"gram" },
        { type:"text_grammar",   label:"章", cls:"gram" }
      ];

      const chipsHtml = ready
        ? `<div class="lv-chips">${TYPE_CHIPS.map(c =>
            `<span class="lv-chip ${c.cls}" data-t="${c.type}">${c.label}</span>`
          ).join("")}</div>`
        : `<div class="lv-soon">Tez kunda</div>`;

      node.innerHTML =
        `<div class="lv-badge">${badge}</div>` +
        `<div><div class="lv-no">${lv.id}</div><div class="lv-jp">${esc(lv.title_jp)}</div></div>` +
        `<div>` +
          `<div class="lv-uz">${esc(lv.title_uz)}</div>` +
          (ready
            ? `<div class="lv-stars">${stars ? "★★★".slice(0,stars)+"☆☆☆".slice(0,3-stars) : "☆☆☆"}</div>`
            : "") +
          chipsHtml +
        `</div>`;

      // Katta karta → boshdan 58 savol
      node.addEventListener("click", (e) => {
        if (!ready) { toast("Bu bosqich hali tayyorlanmoqda 🛠"); return; }
        if (e.target.classList.contains("lv-chip")) return;
        startLevel(lv.id);
      });

      // Kichik chip tugmalari → to'g'ri o'sha turga
      if (ready) {
        node.querySelectorAll(".lv-chip").forEach(chip => {
          chip.addEventListener("click", (e) => {
            e.stopPropagation();
            startLevelByType(lv.id, chip.dataset.t);
          });
        });
      }
      map.appendChild(node);
    });
  }

  /* ===================== SRS ===================== */
  function dueCount() { const now = Date.now(); return Object.values(S.srs).filter(r => r.due <= now && QINDEX[r.id]).length; }
  function srsWrong(qid) {
    const r = S.srs[qid] || { id: qid, ef: 2.2, reps: 0, interval: 0, lapses: 0 };
    r.lapses++; r.reps = 0; r.interval = 0; r.due = Date.now() + 6 * 36e5; // 6 soatdan keyin
    S.srs[qid] = r; save();
  }
  function srsRight(qid, fromReview) {
    const r = S.srs[qid]; if (!r) return;
    r.reps++; r.ef = Math.max(1.3, r.ef + 0.1);
    r.interval = r.reps <= 1 ? 1 : Math.round((r.interval || 1) * r.ef);
    r.due = Date.now() + r.interval * 864e5;
    if (fromReview && r.reps >= 3) delete S.srs[qid];
    save();
  }

  /* ===================== QUIZ ===================== */
  let Q = null; // joriy sessiya
  let lastWrongItems = []; // oxirgi sessiya xatolari → mashq uchun
  function buildQueue(levelId, filterType) {
    const t = getTest(levelId); const items = [];
    t.sections.forEach(sec => sec.problems.forEach(pr => pr.questions.forEach(q => {
      if (filterType && pr.type !== filterType) return;
      items.push({ q, type: pr.type, instr_jp: pr.instruction_jp, instr_uz: pr.instruction_uz,
        sec: sec.name_jp, problem: pr, firstTry: true });
    })));
    return items;
  }

  // Bitta tur bo'yicha (masalan faqat kanji_reading yoki sentence_order)
  function startLevelByType(levelId, type) {
    touchStreak();
    const t = getTest(levelId);
    const ep = EXAM_PROB[type] || {};
    const items = [];
    t.sections.forEach(sec => sec.problems.forEach(pr => pr.questions.forEach(q => {
      if (pr.type !== type) return;
      items.push({ q, type: pr.type, instr_jp: pr.instruction_jp, instr_uz: pr.instruction_uz,
        sec: sec.name_jp, problem: pr, firstTry: true });
    })));
    if (!items.length) { toast("Bu bo'limda savol topilmadi"); return; }
    Q = {
      mode: "level", levelId,
      title: t.title_uz + " · " + (ep.no || type),
      jp: t.title_jp,
      filterType: type,
      queue: items, idx: 0, total: items.length,
      firstCorrect: 0, hearts: 5, combo: 0, maxCombo: 0,
      startedAt: Date.now(),
      timeLeft: Math.ceil(items.length / 58 * (t.minutes || 50) * 60),
      answered: 0
    };
    show("screen-quiz");
    startTimer();
    nextQuestion();
  }

  // Vocab yoki Grammar bo'limiga to'g'ri sakrab o'tish
  function startLevelSection(levelId, section) {
    const VOCAB_TYPES = ["kanji_reading","orthography","context","paraphrase","usage"];
    const GRAM_TYPES  = ["grammar_form","sentence_order","text_grammar"];
    const types = section === "vocab" ? VOCAB_TYPES : GRAM_TYPES;
    touchStreak();
    const t = getTest(levelId);
    const items = [];
    t.sections.forEach(sec => sec.problems.forEach(pr => pr.questions.forEach(q => {
      if (!types.includes(pr.type)) return;
      items.push({ q, type: pr.type, instr_jp: pr.instruction_jp, instr_uz: pr.instruction_uz,
        sec: sec.name_jp, problem: pr, firstTry: true });
    })));
    const label = section === "vocab" ? "語彙" : "文法";
    Q = {
      mode: "level", levelId,
      title: t.title_uz + " · " + label,
      jp: t.title_jp,
      filterType: section,
      queue: items, idx: 0, total: items.length,
      firstCorrect: 0, hearts: 5, combo: 0, maxCombo: 0,
      startedAt: Date.now(),
      timeLeft: Math.ceil(items.length / 58 * (t.minutes || 50) * 60),
      answered: 0
    };
    show("screen-quiz");
    startTimer();
    nextQuestion();
  }

  function startLevel(levelId) {
    touchStreak();
    const t = getTest(levelId);
    Q = {
      mode: "level", levelId, title: t.title_uz, jp: t.title_jp,
      filterType: null,
      queue: buildQueue(levelId), idx: 0,
      total: 0, firstCorrect: 0, hearts: 5, combo: 0, maxCombo: 0,
      startedAt: Date.now(), timeLeft: (t.minutes || 50) * 60, answered: 0
    };
    Q.total = Q.queue.length;
    show("screen-quiz");
    startTimer();
    nextQuestion();
  }

  /* ===== LEVEL OPTIONS SHEET ===== */
  const LSO_TYPES = [
    { type:"kanji_reading",  no:"問題1", name:"漢字読み",      sec:"vocab",   emoji:"📖", count:8  },
    { type:"orthography",    no:"問題2", name:"表記",          sec:"vocab",   emoji:"✏️", count:6  },
    { type:"context",        no:"問題3", name:"文脈規定",      sec:"vocab",   emoji:"💬", count:11 },
    { type:"paraphrase",     no:"問題4", name:"言い換え類義",   sec:"vocab",   emoji:"🔄", count:5  },
    { type:"usage",          no:"問題5", name:"用法",          sec:"vocab",   emoji:"🎯", count:5  },
    { type:"grammar_form",   no:"問題1", name:"文法形式",      sec:"grammar", emoji:"📝", count:13 },
    { type:"sentence_order", no:"問題2", name:"文の組み立て",  sec:"grammar", emoji:"🔀", count:5  },
    { type:"text_grammar",   no:"問題3", name:"文章の文法",    sec:"grammar", emoji:"📄", count:5  }
  ];

  let _lsoLevelId = null;

  function showLevelOptions(levelId) {
    _lsoLevelId = levelId;
    const t = getTest(levelId);
    const stars = S.stars[levelId] || 0;
    const sheet = $("#level-options-sheet");

    // Header
    $("#lso-jp").textContent = t.title_jp;
    $("#lso-uz").textContent = t.title_uz;
    $("#lso-total").textContent = "58 savol";
    $("#lso-stars").innerHTML = stars
      ? "★★★".slice(0,stars) + "☆☆☆".slice(0,3-stars)
      : "☆☆☆";

    // Build chips
    const vocEl  = $("#lso-vocab-chips");
    const gramEl = $("#lso-gram-chips");
    vocEl.innerHTML = ""; gramEl.innerHTML = "";

    LSO_TYPES.forEach(opt => {
      const chip = el("button", "lso-chip lso-chip-" + opt.sec);
      chip.innerHTML =
        `<span class="lsc-no">${esc(opt.no)}</span>` +
        `<span class="lsc-name">${esc(opt.emoji)} ${esc(opt.name)}</span>` +
        `<span class="lsc-count">${opt.count} savol</span>`;
      chip.addEventListener("click", () => startLevelByType(levelId, opt.type));
      (opt.sec === "vocab" ? vocEl : gramEl).appendChild(chip);
    });

    sheet.classList.add("show");
  }

  function closeLevelOptions() {
    $("#level-options-sheet").classList.remove("show");
    _lsoLevelId = null;
  }

  /* ===================== RANDOM MOCK ===================== */
  function startRandomMock() {
    touchStreak();

    function shuffle(arr) {
      const a = arr.slice();
      for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
      }
      return a;
    }

    // Barcha testlardan savollarni turlar bo'yicha guruhlash
    const byType = {};
    Object.keys(TESTS).forEach(k => {
      const t = TESTS[k]; if (!t) return;
      t.sections.forEach(sec => sec.problems.forEach(pr => pr.questions.forEach(q => {
        const item = { q, type: pr.type, instr_jp: pr.instruction_jp,
          instr_uz: pr.instruction_uz, sec: sec.name_jp,
          problem: pr, firstTry: true, levelId: t.id };
        if (!byType[pr.type]) byType[pr.type] = [];
        byType[pr.type].push(item);
      })));
    });

    // Real JLPT N3 tartibi va soni (jami 58 ta — xuddi haqiqiy test kabi)
    const ORDER = [
      { type: "kanji_reading",  count: 8,  sec: "文字・語彙" },
      { type: "orthography",    count: 6,  sec: "文字・語彙" },
      { type: "context",        count: 11, sec: "文字・語彙" },
      { type: "paraphrase",     count: 5,  sec: "文字・語彙" },
      { type: "usage",          count: 5,  sec: "文字・語彙" },
      { type: "grammar_form",   count: 13, sec: "文法" },
      { type: "sentence_order", count: 5,  sec: "文法" },
      { type: "text_grammar",   count: 5,  sec: "文法" }
    ];

    // text_grammar: bir testdan to'liq 5 ta savol birga kelishi shart
    const tgByLevel = {};
    (byType["text_grammar"] || []).forEach(it => {
      if (!tgByLevel[it.levelId]) tgByLevel[it.levelId] = [];
      tgByLevel[it.levelId].push(it);
    });
    const tgLevels = shuffle(Object.keys(tgByLevel));
    const tgItems = tgLevels.length > 0 ? tgByLevel[tgLevels[0]] : [];

    // Har bir turdan tartibda savollarni olamiz
    const finalQueue = [];
    ORDER.forEach(({ type, count }) => {
      if (type === "text_grammar") {
        finalQueue.push(...tgItems.slice(0, count));
      } else {
        finalQueue.push(...shuffle(byType[type] || []).slice(0, count));
      }
    });

    // Sektsiya jami hisobini oldindan hisoblash
    const secTotals = {};
    finalQueue.forEach(it => {
      const bs = (EXAM_PROB[it.type] || {}).bigSec || "?";
      secTotals[bs] = (secTotals[bs] || 0) + 1;
    });

    Q = {
      mode: "random", title: "Random Mock", jp: "ランダムテスト",
      queue: finalQueue, idx: 0,
      total: finalQueue.length, firstCorrect: 0,
      hearts: 99, combo: 0, maxCombo: 0,
      startedAt: Date.now(), timeLeft: 50 * 60, answered: 0,
      secTotals, secCorrect: {}, lastType: null, timeWarn: {}
    };
    show("screen-quiz");
    const qz = $("#screen-quiz");
    qz.classList.add("exam-mode");
    startTimer();
    // Birinchi seksiyani ko'rsatish
    showExamSectionBreak(finalQueue[0], false, () => nextQuestion());
  }

  /* ===== EXAM SECTION BREAK ===== */
  function showExamSectionBreak(item, isTransition, onContinue) {
    const ep = EXAM_PROB[item.type] || {};
    const overlay = $("#exam-section-break");
    $("#esb-badge").textContent  = ep.bigSec  || "";
    $("#esb-badge").className    = "esb-badge esb-" + (ep.color || "vocab");
    $("#esb-prob-no").textContent = ep.no     || "";
    $("#esb-prob-name").textContent = ep.name || "";
    // Remaining question count
    const remaining = Q.queue.slice(Q.idx).filter(it => it.type === item.type).length;
    $("#esb-count").textContent  = remaining + " ta savol";
    // Progress fill (how far through the test)
    const pct = Q.idx / Q.total * 100;
    $("#esb-fill").style.width   = pct + "%";
    overlay.classList.add("show");

    const go = () => {
      overlay.classList.remove("show");
      setTimeout(onContinue, 280);
    };
    // Auto-continue after 2.2s (or click button)
    const autoT = setTimeout(go, isTransition ? 2200 : 2800);
    const btn = $("#btn-esb-continue");
    const handler = () => { clearTimeout(autoT); go(); };
    btn.onclick = handler;
  }

  function startReview() {
    const now = Date.now();
    const due = Object.values(S.srs).filter(r => r.due <= now && QINDEX[r.id]).slice(0, 30);
    if (!due.length) { toast("Hozircha takrorlash uchun savol yo'q ✨"); return; }
    const queue = due.map(r => { const ix = QINDEX[r.id]; return { q: ix.q, type: ix.type, instr_jp: ix.instruction_jp, instr_uz: ix.instruction_uz, sec: ix.sectionName, problem: ix.problem, firstTry: true, review: true }; });
    Q = { mode: "review", title: "Takrorlash", jp: "復習", queue, idx: 0, total: queue.length, firstCorrect: 0, hearts: 5, combo: 0, maxCombo: 0, startedAt: Date.now(), timeLeft: 0, answered: 0 };
    show("screen-quiz");
    $("#quiz-timer").style.display = "none";
    nextQuestion();
  }

  /* ---------- timer ---------- */
  function startTimer() {
    $("#quiz-timer").style.display = "";
    clearInterval(Q._timer);
    drawTimer();
    Q._timer = setInterval(() => {
      Q.timeLeft--;
      if (Q.timeLeft <= 0) {
        Q.timeLeft = 0; clearInterval(Q._timer);
        if (Q.mode === "random") {
          // Mock testda vaqt tugasa — test to'xtaydi
          toast("⏱ Vaqt tugadi!");
          setTimeout(() => finishLevel(), 900);
          return;
        }
      }
      // Exam mode time warnings
      if (Q.mode === "random" && !Q.timeWarn) Q.timeWarn = {};
      if (Q.mode === "random") {
        if (Q.timeLeft === 1200 && !Q.timeWarn[1200]) { Q.timeWarn[1200]=1; toast("⏱ 残り20分 — 20 daqiqa qoldi!"); }
        if (Q.timeLeft === 600  && !Q.timeWarn[600])  { Q.timeWarn[600]=1;  toast("⚠️ 残り10分 — 10 daqiqa qoldi!"); }
        if (Q.timeLeft === 300  && !Q.timeWarn[300])  { Q.timeWarn[300]=1;  toast("🔴 残り5分 — 5 daqiqa qoldi!"); }
        if (Q.timeLeft === 60   && !Q.timeWarn[60])   { Q.timeWarn[60]=1;   toast("⚡ 残り1分 — 1 daqiqa!"); }
      }
      drawTimer();
    }, 1000);
  }
  function drawTimer() {
    const m = Math.floor(Q.timeLeft / 60), s = Q.timeLeft % 60;
    const t = $("#quiz-timer");
    t.textContent = "⏱ " + m + ":" + String(s).padStart(2, "0");
    t.classList.toggle("low",  Q.timeLeft <= 60);
    t.classList.toggle("warn", Q.mode === "random" && Q.timeLeft > 60 && Q.timeLeft <= 300);
  }

  function drawHearts() {
    // Hearts olib tashlandi — bo'sh funksiya
    const h = $("#hearts"); if (h) h.innerHTML = "";
  }

  /* ---------- savolni ko'rsatish ---------- */
  let picked = null;
  function nextQuestion() {
    $("#feedback").classList.remove("show", "ok", "bad");
    if (Q.idx >= Q.queue.length) return finishLevel();
    const item = Q.queue[Q.idx]; const q = item.q; picked = null;

    // ===== EXAM MODE: section break check =====
    if (Q.mode === "random" && item.type !== Q.lastType && Q.idx > 0) {
      Q.lastType = item.type;
      showExamSectionBreak(item, true, () => renderQuestion(item, q));
      return;
    }
    if (Q.mode === "random") Q.lastType = item.type;

    renderQuestion(item, q);
  }

  function renderQuestion(item, q) {
    const isExam = Q.mode === "random";
    const ep = isExam ? (EXAM_PROB[item.type] || {}) : null;

    // Level / section tags
    if (isExam) {
      $("#quiz-level-tag").textContent = "🎓 Random Mock";
      const secTag = $("#quiz-section-tag");
      secTag.textContent = (ep.no || "") + " " + (ep.bigSec || "");
      secTag.className = "sec-tag " + (ep.color === "grammar" ? "gram-sec" : "voc-sec");
      // Savol raqami
      $("#quiz-counter").textContent = "Q" + (Q.idx + 1) + " / " + Q.total;
    } else {
      $("#quiz-level-tag").textContent = (Q.mode === "review" ? "🔁 " : "") + Q.title;
      $("#quiz-section-tag").textContent = item.sec || "";
      $("#quiz-section-tag").className = "sec-tag";
      $("#quiz-counter").textContent = (Q.answered + 1) + (Q.mode === "level" ? " / ~" + Q.total : "");
    }

    $("#qbar-fill").style.width = (Q.answered / Q.total * 100) + "%";
    drawHearts();

    // ko'rsatma
    $("#q-instruction").innerHTML = `<span class="jp">${esc(item.instr_jp || "")}</span>` + (item.instr_uz ? `<span class="uz">${esc(item.instr_uz)}</span>` : "");

    // stem + options turga qarab
    renderByType(item, q);

    // tugmalar
    $("#btn-check").disabled = true;
    $("#btn-check").style.display = "";
    $("#btn-furigana").classList.toggle("on", furiOn);
  }

  function renderStemMarkup(text, type) {
    // 【...】 -> target, （　） -> blank
    let html = "";
    const parts = String(text).split(/【([^】]*)】/);
    for (let i = 0; i < parts.length; i++) {
      if (i % 2 === 1) {
        const tgt = parts[i];
        html += type === "kanji_reading"
          ? `<span class="target">${esc(tgt)}</span>`        // o'qilish savoli: furigana yo'q
          : `<span class="target">${jp(tgt)}</span>`;
      } else {
        html += jp(parts[i]);
      }
    }
    html = html.replace(/（[\s　]*）/g, '<span class="blank">（　）</span>');
    return html;
  }

  function renderByType(item, q) {
    const type = item.type, stem = $("#q-stem"), opts = $("#q-options");
    const isGram = ["grammar_form","sentence_order","text_grammar"].includes(type);
    const examExtra = (Q && Q.mode === "random") ? (isGram ? " gram-card" : " voc-card") : "";
    opts.innerHTML = ""; stem.className = "stem-card" + examExtra;

    if (type === "usage") {
      stem.innerHTML = `<span class="usage-word">${jp(q.stem)}</span>`;
      buildOptions(q.options, true, q.answer);
    } else if (type === "sentence_order") {
      const slots = []; for (let i = 1; i <= 4; i++) slots.push(i === q.starPos ? '<span class="star-slot">★</span>' : '<span class="blank">＿＿</span>');
      stem.innerHTML = jp(q.prefix || "") + " " + slots.join(" ") + " " + jp(q.suffix || "");
      buildOptions(q.options, false, q.answer);
    } else if (type === "text_grammar") {
      const pr = item.problem;
      stem.className = "stem-card passage";
      stem.innerHTML = renderPassage(pr.passage, pr.passage_title, q.blankNo);
      buildOptions(q.options, false, q.answer);
    } else {
      stem.innerHTML = renderStemMarkup(q.stem, type);
      buildOptions(q.options, false, q.answer);
    }
    addTranslate(item, q);
  }

  /* ---------- tarjima (🌐) ---------- */
  function translationHTML(item, q) {
    if (item.type === "usage" && q.optsTr) {
      return "<b>Gaplar tarjimasi:</b><br>" + q.optsTr.map((t, i) => `<span class="trn">${i + 1}.</span> ${esc(t)}`).join("<br>");
    }
    if (item.type === "text_grammar") {
      return "<b>Matn tarjimasi:</b><br>" + esc((item.problem && item.problem.passage_tr) || q.tr || "—");
    }
    return "<b>Tarjima:</b> " + esc(q.tr || "—");
  }
  function addTranslate(item, q) {
    const stem = $("#q-stem");
    const btn = el("button", "tr-btn" + (trOn ? " on" : ""), "🌐");
    btn.title = "Tarjima (o'zbekcha)";
    const panel = el("div", "translation" + (trOn ? "" : " hidden"));
    panel.innerHTML = translationHTML(item, q);
    btn.addEventListener("click", () => { trOn = panel.classList.toggle("hidden") ? false : true; btn.classList.toggle("on", trOn); });
    stem.appendChild(btn);
    stem.appendChild(panel);
  }

  function renderPassage(passage, title, activeNo) {
    let html = title ? `<span class="pt">${esc(title)}</span>` : "";
    // {{19}}, {{22a}} kabi belgilarni chiplarga aylantiramiz
    const raw = String(passage);
    let body = "";
    const re = /\{\{(\d+)([ab]?)\}\}/g; let last = 0, m;
    while ((m = re.exec(raw)) !== null) {
      body += jp(raw.slice(last, m.index));
      const no = m[1], active = (no === String(activeNo));
      body += `<span class="bk${active ? " active" : ""}">${no}${m[2] || ""}</span>`;
      last = re.lastIndex;
    }
    body += jp(raw.slice(last));
    return html + body.replace(/\n/g, "<br>");
  }

  function shuffle(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function buildOptions(options, isSentence, correctAnswer) {
    const wrap = $("#q-options"); wrap.innerHTML = "";
    // Javoblarni aralashtiramiz, to'g'ri javobning yangi pozitsiyasini kuzatamiz
    const correctText = options[correctAnswer - 1];
    const indices = shuffle([...Array(options.length).keys()]); // [0,1,2,3] aralashtirilgan
    // Yangi to'g'ri javob pozitsiyasini saqlash
    let newCorrect = 1;
    indices.forEach((origIdx, newIdx) => {
      const o = options[origIdx];
      const n = newIdx + 1;
      if (o === correctText) newCorrect = n;
      const node = el("div", "opt");
      node.dataset.n = n;
      node.dataset.origN = origIdx + 1;
      node.innerHTML = `<span class="num">${n}</span><span class="otext">${jp(o)}</span>`;
      node.addEventListener("click", () => {
        if (node.classList.contains("disabled")) return;
        wrap.querySelectorAll(".opt").forEach(x => x.classList.remove("sel"));
        node.classList.add("sel"); picked = n; $("#btn-check").disabled = false;
      });
      wrap.appendChild(node);
    });
    // Joriy savolning to'g'ri javobini yangilangan pozitsiyaga o'rnatamiz
    if (Q && Q.queue && Q.queue[Q.idx]) {
      Q.queue[Q.idx]._shuffledAnswer = newCorrect;
    }
  }

  /* ---------- tekshirish ---------- */
  function checkAnswer() {
    if (picked == null) return;
    const item = Q.queue[Q.idx], q = item.q;
    // Shuffled bo'lgan to'g'ri javob pozitsiyasini olamiz
    const correct = item._shuffledAnswer !== undefined ? item._shuffledAnswer : q.answer;
    const wrap = $("#q-options");
    wrap.querySelectorAll(".opt").forEach(o => {
      o.classList.add("disabled");
      const n = +o.dataset.n;
      if (n === correct) o.classList.add("correct");
      else if (n === picked) o.classList.add("wrong");
    });

    const right = picked === correct;
    Q.firstSeen = Q.firstSeen || new Set();
    const firstTime = item.firstTry;

    // Xato savollarni kuzatish (faqat birinchi urinish, mashq rejimida emas)
    if (!right && firstTime && Q.mode !== "wrong-practice") {
      Q.wrongItems = Q.wrongItems || [];
      if (!Q.wrongItems.find(w => w.q.id === q.id)) {
        Q.wrongItems.push(Object.assign({}, item, { firstTry: true }));
      }
    }

    if (right) {
      if (firstTime) {
        Q.firstCorrect++; Q.firstSeen.add(q.id);
        // Exam mode: sektsiya ballini kuzat
        if (Q.mode === "random") {
          const bs = (EXAM_PROB[item.type] || {}).bigSec || "?";
          Q.secCorrect[bs] = (Q.secCorrect[bs] || 0) + 1;
        }
      }
      Q.combo++; Q.maxCombo = Math.max(Q.maxCombo, Q.combo);
      const gain = (firstTime ? 10 : 4) + Math.min(Q.combo - 1, 5) * 2;
      S.xp += gain; save();
      if (Q.combo >= 3 && Q.mode !== "random") flashCombo("🔥 " + Q.combo + " ketma-ket! +" + gain + " XP");
      if (Q.mode === "review") srsRight(q.id, true);
      else if (S.srs[q.id]) srsRight(q.id, false);
    } else {
      Q.combo = 0;
      if (firstTime) {
        if (Q.hearts < 99) Q.hearts = Math.max(0, Q.hearts - 1);
        Q.firstSeen.add(q.id);
      }
      srsWrong(q.id);
      // Exam modeda xato savol qaytib kelmaydi — haqiqiy imtihon kabi
      if (Q.mode !== "random") {
        // Xato savol qaytganda _shuffledAnswer ni tozalaymiz — qayta shuffle bo'lsin
        const again = Object.assign({}, item, { firstTry: false, _shuffledAnswer: undefined });
        const pos = Math.min(Q.queue.length, Q.idx + 4 + Math.floor(Math.random() * 3));
        Q.queue.splice(pos, 0, again);
      }
    }
    Q.answered++;
    drawHearts();
    showFeedback(right, item, q);
  }

  function showFeedback(right, item, q) {
    const fb = $("#feedback");
    fb.classList.add("show", right ? "ok" : "bad");
    $("#fb-head").textContent = right ? pickPraise() : "Xato — yana ko'rasiz 🔁";
    let expl = "";
    if (item.type === "sentence_order" && q.order) {
      const full = (q.prefix || "") + q.order.map(n => q.options[n - 1]).join("") + (q.suffix || "");
      expl = "✅ " + full + (q.explanation_uz ? "<br>" + esc(q.explanation_uz) : "");
    } else {
      // To'g'ri javob matnini ko'rsatamiz (original q.answer pozitsiyasi bilan)
      const ans = q.options ? q.options[q.answer - 1] : "";
      expl = (right ? "" : `To'g'ri javob: <b>${esc(ans)}</b><br>`) + (q.explanation_uz ? esc(q.explanation_uz) : (q.reading ? esc(q.reading) : ""));
    }
    $("#fb-expl").innerHTML = expl;
    $("#btn-next").textContent = (Q.idx + 1 >= Q.queue.length) ? "Yakunlash 🏁" : "Davom →";
  }
  function pickPraise() { const a = ["To'g'ri! 🎯", "Zo'r! ✨", "Barakalla! 👏", "A'lo! 🌟", "Aniq! ✅"]; return a[Math.floor(Math.random() * a.length)]; }

  function gotoNext() { Q.idx++; nextQuestion(); }

  /* ---------- yakun ---------- */
  function finishLevel() {
    clearInterval(Q._timer);
    const acc = Q.total ? Math.round(Q.firstCorrect / Q.total * 100) : 0;
    const stars = acc >= 90 ? 3 : acc >= 70 ? 2 : 1;
    const secs = Math.round((Date.now() - Q.startedAt) / 1000);
    const bonus = 50 + stars * 30 + Q.maxCombo * 3;
    S.xp += bonus; save();

    show("screen-result");
    const isWP = Q.mode === "wrong-practice";
    $("#res-emoji").textContent = isWP ? (acc === 100 ? "🏆" : "🧠") : stars === 3 ? "🏆" : stars === 2 ? "🎉" : "💪";
    $("#res-title").textContent = Q.mode === "review" ? "Takrorlash tugadi!" : isWP ? "Xato mashqi tugadi!" : Q.title + " tugadi!";
    $("#res-stars").innerHTML = isWP ? "" : [1, 2, 3].map(i => `<span class="s${i <= stars ? " on" : ""}">★</span>`).join("");
    $("#res-acc").textContent = acc + "%";
    $("#res-xp").textContent = "+" + bonus;
    $("#res-time").textContent = Math.floor(secs / 60) + ":" + String(secs % 60).padStart(2, "0");

    const unlockBox = $("#res-unlock"), nextBtn = $("#btn-nextlevel");
    if (Q.mode === "level") {
      const prev = S.stars[Q.levelId] || 0;
      if (stars > prev) S.stars[Q.levelId] = stars;
      const nextId = Q.levelId + 1;
      save();
      if (nextId <= META.levelsCount && isReady(nextId)) { unlockBox.textContent = "➡️ " + nextId + "-bosqichga o'tishingiz mumkin!"; nextBtn.style.display = ""; nextBtn.onclick = () => startLevel(nextId); }
      else if (nextId > META.levelsCount) { unlockBox.textContent = "🎌 Barcha bosqichlar tugadi!"; nextBtn.style.display = "none"; }
      else { unlockBox.textContent = nextId + "-bosqich tez kunda tayyor bo'ladi"; nextBtn.style.display = "none"; }
    } else if (Q.mode === "random") {
      // Exam: sektsiya breakdown ko'rsat
      const secC = Q.secCorrect || {}, secT = Q.secTotals || {};
      const mojiC = secC["文字・語彙"] || 0, mojiT = secT["文字・語彙"] || 35;
      const gramC = secC["文法"] || 0,      gramT = secT["文法"] || 23;
      unlockBox.innerHTML =
        `<div class="exam-breakdown">` +
        `<div class="eb-row"><span class="eb-label">文字・語彙</span><span class="eb-val">${mojiC} / ${mojiT} <small>(${Math.round(mojiC/mojiT*100)}%)</small></span></div>` +
        `<div class="eb-row"><span class="eb-label">文法</span><span class="eb-val">${gramC} / ${gramT} <small>(${Math.round(gramC/gramT*100)}%)</small></span></div>` +
        `</div>`;
      nextBtn.style.display = ""; nextBtn.textContent = "🎲 Yangi random →";
      nextBtn.onclick = () => startRandomMock();
    } else if (isWP) {
      unlockBox.textContent = acc === 100 ? "🎉 Barchasini to'g'ri qildingiz!" : "💪 Yana mashq qiling!";
      nextBtn.style.display = "none";
    } else {
      unlockBox.textContent = "Yaxshi ish! 🔁"; nextBtn.style.display = "none";
    }
    if (stars >= 2 || (isWP && acc === 100)) confetti();

    // ❌ Xato savollar paneli (mashq rejimida ko'rsatmaymiz)
    lastWrongItems = Q.wrongItems || [];
    renderWrongPanel(isWP ? [] : lastWrongItems);
  }

  /* ---------- xato savollar paneli ---------- */
  function renderWrongPanel(wrongs) {
    const panel = $("#res-wrong-panel");
    const list = $("#res-wrong-list");
    const count = $("#res-wrong-count");
    const btn = $("#btn-wrong-practice");
    panel.style.display = "";

    if (!wrongs.length) {
      count.textContent = "✅ Barcha savollar to'g'ri!";
      count.style.color = "var(--ok)";
      btn.style.display = "none";
      list.innerHTML = "";
      return;
    }

    count.textContent = "❌ " + wrongs.length + " ta xato savol";
    count.style.color = "var(--bad)";
    btn.style.display = "";
    list.innerHTML = "";

    wrongs.forEach(function(wItem) {
      const q = wItem.q, type = wItem.type;
      const correctOpt = q.options ? q.options[q.answer - 1] : "";

      let stemHtml = "";
      if (type === "sentence_order") {
        stemHtml = (q.prefix || "") + " __ " + (q.suffix || "");
      } else if (type === "text_grammar") {
        stemHtml = "Blank №" + q.blankNo;
      } else if (type === "usage") {
        stemHtml = q.stem || "";
      } else {
        stemHtml = (q.stem || "").replace(/【([^】]*)】/, "[$1]").replace(/（[\s　]*）/, "(____)");
      }

      const entry = el("div", "wrong-entry");
      entry.innerHTML =
        `<div class="wrong-type-tag">${esc(TYPE_UZ[type] || type)}</div>` +
        `<div class="wrong-stem">${esc(stemHtml)}</div>` +
        `<div class="wrong-correct">✅ To'g'ri: <b>${q.answer}. ${esc(correctOpt)}</b></div>` +
        (q.explanation_uz ? `<div class="wrong-expl">${esc(q.explanation_uz)}</div>` : "");
      list.appendChild(entry);
    });
  }

  /* ---------- xato mashqi ---------- */
  function startWrongPractice() {
    if (!lastWrongItems.length) { toast("Xato yo'q — zo'r! ✨"); return; }
    touchStreak();
    const queue = lastWrongItems.map(it => Object.assign({}, it, { firstTry: true }));
    for (let i = queue.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [queue[i], queue[j]] = [queue[j], queue[i]];
    }
    Q = {
      mode: "wrong-practice", title: "Xato mashqi", jp: "間違い練習",
      queue, idx: 0, total: queue.length,
      firstCorrect: 0, hearts: 99, // cheksiz
      combo: 0, maxCombo: 0,
      startedAt: Date.now(), timeLeft: 0, answered: 0
    };
    show("screen-quiz");
    $("#quiz-timer").style.display = "none";
    nextQuestion();
  }

  /* ---------- combo flash ---------- */
  function flashCombo(txt) { const c = $("#combo-flash"); c.textContent = txt; c.classList.remove("show"); void c.offsetWidth; c.classList.add("show"); }

  /* ===================== CONFETTI ===================== */
  const cv = $("#fx-canvas"), cx = cv.getContext("2d"); let parts = [], raf = null;
  function resize() { cv.width = innerWidth; cv.height = innerHeight; }
  addEventListener("resize", resize); resize();
  function confetti() {
    const colors = ["#7c5cff", "#5ad1ff", "#ff7ac2", "#ffce4d", "#2bd47a"];
    for (let i = 0; i < 140; i++) parts.push({ x: innerWidth / 2, y: innerHeight / 3, vx: (Math.random() - .5) * 14, vy: Math.random() * -14 - 4, g: .4 + Math.random() * .3, s: 5 + Math.random() * 7, c: colors[i % colors.length], r: Math.random() * 6, vr: (Math.random() - .5) * .4, life: 90 + Math.random() * 40 });
    if (!raf) tick();
  }
  function tick() {
    cx.clearRect(0, 0, cv.width, cv.height); let alive = false;
    parts.forEach(p => { if (p.life <= 0) return; alive = true; p.life--; p.vy += p.g; p.x += p.vx; p.y += p.vy; p.r += p.vr; cx.save(); cx.translate(p.x, p.y); cx.rotate(p.r); cx.fillStyle = p.c; cx.fillRect(-p.s / 2, -p.s / 2, p.s, p.s * .6); cx.restore(); });
    parts = parts.filter(p => p.life > 0);
    if (alive) raf = requestAnimationFrame(tick); else { raf = null; cx.clearRect(0, 0, cv.width, cv.height); }
  }

  /* ===================== CUSTOM QUIZ BUILDER ===================== */
  let _cqbState = {}; // { levelId: Set<type> }

  function showCustomBuilder() {
    _cqbState = {};
    const overlay = $("#cqb-overlay");
    const levelsWrap = $("#cqb-levels");
    levelsWrap.innerHTML = "";

    const LSO_TYPES_LIST = [
      { type:"kanji_reading",  no:"問題1", name:"漢字読み",    sec:"vocab",   emoji:"📖" },
      { type:"orthography",    no:"問題2", name:"表記",        sec:"vocab",   emoji:"✏️" },
      { type:"context",        no:"問題3", name:"文脈規定",    sec:"vocab",   emoji:"💬" },
      { type:"paraphrase",     no:"問題4", name:"言い換え類義", sec:"vocab",  emoji:"🔄" },
      { type:"usage",          no:"問題5", name:"用法",        sec:"vocab",   emoji:"🎯" },
      { type:"grammar_form",   no:"問題1", name:"文法形式",    sec:"grammar", emoji:"📝" },
      { type:"sentence_order", no:"問題2", name:"文組み立て",  sec:"grammar", emoji:"🔀" },
      { type:"text_grammar",   no:"問題3", name:"文章の文法",  sec:"grammar", emoji:"📄" }
    ];

    META.levels.forEach(lv => {
      if (!isReady(lv.id)) return;
      _cqbState[lv.id] = new Set();

      const card = el("div", "cqb-lv-card");
      const hdr = el("div", "cqb-lv-hdr");
      const chk = el("input");
      chk.type = "checkbox"; chk.className = "cqb-lv-chk"; chk.id = "cqb-lv-" + lv.id;
      const lbl = el("label", "cqb-lv-label");
      lbl.htmlFor = chk.id;
      lbl.innerHTML = `<span class="cqb-lv-no">${lv.id}</span><span>${esc(lv.title_uz)}</span>`;

      const allBtn = el("button", "cqb-all-sec-btn", "Hammasi");
      allBtn.type = "button";

      hdr.appendChild(chk); hdr.appendChild(lbl); hdr.appendChild(allBtn);
      card.appendChild(hdr);

      const chips = el("div", "cqb-chips");
      chips.style.display = "none";

      LSO_TYPES_LIST.forEach(opt => {
        const chip = el("button", "cqb-chip cqb-chip-" + opt.sec);
        chip.type = "button";
        chip.dataset.type = opt.type;
        chip.innerHTML = `<span class="cqb-chip-no">${esc(opt.no)}</span><span>${esc(opt.emoji)} ${esc(opt.name)}</span>`;
        chip.addEventListener("click", () => {
          chip.classList.toggle("on");
          if (chip.classList.contains("on")) _cqbState[lv.id].add(opt.type);
          else _cqbState[lv.id].delete(opt.type);
          updateCqbCount();
        });
        chips.appendChild(chip);
      });

      chk.addEventListener("change", () => {
        chips.style.display = chk.checked ? "" : "none";
        if (!chk.checked) {
          _cqbState[lv.id].clear();
          chips.querySelectorAll(".cqb-chip").forEach(c => c.classList.remove("on"));
        }
        updateCqbCount();
      });

      allBtn.addEventListener("click", () => {
        chk.checked = true;
        chips.style.display = "";
        _cqbState[lv.id].clear();
        chips.querySelectorAll(".cqb-chip").forEach(c => { c.classList.add("on"); _cqbState[lv.id].add(c.dataset.type); });
        updateCqbCount();
      });

      card.appendChild(chips);
      levelsWrap.appendChild(card);
    });

    updateCqbCount();
    overlay.classList.add("show");
  }

  function updateCqbCount() {
    let total = 0;
    const COUNTS = { kanji_reading:8, orthography:6, context:11, paraphrase:5, usage:5, grammar_form:13, sentence_order:5, text_grammar:5 };
    Object.keys(_cqbState).forEach(lid => {
      _cqbState[lid].forEach(t => { total += COUNTS[t] || 0; });
    });
    const btn = $("#cqb-start-btn");
    if (btn) btn.textContent = total > 0 ? `▶ Boshlash — ${total} savol` : "▶ Boshlash";
    btn.disabled = total === 0;
  }

  function closeCustomBuilder() { $("#cqb-overlay").classList.remove("show"); }

  function startCustomQuiz() {
    const items = [];
    touchStreak();
    Object.keys(_cqbState).forEach(lid => {
      const types = _cqbState[lid];
      if (!types.size) return;
      const t = getTest(+lid); if (!t) return;
      t.sections.forEach(sec => sec.problems.forEach(pr => pr.questions.forEach(q => {
        if (!types.has(pr.type)) return;
        items.push({ q, type: pr.type, instr_jp: pr.instruction_jp, instr_uz: pr.instruction_uz,
          sec: sec.name_jp, problem: pr, firstTry: true });
      })));
    });
    if (!items.length) { toast("Hech bo'lim tanlanmadi!"); return; }
    // Shuffle
    for (let i = items.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [items[i], items[j]] = [items[j], items[i]];
    }
    closeCustomBuilder();
    Q = {
      mode: "custom", title: "Maxsus test", jp: "カスタム",
      queue: items, idx: 0, total: items.length,
      firstCorrect: 0, hearts: 99, combo: 0, maxCombo: 0,
      startedAt: Date.now(), timeLeft: Math.ceil(items.length / 58 * 50 * 60), answered: 0
    };
    show("screen-quiz");
    startTimer();
    nextQuestion();
  }

  /* ===================== EVENTLAR ===================== */
  $("#btn-check").addEventListener("click", checkAnswer);
  $("#btn-next").addEventListener("click", gotoNext);
  function leaveExamMode() { $("#screen-quiz").classList.remove("exam-mode"); }
  $("#btn-quit").addEventListener("click", () => { if (Q && Q._timer) clearInterval(Q._timer); leaveExamMode(); show("screen-home"); renderHome(); });
  $("#btn-custom-quiz") && $("#btn-custom-quiz").addEventListener("click", showCustomBuilder);
  $("#cqb-close") && $("#cqb-close").addEventListener("click", closeCustomBuilder);
  $("#cqb-backdrop") && $("#cqb-backdrop").addEventListener("click", closeCustomBuilder);
  $("#cqb-start-btn") && $("#cqb-start-btn").addEventListener("click", startCustomQuiz);
  $("#btn-home").addEventListener("click", () => { leaveExamMode(); show("screen-home"); renderHome(); });
  $("#btn-retry").addEventListener("click", () => {
    if (Q.mode === "review") startReview();
    else if (Q.mode === "wrong-practice") startWrongPractice();
    else if (Q.mode === "random") startRandomMock();
    else if (Q.mode === "custom") showCustomBuilder();
    else if (Q.filterType === "vocab" || Q.filterType === "grammar") startLevelSection(Q.levelId, Q.filterType);
    else if (Q.filterType) startLevelByType(Q.levelId, Q.filterType);
    else startLevel(Q.levelId);
  });
  $("#btn-review").addEventListener("click", startReview);
  $("#btn-random-mock").addEventListener("click", startRandomMock);
  $("#btn-lso-all").addEventListener("click", () => { if (_lsoLevelId) startLevel(_lsoLevelId); });
  $("#btn-lso-close").addEventListener("click", closeLevelOptions);
  $("#lso-backdrop").addEventListener("click", closeLevelOptions);
  $("#btn-wrong-practice").addEventListener("click", startWrongPractice);
  $("#btn-furigana").addEventListener("click", function () {
    if (!(window.Furigana && Furigana.available())) {
      furiOn = false; this.classList.remove("on");
      toast("Furigana hozircha mavjud emas (internet talab qilinadi)");
      Furigana && Furigana.onReady(ok => { if (ok) toast("Furigana tayyor — tugmani yana bosing 🈷️"); });
      return;
    }
    furiOn = !furiOn; this.classList.toggle("on", furiOn);
    if (Q) { const item = Q.queue[Q.idx]; renderByType(item, item.q); /* tanlovni tiklamaymiz */ $("#btn-check").disabled = true; picked = null; }
  });

  /* ===================== KANJI CARDS ENGINE ===================== */
  let KC = null; // joriy kanji sessiya

  // Kanji ma'lumotini savoldan ajratib olamiz
  function extractKanjiCard(q, levelId) {
    const m = String(q.stem).match(/【([^】]+)】/);
    const kanji = m ? m[1] : q.stem;
    return {
      id: q.id,
      kanji,
      reading: q.reading || "",
      meaning: q.explanation_uz || "",
      sentence: q.tr || "",
      stem: q.stem,
      levelId
    };
  }

  // Dars selector UI
  function showKanjiSelector() {
    const overlay = $("#kc-selector");
    const wrap = $("#kc-sel-levels");
    wrap.innerHTML = "";
    const sel = new Set();

    META.levels.forEach(lv => {
      if (!isReady(lv.id)) return;
      // Bu darsdagi kanji_reading savollar soni
      const t = getTest(lv.id);
      let cnt = 0;
      t.sections.forEach(sec => sec.problems.forEach(pr => {
        if (pr.type === "kanji_reading") cnt += pr.questions.length;
      }));
      if (!cnt) return;

      const card = el("div", "cqb-lv-card");
      const hdr = el("div", "cqb-lv-hdr");
      const chk = el("input");
      chk.type = "checkbox"; chk.className = "cqb-lv-chk"; chk.id = "kc-lv-" + lv.id;
      const lbl = el("label", "cqb-lv-label");
      lbl.htmlFor = chk.id;
      lbl.innerHTML = `<span class="cqb-lv-no">${lv.id}</span><span>${esc(lv.title_uz)}</span><small style="color:var(--muted);margin-left:auto">${cnt} kanji</small>`;
      hdr.appendChild(chk); hdr.appendChild(lbl);
      card.appendChild(hdr);

      chk.addEventListener("change", () => {
        if (chk.checked) sel.add(lv.id); else sel.delete(lv.id);
        const btn = $("#kc-sel-start");
        btn.disabled = sel.size === 0;
        btn.textContent = sel.size > 0 ? `⚡ Boshlash` : "⚡ Boshlash";
      });

      wrap.appendChild(card);
    });

    overlay.classList.add("show");

    $("#kc-sel-start").onclick = () => {
      if (!sel.size) return;
      overlay.classList.remove("show");
      startKanjiCards([...sel]);
    };
  }

  function closeKanjiSelector() { $("#kc-selector").classList.remove("show"); }

  // Kanji Cards boshlash
  function startKanjiCards(levelIds) {
    const cards = [];
    levelIds.forEach(lid => {
      const t = getTest(lid); if (!t) return;
      t.sections.forEach(sec => sec.problems.forEach(pr => {
        if (pr.type !== "kanji_reading") return;
        pr.questions.forEach(q => cards.push(extractKanjiCard(q, lid)));
      }));
    });
    // Shuffle
    for (let i = cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cards[i], cards[j]] = [cards[j], cards[i]];
    }
    KC = {
      all: cards,
      deck: cards.slice(), // joriy round kartalar
      known: [],
      unknown: [],
      idx: 0,
      round: 1,
      flipped: false,
      total: cards.length,
      levelIds
    };
    const labels = levelIds.map(id => {
      const lv = META.levels.find(l => l.id === id);
      return lv ? lv.id + "-dars" : id;
    }).join(", ");
    $("#kc-title").textContent = "Kanji Cards";
    $("#kc-subtitle").textContent = labels;
    show("screen-kanji");
    kcRender();
  }

  function kcRender() {
    if (!KC) return;
    // Progress
    const done = KC.idx;
    const total = KC.deck.length;
    const pct = total ? (done / total * 100) : 0;
    $("#kc-prog-fill").style.width = pct + "%";
    $("#kc-prog-label").textContent = done + " / " + total + (KC.round > 1 ? "  (Tur " + KC.round + ")" : "");
    $("#kc-known-count").textContent = "✓ " + KC.known.length;
    $("#kc-unknown-count").textContent = "✕ " + KC.unknown.length;

    if (KC.idx >= KC.deck.length) {
      kcEndRound();
      return;
    }

    const card = KC.deck[KC.idx];
    KC.flipped = false;

    // Reset card. The transition is disabled while removing "flipped" so the
    // next card cannot briefly appear with the previous card's back side.
    const cardEl = $("#kc-card");
    cardEl.style.transition = "none";
    cardEl.classList.remove("flipped", "fly-right", "fly-left");
    void cardEl.offsetWidth; // force reflow before restoring the transition
    cardEl.style.transition = "";

    $("#kc-kanji").textContent = card.kanji;
    $("#kc-back-reading").textContent = card.reading;
    $("#kc-back-meaning").textContent = card.meaning;
    $("#kc-back-sentence").textContent = card.sentence ? "「" + card.sentence + "」" : "";

    // Hint visibility — faqat flipdan keyin ko'rish uchun
    $("#kc-hint-left").style.opacity = "0";
    $("#kc-hint-right").style.opacity = "0";
  }

  function kcFlip() {
    if (!KC) return;
    const cardEl = $("#kc-card");
    KC.flipped = !KC.flipped;
    cardEl.classList.toggle("flipped", KC.flipped);
    if (KC.flipped) {
      $("#kc-hint-left").style.opacity = "1";
      $("#kc-hint-right").style.opacity = "1";
    } else {
      $("#kc-hint-left").style.opacity = "0";
      $("#kc-hint-right").style.opacity = "0";
    }
  }

  function kcAnswer(known) {
    if (!KC || KC.idx >= KC.deck.length) return;
    const card = KC.deck[KC.idx];
    const cardEl = $("#kc-card");
    const wrapEl = $("#kc-card-wrap");

    // Animatsiya
    wrapEl.classList.add(known ? "fly-right" : "fly-left");
    if (known) KC.known.push(card);
    else KC.unknown.push(card);
    KC.idx++;

    setTimeout(() => {
      wrapEl.classList.remove("fly-right", "fly-left");
      kcRender();
    }, 380);
  }

  function kcEndRound() {
    if (!KC.unknown.length) {
      // Hammasi bilindi!
      kcShowResult();
      return;
    }
    // Bilmaganlar qaytadi
    KC.round++;
    // Shuffle unknowns
    const unk = KC.unknown.slice();
    for (let i = unk.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [unk[i], unk[j]] = [unk[j], unk[i]];
    }
    KC.deck = unk;
    KC.unknown = [];
    KC.idx = 0;
    // Flash xabar
    toast("🔁 Tur " + KC.round + " — " + KC.deck.length + " ta bilmaganlar qaytdi");
    setTimeout(kcRender, 600);
  }

  function kcShowResult() {
    const overlay = $("#kc-result-overlay");
    const perfect = KC.known.length === KC.total;
    $("#kc-res-emoji").textContent = perfect ? "🏆" : KC.known.length > KC.total * 0.8 ? "🎉" : "💪";
    $("#kc-res-title").textContent = perfect ? "Mukammal! Barchasini bildingiz!" : "Yaxshi natija!";
    $("#kc-res-known").textContent = KC.known.length;
    $("#kc-res-total").textContent = KC.total;
    $("#kc-res-rounds").textContent = KC.round;
    overlay.classList.add("show");
    if (perfect) confetti();

    $("#kc-res-retry").onclick = () => {
      overlay.classList.remove("show");
      startKanjiCards(KC.levelIds);
    };
    $("#kc-res-home").onclick = () => {
      overlay.classList.remove("show");
      show("screen-home");
      renderHome();
    };
  }

  // Kanji Cards touch/mouse swipe
  (function setupKcSwipe() {
    let startX = 0, startY = 0, dragging = false;
    const arena = document.getElementById("kc-arena");

    function onStart(x, y) {
      if (!KC || KC.idx >= KC.deck.length) return;
      startX = x; startY = y; dragging = true;
    }
    function onMove(x) {
      if (!dragging || !KC) return;
      const dx = x - startX;
      const card = document.getElementById("kc-card-wrap");
      card.style.transform = `translateX(${dx}px) rotate(${dx * 0.04}deg)`;
      // Hint opacity
      const pct = Math.min(Math.abs(dx) / 80, 1);
      if (dx > 0) {
        $("#kc-hint-right").style.opacity = KC.flipped ? pct : 0;
        $("#kc-hint-left").style.opacity = 0;
      } else {
        $("#kc-hint-left").style.opacity = KC.flipped ? pct : 0;
        $("#kc-hint-right").style.opacity = 0;
      }
    }
    function onEnd(x) {
      if (!dragging || !KC) return;
      dragging = false;
      const dx = x - startX;
      const card = document.getElementById("kc-card-wrap");
      card.style.transform = "";
      if (Math.abs(dx) > 80 && KC.flipped) {
        kcAnswer(dx > 0);
      }
    }

    arena.addEventListener("touchstart", e => onStart(e.touches[0].clientX, e.touches[0].clientY), { passive: true });
    arena.addEventListener("touchmove", e => onMove(e.touches[0].clientX), { passive: true });
    arena.addEventListener("touchend", e => onEnd(e.changedTouches[0].clientX));

    arena.addEventListener("mousedown", e => { if (e.target.closest(".kc-card-wrap")) onStart(e.clientX, e.clientY); });
    document.addEventListener("mousemove", e => { if (dragging) onMove(e.clientX); });
    document.addEventListener("mouseup", e => onEnd(e.clientX));
  })();

  // Kanji Cards event listeners
  $("#btn-kanji-cards").addEventListener("click", showKanjiSelector);
  $("#kc-sel-close").addEventListener("click", closeKanjiSelector);
  $("#kc-sel-backdrop").addEventListener("click", closeKanjiSelector);
  $("#kc-btn-back").addEventListener("click", () => { show("screen-home"); renderHome(); });
  $("#kc-btn-flip").addEventListener("click", kcFlip);
  $("#kc-card").addEventListener("click", kcFlip);
  $("#kc-btn-yes").addEventListener("click", () => {
    if (!KC.flipped) { kcFlip(); return; }
    kcAnswer(true);
  });
  $("#kc-btn-no").addEventListener("click", () => {
    if (!KC.flipped) { kcFlip(); return; }
    kcAnswer(false);
  });

  /* ===================== ISHGA TUSHIRISH ===================== */
  buildIndex();
  renderHome();
  show("screen-home");


  /* debug (faqat ?debug bilan) */
  if (location.search.indexOf("debug") >= 0) {
    window.__dbg = {
      start: startLevel,
      jumpType(t) { if (!Q) startLevel(1); const i = Q.queue.findIndex(x => x.type === t); if (i >= 0) { Q.idx = i; nextQuestion(); } return i; },
      finish(acc, wrongCount) {
        if (!Q) startLevel(1);
        Q.total = 58; Q.firstCorrect = Math.round(58 * (acc != null ? acc : 95) / 100);
        // Test uchun xato savollar inject
        if (wrongCount && wrongCount > 0) {
          const t = getTest(Q.levelId || 1);
          Q.wrongItems = [];
          let added = 0;
          t.sections.forEach(sec => sec.problems.forEach(pr => pr.questions.forEach(qItem => {
            if (added >= wrongCount) return;
            Q.wrongItems.push({ q: qItem, type: pr.type, instr_jp: pr.instruction_jp,
              instr_uz: pr.instruction_uz, sec: sec.name_jp, problem: pr, firstTry: true });
            added++;
          })));
        }
        finishLevel();
      },
      wrongPractice: startWrongPractice,
      Q: () => Q,
      getWrongs: () => lastWrongItems
    };
  }
})();
