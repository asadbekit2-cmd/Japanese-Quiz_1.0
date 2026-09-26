# -*- coding: utf-8 -*-
"""
test12.json generatori — 第12回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.13, Savollar p.118-127
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test12.json")

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
  "id": 12,
  "title_jp": "第12回 模擬テスト",
  "title_uz": "12-test",
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
            q("t12-v1-1", "現地の人々が技術を身につけ、仕事に【就ける】ような援助が必要だ。",
              ["とける", "かける", "つける", "あける"], 3,
              "Mahalliy aholi hunar o'rganib, ishga joylasha olishi uchun yordam ko'rsatish zarur.",
              reading="つける", expl="就く → つく (ishga/lavozimga joylashmoq; 就ける = ishga kira oladigan)"),
            q("t12-v1-2", "運動不足であると、汗をかいて体温を【調節】する機能が弱くなってしまう。",
              ["ちょうせつ", "ちゅうせつ", "ちょうせち", "ちゅうせち"], 1,
              "Harakatsizlik (kamharakatlik) natijasida terlab tana haroratini boshqarish (tartibga solish) funksiyasi zaiflashib qoladi.",
              reading="ちょうせつ", expl="調節 → ちょうせつ (tartibga solish, boshqarish)"),
            q("t12-v1-3", "朝、【起床】するのがつらい人は、午前中、太陽光線を浴びるとよい。",
              ["きじょう", "きしょう", "ぎじょう", "きっしょう"], 2,
              "Ertalab uyg'onish (o'rindan turish) qiyin bo'lgan insonlar tushgacha oftobda sayr qilsa yaxshi.",
              reading="きしょう", expl="起床 → きしょう (o'rindan turish, uyg'onish)"),
            q("t12-v1-4", "佐藤さんは、オンラインゲームに【熱中】している。",
              ["ねつちゅう", "ねつじゅう", "ねっちゅう", "ねっじゅう"], 3,
              "Sato onlayn o'yinlarga qattiq berilib ketgan (sho'ng'ib ketgan).",
              reading="ねっちゅう", expl="熱中 → ねっちゅう (berilib ketish, sho'ng'ish)"),
            q("t12-v1-5", "バスや電車でお年寄りに席を【譲らない】若者が多い。",
              ["うつらない", "ゆずらない", "まわらない", "さがらない"], 2,
              "Avtobus yoki poyezdda qariyalarga joy bermaydigan yoshlar ko'p.",
              reading="ゆずらない", expl="譲る → ゆずる (joy berish, o'rnini bo'shatish)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t12-v2-6", "飲み水や食事に使用されている【かがく】物質の安全性に不安のある人が多い。",
              ["科画", "科学", "化画", "化学"], 4,
              "Ichimlik suvi va taomlarda ishlatiladigan kimyoviy moddalarning xavfsizligidan xavotirlanadiganlar ko'p.",
              reading="かがく", expl="化学 → かがく (kimyo, kimyoviy)"),
            q("t12-v2-7", "このチラシの【ゆうこう】期間は、本日より1週間とさせていただきます。",
              ["有効", "優効", "有抗", "結抗"], 1,
              "Ushbu flayerning amal qilish (yaroqlilik) muddati bugundan boshlab 1 hafta etib belgilanadi.",
              reading="ゆうこう", expl="有効 → ゆうこう (yaroqli, amaldagi)"),
            q("t12-v2-8", "この暑さで祖父は体力をすっかり【しょうもう】してしまった。",
              ["消耗", "失耗", "減耗", "省耗"], 1,
              "Bu jaziramada bobom butunlay kuch-quvvatini yo'qotdi (charchab toliqdi).",
              reading="しょうもう", expl="消耗 → しょうもう (charchash, quvvat sarfi/yo'qotish)"),
            q("t12-v2-9", "日本は国土の約70パーセントを森林が【しめて】いる緑豊かな国の1つである。",
              ["示めて", "占めて", "閉めて", "締めて"], 2,
              "Yaponiya hududining taxminan 70 foizini o'rmonlar egallagan ko'm-ko'k tabiatli mamlakatlardan biridir.",
              reading="しめて", expl="占める → しめる (egallamoq, qamrab olmoq)"),
            q("t12-v2-10", "長くて【ようりょう】を得ない話は、聞くほうも疲れてしまう。",
              ["用項", "要項", "用領", "要領"], 4,
              "Uzoq va ma'no-mazmunidan uzoq (chalkash) gapni eshitayotgan tomon ham charchab ketadi.",
              reading="ようりょう", expl="要領 → ようりょう (mohiyat, asosiy ma'no/yo'sinda; 要領を得ない = mujmal)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t12-v3-11", "日本の（　）人口はますます減少していく。",
              ["本", "総", "来", "各"], 2,
              "Yaponiyaning umumiy aholi soni tobora kamayib bormoqda.",
              expl="総人口 (そうじんこう) = umumiy aholi soni"),
            q("t12-v3-12", "新しい土地で（　）出発することにした。",
              ["始", "前", "再", "予"], 3,
              "Yangi zaminda hayotni qaytadan boshlashga (qayta start olishga) qaror qildim.",
              expl="再出発 (さいしゅっぱつ) = qayta boshlash, yangidan yo'lga chiqish"),
            q("t12-v3-13", "来月から勤務（　）が変わります。",
              ["先", "場", "事", "業"], 1,
              "Kelasi oydan boshlab ish joyim (tashkilotim) o'zgaradi.",
              expl="勤務先 (きんむさき) = ish joyi"),
            q("t12-v3-14", "この番組は現場からの（　）放送だ。",
              ["直", "生", "現", "未"], 2,
              "Bu dastur to'g'ridan-to'g'ri voqea joyidan jonli efirda (jonli translyatsiya) uzatilmoqda.",
              expl="生放送 (なまほうそう) = jonli efir, to'g'ridan-to'g'ri translyatsiya"),
            q("t12-v3-15", "バンドのメンバーを集めるのは（　）苦労だった。",
              ["大", "多", "一", "重"], 3,
              "Musiqiy guruh a'zolarini to'plash o'ziga yarasha ancha katta mashaqqat bo'ldi.",
              expl="一苦労 (ひとくろう) = ancha-muncha mashaqqat/qiyinchilik")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t12-v4-16", "それは（　）反抗期というもので、子どもがきっちんと成長しているということです。",
              ["わりに", "いわゆる", "あらゆる", "やたらに"], 2,
              "Bu aytish mumkinki (xalq tilidagi) o'tish davri qarshiligi bo'lib, bola durust ulg'ayayotganidan dalolat beradi.",
              reading="いわゆる", expl="いわゆる = aytish mumkinki, xalq tilida aytiladigan"),
            q("t12-v4-17", "歯はよく（　）刺激しないと丈夫にならない。",
              ["研いで", "砕いて", "噛んで", "畳んで"], 3,
              "Tishlarni yaxshilab chaynash orqali harakatlantirmasa mustahkam bo'lmaydi.",
              reading="かんで", expl="噛む (かむ) = chaynash"),
            q("t12-v4-18", "最近、（　）離れが進んで、新聞の売り上げも落ちた。",
              ["書籍", "活字", "報道", "印刷"], 2,
              "So'nggi paytlarda bosma matnlardan uzoqlashish kuchayib, gazeta savdosi ham tushib ketdi.",
              reading="かつじばなれ", expl="活字離れ (かつじばなれ) = kitob/bosma matndan uzoqlashish"),
            q("t12-v4-19", "アニメ（　）の影響で声優は人気の職業となった。",
              ["メディア", "ベース", "ブーム", "ペース"], 3,
              "Anime ommalashuvi (bum/shov-shuv) ta'sirida ovoz berish aktyori mashhur kasbga aylandi.",
              expl="ブーム (boom) = ommaviy qiziqish to'lqini, shov-shuv"),
            q("t12-v4-20", "明日のことはわからない。明日の（　）はないということはすべての人にあてはまる。",
              ["担当", "保証", "承知", "責任"], 2,
              "Ertangi kun nima bo'lishini bilmaysan. Ertangi kunning kafolati yo'qligi barcha insonlarga tegishlidir.",
              reading="ほしょう", expl="保証 (ほしょう) = kafolat"),
            q("t12-v4-21", "試験は英語で行われたので、日本人学生には（　）だった。",
              ["不利", "不正", "不可", "不平"], 1,
              "Imtihon ingliz tilida o'tkazilganligi sababli, yapon talabalari uchun noqulay (noo'ng'ay/ustunliksiz) bo'ldi.",
              reading="ふり", expl="不利 (ふり) = noqulay, noo'rin, zararga ishlaydigan"),
            q("t12-v4-22", "日本の農業に（　）を感じる若者が増えてきた。",
              ["意思", "利益", "純粋", "魅力"], 4,
              "Yaponiya qishloq xo'jaligida joziba (qiziqish/jozibadorlik) his qilayotgan yoshlar ko'paydi.",
              reading="みりょく", expl="魅力 (みりょく) = joziba, maftunkorlik")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t12-v5-23", "とうとう店を【たたむ】ことにした。",
              ["始める", "休む", "直す", "閉じる"], 4,
              "Nihoyat do'konni yopishga (faoliyatini tugatishga) qaror qildik.",
              reading="たたむ", expl="（店を）たたむ ≈ 閉じる (do'konni butunlay yopmoq)"),
            q("t12-v5-24", "決勝レースのスタートが告げられると、場内は【しいんと】なった。",
              ["華やかに", "明るく", "静かに", "騒がしく"], 3,
              "Final poygasining starti e'lon qilingach, maydon sukunatga cho'mdi (jim-jit bo'lib qoldi).",
              reading="しいんと", expl="しいんと ≈ 静かに (jim-jit, sukunat ichida)"),
            q("t12-v5-25", "古い民家を【改造して】喫茶店にする。",
              ["作り直して", "取り消して", "利用して", "掃除して"], 1,
              "Eski hovli-uyni qayta ta'mirlab (o'zgartirib) qahvaxonaga aylantirmoqchimiz.",
              reading="かいぞうして", expl="改造する ≈ 作り直す (qayta qurmoq, rekonstruksiya qilmoq)"),
            q("t12-v5-26", "お金にはなぜか【縁がない】。",
              ["興味", "関係", "運", "苦労"], 2,
              "Nimadandir pul bilan hech aloqam / nasibam bog'lanmaydi.",
              reading="えんがない", expl="縁がない ≈ 関係がない (aloqasi/bog'liqligi yo'q)"),
            q("t12-v5-27", "彼の【ストレートな】発言に、みな驚いた。",
              ["常識のない", "期待はずれの", "遠慮ない", "突然の"], 3,
              "Uning gapni to'g'ridan-to'g'ri (hech tortinmasdan) aytganiga hamma hayron qoldi.",
              expl="ストレートな ≈ 遠慮ない (ochiqchasiga, tortinmay to'g'ri aytilgan)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'zning gapda eng to'g'ri ishlatilgan variantini tanlang.",
          "questions": [
            q("t12-v6-28", "【恐縮】の使い方として最もよいものを選びなさい。",
              [
                "上司と一緒に外出すると緊張で恐縮してしまう。",
                "泊めていただいた上にごちそうにまでなって、恐縮です。",
                "みなで恐縮して卒業記念の写真をとってもらった。",
                "大勢の人の前で話すなんて、まったく恐縮してしまった。"
              ], 2,
              "恐縮 (kyoushuku) = xijolat bo'lish, minnatdorchilik va uzr aralash his.",
              expl="「ごちそうにまでなって、恐縮です」= mehmondorchilik uchun xijolatdaman/minnatdorman (to'g'ri ishlatilish)."),
            q("t12-v6-29", "【心当たり】の使い方として最もよいものを選びなさい。",
              [
                "娘が帰ってこないので、心当たりに次々と電話した。",
                "んないい奥さんをもらうなんて、彼は女性の心当たりがある。",
                "私の本当の気持ちを、親友に心当たりに打ち明けた。",
                "君はふだんからの心当たりがなっていない。"
              ], 1,
              "心当たり (kokoroatari) = taxmin qilinayotgan manzil/joy.",
              expl="「心当たりに次々と電話した」= ehtimolli barcha tanish joylarga ketma-ket qo'ng'iroq qildim (to'g'ri ishlatilish)."),
            q("t12-v6-30", "【さわやか】の使い方として最もよいものを選びなさい。",
              [
                "今日は寒いので、さわやかな食べ物がいい。",
                "受付の女性はさわやかな笑顔で応対している。",
                "5月の空に鳥がさわやかに飛んでいる。",
                "彼女は細くてさわやかな字を書く。"
              ], 2,
              "さわやか (sawayaka) = yoqimli, tetiklantiruvchi, xushfe'l.",
              expl="「さわやかな笑顔」= samimiy va xushchaqchaq tabassum (to'g'ri ishlatilish)."),
            q("t12-v6-31", "【焦点】の使い方として最もよいものを選びなさい。",
              [
                "この企画は先輩が焦点となって進められる。",
                "2人の話し合いは焦点がずれていて、結論が出ない。",
                "今年の入社試験は面接が焦点です。",
                "よくわかるように焦点してください。"
              ], 2,
              "焦点 (shouten) = asosiy diqqat markazi, fokus.",
              expl="「焦点がずれていて」= asosiy muhokama mavzusidan chalg'ib... (to'g'ri ishlatilish)."),
            q("t12-v6-32", "【考慮】の使い方として最もよいものを選びなさい。",
              [
                "くれぐれも、みなさま方の考慮ある行動をお願い致します。",
                "あの社員にはしっかりした考慮があるので仕事をまかせられる。",
                "参加者の年齢や体力を考慮して、旅行プランを立てた。",
                "どうも今回の事件にはあの人物が考慮しているようだ。"
              ], 3,
              "考慮 (kouryo) = hisobga olish, e'tiborga olish.",
              expl="「年齢や体力を考慮して」= yoshi va jismoniy quvvatini inobatga olib (to'g'ri ishlatilish).")
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
          "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi qavs ichiga eng mos keluvchi grammatik shaklni tanlang.",
          "questions": [
            q("t12-g1-33", "この子犬は、きのう生まれた（　）で、まだ目が開いていない。",
              ["とたん", "まま", "あと", "ばかり"], 4,
              "Bu kuchukcha kechagina tug'ilgani tufayli, hali ko'zlari ochilmagan.",
              expl="「動詞た形 ＋ ばかり」= ...qilinganiga endigina ozgina vaqt bo'ldi."),
            q("t12-g1-34", "交通事情（　）、旅行は1週間延期します。",
              ["により", "につき", "にとり", "に関し"], 1,
              "Yo'l harakati sharoiti sababli, sayohat 1 haftaga qoldiriladi.",
              expl="「〜により」= ...sababli / tufayli (rasmiy bildirishnoma)."),
            q("t12-g1-35", "晩ごはんを作る（　）に、明日の朝ごはんも作っておこう。",
              ["途中", "ついで", "かたわら", "最中"], 2,
              "Kechki ovqat tayyorlash fursatidan foydalanib, ertangi nonushtani ham tayyorlab qo'yay.",
              expl="「〜ついでに」= ...qilish asnosida / fursatdan foydalanib."),
            q("t12-g1-36", "電車が駅に着いたので、読み（　）の本を閉じてバッグにしまった。",
              ["かけ", "つつ", "ながら", "がち"], 1,
              "Poyezd bekatga yetib kelgani uchun o'qib tugatilmagan (chala) kitobni yopib sumkaga soldim.",
              expl="「動詞ます形 ＋ かけ」= chala qolgan / davom etayotgan harakat."),
            q("t12-g1-37", "たばこの購入（　）は、年齢を証明するものが必要になりました。",
              ["にかけて", "に応じて", "にかかわって", "に際して"], 4,
              "Tamaki sotib olish paytida yoshni tasdiqlovchi hujjat talab qilinadigan bo'ldi.",
              expl="「〜に際して（は）」= ...holatida / paytida (rasmiy uslub)."),
            q("t12-g1-38", "自分の国の言葉をよく理解する（　）、外国語を学ぶのはよいことだ。",
              ["以上", "ためで", "うえでも", "ことには"], 3,
              "O'z ona tilini yaxshi tushunish nuqtai nazaridan ham, chet tilini o'rganish juda foydali ishdir.",
              expl="「〜うえで（も）」= ...nuqtai nazaridan / jihatidan qaraganda ham."),
            q("t12-g1-39", "お客さんがげんかんを（　）いなや、電気を消すなんて失礼なことです。",
              ["出るか", "出ないか", "出るや", "出たが"], 3,
              "Mehmon eshikdan chiqishi bilanoq chiroqni o'chirish juda odobsizlikdir.",
              expl="「動詞辞書形 ＋ やいなや」= ...qilishi bilanoq darhol."),
            q("t12-g1-40", "きのうお借りした資料、お返しします。休んだときの分を（　）。",
              ["写していただきました", "写させていただきました", "写させてあげました", "写していただけました"], 2,
              "Kecha sizdan olgan materiallarni qaytarmoqdaman. Darsga kelmagan kunimdagi qismini ko'chirib oldim.",
              expl="「写させていただきました」= ijozatingiz bilan ko'chirib oldim (kamtarinlik ifodasi)."),
            q("t12-g1-41", "もう7時です。女性のみなさんは暗く（　）、早く帰ってください。",
              ["ならないうちに", "なるあいだに", "なりそうなうちに", "ならないあいだに"], 1,
              "Allaqachon soat 7 bo'ldi. Ayollar havo qorong'i bo'lmasdan oldin tezroq uylariga ketsinlar.",
              expl="「〜ないうちに」= ...bo'lmasdan oldin / paytida."),
            q("t12-g1-42", "午後から会議を開きます。昼食を（　）すぐ会議室に来てください。",
              ["食べ終えるなら", "食べ終えたら", "食べ終えると", "食べ終えれば"], 2,
              "Tushdan keyin majlis o'tkazamiz. Tushlikni yeb bo'lishingiz bilanoq darhol majlislar xonasiga keling.",
              expl="「〜たらすぐ」= ...harakat tugashi bilanoq darhol."),
            q("t12-g1-43", "私のピアノの先生はきびしくて、一カ所でも（　）練習をすぐストップさせた。",
              ["間違えるからには", "間違えたからには", "間違えるものなら", "間違えようものなら"], 4,
              "Mening fortepiano ustozim shu qadar qattiqqo'l ediki, hatto bir dona joyda adashib ketsangiz, mashg'ulotni darhol to'xtatardi.",
              expl="「動詞意向形 ＋ ものなら」= mabodo ...qilib qo'ysa (yomon natija)."),
            q("t12-g1-44", "さすがにこのバッグは高かった（　）、10年使ってもまったく形がくずれない。",
              ["にもかかわらず", "というしかなくて", "だけのこと・はあって", "ばかりではなくて"], 3,
              "Bu sumka qimmat bo'lganiga yarasha, 10 yil ishlatilsa ham mutlaqo shakli buzilmadi.",
              expl="「〜だけのことはある」= ...bo'lganiga yarasha arziydi (maqtov).")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の＿★＿に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keladigan eng to'g'ri variantni tanlang.",
          "questions": [
            q("t12-g2-45", None,
              ["いって", "ことは", "からと", "あきらめる"], 1,
              "Bir marta imtihondan yiqilgan sababli deb voz kechishga aslo hojat yo'q.",
              prefix="1回試験に失敗した", suffix="ないですよ。",
              starPos=2, order=[3, 1, 4, 2],
              expl="Tartib: からと(3) いって(1) あきらめる(4) ことは(2) → Yulduzcha 2-o'rinda: いって(1)"),
            q("t12-g2-46", None,
              ["もとで", "水がないという", "条件の", "きびしい"], 3,
              "Sahro jonivorlari suv yo'qligi kabi qattiq sharoitlar ostida jon-jahdi bilan yashab qolmoqda.",
              prefix="砂漠の動物たちは", suffix="必死に生きている。",
              starPos=3, order=[2, 4, 3, 1],
              expl="Tartib: 水がないという(2) きびしい(4) 条件の(3) もとで(1) → Yulduzcha 3-o'rinda: 条件の(3)"),
            q("t12-g2-47", None,
              ["ついて", "お金の問題は", "英語の授業に", "ともかくとして"], 4,
              "Amerika universitetiga borishda pul masalasi o'z yo'liga, ingliz tilidagi darslarni o'zlashtirib keta olarmikanman?",
              prefix="アメリカの大学に行くのに、", suffix="いけるのだろうか。",
              starPos=2, order=[2, 4, 3, 1],
              expl="Tartib: お金の問題は(2) ともかくとして(4) 英語の授業に(3) ついて(1) → Yulduzcha 2-o'rinda: ともかくとして(4)"),
            q("t12-g2-48", None,
              ["かわって", "副社長が", "会社経営", "社長に"], 1,
              "Kasalxonada yotgan prezident o'rniga vitse-prezident kompaniya boshqaruviga mas'ul bo'ldi.",
              prefix="入院中の", suffix="にあたることになった。",
              starPos=2, order=[4, 1, 2, 3],
              expl="Tartib: 社長に(4) かわって(1) 副社長が(2) 会社経営(3) → Yulduzcha 2-o'rinda: かわって(1)"),
            q("t12-g2-49", None,
              ["少なくは", "ものだって", "非常識に", "なってしまった"], 2,
              "A: «Bu jamiyat qoidasi degan narsa.» B: «10 yil avvalgi oddiy qoidalar bugun g'ayrioddiy bema'nilikka aylanib qolgan holatlar ham kam emas.»",
              prefix="A「これが社会の常識というものだ。」\\nB「10年前の常識が", suffix="ないよ。」",
              starPos=3, order=[3, 4, 2, 1],
              expl="Tartib: 非常識に(3) なってしまった(4) ものだって(2) 少なくは(1) → Yulduzcha 3-o'rinda: ものだって(2)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlarga eng mos keluvchi javobni tanlang.",
          "passage": "それまでおだやかだった人が、ちょっとしたことを【 50 】はげしく怒り出すことがあります。まるでその人の血管が突然切れたように見えることから、カタカナで「キレる」と言うようになりました。\n　だまって教室を出ようとした生徒を先生が注意したところ、突然その中学生がナイフを取り出して、先生を刺し殺す事件がありました。その事件以来「キレる若者」が社会の問題になりました。\n　ところが2000年から10代の若者がキレて起こす事件数は大きく増えていないのに、50代、60代の人がキレる事件が非常に多くなりました。\n　たとえば「ちょっと電車が遅れたり、眠っているお客を起こしたりしたとき、怒ってキレるのは中高年の男性です」と証言する駅員もいます。\n　特に、客にはあまり【 51 】サービス業の人たち、役所の公務員などを相手に、つまらないことで何時間も大声で怒るような人が増えました。\n　本来ならキレる若者を注意【 52 】大人が、なぜキレるのでしょうか。\n　昔の老人は、長い人生で得た知識や経験を尊敬されました。現代は次々と新しい機械や技術ができて、ついていけない中高年も少なくありません。以前なら技術を教えて【 53-a 】若者から、教えて【 53-b 】ならなくなりました。これはつらいことでしょう。また会社を辞めてから、地域に話し相手もいない男性が多いのです。心の中にこういう不満やさびしさをかかえることが、中高年がキレる原因かもしれません。\n　人生経験のゆたかな大人【 54 】、おだやかな人ばかりではないのです。",
          "questions": [
            q("t12-g3-50", None,
              ["チャンスに", "きっかけに", "ついでに", "はじめに"], 2,
              "O'sha paytgacha bosiq bo'lgan inson kichik bir sabab tufayli to'satdan qattiq g'azablanib ketishi mumkin.",
              blankNo=50, expl="「〜をきっかけに」= ...tufayli, sabab bo'lib."),
            q("t12-g3-51", None,
              ["文句を言うべき", "文句を言うような", "文句を言えない", "文句を言わせない"], 3,
              "Ayniqsa mijozlariga e'tiroz bildira olmaydigan xizmat ko'rsatish xodimlari...",
              blankNo=51, expl="「文句を言えない」= e'tiroz bildira olmaydigan."),
            q("t12-g3-52", None,
              ["するべき", "していく", "しがちな", "しかねない"], 1,
              "Aslida asabiy yoshlarni ogohlantirishi lozim bo'lgan katta yoshlilar nega o'zlari bunday qilmoqda?",
              blankNo=52, expl="「注意するべき（大人）」= ogohlantirishi lozim bo'lgan."),
            q("t12-g3-53", None,
              ["a くれた ／ b あげなければ", "a もらった ／ b くれなければ", "a もらった ／ b あげなければ", "a やった ／ b もらわなければ"], 4,
              "Ilgari yoshlarga mahorat o'rgatgan bo'lsa, endi yoshlardan o'rganishga majbur bo'lib qoldi.",
              blankNo=53, expl="53-a «やった» (yoshlarga o'rgatib bergan), 53-b «もらわなければ» (yoshlardan o'rganmasa bo'lmay qoldi)."),
            q("t12-g3-54", None,
              ["としては", "だからといって", "だからこそ", "とはいえ"], 2,
              "Hayot tajribasi boy katta yoshli bo'lgani bilan, hamma ham bosiq bo'lavermaydi.",
              blankNo=54, expl="「〜だからといって（〜ない）」= ...bo'lgani sababli deb hamma ham unday emas.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK! test12.json yaratildi: {len(data['sections'][0]['problems'])} vocab + {len(data['sections'][1]['problems'])} grammar bo'limlari.")
