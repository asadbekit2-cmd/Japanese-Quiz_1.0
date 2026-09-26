# -*- coding: utf-8 -*-
"""
test04.json generatori — 第4回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.5
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test04.json")

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
  "id": 4,
  "title_jp": "第4回 模擬テスト",
  "title_uz": "4-test",
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
            q("t4-v1-1", "ロボットは、工場はもちろん国際宇宙ステーションまで、【至る所】で使われている。",
              ["いわゆる", "あらゆる", "いたる", "とおる"], 3,
              "Robotlar fabrikalarda-ku mayli, Xalqaro kosmik stansiyagacha — har bir yerda (hamma joyda) qo'llanilmoqda.",
              reading="いたる", expl="至る所 → いたるところ (hamma joyda, har burchakda)"),
            q("t4-v1-2", "10日前までに予約をすると、早期【割引】で宿泊料金が安くなる。",
              ["わりひき", "わりびき", "かつひき", "かつびき"], 2,
              "10 kun oldin band qilsangiz, erta chegirma (skidka) bilan mehmonxona narxi arzonlashadi.",
              reading="わりびき", expl="割引 → わりびき (chegirma, skidka)"),
            q("t4-v1-3", "机に向かっているときより、散歩中に仕事の【発想】がわいてくることが多い。",
              ["はっそう", "はつそう", "ほっそう", "はつぞう"], 1,
              "Stol atrofida o'tirgandan ko'ra, sayr qilayotganda ish bo'yicha yangi g'oyalar quyilib kelishi ko'proq uchraydi.",
              reading="はっそう", expl="発想 → はっそう (g'oya, fikr uyg'onishi)"),
            q("t4-v1-4", "金銭感覚のなかった父に、母はずっと苦労させられていた。",
              ["かんがく", "かんかく", "がんかく", "がんがく"], 2,
              "Pul qadrini his qilmaydigan (isrofgar) otam tufayli onam uzoq vaqt qiynalib yashagan.",
              reading="かんかく", expl="感覚 → かんかく (hissiyot, sezgi)"),
            q("t4-v1-5", "結婚は人生の一大事だから【慎重】に考えなさい。",
              ["じんじゅう", "しんじゅう", "じんちょう", "しんちょう"], 4,
              "Nikoh inson umrining muhim voqeasi bo'lgani sababli, ehtiyotkorlik (vazminlik) bilan o'yla.",
              reading="しんちょう", expl="慎重 → しんちょう (ehtiyotkor, vazmin, puxta)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t4-v2-6", "あの子はまるでスポンジのように教えたことはすべて【きゅうしゅう】する。",
              ["吸集", "究収", "吸収", "急就"], 3,
              "U bola xuddi gubka (sponj) kabi o'rgatilgan barcha narsani o'ziga singdirib (yutib) oladi.",
              reading="きゅうしゅう", expl="吸収 → きゅうしゅう (singdirish, shimib olish)"),
            q("t4-v2-7", "あの学者は、この島に長期【たいざい】して、植物の研究をしている。",
              ["滞存", "滞在", "帯存", "帯在"], 2,
              "U olim ushbu orolda uzoq muddat yashab (turib), o'simliklarni tadqiq qilmoqda.",
              reading="たいざい", expl="滞在 → たいざい (vaqtincha istiqomat qilish, turish)"),
            q("t4-v2-8", "家族みんなで食卓を【かこむ】ことが少なくなってしまった。",
              ["因む", "図む", "回む", "囲む"], 4,
              "Oila a'zolari birgalikda dasturxon atrofida jamlanishi (o'tirishi) kamayib ketdi.",
              reading="かこむ", expl="囲む → かこむ (o'rab olmoq, atrofida o'tirmoq)"),
            q("t4-v2-9", "娘はチラシの体験談を【あんい】に信じて高いサプリメントをよく買っている。",
              ["安意", "安易", "案意", "案易"], 2,
              "Qizim reklamadagi fikrlarga osongina (yengil-yelpi) ishonib, qimmatbaho qo'shimchalarni sotib olaveradi.",
              reading="あんい", expl="安易 → あんい (yengil-yelpi, osongina)"),
            q("t4-v2-10", "警察犬はトラックの中の爆発物を【かぎ】あてた。",
              ["嗅ぎ", "咲ぎ", "喝ぎ", "喫ぎ"], 1,
              "Xizmat iti yuk mashinasi ichidagi portlovchi moddani hidlab topdi.",
              reading="かぎ", expl="嗅ぐ → かぐ (hidlamoq, hid bilmoq)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t4-v3-11", "夜中に大声で騒ぐなんて（　）常識だ。",
              ["無", "不", "非", "反"], 3,
              "Tunning yarmida baland ovozda baqirib shovqin solish — beodoblikdir (aqlsizlikdir).",
              expl="非常識 (ひじょうしき) = odobsizlik, madaniyatsizlik"),
            q("t4-v3-12", "部長は1日中（　）機嫌だった。",
              ["悪", "非", "無", "不"], 4,
              "Bo'lim boshlig'i kun bo'yi xomush (kayfiyatsiz) yurdi.",
              expl="不機嫌 (ふきげん) = kayfiyatsiz, jahldor holat"),
            q("t4-v3-13", "2人の意見の対立が表面（　）する。",
              ["化", "出", "下", "現"], 1,
              "Ikki kishining fikr qarama-qarshiligi yuzaga chiqadi (oshkor bo'ladi).",
              expl="表面化 (ひょうめんか) = oshkoralashish, yuzaga chiqish"),
            q("t4-v3-14", "今回の選挙の投票（　）は高かった。",
              ["性", "量", "率", "比"], 3,
              "Bu galgi saylovda qatnashish foizi (davomat ko'rsatkichi) yuqori bo'ldi.",
              expl="投票率 (とうひょうりつ) = saylovda qatnashish foizi / davomat ko'rsatkichi"),
            q("t4-v3-15", "（　）料理を友人にふるまう。",
              ["和", "家", "新", "手"], 4,
              "O'z qo'lim bilan tayyorlagan taomni do'stimga mehmon qilib tortiq qilaman.",
              expl="手料理 (てりょうり) = o'z qo'li bilan tayyorlagan taom")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ( ) ga ma'no jihatidan eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t4-v4-16", "天然ガスの利用は世界のエネルギー（　）を変えるであろう。",
              ["展開", "事情", "事態", "体制"], 2,
              "Tabiiy gazdan foydalanish butun dunyodagi energiya holatini (vaziyatini) o'zgartirsa kerak.",
              expl="エネルギー事情 (エネルギーじじょう) = energetika vaziyati/holati"),
            q("t4-v4-17", "小柄な母は体に（　）する服を探すのにいつも苦労している。",
              ["フィット", "セット", "マット", "カット"], 1,
              "Qaddi-qomati kichik onam tanasiga mos tushadigan (fit bo'ladigan) kiyim topishga doim qiynaladi.",
              expl="フィットする (fit) = mos tushmoq, loyiq kelmoq"),
            q("t4-v4-18", "畑作りは生きている命を（　）いるので、今週は忙しいから、水やりは来週というわけにはいかない。",
              ["耕して", "稼いで", "整って", "扱って"], 4,
              "Ekin ekish tirik jon bilan muomala qilish (parvarishlash) bo'lgani sababli, suv quyishni kelasi haftaga qoldirib bo'lmaydi.",
              expl="扱う (あつかう) = muomala qilmoq, parvarishlamoq"),
            q("t4-v4-19", "これは（　）私の意見にすぎません。他の人はたぶん違う意見だと思います。",
              ["あくまでも", "おそらく", "いわゆる", "ほとんど"], 1,
              "Bu faqatgina (qat'iy qilib aytganda) mening shaxsiy fikrim, xolos. Boshqalar boshqacha fikrda bo'lsa kerak.",
              expl="あくまでも = faqatgina, mutlaqo (あくまでも〜にすぎない)"),
            q("t4-v4-20", "意見があれば何でも（　）なく私に言ってください。",
              ["援助", "失敗", "文句", "遠慮"], 4,
              "Fikringiz bo'lsa, hech qanday tortinishsiz (uyalmasdan) menga aytavering.",
              expl="遠慮なく (えんりょなく) = tortinmasdan, bemalol"),
            q("t4-v4-21", "長い行列の真ん中に、1人の女性が（　）割り込んできた。",
              ["ちからづよく", "そそっかしく", "ずうずうしく", "くだらなく"], 3,
              "Uzun navbatning o'rtasiga bir ayol surbetlarcha (uyalmasdan) suqilib kirdi.",
              expl="ずうずうしく = surbetlarcha, yuzsizlarcha"),
            q("t4-v4-22", "法律が（　）され、傘を差したまま自転車に乗るのは禁止された。",
              ["改良", "補助", "改正", "統制"], 3,
              "Qonun qayta ko'rib chiqilib (o'zgartirilib), soyabon ushlagan holda velosiped haydash taqiqlandi.",
              expl="改正 (かいせい) = qonun yoki qoidani o'zgartirish/tuzatish")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin sinonimni tanlang.",
          "questions": [
            q("t4-v5-23", "給料前の急な出費は【痛い】。",
              ["とても困る", "予定が狂う", "頭に来る", "不安だ"], 1,
              "Oylik olish oldidan to'satdan chiqqan xarajat juda qiyin (juda noqulay, ziyonli).",
              reading="いたい", expl="痛い = とても困る (juda qiyin, noqulay, og'ir botadi)"),
            q("t4-v5-24", "春先の低温が【響き】、野菜の値段が高くなった。",
              ["続いて", "影響して", "戻って", "ひどくて"], 2,
              "Bahor boshidagi sovuq havo ta'sir qilib, sabzavotlar narxi ko'tarildi.",
              reading="ひびき", expl="響く → 影響して (ta'sir qilmoq, oqibat keltirmoq)"),
            q("t4-v5-25", "自分の荷物は【めいめいで】気をつけてください。",
              ["毎回", "お互いに", "各自", "常に"], 3,
              "O'z yukingizga har bir kishi o'zi (alohida-alohida) hushyor bo'lsin.",
              reading="めいめいで", expl="めいめいで = 各自 (かくじ — har bir kishi o'zi alohida)"),
            q("t4-v5-26", "女性の社会進出には子育てという大きな【壁】がある。",
              ["障害", "仕事", "苦労", "心配"], 1,
              "Ayollarning jamiyatda faol bo'lishida bola parvarishi kabi katta to'siq (g'ov) mavjud.",
              reading="かべ", expl="壁 = 障害 (しょうがい — to'siq, g'ov)"),
            q("t4-v5-27", "オフは【もっぱら】テレビを見て過ごす。",
              ["週末", "昼休み", "祝日", "休みの日"], 4,
              "Dam olish kunlarini (off) asosan televizor ko'rib o'tkazaman.",
              expl="オフ = 休みの日 (dam olish kuni)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilgan gapini tanlang.",
          "questions": [
            q("t4-v6-28", "演説", [
                "私どもの協会は何よりも自由と平等を演説しております。",
                "選挙中、声を限りに候補者の名前を演説した。",
                "新しい首相は、政策について国会で演説した。",
                "あの男は義務も果たさずに権利ばかり演説する。"], 3,
              "演説 (えんぜつ) = nutq so'zlash (siyosiy, ommaviy nutq).",
              optsTr=[
                "Assotsiatsiyamiz ozodlikni 'nutq so'zlaydi' (noto'g'ri — 主張).",
                "Saylovda nomzod ismini 'nutq so'zladi' (noto'g'ri — 連呼).",
                "Yangi bosh vazir siyosiy rejalari haqida parlamentda nutq so'zladi. (to'g'ri)",
                "U majburiyatni bajarmay, faqat huquqlarni 'nutq so'zlaydi' (noto'g'ri)."]),
            q("t4-v6-29", "生まれ", [
                "あなたの生まれは何月何日ですか。",
                "彼のあのがんこさは生まれのものでどうにもならない。",
                "乳歯から永久歯の生まれは10歳ぐらいに起きる。",
                "彼女は生まれがよいのか、どこか品がある。"], 4,
              "生まれ (うまれ) = nasl-nasab, kelib chiqish muhiti.",
              optsTr=[
                "Tug'ilgan kuningiz qachon (noto'g'ri — 生年月日).",
                "Uning o'jarligi tug'ma (noto'g'ri — 生まれつき).",
                "Sut tishidan doimiy tishga almashish (noto'g'ri — 生え変わり).",
                "Uning nasl-nasabi (kelib chiqishi) yaxshi bo'lgani sabablimi, o'zida bir olijanoblik bor. (to'g'ri)"]),
            q("t4-v6-30", "危うい", [
                "最近子どもの様子が少し危うい。",
                "近所を危うい男がうろうろしている。",
                "この道路は夜とても暗いので、1人で歩くのは危うい。",
                "おぼれかけたが、危ういところで助けられた。"], 4,
              "危うい (あやうい) = xatarli, qilt ustida qolgan (危ういところで = arang/zo'rg'a).",
              optsTr=[
                "Bolaning ahvoli 'qilt ustida' (noto'g'ri — 怪しい).",
                "Mahallada 'shubhali' odam aylanib yuribdi (noto'g'ri — 怪しい).",
                "Kechasi qorong'i bo'lib yurish 'xavfli' (noto'g'ri — 危険/危ない).",
                "Cho'kib ketayozgandim, qilt ustida (arang, bir bahya qolganda) qutqarib qolishdi. (to'g'ri)"]),
            q("t4-v6-31", "実物", [
                "彼のゴルフの腕前はまさに実物だ。",
                "この会社は名前だけで実物がない。",
                "写真では見ていたが、実物の美しさは想像以上だった。",
                "もし実物のダイヤなら、すごい値段のはずだ。"], 3,
              "実物 (じつぶつ) = asil nusxa, ko'z bilan ko'riladigan haqiqiy buyum.",
              optsTr=[
                "Golf mahorati haqiqiy (noto'g'ri — 本物).",
                "Kompaniyaning mohiyati yo'q (noto'g'ri — 実質).",
                "Suratda ko'rgan edim, lekin haqiqiy buyumning o'zidagi go'zallik tasavvurimdan a'lo ekan. (to'g'ri)",
                "Asl brilliant (noto'g'ri — 本物)."]),
            q("t4-v6-32", "予測", [
                "雨でもバザーは予測通りに行います。",
                "気象庁が予測した通り、今年の夏は異常に暑い。",
                "彼の競馬の予測は当たったためしがない。",
                "予測せぬ事態が起こり、会場は大混乱になった。"], 2,
              "予測 (よそく) = ilmiy yoki ma'lumotlarga asoslangan bashorat/taxmin.",
              optsTr=[
                "Reja bo'yicha (noto'g'ri — 予定).",
                "Gidrometeorologiya markazi oldindan bashorat qilganidek, bu yil yoz g'ayritabiiy issiq bo'lmoqda. (to'g'ri)",
                "Ot poygasi taxmini (noto'g'ri — 予想).",
                "Kutilmagan vaziyat (noto'g'ri — 予期せぬ/予期しない)."])
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
            q("t4-g1-33", "景気が悪くなる（　）、新聞の広告が減ってくる。",
              ["に反して", "に関して", "に応じて", "にしたがって"], 4,
              "Iqtisodiyot yomonlashib borgan sari, gazetadagi reklamalar ham kamayib boradi.",
              expl="〜にしたがって = ...gan sari (bir narsa o'zgarishi bilan boshqasi ham o'zgarishi)"),
            q("t4-g1-34", "このレストランは安い（　）おいしいので、いつも客でいっぱいだ。",
              ["わりに", "かわりに", "ついでに", "ゆえに"], 1,
              "Bu restoran arzonligiga qaramasdan (arzonligiga yarasha) juda mazali bo'lgani sababli, doim mijozlarga to'la.",
              expl="〜わりに (わりには) = ...ga qaramasdan, kutilganidan boshqacha"),
            q("t4-g1-35", "え、佐藤さんはまた休みなの。こないだ休んだ（　）なのに。",
              ["かぎり", "ばかり", "だけ", "きり"], 2,
              "Iye, Sato yana kelmadimi? Yaqindagina dam olgan edi-ku!",
              expl="〜たばかり = yaqindagina ... bo'lgan"),
            q("t4-g1-36", "給料が上がらないのに子どもが大学に入り、生活が苦しくなる（　）。",
              ["理由だ", "状態だ", "一方だ", "限界だ"], 3,
              "Oylik oshmayotgan bir paytda bola universitetga kirdi, turmush esa tobora qiyinlashib bormoqda.",
              expl="〜一方だ (いっぽうだ) = tobora faqat bir tomonga (yomon tomonga) qarab o'zgarmoqda"),
            q("t4-g1-37", "今日はかぜ（　）だから、おふろには入らないで寝ます。",
              ["がち", "向き", "気味", "げ"], 3,
              "Bugun biroz shamollash alomati (shamollashdek holat) sezilgani uchun, vanna qilmay uxlayman.",
              expl="〜気味 (ぎみ) = biroz alomati bor, moyillik"),
            q("t4-g1-38", "たとえ法律を知らなかった（　）、決まりをやぶったら罪になる。",
              ["とかいえば", "ともいえ", "とさえいえ", "とはいえ"], 4,
              "Garchi qonunni bilmagan bo'lsangiz ham, qoidani buzsangiz jinoyat hisoblanadi.",
              expl="〜とはいえ = garchi ... bo'lsa ham"),
            q("t4-g1-39", "これから皆で力を合わせて、がんばって（　）ないか！",
              ["いこうでは", "いかずには", "いっては", "いくわけで"], 1,
              "Kelinglar, bundan buyon barchamiz kuchimizni birlashtirib birgalikda harakat qilaylik!",
              expl="〜（よう）ではないか = kelinglar, shunday qilaylik! (chaqiriq/targ'ib)"),
            q("t4-g1-40", "A「もしもし、杉山さんはいらっしゃいますか。」\nB「あの、お名前を（　）。」",
              ["うかがってよろしいですか", "うかがっていただけますか", "申してよろしいですか", "申していただけますか"], 1,
              "A: «Allo, Sugiyama janoblari bormilar?»\nB: «Uzr, ismingizni so'rasam (bilsam) maylimi?»",
              expl="お名前をうかがってよろしいですか = ismingizni so'rasam maylimi (xushmuomala so'rov)"),
            q("t4-g1-41", "がんばっても必ず成功する（　）が、やるだけはやろう。",
              ["というわけではない", "といったところだ", "というわけだ", "といったようだ"], 1,
              "Harakat qilgan bilan albatta muvaffaqiyatga erishiladi degani emas, ammo qo'ldan kelgancha urinib ko'ramiz.",
              expl="〜というわけではない = mutlaqo ... degani emas"),
            q("t4-g1-42", "木村君が時間通りに家を（　）、もう着いているはずなのに、まだ来ていない。",
              ["出発するとすると", "出発したとすると", "出発するとしても", "出発したとしても"], 2,
              "Agar Kimura vaqtida uydan chiqqan deb hisoblasak, allaqachon yetib kelishi kerak edi, ammo hali ham yo'q.",
              expl="〜たとすると = agar ... deb faraz qilsak"),
            q("t4-g1-43", "「私がやります」と言ったからには、私が（　）。",
              ["やらざるを得ない", "やるわけにはいかない", "やるべきではない", "やらないかもしれない"], 1,
              "«O'zim qilaman» deb aytgan ekanman, o'zim qilmasdan boshqa ilojim yo'q.",
              expl="〜からには〜ざるを得ない = aytgan ekansan, qilmaslikning iloji yo'q"),
            q("t4-g1-44", "若い社員に責任のある仕事を（　）、本人もやる気になるのではないか。",
              ["してやったほうが", "させてやったほうが", "してあったほうが", "させてあったほうが"], 2,
              "Yosh xodimlarga mas'uliyatli ishni topshirib ko'rsak, o'zida ham ishtiyoq paydo bo'lmasmikin?",
              expl="〜させてやったほうが = qildirib ko'rgan ma'qulroq")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng to'g'ri bo'lakni tanlang.",
          "questions": [
            q("t4-g2-45", None, ["子どもを", "必死に守るのに", "でさえ", "人間が"], 2,
              "To'g'ri tartib: 動物でさえ子どもを必死に守るのに、人間が子どもを捨てるなんて許せない。",
              prefix="動物", suffix="子どもを捨てるなんて許せない。", starPos=2, order=[3, 1, 2, 4],
              expl="To'g'ri tartib: 動物[でさえ][子どもを][★必死に守るのに][人間が] (3 → 1 → 2 → 4)"),
            q("t4-v2-46", None, ["かねる", "ことが", "理解", "し"], 1,
              "To'g'ri tartib: 今の若者の考えは理解しかねることが多すぎる。",
              prefix="今の若者の考えは", suffix="多すぎる。", starPos=3, order=[3, 4, 1, 2],
              expl="To'g'ri tartib: [理解][し][★かねる][ことが] (3 → 4 → 1 → 2)"),
            q("t4-g2-47", None, ["行く", "まったく", "行く", "町の様子"], 1,
              "To'g'ri tartib: 私が東京に行くたびに、まったく町の様子が変わっている気がする。",
              prefix="私が東京に", suffix="が変わっている気がする。", starPos=2, order=[3, 1, 2, 4],
              expl="To'g'ri tartib: 東京に[行く][たびに][★まったく][町の様子] (3 → 1 → 2 → 4)"),
            q("t4-g2-48", None, ["結果を", "お知らせ", "反した", "ご期待に"], 3,
              "To'g'ri tartib: 残念ながら、みなさんのご期待に反した結果をお知らせしなければなりません。",
              prefix="残念ながら、みなさんの", suffix="しなければなりません。", starPos=2, order=[4, 3, 1, 2],
              expl="To'g'ri tartib: みなさんの[ご期待に][★反した][結果を][お知らせ] (4 → 3 → 1 → 2)"),
            q("t4-g2-49", None, ["あり", "中止", "によっては", "ということ"], 4,
              "To'g'ri tartib: B「いや、天気によっては中止ということもあり得るよ。」",
              prefix="B「いや、天気", suffix="得るよ。」", starPos=3, order=[3, 2, 4, 1],
              expl="To'g'ri tartib: 天気[によっては][中止][★ということ][も][あり] (3 → 2 → 4 → 1)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh joylariga eng to'g'ri variantni tanlang.",
          "passage_title": "地震速報の仕組み",
          "passage": (
            "地震のない国から日本に来た人が驚くことの1つに、テレビやラジオの緊急地震速報があります。番組の途中で突然チャイムが鳴り、「〇〇地方で地震です」とアナウンスが流れます。ふつう放送から大きな揺れが来るまで数秒くらいですが、その間に火を消したりテーブルにもぐったりできます。\n"
            "その後、すぐに震源はどこか、津波の心配があるかどうかも放送されます。\n"
            "これは1995年の阪神・淡路大震災を契機に地震計が日本各地に置かれ始め、そのデータをもとに地震の情報を少しでも早く {{50}} 、研究が始まったものです。2007年から一般人向けに放送されるようになりました。世界でも初めてのシステムです。\n"
            "でも、なぜ揺れを感じるか {{51}} 地震や津波が来るとわかるのでしょうか。\n"
            "地震が起きると、P波と呼ばれる小さな揺れと、S波と呼ばれる大きな揺れが同時に発生します。P波は毎秒7km、S波は毎秒4kmで進みます。\n"
            "先に {{52-a}} が来たときに、どのくらい後に {{52-b}} が来るか予測して、緊急地震速報が発表されるのです。いくつかの地点のP波とS波の時間差を見ると、震源がどこかもわかります。\n"
            "海底にもたくさん地震計が置かれ、地震波を観測するとデータを衛星に送ります。地震波は海の波より100倍速く着くので、津波が来るかどうか {{53}} 。\n"
            "2004年のスマトラ島沖地震であったら、多くの人の命が助かったことでしょう。今や津波は「tsunami」と、世界でそのまま通じる言葉になりました。津波情報も国境を越えて発信する必要があります。\n"
            "緊急地震速報もまだまだ不完全ですが、地震の多い日本 {{54}} の発明と言えるでしょう。"
          ),
          "passage_tr": (
            "Zilzila bo'lmaydigan mamlakatlardan Yaponiyaga kelgan kishilar hayron bo'ladigan jihatlardan biri — bu tele va radio orqali beriladigan favqulodda zilzila tezkor xabarlaridir. Ko'rsatuv davomida to'satdan signal chalinib, «falon mintaqada zilzila» degan e'lon yangraydi. Odatda efirdan katta silkinish yetib kelgunicha bir necha soniya bo'ladi, lekin shu vaqt ichida olovni o'chirish yoki stol tagiga yashirinishga ulgurish mumkin.\n"
            "Shundan so'ng darhol epitsentr qayerdaligi va sunami xavfi bor-yo'qligi ham ma'lum qilinadi.\n"
            "Bu 1995-yildagi Buyuk Xanshin zilzilasi sabab bo'lib, Yaponiya bo'ylab seysmometrlar o'rnatila boshlangach, ushbu ma'lumotlar orqali zilzila xabarini ozgina bo'lsa ham tezroq yetkazish uchun ilmiy izlanishlar boshlanishi bilan yaratilgan. 2007-yildan xalqqa e'lon qilina boshlandi. Bu dunyodagi ilk tizimdir.\n"
            "Lekin nega silkinishni his etishdan oldinoq zilzila va sunami kelishini bilish mumkin?\n"
            "Zilzila yuz berganda P-to'lqin deb ataluvchi kichik to'lqin va S-to'lqin deb ataluvchi kuchli to'lqin bir paytda yuzaga keladi. P-to'lqin soniyasiga 7 km, S-to'lqin esa soniyasiga 4 km tezlikda harakatlanadi.\n"
            "Avval P-to'lqin yetib kelganda, qancha vaqtdan keyin S-to'lqin yetib kelishi hisoblab chiqilib, tezkor xabar e'lon qilinadi.\n"
            "Dengiz tubiga ham ko'plab seysmometrlar joylashtirilgan. Seysmik to'lqin dengiz to'lqinidan 100 baravar tez harakatlangani bois, sunami kelish-kelmasligini oldindan hisoblash mumkin bo'ladi.\n"
            "Favqulodda zilzila xabari hali mukammal bo'lmasa-da, zilzilalarga boy Yaponiyaga xos bo'lgan ajoyib ixtiro deyish mumkin."
          ),
          "questions": [
            q("t4-g3-50", None, ["伝えまいと", "伝えようと", "伝えないと", "伝えるなら"], 2,
              "少しでも早く[伝えようと]、研究が始まった = ozgina bo'lsa ham tezroq yetkazaylik deb izlanishlar boshlangan.",
              blankNo="50", expl="〜ようと = ...qilish niyati/maqsadi bilan"),
            q("t4-g3-51", None, ["感じないかのうちに", "感じないままに", "感じてからでないと", "感じたとたんに"], 1,
              "なぜ揺れを[感じないかのうちに]わかるのでしょうか = nega silkinishni hali his qilar-qilmas bilish mumkin?",
              blankNo="51", expl="〜ないかのうちに = ...qilar-qilmas, birdaniga"),
            q("t4-g3-52", None, [
                "a P波 ／ b P波",
                "a S波 ／ b S波",
                "a S波 ／ b P波",
                "a P波 ／ b S波"], 4,
              "先に[a P波]が来たときに、どのくらい後に[b S波]が来るか予測して (Avval P-to'lqin, keyin S-to'lqin).",
              blankNo="52", expl="Oldin kichik P-to'lqin (a), ortidan katta S-to'lqin (b)"),
            q("t4-g3-53", None, ["計算し得ません", "計算しかねません", "計算し得ます", "計算しかねます"], 3,
              "津波が来るかどうか[計算し得ます] = kelish-kelmasligini oldindan hisoblab chiqish imkoniyati bor.",
              blankNo="53", expl="〜得る (うる/える) = amalga oshira oladi, imkoni bor"),
            q("t4-g3-54", None, ["といったら", "とあって", "だからこそ", "だからといって"], 3,
              "地震の多い日本[だからこそ]の発明と言えるでしょう = zilzilasi ko'p bo'lgan Yaponiyaga aynan xos bo'lgan ixtiro.",
              blankNo="54", expl="〜だからこそ = aynan ... bo'lgani sababliki")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print(f"OK! test04.json yaratildi: {total} ta savol.")
