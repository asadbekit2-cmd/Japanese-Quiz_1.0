# -*- coding: utf-8 -*-
"""
test15.json generatori — 第15回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.16, Savollar p.148-157
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test15.json")

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
  "id": 15,
  "title_jp": "第15回 模擬テスト",
  "title_uz": "15-test",
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
            q("t15-v1-1", "朝食をとると睡眠中に【低下】した体温が上がるので、午前中の集中力が高まる。",
              ["ていか", "ていが", "ていげ", "でいが"], 1,
              "Nonushta qilganda uyqu paytida pasaygan tana harorati ko'tariladi, shuning uchun tushgacha bo'lgan diqqat-e'tibor oshadi.",
              reading="ていか", expl="低下 → ていか (pasayish, tushish)"),
            q("t15-v1-2", "手抜き工事のせいで、家の床が歩くと【沈む】。",
              ["しずむ", "ひずむ", "すすむ", "ゆがむ"], 1,
              "Sifatsiz qurilish tufayli, uyning poli yurganda cho'kadi (o'tirib qoladi).",
              reading="しずむ", expl="沈む → しずむ (cho'kmoq, pasaymoq)"),
            q("t15-v1-3", "景気の回復は就職活動中の学生にとって最大の【関心事】である。",
              ["かんじんじ", "がんじんじ", "かんしんじ", "かんじんし"], 3,
              "Iqtisodiyotning tiklanishi ish qidirayotgan talabalar uchun eng katta qiziqish / diqqat markazidagi masaladir.",
              reading="かんしんじ", expl="関心事 → かんしんじ (qiziqish mavzusi, e'tibor qaratilgan masala)"),
            q("t15-v1-4", "異常気象による【農産物】の被害が各地で起きている。",
              ["のうさんぶつ", "のうざんふつ", "のうさんもつ", "のうさくもつ"], 1,
              "Anormal ob-havo tufayli qishloq xo'jaligi mahsulotlarining nobud bo'lishi har yerda sodir bo'lmoqda.",
              reading="のうさんぶつ", expl="農産物 → のうさんぶつ (qishloq xo'jaligi mahsulotlari)"),
            q("t15-v1-5", "赤ちゃん用おもちゃの安全【基準】は厳し過ぎることはない。",
              ["きてい", "きそく", "きじゅん", "きはん"], 3,
              "Chaqaloqlar o'yinchoqlarining xavfsizlik standarti haddan tashqari qat'iy bo'lishi ortiqchalik qilmaydi.",
              reading="きじゅん", expl="基準 → きじゅん (standart, me'yor)")
          ]
        },
        {
          "id": "v2", "type": "kanji_writing",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zni kanjida yozish uchun eng to'g'risini tanlang.",
          "questions": [
            q("t15-v2-1", "心の病は病名を【しんだん】するのさえ非常に難しい。",
              ["診断", "侵断", "審断", "信断"], 1,
              "Ruhiy kasalliklarga hatto tashxis qo'yishning o'zi ham nihoyatda qiyindir.",
              reading="しんだん", expl="診断 → しんだん (tashxis, tibbiy ko'rik)"),
            q("t15-v2-2", "劇場で、大きな荷物や上着をクロークに【あずける】。",
              ["項ける", "預ける", "領ける", "頂ける"], 2,
              "Teatrda katta yuk va ustki kiyimni kiyimxonaga (saqlash joyiga) topshiraman.",
              reading="あずける", expl="預ける → あずける (saqlashga topshirmoq, berib turmoq)"),
            q("t15-v2-3", "あの子はいかにも【りこう】そうだ。",
              ["利行", "利効", "利口", "利硬"], 3,
              "U bola juda ham aqlli (ziyrak) ko'rinadi.",
              reading="りこう", expl="利口 → りこう (aqlli, zehnli, ziyrak)"),
            q("t15-v2-4", "新入社員の【けんしゅう】は入社後一カ月行う。",
              ["研修", "検修", "研習", "検習"], 1,
              "Yangi xodimlarning malaka oshirish mashg'uloti ishga kirgach bir oy davomida o'tkaziladi.",
              reading="けんしゅう", expl="研修 → けんしゅう (malaka oshirish, stajirovka, trening)"),
            q("t15-v2-5", "昨夜宝石店で2億円相当の商品が何者かに【ぬすまれた】。",
              ["除まれた", "奪まれた", "詐まれた", "盗まれた"], 4,
              "Kecha tunda zargarlik do'konidan 200 million yenlik tovarlar noma'lum kimsalar tomonidan o'g'irlab ketildi.",
              reading="ぬすまれた", expl="盗む → ぬすむ (o'g'irlamoq; 盗まれた = o'g'irlandi)")
          ]
        },
        {
          "id": "v3", "type": "word_formation",
          "instruction_jp": "（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga qo'yish uchun eng to'g'ri so'z yasovchi qo'shimchani tanlang.",
          "questions": [
            q("t15-v3-1", "あの政治家はかつて（【反】）体制運動のリーダーだった。",
              ["新", "現", "反", "前"], 3,
              "U siyosatchi bir paytlar tuzumga qarshi harakatning yetakchisi edi.",
              expl="反体制 → はんたいせい (tuzumga/rejimga qarshi)"),
            q("t15-v3-2", "部長はとても自信（【家】）だ。",
              ["屋", "家", "人", "者"], 2,
              "Bo'lim boshlig'i o'ziga juda ishongan inson.",
              expl="自信家 → じしんか (o'ziga qattiq ishongan odam)"),
            q("t15-v3-3", "火山灰の被害は（【広】）範囲におよんだ。",
              ["大", "多", "広", "全"], 3,
              "Vulqon kuli keltirgan zarar keng ko'lamli hududga yoyildi.",
              expl="広範囲 → こうはんい (keng qamrovli, keng hudud)"),
            q("t15-v3-4", "面接で相手に（【好】）印象を与えるスーツを選ぶ。",
              ["良", "好", "優", "善"], 2,
              "Suhbatda qarshi tomonda ijobiy taassurot qoldiradigan kostyum tanlayman.",
              expl="好印象 → こういんしょう (yaxshi/ijobiy taassurot)"),
            q("t15-v3-5", "彼は少年（【期】）のほとんどを海外で過ごした。",
              ["期", "代", "性", "時"], 1,
              "U o'smirlik davrining aksar qismini chet elda o'tkazdi.",
              expl="少年期 → しょうねんき (o'smirlik/bolalik davri)")
          ]
        },
        {
          "id": "v4", "type": "context_vocab",
          "instruction_jp": "（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gap mazmuniga mos keluvchi eng to'g'ri so'zni tanlang.",
          "questions": [
            q("t15-v4-1", "失業者が増えると犯罪も増える。（【ようするに】）不景気が犯罪の原因と言える。",
              ["ようするに", "そういえば", "おたがいに", "ようやく"], 1,
              "Ishsizlar ko'paysa jinoyat ham ko'payadi. Qisqasi, iqtisodiy inqiroz jinoyatning sababi deb aytish mumkin.",
              expl="要するに → ようするに (qisqasi, xullas)"),
            q("t15-v4-2", "子どものころからこわれたおもちゃを（【修理】）したり、何かを組み立てたりするのが得意だった。",
              ["訂正", "修正", "修理", "治療"], 3,
              "Bolaligimdan buzilgan o'yinchoqlarni ta'mirlash yoki biror narsa yasashga usta edim.",
              expl="修理 → しゅうり (ta'mirlash, tuzatish)"),
            q("t15-v4-3", "狭き門を（【勝ち抜いて】）、人気の会社に就職できた。",
              ["打ち抜いて", "出し抜いて", "引き抜いて", "勝ち抜いて"], 4,
              "Katta raqobatdan g'alaba bilan o'tib, mashhur kompaniyaga ishga kirdi.",
              expl="勝ち抜く → かちぬく (raqobatda g'olib chiqmoq)"),
            q("t15-v4-4", "コンピューターウイルスが、ネットワークに不正に（【侵入】）した。",
              ["進入", "侵入", "加入", "移入"], 2,
              "Kompyuter virusi tarmoqqa noqonuniy ravishda kirib oldi.",
              expl="侵入 → しんにゅう (bostirib kirish, ruxsatsiz suqilib kirish)"),
            q("t15-v4-5", "人と人との結び付きを大切にする彼は、チームのまとめ役に（【ふさわしい】）人物だ。",
              ["うらやましい", "にくらしい", "なつかしい", "ふさわしい"], 4,
              "Odamlar o'rtasidagi munosabatlarni qadrlaydigan u inson jamoa yetakchisi roliga munosib shaxsdir.",
              expl="ふさわしい (munosib, loyiq, mos)"),
            q("t15-v4-6", "1人で困難な仕事をやりとげた経験は、私の人生の（【プラス】）になった。",
              ["アップ", "ダウン", "プラス", "ダブル"], 3,
              "Qiyin ishni bir o'zim uddalagan tajribam mening hayotim uchun katta yutuq bo'ldi.",
              expl="プラス (foyda, yutuq, ijobiy tajriba)"),
            q("t15-v4-7", "この会社が女性に人気なのは、託児所が（【完備】）され子どもを預けて働けるからだ。",
              ["設備", "完備", "建設", "整理"], 2,
              "Bu kompaniya ayollar orasida mashhurligining sababi — bolalar bog'chasi to'liq jihozlangan bo'lib, bolani topshirib ishlash mumkin.",
              expl="完備 → かんび (to'liq jihozlanganlik)")
          ]
        },
        {
          "id": "v5", "type": "paraphrase",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t15-v5-1", "ネット犯罪に対する意識が【薄い】人は多い。",
              ["不十分な", "不正確な", "不明な", "不透明な"], 1,
              "Internet jinoyatlariga nisbatan ogohlik darajasi yetarli bo'lmagan odamlar ko'p.",
              expl="意識が薄い ＝ 不十分な（ふじゅうぶんな） (yetarli bo'lmagan)"),
            q("t15-v5-2", "この曲を聞くたびに、川の流れを【連想する】。",
              ["思い当たる", "思い上がる", "思い浮かべる", "思い出す"], 3,
              "Bu qo'shiqni eshitgan sayin daryo oqimini ko'z oldimga keltiraman.",
              expl="連想する（れんそうする）＝ 思い浮かべる（おもいうかべる） (xayolga keltirmoq)"),
            q("t15-v5-3", "【万一】地震があっても、荷物を持ち出せるように準備している。",
              ["だから", "やがて", "どんな", "もしも"], 4,
              "Mabodo zilzila bo'lib qolsa ham buyumlarni olib chiqib keta oladigan qilib tayyorlab qo'yganman.",
              expl="万一（まんいち）＝ もしも (mabodo, bordiyu)"),
            q("t15-v5-4", "木村先輩はサークル活動に【いちいち】口を出す。",
              ["細かく", "少しは", "最初から", "勝手に"], 1,
              "Kimura senpay to'garak faoliyatiga har bir mayda narsagacha burnini suqadi.",
              expl="いちいち ＝ 細かく（こまかく） (maydalashib, har bir narsaga)"),
            q("t15-v5-5", "今年は過去最高の【速度】で交通事故の死者が増えている。",
              ["ベース", "ペース", "メーター", "パーセント"], 2,
              "Bu yil o'tmishdagi eng yuqori sur'atda yo'l-transport hodisasida vafot etganlar soni oshmoqda.",
              expl="速度（そくど）＝ ペース (sur'at, tezlik)")
          ]
        },
        {
          "id": "v6", "type": "usage",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'z qaysi gapda eng to'g'ri ma'noda ishlatilganini tanlang.",
          "questions": [
            q("t15-v6-1", "【みじめ】",
              [
                "親友が交通事故で亡くなったというみじめなお知らせを受け取った。",
                "息子が口答えしたら母はみじめな顔をした。",
                "彼は事業に失敗し、今ではみじめな生活をしているという。",
                "犯罪が低年齢化しているとは、なんとみじめなことだ。"
              ], 3,
              "U biznesda inqirozga uchrab, hozirda achinarli hayot kechirayotgan ekan.",
              expl="みじめ（惨め）— achinarli, ayanchli, xor holat. 3-gap to'g'ri.",
              optsTr=[
                "Yaqin do'stim vafot etgani haqida ayanchli xabar oldim (xato).",
                "O'g'li gap qaytargach ona ayanchli yuz qildi (xato).",
                "U biznesda inqirozga uchrab, hozirda achinarli hayot kechirayotgan ekan.",
                "Jinoyat yosharib borayotgani naqadar ayanchli ish (xato)."
              ]),
            q("t15-v6-2", "【具合】",
              [
                "最近は経済の具合が悪いので仕事が少ない。",
                "頭の具合がよくないといい考えが浮かばない。",
                "政治の具合がよくならないと国民の生活も大変だ。",
                "車のエンジンの具合が悪くて、変な音がする。"
              ], 4,
              "Mashina motorining ishlash holati yomonlashib, g'alati ovoz chiqaryapti.",
              expl="具合（ぐあい）— tana yoki texnikaning ishlash holati/ahvoli. 4-gap to'g'ri.",
              optsTr=[
                "So'nggi paytlarda iqtisod holati yomon (xato).",
                "Bosh holati yaxshi bo'lmasa yaxshi fikr kelmaydi (xato).",
                "Siyosat holati yaxshilanmasa fuqarolar hayoti ham qiyin (xato).",
                "Mashina dvigatelining holati yomon bo'lib, g'alati ovoz chiqmoqda."
              ]),
            q("t15-v6-3", "【世の中】",
              [
                "子どもが世の中に目を覚ますことが多く寝不足気味だ。",
                "動物の世の中は力の関係がはっきりしている。",
                "そんな甘い考えでは世の中渡っていけない。",
                "彼は若くして政治の世の中に入った。"
              ], 3,
              "Bunday xomxayol fikrlar bilan jamiyatda yashab ketolmaysan.",
              expl="世の中（よのなか）— insonlar jamiyati; 世の中を渡る = hayotda yashab o'tmoq. 3-gap to'g'ri.",
              optsTr=[
                "Bola jamiyatda ko'zini ochib uyqusizlik bo'lyapti (xato, 夜中 ishlatiladi).",
                "Hayvonlar jamiyati kuchlar munosabati aniq (xato, 世界 ishlatiladi).",
                "Bunday xomxayol fikrlar bilan jamiyatda yashab ketolmaysan.",
                "U yoshligidan siyosat jamiyatiga kirdi (xato, 政界 ishlatiladi)."
              ]),
            q("t15-v6-4", "【雑音】",
              [
                "道路工事の雑音がして一晩中眠れなかった。",
                "このラジオは雑音がひどくて、声が聞き取りにくい。",
                "飛行場の近くの住民は、飛行機の雑音に悩まされている。",
                "私の母は細かいことまで雑音を言う。"
              ], 2,
              "Bu radioning shovqini (xirillashi) kuchli bo'lib, ovoz yaxshi eshitilmayapti.",
              expl="雑音（ざつおん）— apparatlar yoki radioning g'ashga teguvchi xirillash shovqini. 2-gap to'g'ri.",
              optsTr=[
                "Yo'l qurilishi xirillashi sabab uxlolmadim (xato, 騒音 ishlatiladi).",
                "Bu radioning shovqini (xirillashi) kuchli bo'lib, ovoz yaxshi eshitilmayapti.",
                "Aeroport yaqinidagi aholi samolyot shovqinidan qiynalmoqda (xato, 騒音 ishlatiladi).",
                "Onam mayda narsalargacha xirillash aytadi (xato, 小言 ishlatiladi)."
              ]),
            q("t15-v6-5", "【拡張】",
              [
                "あっという間に彼らの結婚のうわさが拡張した。",
                "海外事業を拡張するため、社員を募集する。",
                "山頂に着くと目の前に美しい景色が拡張した。",
                "ペットの写真を拡張して、部屋に飾った。"
              ], 2,
              "Chet eldagi biznesni kengaytirish uchun yangi xodimlarni qabul qilmoqda.",
              expl="拡張（かくちょう）— ko'lam yoki maydonni kengaytirish. 2-gap to'g'ri.",
              optsTr=[
                "Tezda ularning to'yi haqidagi mish-mish kengaydi (xato, 広まった ishlatiladi).",
                "Chet eldagi biznesni kengaytirish uchun xodimlarni qabul qilmoqda.",
                "Tog' cho'qqisiga chiqqach go'zal manzara kengaydi (xato, 広がった ishlatiladi).",
                "Uy hayvoni rasmini kengaytirib xonaga qo'ydi (xato, 拡大して ishlatiladi)."
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
            q("t15-g1-1", "「野球の名門」という名前に（【かけても】）、ぜひ我が校が優勝したいものだ。",
              ["とっても", "かけても", "ついても", "よっても"], 2,
              "'Beysbol dargohi' degan nomimiz sha'niga qasamki, maktabimiz albatta g'alaba qozonishini istayman.",
              expl="〜にかけて（も）— ...ning sha'ni yoki obro'sini o'rtaga qo'yib."),
            q("t15-g1-2", "彼は大金持ちの（【くせに】）けちで、払うべき金もなかなか払わない。",
              ["せいで", "ために", "くせに", "あまり"], 3,
              "U boyvachcha bo'la turib shunaqangi xasiski, to'lashi kerak bo'lgan pulni ham sira to'lamaydi.",
              expl="〜くせに — ...bo'la turib (norozilik va tanqidiy urg'u)."),
            q("t15-g1-3", "10年ぶりに息子の顔を見た母は、人目（【もかまわず】）息子を抱きしめた。",
              ["によらず", "にかかわらず", "を問わず", "もかまわず"], 4,
              "10 yildan so'ng o'g'lining yuzini ko'rgan ona odamlarning nigohiga ham parvo qilmay o'g'lini bag'riga bosdi.",
              expl="〜もかまわず — ...ga ham parvo qilmay, e'tibor bermasdan."),
            q("t15-g1-4", "たばこに（【火をつけた】）とたんに、大きな音とともに部屋が爆発した。",
              ["火をつけている", "火をつける", "火をつけそうな", "火をつけた"], 4,
              "Sigaretga o't yoqqan zahoti baland ovoz bilan xona portlab ketdi.",
              expl="動詞タ形＋とたんに — ...qilgan zahotiyoq."),
            q("t15-g1-5", "この件に関しては、上司に確認して（【からでないと】）お答えできません。",
              ["からでないと", "からすると", "からといって", "からして"], 1,
              "Bu masala bo'yicha rahbardan aniqlashtirib olmaguncha javob bera olmayman.",
              expl="〜てからでないと（〜できない）— ...qilmaguncha (keyingisini qilib bo'lmaydi)."),
            q("t15-g1-6", "こんなごみ（【だらけ】）の家には、はずかしくてお客さんが呼べない。",
              ["だらけ", "ばかり", "だけ", "のみ"], 1,
              "Bunday axlatga to'la uyga uyalganimdan mehmon ham chaqira olmayman.",
              expl="〜だらけ — ...ga to'la, bosib ketgan (salbiy narsalar uchun)."),
            q("t15-g1-7", "これはワイン（【というより】）、むしろぶどうジュースに近い味だ。",
              ["というより", "としたら", "とするなら", "といっては"], 1,
              "Bu vino degandan ko'ra ko'proq uzum sharbatiga yaqin ta'mga ega.",
              expl="〜というより（むしろ）— ...degandan ko'ra ko'proq."),
            q("t15-g1-8", "あの男は金のためなら、友人だって裏切り（【かねない】）。",
              ["かねる", "かねない", "きれる", "きれない"], 2,
              "U erkak pul uchun bo'lsa hattoki do'stiga ham xiyonat qilib yuborishi hech gap emas.",
              expl="動詞マス形＋かねない — ...qilib yuborishi mumkin (salbiy ehtimol)."),
            q("t15-g1-9", "雨に（【ぬれたままの】）服を着ていたら、風邪をひきますよ。早く着替えなさい。",
              ["ぬれたままの", "ぬらしたっきりの", "ぬれたばかりの", "ぬらされたものの"], 1,
              "Yomg'irda ivigan kiyimni kiyib yuraversangiz shamollab qolasiz. Tezda kiyimingizni almashtiring.",
              expl="〜たままの — ...holaticha turgan."),
            q("t15-g1-10", "これ以上雨が降らない日が続くと、断水に（【なるおそれがある】）。",
              ["なりっこない", "ならずにはいられない", "なるおそれがある", "なるともかぎらない"], 3,
              "Bundan buyon ham yomg'ir yog'maydigan kunlar davom etsa, suv ta'minoti to'xtab qolish xavfi bor.",
              expl="〜おそれがある — ...xavfi/xatari mavjud."),
            q("t15-g1-11", "A「伊藤といいますが、今夜2名で予約を取っているはずです。」\nB「伊藤様で（【いらっしゃいますね】）。はい、たしかにご予約いただいています。」",
              ["いらっしゃいますね", "おっしゃいますね", "申されますね", "おられますね"], 1,
              "A: 'Ito bo'laman, bugun kechga 2 kishilik joy band qilgan bo'lishim kerak.' B: 'Ito janoblari bo'lasiz-a? Ha, haqiqatan buyurtmangiz bor.'",
              expl="〜でいらっしゃいますね — muloyim ehtirom/hurmat shakli."),
            q("t15-g1-12", "あなたは本当に短気だから、相手（【に怒りそうになったら】）、まずゆっくり1から10まで数えて落ち着きなさい。",
              ["を怒らせそうになったら", "に怒りそうになったら", "が怒られそうになったら", "が怒りそうにしたら"], 2,
              "Siz juda jahldorsiz, shuning uchun qarshi tomonga qarab jahlingiz chiqa boshlaganda, avval 1 dan 10 gacha sanab tinchlaning.",
              expl="相手に怒る — birovga jahli chiqmoq.")
          ]
        },
        {
          "id": "g2", "type": "grammar_sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keluvchi to'g'ri so'zni tanlang.",
          "questions": [
            q("t15-g2-1", None,
              ["待たされた", "診察はすぐ", "あげくに", "さんざん"], 3,
              "Ahvolim yomonlashib shifoxonaga borgan edim, uzoq kuttirishgach tekshiruv tezda tugab, 'shunchaki shamollash' deyishdi.",
              prefix="気分が悪くて病院に行ったが", suffix="終わり、「ただの風邪です」と言われた。", starPos=3, order=[4, 1, 3, 2],
              expl="気分が悪くて病院に行ったが【さんざん】【待たされた】【★あげくに】【診察はすぐ】終わり、「ただの風邪です」と言われた。"),
            q("t15-g2-2", None,
              ["彼も", "子どもに", "対しては", "言われる"], 2,
              "Pishiq va sovuqqon deyilgan u kishi ham bolalarga nisbatan doimo mehribon edi.",
              prefix="皮肉で冷たいと", suffix="いつもやさしかった。", starPos=3, order=[4, 1, 2, 3],
              expl="皮肉で冷たいと【言われる】【彼も】【★子どもに】【対しては】いつもやさしかった。"),
            q("t15-g2-3", None,
              ["既卒かを", "新卒か", "問わず", "採用試験を"], 1,
              "Bu kompaniyada yangi bitiruvchimi yoki avval bitirganmi qat'i nazar qabul imtihonini topshirish mumkin.",
              prefix="この会社は", suffix="受けることができます。", starPos=2, order=[2, 1, 3, 4],
              expl="この会社は【新卒か】【★既卒かを】【問わず】【採用試験を】受けることができます。"),
            q("t15-g2-4", None,
              ["実行されるのに", "試してみる", "少数の学校で", "先立ち"], 4,
              "Yangi ta'lim uslubi amaliyotga joriy etilishidan oldin bir nechta maktablarda sinovdan o'tkaziladigan bo'ldi.",
              prefix="新しい教育方法が", suffix="ことになった。", starPos=2, order=[1, 4, 3, 2],
              expl="新しい教育方法が【実行されるのに】【★先立ち】【少数の学校で】【試してみる】ことになった。"),
            q("t15-g2-5", None,
              ["あるまいが", "道に迷う", "一応", "ことなど"], 1,
              "Kimura kabi tajribali gid yo'ldan adashishi amrimahol bo'lsa-da, har ehtimolga qarshi politsiyaga telefon qilaylik.",
              prefix="木村さんほどのベテランのガイドが", suffix="警察に電話しよう。", starPos=3, order=[2, 4, 1, 3],
              expl="木村さんほどのベテランのガイドが【道に迷う】【ことなど】【★あるまいが】【一応】警察に電話しよう。")
          ]
        },
        {
          "id": "g3", "type": "grammar_passage_context",
          "instruction_jp": "次の文章を読んで、文章全体の趣旨を踏まえて、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlar uchun kontekstga mos eng to'g'ri javobni tanlang.",
          "passage": "うそをついている人を、どこで見分ければいいでしょうか。\nある大学教授が、何人かの人が話しているビデオを学生に見せ、「だれがうそをついているか。なぜそう判断したか」をたずねました。\n最も多くの人が注目したのが「話し方」で、次に「話の内容」でした。「目の動き」「顔の表情」「話す時間」が同じくらいで、「手の動き」「足の動き」に注目した人はわずかでした。\nところが[ 50 ]、一番多くうそをついている人を当てたのは、「手の動き」に注目した人でした。この人たちの実に90パーセントがうそをついている人を当てています。\nこれに続いて「足の動き」に注目した人の正解が多くなっています。反対に正解が少なかったのは「顔の表情」「話す時間」で、半分以下でした。\n以上のデータから、本心が表れやすいのは[ 51 ]だとわかります。\n一生懸命しゃべっているが目と目を合わさないときなどは、手と足に注目すると本心が見えやすくなります。手をオーバーに動かす、何回も座りなおす、足をゆさぶるなどに注意しないと、自分のうそも相手にわかってしまいます。\n顔は、言葉と同じように、その場の状況[ 52 ]本心と異なる表情ができます。つまり、必要ならばうそがつ託けるのです。\nしかし[ 53 ]ことは、人間関係を維持するのに非常に大切です。人々が本心通りにしゃべったり顔に表すようになったら、人間関係の多くがこわれてしまいます。人が着ている服が「似合わない」と思っても、ふつうは「お似合いですね」と言います。正直であることが必ず[ 54 ]。",
          "questions": [
            q("t15-g3-1", "［ 50 ］に入る最もよいものを選びなさい。",
              ["予想通りに", "予想に反し", "予想に基づいて", "予想にかかわらず"], 2,
              "［ 50 ］bo'sh o'rniga mos so'zni tanlang.",
              blankNo=50, expl="Kutilgan taxminlarga zid ravishda: 「予想に反し (kutilganiga teskari o'laroq)」."),
            q("t15-g3-2", "［ 51 ］に入る最もよいものを選びなさい。",
              ["話の内容", "顔の表情", "手足の動き", "目の動き"], 3,
              "［ 51 ］bo'sh o'rniga mos iborani tanlang.",
              blankNo=51, expl="Chin dildagi niyat qo'l va oyoq harakatlarida namoyon bo'ladi: 「手足の動き」."),
            q("t15-g3-3", "［ 52 ］に入る最もよいものを選びなさい。",
              ["に応じて", "に関して", "に際して", "をめぐって"], 1,
              "［ 52 ］bo'sh o'rniga mos grammatik shaklni tanlang.",
              blankNo=52, expl="Vaziyatga qarab o'zgartira olish: 「に応じて (vaziyatga qarab)」."),
            q("t15-g3-4", "［ 53 ］に入る最もよいものを選びなさい。",
              ["うそをつく", "うそをつかない", "本心を語る", "正直に言う"], 1,
              "［ 53 ］bo'sh o'rniga mos ifodani tanlang.",
              blankNo=53, expl="Odamlar bilan munosabatni saqlash uchun yolg'on gapirish (xushomad qilish): 「うそをつく」."),
            q("t15-g3-5", "［ 54 ］に入る最もよいものを選びなさい。",
              ["正しいはずがありません", "正しいに相違ありません", "正しいと決まっています", "正しいわけではありません"], 4,
              "［ 54 ］bo'sh o'rniga mos ifodani tanlang.",
              blankNo=54, expl="To'g'riso'z bo'lish har doim ham to'g'ri degani emas: 「正しいわけではありません」.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK! test15.json yaratildi: 6 vocab + 3 grammar bo'limlari.")
