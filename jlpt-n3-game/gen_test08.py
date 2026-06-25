# -*- coding: utf-8 -*-
"""test08.json — 第8回 模擬テスト (PDF betlari 78-87, javob 201)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test08.json")

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
  "id": 8, "title_jp": "第8回 模擬テスト", "title_uz": "8-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t8-v1-1","大きな鳥が【飛んで】いるのを見ました。",["あそんで","よんで","とんで","さけんで"],3,"Katta qush uchib yurganini ko'rdim.",reading="とんで",expl="飛ぶ → とぶ (uchmoq)"),
         q("t8-v1-2","子どもは、【無料】で入れます。",["むりょ","むりょう","ぶりょ","ぶりょう"],2,"Bolalar bepul kirishlari mumkin.",reading="むりょう",expl="無料 → むりょう (bepul, tekin)"),
         q("t8-v1-3","この道は、車の【通行】ができない。",["とうこう","とうごう","つうこう","つうごう"],3,"Bu yo'ldan mashina o'tolmaydi.",reading="つうこう",expl="通行 → つうこう (yurish, qatnov, o'tish)"),
         q("t8-v1-4","彼は、とても【疲れて】いるようだ。",["つかれて","あきれて","くたびれて","おそれて"],1,"U juda charchaganga o'xshaydi.",reading="つかれて",expl="疲れる → つかれる (charchamoq)"),
         q("t8-v1-5","この計画には、悪いところもあるが、よい【面】もある。",["てん","めん","へん","けん"],2,"Bu rejaning yomon tomonlari ham, yaxshi tomoni ham bor.",reading="めん",expl="面 → めん (tomon, yuza, jihat)"),
         q("t8-v1-6","友だちの【知恵】を借りて、課題を完成させました。",["ちえ","ちしき","ちせい","ちのう"],1,"Do'stimning aqlidan (maslahatidan) foydalanib, vazifani tugatdim.",reading="ちえ",expl="知恵 → ちえ (aql, zakovat, tadbir)"),
         q("t8-v1-7","現代には【多様】な生き方がある。",["おおさま","たさま","おおよう","たよう"],4,"Hozirgi zamonda turli-tuman yashash tarzi bor.",reading="たよう",expl="多様 → たよう (xilma-xil, turli-tuman)"),
         q("t8-v1-8","荷物は、きのう【到着】しました。",["とちゃく","とうちゃく","どちゃく","どうちゃく"],2,"Yuk kecha yetib keldi.",reading="とうちゃく",expl="到着 → とうちゃく (yetib kelish, manzilga yetish)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t8-v2-9","その決定に、【ふまん】を言う人がたくさんいた。",["否満","無満","不満","未満"],3,"Bu qarordan norozilik bildirgan odamlar ko'p edi.",expl="ふまん → 不満 (norozilik)"),
         q("t8-v2-10","駅前でビルを【けんちく】している。",["建設","建造","建立","建築"],4,"Bekat oldida bino qurilyapti.",expl="けんちく → 建築 (qurilish, me'morchilik)"),
         q("t8-v2-11","旅行をして自宅に【もどって】、安心した。",["戻って","帰って","返って","来って"],1,"Sayohatdan o'z uyimga qaytib, xotirjam bo'ldim.",expl="もどる → 戻る (qaytmoq, qaytib kelmoq)"),
         q("t8-v2-12","校則違反を【みとめる】ことはできない。",["求める","救める","許める","認める"],4,"Maktab qoidasini buzishni tan olib (ruxsat berib) bo'lmaydi.",expl="みとめる → 認める (tan olmoq, e'tirof etmoq)"),
         q("t8-v2-13","東京の【こうがい】に家を買いました。",["郊外","戸外","口外","校外"],1,"Tokio chekkasida (atrofida) uy sotib oldim.",expl="こうがい → 郊外 (shahar chekkasi, atrof)"),
         q("t8-v2-14","今月の【やちん】を払った。",["家貸","屋貸","家賃","屋賃"],3,"Shu oylik uy ijara haqini to'ladim.",expl="やちん → 家賃 (uy ijara haqi)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t8-v3-15","現代社会では、だれもが（　）を感じている。",["センス","センチメンタル","ストレス","ニュアンス"],3,"Hozirgi jamiyatda hamma stress his qiladi.",expl="ストレス = stress, ruhiy zo'riqish"),
         q("t8-v3-16","書類のこの部分を（　）してください。",["変更","変化","変革","変身"],1,"Hujjatning bu qismini o'zgartiring.",expl="変更 = o'zgartirish (rejani, ma'lumotni)"),
         q("t8-v3-17","会社に入るために、（　）を受けた。",["対応","対面","面接","応対"],3,"Kompaniyaga kirish uchun suhbatdan o'tdim.",expl="面接 = suhbat, intervyu"),
         q("t8-v3-18","海に（　）、魚をとった。",["しずんで","もぐって","わたって","ころんで"],2,"Dengizga sho'ng'ib, baliq tutdim.",expl="もぐる = sho'ng'imoq, suvga sho'ng'imoq"),
         q("t8-v3-19","私の（　）は、人とすぐになかよくなれることです。",["高所","低所","長所","短所"],3,"Mening yaxshi tomonim — odamlar bilan tez til topisha olishim.",expl="長所 = yaxshi tomon, fazilat"),
         q("t8-v3-20","生まれた国を（　）、10年ほどたった。",["渡って","乗り越えて","曲がって","離れて"],4,"Tug'ilgan mamlakatimni tark etib, 10 yilcha bo'ldi.",expl="離れる = ajralmoq, uzoqlashmoq, tark etmoq"),
         q("t8-v3-21","私の趣味は、プラモデルを（　）ことです。",["まとめあげる","組み立てる","立てかける","作り置く"],2,"Mening sevimli mashg'ulotim — plastik modellarni yig'ish (qurib chiqish).",expl="組み立てる = yig'moq, qismlardan qurmoq"),
         q("t8-v3-22","マラソン大会に参加する人は、参加（　）を払ってください。",["価","金","料","値"],3,"Marafon musobaqasida qatnashadiganlar ishtirok haqini to'lasin.",expl="参加料 = ishtirok haqi (〜料 = haq, to'lov)"),
         q("t8-v3-23","あの人の仕事は、雑誌の（　）です。",["設立","保護","整備","編集"],4,"U odamning ishi — jurnal tahririyati (muharrirligi).",expl="編集 = tahrir qilish, muharrirlik"),
         q("t8-v3-24","ものごとをよく（　）してみましょう。",["感動","観察","関係","熱中"],2,"Narsalarni yaxshilab kuzatib ko'raylik.",expl="観察 = kuzatish, kuzatuv"),
         q("t8-v3-25","山本さんは、（　）で、うそをつかない人です。",["軽薄","派手","地味","誠実"],4,"Yamamoto-san halol (samimiy), yolg'on gapirmaydigan odam.",expl="誠実 = halol, samimiy, vijdonli"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t8-v4-26","彼女は、とても【わがままだ】。",["親切だ","勝手だ","優しい","冷たい"],2,"U juda o'zboshimcha (injiq).",expl="わがまま = o'zboshimcha, injiq → 勝手だ (o'zicha ish qiladigan)"),
         q("t8-v4-27","私はその話を【全然】知らなかった。",["今まで","そのときは","二度と","少しも"],4,"Men bu gapni mutlaqo bilmasdim.",expl="全然〜ない = umuman/mutlaqo ...emas → 少しも〜ない (zarracha ham emas)"),
         q("t8-v4-28","商売でお金を【もうけた】。",["得た","なくした","借りた","貸した"],1,"Savdoda pul ishladim (topdim).",expl="もうける = foyda qilmoq, pul ishlamoq → 得た (qo'lga kiritdi)"),
         q("t8-v4-29","質問があれば、【どんどん】聞いてください。",["よく考えてから","遠慮しないで","みんな一緒に","全部まとめて"],2,"Savolingiz bo'lsa, tortinmasdan so'rayvering.",expl="どんどん = bemalol, ketma-ket, tortinmay → 遠慮しないで"),
         q("t8-v4-30","先輩に【アドバイス】をもらった。",["命令","お礼","助言","心配"],3,"Kattadan (sempaydan) maslahat oldim.",expl="アドバイス = maslahat → 助言"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t8-v5-31","ためす",["試験中にうで時計を見て、時間をためした。","将来はお金をためして、大きな家をたてるつもりです。","古い自転車をためして、乗れるようになった。","日本語の力をためすために、テストを受けようと思います。"],4,
           "ためす(試す) = sinab ko'rmoq, tekshirib ko'rmoq.",optsTr=["Imtihon paytida qo'l soatga qarab, vaqtni 'sinadim' (noto'g'ri — 確認 kerak).","Kelajakda pulni 'sinab', katta uy quraman (noto'g'ri — ためる/jamg'armoq kerak).","Eski velosipedni 'sinab', minadigan bo'ldim (noto'g'ri — 直す kerak).","Yapon tili kuchimni sinash uchun test topshirmoqchiman. (to'g'ri)"]),
         q("t8-v5-32","アンケート",["コンサートの終わりに何度もアンケートがあって、盛り上がった。","大学生活についてのアンケートに質問した。","運動不足なので、友だちとアンケートをしに行った。","クラス全員にアンケートを取って、やり方を決めた。"],4,
           "アンケート = so'rovnoma, anketa.",optsTr=["Konsert oxirida ko'p marta 'so'rovnoma' bo'lib, qizib ketdi (noto'g'ri — アンコール kerak).","Universitet hayoti haqidagi 'so'rovnoma'ga savol berdim (noto'g'ri).","Sport yetishmaganidan, do'stim bilan 'so'rovnoma' qilgani bordik (noto'g'ri).","Sinfdagi hammadan so'rovnoma olib, usulni belgiladik. (to'g'ri)"]),
         q("t8-v5-33","配る",["買い物のとき、レジでお金を配った。","テスト用紙を全員に配ってください。","きのうは母の誕生日だったので、母にプレゼントを配りました。","このパソコンは、作動が早く配られている。"],2,
           "配る = tarqatmoq, ulashmoq.",optsTr=["Xarid paytida kassada pulni 'tarqatdim' (noto'g'ri — 払う kerak).","Test qog'ozlarini hammaga tarqating. (to'g'ri)","Kecha onamning tug'ilgan kuni edi, onamga sovg'a 'tarqatdim' (noto'g'ri — あげる kerak).","Bu kompyuter ishlashi tez 'tarqatilgan' (noto'g'ri)."]),
         q("t8-v5-34","係",["うちの子どもは、クラスのそうじの係だ。","田中さんと鈴木さんは係がよくない。","これは、野菜に見えますが、果物の係です。","私の係は、会社員です。"],1,
           "係(かかり) = mas'ul (xodim), navbatchi, vazifa egasi.",optsTr=["Mening bolam sinfning tozalik mas'uli (navbatchisi). (to'g'ri)","Tanaka va Suzuki 'mas'uli' yaxshi emas (noto'g'ri — 仲 kerak).","Bu sabzavotga o'xshaydi, lekin mevaning 'mas'uli' (noto'g'ri — 仲間/種類 kerak).","Mening 'mas'ulim' — kompaniya xodimi (noto'g'ri — 仕事/職業 kerak)."]),
         q("t8-v5-35","挑戦",["今年は、新しい仕事に挑戦してみたい。","強い選手とテニスの挑戦をして、負けた。","人と出会う挑戦は、多ければ多いほどいい。","あの2人は仲が悪くて、いつも挑戦している。"],1,
           "挑戦(ちょうせん) = sinov, urinib ko'rish, da'vat (challenge).",optsTr=["Bu yil yangi ishga urinib ko'rmoqchiman (challenge qilmoqchiman). (to'g'ri)","Kuchli o'yinchi bilan tennis 'challenge'i qilib, yutqazdim (noto'g'ri — 試合 kerak).","Odam bilan uchrashish 'challenge'i ko'p bo'lsa yaxshi (noto'g'ri — 機会 kerak).","U ikkovi yomon, doim 'challenge' qiladi (noto'g'ri — けんか kerak)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t8-g1-1","松田「今日、飲み会に行く?」竹中「明日のテストの準備もある（　）、今日は行かないよ。」",["けど","と","し","まで"],3,"Matsuda: «Bugun ziyofatga borasanmi?» Takenaka: «Ertangi testga tayyorgarlik ham bor-u, bugun bormayman.»",expl="〜し = ...-u, ham (sabablarni sanash)"),
         q("t8-g1-2","料理がまずく、店員の態度も悪い。（　）店には二度と行きたくない。",["あんな","どんな","ある","どの"],1,"Ovqati ham bemaza, xodimning muomalasi ham yomon. Bunday do'konga ikkinchi bormayman.",expl="あんな = unaqa, bunaqa (salbiy holatga ishora)"),
         q("t8-g1-3","この町は、富士山がよく見える（　）、富士見町という名前が付いた。",["ことに","ことから","ことを","ことは"],2,"Bu shaharchadan Fuji tog'i yaxshi ko'rinishi sababli, Fujimi-machi degan nom berilgan.",expl="〜ことから = ...ligi sababli, shu sababdan"),
         q("t8-g1-4","いくらいそがしい（　）、まったく運動しないのは、体によくない。",["からして","からといって","からには","からあって"],2,"Qanchalik band bo'lsang ham, mutlaqo sport qilmaslik salomatlik uchun yomon.",expl="〜からといって = ...deb (shu bahonada ham)"),
         q("t8-g1-5","すべての大学生が、（　）まじめに勉強しているわけではない。",["かわりに","かろうじて","かえって","かならずしも"],4,"Hamma talaba ham albatta tirishib o'qiydi, deb bo'lmaydi.",expl="かならずしも〜わけではない = har doim ham ...emas"),
         q("t8-g1-6","今日はとても暑いので、プールで泳ぎたくて（　）。",["しかたない","しない","できない","かぎらない"],1,"Bugun juda issiq, basseynda suzgim kelib chidab bo'lmayapti.",expl="〜たくてしかたない = ...gisi kelib chidab bo'lmaslik"),
         q("t8-g1-7","男の学生「空港までは2時間かかるから、8時に（　）10時に着くね。」",["出発し","出発すれば","出発しようと","出発するのは"],2,"O'g'il bola: «Aeroportga 2 soat ketadi, shuning uchun 8 da jo'nasak, 10 da yetib boramiz.»",expl="〜ば = ...sa (shart)"),
         q("t8-g1-8","先生がみんなに、「このゼミの生徒は優秀ですね」と（　）。",["おっしゃいました","うかがいました","申しました","申し上げました"],1,"O'qituvchi hammaga: «Bu seminardagi talabalar a'lo ekan» dedilar.",expl="おっしゃる = 言う ning hurmat shakli (dedilar)"),
         q("t8-g1-9","2時からの会議のために、資料を用意（　）ください。",["することになって","しておいて","するようになって","してくれて"],2,"Soat 2 dagi yig'ilish uchun, hujjatlarni oldindan tayyorlab qo'ying.",expl="〜ておく = oldindan ...qilib qo'ymoq"),
         q("t8-g1-10","残念ながら、この実験は失敗だと（　）。",["言わないではない","言わないでもない","言わざるが得ない","言わざるを得ない"],4,"Afsuski, bu tajriba muvaffaqiyatsiz deb aytmaslikning iloji yo'q.",expl="〜ざるを得ない = ...maslikning iloji yo'q, ...ishga majbur"),
         q("t8-g1-11","これは、ずっと前に私が作った作品に（　）。",["まちがいます","まちがいではありません","ちがいます","ちがいありません"],4,"Bu — ancha oldin men yaratgan asar ekaniga shubha yo'q.",expl="〜にちがいない = ...ligiga shubha yo'q, albatta ...dir"),
         q("t8-g1-12","苦しいことのあとにいいことがあるのが、（　）と思います。",["人生という点だ","人生というところだ","人生というものだ","人生というままだ"],3,"Qiyinchilikdan keyin yaxshilik bo'lishi — hayot degani shu, deb o'ylayman.",expl="〜というものだ = ...degani shu (umumiy haqiqatni aytish)"),
         q("t8-g1-13","チェックアウトの時間に間に合わず、ホテルに追加でお金を（　）。",["払わせることになった","払わすようにした","払うはめになった","払わせるようにした"],3,"Chiqish (checkout) vaqtiga ulgurmay, mehmonxonaga qo'shimcha pul to'lashga majbur bo'lib qoldim.",expl="〜はめになる = (noxush) ...holatga tushib qolmoq"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t8-g2-14",None,["通りに","書いて","ある","やってみて"],1,"To'g'ri jumla: «Men ham yaxshi bilmayman, qo'llanmada yozilganday qilib ko'r-chi.»",
           prefix="「私もよくわからないから、説明書に",suffix="よ。」",starPos=3,order=[2,3,1,4],expl="To'g'ri tartib: 書いてあるとおりにやってみて"),
         q("t8-g2-15",None,["なりたい","お見せ","ようでしたら","ごらんに"],3,"To'g'ri jumla: «Mana, men yig'ayotgan mashina kataloglari, ko'rmoqchi bo'lsangiz, ko'rsataman.»",
           prefix="こちらが、私が集めている車のカタログですが、",suffix="しますよ。",starPos=3,order=[4,1,3,2],expl="To'g'ri tartib: ごらんになりたいようでしたらお見せ (ごらんになる = «ko'rmoq» hurmat shakli)"),
         q("t8-g2-16",None,["簡単な","軽い","上","ので"],2,"To'g'ri jumla: «Bu yangi changyutgich foydalanish oson bo'lgani ustiga, yengil bo'lgani uchun juda qulay.»",
           prefix="この新しいそうじ機は、使い方が",suffix="とても便利だ。",starPos=3,order=[1,3,2,4],expl="To'g'ri tartib: 簡単な上軽いので (〜上 = ...gani ustiga)"),
         q("t8-g2-17",None,["という","では","好きだ","わけ"],4,"To'g'ri jumla: «Yapon bo'lgani uchun ham, hamma sushi yoki tempurani yaxshi ko'radi degani emas.»",
           prefix="日本人だからといって、だれもがすしや天ぷらが",suffix="ない。",starPos=3,order=[3,1,4,2],expl="To'g'ri tartib: 好きだというわけではない (〜というわけではない = ...degani emas)"),
         q("t8-g2-18",None,["反する","だけ","こと","に"],3,"To'g'ri jumla: «Yoshligimda men ota-onamning umidiga zid ishlarnigina qilardim.»",
           prefix="若いころの私は、両親の期待",suffix="していた。",starPos=3,order=[4,1,3,2],expl="To'g'ri tartib: に反することだけ (〜に反する = ...ga zid)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "働く女性のためのセミナー",
       "passage": (
         "今度の日曜日に、働く女性を応援するためのセミナー、「ジョブ・セミナー 働く女性の新しい生き方」"
         "の第1回目の講座が、駅前の市民ホールで行われる予定です。\n"
         "現代の働く女性には、会社員、母、妻、娘など、いろいろな役割があり、いそがしい人が増えています。"
         "しかし以前よりいそがしくなった{{19a}}、手伝ってくれる人がいないのが{{19b}}。"
         "このセミナーでは、さまざまな業界で活躍されている女性が講師となり、全5回の予定で、"
         "{{20}}女性の生き方、上手な働き方を参加者とともに考えていきます。"
         "ただ講演を聞く{{21}}、質問をしたり、意見を言える方を募集します。\n"
         "第1回目の講師は、会社を経営する森川花子さんです。「仕事を持つ女性の時間の使い方」をテーマに"
         "セミナーを行います。講演のあとに、講師と参加者の方々が交流することができるパーティーもあります。\n"
         "第2回目{{22}}講師の予定など、その他の内容については、市民ホールのホームページで公開しています。"
         "参加をご希望の方は、市民ホール事務所まで直接電話でお申し込みください。みなさまのご参加を{{23}}。"
       ),
       "passage_tr": (
         "Kelasi yakshanba kuni, ishlaydigan ayollarni qo'llab-quvvatlash uchun «Job-seminar: ishlaydigan "
         "ayolning yangi hayot tarzi» seminarining 1-mashg'uloti bekat oldidagi shahar zalida o'tkaziladi. "
         "Hozirgi ishlaydigan ayolning kompaniya xodimi, ona, xotin, qiz kabi turli rollari bor va band "
         "odamlar ko'paymoqda. Biroq ilgarigidan band bo'lib qolganiga QARAMAY, yordam beradigan odam "
         "yo'qligi — HOZIRGI AHVOL. Bu seminarda turli sohalarda faoliyat yuritayotgan ayollar o'qituvchi "
         "bo'lib, jami 5 marta o'tkazilishi rejalashtirilgan; KELAJAKDAGI ayol hayoti va mohirona ishlash "
         "usulini ishtirokchilar bilan birga o'ylab ko'ramiz. Shunchaki ma'ruza eshitishnigina EMAS, balki "
         "savol bera oladigan, fikr bildira oladigan kishilarni taklif qilamiz. "
         "1-mashg'ulot o'qituvchisi — kompaniya rahbari Morikava Xanako. «Ishlaydigan ayolning vaqtdan "
         "foydalanishi» mavzusida seminar o'tkazadi. Ma'ruzadan keyin o'qituvchi va ishtirokchilar "
         "muloqot qila oladigan ziyofat ham bor. "
         "2-mashg'ulot va undan KEYINGI o'qituvchilar rejasi kabi boshqa ma'lumotlar shahar zali veb-saytida "
         "e'lon qilingan. Qatnashmoqchi bo'lganlar shahar zali idorasiga to'g'ridan-to'g'ri telefon orqali "
         "murojaat qilsin. Barchangizning ishtirokingizni KUTIB QOLAMIZ."
       ),
       "questions": [
         q("t8-g3-19",None,["からには ／ 結論です","ことから ／ 感想です","からといって ／ 満足です","にもかかわらず ／ 現状です"],4,
           "いそがしくなった[にもかかわらず]…いないのが[現状です] = band bo'lganiga QARAMAY…yo'qligi HOZIRGI AHVOL.",blankNo="19",expl="〜にもかかわらず = ...ga qaramay; 現状です = hozirgi ahvol"),
         q("t8-g3-20",None,["これからの","あれからの","こちらからの","あちらからの"],1,
           "[これからの]女性の生き方 = KELAJAKDAGI ayol hayoti.",blankNo="20",expl="これからの = bundan keyingi, kelajakdagi"),
         q("t8-g3-21",None,["だけであり","だけであれば","だけでなく","だけでなければ"],3,
           "講演を聞く[だけでなく]、質問をしたり… = ma'ruza eshitishnigina EMAS, balki savol ham berib…",blankNo="21",expl="〜だけでなく = faqat ...emas, balki (ham)"),
         q("t8-g3-22",None,["未満の","方面の","以上の","以降の"],4,
           "第2回目[以降の]講師の予定 = 2-mashg'ulot va undan KEYINGI o'qituvchilar rejasi.",blankNo="22",expl="〜以降 = ...dan keyin, ...dan boshlab"),
         q("t8-g3-23",None,["待たれます","お待ちでいらっしゃいます","お待ちいたしております","お待ちくださいます"],3,
           "みなさまのご参加を[お待ちいたしております] = ishtirokingizni KUTIB QOLAMIZ (kamtarlik).",blankNo="23",expl="お待ちいたしております = «kutmoq» ning kamtarlik (謙譲) shakli"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test08.json yozildi. Jami savol:", tot)
