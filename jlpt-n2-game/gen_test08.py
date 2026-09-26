# -*- coding: utf-8 -*-
"""
test08.json generatori — 第8回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.9, Savollar p.78-87
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test08.json")

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
  "id": 8,
  "title_jp": "第8回 模擬テスト",
  "title_uz": "8-test",
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
            q("t8-v1-1", "食器【洗浄機】は、使ってみると不便なところもある。",
              ["せんじょ", "せんざい", "せんじょう", "せんたく"], 3,
              "Idish yuvish mashinasi (posudomoyka) ishlatib ko'rilsa, noqulay tomonlari ham bor.",
              reading="せんじょう", expl="洗浄 → せんじょう (yuvish, tozalash)"),
            q("t8-v1-2", "後輩の第一印象は【神経質】で頼りない感じだ。",
              ["しんけいしつ", "しんきょうしつ", "じんけいしつ", "じんきょうしつ"], 1,
              "Kichik hamkasbning (kouhai) birinchi taassuroti asabiy/o'ta sezgir va ishonchsizdek tuyuldi.",
              reading="しんけいしつ", expl="神経質 → しんけいしつ (asabiy, serzarda, o'ta ta'sirchan)"),
            q("t8-v1-3", "途上国の女性が収入を得られるように、【裁縫】技術の研修を開始した。",
              ["ざいもう", "さいぼう", "さいもう", "さいほう"], 4,
              "Rivojlanayotgan davlatlar ayollari daromad topa olishi uchun tikuvchilik mahorati bo'yicha o'quv-trening boshlandi.",
              reading="さいほう", expl="裁縫 → さいほう (tikuvchilik, kiyim tikish)"),
            q("t8-v1-4", "経済は、都市に集まってくる【有能】で意欲のある人々によって成長してきたといえる。",
              ["うのう", "ゆうえき", "ゆうのう", "ゆうこう"], 3,
              "Iqtisodiyot shaharlarga yig'ilayotgan qobiliyatli va g'ayratli insonlarning mehnati evaziga o'sib kelgan deyish mumkin.",
              reading="ゆうのう", expl="有能 → ゆうのう (iqtidorli, salohiyatli, qobiliyatli)"),
            q("t8-v1-5", "楽をして【稼ぐ】ことを恥としない日本人が多くなってしまった。",
              ["ふせぐ", "かせぐ", "そそぐ", "かつぐ"], 2,
              "Osonlikcha pul topishni (ishlamay daromad ko'rishni) uyat bilmaydigan yaponlar ko'payib ketdi.",
              reading="かせぐ", expl="稼ぐ → かせぐ (pul topmoq, daromad qilmoq)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t8-v2-6", "一部の人間が【ふせい】に利益を得るような世の中であってはならない。",
              ["不政", "不成", "不正", "不制"], 3,
              "Ba'zi odamlar noqonuniy yo'l bilan naf ko'radigan jamiyat bo'lishi aslo mumkin emas.",
              reading="ふせい", expl="不正 → ふせい (adolatsiz, noqonuniy, nohaq)"),
            q("t8-v2-7", "妻とよく話し合ったうえで、離婚【とどけ】を出した。",
              ["届", "居", "展", "届"], 4,
              "Turmush o'rtog'im bilan bafurja gaplashib olgach, ajrashish to'g'risida ariza (xabarnoma) topshirdim.",
              reading="とどけ", expl="届 → とどけ (ariza, xabarnoma, bildirishnoma)"),
            q("t8-v2-8", "過去問題を【ぶんせき】し、短期間で大学合格の力を身につけるつもりだ。",
              ["分責", "分析", "分積", "分折"], 2,
              "O'tgan yillardagi savollarni tahlil qilib, qisqa muddatda universitetga kirish salohiyatini shakllantirmoqchiman.",
              reading="ぶんせき", expl="分析 → ぶんせき (tahlil, analiz)"),
            q("t8-v2-9", "砂糖は畑からできる【てんねん】の調味料だ。",
              ["天燃", "天然", "伝燃", "伝然"], 2,
              "Shakar dalalardan olinadigan tabiiy ta'm beruvchidir (ziravor).",
              reading="てんねん", expl="天然 → てんねん (tabiiy)"),
            q("t8-v2-10", "我が社は「環境にやさしい商品」の開発に力を【そそいで】います。",
              ["注いで", "沿いで", "泊いで", "沖いで"], 1,
              "Bizning kompaniya «ekologik toza mahsulotlar»ni ishlab chiqishga butun kuchini bag'ishlamoqda (sarflamoqda).",
              reading="そそいで", expl="注ぐ → そそぐ (kuch/e'tibor bag'ishlamoq, quymoq)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t8-v3-11", "ファッション界の第一（　）で活躍する。",
              ["者", "人", "線", "陣"], 3,
              "Moda olamining oldingi saflarida (birinchi chizig'ida) faoliyat yuritadi.",
              expl="第一線 (だいいっせん) = eng oldingi saf, yetakchi pozitsiya"),
            q("t8-v3-12", "あなたの国の住所ではなく、今住んでいる（　）住所を書いてください。",
              ["現", "今", "在", "再"], 1,
              "O'z vataningizdagi manzilni emas, hozir yashab turgan joriy manzilingizni yozing.",
              expl="現住所 (げんじゅうしょ) = hozirgi yashash manzili"),
            q("t8-v3-13", "よく山に登るが、（　）天候になったらすぐ引き返すことにしている。",
              ["雨", "荒", "悪", "激"], 3,
              "Tog'ga ko'p chiqaman, biroq yomon ob-havo bo'lsa darhol ortga qaytishni qoida qilganman.",
              expl="悪天候 (あくてんこう) = noqulay/yomon ob-havo"),
            q("t8-v3-14", "この乗り物は安全（　）での問題がある。",
              ["値", "面", "感", "下"], 2,
              "Ushbu transport vositasida xavfsizlik jihatidan muammo mavjud.",
              expl="安全面 (あんぜんめん) = xavfsizlik jihati/tomoni"),
            q("t8-v3-15", "彼はだぶだぶで（　）格好な服を着ている。",
              ["反", "非", "悪", "不"], 4,
              "U xaltadek osilgan noqulay va beo'xshov kiyim kiyib olgan.",
              expl="不格好 (ぶかっこう) = beo'xshov, xunuk, beo'rin")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t8-v4-16", "先日、彼を両親に紹介しました。（　）結婚式をあげるつもりです。",
              ["着々", "近々", "急に", "にわかに"], 2,
              "Kuni kecha uni ota-onamga tanishtirdim. Yaqin kunlarda to'y o'tkazmoqchimiz.",
              reading="ちかぢか", expl="近々 (ちかぢか) = yaqinda, tez kunlarda"),
            q("t8-v4-17", "50代という年齢の（　）をものともせず、再就職が決まった。",
              ["バンク", "ハント", "ハンデ", "ハンター"], 3,
              "50 yoshdagi noqulaylikni (yosh to'sig'ini) pisand qilmay, qayta ishga joylashishi hal bo'ldi.",
              expl="ハンデ (handicap) = noqulaylik, kamchilik, to'siq"),
            q("t8-v4-18", "仕事でも勉強でも我を忘れるほど夢中になることそのものに、喜びを（　）。",
              ["震える", "越える", "支える", "覚える"], 4,
              "Ishda ham, o'qishda ham o'zini unutadigan darajada berilib ketishning o'zidan katta quvonch his qilaman.",
              reading="おぼえる", expl="（喜びを）覚える = quvonch/hissiyot tuyg'usini his qilmoq"),
            q("t8-v4-19", "世界の（　）7カ国が集まって、国際会議が開かれた。",
              ["重要", "主要", "重大", "長大"], 2,
              "Dunyoning yetakchi 7 ta davlati (Katta yettilik) yig'ilib, xalqaro anjuman o'tkazildi.",
              reading="しゅよう", expl="主要 (しゅよう) = asosiy, yetakchi"),
            q("t8-v4-20", "人のものを欲しがるなんて、（　）まねはやめなさい。",
              ["だらしない", "もったいない", "みっともない", "ものすごい"], 3,
              "Birovning narsasiga ko'z olaytirish kabi uyatli (sharmandali) qiliqni bas qil.",
              reading="みっともない", expl="みっともない = xunuk, sharmandali, uyatli"),
            q("t8-v4-21", "まだたっぷり時間があると（　）していたため、今レポートの締め切りに追われて大変です。",
              ["油断", "怠慢", "停止", "休暇"], 1,
              "Hali vaqt bemalol deb beparvolik (xotirjamlik) qilganim sababli, hozir hisobot muddati yetib kelib qiyin ahvoldaman.",
              reading="ゆだん", expl="油断 (ゆだん) = xotirjamlikka berilish, hushyorlikni yo'qotish"),
            q("t8-v4-22", "つる性の植物で日陰を作って電気代を（　）する。",
              ["減少", "縮小", "節約", "解約"], 3,
              "Chirmashuvchi o'simliklar bilan soya hosil qilib elektr energiyasi xarajatini tejaymiz.",
              reading="せつやく", expl="節約 (せつやく) = tejash, iqtisod qilish")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t8-v5-23", "彼は信頼するに【足りる】人物だ。",
              ["不安な", "十分な", "危うい", "問題の"], 2,
              "U ishonch bildirishga arziydigan (yetarli darajada ishonchli) inson.",
              reading="たりる", expl="足りる ≈ 十分な (yetarli bo'lgan, arziydigan)"),
            q("t8-v5-24", "祭りに集まる観光客は、【ざっと】十万人だろう。",
              ["おおよそ", "おそらく", "少なくとも", "多ければ"], 1,
              "Bayramga yig'iladigan sayyohlar taxminan 100 ming kishini tashkil qilsa kerak.",
              reading="ざっと", expl="ざっと ≈ おおよそ (taxminan, chamasi)"),
            q("t8-v5-25", "その行動は法律に【触れる】。",
              ["よっている", "基づく", "違反する", "合っている"], 3,
              "Bu harakat qonunbuzarlik hisoblanadi (qonunga zid).",
              reading="ふれる", expl="（法に）触れる ≈ 違反する (qonunni buzmoq, ziddiyat keltirib chiqarmoq)"),
            q("t8-v5-26", "お寺のふすまの絵は【架空の】動物だ。",
              ["信仰上の", "不思議な", "特殊な", "想像上の"], 4,
              "Ibodatxona eshigidagi rasmda to'qima (xayoliy) hayvon tasvirlangan.",
              reading="かくうの", expl="架空 ≈ 想像上 (xayoliy, to'qima, hayotda yo'q)"),
            q("t8-v5-27", "大学ごとに、その学校の【カラー】というものがある。",
              ["規則", "特色", "方針", "伝統"], 2,
              "Har bir universitetning o'ziga xos xarakteri / o'ziga xosligi (rangi) bo'ladi.",
              expl="カラー ≈ 特色 (o'ziga xos xususiyat, xarakter)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'zning gapda eng to'g'ri ishlatilgan variantini tanlang.",
          "questions": [
            q("t8-v6-28", "【警告】の使い方として最もよいものを選びなさい。",
              [
                "電車の中で騒いでいる子どもにだれも警告しなかった。",
                "彼は他人の間違いばかり警告するいやな人間だ。",
                "世界各地の気候変化は人類に地球の異常を警告している。",
                "二度とこのような失敗をしないよう警告してまいります。"
              ], 3,
              "警告 (keikoku) = ogohlantirish, ogohlikka chaqirish.",
              expl="「気候変化は地球の異常を警告している」= iqlim o'zgarishi insoniyatni yer shari xavfidan ogohlantirmoqda (to'g'ri ishlatilish)."),
            q("t8-v6-29", "【つながり】の使い方として最もよいものを選びなさい。",
              [
                "大企業につながりの子会社に入社した。",
                "来月工事が完成すると道路はつながりになる。",
                "子どもたちは手をつながりながら歩いている。",
                "彼は夫の兄で、私とは血のつながりはない。"
              ], 4,
              "つながり (tsunagari) = bog'liqlik, qarindoshlik/aloqa munosabati.",
              expl="「血のつながりはない」= qon-qarindoshlik aloqasi yo'q (to'g'ri ishlatilish)."),
            q("t8-v6-30", "【余計】の使い方として最もよいものを選びなさい。",
              [
                "今年の会費の余計は来年に回しますのでよろしく。",
                "会社の経営がうまくいっていないという証拠は余計にある。",
                "ついひと言余計なことを言って、上司を怒らせてしまった。",
                "お金なら余計にあるのでどうぞご心配しないでください。"
              ], 3,
              "余計 (yokei) = ortiqcha, keraksiz.",
              expl="「余計なことを言って」= ortiqcha gap aytib yuborib... (to'g'ri ishlatilish)."),
            q("t8-v6-31", "【世間】の使い方として最もよいものを選びなさい。",
              [
                "法律上は罪にならないが、世間が許しません。",
                "大人になったら広い世間を旅行してみたい。",
                "退職したら畑仕事でもしてのんびり世間を送りたい。",
                "若者の世間ではそんなことは常識だそうだ。"
              ], 1,
              "世間 (seken) = jamiyat, jamoatchilik, el-yurt qarashi.",
              expl="「世間が許しません」= jamoatchilik (el-yurt) kechirmaydi (to'g'ri ishlatilish)."),
            q("t8-v6-32", "【交代】の使い方として最もよいものを選びなさい。",
              [
                "テレビが故障したので、新しいものと交代した。",
                "昼と夜姉妹で交代しながら、母の看病をした。",
                "このぼくの本と君の本を交代しないか。",
                "彼は文系志望だったのだが、理系に交代した。"
              ], 2,
              "交代 (koutai) = navbatlashish, almashib turish.",
              expl="「姉妹で交代しながら」= opa-singillar navbatlashib... (to'g'ri ishlatilish).")
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
            q("t8-g1-33", "家族全員が集まって、まるで正月が（　）のようだ。",
              ["来るか", "来たか", "来つつ", "来ないか"], 2,
              "Oilaning barcha a'zolari to'planib, go'yo Yangi yil bayrami kelgandek bo'ldi.",
              expl="「まるで〜かのようだ」= go'yo xuddi ...dek (tashbeh ifodasi)."),
            q("t8-g1-34", "A「おさしみの切り方を教えて。」\\nB「まず、ほうちょうの持ち方から（　）間違っているよ。」",
              ["して", "すれば", "したら", "しないと"], 1,
              "A: «Sashimi to'g'rashni o'rgating.» — B: «Avvalo, pichoqni ushlashingizdan boshlab noto'g'ri-ku.»",
              expl="「〜からして」= ...dan boshlab hatto (eng asosiy/boshlang'ich nuqtadan misol keltirish)."),
            q("t8-g1-35", "あなたにはおこづかいでも、私（　）10万円は大金です。",
              ["によっては", "にとっては", "については", "にかけては"], 2,
              "Siz uchun cho'ntak puli bo'lishi mumkin, lekin men uchun 100 ming iyen katta pul.",
              expl="「〜にとって（は）」= ...shaxs uchun, ...nuqtai nazaridan."),
            q("t8-g1-36", "いくら北海道でも8月に雪が降るなんて、（　）。",
              ["あり得る", "あり得ない", "あるらしい", "ありそうだ"], 2,
              "Hatto Xokkaydo bo'lsa ham, avgustda qor yog'ishi mumkin bo'lmagan hodisadir.",
              expl="「〜得ない（えない）」= bo'lishi mumkin emas / imkonsiz."),
            q("t8-g1-37", "リンさんは教授に厳しく指導され、（　）になっていた。",
              ["泣くよう", "泣くそう", "泣いたよう", "泣きそう"], 4,
              "Lin professordan qattiq tanbeh olib, yig'lab yuboray degan holatda edi.",
              expl="「動詞ます形 ＋ そう」= ...holatga tushay degan (hozir sodir bo'lish arafasida)."),
            q("t8-g1-38", "結婚したら法律（　）男女どちらの姓になってもよいが、95％が男性の姓になっている。",
              ["上は", "中は", "下は", "間は"], 1,
              "Turmush qurgach qonun jihatidan er yoki xotin familiyasini olish mumkin bo'lsa-da, 95% holatda erkakning familiyasi olinadi.",
              expl="「〜上（は）」= ...nuqtai nazaridan / rasmiy me'yor jihatidan."),
            q("t8-g1-39", "A「社長、山本さまと（　）が見えましたが。」\\nB「こちらにお通ししてくれ。」",
              ["申される方が", "言っている方が", "おっしゃる方が", "呼ばれる方が"], 3,
              "A: «Direktor janoblari, Yamamoto degan shaxs keldilar.» — B: «Bu yerga taklif qiling.»",
              expl="「〜とおっしゃる方」= ...deb aytuvchi shaxs (hurmat shakli)."),
            q("t8-g1-40", "よく問題を読まなかったせいで、答えを（　）。",
              ["間違えてしまった", "間違えずにすんだ", "間違えるはずだった", "間違えようがなかった"], 1,
              "Savolni yaxshilab o'qimaganim sababli javobni xato belgilab qo'ydim.",
              expl="「〜せいで」salbiy oqibat bilan birga keladi → 間違えてしまった."),
            q("t8-g1-41", "熱が高いのに無理をして学校に（　）、休んだほうがいいよ。",
              ["行かないままなら", "行くままなら", "行かないくらいなら", "行くくらいなら"], 4,
              "Isitma baland bo'lib turib majburlab maktabga borgandan ko'ra, uyda dam olganing ma'qul.",
              expl="「〜くらいなら」= ...qilgandan ko'ra (yomonroq variantni qiyoslash)."),
            q("t8-g1-42", "いくら生活に困っているからと言って、まじめな彼が盗み（　）。",
              ["をするはずがない", "をしないはずがない", "をすることもない", "をしないこともない"], 1,
              "Qanchalik qiyin ahvolda yashayotgan bo'lmasin, vijdonli u insonning o'g'irlik qilishi aslo mumkin emas.",
              expl="「〜はずがない」= mutlaqo bo'lishi mumkin emas / aslo unday emas."),
            q("t8-g1-43", "歌手になることを両親に反対されて大学に進学したが、夢を（　）いる。",
              ["捨てかねないで", "捨てようかと思って", "捨てきれないで", "捨てたがって"], 3,
              "Xonanda bo'lishimga ota-onam qarshi bo'lib universitetga kirgan bo'lsam-da, orzuyimdan butunlay voz kecha olmayapman.",
              expl="「〜きれない」= oxirigacha / butunlay qila olmaslik."),
            q("t8-g1-44", "税金を自分のために使った市長は、市民の力によって（　）。",
              ["やめられることになった", "やめてあげることになった", "やめさせてもらうことになった", "やめさせられることになった"], 4,
              "Soliq pullarini o'z manfaati uchun sarflagan shahar hokimi fuqarolarning bosimi natijasida lavozimidan chetlatildi (majburiy ketkazildi).",
              expl="「〜させられる」= majburlanmoq (majhul-istak shakli) + 「〜ことになる」.")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の＿★＿に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keladigan eng to'g'ri variantni tanlang.",
          "questions": [
            q("t8-g2-45", None,
              ["会社に", "入ってくる", "会社の", "たび"], 2,
              "Yangi xodim kompaniyaga kelgan har gal kompaniya qoidalarini o'rgatib qo'yish kerak.",
              prefix="新しい社員が", suffix="規則を教えてやらなければいけない。",
              starPos=2, order=[1, 2, 4, 3],
              expl="Tartib: 会社に(1) 入ってくる(2) たび(4) 会社の(3) → Yulduzcha 2-o'rinda: 入ってくる(2)"),
            q("t8-g2-46", None,
              ["待たされて", "加えて", "次々と", "長い時間"], 4,
              "Bu jaziramaga qo'shimcha ravishda uzoq vaqt kuttirilib, ketma-ket yiqilib tushganlar bo'ldi.",
              prefix="この暑さに", suffix="倒れる人が出た。",
              starPos=2, order=[2, 4, 1, 3],
              expl="Tartib: 加えて(2) 長い時間(4) 待たされて(1) 次々と(3) → Yulduzcha 2-o'rinda: 長い時間(4)"),
            q("t8-g2-47", None,
              ["も", "が", "逃げように", "逃げ道"], 1,
              "Ko'z o'ngimda ayiq paydo bo'ldi, orqam esa vodiy bo'lib, qochishga yo'l ham yo'qligidan shoshilib daraxtga chiqdim.",
              prefix="目の前に熊がいたが、後ろは谷で", suffix="なく、あわてて木に登った。",
              starPos=2, order=[3, 1, 4, 2],
              expl="Tartib: 逃げように(3) も(1) 逃げ道(4) が(2) → Yulduzcha 2-o'rinda: も(1)"),
            q("t8-g2-48", None,
              ["間違い", "名前", "だらけで", "だけが"], 2,
              "Bu inshodagi kanjilar xatolarga to'la bo'lib, faqatgina ismi to'g'ri kanjida yozilgan.",
              prefix="この作文の漢字は", suffix="正しい漢字で書けている。",
              starPos=3, order=[1, 3, 2, 4],
              expl="Tartib: 間違い(1) だらけで(3) 名前(2) だけが(4) → Yulduzcha 3-o'rinda: 名前(2)"),
            q("t8-g2-49", None,
              ["と", "から", "言っても", "必ず"], 3,
              "Zamonaviy davrda universitetni tamomlagan bilan har doim ham ish topish kafolatlangan emas.",
              prefix="現代は大学を出た", suffix="就職できない時代だ。",
              starPos=3, order=[2, 1, 3, 4],
              expl="Tartib: から(2) と(1) 言っても(3) 必ず(4) → Yulduzcha 3-o'rinda: 言っても(3)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlarga eng mos keluvchi javobni tanlang.",
          "passage": "どの時代にも、かならず流行語【 50 】。\n　たとえば「サボる」などということばは、もうすっかり普通になってしまったが、あれはもともと「サボタージュ（注1）」からきている。\n　それから、「セコい」ということば、あれはもともとは「セコンドハンド（注2）」という外来語から出たことばである、その略語（注3）である「セコハン」を経由（注4）して、「セコハン」は、多くの場合「【 51-a 】古物」という意味だから、「あいつが着ているものは、どうもセコイ」というのはよっぽど古いもの、【 51-b 】ものを着ているという意味になった。そこから「けちんぼう」という意味が派生（注5）してきて、「お前、セコイこと言うなよ」みたいに使われるようになったのである。\n　このように、ことばとしてどんどん市民権を獲得してしまったことばもあるのである。今「サボる」「セコい」と聞いても、それが【 52 】だと思う人などほとんどいないかもしれない。\n　いまでは、ひらがなで「さぼる」「せこい」と書くようにさえなったから、もはや日本語【 53 】。けれども、日本語の語彙として定着するまでにはやはり時間が必要である。さぼる、せこい、などでもおそらく出現してから五十年以上は経っているように想像される。\n　したがって、まだ定着しないうちの、生な流行語のようなものはやはり、【 54 】のが上品な話し方だと言えるのである。\n（林望『日本語は死にかかっている』NTT出版）",
          "questions": [
            q("t8-g3-50", None,
              ["といったわけがある", "というわけがある", "といったことがある", "というものがある"], 4,
              "Har qanday zamonda albatta urf bo'lgan so'zlar (sleng/moda iboralar) mavjud bo'ladi.",
              blankNo=50, expl="「〜というものがある」= ...kabi narsa/hodisa mavjud bo'ladi."),
            q("t8-g3-51", None,
              ["a 高い ／ b 安い", "a 安いらしい ／ b 高いらしい", "a 高いような ／ b 安いような", "a 安っぽい ／ b 安っぽい"], 4,
              "a: 安っぽい (arzonbaho ko'rinishdagi), b: 安っぽい (arzonbaho).",
              blankNo=51, expl="51-a va 51-b ikkalasiga ham «安っぽい» (arzonbaho, sifatsiz) mos tushadi."),
            q("t8-g3-52", None,
              ["日本語", "外来語", "流行語", "略語"], 2,
              "Hozir «saboru» yoki «sekoi» so'zlarini eshitib ularni o'zlashma so'z (gairaigo) deb o'ylaydigan odam deyarli yo'q.",
              blankNo=52, expl="「外来語 (gairaigo)」= chet tilidan kirib kelgan o'zlashma so'z."),
            q("t8-g3-53", None,
              ["として完全に忘れ去られたのだろう", "としてすっかり定着したのであろう", "としてはけっして使えないだろう", "とはまったく言えないだろう"], 2,
              "...yapon tili sifatida butunlay mustahkam o'rnashib qolgan bo'lsa kerak.",
              blankNo=53, expl="「日本語としてすっかり定着したのであろう」= yapon tili sifatida to'liq singib ketgan bo'lsa kerak."),
            q("t8-g3-54", None,
              ["できるだけ使う", "できれば使う", "できるかぎり使わない", "少しは使ってみる"], 3,
              "Shuning uchun, hali to'liq singib ketmagan xom yangi iboralarni imkon qadar ishlatmaslik madaniyatli nutq uslubi hisoblanadi.",
              blankNo=54, expl="「できるかぎり使わない」= imkon qadar ishlatmaslik.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK! test08.json yaratildi: {len(data['sections'][0]['problems'])} vocab + {len(data['sections'][1]['problems'])} grammar bo'limlari.")
