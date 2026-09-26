/* Furigana — kanji ustiga o'qilish qo'shadi. kuromoji bo'lmasa, sokin ishlamaydi. */
(function () {
  const Fz = {
    _tok: null, _init: false, _ok: false, _waiters: [],
    available() { return this._ok; },
    onReady(cb) { this._ok ? cb(true) : (this._done ? cb(false) : this._waiters.push(cb)); },
    init() {
      if (this._init) return; this._init = true;
      if (typeof kuromoji === "undefined") { this._finish(false); return; }
      try {
        kuromoji.builder({ dicPath: "dict/" })
          .build((err, tok) => {
            if (err) { this._finish(false); return; }
            this._tok = tok; this._finish(true);
          });
      } catch (e) { this._finish(false); }
    },
    _finish(ok) { this._ok = ok; this._done = true; this._waiters.forEach(f => f(ok)); this._waiters = []; },

    kata2hira(s) { return (s || "").replace(/[ァ-ヶ]/g, c => String.fromCharCode(c.charCodeAt(0) - 0x60)); },
    hasKanji(s) { return /[一-龯々]/.test(s); },

    // Matnni <ruby> li HTML ga aylantiradi. skip = furigana qo'yilmaydigan so'z (masalan kanji_reading nishoni)
    toRuby(text, skip) {
      if (!this._ok || !this._tok || !text) return escapeHtml(text);
      let out = "";
      const tokens = this._tok.tokenize(text);
      for (const t of tokens) {
        const sf = t.surface_form;
        const reading = this.kata2hira(t.reading && t.reading !== "*" ? t.reading : "");
        if (!this.hasKanji(sf) || !reading || (skip && sf === skip)) { out += escapeHtml(sf); continue; }
        // okurigana: oxiridagi umumiy kana'ni ajratamiz
        let head = sf, tail = "", rd = reading;
        const m = sf.match(/([぀-ゟ゠-ヿ]+)$/);
        if (m) {
          tail = m[1];
          const rdh = this.kata2hira(reading);
          if (rdh.endsWith(this.kata2hira(tail))) { head = sf.slice(0, -tail.length); rd = rdh.slice(0, -tail.length); }
          else { tail = ""; }
        }
        if (head) out += "<ruby>" + escapeHtml(head) + "<rt>" + escapeHtml(rd) + "</rt></ruby>" + escapeHtml(tail);
        else out += escapeHtml(sf);
      }
      return out;
    }
  };
  function escapeHtml(s) { return (s || "").replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c])); }
  Fz.escapeHtml = escapeHtml;
  window.Furigana = Fz;
})();
