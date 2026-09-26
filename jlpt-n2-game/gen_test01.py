# -*- coding: utf-8 -*-
"""
test01.json generatori — 第1回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.2
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test01.json")

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
  "id": 1,
  "title_jp": "第1回 模擬テスト",
  "title_uz": "1-test",
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
            q("t1-v1-1", "彼女は子どものとき、【行儀作法】を家庭で厳しく教え込まれた。",
              ["こうぎ", "こうき", "ぎょうぎ", "ぎょうき"], 3,
              "U bolaligida odob-axloq qoidalarini oilada qattiq o'rgatilgan edi.",
              reading="ぎょうぎ", expl="行儀作法 → ぎょうぎさほう (odob-axloq, yurish-turish qoidalari)"),
            q("t1-v1-2", "国際コンクールでの優勝は、若い音楽家の人生を【一瞬】にして変えた。",
              ["いちしゅん", "いつしゅん", "いっじゅん", "いっしゅん"], 4,
              "Xalqaro tanlovdagi g'alaba yosh musiqachining hayotini bir lahzada o'zgartirdi.",
              reading="いっしゅん", expl="一瞬 → いっしゅん (bir lahza, bir on)"),
            q("t1-v1-3", "「残りわずか」の声に【誘われて】、思わずテレビショッピングで買い物をしてしまった。",
              ["さそわれて", "おそわれて", "とらわれて", "うたわれて"], 1,
              "«Oz qoldi» degan so'zga qiziqib (vasvasaga tushib), beixtiyor teledo'kondan xarid qilib qo'ydim.",
              reading="さそわれて", expl="誘う → さそう (taklif qilmoq, qiziqtirmoq / vasvasaga solmoq)"),
            q("t1-v1-4", "以前は静かな町だったのに、最近は【物騒な】事件が多くなった。",
              ["ぶっぞう", "ぶっそう", "ぶつぞう", "ぶつそう"], 2,
              "Ilgari tinch shahar edi, yaqinda esa xavfli/notinch hodisalar ko'paydi.",
              reading="ぶっそう", expl="物騒 → ぶっそう (xavfli, bexavotir bo'lmagan, notinch)"),
            q("t1-v1-5", "インフルエンザでの死亡率が低い理由の1つに、国民の【衛生】知識の高さがあげられる。",
              ["ええせい", "えいぜい", "えいせい", "ええぜい"], 3,
              "Grippdan o'lim darajasi pastligining bir sababi xalqning gigiyena bilimi yuqoriligidir.",
              reading="えいせい", expl="衛生 → えいせい (gigiyena, sanitariya)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t1-v2-6", "節約生活に疲れた消費者に安いだけの商品は【あきられて】きた。",
              ["飯きられて", "飽きられて", "館きられて", "飲きられて"], 2,
              "Tejamkor hayotdan charchagan iste'molchilarga faqat arzon bo'lgan mahsulotlar jonga tegib qoldi.",
              reading="あきられて", expl="飽きる → あきる (me'daga tegmoq, jonga tegmoq)"),
            q("t1-v2-7", "『源氏物語』は日本の代表的な【こてん】文学だ。",
              ["古展", "箇典", "個展", "古典"], 4,
              "«Genji monogatari» — Yaponiyaning vakillik qiluvchi mumtoz (klassik) adabiyotidir.",
              reading="こてん", expl="古典 → こてん (mumtoz, klassik)"),
            q("t1-v2-8", "自分の欠点を【なげいて】ばかりいないで、長所を伸ばすべきだ。",
              ["難いて", "嘆いて", "喝いて", "漢いて"], 2,
              "O'z kamchiliklaringga faqat qayg'uravermasdan (hasrat chekmasdan), kuchli tomonlaringni rivojlantirishing kerak.",
              reading="なげいて", expl="嘆く → なげく (qayg'urmoq, hasrat chekmoq, nola qilmoq)"),
            q("t1-v2-9", "ストレスの多い現代、うつ病を病む人が【げきぞう】している。",
              ["激増", "激象", "劇増", "劇象"], 1,
              "Stress ko'p bo'lgan zamonamizda depressiyaga chalingan odamlar keskin ko'paymoqda.",
              reading="げきぞう", expl="激増 → げきぞう (keskin/tez ko'payish)"),
            q("t1-v2-10", "高い技術力のおかげで海水が【たんすい】化されて、飲めるようになった。",
              ["単水", "短水", "淡水", "採水"], 3,
              "Yuqori texnologiya tufayli dengiz suvi chuchuklashtirilib, ichish mumkin bo'ldi.",
              reading="たんすい", expl="淡水 → たんすい (chuchuk suv) (淡水化 = chuchuklashtirish)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t1-v3-11", "自分の手で文字を書くと記憶（　）がより高まるそうだ。",
              ["質", "化", "力", "性"], 3,
              "O'z qo'ling bilan harflarni yozsang, xotira qobiliyati (kuchi) yanada oshar ekan.",
              expl="記憶力 (きおくりょく) = xotirlash qobiliyati"),
            q("t1-v3-12", "この絵は彼の代表（　）である。",
              ["品", "作", "物", "者"], 2,
              "Bu surat uning eng mashhur (namoyondalik) asaridir.",
              expl="代表作 (だいひょうさく) = muallifning eng mashhur / vakillik asari"),
            q("t1-v3-13", "ここは高山植物の保護（　）です。",
              ["区", "場", "所", "域"], 1,
              "Bu yer baland tog' o'simliklarini muhofaza qilish hududidir (zonasidir).",
              expl="保護区 (ほごく) = qo'riqxona zonasi, muhofaza hududi"),
            q("t1-v3-14", "プロ野球の公式（　）が始まるところだ。",
              ["軍", "陣", "戦", "権"], 3,
              "Professional beysbolning rasmiy musobaqasi (o'yini) boshlanish arafasida.",
              expl="公式戦 (こうしきせん) = rasmiy o'yin / musobaqa"),
            q("t1-v3-15", "この薬は胃を荒らす（　）作用がある。",
              ["悪", "副", "複", "反"], 2,
              "Bu dorining oshqozonni bezovta qiladigan nojo'ya ta'siri (aks ta'siri) bor.",
              expl="副作用 (ふくさよう) = nojo'ya ta'sir")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ( ) ga ma'no jihatidan eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t1-v4-16", "「歴史は繰り返す」と言うが、同じように繰り返されることは（　）にない。",
              ["滅多に", "滅多", "まれ", "たま"], 2,
              "«Tarix takrorlanadi» deyiladi-ku, lekin bir xil bo'lib takrorlanishi kamdan-kam bo'ladi.",
              reading="めった", expl="滅多に〜ない (めったに〜ない) = kamdan-kam, deyarli bo'lmaydi"),
            q("t1-v4-17", "洗濯機がこう（　）故障するのでは、買い替えるしかない。",
              ["それぞれ", "しばしば", "ぞくぞく", "とうとう"], 2,
              "Kir yuvish mashinasi bunchalik tez-tez buzilaversa, yangisini sotib olishdan boshqa chora yo'q.",
              expl="しばしば = tez-tez, bot-bot (たびたび)"),
            q("t1-v4-18", "この地域は一人暮らしのお年寄りが多く、（　）に不安がある。",
              ["セキュリティー", "コンディション", "オペレーション", "コンタクト"], 1,
              "Bu hududda yolg'iz yashovchi qariyalar ko'p bo'lib, xavfsizlik (security) masalasida xavotir bor.",
              expl="セキュリティー = xavfsizlik, xavfsizlik tizimi"),
            q("t1-v4-19", "私の夢は、グローバルな（　）で活躍することです。",
              ["信頼", "資本", "舞台", "現実"], 3,
              "Mening orzum — global maydonda (sahna) faoliyat yuritishdir.",
              expl="舞台 (ぶたい) = sahna, maydon (global maydon = グローバルな舞台)"),
            q("t1-v4-20", "この家の建て方は、この地方（　）のものです。",
              ["独特", "格別", "特例", "特殊"], 1,
              "Bu uyning qurilish uslubi faqat shu hududga xosdir (o'ziga xosdir).",
              expl="独特 (どくとく) = o'ziga xos, betakror"),
            q("t1-v4-21", "屋根を（　）するついでに、太陽光発電システムを取り入れることにした。",
              ["調節", "管理", "修正", "修繕"], 4,
              "Tomni ta'mirlash bahonasida quyosh energiyasi tizimini o'rnatishga qaror qildik.",
              expl="修繕 (しゅうぜん) = ta'mirlash, tuzatish"),
            q("t1-v4-22", "新聞の料理記事の（　）を献立の参考にしている。",
              ["切り抜き", "切り取り", "書き取り", "選り抜き"], 1,
              "Gazetadagi taom maqolalaridan qirqib olingan parchalarni taomnoma tuzishda qo'llanma qilyapman.",
              expl="切り抜き (きりぬき) = gazetadan qirqib olingan parcha (vyrezka)")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin sinonimni tanlang.",
          "questions": [
            q("t1-v5-23", "この私鉄は次の駅でJRと【連絡している】。",
              ["乗り換えになる", "交差している", "一体化している", "つながっている"], 4,
              "Bu xususiy temiryo'l keyingi bekatda JR bilan tutashgan (bog'langan).",
              reading="れんらくしている", expl="連絡している = つながっている (bog'langan, tutashgan)"),
            q("t1-v5-24", "選挙の予想が【外れた】。",
              ["騒がれた", "おかしかった", "当たらなかった", "難しかった"], 3,
              "Saylov bo'yicha taxmin xato chiqdi (to'g'ri chiqmadi).",
              reading="はずれた", expl="外れる (はずれる) = 当たらなかった (to'g'ri chiqmadi, adashdi)"),
            q("t1-v5-25", "近道したのに【かえって】時間がかかった。",
              ["非常に", "改めて", "逆に", "多少"], 3,
              "Yaqin yo'ldan borgan bo'lsak-da, aksincha ko'proq vaqt ketdi.",
              expl="かえって = 逆に (aksincha, teskarisiga)"),
            q("t1-v5-26", "はっきり意見を申し上げるなら、その案には【反対です】。",
              ["率直に", "適当に", "簡単に", "自由に"], 1,
              "Ochiqchasiga (samimiy) fikrimni aytsam, u taklifga qarshiman.",
              expl="率直に (そっちょくに) = はっきりと、ありのままに (ochiqchasiga, to'g'ridan-to'g'ri)"),
            q("t1-v5-27", "上司が休日出勤して、部下の遅れた仕事を【カバーした】。",
              ["進めた", "終わらせた", "引き受けた", "補った"], 4,
              "Rahbar dam olish kuni ishga chiqib, xodimining kechikkan ishini to'ldirdi (yordam berdi).",
              expl="カバーした = 補った (おぎなった — kam-ko'stini to'ldirdi, qopladi)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilgan gapini tanlang.",
          "questions": [
            q("t1-v6-28", "通用", [
                "この仕事には能力のある人物を通用する予定だ。",
                "そんなへたな言い訳は、私には通用しない。",
                "この危険な仕事に、これだけの給料では通用しない。",
                "この本はあなたの勉強に通用するのでお読みなさい。"], 2,
              "通用 (つうよう) = yaroqli bo'lmoq, o'tmoq, qabul qilinmoq.",
              optsTr=[
                "Bu ishga qobiliyatli odamni 'o'tkazish' rejamiz bor (noto'g'ri).",
                "Bunday puch bahonalar menga o'tmaydi (ish bermaydi). (to'g'ri)",
                "Bu xavfli ishga buncha oylik 'o'tmaydi' (noto'g'ri).",
                "Bu kitob sizning o'qishingizga 'o'tadi', o'qing (noto'g'ri)."]),
            q("t1-v6-29", "あらすじ", [
                "論文は、あらすじ書き上がっています。",
                "会議で経営方針のあらすじが決まった。",
                "仲間同士で激しいあらすじになってしまった。",
                "この小説のあらすじを400字以内にまとめなさい。"], 4,
              "あらすじ = qisqacha mazmun (syujet bayoni).",
              optsTr=[
                "Ilmiy maqola 'qisqacha syujeti' yozib bo'lindi (noto'g'ri).",
                "Yig'ilishda boshqaruv rejasining 'syujeti' hal bo'ldi (noto'g'ri).",
                "Do'stlar o'rtasida shiddatli 'syujet' yuz berdi (noto'g'ri).",
                "Ushbu romanning qisqacha mazmunini (syujetini) 400 belgidan oshirmay xulosa qiling. (to'g'ri)"]),
            q("t1-v6-30", "迷惑", [
                "だれにでも迷惑な思い出の1つや2つはあるものだ。",
                "込んでいる電車の中で新聞を広げるのは、他の客に迷惑だ。",
                "こんな少ない給料では家族の生活はいい迷惑だ。",
                "病気だとわかったときにはもうすでに手遅れで、迷惑な状態だった。"], 2,
              "迷惑 (めいわく) = boshqalarga noqulaylik/tashvish tug'dirish.",
              optsTr=[
                "Har kimda ham 'noqulay' xotira bitta-ikkita bo'ladi (noto'g'ri).",
                "Odam gavjum poyezdda gazeta yoyish — boshqa yo'lovchilarga halal beradi (noqulaylikdir). (to'g'ri)",
                "Bunday kam maosh bilan oilaning turmushi 'katta noqulaylik' (noto'g'ri).",
                "Kasal ekani bilinganda kech bo'lib, 'noqulay' holatda edi (noto'g'ri)."]),
            q("t1-v6-31", "売買", [
                "この店は土日も休まず売買している。",
                "この商品は売買がよくて、生産が追いつかない。",
                "やむを得ない事情でこの土地を売買することにした。",
                "不動産を売買するには資格が必要だ。"], 3,
              "売買 (ばいばい) = oldi-sotdi (savdo qilish).",
              optsTr=[
                "Bu do'kon shanba-yakshanba ham dam olmasdan 'oldi-sotdi qiladi' (noto'g'ri — 営業).",
                "Bu mahsulotning 'oldi-sotdisi' yaxshi bo'lib, yetkazib bo'lmayapti (noto'g'ri — 売れ行き).",
                "Majburiy vaziyat tufayli ushbu yerni oldi-sotdi qilishga (sotishga) qaror qildik. (to'g'ri)",
                "Ko'chmas mulkni oldi-sotdi qilish uchun litsenziya kerak (noto'g'ri)."]),
            q("t1-v6-32", "過半数", [
                "新しい法案は過半数の賛成を得たので国会で成立した。",
                "今回の地震の被害者の数は過半数だった。",
                "狭い会場にファンが過半数で押しかけてきた。",
                "彼が犯人だという証拠は過半数である。"], 1,
              "過半数 (かはんすう) = ko'pchilik qism (yarmidan ko'pi, 50% dan ortig'i).",
              optsTr=[
                "Yangi qonun loyihasi yarmidan ko'pining (ko'pchilikning) ovozini olib, parlamentda ma'qullandi. (to'g'ri)",
                "Bu galgi zilzila qurbonlarining soni 'ko'pchilik' edi (noto'g'ri).",
                "Tor zalga muxlislar 'ko'pchilik bo'lib' bostirib keldi (noto'g'ri).",
                "U jinoyatchi ekanligi haqidagi dalil 'yarmidan ko'p' (noto'g'ri)."])
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
          "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
          "questions": [
            q("t1-g1-33", "転職はよく考えた（　）決めたことですから、たとえ失敗してもかまいません。",
              ["際に", "あげく", "上で", "ついでに"], 3,
              "Ishni o'zgartirish yaxshilab o'ylab ko'rgach qabul qilgan qarorim bo'lgani uchun, xato bo'lsa ham mayli.",
              expl="〜た上で (うえで) = ...gach, ...ganidan so'ng (oldin sinchiklab o'ylab, keyin qilingan harakat)"),
            q("t1-g1-34", "税金が上がるのは困る。しかし高齢者がますます増える現実（　）、仕方がない。",
              ["からいって", "だからといって", "だけあって", "といって"], 1,
              "Soliqlar oshishi qiyin. Ammo qariyalar soni tobora oshib borayotgan voqelikdan kelib chiqsak, iloj yo'q.",
              expl="〜からいって = ...dan kelib chiqib mulohaza yuritilsa"),
            q("t1-g1-35", "ここのタイ料理は、日本人（　）すこし辛さをおさえてあります。",
              ["的に", "用に", "寄りに", "向けに"], 4,
              "Bu yerdagi tay taomlari yaponlar uchun (yaponlarga mo'ljallab) achchiqligi biroz pasaytirilgan.",
              expl="〜向けに (むけに) = ...uchun maxsus mo'ljallangan"),
            q("t1-g1-36", "私が見た（　）、山田さんがそんなに悪い人だとは思えない。",
              ["ことでは", "ものでは", "かぎりでは", "まででは"], 3,
              "Mening ko'rganim bo'yicha (kuzatishim doirasida) qaralsa, Yamada-sanni bunchalik yomon odam deb hisoblay olmayman.",
              expl="〜かぎりでは = ...ganimcha, ...doirasida hukm qilinsa"),
            q("t1-g1-37", "「自分ならもっとうまくやれる」と言うなら、君がやってみる（　）だね。",
              ["わけ", "もの", "こと", "はず"], 3,
              "«O'zim bo'lsam bundan ham yaxshi qilardim» deydigan bo'lsang, o'zing qilib ko'rishing kerak-da.",
              expl="〜ことだ = ...qilish kerak (maslahat yoki kinoya)"),
            q("t1-g1-38", "結婚後も仕事をする女性が増える（　）、専業主婦になりたい女性も増えている。",
              ["反対で", "以外で", "片面で", "一方で"], 4,
              "Turmush qurgandan keyin ham ishlaydigan ayollar ko'payayotgan bir paytda, uy bekasi bo'lishni xohlaydigan ayollar ham ko'paymoqda.",
              expl="〜一方で (いっぽうで) = bir tomondan ... bo'lsa, ikkinchi tomondan esa..."),
            q("t1-g1-39", "検査の結果が心配（　）、朝まで眠ることができなかった。",
              ["のあまり", "のせいか", "のくせに", "のおかげで"], 1,
              "Tekshiruv natijasidan haddan tashqari xavotirlanganimdan, tonggacha uxlay olmadim.",
              expl="〜あまり = ...ning haddan ziyodligi natijasida"),
            q("t1-g1-40", "この果物はとても健康にいい（　）、昔から「医者いらず」とも呼ばれる。",
              ["ことから", "ことだから", "ことに", "ことなら"], 1,
              "Bu meva salomatlik uchun juda foydali bo'lgani sababli, qadimdan «shifokorga hojat qoldirmas» deb ham ataladi.",
              expl="〜ことから = ...bo'lganligi sababli (sabab/kelib chiqish)"),
            q("t1-g1-41", "健康に悪いと（　）、どうして煙草がやめられない。",
              ["知りつつも", "知らないものの", "知るからには", "知らないくせに"], 1,
              "Salomatlikka zarar ekanligini bilsa ham, nega tamakini tashlay olmaydi-a!",
              expl="〜つつも = ...sa ham, qaramay (ziddiyatli harakat)"),
            q("t1-g1-42", "このなかでだれも免許を持っていないなら、私が運転（　）ね。",
              ["するわけにはいかない", "しないわけにはいかない", "するべきでない", "してはいられない"], 2,
              "Agar oramizda hech kimning haydovchilik guvohnomasi bo'lmasa, men haydamasam bo'lmaydi (haydashga majburman).",
              expl="〜ないわけにはいかない = ...maslikning iloji yo'q, shart"),
            q("t1-g1-43", "たとえ贈り物が（　）、下さった方にお礼の手紙くらい書くものですよ。",
              ["気に入らなかったにしても", "気に入らなかったとしたら", "気に入ったとしても", "気に入ったとしたら"], 1,
              "Garchi sovg'a yoqmagan bo'lsa ham, uni bergan kishiga hech bo'lmaganda minnatdorchilik maktubi yozish odobdandir.",
              expl="たとえ〜にしても = garchi ... bo'lgan taqdirda ham"),
            q("t1-g1-44", "A「あいにく田中は外出しております。」\nB「では、A社の山田から電話があったと（　）。」",
              ["伝えていただけますか", "お伝えいただけますか", "お伝えになれますか", "お伝えいたしましょうか"], 2,
              "A: «Afsuski Tanaka tashqariga chiqqan edilar.»\nB: «U holda, A kompaniyasining Yamadasidan qo'ng'iroq bo'lganini yetkazib qo'ya olasizmi?»",
              expl="お伝えいただけますか = yetkazib bera olasizmi (xushmuomala so'rov: お〜いただく)")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng to'g'ri bo'lakni tanlang.",
          "questions": [
            q("t1-g2-45", None, ["やれる", "やって", "できるか", "ものなら"], 4,
              "To'g'ri tartib: そんな勉強のやり方で合格できるか、やれるものならやってみればいいよ。",
              prefix="そんな勉強のやり方で合格", suffix="みればいいよ。", starPos=3, order=[3, 1, 4, 2],
              expl="To'g'ri tartib: 合格[できるか]、[やれる][★ものなら][やって]みればいいよ。 (3 → 1 → 4 → 2)"),
            q("t1-g2-46", None, ["がち", "飲める", "忘れ", "ありがたさを"], 3,
              "To'g'ri tartib: 日本人は、どこでも水がただで飲めるありがたさを忘れがちです。",
              prefix="日本人は、どこでも水がただで", suffix="です。", starPos=3, order=[2, 4, 3, 1],
              expl="To'g'ri tartib: ただで[飲める][ありがたさを][★忘れ][がち]です。 (2 → 4 → 3 → 1)"),
            q("t1-g2-47", None, ["なれば", "という", "ものでは", "平気になる"], 2,
              "To'g'ri tartib: 歯医者に行くのは、大人になれば平気になるというものではありません。",
              prefix="歯医者に行くのは、大人に", suffix="ありません。", starPos=3, order=[1, 4, 2, 3],
              expl="To'g'ri tartib: 大人になれば[平気になる][という][★ものでは]ありません。 (1 → 4 → 2 → 3)"),
            q("t1-g2-48", None, ["忘れた", "に", "かけるのを", "ばかり"], 1,
              "To'g'ri tartib: 私が家のかぎをかけるのを忘れたばかりに、どろぼうに入られてしまった。",
              prefix="私が家のかぎを", suffix="どろぼうに入られてしまった。", starPos=2, order=[3, 1, 4, 2],
              expl="To'g'ri tartib: かぎを[かけるのを][★忘れた][ばかり][に] (3 → 1 → 4 → 2)"),
            q("t1-g2-49", None, ["ある", "以上は", "うつす", "おそれが"], 4,
              "To'g'ri tartib: B「病気を人にうつすおそれがある以上は、学校を休んだほうがいいわよ。」",
              prefix="B「病気を人に", suffix="学校を休んだほうがいいわよ。」", starPos=2, order=[3, 4, 1, 2],
              expl="To'g'ri tartib: 病気を人に[うつす][★おそれが][ある][以上は] (3 → 4 → 1 → 2)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh joylariga eng to'g'ri variantni tanlang.",
          "passage_title": "囲碁の広がり",
          "passage": (
            "少し前の日本の家庭には、たいてい囲碁（いご）の道具があった {{50}} 。子どもたちは、"
            "祖父や近所のおじさんたちが遊ぶのをそばで見て、自分たちもルールを覚えていった。だが"
            "最近は核家族が増えて、ルールを知らない若い親は子どもに教えることがなくなり、子どもたちも囲碁からは離れていった。\n"
            "囲碁は本当に強くなるためには、子どものときから始めるのが重要だそうだ。しかし、"
            "かつて1200万人とも言われた競技人口が300万人台にまで落ち込み、しかも子どもの数がとても少なくなった。囲碁にかかわる人々は、日本の囲碁の将来に {{51}} 。\n"
            "そこへ救いの神が現れた。1998年から雑誌に囲碁がテーマのマンガが連載され、大ヒットしたのだ。マンガはテレビアニメにもなり、子ども向けに囲碁を教えるテレビ番組も放送された。このマンガを {{52}} として、囲碁を始めた子どもはざっと100万人と言われる。\n"
            "だが何しろ日本人は熱しやすく冷めやすい国民だ。事実、すでに新しく囲碁を始める人は {{53}} 。\n"
            "「この機会を一時のブームで {{54}} 」と、関係者はいろいろなアイデアを出している。"
          ),
          "passage_tr": (
            "Biroz avvalgi yapon xonadonlarida odatda go (igo) o'yini anjomlari bo'lar edi. Bolalar bobolari va "
            "qo'shni amakilarning o'ynashini yonidan kuzatib, o'zlari ham qoidalarini o'rganib olishardi. Ammo "
            "so'nggi paytlarda alohida yashovchi oilalar ko'payib, qoidani bilmaydigan yosh ota-onalar bolalariga "
            "o'rgatmay qo'ydi, bolalar ham godan uzoqlashdi.\n"
            "Go o'yinida chinakam kuchli bo'lish uchun bolalikdan boshlash muhim ekan. Biroq, bir paytlar 12 million kishi "
            "deb aytilgan o'yinchilar soni 3 milliongacha tushib ketdi, buning ustiga bolalar soni ham juda kamaydi. "
            "Go sohasidagi insonlar yapon gosi kelajagidan qattiq xavotirda edilar.\n"
            "Shu paytda najotkor paydo bo'ldi. 1998-yildan jurnalda go mavzusidagi manga chop etila boshlab, juda mashhur bo'ldi. "
            "Manga teleanimatsiyaga aylandi, bolalar uchun go o'rgatadigan teledasturlar ham efirga uzatildi. Ushbu mangani "
            "turtki (sabab) qilib, go o'ynashni boshlagan bolalar taxminan 1 million kishi deb aytiladi.\n"
            "Lekin nima bo'lganda ham yaponlar tez qizib, tez soviydigan xalqdir. Aslida allaqachon yangidan goni boshlayotganlar "
            "kamayib bormoqda.\n"
            "«Ushbu imkoniyatni vaqtinchalik shov-shuv bilan tugatib qo'ymaylik» deb, soha xodimlari turli g'oyalarni ilgari surmoqdalar."
          ),
          "questions": [
            q("t1-g3-50", None, ["ことだ", "ものだ", "ところだ", "ようだ"], 2,
              "かつての習慣: 囲碁の道具があった[ものだ] (Ilgari bo'lar edi - o'tmishdagi xotira/odat).",
              blankNo="50", expl="〜ものだ = o'tmishdagi doimiy holat / xotira"),
            q("t1-g3-51", None, ["大きな希望を持っていた", "強い不安を持っていた", "安心しかねなかった", "少しの心配もなかった"], 2,
              "日本の囲碁の将来に[強い不安を持っていた] (Kelajagidan qattiq xavotirda edilar).",
              blankNo="51", expl="O'yinchilar soni keskin kamaygani sababli: 強い不安を持っていた"),
            q("t1-g3-52", None, ["きっかけ", "もと", "事情", "原因"], 1,
              "このマンガを[きっかけ]として = Ushbu mangani turtki qilib / bahona qilib.",
              blankNo="52", expl="〜をきっかけとして = ...ni turtki / sabab qilib olib"),
            q("t1-g3-53", None, ["減りつつある", "減りそうもない", "増えるかもしれない", "増えざるを得ない"], 1,
              "新しく囲碁を始める人は[減りつつある] = Yangi boshlovchilar kamayib bormoqda.",
              blankNo="53", expl="〜つつある = tobora ...yotgan bo'lmoq (davomiy o'zgarish)"),
            q("t1-g3-54", None, ["終わらせたい", "終わらせよう", "終わらせまい", "終わりたくない"], 3,
              "この機会を一時のブームで[終わらせまい]と = bir lahzalik shov-shuv bilan tugatib qo'ymaylik deb.",
              blankNo="54", expl="〜まい = ...maslik niyati / qarori (tugatmaslikka qaror qilish)")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print(f"OK! test01.json yaratildi: {total} ta savol.")
