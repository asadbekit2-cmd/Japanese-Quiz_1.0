# -*- coding: utf-8 -*-
"""test15.json — 第15回 模擬テスト."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test15.json")

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
  "id": 15, "title_jp": "第15回 模擬テスト", "title_uz": "15-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t15-v1-1","大事なことなので、【文書】で回答してください。",["もんしょう","もんしょ","ぶんしょう","ぶんしょ"],4,"Muhim masala bo'lgani uchun yozma ravishda javob bering.",reading="ぶんしょ",expl="文書 → ぶんしょ (hujjat, yozma material)"),
         q("t15-v1-2","毎日練習をしたので、【実力】がついた。",["しつりょく","じつりょく","しつりき","じつりき"],2,"Har kuni mashq qilganimdan keyin haqiqiy kuch (mahorat) paydo bo'ldi.",reading="じつりょく",expl="実力 → じつりょく (haqiqiy qobiliyat, mahorat)"),
         q("t15-v1-3","冷蔵庫で氷が【固まる】。",["つまる","あまる","あつまる","かたまる"],4,"Muzlatgichda muz qotadi (qattiq bo'ladi).",reading="かたまる",expl="固まる → かたまる (qotmoq, qattiqlashmoq)"),
         q("t15-v1-4","風に木の葉が【舞って】いました。",["おどって","ちって","まって","さって"],3,"Shamolda daraxt barglari g'ir aylanar edi.",reading="まって",expl="舞う → まう (aylanib uchmoq, g'ir aylanmoq)"),
         q("t15-v1-5","食べ続けても、体に【害】はありません。",["かい","がい","とく","どく"],2,"Yeya bersangiz ham tanaga zarari yo'q.",reading="がい",expl="害 → がい (zarar, ziyon)"),
         q("t15-v1-6","新しいルールは、わが社にとって【有利】だ。",["ふり","ふうり","ゆり","ゆうり"],4,"Yangi qoida bizning kompaniya uchun qulay (foydali).",reading="ゆうり",expl="有利 → ゆうり (afzallik, qulay holat)"),
         q("t15-v1-7","この町には、有名な【港】があります。",["きし","みなと","うみ","はま"],2,"Bu shaharda mashhur port bor.",reading="みなと",expl="港 → みなと (port, qayiqxona)"),
         q("t15-v1-8","2人の意見が【対立】している。",["たいりつ","だいりつ","たいりゅう","だいりゅう"],1,"2 kishining fikri qarama-qarshi turibdi.",reading="たいりつ",expl="対立 → たいりつ (qarama-qarshilik, ziddiyat)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t15-v2-9","【みごと】なポーズで着地した。",["美事","味事","夢事","見事"],4,"Go'zal poza bilan yerga tushdi.",expl="みごと → 見事 (ajoyib, chiroyli, muvaffaqiyatli)"),
         q("t15-v2-10","【きょうどう】で、新しい仕事をはじめた。",["強同","強道","共同","共道"],3,"Hamkorlikda yangi ish boshladik.",expl="きょうどう → 共同 (hamkorlik, birgalikda)"),
         q("t15-v2-11","初めて会った人に【めいし】をもらった。",["名氏","名札","名刺","名紙"],3,"Birinchi marta uchrashgan odamdan vizit kartochka oldim.",expl="めいし → 名刺 (vizit kartochka)"),
         q("t15-v2-12","あなたの行いは、だれかを【すくう】ことができるかもしれない。",["補う","助う","求う","救う"],4,"Sizning harakatingiz biror kishini qutqarishi mumkin.",expl="すくう → 救う (qutqarmoq, najot bermoq)"),
         q("t15-v2-13","クリスマスの【ていばん】の商品は、このケーキだ。",["丁番","定番","丁版","定版"],2,"Rojdestvo uchun eng an'anaviy mahsulot — bu tort.",expl="ていばん → 定番 (an'anaviy, klassik, standarт mahsulot)"),
         q("t15-v2-14","夜中に家の外で【あしおと】が聞こえた。",["足声","足後","足音","足元"],3,"Yarim tunda uydan tashqarida oyoq tovushi eshitildi.",expl="あしおと → 足音 (oyoq tovushi, qadam tovushi)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t15-v3-15","毎月たくさん雑誌を買うので、部屋に置く（　）がない。",["ウェイト","アウトドア","インテリア","スペース"],4,"Har oy juda ko'p jurnal sotib olganimdan xonada qo'yadigan joy yo'q.",expl="スペース = joy, bo'sh joy (space)"),
         q("t15-v3-16","私が動物を好きになったのは、両親の（　）だ。",["反響","伝統","影響","代表"],3,"Men hayvonlarni yaxshi ko'rib qolganim ota-onamning ta'siri.",expl="影響 = ta'sir (influence)"),
         q("t15-v3-17","旅行者がけんかをしたことがA国とB国の（　）問題になった。",["海外","国外","交通","外交"],4,"Sayyohlarning janjali A va B mamlakatlar o'rtasida diplomatik muammoga aylandi.",expl="外交 = diplomatiya, tashqi siyosat"),
         q("t15-v3-18","外出するので、アクセサリーを（　）。",["はいた","かぶった","つけた","せおった"],3,"Tashqariga chiqayotganim uchun aksessuarlarni taqdim (kiydim).",expl="つける = taqmoq, kiymoq (aksessuar, bezak)"),
         q("t15-v3-19","この生き物は、魚の（　）だ。",["一派","一種","一期","一流"],2,"Bu jonzot baliqning bir turi.",expl="一種 = bir tur, bir xil (kind/species)"),
         q("t15-v3-20","一か月の生活（　）はどのくらいですか。",["金","価","費","値"],3,"Bir oylik hayot xarajati qancha?",expl="費 = xarajat, sarf (生活費 = tirikchilik xarajati)"),
         q("t15-v3-21","彼女を（　）して、この曲を作りました。",["イコール","アレンジ","イメージ","スケッチ"],3,"Uni tasavvur qilib (xayolimga keltirb) bu qo'shiqni yaratdim.",expl="イメージする = tasavvur qilmoq, ko'z o'ngida keltirmoq"),
         q("t15-v3-22","彼は動物学者なので、動物に（　）。",["くわしい","まぶしい","くやしい","たのもしい"],1,"U zoolog bo'lgani uchun hayvonlarga oid narsalarni yaxshi biladi.",expl="くわしい = yaxshi biladigan, teran biladigan (詳しい)"),
         q("t15-v3-23","今日は休むと、中田さんに（　）してください。",["提案","伝言","要求","指摘"],2,"Bugun ishga kelmaydi deb Nakata janobga xabar qilib qo'ying.",expl="伝言 = xabar berish, so'z qoldirish"),
         q("t15-v3-24","休みには温泉に行って、何もしないで旅館で（　）したい。",["そろそろ","せっせと","ぐるぐる","のんびり"],4,"Dam olish kunlari issiq buloqqa borib, mexmonxonada hech narsa qilmasdan dam olmoqchiman.",expl="のんびり = tashasusiz, xotirjam, dam olib (relaxed)"),
         q("t15-v3-25","エジプトのピラミッドは、とても（　）だ。",["多大","最大","巨大","盛大"],3,"Misr ehromlari juda ulkan (buyuk).",expl="巨大 = ulkan, juda katta (gigantic)"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t15-v4-26","【マニュアル】を見ながら作業をする。",["地図","手帳","時刻表","説明書"],4,"Qo'llanmani ko'rib ish qilaman.",expl="マニュアル = qo'llanma, yo'riqnoma → 説明書"),
         q("t15-v4-27","そこに【じっと】してください。",["動いて","動かないで","見て","見ないで"],2,"U yerda jim (harakat qilmay) turing.",expl="じっとする = qimirlamasdan turmoq → 動かないで"),
         q("t15-v4-28","田中さんはとても【顔が広い】。",["頭が大きい","心がやさしい","知り合いが多い","親せきが多い"],3,"Tanaka janobing tanish-bilishi ko'p.",expl="顔が広い = tanish-bilishi ko'p, nufuzli → 知り合いが多い"),
         q("t15-v4-29","【あわてて】出かける準備をした。",["時間をかけて","簡単に","急いで","ゆっくり"],3,"Shoshib-poshib chiqishga tayyorlandim.",expl="あわてる = shoshmoq, to'lg'onmoq → 急いで"),
         q("t15-v4-30","妻「料理の味はどうかな。」夫「【割合】おいしいよ。」",["思っていたよりも","すばらしく","今まででいちばん","少しは"],1,"Xotin: «Taomning ta'mi qalaymikin?» Er: «O'ylagan darajadan ham mazali.»",expl="割合 = nisbatan, o'ylagandan → 思っていたよりも"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t15-v5-31","たまたま",["お正月は、ずっと家族とたまたま一緒にいた。","彼にたまたま会うのは、5年ぶりです。","散歩をしていたら、ファンさんとたまたま会った。","きちんと計画をたてて、たまたま旅行に行った。"],3,
           "たまたま = tasodifan, kutilmagan holda.",optsTr=["Yangi yilda doim oila bilan 'tasodifan' birga bo'ldim (noto'g'ri — ずっと kerak).","U bilan 'tasodifan' uchrashish 5 yildan beri (noto'g'ri — ばったり kerak).","Sayr qilayotganda Fan janob bilan tasodifan uchrab qoldim. (to'g'ri)","Rejalashtirgan holda 'tasodifan' sayhonga chiqdim (noto'g'ri — zid)."]),
         q("t15-v5-32","補う",["やぶれたシャツを糸で補ってください。","サッカーの試合中けがをした足を、すぐに補った。","夫婦げんかをした後は、早く補ったほうがいい。","私の足りない部分を、中山さんが補ってくれた。"],4,
           "補う(おぎなう) = to'ldirmoq, qoplab bermoq.",optsTr=["Yirtilgan ko'ylakni ip bilan 'to'ldiring' (noto'g'ri — 縫う kerak).","Futbol paytida jarohatlangan oyoqni 'to'ldirdi' (noto'g'ri — 治療した kerak).","Er-xotin janjalidan keyin tez 'to'ldirgan' maqul (noto'g'ri — 仲直りした kerak).","Kamchiligimni Nakayama janob to'ldirib berdi. (to'g'ri)"]),
         q("t15-v5-33","たば",["明日、机のたばを捨ててください。","駅前に10人くらいの人のたばが立っています。","この地方には、めずらしい動物のたばが住んでいます。","台の上に紙のたばが置いてあります。"],4,
           "たば(束) = to'plam, boglam, tutam.",optsTr=["Ertaga stol 'boglamini' tashlab bering (noto'g'ri — 引き出し kerak).","Bekat oldida 10 kishilik odamlar 'boglamı' turibdi (noto'g'ri — 群れ kerak).","Bu hududda noyob hayvonlar 'boglamı' yashaydi (noto'g'ri — 群れ kerak).","Stol ustida qog'oz boglamı qo'yilgan. (to'g'ri)"]),
         q("t15-v5-34","都合",["今日は、都合がなくて一緒に遊びに行けません。","明日、都合がよければ、うちに食事に来てください。","これから1週間、外国へ旅行に行く都合です。","悪い都合で会議に出られず、すみませんでした。"],2,
           "都合(つごう) = qulay holat, sharoit, ahvol.",optsTr=["Bugun 'qulay holat' yo'q, birga o'ynagani bormayman (noto'g'ri — 用事 kerak).","Ertaga qulay bo'lsa, biznikiga ovqatga keling. (to'g'ri)","Keyingi 1 hafta chet elga safarim bor 'qulay holat' (noto'g'ri — 予定 kerak).","Yomon 'qulay holat'dan yig'ilishga chiqa olmadim, kechirasiz (noto'g'ri — 事情 kerak)."]),
         q("t15-v5-35","きつい",["容器のふたをきつく閉めてください。","林さんは、ほかのどの社員よりも能力がきつい。","どんなにきつく考えても、新しいアイデアが出てこなかった。","田中さんなら体がきついので、あの山に登れるでしょう。"],1,
           "きつい = mahkam, qattiq; og'ir, qiyin; tor.",optsTr=["Idishning qopqog'ini mahkam yoping. (to'g'ri)","Hayashi janob boshqa xodimlardan 'qattiqroq' (noto'g'ri — 優れている kerak).","Qanchalik 'qattiq' o'ylasam ham yangi g'oya kelmadi (noto'g'ri — 一生懸命 kerak).","Tanaka janob tana 'qattiq' bo'lgani uchun o'sha tog'ga chiqoladi (noto'g'ri — 丈夫 kerak)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t15-g1-1","彼女と連絡が取れなくなってから、今日（　）5日になります。",["は","で","に","が"],2,"U bilan aloqa yo'qolganidan bugun 5 kun bo'ldi.",expl="今日で〜日になる = bugun ...kunga to'ldi (で = o'tish muddatini ko'rsatish)"),
         q("t15-g1-2","お金（　）あれば、今よりもっといい生活ができるのに。",["まで","しか","さえ","ほど"],3,"Pul bo'lsa, hozirdan yaxshiroq hayot kechirgan bo'lardim.",expl="〜さえあれば = faqat ...bo'lsa (yetarlilik sharti). お金さえあれば = faqat pul bo'lsa kifoya."),
         q("t15-g1-3","一度約束した（　）、絶対に守ってください。",["からでは","からには","からいって","からといって"],2,"Bir marta va'da bergan ekanmiz, albatta bajarish kerak.",expl="〜からには = ...ekan, ...dan keyin (mas'uliyat, zaruriyat). 約束したからには = va'da bergan ekanmiz."),
         q("t15-g1-4","今井「今日のセミナー、なんだか出席者が少ないね。」山本「電車の事故（　）、みんなが来るのが遅れているらしいよ。」",["ので","のわけで","のに","のせいで"],4,"Imai: «Bugungi seminar, qatnashchilar kamligi bor.» Yamamoto: «Poyezd avariyas sababli hammasining kechikayotgani.»",expl="〜のせいで = ...sababidan (salbiy natija). 事故のせいで = avariya sababli."),
         q("t15-g1-5","先週は、3日間（　）大雪が降りました。",["にまで","にかけて","にこそ","にわたって"],4,"O'tgan hafta 3 kun davomida katta qor yog'di.",expl="〜にわたって = ...davomida, ...bo'yi (muddatni ko'rsatish). 3日間にわたって = 3 kun mobaynida."),
         q("t15-g1-6","2年前の旅行を（　）、彼女と親しくなった。",["最中に","限りに","きっかけに","ついでに"],3,"2 yil oldingi sayohatni bahona qilib u qiz bilan yaqinlashdim.",expl="〜をきっかけに = ...ni bahona (sabab) qilib. 旅行をきっかけに = sayohatdan keyin."),
         q("t15-g1-7","なんでこんなに手がよごれているんだ。すぐに（　）しろ。",["きれいに","きれいな","きれい","きれいで"],1,"Nima uchun qo'ling shunchalik ifloslangan? Darhol tozala.",expl="きれいに + する = toza holga keltirmoq (副詞的に使う)"),
         q("t15-g1-8","テストの答えを聞かれても、（　）わけがありません。",["教えない","教えられる","教えて","教えた"],2,"Test javoblarini so'rasalar ham ayta olmayman (aytishim mumkin emas).",expl="教えられるわけがない = aytishim aslo mumkin emas (できるわけがない = imkoni yo'q)"),
         q("t15-g1-9","私が旅行で買ってきたおみやげを、社長に（　）。",["しました","くださいました","やりました","さしあげました"],4,"Safardan sotib kelgan sovg'amni direktorga taqdim etdim.",expl="さしあげる = bermoqning kamtarlik shakli (目上の人に物をあげる). やる < あげる < さしあげる."),
         q("t15-g1-10","父「どうして泣いてるんだ?」娘「だって、お母さんが（　）。」",["いないんだっけ","いないんだもん","いなかったっけ","いないんだそう"],2,"Ota: «Nima uchun yig'layapsan?» Qiz: «Chunki onam yo'q-da.»",expl="〜んだもん = ...da-ku (o'zi oqlash, bolalar tili). いないんだもん = yo'q-da, bo'lmasa nima qilay."),
         q("t15-g1-11","子どものころは、この川でよく（　）。",["泳いだものです","泳ぎたいものです","泳いだやらです","泳ぎたいやらです"],1,"Bolaligimda bu daryoda ko'p suzardim.",expl="〜たものだ = ilgari shunday qilardim (nostalgiya, o'tmiш odati). 泳いだものだ = suzar edim."),
         q("t15-g1-12","おかげさまで、とても楽しくこの仕事を（　）。またよろしくお願い申し上げます。",["していただきました","されていただきました","なさっていただきました","させていただきました"],4,"Siz tufayli bu ishni juda zavq bilan bajarish imkoniga ega bo'ldim. Yana yordam so'rayman.",expl="させていただく = ruxsat so'rab bajarish, kamtarlik (〜させていただきました = qilishga ruxsat berdingiz)."),
         q("t15-g1-13","情報は、新聞が伝えているから正しい（　）、自分で正しいかどうか考えることが大切だ。",["としたことでなく","としたことで","というものではなく","というもので"],3,"Axborot gazetada yozilgan uchun to'g'ri deyish mumkin emas — o'zing ham to'g'ri yoki yo'qligini o'yla.",expl="〜というものではない = ...deb bo'lmaydi, ...degani emas (kategorik inkor)"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t15-g2-14",None,["あげく","どちらに","なやんだ","行くか"],3,"To'g'ri jumla: «Ta'tilda dengizgami, tog'gami borishni uzoq o'ylab, oxirida hammamiz dengizga cho'mish borishga qaror qildik.»",
           prefix="連休に、海か山か",suffix="、みんなで海水浴に行った。",starPos=3,order=[2,4,3,1],expl="どちらに行くか なやんだ あげく (〜あげく = uzoq o'ylanganidan keyin, oxir-oqibatda)"),
         q("t15-g2-15",None,["後で","が","お休みになった","その"],4,"To'g'ri jumla: «Kecha kechqurun o'qituvchi dam olib bo'lgandan keyin hammamiz spirtli ichimlik ichdik.»",
           prefix="きのうの夜、先生",suffix="みんなでお酒を飲みました。",starPos=3,order=[2,3,4,1],expl="先生がお休みになったその後で (お休みになる = «dam olmoq» hurmat shakli; その後で = undan keyin)"),
         q("t15-g2-16",None,["けんかでも","ものなら","しよう","友だちと"],3,"To'g'ri jumla: «Bolaligimda do'stim bilan janjallashay deb tursamgina, onam qattiq urar edi.»",
           prefix="子どものころ、",suffix="、母にひどくしかられました。",starPos=3,order=[4,1,3,2],expl="友だちとけんかでもしようものなら (〜ようものなら = ...qilmoqchi bo'lsang, darhol yomon narsa bo'ladi)"),
         q("t15-g2-17",None,["わりに","小さい","体が","ほうだ"],2,"To'g'ri jumla: «U kishi sportchi bo'lishiga qaramay, tanasi nisbatan kichik deb o'ylayman.»",
           prefix="あの人は、スポーツ選手の",suffix="と思います。",starPos=3,order=[3,1,2,4],expl="体がわりに小さいほうだ (〜わりに = ...ga nisbatan, kutilgandan farqli holda)"),
         q("t15-g2-18",None,["ともかく","なら","そんな","今は"],1,"To'g'ri jumla: «Ilgari bo'lsa mayli, bunday davrda endi bu odat yo'q.»",
           prefix="昔",suffix="習慣はありません。",starPos=2,order=[2,1,3,4],expl="昔ならともかく、そんな今は習慣はありません (ならともかく = ilgari bo'lsa mayli, lekin hozir...)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "美術館めぐりのすすめ",
       "passage": (
         "この秋、A市の中心エリアでは、美術館めぐりのイベントを行っています。芸術に力を入れているA市には、"
         "3つのとても有名な美術館があります。このイベントは、県立美術館、市立美術館、山田太郎記念美術館の"
         "3つをまわり、それぞれの美術館に入場するときに、用紙にスタンプをもらうというものです。"
         "期間中はどの美術館でも入場料は、{{19}} 500円です。3つの美術館は、駅から電車やバスを使えば"
         "10分以内で行ける便利な場所にあります。2館以上スタンプを{{20a}}、絵はがきやポスター、"
         "シールなどの景品の中から好きなものを1つ{{20b}}\n"
         "イベントの期間中、すべての美術館で、特別展覧会も開かれています。{{21}}展覧会もおすすめです。"
         "特に、山田太郎美術館では、いつもは公開されていない、日本の美術の歴史の中でも「名作」とされている"
         "山田太郎氏の絵画3枚を公開します。その他の美術館でも、{{22}}知っている有名な絵画がいくつも"
         "展示される予定です。\n"
         "美術や絵画にあまり関心のない方も、このような機会に美術館めぐりをしながら「芸術の秋」をゆっくりと"
         "味わってみては{{23}}"
       ),
       "passage_tr": (
         "Bu kuz, A shahrining markaziy hududida san'at muzeylari aylanish tadbirini o'tkazmoqda. San'atga "
         "alohida e'tibor beradigan A shahrida 3 ta juda mashhur muzey bor. Bu tadbir viloyat san'at muzeyi, "
         "shahar san'at muzeyi va Yamada Taro yodgorlik muzeyini aylanib, har biriga kirishda varaqqa muhur "
         "olish tarzida o'tadi. Tadbir davomida har qanday muzeyga kirish narxi YOSHDAN QATI NAZAR 500 yen. "
         "3 ta muzey ham bekatdan poyezd yoki avtobus bilan 10 daqiqada yetib boradigan qulay joyda. "
         "2 va undan ko'p muzeylarda muhur TO'PLASANGIZ, rasmli kartochka, poster, stiker kabi sovg'alar "
         "orasidan 1 ta OLASIZ.\n"
         "Tadbir davomida barcha muzeylarda maxsus ko'rgazma ham ochiladi. BU ko'rgazma ham tavsiya etiladi. "
         "Xususan, Yamada Taro muzeyida odatda namoyish etilmaydigan, yapon san'ati tarixida «durdonа» "
         "sanaluvchi Yamada Taro-ning 3 ta rasmini ko'rgazmaga qo'yadi. Boshqa muzeylarda ham HAMMA "
         "bilgan mashhur rasmlar ko'rgazmaga qo'yilishi rejalashtirilgan.\n"
         "San'at va rasmlarga ko'p qiziqmaydigan kimsalar ham bunday imkoniyatda muzeylarni aylanib «kuz "
         "san'ati»ni xotirjam tatib ko'rsalar QANDAY BO'LARKIN?"
       ),
       "questions": [
         q("t15-g3-19",None,["年齢にもかかわらず","年齢にかかわらず","年齢にもかぎらず","年齢にかぎらず"],2,
           "入場料は[年齢にかかわらず]500円 = kirish narxi YOSHDAN QATI NAZAR 500 yen.",blankNo="19",expl="年齢にかかわらず = yoshdan qat'i nazar (〜にかかわらず = ...dan qat'i nazar, ...ga qaramasdan)"),
         q("t15-g3-20",None,["集めると ／ もらえるようです","集めると ／ もらえます","集めるとき ／ もらいます","集めるとき ／ もらうことができます"],2,
           "2館以上スタンプを[集めると]…景品の中から1つ[もらえます] = to'plasangiz…sovg'a olasiz.",blankNo="20",expl="集めると (shartli: to'plasangiz) + もらえます (olasiz — aniq va'da)"),
         q("t15-g3-21",None,["あの","ああ","この","こう"],3,
           "すべての美術館で特別展覧会も開かれています。[この]展覧会もおすすめです = ...maxsus ko'rgazma ham bor. BU ko'rgazma ham tavsiya etiladi.",blankNo="21",expl="この = bu (yaqin kontekstga ishora — avval aytilgan ko'rgazmaga ishora)"),
         q("t15-g3-22",None,["だれかが","だれかは","だれにも","だれでも"],4,
           "その他の美術館でも、[だれでも]知っている有名な絵画が… = boshqa muzeylarda ham HAMMA bilgan mashhur rasmlar.",blankNo="22",expl="だれでも = hamma, istalgan kishi (umumiy qamrov). だれかが ≠ hamma."),
         q("t15-g3-23",None,["よかったでしょうか","よろしいでしょうか","どうだったでしょうか","いかがでしょうか"],4,
           "「芸術の秋」をゆっくりと味わってみては[いかがでしょうか] = «kuz san'ati»ni tatib ko'rsalar QANDAY BO'LARKIN?",blankNo="23",expl="いかがでしょうか = qanday bo'lar ekan? (taklif/tavsiya qilishda yumshoq ifodalash). よろしいでしょうか bilan farqi: いかが = taklif, よろしい = ruxsat so'rash."),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test15.json yozildi. Jami savol:", tot)
