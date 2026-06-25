# -*- coding: utf-8 -*-
"""test10.json — 第10回 模擬テスト (PDF betlari 98-107, javob 203)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test10.json")

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
  "id": 10, "title_jp": "第10回 模擬テスト", "title_uz": "10-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t10-v1-1","ものを【盗んで】はいけません。",["にくんで","かんで","ぬすんで","ふんで"],3,"Narsa o'g'irlamaslik kerak.",reading="ぬすんで",expl="盗む → ぬすむ (o'g'irlamoq)"),
         q("t10-v1-2","彼のけがの【程度】は、まだわからない。",["ていど","でいど","しょうど","じょうど"],1,"Uning jarohati darajasi hali noma'lum.",reading="ていど",expl="程度 → ていど (daraja, miqdor)"),
         q("t10-v1-3","【帰国】する前に先生に会いたいです。",["きくに","きぐに","きこく","きごく"],3,"Vatanga qaytishdan oldin o'qituvchim bilan ko'rishmoqchiman.",reading="きこく",expl="帰国 → きこく (vatanga qaytish)"),
         q("t10-v1-4","彼女は、目を【閉じて】音楽を聞いていた。",["かんじて","とじて","はじて","ふうじて"],2,"U ko'zini yumib musiqa tinglardi.",reading="とじて",expl="閉じる → とじる (yopmoq, yummoq)"),
         q("t10-v1-5","あの人には、あまり【欲】がないようです。",["こころ","こころざし","いよく","よく"],4,"U odamda unchalik nafs (ochko'zlik) yo'qqa o'xshaydi.",reading="よく",expl="欲 → よく (nafs, istak, ochko'zlik)"),
         q("t10-v1-6","田中さんは、私の【親友】です。",["しんゆう","しにゅう","じんゆう","じにゅう"],1,"Tanaka-san mening qadrdon do'stim.",reading="しんゆう",expl="親友 → しんゆう (qadrdon do'st)"),
         q("t10-v1-7","【袋】が破れているので、とりかえてください。",["ぬの","はこ","ひも","ふくろ"],4,"Xalta yirtilgan, almashtiring.",reading="ふくろ",expl="袋 → ふくろ (xalta, qop)"),
         q("t10-v1-8","次の場所へ【移動】しなければなりません。",["うんどう","かつどう","こうどう","いどう"],4,"Keyingi joyga ko'chishimiz (siljishimiz) kerak.",reading="いどう",expl="移動 → いどう (ko'chish, siljish)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t10-v2-9","仕事は、【じゅんちょう】に進んでいる。",["順常","順調","順長","順状"],2,"Ish silliq (yaxshi) ketyapti.",expl="じゅんちょう → 順調 (silliq, muvaffaqiyatli kechayotgan)"),
         q("t10-v2-10","友だちのことばを【しんよう】する。",["信用","信頼","真用","真要"],1,"Do'stimning so'ziga ishonaman.",expl="しんよう → 信用 (ishonch, ishonish)"),
         q("t10-v2-11","一晩中【おどって】、とても楽しかった。",["通って","音って","踊って","舞って"],3,"Tun bo'yi raqsga tushib, juda zavqlandim.",expl="おどる → 踊る (raqsga tushmoq)"),
         q("t10-v2-12","ラッシュアワーを【さけて】、早い時間の電車に乗った。",["逃けて","裂けて","割けて","避けて"],4,"Tirbandlik (rush hour) dan qochib, erta vaqtdagi poyezdga chiqdim.",expl="さける → 避ける (qochmoq, chetlab o'tmoq)"),
         q("t10-v2-13","【へいわ】な生活を送りたい。",["平安","安平","平和","和平"],3,"Tinch hayot kechirmoqchiman.",expl="へいわ → 平和 (tinchlik)"),
         q("t10-v2-14","サッカーの【しあい】に出場した。",["試場","試合","技場","技合"],2,"Futbol o'yiniga (musobaqasiga) chiqdim.",expl="しあい → 試合 (o'yin, musobaqa)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t10-v3-15","この雑誌の（　）は、中年男性だ。",["メーカー","ニーズ","ターゲット","リンク"],3,"Bu jurnalning maqsadli auditoriyasi — o'rta yoshli erkaklar.",expl="ターゲット = nishon, maqsadli auditoriya"),
         q("t10-v3-16","明日の5時に荷物の（　）をお願いします。",["伝達","発達","到達","配達"],4,"Ertaga soat 5 da yukni yetkazib berishni so'rayman.",expl="配達 = yetkazib berish (pochta/yuk)"),
         q("t10-v3-17","車が（　）したので、自転車で会社に行くことにした。",["破壊","故障","悪化","滅亡"],2,"Mashina buzilgani uchun, ishga velosipedda borishga qaror qildim.",expl="故障 = buzilish, nosozlik (texnika)"),
         q("t10-v3-18","時間がたって、コーヒーが（　）しまった。",["凍って","冷めて","わいて","とけて"],2,"Vaqt o'tib, kofe sovib qoldi.",expl="冷める = sovimoq (issiq narsa)"),
         q("t10-v3-19","田中さんは、私とリンさんの（　）の友人だ。",["共同","共感","共通","共有"],3,"Tanaka-san men va Lin-sanning umumiy (mushtarak) do'stimiz.",expl="共通 = umumiy, mushtarak"),
         q("t10-v3-20","難しい問題が（　）、うれしかった。",["解けて","割れて","折れて","破れて"],1,"Qiyin masala yechilib, xursand bo'ldim.",expl="解ける = yechilmoq (masala)"),
         q("t10-v3-21","あと1000円（　）すると、もっとよい部屋に変更できます。",["ダブル","シングル","プラス","チップ"],3,"Yana 1000 yen qo'shsangiz, yaxshiroq xonaga o'zgartira olasiz.",expl="プラスする = qo'shmoq, ustiga qo'shish"),
         q("t10-v3-22","このバイオリンはイタリア（　）です。",["造","産","作","製"],4,"Bu skripka Italiyada ishlangan (Italiya ishi).",expl="〜製 = ...da ishlangan, ...ishi (mamlakat + 製)"),
         q("t10-v3-23","3人の意見が（　）した。",["合同","選択","統一","一致"],4,"Uch kishining fikri bir xil chiqdi (mos keldi).",expl="一致 = mos kelish, bir xil bo'lish"),
         q("t10-v3-24","有名なレストランの料理を食べたが、おいしくなくて（　）した。",["ぴったり","にっこり","めっきり","がっかり"],4,"Mashhur restoran taomini yedim, lekin mazasiz bo'lib, hafsalam pir bo'ldi.",expl="がっかりする = hafsalasi pir bo'lmoq, umidsizlanmoq"),
         q("t10-v3-25","今年の夏は、いつもより（　）すずしかった。",["特殊","特別","一斉","同一"],2,"Bu yilgi yoz odatdagidan ko'ra alohida salqin edi.",expl="特別 = alohida, ayniqsa, juda"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t10-v4-26","【とんでもない】ことが起こった。",["初めての","よくある","普通の","意外な"],4,"Kutilmagan (g'ayrioddiy) voqea yuz berdi.",expl="とんでもない = kutilmagan, aql bovar qilmas → 意外な (kutilmagan)"),
         q("t10-v4-27","部屋を【散らかした】。",["きれいにした","汚くした","明るくした","暗くした"],2,"Xonani to'zitib (kir qilib) tashladim.",expl="散らかす = to'zitmoq, tartibsiz qilmoq → 汚くした"),
         q("t10-v4-28","彼女は、道の途中で【ふり返った】。",["前を見た","後ろを見た","あちらへ行った","こちらへ帰ってきた"],2,"U yo'l o'rtasida ortiga qaradi.",expl="ふり返る = ortiga qaramoq → 後ろを見た"),
         q("t10-v4-29","後輩「おかわりを注文しましょうか。」先輩「今、料理は【間に合っている】よ。」",["時間通りに来る","十分である","完成している","もっと必要である"],2,"Kichik: «Yana buyurtma beraymi?» Katta: «Hozir ovqat yetarli (kifoya).»",expl="間に合っている = yetarli, kifoya → 十分である"),
         q("t10-v4-30","彼女は、とても【慎重な】人です。",["人より静かな","太っている","よく考えてから行動する","何を考えているかわからない"],3,"U juda ehtiyotkor odam.",expl="慎重 = ehtiyotkor, o'ylab ish qiladigan → よく考えてから行動する"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t10-v5-31","ほえる",["家の外で、虫のほえる声が聞こえた。","新入社員が社長に向かって友だちのようにほえていた。","私の家の犬は、夜中によくほえます。","かわいがっていたペットが死んで、悲しくてほえた。"],3,
           "ほえる(吠える) = (it/yirtqich) vovullamoq, akillamoq.",optsTr=["Uy tashqarisida hasharotning 'vovullashi' eshitildi (noto'g'ri — 鳴く kerak).","Yangi xodim rahbarga do'stiday 'vovullardi' (noto'g'ri).","Mening uy itim kechalari tez-tez vovullaydi. (to'g'ri)","Sevimli uy hayvonim o'lib, qayg'udan 'vovulladim' (noto'g'ri — 泣く kerak)."]),
         q("t10-v5-32","あふれる",["お菓子を買いすぎてあふれたので、少しあげます。","コップに水を入れたら、あふれてしまった。","授業が終わったあとも、教室に生徒が1人あふれていた。","道で転んで、足が赤くあふれてしまいました。"],2,
           "あふれる(溢れる) = toshib ketmoq, to'lib oshmoq.",optsTr=["Shirinlik ko'p olib 'toshib ketdi', ozini beraman (noto'g'ri — 余る kerak).","Stakanga suv quysam, toshib ketdi. (to'g'ri)","Dars tugagach ham, sinfda 1 o'quvchi 'toshib' turardi (noto'g'ri — 残る kerak).","Yo'lda yiqilib, oyog'im qizarib 'toshib ketdi' (noto'g'ri — はれる kerak)."]),
         q("t10-v5-33","しばる",["出かけるときは、ちゃんとドアのかぎをしばってください。","シャツのボタンが開いているので、しばったほうがいいですよ。","手紙に切手をしばって、ポストに入れた。","その荷物をロープでかたくしばってください。"],4,
           "しばる(縛る) = bog'lamoq, mahkam bog'lab qo'ymoq.",optsTr=["Chiqayotganda eshik qulfini 'bog'lang' (noto'g'ri — かける kerak).","Ko'ylak tugmasi ochiq, 'bog'lagan' ma'qul (noto'g'ri — とめる kerak).","Xatga markani 'bog'lab', qutiga soldim (noto'g'ri — はる kerak).","U yukni arqon bilan mahkam bog'lang. (to'g'ri)"]),
         q("t10-v5-34","得",["彼女はギターがとても得だ。","商売で大きな得をした。","私はあなたよりテニスが得です。","デパートで得でかばんを買った。"],2,
           "得(とく) = foyda, manfaat, yutuq.",optsTr=["U gitarada juda 'foydali' (noto'g'ri — 得意 kerak).","Savdoda katta foyda ko'rdim. (to'g'ri)","Men sizdan tennis o'yinida 'foydaliman' (noto'g'ri — 得意 kerak).","Univermagda 'foyda bilan' sumka oldim (noto'g'ri — 安く kerak)."]),
         q("t10-v5-35","鋭い",["一日中、鋭い仕事をするのは大変だ。","このかばんは、鋭くてとても便利だ。","このスープは、鋭いので気をつけて食べてください。","彼の批判は、ときどきとても鋭い。"],4,
           "鋭い(するどい) = o'tkir, keskin, teran.",optsTr=["Kun bo'yi 'o'tkir' ish qilish og'ir (noto'g'ri — きつい kerak).","Bu sumka 'o'tkir' va juda qulay (noto'g'ri — 便利 kerak).","Bu sho'rva 'o'tkir', ehtiyot bo'lib yeng (noto'g'ri — 熱い kerak).","Uning tanqidi ba'zan juda o'tkir (teran) bo'ladi. (to'g'ri)"]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t10-g1-1","こんな小さな子ども用の服が、1万円（　）する。",["は","も","と","を"],2,"Bunday kichkina bolalar kiyimi 10 ming yen turadi (shuncha qimmat).",expl="数量+も = ...cha (ko'plik/hayratni ta'kidlash)"),
         q("t10-g1-2","学生「資料を50部コピーしましたが、足りますか。」先生「参加者は40人なので、（　）くらいでいいでしょう。」",["それ","そこ","あれ","あそこ"],1,"Talaba: «Hujjatdan 50 nusxa oldim, yetadimi?» O'qituvchi: «Ishtirokchi 40 kishi, shuncha bo'lsa bo'ldi.»",expl="それくらい = shuncha (yaqindagi narsa/miqdorga ishora)"),
         q("t10-g1-3","地図を（　）浅草を歩く。",["見たところ","見るに応じて","見るかと思うと","見つつ"],4,"Xaritaga qarab-qarab Asakusani aylanaman.",expl="〜つつ = ...gan holda, bir vaqtda (ikki harakat)"),
         q("t10-g1-4","今年はたくさん雪が降り、昨年（　）、かなり寒い。",["とひきかえ","としたら","におうじて","にくらべ"],4,"Bu yil ko'p qor yog'di, o'tgan yilga nisbatan ancha sovuq.",expl="〜にくらべ = ...ga nisbatan, taqqoslaganda"),
         q("t10-g1-5","中田くんは、スポーツ選手（　）、走るのがとても速い。",["まであって","だけあって","ほどあって","しかあって"],2,"Nakata sportchi bo'lgani uchun ham, juda tez yuguradi.",expl="〜だけあって = ...ga yarasha, ...bo'lgani uchun (kutilgandek)"),
         q("t10-g1-6","学校のある駅から銀座までは、2回（　）といけない。",["乗り換え","乗り換えた","乗り換えない","乗り換える"],3,"Maktab bekatidan Ginzagacha 2 marta poyezd almashtirmasa bo'lmaydi.",expl="〜ないといけない = ...masa bo'lmaydi. 乗り換えないと"),
         q("t10-g1-7","男女を（　）だれでも参加できます。",["問えば","問わず","問うと","問えず"],2,"Erkak-ayolligidan qat'i nazar, hamma qatnasha oladi.",expl="〜を問わず = ...ga qaramay, ...dan qat'i nazar"),
         q("t10-g1-8","石川君が大切な書類をなくしたらしい。無責任な彼が（　）ことだ。",["やらなそうな","やりそうな","やらないような","やったような"],2,"Ishikava muhim hujjatni yo'qotibdi. Mas'uliyatsiz uning qiladigan ishi-da.",expl="〜そうな = ...adigandek, ...ishi mumkin (taxmin). やりそうな = qiladigandek"),
         q("t10-g1-9","もし川島さんの電話番号を（　）、教えてください。",["知りましたら","知られましたら","存じましたら","ご存じでしたら"],4,"Agar Kavashima-sanning telefon raqamini bilsangiz, ayting.",expl="ご存じ = 知っている ning hurmat shakli (bilsangiz)"),
         q("t10-g1-10","今日の朝は、とてもいそがしかったので、（　）会社へ行った。",["何を食べても","何も食べずに","何も食べないと","何を食べるまでもなく"],2,"Bugun ertalab juda band edim, shuning uchun hech narsa yemay ishga ketdim.",expl="〜ずに = ...masdan. 食べずに = yemasdan"),
         q("t10-g1-11","あそこに立っている男の人は、これから何を（　）いるのですか。",["しようとして","しろといって","するとして","したといって"],1,"Anavi turgan erkak hozir nima qilmoqchi bo'lyapti?",expl="〜(よ)うとしている = ...moqchi bo'lyapti (harakat oldidagi holat)"),
         q("t10-g1-12","三井「あなたはドイツ語がお上手だそうですね。」山中「いいえ、（　）が、まだまだです。」",["話さないことはできます","話さないことはできません","話せないことはあります","話せないことはありません"],4,"Mitsui: «Siz nemis tilini yaxshi bilarkansiz.» Yamanaka: «Yo'q, gapira olmasligim emas-u (ozroq gapiraman), lekin hali yo'l bor.»",expl="〜ないことはない = ...sa qila olaman (yumshoq tasdiq). 話せないことはない = gapira olmasligim emas"),
         q("t10-g1-13","先週借りたお金は、もうほとんど（　）。",["使うところでした","使わないことでした","使ってしまいました","使ってしまいませんでした"],3,"O'tgan hafta qarz olgan pulni endi deyarli sarflab bo'ldim.",expl="〜てしまう = ...ib bo'lmoq (tugatish/tugallanish). 使ってしまいました"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t10-g2-14",None,["電車が","ものですから","遅れた","事故で"],3,"To'g'ri jumla: «Kechirasiz. Avariya tufayli poyezd kechikkani sababli, kechikib qoldim.»",
           prefix="内田「もうしわけありません。",suffix="、遅くなりました。」",starPos=3,order=[4,1,3,2],expl="To'g'ri tartib: 事故で電車が遅れたものですから (〜ものですから = ...gani sababli)"),
         q("t10-g2-15",None,["遊びに","いい","行きたい","から"],1,"To'g'ri jumla: «Bugun yozги ta'tilning birinchi kuni, havo ham yaxshi, qayerga bo'lsa ham sayrga borgim kelyapti.»",
           prefix="今日は夏休みの初日だし、天気もいいし、どこでも",suffix="なあ。",starPos=3,order=[2,4,1,3],expl="To'g'ri tartib: いいから遊びに行きたい"),
         q("t10-g2-16",None,["思い出す","多い","人も","のでは"],2,"To'g'ri jumla: «Yaponiyaning mashhur tog'i deyilsa, Fuji tog'ini eslaydigan odam ham ko'p emasmi.»",
           prefix="日本の有名な山と言われれば、富士山を",suffix="ないか。",starPos=3,order=[1,3,2,4],expl="To'g'ri tartib: 思い出す人も多いのでは (〜のではないか = ...emasmi)"),
         q("t10-g2-17",None,["要求に","形で","強い","こたえる"],4,"To'g'ri jumla: «Ilgaridan beri xodimlarning kuchli talabiga javob bergan tarzda, rahbar maoshni oshirdi.»",
           prefix="以前からの、社員の",suffix="社長は給料を上げた。",starPos=3,order=[3,1,4,2],expl="To'g'ri tartib: 強い要求にこたえる形で (〜にこたえる = ...ga javob bermoq)"),
         q("t10-g2-18",None,["わたる","数か月に","して","船の旅を"],4,"To'g'ri jumla: «Ilgari samolyot bo'lmagani uchun, bir necha oyga cho'zilgan kema sayohatini qilib chet elga borardik.»",
           prefix="昔は、飛行機がなかったので、",suffix="海外へ行きました。",starPos=3,order=[2,1,4,3],expl="To'g'ri tartib: 数か月にわたる船の旅をして (〜にわたる = ...davomida cho'zilgan)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "食べ物とコミュニケーション",
       "passage": (
         "「男性の心をつかむには、まず胃袋から」という言葉を聞いたことがありますか。"
         "恋愛について相談をしているときに、だれかから聞いたことがあるかもしれません。"
         "男性は、{{19}}を作ってくれる女性を好きになることが多い、つまり、食事は男性にとっては"
         "重要だということです。\n"
         "{{20}}、この言葉は、恋愛や男性だけにあてはまるわけではありません。"
         "人と人とのコミュニケーションにおいて、食べ物は非常に重要な役割をはたすからです。\n"
         "たとえば、ある人と親しくなりたいと思った場合、「一緒に近くを歩きませんか」と言うよりも、"
         "「一緒においしいケーキを食べに行きませんか」と言うほうが、ずっと仲よくなれそうな気が"
         "しませんか。\n"
         "実際に、一緒にものを食べたり飲んだりした人と、前よりずっと仲よくなった、という思い出が{{21}}。\n"
         "食事が重要な役割をはたすのは、友だちや彼氏、彼女を作る場合だけに{{22}}。"
         "仕事の話をする場合でも、一緒に食事をすることは大きな意味を持ちます。"
         "落ちついて話ができる、サービスも味もよいお店を知っていることが、"
         "仕事の話をうまく進めるための手段に{{23}}。"
       ),
       "passage_tr": (
         "«Erkakning ko'nglini olish uchun, avvalo oshqozonidan» degan iborani eshitganmisiz? Sevgi haqida "
         "maslahatlashayotganda, kimdandir eshitgan bo'lishingiz mumkin. Erkaklar MAZALI TAOM pishirib "
         "beradigan ayolni yoqtirib qolishi ko'p uchraydi — ya'ni, ovqat erkak uchun muhim degani. "
         "SHUNDAY BO'LSA-DA, bu ibora faqat sevgi yoki erkaklarga taalluqli emas. Chunki inson bilan inson "
         "muloqotida ovqat juda muhim rol o'ynaydi. "
         "Masalan, kimdir bilan yaqinlashmoqchi bo'lsangiz, «birga yaqin-atrofda yuramizmi» deyishdan ko'ra "
         "«birga mazali tort yegani boramizmi» deganingiz ancha yaqinlashtiradigandek tuyulmaydimi? "
         "Haqiqatan, birga biror narsa yeb-ichgan odam bilan oldingidan ancha yaqinlashgan degan xotirangiz "
         "BORDIR deb o'ylayman. "
         "Ovqat muhim rol o'ynashi faqat do'st, yigit yoki qiz orttirish holatigagina TAALLUQLI EMAS. Ish "
         "haqida gaplashganda ham birga ovqatlanish katta ma'no kasb etadi. Bemalol gaplasha oladigan, "
         "xizmati ham, mazasi ham yaxshi joyni bilish — ish muzokarasini muvaffaqiyatli olib borish "
         "vositasiga AYLANISHI HAM MUMKIN."
       ),
       "questions": [
         q("t10-g3-19",None,["まあまあの料理","おいしい料理","いつもの料理","すべての料理"],2,
           "男性は[おいしい料理]を作ってくれる女性 = erkak MAZALI TAOM pishirib beradigan ayolni yoqtiradi.",blankNo="19",expl="おいしい料理 = mazali taom (kontekstga mos)"),
         q("t10-g3-20",None,["そのため","それだけ","そうはいっても","なぜなら"],3,
           "[そうはいっても]、恋愛や男性だけにあてはまるわけではない = SHUNDAY BO'LSA-DA, faqat sevgi/erkakka taalluqli emas.",blankNo="20",expl="そうはいっても = shunday bo'lsa-da, shunga qaramay"),
         q("t10-g3-21",None,["するかと思います","なるかと思います","いることと思います","あることと思います"],4,
           "思い出が[あることと思います] = bunday xotirangiz BORDIR deb o'ylayman.",blankNo="21",expl="〜ことと思います = ...dir deb o'ylayman (muloyim taxmin)"),
         q("t10-g3-22",None,["限りました","限るようです","限ります","限りません"],4,
           "作る場合だけに[限りません] = ...holatigagina TAALLUQLI EMAS (faqat shuning bilan cheklanmaydi).",blankNo="22",expl="〜に限りません = faqat ...bilan cheklanmaydi"),
         q("t10-g3-23",None,["なることさえあるのです","することはあるのです","なるしかないのです","するしかないのです"],1,
           "手段に[なることさえあるのです] = vositaga AYLANISHI HAM MUMKIN (hatto).",blankNo="23",expl="〜さえある = hatto ...ham bo'ladi"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test10.json yozildi. Jami savol:", tot)
