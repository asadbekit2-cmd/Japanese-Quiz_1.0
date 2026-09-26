# -*- coding: utf-8 -*-
"""
test02.json generatori — 第2回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.3
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test02.json")

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
  "id": 2,
  "title_jp": "第2回 模擬テスト",
  "title_uz": "2-test",
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
            q("t2-v1-1", "ネット環境が整えばオフィスに【縛られる】ことなく、どこにいても仕事ができる。",
              ["はめられる", "おさめられる", "とられる", "しばられる"], 4,
              "Internet muhiti yaxshilansa, ofisga bog'lanib qolmasdan (cheklanmasdan), qayerda bo'lsa ham ishlash mumkin.",
              reading="しばられる", expl="縛る → しばる (bog'lamoq, cheklamoq)"),
            q("t2-v1-2", "電車の中は、たくさんの子どもが乗っていて【騒々しかった】。",
              ["そうぞう", "ずうずう", "あらあら", "いまいま"], 1,
              "Poyezd ichida ko'plab bolalar ketayotgani sababli juda shovqin-suronli edi.",
              reading="そうぞうしかった", expl="騒々しい → そうぞうしい (shovqinli, g'ovur-g'uvur)"),
            q("t2-v1-3", "我が社は今年から面接の回数を増やして、知識より人物【重視】で社員を採用する。",
              ["ちょうし", "ちょうじ", "しゅうじ", "じゅうし"], 4,
              "Bizning kompaniya bu yildan suhbat sonini ko'paytirib, bilimdan ko'ra shaxsiyatga ahamiyat berib (muhim deb bilib) xodimlarni qabul qiladi.",
              reading="じゅうし", expl="重視 → じゅうし (muhim deb bilish, ahamiyat qaratish)"),
            q("t2-v1-4", "お買い物でためたポイントは、商品券に【交換】できます。",
              ["こうかん", "ごうがん", "こうがん", "ごうかん"], 1,
              "Xaridlar orqali to'plangan ballarni tovar kuponlariga almashtirish mumkin.",
              reading="こうかん", expl="交換 → こうかん (almashtirish, o'zaro almashuv)"),
            q("t2-v1-5", "スーパーでは食品の【包装】を少なくする活動が進んでいる。",
              ["ほうぞう", "ほうそう", "ほうそう", "ほうぞう"], 3,
              "Supermarketlarda oziq-ovqatlarni qadoqlashni (o'rab-chirmashni) kamaytirish bo'yicha harakatlar olib borilmoqda.",
              reading="ほうそう", expl="包装 → ほうそう (qadoqlash, o'rash)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t2-v2-6", "太陽エネルギーが生み出す熱は【だんぼう】に、光は電気に利用できる。",
              ["暖房", "暖冒", "断房", "断冒"], 1,
              "Quyosh energiyasi hosil qiladigan issiqlik isitish tizimiga, yorug'lik esa elektrga ishlatilishi mumkin.",
              reading="だんぼう", expl="暖房 → だんぼう (isitish tizimi)"),
            q("t2-v2-7", "あの2人は夫婦だと【かんちがい】している人が多い。",
              ["勘違い", "肝違い", "感違い", "塞違い"], 1,
              "U ikki kishini er-xotin deb yanglish (noto'g'ri tushunadigan) o'ylaydigan odamlar ko'p.",
              reading="かんちがい", expl="勘違い → かんちがい (yanglishish, noto'g'ri tushunish)"),
            q("t2-v2-8", "常識に【てらして】考えてみれば、君が今、何をすべきかわかるだろう。",
              ["焦らして", "燃らして", "照らして", "烈らして"], 3,
              "Umumiy qoidalar (aql-idrok) bilan qiyoslab (solishtirib) ko'rsang, hozir nima qilishing kerakligi ayon bo'ladi.",
              reading="てらして", expl="照らす → てらす (solishtirmoq, qiyoslamoq; yoritmoq)"),
            q("t2-v2-9", "このあたりは地震で【じばん】が沈んでしまった。",
              ["地敷", "地版", "地番", "地盤"], 4,
              "Bu atrofda zilzila oqibatida yer poydevori (tuproq qatlami) cho'kib ketdi.",
              reading="じばん", expl="地盤 → じばん (yer sathi, poydevor tuproq)"),
            q("t2-v2-10", "工場の事故で有害物質が流れ、川が【おせん】された。",
              ["汚洗", "御染", "汚染", "冒染"], 3,
              "Zavod halokati tufayli zararli moddalar oqib, daryo ifloslandi.",
              reading="おせん", expl="汚染 → おせん (ifloslanish, zaharlanish)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t2-v3-11", "インドのガンジーは（　）暴力を信条に独立運動を指導した。",
              ["無", "反", "非", "不"], 3,
              "Hindistonlik Gandi zo'ravonliksiz (tinchlik) tamoyiliga tayanib, mustaqillik harakatiga boshchilik qildi.",
              expl="非暴力 (ひぼうりょく) = zo'ravonliksizlik tamoyili"),
            q("t2-v3-12", "山田氏は、個性（　）俳優として活躍している。",
              ["人", "風", "流", "派"], 4,
              "Yamada janoblari o'ziga xos uslubdagi (individual tipdagi) aktyor sifatida faoliyat yuritmoqda.",
              expl="個性派 (こせいは) = o'ziga xos individual yo'nalishga ega bo'lgan shaxs/aktyor"),
            q("t2-v3-13", "全社員に劇場の改善（　）を開く。",
              ["点", "見", "場", "所"], 1,
              "Barcha xodimlardan teatrni yaxshilash nuqtalari (takliflari) so'raladi.",
              expl="改善点 (かいぜんてん) = yaxshilanishi kerak bo'lgan jihatlar/nuqtalar"),
            q("t2-v3-14", "自然（　）の法則には逆らえない。",
              ["方", "側", "界", "世"], 3,
              "Tabiat olami qonuniyatlariga qarshi chiqib bo'lmaydi.",
              expl="自然界 (しぜんかい) = tabiat olami / tabiat dunyosi"),
            q("t2-v3-15", "子どもたちは（　）年齢とあって、すぐに仲よくなった。",
              ["近", "同", "何", "当"], 2,
              "Bolalar tengdosh bo'lganlari sababli, darrov do'stlashib ketishdi.",
              expl="同年齢 (どうねんれい) = tengdosh, bir yoshdagi")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ( ) ga ma'no jihatidan eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t2-v4-16", "サークルのホームページに「イベント情報」を追加し、（　）した。",
              ["制作", "工事", "閉鎖", "更新"], 4,
              "To'garakning veb-saytiga «Tadbirlar ma'lumoti»ni qo'shib, yangiladik (update qildik).",
              expl="更新 (こうしん) = yangilash, yangi ma'lumot kiritish"),
            q("t2-v4-17", "最も（　）な成績の学生には、大学から学長賞が贈られます。",
              ["上等", "優秀", "有効", "優良"], 2,
              "Eng a'lo natija ko'rsatgan talabaga universitet tomonidan rektor mukofoti beriladi.",
              expl="優秀 (ゆうしゅう) = a'lo, yetakchi, iqtidorli"),
            q("t2-v4-18", "買い物という日常的な行いが、消費を（　）して世の中を元気にする。",
              ["重視", "指導", "活用", "刺激"], 4,
              "Xarid qilish kabi kundalik odat iste'molni rag'batlantirib (kuchaytirib), jamiyatni jonlantiradi.",
              expl="刺激 (しげき) = rag'batlantirish, qo'zg'atish"),
            q("t2-v4-19", "バスがなかなか来なくて、待っている人たちは次第に（　）し始めた。",
              ["いらいら", "ぶつぶつ", "のろのろ", "まごまご"], 1,
              "Avtobus aslo kelavermagach, kutayotgan odamlar asta-sekin asabiylasha (g'azablana) boshladi.",
              expl="いらいら = asabiylashish, betoqat bo'lish"),
            q("t2-v4-20", "日本の寿司を（　）した洋風の寿司が海外で人気だ。",
              ["アプローチ", "アレンジ", "アシスト", "アドバイス"], 2,
              "Yapon sushisini moslashtirgan (modifikatsiya qilgan) g'arbona sushi chet elda mashhur.",
              expl="アレンジ (arrange) = yangicha talqin qilish, moslashtirish"),
            q("t2-v4-21", "幸福が（　）に続くことはありえないのだろうか。",
              ["長期", "不変", "永遠", "不滅"], 3,
              "Baxt abadiy davom etishi mumkin emasmi-a?",
              expl="永遠に (えいえんに) = abadiy, mangu"),
            q("t2-v4-22", "あの大企業の社長は自分にはこれといった才能はないと（　）している。",
              ["謙遜", "遠慮", "配慮", "恐縮"], 1,
              "U ulkan korporatsiya prezidenti o'zida aytarli iste'dod yo'qligini kamtarlik bilan aytadi.",
              expl="謙遜 (けんそん) = kamtarlik qilish")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin sinonimni tanlang.",
          "questions": [
            q("t2-v5-23", "試合に負けた悔しさを【味わった】。",
              ["記録した", "発表した", "重視した", "経験した"], 4,
              "O'yinda yutqazish alamini totib ko'rdim (boshdan kechirdim).",
              reading="あじわった", expl="味わう → 経験した (boshdan kechirish, his qilish)"),
            q("t2-v5-24", "旅先で【偶然】昔の友人に出会った。",
              ["約束通り", "思いがけなく", "確かに", "都合よく"], 2,
              "Sayohat paytida kutilmaganda (tasodifan) eski do'stimni uchratib qoldim.",
              reading="ぐうぜん", expl="偶然 → 思いがけなく (kutilmaganda, tasodifan)"),
            q("t2-v5-25", "工場の【単調な】作業にあきてきた。",
              ["変化がない", "よく変わる", "手間がかかる", "休みがない"], 1,
              "Zavoddagi bir xil (zerikarli, monoton) ishdan zerikib qoldim.",
              reading="たんちょうな", expl="単調な → 変化がない (o'zgarishsiz, monoton)"),
            q("t2-v5-26", "負けて困っているところに、【強力な】味方が現れた。",
              ["のんびりした", "予想しない", "頼りになる", "元気のよい"], 3,
              "Yutqazib qiynalib turganda, kuchli (suyanadigan, ishonchli) ittifoqchi paydo bo'ldi.",
              reading="きょうりょくな", expl="強力な → 頼りになる (ishonchli, suyansa bo'ladigan)"),
            q("t2-v5-27", "彼は【バイリンガル】だ。",
              ["国際性がある", "物知りだ", "二カ国語を話す", "二重国籍だ"], 3,
              "U ikki tilda gaplashuvchi (bilingual) shaxsdir.",
              expl="バイリンガル = 二カ国語を話す (ikki tilda so'zlasha oladigan)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilgan gapini tanlang.",
          "questions": [
            q("t2-v6-28", "反映", [
                "彼は酒を飲むとすぐに本性を反映する。",
                "隠していた事実がついに世間に反映されてしまった。",
                "客の希望を反映して、配達のサービスを始めた。",
                "黒のドレスは色白の女性の美しさを特に反映していた。"], 3,
              "反映 (はんえい) = aks ettirish, inobatga olish.",
              optsTr=[
                "U ichgach o'z xarakterini 'aks ettiradi' (noto'g'ri — 現す).",
                "Yashiringan haqiqat omma orasida 'aks etdi' (noto'g'ri — 知れ渡った).",
                "Mijozlarning istaklarini inobatga olib (aks ettirib), yetkazib berish xizmatini yo'lga qo'ydik. (to'g'ri)",
                "Qora ko'ylak oqtanli ayol go'zalligini 'aks ettirdi' (noto'g'ri — 引き立てる)."]),
            q("t2-v6-29", "ためいき", [
                "話がおもしろくてためいきが出た。",
                "苦手な上司の声を聞いただけで、ぞっとためいきが出る。",
                "息子のひどい成績に母は思わずためいきをついた。",
                "プールに入る前に、ためいきをしてください。"], 3,
              "ためいき (溜め息) = chuqur xo'rsinish, nafas chiqarish.",
              optsTr=[
                "Gap qiziq bo'lgani uchun 'xo'rsindim' (noto'g'ri — 笑った).",
                "Yoqtirmaydigan boshliq ovozidan qo'rqib 'xo'rsindi' (noto'g'ri).",
                "O'g'lining yomon baholarini ko'rib ona beixtiyor chuqur xo'rsinib qo'ydi. (to'g'ri)",
                "Basseynga tushishdan oldin 'xo'rsinib oling' (noto'g'ri — 準備運動)."]),
            q("t2-v6-30", "特殊", [
                "動物には、人間にない特殊な能力を持つものが多い。",
                "夜中に特殊な物音がして目が覚めた。",
                "彼って特殊にもてるけど、どこがいいのかしらね。",
                "今日は特殊にあなただけにプレゼントをあげます。"], 1,
              "特殊 (とくしゅ) = o'ziga xos, maxsus, g'ayrioddiy.",
              optsTr=[
                "Hayvonlar orasida insonda bo'lmagan o'ziga xos (maxsus) qobiliyatga ega bo'lganlari ko'p. (to'g'ri)",
                "Tunda 'maxsus' tovush eshitilib uyg'ondim (noto'g'ri — 奇妙な).",
                "U 'maxsus' mashhur (noto'g'ri — やたら).",
                "Bugun 'maxsus' sovg'a beraman (noto'g'ri — 特別)."]),
            q("t2-v6-31", "加速度", [
                "授業は個々の生徒の能力に合った加速度で進める。",
                "もう少し加速度をつけないと時間に遅れてしまう。",
                "あの人とはなぜか話の加速度が合わない。",
                "地上を離れた飛行機は一気に加速度を増した。"], 4,
              "加速度 (かそくど) = tezlanish (akseleratsiya).",
              optsTr=[
                "Darsni har bir o'quvchi qobiliyatiga mos 'tezlanish' bilan o'tamiz (noto'g'ri — ペース/速度).",
                "Biroz 'tezlanish' qo'shmasak kech qolamiz (noto'g'ri — スピード).",
                "U bilan gapning 'tezlanishi' to'g'ri kelmaydi (noto'g'ri — テンポ).",
                "Yerdan ko'tarilgan samolyot birdaniga tezlanishini oshirdi. (to'g'ri)"]),
            q("t2-v6-32", "矛盾", [
                "私は工場建設に賛成の彼とは矛盾する立場にある。",
                "2人は最初から最後まで矛盾ばかりだ。",
                "税金は安くして行政サービスはよくしろだなんて、矛盾している。",
                "やっぱり聞くことと見るのでは矛盾している。"], 3,
              "矛盾 (むじゅん) = qarama-qarshilik, zidlik (mantiqsizlik).",
              optsTr=[
                "Men zavod qurilishini qo'llagan u kishi bilan 'zid' pozitsiyadaman (noto'g'ri — 対立).",
                "Ikkovi boshidan oxirigacha 'zid' (noto'g'ri — 口喧嘩).",
                "Soliqni arzon qilib, davlat xizmatlarini yaxshilang deyish — mantiqan qarama-qarshidir (ziddir). (to'g'ri)",
                "Eshitish bilan ko'rish 'zid' (noto'g'ri — 異なる)."])
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
            q("t2-g1-33", "お金がない（　）ではないが、必要ないものは買わないことにしている。",
              ["わけ", "こと", "もの", "どころ"], 1,
              "Puli yo'q degani emas-ku, ammo keraksiz narsani sotib olmaslikka qaror qilganman.",
              expl="〜わけではない = mutlaqo ... degani emas (qisman rad etish)"),
            q("t2-g1-34", "これから大急ぎで行った（　）、授業に間に合わないだろう。",
              ["としたら", "としても", "とすると", "となれば"], 2,
              "Hozirdan juda shoshib borgan taqdirda ham, baribir darsga ulgura olmasak kerak.",
              expl="〜としても = garchi ... bo'lgan taqdirda ham"),
            q("t2-g1-35", "友人とおしゃべりをしている（　）、別の友人から電話がかかってきた。",
              ["最中に", "直後に", "途端に", "瞬間に"], 1,
              "Do'stim bilan gurunglashib turgan ayni paytimda boshqa bir do'stimdan qo'ng'iroq bo'lib qoldi.",
              expl="〜最中に (さいちゅうに) = ayni ... qilib turgan fursatda"),
            q("t2-g1-36", "この小さな絵が1億円もするなんて、（　）ですね。",
              ["信じかねない", "信じるしかない", "信じがたい", "信じざるを得ない"], 3,
              "Bu kichkina surat 100 million iyen turadi deb ishonish juda qiyin-a!",
              expl="〜がたい = qilish/tasavvur qilish juda mushkul, qiyin"),
            q("t2-g1-37", "こんな難しい本は売れないだろうという予想（　）、10万冊以上売れた。",
              ["に対して", "に応じて", "に当たって", "に反して"], 4,
              "Bunday qiyin kitob sotilmaydi degan taxminga zid ravishda, 100 ming nusxadan ziyod sotildi.",
              expl="〜に反して (にはんして) = ...ga qarama-qarshi o'laroq, zid bo'lib"),
            q("t2-g1-38", "もう二度と失敗は（　）と思ったのに、またやってしまった。",
              ["するものか", "するものか", "しないものだ", "しないものか"], 2,
              "Boshqa aslo xato qilmayman deb qat'iy o'ylagan edim, ammo yana qilib qo'ydim.",
              expl="〜ものか = aslo ...mayman (qat'iy inkor qarori)"),
            q("t2-g1-39", "A「お久しぶりです。」\nB「本当に。（　）言えば、お父さまの病気はその後、いかがですか。」",
              ["もう", "こう", "そう", "どう"], 3,
              "A: «Ko'rishmaganimizga ancha bo'ldi-ya!»\nB: «Haqiqatan ham. Shu mavzu esga tushgan ekan, otangizning betobligi shundan so'ng qanday bo'ldi?»",
              expl="そう言えば = aytgancha, shu esimga tushdi"),
            q("t2-g1-40", "私が結婚（　）がしまいが、あなたには関係ないことだ。",
              ["したい", "した", "しよう", "しない"], 3,
              "Men turmush quramanmi yoki qurmaymanmi — bu sizga aloqasi bo'lmagan ishdir.",
              expl="〜ようが〜まいが = qilsam ham, qilmasam ham (baribir)"),
            q("t2-g1-41", "この薬の粒は大きすぎて、とても（　）。",
              ["飲みすぎない", "飲みかねない", "飲みやすい", "飲みにくい"], 4,
              "Bu dorining donasi juda katta bo'lgani uchun, yutish juda noqulay (qiyin).",
              expl="〜にくい = qilish/yutish qiyin, noqulay"),
            q("t2-g1-42", "A「たばこを吸っても、必ず病気になるわけではないだろう。」\nB「それでも医者にすれば、禁煙を（　）。」",
              ["指導するしかないよ", "指導するわけがないよ", "指導するどころではないよ", "指導するはずがないよ"], 1,
              "A: «Chekkan bilan hamma ham kasal bo'lavermaydi-ku.»\nB: «Shunday bo'lsa-da shifokor nazdida, chekishni tashlashni tavsiya qilishdan boshqa chora yo'q.»",
              expl="〜しかない = ...dan boshqa iloj/chora yo'q"),
            q("t2-g1-43", "会社の一駅前で降りて（　）、3カ月で体重がかなり減った。",
              ["歩くようにしたものの", "歩くようにしたところ", "歩くようにしたものが", "歩くようにしたところで"], 2,
              "Kompaniyadan bir bekat oldin tushib piyoda yurishga odatlangan edim, 3 oyda vaznim ancha kamaydi.",
              expl="〜たところ = ...qilgan edimki, natijada..."),
            q("t2-g1-44", "会議に出席できなかったので、資料を（　）",
              ["お見せいただけますか", "見られていただけますか", "見ていただけますか", "見せていただけますか"], 4,
              "Yig'ilishda qatnasha olmaganim sababli, materiallarni ko'rsatib bera olasizmi?",
              expl="見せていただけますか = ko'rsatib bera olasizmi (xushmuomala so'rov: 〜ていただく)")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng to'g'ri bo'lakni tanlang.",
          "questions": [
            q("t2-g2-45", None, ["忘れてしまう", "忘れない", "ので", "そばから"], 3,
              "To'g'ri tartib: 難しい漢字は、習うそばから忘れてしまうので、忘れないうちにきちんと復習しよう。",
              prefix="難しい漢字は、習う", suffix="うちにきちんと復習しよう。", starPos=3, order=[4, 1, 3, 2],
              expl="To'g'ri tartib: 習う[そばから][忘れてしまう][★ので][忘れない] (4 → 1 → 3 → 2)"),
            q("t2-g2-46", None, ["でも", "では", "次第", "話し方"], 4,
              "To'g'ri tartib: 同じ言葉でも、話し方次第では印象が変わってしまうことがある。",
              prefix="同じ言葉", suffix="印象が変わってしまうことがある。", starPos=2, order=[1, 4, 3, 2],
              expl="To'g'ri tartib: 同じ言葉[でも][★話し方][次第][では] (1 → 4 → 3 → 2)"),
            q("t2-g2-47", None, ["最初の", "限って", "無料", "レッスンに"], 2,
              "To'g'ri tartib: この学校では、最初のレッスンに限って無料で受けることができます。",
              prefix="この学校では、", suffix="で受けることができます。", starPos=3, order=[1, 4, 2, 3],
              expl="To'g'ri tartib: [最初の][レッスンに][★限って][無料] (1 → 4 → 2 → 3)"),
            q("t2-g2-48", None, ["の", "わりには", "年齢", "ピアノ"], 1,
              "To'g'ri tartib: この子は年齢のわりにはピアノが上手だ。",
              prefix="この子は", suffix="が上手だ。", starPos=2, order=[3, 1, 2, 4],
              expl="To'g'ri tartib: この子は[年齢][★の][わりには][ピアノ] (3 → 1 → 2 → 4)"),
            q("t2-g2-49", None, ["取る", "成績から", "こんな成績を", "見ても"], 3,
              "To'g'ri tartib: あの学生の今までの成績から見ても、こんな成績を取るなんて信じられない。",
              prefix="あの学生の今までの", suffix="なんて信じられない。", starPos=3, order=[2, 4, 3, 1],
              expl="To'g'ri tartib: [成績から][見ても][★こんな成績を][取る] (2 → 4 → 3 → 1)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh joylariga eng to'g'ri variantni tanlang.",
          "passage_title": "寿司の歴史と工夫",
          "passage": (
            "あなたは日本のすし屋のカウンターで、「お好み」ですしを食べたことがありますか。\n"
            "カウンターのケースの中を見ながら、好きな魚を選び、それを注文して、にぎってもらうので、いちばんおいしい状態で食べられます。ただ自分がどれくらい食べたか、金額が {{50}} 注意が必要です。\n"
            "このとき、たとえば「マグロ」と注文すると、通常、マグロのすしが2つ出てきます。なぜそうなのか。江戸時代のおすしは大きかったので、2つに切って出したなごりとか、計算しやすくするためだとか、いろいろな説があります。結局、はっきりとはわからなくて、「昔からそうなっている」としか {{51}} 。\n"
            "ところで、この場合、 {{52}} で行けば食べればいいけれど、1人で行って10個食べるとしたら、魚は5種類しか食べられません。ある回転ずし店で、1枚の皿に違う種類のすしを1つずつ2個、乗せ始めました。これなら、食べた寿司の数だけ {{53}} が食べられるので人気が出て、客が増えたそうです。考えたら単純なアイデアです。でも「昔からそうなっている」ことをちょっと変えてみる、そこにお客が増えるかぎがありました。\n"
            "私たちの身の回りにも、「ちょっと変えてみたらよくなる」ことがたくさんあるかもしれません。常識 {{54}} 、頭を柔らかくしておくことが大事なのです。"
          ),
          "passage_tr": (
            "Siz Yaponiyadagi sushi restoranining bar peshtaxtasida «o'z xohishingiz bo'yicha» (okonomi) sushi yeb ko'rganmisiz?\n"
            "Vitrindagi baliqlarni ko'rib turib, yoqtirganingizni tanlab buyurtma berasiz va yangi tayyorlab beriladi, shuning uchun eng mazali holatida yeya olasiz. Faqat qancha yeganingiz va pul miqdorini payqash qiyin bo'lgani sababli ehtiyotkorlik zarur.\n"
            "Bu paytda, masalan «Maguro» deb buyurtma bersangiz, odatda 2 dona maguro sushisi keltiriladi. Nega unday? Edo davridagi sushi katta bo'lgani uchun ikkiga bo'lib berilganidan qolgan odat degan yoki hisob-kitobni osonlashtirish uchun degan turli qarashlar bor. Yakunda aniq ma'lum bo'lmay, «qadimdan shunday bo'lib kelgan» deb aytishdan boshqa chora yo'q.\n"
            "Aytgancha, bunday vaziyatda 2 kishi bo'lib borsangiz yaxshi-ku, lekin 1 kishi borib 10 dona yesa, atigi 5 xil baliqni tatib ko'ra oladi, xolos. Bir aylanma sushi do'koni 1 ta likopchaga 2 xil sushidan bittadan qo'yib bera boshladi. Shunday qilinganda yegan sushi sonicha har xil sushilarni yeyish mumkinligi sababli juda ommalashdi. O'ylab ko'rsa oddiy g'oya. Biroq «qadimdan shunday bo'lgan» narsani biroz o'zgartirib ko'rish — mijozlarni jalb qilish siri shu yerda edi.\n"
            "Bizning atrofimizda ham «biroz o'zgartirsa yaxshi bo'ladigan» jihatlar juda ko'p bo'lishi mumkin. Qotib qolgan tushunchalarga yopishib olmasdan, fikrlashni moslashuvchan tutish muhimdir."
          ),
          "questions": [
            q("t2-g3-50", None, ["わかりやすいので", "わかってしまうので", "わかりづらいので", "わかりかねないので"], 3,
              "金額が[わかりづらいので]注意が必要です = hisob-kitob miqdorini bilish qiyin bo'lgani uchun.",
              blankNo="50", expl="〜づらい = bilish/aniqlash mushkul"),
            q("t2-g3-51", None, ["言えるでしょう", "言いようがありません", "言いかねません", "言うまでもありません"], 2,
              "昔からそうなっているとしか[言いようがありません] = «qadimdan shunday» deb aytishdan boshqa so'z yo'q.",
              blankNo="51", expl="〜ようがない = aytishning/qilishning hech bir yo'li yo'q"),
            q("t2-g3-52", None, [
                "a 1人 ／ b 1個ずつ ／ c 1人",
                "a 1人 ／ b 2個ずつ ／ c 2人",
                "a 2人 ／ b 1個ずつ ／ c 1人",
                "a 2人 ／ b 2個ずつ ／ c 1人"], 3,
              "2人で行けば1個ずつ食べればいいけれど、1人で行って... (2 kishi borsa 1 donadan yeydi).",
              blankNo="52", expl="Tartib: 2人 (a) / 1個ずつ (b) / 1人 (c)"),
            q("t2-g3-53", None, ["同じすし", "たくさんのすし", "全部のすし", "いろいろなすし"], 4,
              "食べた寿司の数だけ[いろいろなすし]が食べられる = yeganicha har xil turlarini yeyish mumkin.",
              blankNo="53", expl="Turli baliq turlarini tatib ko'rish haqida: いろいろなすし"),
            q("t2-g3-54", None, ["にとらわれないで", "をこわさないように", "にかかわらないで", "をぬきにして"], 1,
              "常識[にとらわれないで]、頭を柔らかくしておくことが大事 = qolipga yopishib qolmasdan.",
              blankNo="54", expl="〜にとらわれる = biror tushunchaga bandi/cheklanib qolish (にとらわれないで = cheklanmasdan)")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print(f"OK! test02.json yaratildi: {total} ta savol.")
