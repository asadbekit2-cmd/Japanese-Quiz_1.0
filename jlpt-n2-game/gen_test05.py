# -*- coding: utf-8 -*-
"""
test05.json generatori — 第5回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.6
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test05.json")

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
  "id": 5,
  "title_jp": "第5回 模擬テスト",
  "title_uz": "5-test",
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
            q("t5-v1-1", "親の経済事情で、専門学校へ進路を【変更】した。",
              ["へんごう", "へんか", "へんこう", "へんかん"], 3,
              "Ota-onamning moliyaviy ahvoli tufayli, kasb-hunar kollejiga borish yo'nalishini o'zgartirdim.",
              reading="へんこう", expl="変更 → へんこう (o'zgartirish, boshqasiga almashtirish)"),
            q("t5-v1-2", "この種目ではオリンピック初となるメダルへの期待が【膨らんだ】。",
              ["からんだ", "ふくらんだ", "にらんだ", "はらんだ"], 2,
              "Ushbu sport turida Olimpiadada ilk medalni qo'lga kiritishga bo'lgan umid yanada oshdi (kengaydi).",
              reading="ふくらんだ", expl="膨らむ → ふくらむ (kengaymoq, shishmoq, oshmoq)"),
            q("t5-v1-3", "学生に人気があるのは「経済学【概論】」の講座だ。",
              ["きろん", "しょろん", "がいろん", "じろん"], 3,
              "Talabalar orasida mashhurlik qozonayotgani «Iqtisodiyotga kirish / umumiy asoslari» kursidir.",
              reading="がいろん", expl="概論 → がいろん (kirish kursi, umumiy asoslar)"),
            q("t5-v1-4", "私の登山の目的は【頂上】に立つことではなく、大自然をゆっくり楽しむことにある。",
              ["とうじょう", "ちょうじょう", "こうじょう", "ていじょう"], 2,
              "Mening toqqa chiqishdan maqsadim cho'qqiga chiqish emas, balki tabiatdan xotirjam zavqlanishdir.",
              reading="ちょうじょう", expl="頂上 → ちょうじょう (cho'qqi, eng baland nuqta)"),
            q("t5-v1-5", "東京都は医療【水準】の向上を目指す新制度を発表した。",
              ["すいじゅん", "すいじゅん", "すいしゅん", "ずいしゅん"], 2,
              "Tokio hukumati tibbiyot darajasini oshirishga qaratilgan yangi tizimni e'lon qildi.",
              reading="すいじゅん", expl="水準 → すいじゅん (daraja, saviya)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t5-v2-6", "弱い立場の人に精神的、身体的【くつう】を与えることをパワーハラスメントという。",
              ["苦痛", "苦適", "具痛", "悲痛"], 1,
              "Zaif mavqedagi insonga ruhiy va jismoniy azob (og'riq) yetkazish vakolatni suiiste'mol qilish (power harassment) deyiladi.",
              reading="くつう", expl="苦痛 → くつう (azob, og'riq)"),
            q("t5-v2-7", "今朝は手が【こごえて】、物がうまくつかめないほど寒かった。",
              ["冷えて", "寒えて", "凍えて", "涼えて"], 3,
              "Bugun ertalab qo'llar uvishib (muzlab), biror narsani ushlab bo'lmaydigan darajada sovuq edi.",
              reading="こごえて", expl="凍える → こごえる (muzlamoq, uvishmoq)"),
            q("t5-v2-8", "相手チームの弱点を【にぎって】いたので、試合を有利に進めることができた。",
              ["挟って", "握って", "担って", "捕って"], 2,
              "Raqib jamoaning zaif tomonini qo'lga kiritib olganimiz (ushlab olganimiz) sababli, o'yinni o'zimizga qulay olib bordik.",
              reading="にぎって", expl="握る → にぎる (siqimlab ushlamoq, qo'lda tutmoq)"),
            q("t5-v2-9", "取引先と【りがい】が一致して、契約の話がまとまった。",
              ["理外", "理害", "利外", "利害"], 4,
              "Hamkor kompaniya bilan o'zaro manfaatlar mos kelib, shartnoma masalasi hal bo'ldi.",
              reading="りがい", expl="利害 → りがい (foyda va ziyon, manfaat)"),
            q("t5-v2-10", "厳しいトレーニングを積み重ねて、やっと自分の欠点を【こくふく】することができた。",
              ["克服", "告服", "降服", "攻服"], 1,
              "Og'ir mashg'ulotlarni ketma-ket bajarib, nihoyat o'z kamchiligimni yengib o'tishga (bartaraf etishga) muvaffaq bo'ldim.",
              reading="こくふく", expl="克服 → こくふく (yengib o'tish, mag'lub etish)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t5-v3-11", "この作業は（　）仕事ではないので、お年寄りに向いている。",
              ["力", "重", "諸", "全"], 1,
              "Bu yumush jismoniy og'ir ish (kuch talab qiladigan ish) bo'lmagani uchun, keksalar uchun mos keladi.",
              expl="力仕事 (ちからしごと) = og'ir jismoniy mehnat"),
            q("t5-v3-12", "飲み会はなんとか1人3000円の予算（　）におさまった。",
              ["中", "下", "外", "内"], 4,
              "O'tirish qandaydir qilib har bir kishiga 3000 iyen byudjet doirasida (ichida) yakunlandi.",
              expl="予算内 (よさんない) = byudjet doirasida/ichida"),
            q("t5-v3-13", "彼は町の有力（　）だ。",
              ["家", "者", "人", "民"], 2,
              "U shahardagi nufuzli (ta'sir doirasi katta) shaxsdir.",
              expl="有力者 (ゆうりょくしゃ) = nufuzli, obro'li shaxs"),
            q("t5-v3-14", "これは（　）個人としての意見です。",
              ["単", "各", "唯", "一"], 4,
              "Bu faqat bir shaxs (oddiy inson) sifatidagi shaxsiy fikrimdir.",
              expl="一見 / 一個人 (いっこじん) = alohida bir shaxs, oddiy inson"),
            q("t5-v3-15", "病気をして以来、人生（　）が変わった。",
              ["感", "考", "観", "想"], 3,
              "Betob bo'lib chiqqanimdan beri hayotga bo'lgan qarashim (dunyoqarashim) butunlay o'zgardi.",
              expl="人生観 (じんせいかん) = hayotga bo'lgan qarash, dunyoqarash")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ( ) ga ma'no jihatidan eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t5-v4-16", "東洋医学は、全身を支える足を特に（　）視する。",
              ["大事", "優先", "貴重", "重要"], 4,
              "Sharq tabobati butun vujudni ko'tarib turuvchi oyoqlarni alohida muhim (ahamiyatli) deb biladi.",
              expl="重要視する (じゅうようしする) = juda muhim deb hisoblamoq"),
            q("t5-v4-17", "エアコンが吐き出す熱が、外の暑さをさらに（　）させている。",
              ["増大", "急増", "増減", "激増"], 1,
              "Konditsioner chiqarib tashlayotgan issiqlik tashqaridagi havoni yanada qizdirib (kuchaytirib) yubormoqda.",
              expl="増大 (ぞうだい) = kuchayish, ortish, ko'payish"),
            q("t5-v4-18", "もう子どもではないんだから、（　）言われなくても自分で決めなさいよ。",
              ["あちこち", "まあまあ", "いちいち", "それぞれ"], 3,
              "Endi yosh bola emassan, har bitta mayda-chuyda narsani aytilmasa ham o'zing hal qilgin.",
              expl="いちいち = birma-bir, har bir mayda narsagacha"),
            q("t5-v4-19", "この商品が売れない原因の1つは商品の（　）のデザインが平凡すぎるからだと思う。",
              ["パート", "パーソナル", "パターン", "パッケージ"], 4,
              "Ushbu tovar sotilmasligining bir sababi uning qadoqlanish (package) dizayni o'ta oddiyligidir deb o'ylayman.",
              expl="パッケージ (package) = qadoq, qadoqlash"),
            q("t5-v4-20", "仕事の悩みなら（　）見のよい職場の上司に相談するのがいちばんだと思う。",
              ["面倒", "世話", "加減", "手数"], 1,
              "Ishdagi muammo bo'lsa, xodimlarga yaxshi qaraydigan (g'amxo'r) rahbarga maslahat solgan ma'qul.",
              expl="面倒見のよい (めんどうみのよい) = g'amxo'r, yaxshi qaraydigan"),
            q("t5-v4-21", "博士号は取るし、結婚も決まったし、彼にとって（　）ことが続いている。",
              ["かしこい", "ふさわしい", "おめでたい", "したい"], 3,
              "Doktorlik unvonini oldi, to'yi ham belgilandi — uning uchun faqat quvonchli (muborak) ishlar davom etmoqda.",
              expl="おめでたい = quvonchli, tabriklashga arziydigan"),
            q("t5-v4-22", "疲れ気味かなと思ったら、ビタミンCを多く（　）食品をとるといい。",
              ["包む", "含む", "帯びる", "握る"], 2,
              "Biroz toliqqandek bo'lsangiz, tarkibida C vitamini ko'p bo'lgan (o'z ichiga olgan) ozuqalarni iste'mol qilgan ma'qul.",
              expl="含む (ふくむ) = o'z ichiga olmoq, tarkibida bo'lmoq")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin sinonimni tanlang.",
          "questions": [
            q("t5-v5-23", "ハイキングは雨で【流れた】。",
              ["延期になった", "中止になった", "見直された", "変更になった"], 2,
              "Sayr (hiking) yomg'ir sababli bekor qilindi (amalga oshmadi).",
              reading="ながれた", expl="流れる → 中止になった (bekor bo'lmoq, qolib ketmoq)"),
            q("t5-v5-24", "空が【にわかに】暗くなり、大粒の雨が降り出した。",
              ["すっかり", "ぼんやり", "くっきり", "いきなり"], 4,
              "Osmon to'satdan qorayib, yirik tomchili yomg'ir yog'a boshladi.",
              reading="にわかに", expl="にわかに = いきなり (to'satdan, birdaniga)"),
            q("t5-v5-25", "彼女はいつも【覚めた】目で世間を見ている。",
              ["冷静な", "鋭い", "確かな", "温かい"], 1,
              "U doim atrof-olamga vazmin (hissiyotga berilmasdan, sovuqqon) nigoh bilan qaraydi.",
              reading="さめた", expl="覚めた目 = 冷静な (vazmin, bosiq, mulohazali)"),
            q("t5-v5-26", "友人に【強引に】パーティーに連れて行かれた。",
              ["むりやり", "こっそり", "しきりに", "わざわざ"], 1,
              "Do'stim meni majburlab (zo'rlab) bazmga sudrab olib bordi.",
              reading="ごういんに", expl="強引に = むりやり (majburlab, zo'ravonlik bilan)"),
            q("t5-v5-27", "先輩は私の仕事を【サポート】してくれる。",
              ["理解して", "評価して", "応援して", "仕上げて"], 3,
              "Katta hamkasbim mening ishimni qo'llab-quvvatlab (yordam berib) turadi.",
              expl="サポートする = 応援して (yordam bermoq, suyamoq)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilgan gapini tanlang.",
          "questions": [
            q("t5-v6-28", "圧縮", [
                "通勤時間を圧縮するため引っ越しをする。",
                "景気が悪いので、社員数を圧縮しなければならない。",
                "袋にふとんを入れて空気を抜くと、薄く圧縮できる。",
                "スカート丈を3センチ圧縮したら、イメージが変わった。"], 3,
              "圧縮 (あっしゅく) = siqish, hajmini kichraytirish (havosini chiqarib qisish).",
              optsTr=[
                "Yo'l vaqtini qisqartirish (noto'g'ri — 短縮).",
                "Xodimlar sonini qisqartirish (noto'g'ri — 削減).",
                "Xaltaga ko'rpani solib havosini so'rib olinsa, yupqa qilib siqib (presslab) qo'yish mumkin. (to'g'ri)",
                "Yubkani kaltalatish (noto'g'ri — 詰める)."]),
            q("t5-v6-29", "ぼろ", [
                "このお菓子の名前はぼろがいい。",
                "彼女、上品ぶっているけれど、そのうちぼろを出すよ。",
                "去年買った服のデザインがぼろになって着られない。",
                "彼は他人のぼろばかり探すいやな男だ。"], 2,
              "ぼろ = yashiringan kamchilik, nuqson (ぼろを出す = sirini/kamchiligini fosh qilib qo'ymoq).",
              optsTr=[
                "Shirinlikning nomi yaxshi (noto'g'ri — ごろ).",
                "U o'zini olijanob ko'rsatmoqda, ammo tez orada asl qiyofasini (kamchiligini) fosh qilib qo'yadi. (to'g'ri)",
                "Kiyim dizayni eskirib (noto'g'ri — 流行遅れ).",
                "Odamlarning kamchiligini qidiradi (noto'g'ri — あら)."]),
            q("t5-v6-30", "上等", [
                "これはたいへん上等なお品でございます。",
                "あの子は病気の母親の世話をして上等だ。",
                "上等な考えを持っている若者もたくさんいる。",
                "彼女は1人で5人の子どもを育てた上等な女性だ。"], 1,
              "上等 (じょうとう) = yuqori sifatli, a'lo darajali (buyum/mahsulot haqida).",
              optsTr=[
                "Bu juda yuqori sifatli (a'lo darajadagi) buyumdir. (to'g'ri)",
                "Onasiga qarab 'a'lo' (noto'g'ri — えらい/感心).",
                "Ajoyib fikrga ega (noto'g'ri — 立派な).",
                "Ulug' ayol (noto'g'ri — 立派な)."]),
            q("t5-v6-31", "規律", [
                "今日の練習の規律はいつもより忙しい。",
                "彼はまるで軍隊のように規律正しい生活をしている。",
                "社長の大胆な規律で会社は危機を脱した。",
                "受験資格を経験者だけに規律する。"], 2,
              "規律 (きりつ) = intizom, tartib-qoida (規律正しい = intizomli).",
              optsTr=[
                "Mashg'ulot jadvali (noto'g'ri — スケジュール).",
                "U xuddi armiyadagidek qat'iy intizomli hayot kechiradi. (to'g'ri)",
                "Prezidentning qat'iy qarori (noto'g'ri — 決断).",
                "Tajribalilarga cheklash (noto'g'ri — 限定)."]),
            q("t5-v6-32", "空想", [
                "こんな結果になるなんて空想もつきませんでした。",
                "子どものころからスターになる空想を見続けている。",
                "将来の生活の空想を立ててください。",
                "彼女は「もし大金持ちと結婚したら」とか、空想ばかりしている。"], 4,
              "空想 (くうそう) = xayol surish, fantaziya (asossiz xayollar).",
              optsTr=[
                "Bunday bo'lishini o'ylamovdim (noto'g'ri — 予想).",
                "Yulduz bo'lish orzusini ko'rmoqda (noto'g'ri — 夢).",
                "Reja tuzing (noto'g'ri — 計画).",
                "U doim «agar boy odamga tegsam» kabi asossiz xayollarni suraveradi. (to'g'ri)"])
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
            q("t5-g1-33", "私の部屋は広い（　）、新しくて気持ちがよい。",
              ["ながらも", "かわりに", "とはいえ", "上に"], 4,
              "Mening xonam keng bo'lishi ustiga-ustak, yangi va juda shinamdir.",
              expl="〜上に (うえに) = ...ning ustiga-ustak, bundan tashqari"),
            q("t5-g1-34", "明日から週末（　）、全国的によい天気が続くでしょう。",
              ["に続いて", "にかけて", "に渡って", "に及んで"], 2,
              "Ertadan dam olish kunlarigacha butun mamlakat bo'ylab yaxshi ob-havo davom etsa kerak.",
              expl="〜から〜にかけて = ...dan ...gacha bo'lgan davrda"),
            q("t5-g1-35", "悪いとわかっていても、時には罪をおかす。それが人間と（　）だ。",
              ["いうこと", "いう人", "いうもの", "いうわけ"], 3,
              "Yomonligini bilaturib ham ba'zida gunoh qiladi. Inson tabiati degani o'zi shunaqa-da.",
              expl="〜というものだ = ...tabiati shundaydir (inson tabiati)"),
            q("t5-g1-36", "たった1番違いで宝くじに外れるなんて、くやしくて（　）。",
              ["ならない", "なれない", "なるまい", "なりきれない"], 1,
              "Atigi bir raqam farqi bilan lotereyada yutqazib qo'yish — shunchalik alam qiladiki, chidab bo'lmaydi.",
              expl="〜てならない = juda ham, his-tuyg'uni jilovlab bo'lmaydi"),
            q("t5-g1-37", "A「顔色が悪いですね。」\nB「（　）忙しくて、休むひまがないんです。」",
              ["なんとか", "なんでも", "なににとぞ", "なにしろ"], 4,
              "A: «Rangingiz o'chiq-ku.»\nB: «Nima bo'lganda ham juda band bo'lib, dam olishga fursat yo'q-da.»",
              expl="なにしろ = nima bo'lganda ham, qanday bo'lmasin"),
            q("t5-g1-38", "子どものときは（　）でしたが、すっかり丈夫になりました。",
              ["病気みたい", "病気がち", "病気っぽい", "病気ぎみ"], 2,
              "Bolaligimda tez-tez kasal bo'lib turar edim, ammo butunlay baquvvat bo'lib ketdim.",
              expl="〜がち = tez-tez ... bo'ladigan (moyil bo'lgan)"),
            q("t5-g1-39", "最初は嫌いだった日本食も、少しずつ（　）好きになってきた。",
              ["食べるうちに", "食べたうちに", "食べもしないで", "食べるそばから"], 1,
              "Boshida yoqtirmagan yapon taomlarini ham asta-sekin yeyaverish asnosida yoqtirib qoldim.",
              expl="〜うちに = ...qilib yuraverish davomida (o'zgarish sodir bo'lishi)"),
            q("t5-g1-40", "中国語は得意です。通訳が必要ならいつでも（　）。",
              ["おっしゃってください", "申されてください", "言われていただけますか", "申していただけますか"], 1,
              "Xitoy tilini yaxshi bilaman. Tarjimon kerak bo'lsa xohlagan paytda aytavering.",
              expl="おっしゃってください = ayting, buyuring (xushmuomala so'rov: 言う ning sonkeigo shakli)"),
            q("t5-g1-41", "彼はよく「寝たきりになってまで（　）」と言うが、病気になると大騒ぎする。",
              ["長生きをしたいものだ", "長生きはするものだ", "長生きをしたくないものだ", "長生きはしないものだ"], 3,
              "U doim «to'shakka mixlanib qolguncha uzoq yashashni aslo xohlamasdim» deydi-yu, lekin ozgina betob bo'lsa shov-shuv ko'taradi.",
              expl="〜たくないものだ = aslo ... bo'lishni xohlamasdim"),
            q("t5-g1-42", "子どものときからずっとピアノを習ってはきたものの、（　）。",
              ["とてもうまくなった", "あまりうまくならなかった", "きっ とうまくなるだろう", "うまくなるべきだ"], 2,
              "Bolaligimdan beri pianino o'rganib kelgan bo'lsam-da, unchalik yaxshi o'rganib keta olmadim.",
              expl="〜ものの = ...gan bo'lsa-da (kutilgan natija bo'lmadi)"),
            q("t5-g1-43", "最高の材料で最高のシェフが作ったのだから、（　）。",
              ["まずいわけではない", "まずくないわけでもない", "まずいわけがない", "まずくないわけにもいかない"], 3,
              "Eng sara masalliqlardan eng yetuk oshpaz tayyorlagan ekan, bemaza bo'lishi aslo mumkin emas!",
              expl="〜わけがない = aslo ... bo'lishi mumkin emas"),
            q("t5-g1-44", "学園祭について、ただ意見を言うだけで何もしなければ、参加（　）。",
              ["することにはならない", "することにはならない", "したことにはなる", "したことになる"], 1,
              "Talabalar festivali haqida shunchaki fikr aytib, o'zing hech narsa qilmasang, qatnashgan hisoblanmaysan.",
              expl="〜ことにはならない = ...qilgan deb hisoblab bo'lmaydi")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng to'g'ri bo'lakni tanlang.",
          "questions": [
            q("t5-g2-45", None, ["発音", "だけ", "アメリカ育ち", "あって"], 4,
              "To'g'ri tartib: 彼女の英語はアメリカ育ちだけあって発音はきれいだが、文法は正しくない。",
              prefix="彼女の英語は", suffix="はきれいだが、文法は正しくない。", starPos=3, order=[3, 2, 4, 1],
              expl="To'g'ri tartib: [アメリカ育ち][だけ][★あって][発音] (3 → 2 → 4 → 1)"),
            q("t5-g2-46", None, ["とき", "あやまらざる", "お客様に", "を得ない"], 2,
              "To'g'ri tartib: 私のミスではないのにお客様にあやまらざるを得ないときも、たまにはあります。",
              prefix="私のミスではないのに", suffix="も、たまにはあります。", starPos=2, order=[3, 2, 4, 1],
              expl="To'g'ri tartib: [お客様に][★あやまらざる][を得ない][とき] (3 → 2 → 4 → 1)"),
            q("t5-g2-47", None, ["しても", "建てる", "と", "ずっと"], 3,
              "To'g'ri tartib: もし私が家を建てるとしたら、ずっと町の中心から遠いところだ。",
              prefix="もし私が家を", suffix="町の中心から遠いところだ。", starPos=2, order=[2, 3, 1, 4],
              expl="To'g'ri tartib: [建てる][★と][しても][ずっと] (2 → 3 → 1 → 4)"),
            q("t5-g2-48", None, ["限り", "雨の日", "来ない", "台風でも"], 1,
              "To'g'ri tartib: 優勝したマラソン選手は台風でも来ない限り、雨の日も練習を休むことはないそうだ。",
              prefix="優勝したマラソン選手は", suffix="も練習を休むことはないそうだ。", starPos=3, order=[4, 3, 1, 2],
              expl="To'g'ri tartib: [台風でも][来ない][★限り][雨の日] (4 → 3 → 1 → 2)"),
            q("t5-g2-49", None, ["収穫量は", "次第", "秋の", "夏の天気"], 4,
              "To'g'ri tartib: 米や果物の秋の収穫量は夏の天気次第です。",
              prefix="米や果物の", suffix="です。", starPos=3, order=[3, 1, 4, 2],
              expl="To'g'ri tartib: [秋の][収穫量は][★夏の天気][次第] (3 → 1 → 4 → 2)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh joylariga eng to'g'ri variantni tanlang.",
          "passage_title": "緑のカーテン",
          "passage": (
            "最近の日本の夏の暑さには異常な {{50}} 。\n"
            "以前は体に悪いと言われたエアコンも、今では使わないと命が {{51}} 。しかしエアコンをつけると熱い空気が外に吹き出て外の空気が温まり、日が落ちても地面の温度が下がらず、夜も暑いままです。エアコンを使うことが、夏をますます {{52}} とも言えます。\n"
            "最近街を歩いていて、窓の外やベランダ一面にひもがつるされたり棒が立てられていて、下に植えた植物の葉が茂っているのを見かけませんか。あれを「緑のカーテン」と言います。\n"
            "人間が暑いと汗をかくように、植物も暑くなると根から水を吸い、葉の表面が汗をかいたようにぬれます。 {{53-a}} 葉の間を空気が通ると、 {{53-b}} 葉の間を通るよりたくさんの熱を奪います。そのために空気の温度が下がります。\n"
            "エアコンのない小学校で「緑のカーテン」を作ったところ、今まで暑くて勉強できなかった窓際の生徒たちも、落ち着いて勉強できるようになりました。\n"
            "電気代もかからないし、外の地面をあたためることもありません。緑色は勉強で疲れた目を休めるし、実のなる植物なら実を給食に使うこともあるそうです。電気代の節約 {{54}} 、見た目にも美しく食べることもできると、よいことばかりです。\n"
            "市役所が住民に「ぜひ緑のカーテンを作ってください」と呼びかけているところもあります。地球温暖化を食い止めるためにも、広がってほしいものです。"
          ),
          "passage_tr": (
            "So'nggi paytlarda Yaponiyada yozning issiqligi g'ayritabiiy darajada deb aytish mumkin.\n"
            "Ilgari salomatlikka yomon deb qaralgan konditsioner ham hozir ishlatilmasa hayot xavf ostida qoladigan darajada. Ammo konditsionerni yoqqanda issiq havo tashqariga haydalib, ko'chadagi havo isiydi, quyosh botsa ham yer soviymay, kechalari ham issiqligicha qoladi. Konditsioner ishlatish yozni yanada issiqroq qilmoqda deyish ham mumkin.\n"
            "Yaqinda ko'chada yurganda derazalar tashqarisida yoki balkonda iplar tortilib, o'simlik barglari qoplab turganiga ko'zingiz tushmadimi? Buni «Yashil parda» (Midori no kaaten) deb atashadi.\n"
            "Inson issiqda terlaganidek, o'simlik ham issiq bo'lganda ildizidan suv tortib, barglar sathi xuddi terlagandek namlanadi. Namlangan barglar orasidan havo o'tsa, quruq barglar orasidan o'tgandan ko'ra ancha ko'p issiqlikni o'ziga yutadi. Shu sababli havoning harorati pasayadi.\n"
            "Konditsioneri bo'lmagan maktabda «yashil parda» o'rnatilgach, issiqdan o'qiy olmagan deraza yonidagi o'quvchilar ham xotirjam o'qiy boshladilar.\n"
            "Elektr energiyasini tejash-ku mayli, ko'rinishi ham chiroyli va mevasini yeyish ham mumkin — faqatgina yaxshilik keltiradi."
          ),
          "questions": [
            q("t5-g3-50", None, ["ことがあります", "ものがあります", "わけです", "ところです"], 2,
              "夏の暑さには異常な[ものがあります] = yozning issiqligida g'ayritabiiylik bor.",
              blankNo="50", expl="〜ものがある = ...deb hisoblaydigan jihati bor"),
            q("t5-g3-51", None, ["危ないばかりです", "危ないはずです", "危ないほどです", "危ないところです"], 3,
              "使わないと命が[危ないほどです] = ishlatilmasa hayot xavf ostida qoladigan darajada.",
              blankNo="51", expl="〜ほどです = ...darajada"),
            q("t5-g3-52", None, ["過ごしやすくする", "暑くしている", "涼しくする", "快適にする"], 2,
              "夏をますます[暑くしている]とも言えます = yozni yanada issiqroq qilmoqda deyish ham mumkin.",
              blankNo="52", expl="Issiqlik tashqariga chiqishi sababli: 暑くしている"),
            q("t5-g3-53", None, [
                "a ぬれた ／ b かわいた",
                "a かわいた ／ b ぬれた",
                "a ぬれた ／ b ぬれた",
                "a かわいた ／ b かわいた"], 1,
              "a ぬれた (nam) barglar oralig'idan o'tsa, b かわいた (quruq) barglardan o'tgandan ko'proq issiqlikni yutadi.",
              blankNo="53", expl="Tartib: a ぬれた / b かわいた"),
            q("t5-g3-54", None, ["はともかく", "どころか", "ばかりで", "のみならず"], 4,
              "電気代の節約[のみならず]、見た目にも美しく = elektr tejashdan tashqari, ko'rinishi ham go'zal.",
              blankNo="54", expl="〜のみならず = faqatgina ... bo'lib qolmasdan, balki")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print(f"OK! test05.json yaratildi: {total} ta savol.")
