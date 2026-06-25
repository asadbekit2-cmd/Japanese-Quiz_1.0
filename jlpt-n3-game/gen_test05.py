# -*- coding: utf-8 -*-
"""test05.json — 第5回 模擬テスト (PDF betlari 48-57, javob 198)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test05.json")

def q(qid, stem, options, answer, tr, reading=None, expl=None, optsTr=None,
      prefix=None, suffix=None, starPos=None, order=None, blankNo=None):
    d = {"id": qid}
    if stem is not None: d["stem"] = stem
    d["options"] = options; d["answer"] = answer
    if reading: d["reading"] = reading
    if blankNo is not None: d["blankNo"] = blankNo
    if prefix is not None: d["prefix"] = prefix
    if suffix is not None: d["suffix"] = suffix
    if starPos is not None: d["starPos"] = starPos
    if order is not None: d["order"] = order
    if expl: d["explanation_uz"] = expl
    if optsTr: d["optsTr"] = optsTr
    d["tr"] = tr
    return d

data = {
  "id": 5, "title_jp": "第5回 模擬テスト", "title_uz": "5-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t5-v1-1","田中さんは、仕事の【経験】が豊富だ。",["けけん","けいけん","きけん","きいけん"],2,"Tanaka-sanning ish tajribasi boy.",reading="けいけん",expl="経験 → けいけん (tajriba)"),
         q("t5-v1-2","あの車は、【速度】が速い。",["そくど","そくどう","そぐど","そぐどう"],1,"Anavi mashinaning tezligi yuqori.",reading="そくど",expl="速度 → そくど (tezlik)"),
         q("t5-v1-3","先生にほめられて、【自信】がついた。",["ししん","じしん","しじん","じじん"],2,"O'qituvchi maqtagach, o'zimga bo'lgan ishonchim ortdi.",reading="じしん",expl="自信 → じしん (o'ziga ishonch)"),
         q("t5-v1-4","今から【重要な】お知らせをします。",["じゆような","じゆうような","じゅような","じゅうような"],4,"Hozir muhim e'lonni aytaman.",reading="じゅうような",expl="重要な → じゅうような (muhim)"),
         q("t5-v1-5","パソコンの電源を【切って】ください。",["きって","けって","はって","とって"],1,"Kompyuterning tokini o'chiring.",reading="きって",expl="切る → きる (o'chirmoq, kesmoq)"),
         q("t5-v1-6","この川の【浅い】ところで遊びましょう。",["うすい","せまい","ほそい","あさい"],4,"Bu daryoning sayoz joyida o'ynaylik.",reading="あさい",expl="浅い → あさい (sayoz)"),
         q("t5-v1-7","手のひらを【太陽】に向けてみる。",["たよう","たいよう","だよう","だいよう"],2,"Kaftimni quyoshga qaratib ko'raman.",reading="たいよう",expl="太陽 → たいよう (quyosh)"),
         q("t5-v1-8","家の前に、ごみが【散らかって】いる。",["かたづいて","ちらかって","ころがって","ひろがって"],2,"Uyning oldida axlat sochilib yotibdi.",reading="ちらかって",expl="散らかる → ちらかる (sochilib yotmoq)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t5-v2-9","彼は、【いだいな】政治家だ。",["違大","遠大","異大","偉大"],4,"U buyuk siyosatchi.",expl="いだい → 偉大 (buyuk)"),
         q("t5-v2-10","この機械を【そうさ】するのは、簡単だ。",["操件","動件","操作","動作"],3,"Bu uskunani boshqarish oson.",expl="そうさ → 操作 (boshqaruv, operatsiya)"),
         q("t5-v2-11","子どもにお菓子を【あたえた】。",["与えた","授えた","余えた","貸えた"],1,"Bolaga shirinlik berdim.",expl="あたえる → 与える (bermoq, in'om etmoq)"),
         q("t5-v2-12","道を左に【まがる】。",["反がる","折がる","分がる","曲がる"],4,"Yo'ldan chapga burilaman.",expl="まがる → 曲がる (burilmoq)"),
         q("t5-v2-13","彼は、筋肉が【はったつ】している。",["配達","発達","伝達","到達"],2,"Uning muskullari rivojlangan.",expl="はったつ → 発達 (rivojlanish, taraqqiyot)"),
         q("t5-v2-14","私の趣味は、【とざん】です。",["徒山","踏山","登山","道山"],3,"Mening xobbiyim — toqqa chiqish.",expl="とざん → 登山 (toqqa chiqish)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t5-v3-15","明日歩く（　）を地図で調べておいた。",["ゴール","コース","センター","シーン"],2,"Ertaga yuradigan yo'nalishimizni xaritada tekshirib qo'ydim.",expl="コース = marshrut, yo'nalish"),
         q("t5-v3-16","彼は（　）車をほしがっているけれど、買うお金はないようだ。",["単に","次第に","しきりに","ついに"],3,"U tez-tez mashina xohlayotganini aytadi-yu, lekin sotib olishga puli yo'q ko'rinadi.",expl="しきりに = tez-tez, qayta-qayta"),
         q("t5-v3-17","あの人はまったくお金を使わない（　）な人だ。",["十分","多大","あいまい","けち"],4,"U umuman pul ishlatmaydigan xasis odam.",expl="けち = xasis, ziqna"),
         q("t5-v3-18","やっと大雨が（　）が、あちこちで被害があった。",["やんだ","とめた","すんだ","やめた"],1,"Nihoyat jala tindi, lekin turli joylarda talafotlar bo'ldi.",expl="やむ = (yomg'ir, qor) tinmoq"),
         q("t5-v3-19","毎日、（　）の公園へ散歩に出かけます。",["接近","存在","近所","所在"],3,"Har kuni mahalladagi parkka sayrga chiqaman.",expl="近所 = atrofdagi, mahalladagi"),
         q("t5-v3-20","私の誕生日をみんなで（　）くれて、うれしかった。",["祝って","泣いて","望んで","願って"],1,"Tug'ilgan kunimni hammamiz birga nishonlaganimizdan xursand bo'ldim.",expl="祝う (いわう) = nishonlamoq, tabriklamoq"),
         q("t5-v3-21","そのニュースを知って、大きな（　）を受けた。",["アドバイス","ショック","ファックス","メッセージ"],2,"O'sha yangilikni eshitib, qattiq shokka tushdim.",expl="ショック = shok, zarba"),
         q("t5-v3-22","私がその人に会ったのは、5年前に1度（　）です。",["まま","ぱなし","きり","ごと"],3,"U odam bilan 5 yil oldin bir marta uchrashganman xolos.",expl="〜きり = faqatgina ... marta xolos"),
         q("t5-v3-23","この工場では、食品を（　）している。",["創造","創作","製造","製作"],3,"Bu zavodda oziq-ovqat mahsulotlari ishlab chiqariladi.",expl="製造 (せいぞう) = ishlab chiqarish"),
         q("t5-v3-24","お父さまに、（　）お体をお大事に、と伝えてください。",["いまでも","くれぐれも","実に","常に"],2,"Otangizga o'zlarini juda asrashlarini aytib qo'ying.",expl="くれぐれも = chin dildan, qayta-qayta (iltimos, ehtiyot bo'ling ma'nosida)"),
         q("t5-v3-25","ひどいことを言われて、彼女が怒るのも（　）はない。",["無実","無視","無限","無理"],4,"Bunday yomon gaplarni eshitib, uning g'azablanishi o'rinli (g'azablanmasligining iloji yo'q).",expl="無理はない = o'rinli, asabbuzarlikka haqiqiy sabab bor"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t5-v4-26","あの子どもは、水泳が【うまい】。",["好きだ","きらいだ","上手だ","下手だ"],3,"Anavi bola suzishga usta.",expl="うまい = 上手だ (usta, yaxshi uddalaydi)"),
         q("t5-v4-27","両親は、今、【留守にして】います。",["退職して","失業して","離婚して","外出して"],4,"Ota-onam hozir uyda yo'q (tashqariga chiqib ketishgan).",expl="留守にする = 外出する (uyda bo'lmaslik, tashqariga chiqmoq)"),
         q("t5-v4-28","お皿を【さげて】ください。",["持って来て","持って行って","洗って","ふいて"],2,"Likopchalarni olib keting (yig'ishtiring).",expl="さげる = 持って行く (olib ketmoq, stoldan yig'ishtirmoq)"),
         q("t5-v4-29","私の父は【温厚だ】。",["陽気だ","体温が高い","おだやかだ","太っている"],3,"Otam muloyim (bosiq) odam.",expl="温厚だ = おだやかだ (muloyim, xotirjam tabiatli)"),
         q("t5-v4-30","彼の話し方はいつも【皮肉だ】。",["意地が悪い","役に立つ","わけがわからない","とても優しい"],1,"Uning gapirish tarzi doim kinoyali.",expl="皮肉だ = 意地が悪い (kinoyali, g'arazli)"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t5-v5-31","集中",["私はきれいな外国の切手を集中している。","お店が駅から遠いので、お客が集中しない。","飲み会に参加する人を集中しましょう。","テレビを消して、勉強に集中する。"],4,
           "集中 (しゅうちゅう) = diqqatni jamlash, to'plash.",optsTr=["Men chiroyli chet el markalarini 'diqqat qilyapman' (noto'g'ri, 'to'playapman' bo'lishi kerak).","Do'kon stansiyadan uzoq, shuning uchun mijozlar 'jamlanmaydi' (noto'g'ri).","Ziyofat ishtirokchilarini 'diqqat qilaylik' (noto'g'ri).","Televizorni o'chirib, o'qishga diqqatimni jamlayman. (to'g'ri)"]),
         q("t5-v5-32","あきる",["日本にあきたので、どんな場所でも1人で行けます。","毎日この店のラーメンを食べたので、もうあきた。","ドアをあきて、ベランダへ出ました。","テニスにあきたので、プロのテニス選手を目指すことにした。"],2,
           "あきる (飽きる) = joniga tegmoq, me'daga tegmoq.",optsTr=["Yaponiyaga 'jonim tekkani' uchun, har qayerga yolg'iz bora olaman (noto'g'ri).","Har kuni bu do'konning ramenini yeganim uchun, endi jonimga tegdi. (to'g'ri)","Eshikni 'joniga tegib', balkonga chiqdim (noto'g'ri).","Tennis 'jonimga tekkani' uchun, professional o'yinchi bo'lishga qaror qildim (noto'g'ri)."]),
         q("t5-v5-33","付き合い",["雨が降ってきたので、駅まで付き合いに来てください。","この魚の料理は、ごはんといい付き合いだ。","私と彼の付き合いは、長い。","田口さんと山川さんは仲が悪いので、ときどき付き合いをする。"],3,
           "付き合い (つきあい) = munosabat, aloqa, tanishlik.",optsTr=["Yomg'ir yog'ayotgani uchun stansiyagacha 'munosabat'ga keling (noto'g'ri).","Bu baliq taomi guruch bilan yaxshi 'munosabat'da (noto'g'ri).","U bilan munosabatlarimiz (tanishligimiz) uzoq muddatli. (to'g'ri)","Taguchi va Yamakavaning munosabati yomon, shuning uchun ba'zan 'aloqa qilishadi' (noto'g'ri)."]),
         q("t5-v5-34","じゃま",["あの人は性格がじゃまなので、みんなにきらわれている。","道に大きな石があってじゃまだ。","1週間そうじをしなかったら、部屋がとてもじゃまになった。","この本は、内容がとてもじゃまで、理解できない。"],2,
           "じゃま (邪魔) = xalaqit, to'siq.",optsTr=["Uning xarakteri 'to'siq' bo'lgani uchun hamma yomon ko'radi (noto'g'ri).","Yo'lda katta tosh yotibdi, u juda xalaqit beryapti. (to'g'ri)","1 hafta tozalamasam, xona juda 'xalaqit' bo'lib ketdi (noto'g'ri).","Bu kitobning mazmuni juda 'to'siq' shuning uchun tushuna olmayapman (noto'g'ri)."]),
         q("t5-v5-35","寄る",["私の娘は、私の両親にとても寄っている。","1週間前に寄った荷物が、まだ着きません。","寄った食事をしていると、体によくないですよ。","会社に行く前に、私の家に寄ってください。"],4,
           "寄る (よる) = yo'l-yo'lakay kirib o'tmoq.",optsTr=["Qizim ota-onamga juda 'kirib o'tmoqda' (noto'g'ri).","1 hafta oldin 'kirib o'tgan' yuk hamon kelmadi (noto'g'ri).","'Kirib o'tgan' ovqat yesangiz, sog'liqqa zarar (noto'g'ri).","Ishga borishdan oldin, mening uyimga kirib o'ting. (to'g'ri)"]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t5-g1-1","吉田「あなたも一緒に食事に行く（　）。」山本「うん、行くよ。」",["わ","の","し","のに"],2,"Yoshida: «Siz ham birga ovqatlanishga borasizmi?» Yamamoto: «Ha, boraman.»",expl="〜の？ = ...mi? (ko'proq og'zaki tilda savol berish)"),
         q("t5-g1-2","自分でやると決めた（　）、何が何でもやり抜くぞ。",["以上","以上の","以上から","以上も"],1,"O'zim qilaman deb qaror qilgan ekanman, nima bo'lsa ham oxiriga yetkazaman.",expl="〜以上 = ...ekan, ...gandan keyin albatta"),
         q("t5-g1-3","50個（　）セール品はなくなりますので、お早めに。",["あいだに","しか","限りで","まで"],3,"50 dona sotilgandan so'ng chegirmadagi mahsulotlar tugaydi, shuning uchun tezroq oling.",expl="〜限りで = shu bilan tugaydi, shu chegaragacha"),
         q("t5-g1-4","林さんがなくなったなんて、まさか（　）はずはない。",["そんな","どんな","この","あの"],1,"Hayashi-san vafot etdi degani, aslo bunday bo'lishi mumkin emas.",expl="そんなはずはない = aslo bunday bo'lishi mumkin emas"),
         q("t5-g1-5","明日のハイキングが行われるかどうかは、天気（　）。",["限りだ","次第だ","ばかりだ","通りだ"],2,"Ertangi xiking bo'lish-bo'lmasligi ob-havoga bog'liq.",expl="〜次第だ = ...ga bog'liq"),
         q("t5-g1-6","うれしい（　）、みんなから結婚のお祝いをもらった。",["ものに","ことに","ほどに","わけに"],2,"Qanday quvonchliyki, hammadan to'y sovg'asini oldim.",expl="〜ことに = shunday (quvonchli) narsaki, ..."),
         q("t5-g1-7","参加したい人は、男女に関係なくだれでも参加して（　）。",["できます","できません","かまいます","かまいません"],4,"Qatnashishni xohlovchilar jinsidan qat'iy nazar hammalari qatnashaverishsa bo'ladi.",expl="〜てかまいません = ...sa hechqisi yo'q, ...sa bo'ladi"),
         q("t5-g1-8","試験は明日なのだから、今から（　）ようがない。もうあきらめた。",["準備","準備する","準備して","準備し"],4,"Imtihon ertaga, shuning uchun hozirdan tayyorgarlik ko'rishning imkoni yo'q. Allaqachon taslim bo'ldim.",expl="〜ようがない = ...ishning umuman imkoni yo'q (fe'lning o'zagi qo'shiladi: 準備する -> 準備し)"),
         q("t5-g1-9","たとえこの先（　）、私たちはずっと友だちだ。",["会えなくなったとしても","会ったとしても","会うまいとしたら","会えるとしたら"],1,"Mobodo bundan keyin ko'risha olmasak ham, biz doim do'stmiz.",expl="たとえ〜としても = mobodo ...sa ham"),
         q("t5-g1-10","鈴木「森先生が学校をやめるんだって。」川村「ちっとも（　）よ。」",["知っていた","知らなかった","知ればよかった","知らないはずだ"],2,"Suzuki: «Mori ustoz maktabdan ketarmish.» Kawamura: «Zarracha ham bilmagandim.»",expl="ちっとも〜ない = umuman ...yo'q"),
         q("t5-g1-11","社長は、あの新聞記事をもう（　）。",["読ませていただきましたか","お読みいたしましたか","読んでまいりましたか","お読みになりましたか"],4,"Hurmatli direktor, u gazeta maqolasini o'qib chiqdingizmi?",expl="お〜になる = hurmat shakli (boshqa shaxsga nisbatan)"),
         q("t5-g1-12","この国の将来が（　）。",["楽しんでできます","楽しみでできません","楽しみでなります","楽しみでなりません"],4,"Bu mamlakatning kelajagini juda intizorlik bilan kutyapman (kuta olmayapman darajasida).",expl="〜てならない = juda, g'oyatda (his-tuyg'ular jilovlab bo'lmaydigan darajada)"),
         q("t5-g1-13","このまま木村さんが（　）、木村さんの意見は聞かないことにします。",["来たそうなら","来そうなら","来ないようなら","来るようなら"],3,"Agar Kimura-san kelmaydigan bo'lsa, uning fikrini eshitmaslikka qaror qilamiz.",expl="〜ようなら = agar ...dek holat bo'lsa"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t5-g2-14",None,["教えて","おかげで","親切に","くださった"],4,"To'g'ri tartib: «Ishga kirganimdan so'ng, bo'lim boshlig'i mehribonlik bilan o'rgatganlari sharofati bilan boshqa xodimlardan tezroq ishni o'rganib oldim.»",
           prefix="入社してから、課長が",suffix="、ほかの社員より早く仕事を覚えることができました。",starPos=3,order=[3,1,4,2],expl="To'g'ri tartib: 親切に 教えて くださった おかげで"),
         q("t5-g2-15",None,["言って","言っていた","もう一度","ことを"],3,"To'g'ri tartib: «Kechirasiz-u, boya aytgan narsangizni yana bir marta qaytara olasizmi.»",
           prefix="悪いけど、さっき",suffix="くれる。",starPos=3,order=[2,4,3,1],expl="To'g'ri tartib: 言っていた ことを もう一度 言って"),
         q("t5-g2-16",None,["きれいで","よければ","最高だ","見た目も"],1,"To'g'ri tartib: «Bu restoranning taomlari ta'mi ham yaxshi, ko'rinishi ham chiroyli va eng zo'ridir deb o'ylayman.»",
           prefix="この店の料理は、味も",suffix="と思います。",starPos=3,order=[2,4,1,3],expl="To'g'ri tartib: よければ 見た目も きれいで 最高だ"),
         q("t5-g2-17",None,["ぽろぽろ","とたん","見た","一目"],2,"To'g'ri tartib: «Uzoq safardan qaytib, ota-onamning yuzini bir ko'rishim bilanoq ko'zlarimdan duv-duv yosh to'kildi.»",
           prefix="長い旅から帰って、両親の顔を",suffix="涙がこぼれてきた。",starPos=3,order=[4,3,2,1],expl="To'g'ri tartib: 一目 見た とたん ぽろぽろ"),
         q("t5-g2-18",None,["講演が","予定","林先生による","行われる"],4,"To'g'ri tartib: «Ertaga ertalab soat 10 da universitet zali, Hayashi-sensei tomonidan leksiya o'tkazilishi rejalashtirilgan.»",
           prefix="明日の午前10時から、大学のホールで、",suffix="です。",starPos=3,order=[3,1,4,2],expl="To'g'ri tartib: 林先生による 講演が 行われる 予定"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "新聞の保存のしかた",
       "passage": (
         "私は、いろいろな情報を得るため、日本語の新聞{{19}}、英字新聞も読むようにして\n"
         "います。これは、もう10年続けている習慣です。このことにより、情報を得るだけでなく、\n"
         "英語の勉強にもなっています。長い間読んできた{{20}}、最近では最初のページから\n"
         "ざっと目を通すだけで、おおよその内容を理解できるようになりました。\n\n"
         "ところが問題が1つあります。それは、増えていく新聞を、どうやってわかりやすく整\n"
         "理して保存するかということです。毎週英字新聞を買うので、重ねてそのままにしておけば、\n"
         "もし古い新聞をもう一度読みたくなったときに、どこにあるかわからなくなってしまいます。\n\n"
         "新聞を読むのが大好きな私にとって、古い新聞を捨てるということは{{21}}。その\n"
         "ためいろいろやってみて、最近{{22}}この問題を解決する方法を見つけました。それは、\n"
         "年と月で新聞をわけて箱に入れて保存しておくというやり方です。簡単な方法ですが、結\n"
         "局これがもっとも効率のよい保存方法で、すぐに新聞を取り出せるようになりました。\n"
         "{{23}}ことには、わくわくするような楽しさがあるのです。"
       ),
       "passage_tr": (
         "Men turli ma'lumotlarni olish uchun faqat yapon gazetasini emas, inglizcha gazetani ham o'qishga harakat qilyapman. "
         "Bu allaqachon 10 yildan beri davom etib kelayotgan odatdir. Bu orqali nafaqat ma'lumot olaman, balki ingliz "
         "tilini ham o'rganyapman. Uzoq vaqt davomida o'qib kelganim sharofati bilan, oxirgi paytlarda faqat birinchi "
         "sahifasiga ko'z yugurtirishning o'zi bilan mazmunni tushuna oladigan bo'ldim.\n\n"
         "Biroq bitta muammo bor. U ham bo'lsa, ko'payib borayotgan gazetalarni qanday qilib tushunarli tarzda tartibga "
         "solib saqlashdir. Har hafta inglizcha gazeta olaman, shuning uchun ularni ustma-ust taxlab qo'ysam, mobodo "
         "eski gazetani yana bir marta o'qigim kelganda, uning qayerdaligini bilmay qolaman.\n\n"
         "Gazeta o'qishni yaxshi ko'radigan men uchun, eski gazetalarni tashlab yuborish degan narsani aslo o'ylab ham "
         "bo'lmaydi. Shuning uchun turli usullarni sinab ko'rib, yaqinda nihoyat bu muammoni hal qilish yo'lini topdim. "
         "U yil va oy bo'yicha gazetalarni ajratib, qutiga solib saqlash usulidir. Garchi oddiy usul bo'lsa-da, oxir-oqibat "
         "bu eng samarali saqlash usuli bo'ldi va darrov gazetani olib chiqa oladigan bo'ldim. O'tmishdagi gazetalarni "
         "ko'rishda o'zgacha hayajonli zavq bor-da."
       ),
       "questions": [
         q("t5-g3-19",None,["に限り","に限らず","からして","からすると"],2,
           "日本語の新聞[に限らず] = faqat yapon gazetasigina emas.",blankNo="19",expl="〜に限らず = faqat ...emas, balki ...ham"),
         q("t5-g3-20",None,["a からには / b 理解しようと思います","a ばかりに / b 理解できなくなりました","a おかげで / b 理解できるようになりました","a せいで / b 理解することができます"],3,
           "読んできた[おかげで]、おおよその内容を[理解できるようになりました] = O'qiganim sharofati bilan, taxminiy mazmunni tushuna oladigan bo'ldim.",blankNo="20",expl="〜おかげで = ...sharofati bilan; 〜ようになる = ...adigan holatga kelmoq"),
         q("t5-g3-21",None,["考えません","考えさせません","考えられません","考えさせられません"],3,
           "捨てるということは[考えられません] = tashlab yuborishni hatto o'ylab (tasavvur qilib) ham bo'lmaydi.",blankNo="21",expl="考えられる = o'ylash mumkin (potensial), 考えられない = o'ylab/tasavvur qilib bo'lmaydi"),
         q("t5-g3-22",None,["だんだん","ますます","なかなか","とうとう"],4,
           "いろいろやってみて、最近[とうとう]見つけました = Turli xil narsalarni sinab, oxiri (nihoyat) topdim.",blankNo="22",expl="とうとう = nihoyat, oxir-oqibat"),
         q("t5-g3-23",None,["現在の新聞を見る","過去の新聞を見る","現在の新聞を保存する","過去の新聞を保存する"],2,
           "古い新聞をもう一度読みたくなった (Eski gazetani yana o'qigim kelganda) -> [過去の新聞を見る]ことには...楽しさがあるのです (O'tmishdagi gazetalarni ko'rishda...).",blankNo="23",expl="Kontekst bo'yicha: eski (o'tmishdagi) gazetalarni qayta o'qish/ko'rish zavqi haqida gap ketyapti."),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test05.json yozildi. Jami savol:", tot)
