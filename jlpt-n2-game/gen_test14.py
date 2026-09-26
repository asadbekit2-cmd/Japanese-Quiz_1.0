# -*- coding: utf-8 -*-
"""
test14.json generatori — 第14回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.15, Savollar p.138-147
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test14.json")

def q(qid, stem, options, answer, tr, reading=None, expl=None, optsTr=None,
      prefix=None, suffix=None, starPos=None, order=None, blankNo=None):
    d = {"id": qid, "options": options, "answer": answer, "tr": tr}
    if stem is not None: d["stem"] = stem
    if reading: d["reading"] = reading
    if expl: d["explanation_uz"] = expl
    if optsTr: d["optsTr"] = optsTr
    if prefix is not None: d["prefix"] = prefix
    if suffix is not None: d["suffix"] = suffix
    if starPos is not None: d["starPos"] = starPos
    if order is not None: d["order"] = order
    if blankNo is not None: d["blankNo"] = blankNo
    return d

data = {
  "id": 14,
  "title_jp": "第14回 模擬テスト",
  "title_uz": "14-test",
  "minutes": 45,
  "sections": [
    {
      "id": "vocab",
      "name_jp": "文字・語彙",
      "name_uz": "Kanji va lug'at",
      "problems": [
        {
          "id": "v1", "type": "kanji_reading",
          "instruction_jp": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
          "questions": [
            q("t14-v1-1", "責任をとって、議員を【辞める】。",
              ["あきらめる", "うめる", "つとめる", "やめる"], 4,
              "Mas'uliyatni o'z bo'yniga olib, deputatlikdan iste'foga chiqadi (ketadi).",
              reading="やめる", expl="辞める → やめる (iste'foga chiqmoq, ishdan ketmoq)"),
            q("t14-v1-2", "LED電球は【消費】電力が少なく寿命が長い。",
              ["じょうひ", "しょうひ", "しょうび", "じょうび"], 2,
              "LED lampalarning elektr energiyasi sarfi kam va xizmat muddati uzoq.",
              reading="しょうひ", expl="消費 → しょうひ (iste'mol, sarflash)"),
            q("t14-v1-3", "将来に【明確】な目標をもって努力することが大切だ。",
              ["めいたく", "めいかく", "みょうたく", "みょうかく"], 2,
              "Kelajakda aniq maqsad qo'yib harakat qilish muhimdir.",
              reading="めいかく", expl="明確 → めいかく (aniq, ravshan)"),
            q("t14-v1-4", "急に寒さが【逆戻り】したため、風邪をひいてしまった。",
              ["さかもどり", "ぎゃくもどり", "ぎゃくもとり", "さかさもどり"], 2,
              "To'satdan sovuq qaytgani (orqaga qaytgani) sababli shamollab qoldim.",
              reading="ぎゃくもどり", expl="逆戻り → ぎゃくもどり (orqaga qaytish, avvalgi holatga qaytish)"),
            q("t14-v1-5", "彼は仕事はできるが、時間の【観念】がない。",
              ["がいねん", "けねん", "かんねん", "りねん"], 3,
              "U ishni yaxshi uddalaydi, biroq vaqt hissi (vaqt qadri tushunchasi) yo'q.",
              reading="かんねん", expl="観念 → かんねん (tushuncha, ong, his)")
          ]
        },
        {
          "id": "v2", "type": "kanji_writing",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zni kanjida yozish uchun eng to'g'risini tanlang.",
          "questions": [
            q("t14-v2-1", "私は精神的にも時間的にも【よゆう】をもつように心がけている。",
              ["予裕", "余裕", "予有", "余有"], 2,
              "Men ruhiy jihatdan ham, vaqt jihatdan ham xotirjamlik (erkinlik) saqlashga intilaman.",
              reading="よゆう", expl="余裕 → よゆう (mo'llik, xotirjamlik, vaqt/mablag' erkinligi)"),
            q("t14-v2-2", "携帯電話が【こわれて】しまい、友人と連絡が取れない。",
              ["壊れて", "傷れて", "破れて", "崩れて"], 1,
              "Mobil telefonim buzilib qolib, do'stim bilan bog'lana olmayapman.",
              reading="こわれて", expl="壊れる → こわれる (buzilmoq, sinmoq)"),
            q("t14-v2-3", "電気や水道などの【こうきょう】料金を、クレジットカードで支払う。",
              ["公協", "交協", "公共", "交共"], 3,
              "Elektr va suv kabi kommunal (jamoat xizmatlari) to'lovlarini kredit karta orqali to'layman.",
              reading="こうきょう", expl="公共 → こうきょう (jamoat, ommaviy, kommunal)"),
            q("t14-v2-4", "校則や試験を厳しくする教育によって少年【はんざい】を減らした。",
              ["犯罰", "犯罪", "反罰", "反罪"], 2,
              "Maktab qoidalari va imtihonlarni qat'iylashtirish orqali o'smirlar jinoyatchiligini kamaytirdi.",
              reading="はんざい", expl="犯罪 → はんざい (jinoyat)"),
            q("t14-v2-5", "空き巣の被害に【あう】一人暮らしの女性が少なくない。",
              ["遂う", "遣う", "逸う", "遭う"], 4,
              "Uy o'g'riligi jabrini tortgan yolg'iz yashovchi ayollar kam emas.",
              reading="あう", expl="遭う → あう (baxsiz hodisa yoki zararga uchramoq)")
          ]
        },
        {
          "id": "v3", "type": "word_formation",
          "instruction_jp": "（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga qo'yish uchun eng to'g'ri so'z yasovchi qo'shimchani tanlang.",
          "questions": [
            q("t14-v3-1", "手続きについては、お配りした（【小】）冊子をご覧ください。",
              ["薄", "厚", "大", "小"], 4,
              "Jarayon bo'yicha tarqatilgan risolaga (kichik kitobchaga) qarang.",
              expl="小冊子 → しょうさっし (risola, kichik buklet)"),
            q("t14-v3-2", "この世界で一人（【前】）の職人になるには、10年かかるそうだ。",
              ["力", "前", "者", "並"], 2,
              "Bu sohada yetuk (mustaqil) hunarmand bo'lish uchun 10 yil kerak bo'lar ekan.",
              expl="一人前 → いちにんまえ (yetuk, to'laqonli mutaxassis)"),
            q("t14-v3-3", "週刊誌は芸能人の（【私】）生活を書き立てた。",
              ["俗", "個", "私", "自"], 3,
              "Haftalik jurnal mashhurlarning shaxsiy hayoti haqida shov-shuvli maqola yozdi.",
              expl="私生活 → しせいかつ (shaxsiy hayot)"),
            q("t14-v3-4", "この地域にはときどき野生動物が人間の生活（【圏】）に入り込んでくる。",
              ["圏", "層", "間", "中"], 1,
              "Bu hududga vaqti-vaqti bilan yovvoyi hayvonlar insonlarning yashash hududiga kirib keladi.",
              expl="生活圏 → せいかつけん (yashash hududi/doirasi)"),
            q("t14-v3-5", "先着（【順】）に整理券を配ります。",
              ["者", "番", "順", "人"], 3,
              "Birinchi kelish tartibida navbat chiptalari tarqatiladi.",
              expl="先着順 → せんちゃくじゅん (kelish navbati/tartibi bo'yicha)")
          ]
        },
        {
          "id": "v4", "type": "context_vocab",
          "instruction_jp": "（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gap mazmuniga mos keluvchi eng to'g'ri so'zni tanlang.",
          "questions": [
            q("t14-v4-1", "父に代わって社長に（【就任】）したころは、父を追い抜きたいとばかり思っていた。",
              ["就任", "交代", "就職", "後任"], 1,
              "Otamning o'rniga prezidentlik lavozimiga tayinlangan paytlarimda faqat otamdan o'zib ketishni o'ylar edim.",
              expl="就任 → しゅうにん (lavozimga kirishish, tayinlanish)"),
            q("t14-v4-2", "朝ごはんを食べないで登校する児童が多いのは（【深刻】）な問題だ。",
              ["皮肉", "深刻", "格別", "真剣"], 2,
              "Nonushta qilmasdan maktabga keladigan o'quvchilar ko'pligi jiddiy muammodir.",
              expl="深刻 → しんこく (jiddiy, og'ir)"),
            q("t14-v4-3", "学生時代のアルバイトは、（【純粋】）に生活費のためのものだった。",
              ["平等", "陽気", "面倒", "純粋"], 4,
              "Talabalik davridagi qo'shimcha ishim faqatgina tirikchilik xarajatlari uchun edi.",
              expl="純粋に → じゅんすいに (faqatgina, sof)"),
            q("t14-v4-4", "大統領の通る道は、おおぜいの警官が（【厳重】）に警備していた。",
              ["厳重", "強力", "膨大", "過多"], 1,
              "Prezident o'tadigan yo'lni ko'plab politsiyachilar qattiq qo'riqlayotgan edi.",
              expl="厳重 → げんじゅう (qat'iy, kuchaytirilgan)"),
            q("t14-v4-5", "競馬の世界では、ダービーに勝つことが最高の（【誇り】）である。",
              ["栄え", "譲り", "誇り", "見ばえ"], 3,
              "Ot poygasi olamida Derbida g'alaba qozonish eng oliy faxr (iftixor) hisoblanadi.",
              expl="誇り → ほこり (faxr, iftixor)"),
            q("t14-v4-6", "遅くなりましたから（【そろそろ】）失礼します。どうもごちそうになりました。",
              ["とうとう", "いよいよ", "そろそろ", "たまたま"], 3,
              "Kech bo'lib qoldi, endi asta ruxsatingiz bilan qaytay. Ziyofat uchun katta rahmat.",
              expl="そろそろ (sekin-asta, vaqti kelmoq)"),
            q("t14-v4-7", "条例の改正について発言が続き、議論は（【ヒートアップ】）した。",
              ["ヒートアップ", "イメージアップ", "バックアップ", "タイアップ"], 1,
              "Qoidani qayta ko'rib chiqish bo'yicha fikrlar davom etib, bahs-munozara qizib ketdi.",
              expl="ヒートアップ (qizib ketish, avj olish)")
          ]
        },
        {
          "id": "v5", "type": "paraphrase",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t14-v5-1", "彼は自分の発言を【打ち消した】。",
              ["修正した", "伝達した", "記録した", "否定した"], 4,
              "U o'zining aytgan gapini rad etdi (inkor qildi).",
              expl="打ち消す（うちけす）＝ 否定する（ひていする） (inkor qilmoq, rad etmoq)"),
            q("t14-v5-2", "政治を批判したこの新聞記事は、とても【鋭い】。",
              ["間違っている", "優れている", "冷静である", "読まれている"], 2,
              "Siyosatni tanqid qilgan ushbu gazeta maqolasi nihoyatda o'tkir (yetuk).",
              expl="鋭い（するどい）＝ 優れている（すぐれている） (yetuk, teran, o'tkir)"),
            q("t14-v5-3", "木村さんは、【始終】携帯のメールをチェックしている。",
              ["何度か", "いつも", "はじめに", "たまに"], 2,
              "Kimura doimiy ravishda telefonidagi xabarlarni tekshirib turadi.",
              expl="始終（しじゅう）＝ いつも (doim, to'xtovsiz)"),
            q("t14-v5-4", "君にこの仕事を任せるから【せいぜい】がんばってくれ。",
              ["いいかげんに", "つらくても", "できるだけ", "最後まで"], 3,
              "Senga bu ishni ishonib topshiryapman, shuning uchun bor kuching bilan harakat qil.",
              expl="せいぜい ＝ できるだけ (qo'ldan kelgancha, bor kuchi bilan)"),
            q("t14-v5-5", "この計画を実施する場合、どんな【メリット】がありますか。",
              ["不利な点", "有利な点", "疑問点", "問題点"], 2,
              "Bu rejani amalga oshiradigan bo'lsak, qanday afzalliklari bor?",
              expl="メリット ＝ 有利な点（ゆうりなてん） (afzallik, foydali jihat)")
          ]
        },
        {
          "id": "v6", "type": "usage",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'z qaysi gapda eng to'g'ri ma'noda ishlatilganini tanlang.",
          "questions": [
            q("t14-v6-1", "【大半】",
              [
                "地震の被害は2兆円の大半に達した。",
                "日本はエネルギーの大半を輸入に頼っている。",
                "彼が犯人だという証拠は大半ある。",
                "あの人は株で大半の富を得たらしい。"
              ], 2,
              "Yaponiya energiyaning katta qismini importga tayanadi.",
              expl="大半（たいはん）— katta qismi, aksariyati. 2-gap to'g'ri.",
              optsTr=[
                "Zilzila zarari 2 trillion yenning katta qismiga yetdi (xato).",
                "Yaponiya energiyaning katta qismini importga tayanadi.",
                "Uning jinoyatchi ekanligiga dalil katta qismi bor (xato).",
                "U odam aksiyada katta qismi boylikka erishdi (xato)."
              ]),
            q("t14-v6-2", "【口実】",
              [
                "夫は仕事の付き合いを口実に、毎晩飲んで帰ってくる。",
                "財布を拾ったことが口実で彼女と知り合いになった。",
                "お金を借りるには一定の口実がある。",
                "学校に来ないのはどうもいじめが口実のようだ。"
              ], 1,
              "Erim ishdagi oshno-og'aynigarchilikni bahona qilib, har kecha ichib qaytadi.",
              expl="口実（こうじつ）— bahona, vaj. 1-gap to'g'ri.",
              optsTr=[
                "Erim ishdagi muloqotni bahona qilib, har kecha ichib qaytadi.",
                "Hamyon topib olganim sabab bo'lib u bilan tanishdim (xato, きっかけ ishlatiladi).",
                "Pul qarz olishda ma'lum bahona bor (xato, 理由 ishlatiladi).",
                "Maktabga kelmasligi bezorilik bahona shekilli (xato, 原因 ishlatiladi)."
              ]),
            q("t14-v6-3", "【あいまい】",
              [
                "明け方、亡くなった母のあいまいな夢を見た。",
                "あいまいな発言を繰り返す首相に国民は失望した。",
                "その情報は今のところあいまいなので、確からしい。",
                "暇がなくてあいまいになっている本がたくさんある。"
              ], 2,
              "Noaniq bayonotlarni takrorlagan bosh vazirdan xalq hafsalasi pir bo'ldi.",
              expl="あいまい（曖昧）— noaniq, tushunarsiz, mujmal. 2-gap to'g'ri.",
              optsTr=[
                "Tong payti vafot etgan onamning noaniq tushini ko'rdim (xato).",
                "Noaniq bayonotlarni takrorlayotgan bosh vazirdan xalq hafsalasi pir bo'ldi.",
                "U ma'lumot hozircha noaniq bo'lgani uchun ishonchli (xato, mantiqsiz).",
                "Vaqt bo'lmay noaniq bo'lib yotgan kitoblar ko'p (xato)."
              ]),
            q("t14-v6-4", "【要点】",
              [
                "この演説は要点よくまとめられている。",
                "彼は何をやらせても要点が悪い。",
                "人に説明するときは、要点をおさえて話しなさい。",
                "古都の要点を1日案内してもらった。"
              ], 3,
              "Odamlarga tushuntirayotganda, asosiy mazmunni (muhim nuqtani) qamrab gapir.",
              expl="要点（ようてん）— asosiy muhim nuqta. 3-gap to'g'ri.",
              optsTr=[
                "Bu nutq asosiy nuqta yaxshi tuzilgan (xato, 要領よく ishlatiladi).",
                "Unga nima topshirsang ham asosiy nuqtasi yomon (xato).",
                "Odamlarga tushuntirganda asosiy nuqtani qamrab gapir.",
                "Qadimiy shaharning asosiy nuqtasini 1 kun aylantirdi (xato)."
              ]),
            q("t14-v6-5", "【持続】",
              [
                "この頭痛薬は約12時間、効き目が持続する。",
                "一晩中持続して運転しないと、明日の朝までに故郷に帰れない。",
                "このところ、いやな事件が持続して起こる。",
                "この和菓子はあまり持続しないので早目に食べてください。"
              ], 1,
              "Bu bosh og'rig'i dorisining ta'siri taxminan 12 soat davom etadi.",
              expl="持続（じぞく）— ta'sir yoki holatning uzoq saqlanib turishi. 1-gap to'g'ri.",
              optsTr=[
                "Bu bosh og'rig'i dorisining ta'siri taxminan 12 soat davom etadi.",
                "Tun bo'yi to'xtovsiz haydamasang ertalabgacha yetib bo'lmaydi (xato).",
                "So'nggi paytlarda yoqimsiz hodisalar ketma-ket yuz beryapti (xato).",
                "Bu shirinlik uzoq saqlanmaydi, tezroq yeng (xato)."
              ])
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
          "id": "g1", "type": "grammar_sent_form",
          "instruction_jp": "次の文の（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi qavs ichiga qo'yish uchun eng to'g'ri grammatik shaklni tanlang.",
          "questions": [
            q("t14-g1-1", "A「試験はいつだっけ？」\nB「たしか来週（【だとさ】）、ヨウさんが言っていたよ。」",
              ["だか", "だとさ", "だが", "だけど"], 2,
              "A: 'Imtihon qachon edi?' B: 'Adashmasam keyingi hafta emish, Yo shunday dedi.'",
              expl="〜だとさ（だとか）— eshitgan gapni yetkazish (eshitdimki / emish)."),
            q("t14-g1-2", "めいのかわいらしさ（【といったら】）、まるで天使のようだ。",
              ["としたら", "といえば", "といっても", "といったら"], 4,
              "Jiyanimning shiringina yoqimtoyligini aytmaysizmi, xuddi farishtaning o'zginasi!",
              expl="〜といったら（ありはしない）— ...darajasini aytmaysizmi (kuchli hayrat/his)."),
            q("t14-g1-3", "私も同じ失敗をした（【からこそ】）、あなたに注意しているのです。",
              ["からこそ", "からは", "くせに", "ことだから"], 1,
              "Men ham aynan shunday xatoga yo'l qo'yganim sababli ham sizni ogohlantiryapman.",
              expl="〜からこそ — aynan shu sabab tufayligina (kuchli urg'u)."),
            q("t14-g1-4", "我が社は、子ども向けの絵本を（【中心に】）多くの本を出版しています。",
              ["真ん中に", "中心に", "中央に", "最大に"], 2,
              "Bizning kompaniya bolalar uchun rasmli kitoblarni asosiy yo'nalish qilib, ko'plab kitoblarni nashr etadi.",
              expl="〜を中心に — ...ni asosiy qilib olgan holda."),
            q("t14-g1-5", "年齢（【にかかわりなく】）社員を募集するように、政府は会社を指導した。",
              ["にかぎりなく", "にかかわりなく", "はぬきにして", "のせいで"], 2,
              "Hukumat kompaniyalarga yoshiga qaramasdan (yoshidan qat'i nazar) xodimlarni ishga olishni tayinladi.",
              expl="〜にかかわりなく — ...dan qat'i nazar, farqsiz."),
            q("t14-g1-6", "その人は道を教えてくれた（【ばかりか】）、わざわざ駅まで連れて行ってくれた。",
              ["ばかりに", "ところに", "ばかりか", "どころか"], 3,
              "U kishi yo'l ko'rsatib bergani yetmagandek, ataylab vokzalga qadar olib borib qo'ydi.",
              expl="〜ばかりか — ...gina emas, balki (ustiga-ustak)."),
            q("t14-g1-7", "社長が交代したことを（【契機にして】）、社名を変えることになった。",
              ["事情にして", "結果として", "契機にして", "原因にして"], 3,
              "Rahbar almashishini yaxshi burilish yasab, kompaniya nomini o'zgartiradigan bo'ldik.",
              expl="〜を契機（けいき）にして — ...ni yaxshi fursat/turtki bilib."),
            q("t14-g1-8", "試験の心配はしなくていい。君ほどの学力があれば（【合格するに決まっている】）よ。",
              ["合格するわけがある", "合格するものがある", "合格することに決めてある", "合格するに決まっている"], 4,
              "Imtihondan xavotir olmasang ham bo'ladi. Sendek bilim bo'lsa, o'tishing aniq-ku!",
              expl="〜に決まっている — albatta ...bo'lishi aniq, shubhasiz."),
            q("t14-g1-9", "結婚のお祝いに包丁を（【贈るものではない】）と言われるが、相手が欲しいならよいのではないか。",
              ["贈らないものでない", "贈るものではない", "贈らないわけではない", "贈るわけはない"], 2,
              "To'y sovg'asiga pichoq berish to'g'ri emas deyilsa-da, agar qarshi tomon xohlayotgan bo'lsa yaxshi emasmi?",
              expl="〜ものではない — odatda ...qilish to'g'ri kelmaydi (axloqiy/an'anaviy qoida)."),
            q("t14-g1-10", "あまり（【がんばりすぎない】）人のほうが、かえって長続きするものだ。",
              ["がんばるにすぎない", "がんばりすぎない", "がんばろうとする", "がんばるばかりの"], 2,
              "Haddan ortiq o'zini zo'riqtirmaydigan odamlar aksincha ishni uzoqroq davom ettira oladi.",
              expl="〜すぎない — me'yoridan oshirmaslik; がんばりすぎない = haddan ortiq zo'riqmaslik."),
            q("t14-g1-11", "本来なら社長が（【お見舞いにくるところ】）ですが、失礼ながら部長の私がまいりました。",
              ["お見舞いにくるところ", "お見舞いされるはず", "お見舞いにくること", "お見舞いにくるとき"], 1,
              "Aslida rahbarning o'zi hol so'ragani kelishi kerak bo'lgan vaziyat edi, ammo bo'lim boshlig'i bo'lgan men keldim.",
              expl="〜ところ（ですが）— aslida shunday bo'lishi kerak bo'lgan vaziyatda."),
            q("t14-g1-12", "A「成人式であばれる人が増えているようですね。」\nB「日本では20歳になっても、大人に（【なりきれない】）人が多いのです。」",
              ["なりそうもない", "なるはずがない", "なりきれない", "なっていられない"], 3,
              "A: 'Balog'at bayramida to'polon qiladiganlar ko'payayotganga o'xshaydi-a?' B: 'Yaponiyada 20 yoshga to'lsa ham to'liq katta odam bo'la olmaganlar ko'p-da.'",
              expl="〜きれない — oxirigacha / to'liq ...bo'la olmaslik.")
          ]
        },
        {
          "id": "g2", "type": "grammar_sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keluvchi to'g'ri so'zni tanlang.",
          "questions": [
            q("t14-g2-1", None,
              ["にも", "ように", "理解できる", "絵による"], 2,
              "Yapon tilida o'qiy olmaydigan odamlarga ham tushunarli bo'lishi uchun rasmli belgilar qo'yilgan.",
              prefix="日本語が読めない人", suffix="マークがつけられている。", starPos=3, order=[1, 3, 2, 4],
              expl="日本語が読めない人【にも】【理解できる】【★ように】【絵による】マークがつけられている。"),
            q("t14-g2-2", None,
              ["やったほうが", "迷ったときは", "かと", "やめよう"], 3,
              "Qilsammi yoki qilmasammi deb ikkilanib qolganda qilgan afzalroq, shunda pushaymon bo'lmaysan.",
              prefix="やろうか", suffix="悔やまなくてすむことが多い。", starPos=2, order=[4, 3, 2, 1],
              expl="やろうか【やめよう】【★かと】【迷ったときは】【やったほうが】悔やまなくてすむことが多い。"),
            q("t14-g2-3", None,
              ["新製品を", "もとに", "作る", "して"], 4,
              "Mijozlarning fikr-mulohazalari asosida yangi mahsulot ishlab chiqish uchun yig'ilish o'tkazildi.",
              prefix="お客様の意見を", suffix="ための会議が開かれた。", starPos=2, order=[2, 4, 1, 3],
              expl="お客様の意見を【もとに】【★して】【新製品を】【作る】ための会議が開かれた。"),
            q("t14-g2-4", None,
              ["めぐって", "兄弟が", "あげく", "はげしく争った"], 4,
              "Ota-onaning merosi ustida aka-ukalar qattiq janjallashishi oqibatida oxir-oqibat bir-biridan yuz o'girdi.",
              prefix="親の遺産を", suffix="とうとうけんか別れになった。", starPos=3, order=[1, 2, 4, 3],
              expl="親の遺産を【めぐって】【兄弟が】【★はげしく争った】【あげく】とうとうけんか別れになった。"),
            q("t14-g2-5", None,
              ["料理をしなくていい", "好きな", "だけでなく", "ということ"], 1,
              "Sayohatni yoqtiruvchi uy bekalari ko'pligiga manzaralarni yoqtirishdan tashqari, ovqat pishirmaslik imkoni ham sababdir.",
              prefix="旅好きの主婦が多いのは、めずらしい景色を見るのが", suffix="も理由の1つだ。", starPos=3, order=[2, 3, 1, 4],
              expl="旅好きの主婦が多いのは、めずらしい景色を見るのが【好きな】【だけでなく】【★料理をしなくていい】【ということ】も理由の1つだ。")
          ]
        },
        {
          "id": "g3", "type": "grammar_passage_context",
          "instruction_jp": "次の文章を読んで、文章全体の趣旨を踏まえて、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlar uchun kontekstga mos eng to'g'ri javobni tanlang.",
          "passage": "コミュニケーションには「聞く」「[ 50-a ]」という情報を中に取り入れる作業と、「話す」「[ 50-b ]」という情報を外に発信する作業があります。\nその場合、特に重要なのが「聞く」という作業です。ある学者の調査によると、コミュニケーションに使われる時間は、「話す」が30%、「読む」が16%、「書く」が9%なのに対して、「聞く」は45%も使われています。それ[ 51 ]、聞く練習はあまり行われない傾向があります。これは、声や音は自然に耳に入ってくるのに対して、話す・読む・書くは[ 52 ]作業になるからでしょう。\nそこで自然に音が耳に入ってくることを「聞く」、意識して聞くことを「聴く」と表しましょう。\nまず、話を聴くことによって、相手がどう考え、何を感じ、どうしようとしているかがわかります。一般的な情報も相手から得ることができます。\nその次に、相手の話を聴くことは、相手に注目すること、すなわち相手の存在を認めることを意味します。話を聴かないと逆に、相手は自分を[ 53 ]感じます。\n第三に、相手との関係をよくすることができます。話をよく聴くことによって、相手と親しい関係に[ 54 ]、相手もこちらに好意を感じるようになるのです。\nというわけで、コミュニケーション能力をつけるには、まず「聴く技術」を身につけることが大切なのです。",
          "questions": [
            q("t14-g3-1", "［ 50-a ］ / ［ 50-b ］に入る組み合わせとして最もよいものを選びなさい。",
              ["a 読む / b 書く", "a 書く / b 読む", "a 話す / b 聞く", "a 読む / b 聞く"], 1,
              "［ 50-a ］va［ 50-b ］uchun to'g'ri juftlikni tanlang.",
              blankNo=50, expl="Axborotni qabul qilishga 'o'qish (読む)', tashqariga uzatishga 'yozish (書く)' to'g'ri keladi."),
            q("t14-g3-2", "［ 51 ］に入る最もよいものを選びなさい。",
              ["だからこそ", "のために", "にもかかわらず", "にしたがって"], 3,
              "［ 51 ］bo'sh o'rniga mos bog'lovchini tanlang.",
              blankNo=51, expl="45% ishlatilishiga qaramasdan mashq qilinmaydi: 「にもかかわらず (qaramasdan)」."),
            q("t14-g3-3", "［ 52 ］に入る最もよいものを選びなさい。",
              ["無意識の", "自然な", "意識的な", "不自然な"], 3,
              "［ 52 ］bo'sh o'rniga mos so'zni tanlang.",
              blankNo=52, expl="O'z ixtiyori bilan ongli ravishda bajariladigan faoliyat: 「意識的な (ongli/maqsadli)」."),
            q("t14-g3-4", "［ 53 ］に入る最もよいものを選びなさい。",
              ["攻撃されたように", "否定されたように", "認められたように", "注目されたように"], 2,
              "［ 53 ］bo'sh o'rniga mos ifodani tanlang.",
              blankNo=53, expl="Suhbatdoshi uni eshitmasa, inkor etilgandek his qiladi: 「否定されたように」."),
            q("t14-g3-5", "［ 54 ］に入る最もよいものを選びなさい。",
              ["なりそうになると", "なるとしても", "なるにつけても", "なるとともに"], 4,
              "［ 54 ］bo'sh o'rniga mos grammatik shaklni tanlang.",
              blankNo=54, expl="Yaqin munosabatga aylanishi bilan birga: 「なるとともに」.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK! test14.json yaratildi: 6 vocab + 3 grammar bo'limlari.")
