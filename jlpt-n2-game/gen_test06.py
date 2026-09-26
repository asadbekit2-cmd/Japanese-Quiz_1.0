# -*- coding: utf-8 -*-
"""
test06.json generatori — 第6回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.7
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test06.json")

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
  "id": 6,
  "title_jp": "第6回 模擬テスト",
  "title_uz": "6-test",
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
            q("t6-v1-1", "この品質で1万円なら、まあ【妥当な】値段でしょう。",
              ["だどう", "だっとう", "だとう", "たとう"], 3,
              "Ushbu sifat uchun 10 ming iyen bo'lsa, ancha munosib (adolatli/o'rinli) narx bo'lsa kerak.",
              reading="だとう", expl="妥当 → だとう (o'rinli, munosib, to'g'ri keladigan)"),
            q("t6-v1-2", "血液の【循環】が悪くなると、疲れが取れにくい体になってしまう。",
              ["じゅんがん", "しゅんかん", "しゅんがん", "じゅんかん"], 4,
              "Qon aylanishi (sirkulyatsiyasi) yomonlashsa, charchoq osonlikcha chiqmaydigan tana holatiga kelib qoladi.",
              reading="じゅんかん", expl="循環 → じゅんかん (aylanish, sirkulyatsiya)"),
            q("t6-v1-3", "あの人はいつも【損得】を判断して行動するような人間だ。",
              ["そんとく", "そんどく", "そうとく", "そうどぐ"], 1,
              "U doim foyda va zararni hisob-kitob qilib harakatlanadigan odamdir.",
              reading="そんとく", expl="損得 → そんとく (foyda va zarar, naf)"),
            q("t6-v1-4", "衣食住に【順位】をつけるなら、私の場合は、食の次に住がくる。",
              ["いじょくしゅう", "いじょくじゅう", "いしょくじゅう", "いじょくしゅう"], 3,
              "Kiyinish, ovqatlanish va uy-joyga (衣食住) daraja qo'yilsa, mening holimda taomdan keyin uy turadi.",
              reading="いしょくじゅう", expl="衣食住 → いしょくじゅう (kiyim, taom va boshpana — hayotiy ehtiyojlar)"),
            q("t6-v1-5", "料理の手間を【省く】調理器具を母の日のプレゼントにした。",
              ["ぬく", "くだく", "のぞく", "はぶく"], 4,
              "Ovqat tayyorlashdagi mashaqqatni tejaydigan (kamaytiradigan) oshxona anjomlarini Onalar kuni sovg'asi qildim.",
              reading="はぶく", expl="省く → はぶく (qisqartirmoq, tejamoq, chetlab o'tmoq)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t6-v2-6", "14〜15歳という年齢は子どもの終わりであり、大人の始まりである【びみょう】な時期だ。",
              ["微妙", "微妙", "徴明", "徴明"], 1,
              "14-15 yosh bolalikning intihosi va ulg'ayishning ibtidosi bo'lgan nozik (o'ta sezgir/murakkab) davrdir.",
              reading="びみょう", expl="微妙 → びみょう (nozik, sezgir, o'zgaruvchan)"),
            q("t6-v2-7", "家計を【おぎなう】ために働きに出る主婦は増え続けている。",
              ["添う", "充う", "補う", "授う"], 3,
              "Ro'zg'or byudjetini to'ldirish (yetishmovchilikni qoplash) uchun ishlashga chiqadigan uy bekalari tobora ko'paymoqda.",
              reading="おぎなう", expl="補う → おぎなう (to'ldirmoq, qoplamoq)"),
            q("t6-v2-8", "人の頭の中にはパソコンも及ばないような記憶【そうち】があるという。",
              ["創置", "構置", "操置", "装置"], 4,
              "Inson bosh miyasida hatto kompyuter ham yetolmaydigan xotira qurilmasi (tizimi) mavjud emish.",
              reading="そうち", expl="装置 → そうち (qurilma, apparat)"),
            q("t6-v2-9", "【しゅっきん】前に会社の近くの喫茶店で朝食を食べることにしている。",
              ["出勤", "出緊", "出務", "出働"], 1,
              "Ishga borishdan oldin kompaniya yaqinidagi qahvaxonada nonushta qilishni odat qilganman.",
              reading="しゅっきん", expl="出勤 → しゅっきん (ishga chiqish, xizmatga borish)"),
            q("t6-v2-10", "50年前までは地図になかったヒマラヤのこの湖は、氷が【とけて】できた。",
              ["湯けて", "解けて", "割けて", "削けて"], 2,
              "50 yil muqaddam xaritada bo'lmagan Himolaydagi bu ko'l muzning erishi natijasida hosil bo'lgan.",
              reading="とけて", expl="解ける (溶ける) → とける (erimoq)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t6-v3-11", "雨水をタンクにためて、火災（　）の消火に使う。",
              ["場", "時", "防", "間"], 2,
              "Yomg'ir suvini idishda to'plab, yong'in sodir bo'lgan paytda o'chirishga ishlatamiz.",
              expl="火災時 (かさいじ) = yong'in payti/vaqti"),
            q("t6-v3-12", "長年（　）解決だった事件が解決した。",
              ["非", "不", "未", "無"], 3,
              "Uzoq yillar davomida hal bo'lmagan (yechilmagan) hodisa nihoyat oydinlashdi.",
              expl="未解決 (みかいけつ) = hali yechilmagan, hal etilmagan"),
            q("t6-v3-13", "新しい機械の（　）運転をする。",
              ["試", "実", "始", "再"], 1,
              "Yangi dastgohni sinov tariqasida ishlatib ko'ramiz (sinov haydovi).",
              expl="試運転 (しうんてん) = sinov tariqasida ishga tushirish"),
            q("t6-v3-14", "軍事（　）に頼らない外交を望む。",
              ["権", "戦", "力", "上"], 3,
              "Harbiy kuchga tayanmaydigan diplomatiyani xohlaymiz.",
              expl="軍事力 (ぐんじりょく) = harbiy qudrat/kuch"),
            q("t6-v3-15", "子どもの成長は個人（　）が大きい。",
              ["面", "期", "別", "差"], 4,
              "Bolalarning o'sishi va rivojlanishida individual farq (shaxsiy tafovut) katta bo'ladi.",
              expl="個人差 (こじんさ) = individual farq, shaxsiy tafovut")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ( ) ga ma'no jihatidan eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t6-v4-16", "古いアルバムが出てきて、子ども時代を（　）思い出した。",
              ["めでたく", "おしく", "醜く", "懐かしく"], 4,
              "Eski fotosuratlar albomi chiqib qolib, bolaligimni sog'inch bilan esladim.",
              reading="なつかしく", expl="懐かしく (なつかしく) = sog'inch/quvonch bilan eslash"),
            q("t6-v4-17", "景気が回復しつつあるので、自分で（　）できるまで就職活動を続けることにした。",
              ["納得", "了解", "公認", "承知"], 1,
              "Iqtisodiyot tiklanayotgani bois, o'zim to'liq qanoat hosil qilgunimcha ish izlashni davom ettirishga qaror qildim.",
              expl="納得 (なっとく) = qanoat hosil qilish, rozi bo'lish"),
            q("t6-v4-18", "課長のお説教はいつも（　）だ。",
              ["ワンセット", "ワンパターン", "ワンクッション", "ワンタッチ"], 2,
              "Bo'lim boshlig'ining tanbehlari doim bir xil qolipda (o'zgarishsiz, one-pattern) bo'ladi.",
              expl="ワンパターン (one pattern) = bir xil shablon, o'zgarishsiz qolip"),
            q("t6-v4-19", "今年はスポーツ界に新しいスターが（　）誕生した。",
              ["繰り上げて", "引き分けて", "相次いで", "乗り出して"], 3,
              "Bu yil sport olamida yangi yulduzlar ketma-ket (biri ketidan biri) dunyoga keldi.",
              expl="相次いで (あいついで) = ketma-ket, birin-ketin"),
            q("t6-v4-20", "その迷子は自分の名前を（　）と答えたので、すぐに親を見つけることができた。",
              ["なかなか", "ひろびろ", "てんてん", "はきはき"], 4,
              "U adashgan bola o'z ismini dadil va ravon (tiniq) aytib bergani sababli, darrov ota-onasini topishga muvaffaq bo'ldik.",
              expl="はきはき = dadil, ravon, tiniq"),
            q("t6-v4-21", "最近家族で（　）がけの旅行に出かけることが少なくなった。",
              ["宿泊", "泊まり", "日帰り", "遠出"], 2,
              "So'nggi paytlarda oilaviy tunab qolinadigan sayohatlarga chiqish kamaydi.",
              expl="泊まりがけ (とまりがけ) = tunab qolish bilan bo'ladigan sayohat"),
            q("t6-v4-22", "目の（　）を利用した現代アート展で不思議な感覚を楽しんできた。",
              ["観測", "記憶", "誤解", "錯覚"], 4,
              "Ko'z aldanuvidan (illyuziyadan) foydalangan zamonaviy san'at ko'rgazmasida ajoyib tuyg'ulardan bahramand bo'ldim.",
              expl="錯覚 (さっかく) = illyuziya, yanglish sezgi (目の錯覚 = ko'z aldanuvi)")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin sinonimni tanlang.",
          "questions": [
            q("t6-v5-23", "担当者が戻りましたら、折り返し電話を差し上げます。【すぐに】",
              ["すぐに", "明日までに", "必ず", "とりあえず"], 1,
              "Mas'ul xodim qaytsa, darhol (qayta) qo'ng'iroq qiladi.",
              reading="おりかえし", expl="折り返し = すぐに (darhol, to'xtamasdan)"),
            q("t6-v5-24", "あの教授の話はすぐ【それる】。",
              ["出版する", "翻訳する", "脱線する", "延長する"], 3,
              "U professorning gapi darrov mavzudan chetga chiqib ketadi.",
              reading="それる", expl="それる = 脱線する (だっせんする — mavzudan chetga chiqish)"),
            q("t6-v5-25", "マラソン選手は、【一気に】坂を下った。",
              ["全速力で", "たちまち", "休まずに", "なんとか"], 3,
              "Marafonchi to'xtamasdan (bir nafasda, uzluksiz) qiyalikdan pastga tushdi.",
              reading="いっきに", expl="一気に = 休まずに (to'xtamasdan, bir zarbda)"),
            q("t6-v5-26", "そのニュースを聞いて父は【苦い顔】をした。",
              ["不愉快な", "不安な", "真剣な", "得意な"], 1,
              "U xabarni eshitib dadam norozi (yoqimsiz) qiyofaga kirdi.",
              reading="にがいかお", expl="苦い顔 = 不愉快な顔 (norozi, yoqimsiz qiyofa)"),
            q("t6-v5-27", "彼らの語学力は【レベルアップ】している。",
              ["低下", "上達", "信用", "承知"], 2,
              "Ularning til bilish mahorati ancha o'sdi (yaxshilandi).",
              expl="レベルアップ = 上達 (じょうたつ — o'sish, mohirlik oshishi)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilgan gapini tanlang.",
          "questions": [
            q("t6-v6-28", "往復", [
                "子どものころの思い出が頭の中を往復する。",
                "毎朝学校へバスで往復している。",
                "工事が終わり、道路はすっかり往復している。",
                "家と会社の間を往復するだけの毎日だ。"], 4,
              "往復 (おうふく) = borib-kelish (ikki nuqta orasida qatnash).",
              optsTr=[
                "Xotiralar miyada aylanadi (noto'g'ri).",
                "Har kuni maktabga borib-keladi (noto'g'ri — 通学).",
                "Yo'l tiklandi (noto'g'ri — 復旧).",
                "Uy bilan ishxona o'rtasida shunchaki qatnashdan iborat kundalik hayot. (to'g'ri)"]),
            q("t6-v6-29", "あらわれ", [
                "昔の町並みをあらわれにして観光客を呼ぶ。",
                "一度あきらめた歌手になる希望があらわれになった。",
                "この投票率の低さは、政治への無関心のあらわれだ。",
                "お祭りには、たくさんの人々のあらわれがある。"], 3,
              "あらわれ (現れ) = ifodasi, belgisi, ko'rinishi.",
              optsTr=[
                "Ko'cha ko'rinishi (noto'g'ri).",
                "Umid paydo bo'ldi (noto'g'ri — 復活).",
                "Ovoz berish foizining bunday pastligi — siyosatga bo'lgan beparvolikning ifodasidir (ko'rinishidir). (to'g'ri)",
                "Odamlar yig'iladi (noto'g'ri)."]),
            q("t6-v6-30", "効力", [
                "勉強した効力があって合格した。",
                "仕事をまかせられて大きな効力を感じる。",
                "この薬は古くなると、効力がほとんど失われる。",
                "この部屋の間取りは効力が悪い。"], 3,
              "効力 (こうりょく) = kuch, ta'sir kuchi, samara (dori, qonun va h.k.).",
              optsTr=[
                "Harakat samarasi (noto'g'ri — 甲斐).",
                "Mas'uliyat hissi (noto'g'ri — やりがい).",
                "Bu dori eskirib qolsa, ta'sir kuchi deyarli yo'qoladi. (to'g'ri)",
                "Xona joylashuvi qulay emas (noto'g'ri — 使い勝手)."]),
            q("t6-v6-31", "見事", [
                "息子は見事な会社に就職できて喜んでいる。",
                "私の友人の画家は有名ではないが見事な絵を描く。",
                "20歳になればもう見事な大人といえる。",
                "あの子は幼い弟の世話をよくする見事な子どもだ。"], 2,
              "見事 (みごと) = ajoyib, qoyilmaqom, ko'rkam (san'at, mahorat haqida).",
              optsTr=[
                "Yaxshi kompaniya (noto'g'ri — 立派な).",
                "Rassom do'stim mashhur emas, ammo qoyilmaqom (ajoyib) suratlar chizadi. (to'g'ri)",
                "To'laqonli katta odam (noto'g'ri — 一人前).",
                "Yaxshi bola (noto'g'ri — えらい/感心な)."]),
            q("t6-v6-32", "開放", [
                "犯人につかまっていた人質が開放された。",
                "この庭園は、日曜日だけ市民に開放される。",
                "旅行から帰ってきて、駅でみんな開放した。",
                "最近景気がようやく開放してきた。"], 2,
              "開放 (かいほう) = keng jamoatchilik uchun ochiq qilib qo'yish (eshigini ochish).",
              optsTr=[
                "Garovdagilar ozod qilindi (noto'g'ri — 解放).",
                "Ushbu bog' faqat yakshanba kunlari shahar aholisi uchun ochiq qilib qo'yiladi. (to'g'ri)",
                "Bekatda tarqaldi (noto'g'ri — 解散).",
                "Iqtisod tiklandi (noto'g'ri — 回復)."])
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
            q("t6-g1-33", "A「来週には退院できますか。」\nB「検査の結果（　）は、もっと早くできるかもしれませんよ。」",
              ["において", "によって", "にあたって", "について"], 2,
              "A: «Kelasi hafta shifoxonadan chiqa olamanmi?»\nB: «Tekshiruv natijasiga qarab, balki bundan ham tezroq chiqa olarsiz.»",
              expl="〜によって(は) = ...ga qarab, holatga bog'liq ravishda"),
            q("t6-g1-34", "電車でたまたま隣に座ったこと（　）、彼女と付き合い始めた。",
              ["をきっかけに", "をもとにして", "を通じて", "をめぐって"], 1,
              "Poyezdda tasodifan yonma-yon o'tirib qolishimiz turtki (sabab) bo'lib, u bilan uchrasha boshladik.",
              expl="〜をきっかけに = ...ni turtki/sabab qilib olib"),
            q("t6-g1-35", "彼は会社の社長だ（　）、従業員は2人しかいない。",
              ["というのに", "といったところで", "といっても", "といえば"], 3,
              "Kompaniya direktori deyilgani bilan, xodimlari atigi 2 kishidan iborat, xolos.",
              expl="〜といっても = ...deyilsa-da (aslida kutilganidan kam)"),
            q("t6-g1-36", "車による旅行は便利な（　）、疲れるし事故の危険性も高い。",
              ["他方", "反面", "反対", "半分"], 2,
              "Avtomobilda sayohat qilish qulay bo'lgani bilan, boshqa tomondan charchatadi va halokat xavfi ham yuqori.",
              expl="〜反面 (はんめん) = boshqa tomondan esa (qarama-qarshi xususiyat)"),
            q("t6-g1-37", "仕事が忙しく、結婚（　）彼女さえ見つけることができない。",
              ["するどころか", "したところで", "してみたところで", "するところが"], 1,
              "Ishim band bo'lib, uylanish tugul (u yoqda tursin), hatto sevgan qiz ham topa olmayapman.",
              expl="〜どころか = ...tugul, ...u yoqda tursin"),
            q("t6-g1-38", "みんな、くびになるのがこわい（　）だから、社長に何も言えないでいる。",
              ["もの", "こと", "ところ", "わけ"], 1,
              "Hamma ishdan haydalib ketishdan qo'rqqani sababli prezidentga hech narsa deya olmayapti.",
              expl="〜ものだから = ...bo'lgani sababli (sabab/oqlanish)"),
            q("t6-g1-39", "今（　）と思ったら、もう帰ってしまった。なんて忙しい人だ。",
              ["来るだろう", "来ないか", "来るものか", "来たか"], 4,
              "Endi keldimi desam, allaqachon qaytib ketibdi. Bunchalik band odam-a!",
              expl="〜かと思ったら = ...bo'ldi deb o'ylashim bilanoq (kutilmagan harakat)"),
            q("t6-g1-40", "今夜は妻がいないから、自分で料理を（　）。",
              ["作るはずがない", "作るしかない", "作りかねない", "作りようがない"], 2,
              "Bugun oqshom xotinim uyda yo'q, shuning uchun o'zim ovqat pishirishimdan boshqa chora yo'q.",
              expl="〜しかない = ...dan boshqa iloj yo'q"),
            q("t6-g1-41", "旅行会社に連絡（　）ので、旅行に参加するかしないか早く返事をください。",
              ["してはいけない", "しないといけない", "するのはいけない", "するわけにはいかない"], 2,
              "Sayyohlik agentligiga xabar berishim shart bo'lgani uchun, sayohatga borish-bormasligingiz haqida tezda javob bering.",
              expl="〜ないといけない = ...masam bo'lmaydi (shart)"),
            q("t6-g1-42", "パソコンが動かない。こうなったら買ったお店に修理を（　）。",
              ["頼むにほかならない", "頼むよりほかはない", "頼むほかよりない", "頼むほかにある"], 2,
              "Kompyuter ishlamayapti. Bunday bo'lgach, sotib olgan do'konga ta'mirlashni iltimos qilishdan boshqa iloj yo'q.",
              expl="〜よりほかはない = ...dan o'zga chora yo'q"),
            q("t6-g1-43", "B「ありがとう。（　）、幸せな家庭を作りたいです。」",
              ["結婚することには", "結婚しないことには", "結婚するからには", "結婚しないからには"], 3,
              "B: «Rahmat. Modomiki turmush qurar ekanmiz, baxtli oila barpo etmoqchiman.»",
              expl="〜からには = modomiki ... qilar ekanman (qatiy niyat)"),
            q("t6-g1-44", "お父さんは毎朝早く出かけるのだから、日曜くらいは（　）。",
              ["寝てあげなさい", "寝られてしまいなさい", "寝てしまいなさい", "寝かせておきなさい"], 4,
              "Dadang har kuni erta tongda ishga ketadi, shuning uchun yakshanba kuni hech bo'lmasa o'z holiga qo'yib uxlashiga qo'yib bering.",
              expl="〜ておきなさい = o'z holida qoldir (寝かせておきなさい = uxlashiga imkon ber)")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng to'g'ri bo'lakni tanlang.",
          "questions": [
            q("t6-g2-45", None, ["心配", "疲れ", "ようで", "気味の"], 3,
              "To'g'ri tartib: 部長は忙しすぎて疲れ気味のようで心配です。",
              prefix="部長は忙しすぎて", suffix="です。", starPos=3, order=[2, 4, 3, 1],
              expl="To'g'ri tartib: [疲れ][気味の][★ようで][心配] (2 → 4 → 3 → 1)"),
            q("t6-g2-46", None, ["近づいて", "行く", "どころでは", "台風が"], 2,
              "To'g'ri tartib: 明日は旅行の予定だが、台風が近づいて行くどころではなくなった。",
              prefix="明日は旅行の予定だが、", suffix="なくなった。", starPos=3, order=[4, 1, 2, 3],
              expl="To'g'ri tartib: [台風が][近づいて][★行く][どころでは] (4 → 1 → 2 → 3)"),
            q("t6-g2-47", None, ["言われて", "忘れて", "あると", "いながら"], 4,
              "To'g'ri tartib: 今日の朝早くから会議があると知っていながら、忘れてしまって遅刻した。",
              prefix="今日の朝早くから会議が", suffix="しまって、遅刻した。", starPos=2, order=[3, 1, 4, 2],
              expl="To'g'ri tartib: 会議が[あると][言われて][★いながら][忘れて] (3 → 1 → 4 → 2)"),
            q("t6-g2-48", None, ["だれが", "リーさんに", "見ても", "決まって"], 3,
              "To'g'ri tartib: B「もちろん、だれが見てもリーさんに決まっているよ。」",
              prefix="B「もちろん、", suffix="いるよ。」", starPos=3, order=[1, 3, 2, 4],
              expl="To'g'ri tartib: [だれが][見ても][★リーさんに][決まって] (1 → 3 → 2 → 4)"),
            q("t6-g2-49", None, ["やらないと", "体力に", "応じて", "かえって"], 1,
              "To'g'ri tartib: 運動はその人の体力に応じてやらないと、かえって体をこわしますよ。",
              prefix="運動はその人の", suffix="体をこわしますよ。", starPos=3, order=[2, 3, 1, 4],
              expl="To'g'ri tartib: [体力に][応じて][★やらないと][かえって] (2 → 3 → 1 → 4)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh joylariga eng to'g'ri variantni tanlang.",
          "passage_title": "現代の占いブーム",
          "passage": (
            "現代は科学の時代 {{50}} 、占いの好きな人は多い。朝のテレビ番組では、必ずといっていいほど、「今日の運勢」を取り上げているし、女性向けの雑誌の新年号は、「今年のあなたの運命」という特集を {{51}} 作れない。\n"
            "実は大会社の社長や政治家にも占い師に頼る人が少なくない。\n"
            "占いが科学的に正しいかどうかはわからない。しかし占い師はたくさんの人を見てきている。顔だけで「この人はどんな人か。何に悩んでいるか」とわかるのではないか。相談する人も悩みを {{52}} だけで心が軽くなるものだ。\n"
            "また、ある人が「こんな仕事を始めたいのだが」と相談して、占い師が「最初は苦労するけれど、かならず成功すると占いに出ています」と答えたとする。\n"
            "たとえば、3年やってなかなか成功せず {{53}} 、「占い師が『最初は苦労する』と言ってたな」と思い直して、その後さらに10年がんばって成功するかもしれない。\n"
            "生まれた日や名前や血液型で運命が {{54}} 。だが占いをうまく使えば、迷ったときに背中を押してくれたり、心を支えてくれるものになるのだ。"
          ),
          "passage_tr": (
            "Hozirgi davr ilm-fan zamoni bo'lishiga qaramasdan, folbinlikni yoqtiradiganlar ko'p. Ertalabki teledasturlarda «kunlik munajjimlar bashorati» ko'rsatiladi, ayollar jurnallarining yangi yil sonini esa fol mavzusisiz tayyorlab bo'lmaydi.\n"
            "Aslida yirik korporatsiyalar rahbarlari va siyosatchilar orasida ham munajjimlarga tayanadiganlar kam emas.\n"
            "Fol ilmiy jihatdan to'g'rimi-yo'qmi bilmaymiz, ammo folbinlar juda ko'p odamni ko'rishgan. Yuzining o'zidan uning qanday insonligini va nimadan qiynalayotganini bilib olishsa kerak. Maslahat so'rab borgan inson ham dardini eshittirib olishning (aytishning) o'zi bilan ko'ngli yengil tortadi.\n"
            "Yana biror kishi ish boshlamoqchi bo'lib borsa va «boshida qiynalasiz, ammo oxiri albatta omad keltiradi» deb aytsa, u inson 3 yil ishlab qiynalib taslim bo'layozganda «folbin boshida qiynalasan degandi-ku» deb o'zini qo'lga olib, yana 10 yil ishlab muvaffaqiyatga erishishi mumkin.\n"
            "Tug'ilgan kun, ism yoki qon guruhi bilan taqdir hal bo'lib qolmaydi, albatta. Ammo folbinlikdan to'g'ri foydalanilsa, ikkilanib turganda dadillik berib, ruhiy tayanch bo'la oladi."
          ),
          "questions": [
            q("t6-g3-50", None, ["にもかかわらず", "にかかわって", "にかけても", "につけても"], 1,
              "科学の時代[にもかかわらず]、占いの好きな人は多い = ilm-fan davri bo'lishiga qaramasdan.",
              blankNo="50", expl="〜にもかかわらず = ...bo'lishiga qaramay"),
            q("t6-g3-51", None, ["なければ", "ぬきには", "とわずに", "なくては"], 2,
              "特集を[ぬきには]作れない = maxsus maqolalarsiz chiqarib bo'lmaydi.",
              blankNo="51", expl="〜ぬきには = ...siz (amalga oshmaydi)"),
            q("t6-g3-52", None, ["聞いてあげる", "聞かせてあげる", "聞いてもらう", "聞かせてもらう"], 3,
              "悩みを[聞いてもらう]だけで心が軽くなる = dardini eshittirib olishning o'zi bilan.",
              blankNo="52", expl="〜てもらう = o'zi uchun qildirib olish"),
            q("t6-g3-53", None, ["あきらめられるが", "あきらめきれず", "あきらめるところを", "あきらめたのに"], 3,
              "なかなか成功せず[あきらめるところを] = taslim bo'layozgan joyida / arafasida.",
              blankNo="53", expl="〜ところを = ayni ... bo'layotgan vaziyatda"),
            q("t6-g3-54", None, ["決めるものがない", "決めることがない", "決まるものではない", "決まることはない"], 4,
              "運命が[決まることはない] = taqdir belgilanishi aslo yo'q (mumkin emas).",
              blankNo="54", expl="〜ことはない = aslo bunday bo'lmaydi / bunga hojat yo'q")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print(f"OK! test06.json yaratildi: {total} ta savol.")
