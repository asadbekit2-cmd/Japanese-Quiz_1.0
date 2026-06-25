# -*- coding: utf-8 -*-
"""test03.json — 第3回 模擬テスト (PDF betlari 28-37, javob 196)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test03.json")

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
  "id": 3, "title_jp": "第3回 模擬テスト", "title_uz": "3-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t3-v1-1","桜の花は、もう【散って】しまった。",["いって","まって","さって","ちって"],4,"Sakura gullari allaqachon to'kilib bo'ldi.",reading="ちって",expl="散る → ちる (to'kilmoq, sochilmoq)"),
         q("t3-v1-2","今の生活に【満足】ですか。",["まんそく","まんぞく","まんそぐ","まんぞぐ"],2,"Hozirgi hayotingizdan mamnunmisiz?",reading="まんぞく",expl="満足 → まんぞく (mamnunlik, qoniqish)"),
         q("t3-v1-3","この駅から【急行】に乗るつもりだ。",["くこう","くうこう","きゅこう","きゅうこう"],4,"Shu bekatdan tezyurar poyezdga chiqmoqchiman.",reading="きゅうこう",expl="急行 → きゅうこう (tezyurar (poyezd))"),
         q("t3-v1-4","彼女は川に落ち、【意識】がなくなった。",["ちしき","にんしき","けんしき","いしき"],4,"U daryoga yiqilib, hushini yo'qotdi.",reading="いしき",expl="意識 → いしき (hush, ong)"),
         q("t3-v1-5","あの人と私の能力の【差】は大きい。",["さ","ざ","さい","ざい"],1,"U bilan mening qobiliyatim o'rtasidagi farq katta.",reading="さ",expl="差 → さ (farq, tafovut)"),
         q("t3-v1-6","新聞に【広告】をのせる。",["ここく","こうく","こうこく","こうくう"],3,"Gazetaga reklama joylashtiraman.",reading="こうこく",expl="広告 → こうこく (reklama, e'lon)"),
         q("t3-v1-7","運動をして、【汗】をたくさんかいた。",["なみだ","あせ","いき","みず"],2,"Sport bilan shug'ullanib, ko'p terladim.",reading="あせ",expl="汗 → あせ (ter)"),
         q("t3-v1-8","夜中の外出を【禁止】する。",["きんし","きんじ","ぎんし","ぎんじ"],1,"Tunda tashqariga chiqish taqiqlanadi.",reading="きんし",expl="禁止 → きんし (taqiq)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t3-v2-9","この国は、天然資源が【ほうふ】だ。",["盛富","宝富","豊富","広富"],3,"Bu mamlakatda tabiiy resurslar mo'l-ko'l.",expl="ほうふ → 豊富 (mo'l-ko'l, boy)"),
         q("t3-v2-10","テストの前に、単語を【あんき】した。",["案記","明記","安記","暗記"],4,"Test oldidan so'zlarni yodladim.",expl="あんき → 暗記 (yod olish)"),
         q("t3-v2-11","地震に【そなえて】、水と食べ物を買う。",["準えて","備えて","供えて","背えて"],2,"Zilzilaga tayyorgarlik ko'rib, suv va oziq-ovqat sotib olaman.",expl="そなえる → 備える (tayyorgarlik ko'rmoq)"),
         q("t3-v2-12","大きなミスをして、仕事を【うしなう】ことになった。",["失う","夫う","矢う","央う"],1,"Katta xato qilib, ishimdan ayriladigan bo'ldim.",expl="うしなう → 失う (yo'qotmoq, ayrilmoq)"),
         q("t3-v2-13","日本のマンガに【きょうみ】があります。",["教味","教見","興味","興見"],3,"Yapon mangasiga qiziqaman.",expl="きょうみ → 興味 (qiziqish)"),
         q("t3-v2-14","結婚して、2人は【ふうふ】になった。",["夫妻","妻夫","夫婦","婦夫"],3,"Turmush qurib, ikkovi er-xotin bo'lishdi.",expl="ふうふ → 夫婦 (er-xotin)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t3-v3-15","高校生のとき、初めて海外で（　）した。",["パスポート","クラスメート","ホームページ","ホームステイ"],4,"O'rta maktabda ilk bor chet elda oilada (homestay) yashadim.",expl="ホームステイ = mahalliy oilada yashash"),
         q("t3-v3-16","今日は、晴れて空気が（　）している。",["燃焼","点火","乾燥","熱中"],3,"Bugun ochiq, havo quruq.",expl="乾燥 = quruqlik, qurish"),
         q("t3-v3-17","その日は、風が強く（　）いました。",["空いて","巻いて","開いて","吹いて"],4,"O'sha kuni shamol kuchli esardi.",expl="吹く = esmoq (shamol)"),
         q("t3-v3-18","彼は、エンジニアの仕事でたくさん（　）いる。",["かせいで","得て","あげて","受けて"],1,"U muhandislik ishida ko'p pul topadi.",expl="稼ぐ (かせぐ) = pul topmoq"),
         q("t3-v3-19","うそを言わず、（　）で話し合いたい。",["意見","本音","解答","正解"],2,"Yolg'on aytmasdan, ochiq dildan (samimiy) gaplashmoqchiman.",expl="本音 = chin dildagi fikr"),
         q("t3-v3-20","この車は、まだ新しいので（　）だ。",["ぴかぴか","ふらふら","ぺこぺこ","くるくる"],1,"Bu mashina hali yangi, shuning uchun yaltirab turibdi.",expl="ぴかぴか = yaltiroq, charaqlagan"),
         q("t3-v3-21","その問題については、よくわからないので（　）できません。",["コート","コンセント","コンクール","コメント"],4,"Bu masala bo'yicha yaxshi bilmaganim uchun izoh bera olmayman.",expl="コメント = izoh, sharh"),
         q("t3-v3-22","毎日、校庭の木の（　）をするのは、大変だ。",["手入れ","手引き","手出し","手抜き"],1,"Har kuni maktab hovlisidagi daraxtlarni parvarish qilish og'ir.",expl="手入れ = parvarish, qarov"),
         q("t3-v3-23","留学させてくれた両親に、（　）しています。",["成功","要望","救助","感謝"],4,"Chet elda o'qishimga imkon bergan ota-onamga minnatdorman.",expl="感謝 = minnatdorchilik"),
         q("t3-v3-24","いただいた本を（　）読もうと思います。",["やがて","いきなり","さっそく","はっきり"],3,"Bergan kitobingizni darrov o'qiyman deb o'ylayapman.",expl="さっそく = darrov, zudlik bilan"),
         q("t3-v3-25","散歩やジョギングなど、軽い運動は（　）によい。",["体重","元気","体温","健康"],4,"Sayr va yugurish kabi yengil mashqlar salomatlikka foydali.",expl="健康 = salomatlik"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t3-v4-26","彼の考え方は、いつも【ネガティブ】だ。",["まじめ","ふまじめ","肯定的","否定的"],4,"Uning fikrlash tarzi doim salbiy.",expl="ネガティブ = 否定的 (salbiy)"),
         q("t3-v4-27","2本のロープを【つないで】ください。",["関係して","接続して","注意して","切断して"],2,"Ikki arqonni bir-biriga ulang.",expl="つなぐ = 接続する (ulamoq)"),
         q("t3-v4-28","彼は、自分の言ったことを【打ち消した】。",["忘れた","途中でやめた","否定した","そのままにした"],3,"U aytgan gapini inkor qildi.",expl="打ち消す = 否定する (inkor qilmoq)"),
         q("t3-v4-29","【さっさと】仕事を終わらせた。",["早く","ゆっくりと","正確に","だいたい"],1,"Ishni tez (darrov) tugatdi.",expl="さっさと = 早く (tez, darrov)"),
         q("t3-v4-30","彼女は、いつも【落ち着いて】いる。",["優秀だ","有能だ","冷静だ","温厚だ"],3,"U doim xotirjam.",expl="落ち着いている = 冷静だ (xotirjam)"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t3-v5-31","気に入る",["明日のテストが気に入って、とても心配だ。","その店の服がとても気に入ったので、買うことにした。","どうも午後は、よい天気になるような気に入る。","会社に着いてから、さいふがないことに気に入った。"],2,
           "気に入る = yoqmoq, ma'qul kelmoq.",optsTr=["Ertangi test 'yoqib', juda xavotirdaman (noto'g'ri).","Do'kondagi kiyim juda yoqqani uchun, sotib olishga qaror qildim. (to'g'ri)","Tushdan keyin ob-havo yaxshi bo'ladiganga 'yoqaman' (noto'g'ri).","Ishxonaga yetib, hamyonim yo'qligi 'yoqdi' (noto'g'ri)."]),
         q("t3-v5-32","まぜる",["花びんに花をまぜようと思います。","このシャツにボタンをまぜていただけませんか。","たまごと牛乳をよくまぜてください。","顔をよくまぜてから、外に出かけましょう。"],3,
           "まぜる = aralashtirmoq.",optsTr=["Guldonga gulni 'aralashtirmoqchiman' (noto'g'ri).","Bu ko'ylakka tugmani 'aralashtirib' bera olasizmi (noto'g'ri).","Tuxum va sutni yaxshilab aralashtiring. (to'g'ri)","Yuzni yaxshilab 'aralashtirib', tashqariga chiqaylik (noto'g'ri)."]),
         q("t3-v5-33","現実",["私はものを考えるより現実が得意だ。","まだ試験に受かったという現実がわかる。","昔にくらべて、現実はきびしい時代だと思います。","とても現実とは思えないニュースを聞いた。"],4,
           "現実 = haqiqat, reallik.",optsTr=["Men o'ylashdan ko'ra 'reallik'ni yaxshi eplayman (noto'g'ri).","Hali imtihondan o'tganlik 'realligi' bilinadi (noto'g'ri).","Ilgariga nisbatan, 'reallik' qattiq davr deb o'ylayman (noto'g'ri).","Aslo haqiqat deb bo'lmaydigan yangilik eshitdim. (to'g'ri)"]),
         q("t3-v5-34","おかず",["昼食と夕食のあいだのおかずに、ケーキを食べた。","今日の晩ごはんのおかずは、肉と野菜の料理です。","おかずを沸かしてお茶を飲みます。","私の好きなおかずは、ごはんよりもパンです。"],2,
           "おかず = garnir, ovqatga qo'shimcha taom.",optsTr=["Tushlik va kechki ovqat orasidagi 'garnir'ga tort yedim (noto'g'ri).","Bugungi kechki ovqat garniri — go'sht va sabzavot taomi. (to'g'ri)","'Garnir'ni qaynatib choy ichaman (noto'g'ri).","Yoqtirgan 'garnirim' — guruchdan ko'ra non (noto'g'ri)."]),
         q("t3-v5-35","できあがる",["私の夢は、先生にできあがることです。","エレベーターで10階までできあがってください。","階段をできあがると、私の家があります。","料理ができあがったので、食べてください。"],4,
           "できあがる = tayyor bo'lmoq, bitmoq.",optsTr=["Orzuyim — o'qituvchiga 'tayyor bo'lish' (noto'g'ri).","Lift bilan 10-qavatgacha 'tayyor bo'ling' (noto'g'ri).","Zinadan 'tayyor bo'lsang', mening uyim bor (noto'g'ri).","Ovqat tayyor bo'ldi, shuning uchun yeng. (to'g'ri)"]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t3-g1-1","夏から秋（　）、いろいろな祭りがひらかれる。",["をかけて","にかけて","でかけて","とかけて"],2,"Yozdan kuzgacha bo'lgan davrda turli bayramlar o'tkaziladi.",expl="〜から〜にかけて = ...dan ...gacha (davr oralig'i)"),
         q("t3-g1-2","森さんはこの会社にエンジニア（　）採用された。",["として","といって","だと","だとして"],1,"Mori-san bu kompaniyaga muhandis sifatida ishga olindi.",expl="〜として = ...sifatida"),
         q("t3-g1-3","山田さんはアメリカに住んでいた（　）、英語の発音がきれいですね。",["だけは","だけに","ところは","ところに"],2,"Yamada-san Amerikada yashagani uchun, ingliz talaffuzi chiroyli ekan.",expl="〜だけに = aynan ...gani uchun"),
         q("t3-g1-4","家を出た（　）、大雨が降ってきた。",["たびに","とたん","ごとに","からには"],2,"Uydan chiqishim bilanoq, kuchli yomg'ir yog'a boshladi.",expl="〜たとたん = ...ishi bilanoq"),
         q("t3-g1-5","最近、そうじをしていないので、部屋がごみ（　）だ。",["しか","気味","きり","だらけ"],4,"Yaqinda tozalamaganim uchun, xona axlatga to'la.",expl="〜だらけ = ...ga to'la, ...ga botgan"),
         q("t3-g1-6","彼はしっかりしているので、（　）ことはないでしょう。",["心配し","心配しよう","心配しろ","心配する"],4,"U ishonchli odam, shuning uchun xavotir olishga hojat yo'q.",expl="〜することはない = ...ga hojat yo'q"),
         q("t3-g1-7","ラーメンを作ったので、（　）食べてください。",["熱いうちで","熱いうちへ","熱いうちに","熱いうちが"],3,"Ramen pishirdim, issig'ida yeng.",expl="〜うちに = ...turib, ...gacha (holat o'zgarmasdan)"),
         q("t3-g1-8","これは、2、3日前に先生から（　）本です。",["お借りした","借りてあげた","借りてくださった","お借りになった"],1,"Bu 2-3 kun oldin o'qituvchidan olgan kitobim.",expl="お〜する = kamtarlik shakli (men oldim)"),
         q("t3-g1-9","あの人は、まるで本当の家族（　）かのように、私に優しかった。",["だ","だろう","である","だったら"],3,"U xuddi haqiqiy oilamdek menga mehribon edi.",expl="〜であるかのように = xuddi ...dek"),
         q("t3-g1-10","そこに置いてあるパンは、私の（　）です。",["食べきり","食べかけ","食べたまま","食べたばかり"],2,"U yerdagi non — mening yarim yeб qo'yganim.",expl="〜かけ = yarim ...gan, boshlab qo'yilgan"),
         q("t3-g1-11","ご病気が（　）を聞いて、安心しました。",["治ったということ","治ったというもの","治るというところ","治るというほど"],1,"Kasalingiz tuzalganini eshitib, xotirjam bo'ldim.",expl="〜ということ = ...ganligi (faktni bildiradi)"),
         q("t3-g1-12","きのうは、大雨が（　）、一日じゅう外でサッカーをしました。",["降っていたからといって","降っていたからには","降っていたにもかかわらず","降っていたにしては"],3,"Kecha kuchli yomg'ir yog'ayotgan bo'lsa-da, kun bo'yi tashqarida futbol o'ynadik.",expl="〜にもかかわらず = ...ga qaramay"),
         q("t3-g1-13","社長「みなさん、今は大変なときですが、社員一同、会社のために（　）。」社員「はい、がんばります。」",["がんばるのではないですか","がんばったではありませんか","がんばらないのではないですか","がんばろうではありませんか"],4,"Direktor: «Hozir og'ir payt, lekin xodimlar birgalashib kompaniya uchun harakat qilaylik-a.»",expl="〜ようではありませんか = kelinglar, ...aylik"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t3-g2-14",None,["いい","もらっても","帰らせて","もう"],2,"To'g'ri tartib: «Kechirasiz, boshim og'riyapti, bugun endi (meni) qaytishimga ruxsat bersangiz bo'ladimi?»",
           prefix="女の学生「悪いけど、頭が痛いから、今日は",suffix="？」",starPos=3,order=[4,3,2,1],expl="To'g'ri tartib: もう帰らせてもらってもいい"),
         q("t3-g2-15",None,["ので","お願い","まいります","よろしく"],1,"To'g'ri tartib: «Biroz kechikdim; hozir zalga boraman, iltimos, yaxshi munosabatda bo'lishingizni so'rayman.»",
           prefix="少し遅れましたが、今から会場に",suffix="いたします。",starPos=2,order=[3,1,4,2],expl="To'g'ri tartib: まいりますのでよろしくお願い (いたします)"),
         q("t3-g2-16",None,["とても","しても","たとえ","難しいと"],4,"To'g'ri tartib: «Bu ishni qilish juda qiyin bo'lsa ham, harakatni davom ettirsam, qachondir albatta uddalay olaman deb ishonaman.»",
           prefix="この仕事をするのが、",suffix="努力を続ければ、いつかきっとできるようになると信じている。",starPos=3,order=[3,1,4,2],expl="To'g'ri tartib: たとえとても難しいとしても"),
         q("t3-g2-17",None,["ない","あやまる","ほか","より"],3,"To'g'ri tartib: «Mening xatoyim tufayli reja barbod bo'ldi, shuning uchun kechirim so'rashdan boshqa chora yo'q deb o'ylab, darrov xat yubordim.»",
           prefix="私のミスで、計画が失敗してしまったのだから、",suffix="と思い、すぐにメールを送った。",starPos=3,order=[2,4,3,1],expl="To'g'ri tartib: あやまるよりほかない"),
         q("t3-g2-18",None,["ひどい","ちょっと","対する","態度は"],4,"To'g'ri tartib: «Chetdan qaraganda ham, uning qiziga bo'lgan munosabati biroz qo'pol deb o'ylayman.»",
           prefix="まわりから見ても、彼の彼女に",suffix="と思う。",starPos=2,order=[3,4,2,1],expl="To'g'ri tartib: 対する態度はちょっとひどい"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "新マーク発表",
       "passage": (
         "A市の青木市長は、チューリップの花をモチーフにした新しい市のマークを発表した。"
         "A市市役所の広報課{{19a}}、この新しいマークは青木市長からのメッセージを{{19b}}。"
         "マークのまんなかに、A市の花であるチューリップをデザインし、まわりの小さい模様は"
         "市民が楽しく生活している様子を表しているという。このマークは、市長が親しみやすさと"
         "あたたかさを{{20}}ものにしたいと考えて、もとになるアイデアを出し、A市に住むデザイナーに頼んで作った。\n"
         "A市は、今日から市のホームページ{{21}}、この新しいマークを公開する。また、近日中に"
         "このマークをもとにしてキャラクターを作り、その名前を市民から広く募集する予定だ。\n"
         "日本では、各市町村にいろいろなキャラクターがいて、人気者になっている。とても{{22}}、"
         "ハンカチなどの商品になったり、テレビで取り上げられることもある。A市のキャラクターにも、"
         "たくさんの人に愛される名前を考えて{{23}}と、市長は語っている。"
       ),
       "passage_tr": (
         "A shahar meri Aoki tulpan gulini asos qilib olgan shaharning yangi belgisini (logotipini) e'lon qildi. "
         "A shahar hokimligi matbuot bo'limiga ko'ra, bu yangi belgi mer Aokining xabarini ifodalab turarmish. "
         "Belgining markazida A shaharning guli — tulpan tasvirlangan, atrofdagi mayda naqshlar esa fuqarolarning "
         "xushchaqchaq hayotini aks ettiradi. Bu belgini mer yaqinlik va iliqlikni his ettiradigan qilmoqchi bo'lib, "
         "asos g'oyani taklif etgan va A shaharda yashovchi dizaynerga buyurtma berib yasatgan. A shahar bugundan "
         "shaharning veb-saytida bu yangi belgini ommaga taqdim etadi. Shuningdek, yaqin kunlarda shu belgi asosida "
         "personaj yaratib, uning nomini fuqarolardan keng so'rab olish rejalashtirilgan. Yaponiyada har bir shahar "
         "va qishloqda turli personajlar bo'lib, ular mashhur. Juda mashhur personajlar ro'molcha kabi mahsulotlarga "
         "aylanadi yoki televideniyada namoyish etiladi. A shahar personajiga ham ko'p odamlar sevadigan nom o'ylab "
         "qo'yishlarini istayman, deb mer aytmoqda."
       ),
       "questions": [
         q("t3-g3-19",None,["からして ／ 表すことだ","にしろ ／ 表すものだ","によると ／ 表しているそうだ","にかかわらず ／ 表したわけだ"],3,
           "[a によると]…[b 表しているそうだ] = ...ga ko'ra ... ifodalarmish.",blankNo="19",expl="〜によると = ...ga ko'ra; 〜そうだ = ...mish (eshitilgan)"),
         q("t3-g3-20",None,["感じさせる","感じようとする","感じないでもない","感じがちな"],1,
           "親しみやすさとあたたかさを[感じさせる]ものに = yaqinlik va iliqlikni his ettiradigan qilib.",blankNo="20",expl="〜させる = his ettirmoq (orttirma nisbat)"),
         q("t3-g3-21",None,["にともなって","において","につれて","に対して"],2,
           "ホームページ[において]公開する = veb-saytda e'lon qiladi.",blankNo="21",expl="〜において = ...da (joy/soha)"),
         q("t3-g3-22",None,["市町村のキャラクター","このマークのキャラクター","新しいキャラクター","人気があるキャラクター"],4,
           "とても[人気があるキャラクター]は商品になる = juda mashhur personaj mahsulotga aylanadi.",blankNo="22",expl="kontekstga ko'ra: mashhur personajlar haqida"),
         q("t3-g3-23",None,["つけられてほしい","つけてもいい","つけてみたい","つけてほしい"],4,
           "名前を考えて[つけてほしい] = nom o'ylab qo'yishlarini istayman.",blankNo="23",expl="〜てほしい = ...ishlarini istayman"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test03.json yozildi. Jami savol:", tot)
