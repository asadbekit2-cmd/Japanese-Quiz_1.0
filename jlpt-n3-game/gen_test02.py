# -*- coding: utf-8 -*-
"""test02.json generatori — 第2回 模擬テスト (manba PDF betlari p018-027, javob p195)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test02.json")

def q(qid, stem, options, answer, tr, reading=None, expl=None, optsTr=None,
      prefix=None, suffix=None, starPos=None, order=None, blankNo=None):
    d = {"id": qid, "stem": stem, "options": options, "answer": answer, "tr": tr}
    if reading: d["reading"] = reading
    if expl: d["explanation_uz"] = expl
    if optsTr: d["optsTr"] = optsTr
    if prefix is not None: d["prefix"] = prefix
    if suffix is not None: d["suffix"] = suffix
    if starPos is not None: d["starPos"] = starPos
    if order is not None: d["order"] = order
    if blankNo is not None: d["blankNo"] = blankNo
    # sentence_order/text_grammar uchun stem shart emas
    if stem is None: del d["stem"]
    return d

data = {
  "id": 2,
  "title_jp": "第2回 模擬テスト",
  "title_uz": "2-test",
  "minutes": 50,
  "sections": [
    {
      "id": "vocab",
      "name_jp": "文字・語彙",
      "name_uz": "Kanji va lug'at",
      "problems": [
        {
          "id": "v1", "type": "kanji_reading",
          "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
          "questions": [
            q("t2-v1-1", "家の前に、きれいな花が【咲いて】います。", ["まいて","おいて","ついて","さいて"], 4,
              "Uy oldida chiroyli gul ochilib turibdi.", reading="さいて", expl="咲く → さく (ochilmoq, gullamoq)"),
            q("t2-v1-2", "父は、【普通】の会社員です。", ["ふつう","ふうつう","ふづう","ふうづう"], 1,
              "Otam oddiy kompaniya xodimi.", reading="ふつう", expl="普通 → ふつう (oddiy)"),
            q("t2-v1-3", "【借金】して車を買った。", ["かりきん","かしきん","しゃっきん","しゃくきん"], 3,
              "Qarz olib mashina sotib oldim.", reading="しゃっきん", expl="借金 → しゃっきん (qarz)"),
            q("t2-v1-4", "部屋に何人か【残って】いる。", ["あまって","かえって","そろって","のこって"], 4,
              "Xonada bir necha kishi qolyapti.", reading="のこって", expl="残る → のこる (qolmoq)"),
            q("t2-v1-5", "仕事のことを考えると、【胃】が痛い。", ["おなか","い","ちょう","はら"], 2,
              "Ish haqida o'ylasam, oshqozonim og'riydi.", reading="い", expl="胃 → い (oshqozon)"),
            q("t2-v1-6", "アルバイトで遅くなり、午前1時に【帰宅】しました。", ["きてく","きでく","きたく","きだく"], 3,
              "Ish (albatta) tufayli kechikib, tungi soat 1 da uyga qaytdim.", reading="きたく", expl="帰宅 → きたく (uyga qaytish)"),
            q("t2-v1-7", "私は、【乱暴】な人はきらいです。", ["ぼうりょく","おうぼう","らんぼう","らんざつ"], 3,
              "Men qo'pol odamlarni yoqtirmayman.", reading="らんぼう", expl="乱暴 → らんぼう (qo'pol, dag'al)"),
            q("t2-v1-8", "有名な俳優がステージに【登場】した。", ["とじょう","とうじょう","とじょ","とうじょ"], 2,
              "Mashhur aktyor sahnaga chiqdi.", reading="とうじょう", expl="登場 → とうじょう (sahnaga chiqish, paydo bo'lish)"),
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
          "questions": [
            q("t2-v2-9", "【じゆう】に生きたいと思っている。", ["自由","時由","治由","事由"], 1,
              "Erkin yashashni xohlayman.", expl="じゆう → 自由 (erkinlik)"),
            q("t2-v2-10", "その映画を見て、深く【かんどう】した。", ["感情","感動","感働","感激"], 2,
              "O'sha filmni ko'rib, qattiq ta'sirlandim.", expl="かんどう → 感動 (ta'sirlanish, hayajonlanish)"),
            q("t2-v2-11", "敵から【にげて】、ここまで来た。", ["込げて","退げて","迫げて","逃げて"], 4,
              "Dushmandan qochib, shu yergacha keldim.", expl="にげる → 逃げる (qochmoq)"),
            q("t2-v2-12", "できるだけ早い返事を【もとめる】。", ["許める","求める","元める","基める"], 2,
              "Iloji boricha tezroq javob talab qilaman.", expl="もとめる → 求める (talab qilmoq, izlamoq)"),
            q("t2-v2-13", "地図が【ふくざつ】すぎて、よくわからない。", ["乱雑","混雑","複雑","服雑"], 3,
              "Xarita juda murakkab, yaxshi tushunmayapman.", expl="ふくざつ → 複雑 (murakkab)"),
            q("t2-v2-14", "彼のやり方について、【もんく】を言う。", ["文苦","文口","文句","文言"], 3,
              "Uning uslubiga e'tiroz (norozilik) bildiraman.", expl="もんく → 文句 (e'tiroz, norozilik)"),
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
          "questions": [
            q("t2-v3-15", "駅で、電車が遅れるという（　）があった。", ["インタビュー","アナウンス","コーラス","スピーチ"], 2,
              "Bekatda poyezd kechikishi haqida e'lon (anons) bo'ldi.", expl="アナウンス = e'lon, ovozli xabar"),
            q("t2-v3-16", "買い物するときに、クレジットカードで（　）した。", ["代用","作用","利用","応用"], 3,
              "Xarid qilganda kredit kartadan foydalandim.", expl="利用 = foydalanish"),
            q("t2-v3-17", "仕事をやめて、外国に住むことを（　）した。", ["決意","感覚","感想","意志"], 1,
              "Ishni tashlab, chet elda yashashga qat'iy qaror qildim.", expl="決意 = qat'iy qaror"),
            q("t2-v3-18", "友だちの肩を（　）、名前を呼んだ。", ["曲げて","たたいて","攻めて","守って"], 2,
              "Do'stimning yelkasiga sekin urib, ismini chaqirdim.", expl="たたく = urmoq, taqillatmoq"),
            q("t2-v3-19", "今年も、去年と（　）のイベントが開かれる。", ["同意","同点","同様","同級"], 3,
              "Bu yil ham o'tgan yildagi kabi (xuddi shunday) tadbir o'tkaziladi.", expl="同様 = xuddi shunday, bir xil"),
            q("t2-v3-20", "誕生日にプレゼントを（　）つもりです。", ["つかむ","つまむ","投げる","贈る"], 4,
              "Tug'ilgan kunda sovg'a qilmoqchiman.", expl="贈る = sovg'a qilmoq (taqdim etmoq)"),
            q("t2-v3-21", "家の前で、道が大きく（　）している。", ["アウト","レール","カーブ","ドロップ"], 3,
              "Uy oldida yo'l keskin buriladi.", expl="カーブ = burilish, egrilik"),
            q("t2-v3-22", "きのう、大学入学の（　）が終わりました。", ["手分け","手直し","手回し","手続き"], 4,
              "Kecha universitetga kirish rasmiylashtiruvi tugadi.", expl="手続き = rasmiylashtirish, jarayon"),
            q("t2-v3-23", "おなかがすいたが、何も食べないで（　）した。", ["我慢","通用","飲食","許可"], 1,
              "Qornim ochdi, lekin hech narsa yemay chidadim (sabr qildim).", expl="我慢 = sabr, chidam"),
            q("t2-v3-24", "伊藤「山田さんは、大学の先生なんですって。」清水「へえ、（　）、田中さんも大学に勤めているそうですよ。」",
              ["そうしたら","それとも","そうすれば","そういえば"], 4,
              "Ito: «Yamada-san universitet o'qituvchisi emish.» Shimizu: «Voy, aytgancha, Tanaka-san ham universitetda ishlarmish.»",
              expl="そういえば = aytgancha, shu esimga tushdi"),
            q("t2-v3-25", "国と国との関係が悪くなって、（　）が起こった。", ["競走","和平","戦争","平和"], 3,
              "Davlatlararo munosabat yomonlashib, urush boshlandi.", expl="戦争 = urush"),
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
          "questions": [
            q("t2-v4-26", "この店は、いつも【そうぞうしい】。", ["安い","高い","静かだ","うるさい"], 4,
              "Bu do'kon doim shovqinli.", expl="騒々しい (そうぞうしい) = うるさい (shovqinli)"),
            q("t2-v4-27", "彼はとても【がんこだ】。", ["考えを変える","考えを変えない","気が強い","気が弱い"], 2,
              "U juda o'jar.", expl="頑固 (がんこ) = o'jar (fikrini o'zgartirmaydigan)"),
            q("t2-v4-28", "私は山を【ながめる】ことが好きです。", ["見る","登る","文章にする","絵を描く"], 1,
              "Men tog'ga (uzoq) tikilib qarashni yaxshi ko'raman.", expl="眺める (ながめる) = 見る (tikilib qaramoq)"),
            q("t2-v4-29", "彼は、いつも時間に【だらしない】。", ["時間を守らない","時間通りに行動する","時間を気にしている","時間に正確だ"], 1,
              "U doim vaqtga beparvo (vaqtni saqlamaydi).", expl="だらしない = tartibsiz; vaqtni saqlamaydi"),
            q("t2-v4-30", "このパンは【ふわふわ】している。", ["軽くなっている","古くなっている","やわらかい","かたい"], 3,
              "Bu non yumshoq (g'ovak).", expl="ふわふわ = yumshoq, g'ovak"),
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
          "questions": [
            q("t2-v5-31", "思い出す", [
                "全員で会議をして、新しいアイデアを思い出した。",
                "何度も書き順の練習をして、難しい漢字を思い出した。",
                "長い時間考えて、知り合いの名前をやっと思い出した。",
                "心配なことがあると、いつもカフェで1人、思い出した。"], 3,
              "思い出す = (esga) eslamoq, yodga tushirmoq.",
              optsTr=[
                "Hammamiz yig'ilish qilib, yangi g'oyani 'esladik'.",
                "Ko'p marta yozuv tartibini mashq qilib, qiyin kanjini 'esladim'.",
                "Uzoq o'ylab, tanishimning ismini nihoyat esladim.",
                "Xavotirim bo'lsa, doim kafeda yolg'iz 'eslardim'."]),
            q("t2-v5-32", "こめる", [
                "燃えないごみを、ごみ箱にこめてください。",
                "スカートをこめて、短くしなければなりません。",
                "今日は早めにおふろに水をこめてください。",
                "手紙に、気持ちをこめて書きなさい。"], 4,
              "こめる (込める) = (his-tuyg'u, kuch) singdirmoq, jamlamoq.",
              optsTr=[
                "Yonmaydigan chiqindini axlat qutisiga 'singdiring' (noto'g'ri).",
                "Yubkani 'singdirib' qisqartirish kerak (noto'g'ri).",
                "Bugun erta vannaga suvni 'singdiring' (noto'g'ri).",
                "Xatga his-tuyg'uni singdirib yozing. (to'g'ri)"]),
            q("t2-v5-33", "ルート", [
                "外国では、その国のルートの通りにしなければならない。",
                "駅から会社まで、いちばん近いルートを教えてください。",
                "彼女の顔にはよいルートが出ていた。",
                "ルートをしたまま、おふろに入らないでください。"], 2,
              "ルート = yo'nalish, marshrut.",
              optsTr=[
                "Chet elda o'sha mamlakatning 'marshruti' bo'yicha qilish kerak (noto'g'ri).",
                "Bekatdan kompaniyagacha eng yaqin yo'lni (marshrutni) ayting. (to'g'ri)",
                "Uning yuzida yaxshi 'marshrut' chiqqan edi (noto'g'ri).",
                "'Marshrut' qilgan holda vannaga kirmang (noto'g'ri)."]),
            q("t2-v5-34", "得意", [
                "やり方を教えてもらって、得意をしました。",
                "私は、子どものころからピアノを得意でした。",
                "彼女の電話番号が得意だったら、教えてください。",
                "私は、そうじより料理のほうが得意です。"], 4,
              "得意 = mohir, ustasi; (biror ishni) yaxshi eplaydigan.",
              optsTr=[
                "Uslubni o'rganib, 'mohirlik' qildim (noto'g'ri).",
                "Men bolaligimdan pianino 'mohir edim' (noto'g'ri).",
                "Uning telefon raqami 'mohir' bo'lsa, ayting (noto'g'ri).",
                "Men tozalashdan ko'ra ovqat pishirishni yaxshiroq eplayman. (to'g'ri)"]),
            q("t2-v5-35", "うらやましい", [
                "スポーツも勉強もできる友人がうらやましい。",
                "悪い人にだまされて、とてもうらやましい。",
                "外国で1人で生活していたら、うらやましくなった。",
                "母の作った料理がうらやましくて、たくさん食べた。"], 1,
              "うらやましい = havasi keladigan, rashk qiladigan.",
              optsTr=[
                "Sport ham, o'qish ham qo'lidan keladigan do'stimga havasim keladi. (to'g'ri)",
                "Yomon odam aldab ketdi, juda 'havasim keladi' (noto'g'ri).",
                "Chet elda yolg'iz yashasam, 'havasim keldi' (noto'g'ri).",
                "Onam pishirgan ovqatga 'havasim kelib', ko'p yedim (noto'g'ri)."]),
          ]
        }
      ]
    },
    {
      "id": "grammar",
      "name_jp": "文法",
      "name_uz": "Grammatika",
      "problems": [
        {
          "id": "g1", "type": "grammar_form",
          "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
          "questions": [
            q("t2-g1-1", "確か先輩が、今日の授業はない（　）言っていました。", ["だと","と","を","に"], 2,
              "Aniq esimda, sempay bugun dars yo'q deб aytgan edi.", expl="〜と言う = deб aytmoq (iqtibos)"),
            q("t2-g1-2", "私が元気でいる（　）家族に伝えてください。", ["を","ものを","ことを","あいだを"], 3,
              "Men sog'-salomat ekanimni oilamga yetkazing.", expl="〜ことを伝える = ...ekanini yetkazmoq"),
            q("t2-g1-3", "走れる（　）、マラソンを続けるつもりだ。", ["までは","限りは","ばかりは","中は"], 2,
              "Yugura olganimcha, marafonni davom ettirmoqchiman.", expl="〜限り(は) = ...gancha, ...gan ekan"),
            q("t2-g1-4", "このまま夜遅くまで働く毎日が続くと、病気になる（　）。", ["おそれがある","気がある","ところがある","ものがある"], 1,
              "Shu zaylda har kuni kechgacha ishlash davom etsa, kasal bo'lib qolish xavfi bor.", expl="〜おそれがある = ...xavfi bor"),
            q("t2-g1-5", "彼は大学で英語を勉強し、（　）自分でフランス語も学習している。", ["むしろ","または","さらに","上に"], 3,
              "U universitetda ingliz tilini o'qigan, bundan tashqari o'zicha fransuz tilini ham o'rganmoqda.", expl="さらに = bundan tashqari, yana"),
            q("t2-g1-6", "ジョギングを始める（　）、体の調子がよくありませんでした。", ["前に","前で","前と","前は"], 4,
              "Yugurishni boshlashdan oldin, sog'lig'im yaxshi emas edi.", expl="〜前は = ...dan oldin (avvalgi holat)"),
            q("t2-g1-7", "寒くならない（　）、家へ帰りましょう。", ["うちで","うちに","うちは","うちまでに"], 2,
              "Sovuq bo'lib qolmasdan (sovimasdan) turib, uyga qaytaylik.", expl="〜ないうちに = ...magunicha, ...masdan turib"),
            q("t2-g1-8", "寒い季節には風邪を（　）ので、気をつけてください。", ["ひき気味","ひきがち","ひききり","ひきかけ"], 2,
              "Sovuq faslda tez-tez shamollab qolasiz, shuning uchun ehtiyot bo'ling.", expl="〜がち = tez-tez ...adigan, moyil"),
            q("t2-g1-9", "学生なのだから、宿題は（　）なりません。", ["しないでは","しなくても","しなくて","しなくては"], 4,
              "Talaba ekansiz, uy vazifasini bajarmasangiz bo'lmaydi.", expl="〜なくてはならない = ...masa bo'lmaydi (shart)"),
            q("t2-g1-10", "店長「明日から、もうバイトに来ないでください。」店員「えっ、（　）ことですか。理由を教えてください。」",
              ["あのくらいの","どのくらいの","ああいう","どういう"], 4,
              "Boshliq: «Ertadan ishga kelmang.» Xodim: «A, bu qanaqasi (nima degani)? Sababini ayting.»",
              expl="どういうことですか = bu nima degani / qanday gap"),
            q("t2-g1-11", "いくらチョコレートが好きでも、一度に（　）体によくないだろう。",
              ["あんなに食べたら","こんなに食べてみて","あれほどに食べたいなら","これくらい食べても"], 1,
              "Shokoladni qancha yaxshi ko'rsang ham, bir vaqtda 'shuncha' yesang, salomatlikka yomon-da.",
              expl="あんなに〜たら = shuncha ...sa (haddan ortiq)"),
            q("t2-g1-12", "加藤「週末、一緒に映画を見に行きませんか。」高田「すみません。仕事がいそがしくて、映画を（　）のです。」",
              ["見に行くことがない","見に行くことではない","見に行くところがない","見に行くどころではない"], 4,
              "Kato: «Dam olishda birga kinoga bormaymizmi?» Takada: «Kechirasiz, ishim band, kino ko'rishga vaqt yo'q (bunaqa holatda emasman).»",
              expl="〜どころではない = ...ga vaqt/hol yo'q"),
            q("t2-g1-13", "姉はある歌手の大ファンで、「彼くらい歌が（　）」と、必ずライブに行く。",
              ["上手な人がいるだろう","上手な人はいない","上手な人もいた","上手な人になりえない"], 2,
              "Opam bir qo'shiqchining katta muxlisi, «undan ko'ra yaxshi kuylaydigan odam yo'q» deб, albatta konsertga boradi.",
              expl="〜くらい〜はいない = ...chalik (yaxshi) yana yo'q"),
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
          "questions": [
            q("t2-g2-14", None, ["じゃありませんか","動いている","ばかり","私"], 3,
              "To'g'ri tartib: «Anchadan beri faqat men ishlayapman-ku!»",
              prefix="小池「さっきから、", suffix="。」", starPos=2, order=[4,3,2,1],
              expl="To'g'ri tartib: 私ばかり動いているじゃありませんか"),
            q("t2-g2-15", None, ["して","ことが","いる","過ごして"], 3,
              "To'g'ri tartib: «Odatda golf o'ynab vaqt o'tkazaman.»",
              prefix="山本「だいたいゴルフを", suffix="多いですね。」", starPos=3, order=[1,4,3,2],
              expl="To'g'ri tartib: ゴルフをして過ごしていることが多い"),
            q("t2-g2-16", None, ["ご予定","いらっしゃる","なのか","何時ごろ"], 1,
              "To'g'ri tartib: «Ertangi yig'ilishga soat nechada kelishingizni aytib bera olasizmi?»",
              prefix="社員「社長、明日の会議に、", suffix="教えていただけますか。」", starPos=3, order=[4,2,1,3],
              expl="To'g'ri tartib: 何時ごろいらっしゃるご予定なのか"),
            q("t2-g2-17", None, ["あって","こと","いろいろな","だけ"], 3,
              "To'g'ri tartib: «Morikava-san olim bo'lgani uchun turli narsani biladi.»",
              prefix="さすが森川さんは、学者", suffix="を知っている。", starPos=3, order=[4,1,3,2],
              expl="To'g'ri tartib: 学者だけあっていろいろなことを (知っている)"),
            q("t2-g2-18", None, ["仕事が","ロボットが","する","かわって"], 2,
              "To'g'ri tartib: «Bir maqolaga ko'ra, kelajakda inson o'rniga robot bajaradigan ishlar ko'payarmish.»",
              prefix="ある論文によると、今後は、人間に", suffix="増えるそうだ。", starPos=2, order=[4,2,3,1],
              expl="To'g'ri tartib: 人間にかわってロボットがする仕事が (増える)"),
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
          "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
          "passage_title": "大人になれば",
          "passage": (
            "子どものころ、自分の親と同じ年齢になれば、立派な大人になれるのだろうと思っていた。"
            "だが、自分が「大人」であると思っていた年齢に{{19}}、成長できていない自分に驚く。\n"
            "たとえば、朝はいつまでも寝ていたいと思うのも、子どものころと同じだ。さらに、仕事が大変なときに、"
            "何度も会社を休みたくなったりする。「熱が出たから」とうそをついて、本当に会社を休んだことも{{20}}。"
            "子どものころは、本当に熱があっても、学校へきちんと通っていたのに。また、にんじんやピーマンなど、"
            "子どものころきらいだった食べ物は、今でも{{21a}}、料理に入っていると{{21b}}。それなのに、"
            "自分の子どもには「好ききらいをせずに、なんでも食べなさい」と言ったりする。\n"
            "{{22}}いばったり、うまくうそがつけるような大人になった今の自分は、子どものころより成長するどころか、"
            "悪くなっているのかもしれない。{{23}}、自分の父や母も、昔は今の自分のように考え、"
            "「大人」になろうとがんばっていたのかと思うと、なんだかあたたかい気持ちになるのだ。"
          ),
          "passage_tr": (
            "Bolaligimda, ota-onam bilan teng yoshga yetsam, yetuk katta odam bo'laman deb o'ylardim. "
            "Ammo o'zim «katta odam» deb hisoblagan yoshga yetib qarasam, hali ulg'aymaganimdan hayron bo'laman. "
            "Masalan, ertalab uzoq uxlagim kelishi ham bolalikdagidek. Bundan tashqari, ish og'ir bo'lganda "
            "necha marta ishni qoldirgim keladi. «Isitmam chiqdi» deb yolg'on aytib, rostdan ishga bormagan "
            "paytlarim ham bo'lgan. Holbuki bolaligimda rost isitmam bo'lsa ham, maktabga muntazam borardim. "
            "Yana, sabzi va qalampir kabi bolaligimda yoqtirmagan taomlarni hozir ham yoqtirmayman, shuning uchun "
            "ovqatga solingan bo'lsa, yemaslikka harakat qilaman. Shunga qaramay, o'z bolamga «tanlamasdan, "
            "hamma narsani ye» deb aytaman. Shunday kekkayadigan, ustalik bilan yolg'on aytadigan katta odamga "
            "aylangan hozirgi o'zim — bolaligimdagidan o'sish o'rniga, balki yomonlashgandirman. Shunday ekan, "
            "ota-onam ham ilgari xuddi hozirgi men kabi o'ylab, «katta odam» bo'lishga harakat qilgan ekan-da deb "
            "o'ylasam, allaqanday iliq tuyg'u paydo bo'ladi."
          ),
          "questions": [
            q("t2-g3-19", None, ["なるところに","なったように","なってみると","なるとしたら"], 3,
              "「大人」だと思っていた年齢に[なってみると]、成長できていない自分に驚く。",
              blankNo="19", expl="〜てみると = ...sam/qilib ko'rsam (natija)"),
            q("t2-g3-20", None, ["あるかないかわからない","めったにない","あるくらいだ","あるはずがないのだ"], 3,
              "会社を休んだことも[あるくらいだ] = hatto ishni qoldirgan paytlarim ham bor.",
              blankNo="20", expl="〜くらいだ = hatto ... darajada"),
            q("t2-g3-21", None, [
                "きらいだから ／ 食べないようにしている",   # (boshqa joylashuv emas — 1-variant pastda)
                "きらいだから ／ 食べないようにしている",
                "好きだから ／ 食べるようにしている",
                "好きだから ／ 食べないようにしている"], 2,
              "今でも[a きらいだから]、料理に入っていると[b 食べないようにしている].",
              blankNo="21", expl="a きらいだから (yoqtirmayman) / b 食べないようにしている (yemaslikka harakat)"),
            q("t2-g3-22", None, ["そんなふうに","どんなふうに","あんなふうに","どんなような"], 1,
              "[そんなふうに]いばったり… = o'shanday kekkayib…",
              blankNo="22", expl="そんなふうに = o'shanday, shu tarzda"),
            q("t2-g3-23", None, ["ところが","つまり","または","そして"], 4,
              "[そして]、自分の父や母も… = Va, ota-onam ham…",
              blankNo="23", expl="そして = va, shundan keyin (qo'shimcha)"),
          ]
        }
      ]
    }
  ]
}

# 21-savol variantlarini to'g'rilaymiz (1-variant a=きらい/b=食べるようにしている)
data["sections"][1]["problems"][2]["questions"][2]["options"][0] = "きらいだから ／ 食べるようにしている"

json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
# tekshiruv
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test02.json yozildi. Jami savol:", tot)
for s in data["sections"]:
    for p in s["problems"]:
        print(" ", p["type"], len(p["questions"]))
