# -*- coding: utf-8 -*-
"""test04.json — 第4回 模擬テスト (PDF betlari 38-47, javob 197)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test04.json")

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
  "id": 4, "title_jp": "第4回 模擬テスト", "title_uz": "4-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t4-v1-1","荷物は、もう【届いて】います。",["あいて","ほどいて","ついて","とどいて"],4,"Yuk allaqachon yetib keldi.",reading="とどいて",expl="届く → とどく (yetib bormoq, kelmoq)"),
         q("t4-v1-2","【適度】な運動は、体によい。",["てきと","てきとう","てきど","てきどう"],3,"Me'yoridagi sport tanaga foydali.",reading="てきど",expl="適度 → てきど (me'yor, mo'tadillik)"),
         q("t4-v1-3","部長は今、大阪へ【出張】しています。",["しゅちょう","しゅっちょう","でちょう","でっちょう"],2,"Bo'lim boshlig'i hozir Osakaga xizmat safarida.",reading="しゅっちょう",expl="出張 → しゅっちょう (xizmat safari)"),
         q("t4-v1-4","両親が子どもたちを【養う】。",["さそう","やしなう","ととのう","うたがう"],2,"Ota-ona bolalarini boqadi (ta'minlaydi).",reading="やしなう",expl="養う → やしなう (boqmoq, ta'minlamoq)"),
         q("t4-v1-5","【勇気】がなくて、好きな人に話しかけられない。",["よき","ようき","ゆき","ゆうき"],4,"Jasoratim yo'q, yoqtirgan odamim bilan gaplasha olmayman.",reading="ゆうき",expl="勇気 → ゆうき (jasorat)"),
         q("t4-v1-6","空港で日本円をユーロに【両替】した。",["りょかえ","りょがえ","りょうかえ","りょうがえ"],4,"Aeroportda yenni yevroga almashtirdim.",reading="りょうがえ",expl="両替 → りょうがえ (pul almashtirish)"),
         q("t4-v1-7","遠くに白い【煙】が見えます。",["くも","きり","けむり","はい"],3,"Uzoqda oq tutun ko'rinadi.",reading="けむり",expl="煙 → けむり (tutun)"),
         q("t4-v1-8","家の前で車が【停止】した。",["ていし","てんし","ていじ","てんじ"],1,"Uy oldida mashina to'xtadi.",reading="ていし",expl="停止 → ていし (to'xtash)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t4-v2-9","【ぜんりょく】で課題に取り組む。",["戦力","全力","前力","総力"],2,"Bor kuchim bilan vazifaga kirishaman.",expl="ぜんりょく → 全力 (bor kuch)"),
         q("t4-v2-10","【しゅうだん】で旅行する。",["衆団","集団","衆段","集段"],2,"Guruh bo'lib sayohat qilamiz.",expl="しゅうだん → 集団 (guruh, jamoa)"),
         q("t4-v2-11","あるテーマについて、全員で【ぎろん】した。",["異論","討論","理論","議論"],4,"Bir mavzu bo'yicha hammamiz bahslashdik.",expl="ぎろん → 議論 (bahs, munozara)"),
         q("t4-v2-12","ホストファミリーが私をあたたかく【むかえて】くれた。",["拝えて","待えて","迎えて","歓えて"],3,"Mezbon oila meni iliq kutib oldi.",expl="むかえる → 迎える (kutib olmoq)"),
         q("t4-v2-13","来週の授業の【よしゅう】をしてきてください。",["余習","復習","予習","複習"],3,"Keyingi hafta darsiga oldindan tayyorgarlik qiling.",expl="よしゅう → 予習 (oldindan tayyorgarlik)"),
         q("t4-v2-14","【てま】のかかる料理を作る。",["手間","手真","手麻","手試"],1,"Mashaqqat (vaqt) talab qiladigan taom tayyorlayman.",expl="てま → 手間 (ovora, mashaqqat, sarflanadigan vaqt)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t4-v3-15","あの人の、研究者としての（　）は長い。",["アイテム","タイム","キャリア","スケジュール"],3,"U odamning tadqiqotchi sifatidagi tajribasi (karyerasi) uzoq.",expl="キャリア = karyera, ish tajribasi"),
         q("t4-v3-16","お金を（　）、入場する。",["買って","与えて","贈って","払って"],4,"Pul to'lab, ichkariga kiraman.",expl="払う = to'lamoq (pul)"),
         q("t4-v3-17","このショッピングセンターは、去年より客が（　）している。",["加入","増加","成立","流行"],2,"Bu savdo markazida mijozlar o'tgan yilga nisbatan ko'paygan.",expl="増加 = ko'payish, ortish"),
         q("t4-v3-18","1日中歩いたので、とても（　）います。",["くたびれて","迷って","なやんで","病んで"],1,"Kun bo'yi yurganim uchun juda charchadim.",expl="くたびれる = charchamoq, holdan toymoq"),
         q("t4-v3-19","私もあなたの意見に（　）です。",["同等","平等","賛成","賛同"],3,"Men ham sizning fikringizga qo'shilaman.",expl="賛成 = qo'shilish, ma'qullash"),
         q("t4-v3-20","彼は、去年この町に（　）来た。",["引っ越して","引き出して","乗り越して","乗り出して"],1,"U o'tgan yili bu shaharga ko'chib keldi.",expl="引っ越す = ko'chib o'tmoq"),
         q("t4-v3-21","このお店はとても（　）がいい。",["チャンス","サービス","ルール","ショッピング"],2,"Bu do'konning xizmati juda yaxshi.",expl="サービス = xizmat ko'rsatish"),
         q("t4-v3-22","人を（　）で判断してはいけません。",["見合い","見回り","見立て","見かけ"],4,"Odamni tashqi ko'rinishiga qarab baholamaslik kerak.",expl="見かけ = tashqi ko'rinish"),
         q("t4-v3-23","明日何時に集まるか、電話で友だちに（　）した。",["理解","納得","確認","調査"],3,"Ertaga nechada yig'ilishni telefonda do'stim bilan aniqlashtirdim.",expl="確認 = tasdiqlash, aniqlashtirish"),
         q("t4-v3-24","12月に入って、（　）クリスマスが来るのを思い出した。",["さっき","さきに","もうすぐ","きっと"],3,"Dekabr kirib, tez orada Rojdestvo kelishini esladim.",expl="もうすぐ = tez orada, hademay"),
         q("t4-v3-25","彼は、パンクした自転車を（　）に直してくれた。",["単調","器用","得意","上等"],2,"U teshilgan velosipedni epchillik bilan tuzatib berdi.",expl="器用 = epchil, qo'li gul"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t4-v4-26","私の妹は、とても【おとなしい】。",["おとなっぽい","子どもっぽい","うるさい","静かだ"],4,"Singlim juda bosiq (yuvosh).",expl="おとなしい = yuvosh, bosiq → 静かだ (sokin)"),
         q("t4-v4-27","日曜日は、いつも家で【ごろごろ】しています。",["休んで","仕事して","運動して","そうじして"],1,"Yakshanba kuni doim uyda bekorchi yotaman (dam olaman).",expl="ごろごろする = bekorchi yotmoq → 休む (dam olmoq)"),
         q("t4-v4-28","彼女は、【いいかげん】な性格だ。",["すばらしい","だれにでも優しい","適当な","素直な"],3,"Uning fe'l-atvori beparvo (loqayd).",expl="いいかげん = beparvo, qovushmagan → 適当 (beparvo)"),
         q("t4-v4-29","新しい【職】を探しています。",["住むところ","働くところ","食べるところ","学ぶところ"],2,"Yangi ish qidiryapman.",expl="職 = ish, kasb → 働くところ (ish joyi)"),
         q("t4-v4-30","私たちは【もともとの】知り合いです。",["仲のよい","あまり仲のよくない","前からの","最近出会った"],3,"Biz aslidan (oldindan) tanish odamlarmiz.",expl="もともとの = aslidan, dastlabki → 前からの (oldindan)"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t4-v5-31","申し込む",["きっぷを買うために、機械にお金を申し込んだ。","自分はいつも正しいと申し込むほうがよい。","電話で会への参加を申し込んだ。","机の上に置いてある本を本棚に申し込んでください。"],3,
           "申し込む = ariza bermoq, yozilmoq, murojaat qilmoq.",optsTr=["Chipta olish uchun mashinaga pulni 'ariza qildim' (noto'g'ri).","O'zimni doim haq deb 'ariza qilgan' ma'qul (noto'g'ri).","Telefon orqali tadbirda qatnashishga yozildim (ariza berdim). (to'g'ri)","Stol ustidagi kitobni javonga 'ariza qiling' (noto'g'ri)."]),
         q("t4-v5-32","植える",["かばんに本とノートを植えました。","家の前に1本の桜の木を植えた。","地面をもっと深く植えてください。","来年、新しい家を植えようと思います。"],2,
           "植える = ekmoq (o'simlik).",optsTr=["Sumkaga kitob va daftarni 'ekdim' (noto'g'ri).","Uy oldiga bitta sakura daraxti ekdim. (to'g'ri)","Yerni yanada chuqurroq 'eking' (noto'g'ri).","Kelasi yil yangi uy 'ekmoqchiman' (noto'g'ri)."]),
         q("t4-v5-33","ユニーク",["この商品はどこにでも売っているユニークなものだ。","後の文章には、ユニークがたくさんある。","明日は1日中仕事なので、とてもユニークだ。","彼女の考え方は、とてもユニークでおもしろい。"],4,
           "ユニーク = o'ziga xos, noyob.",optsTr=["Bu mahsulot hamma joyda sotiladigan 'noyob' narsa (noto'g'ri).","Keyingi matnda 'noyob' ko'p bor (noto'g'ri).","Ertaga kun bo'yi ish, shuning uchun juda 'noyob' (noto'g'ri).","Uning fikrlash tarzi juda o'ziga xos va qiziqarli. (to'g'ri)"]),
         q("t4-v5-34","技術",["この会社には、すばらしい技術がある。","重い病気になって、病院で技術をした。","絵や音楽など、技術がとても好きだ。","1日で家を建てるなんて、まるで技術のようだ。"],1,
           "技術 = texnologiya, mahorat, texnika.",optsTr=["Bu kompaniyada ajoyib texnologiya bor. (to'g'ri)","Og'ir kasal bo'lib, kasalxonada 'texnika' qildim (noto'g'ri — 手術 jarrohlik kerak).","Rasm va musiqa kabilarning 'texnikasi'ni juda yaxshi ko'raman (noto'g'ri).","Bir kunda uy qurish — xuddi 'texnika'dek (noto'g'ri)."]),
         q("t4-v5-35","つらい",["かわいい服より、つらい服のほうが好きです。","親しい友だちと別れなければならないのは、つらい。","この料理はとてもつらいので、水を持ってきてください。","彼女から、つらい声で電話がかかってきた。"],2,
           "つらい = og'ir, alamli, mashaqqatli.",optsTr=["Chiroyli kiyimdan ko'ra 'alamli' kiyimni yaxshi ko'raman (noto'g'ri).","Yaqin do'st bilan xayrlashishga majbur bo'lish — og'ir (alamli). (to'g'ri)","Bu taom juda 'alamli', suv olib keling (noto'g'ri — 辛い achchiq kerak).","Undan 'alamli' ovozda qo'ng'iroq keldi (noto'g'ri)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t4-g1-1","このレポートを、明日の夜（　）書き終えるつもりだ。",["までで","までは","までの","までに"],4,"Bu hisobotni ertaga kechgacha yozib tugatmoqchiman.",expl="〜までに = ...gacha (oxirgi muddat, bir martalik ish)"),
         q("t4-g1-2","高校生の妹は、毎日遊んで（　）いる。",["より","しか","から","ばかり"],4,"O'rta maktabda o'qiydigan singlim har kuni faqat o'ynaydi.",expl="〜てばかりいる = faqat ...ish bilan band"),
         q("t4-g1-3","日本はほとんどの食料を輸入する（　）、毎日多くの食べ物が捨てられている。",["一方で","一方なら","だけで","だけなら"],1,"Yaponiya oziq-ovqatining ko'pini import qiladi, shu bilan birga har kuni ko'p ovqat tashlab yuboriladi.",expl="〜一方で = bir tomondan ...; bir vaqtning o'zida (qarama-qarshilik)"),
         q("t4-g1-4","朝から体の調子が（　）、今日は遊びに行けません。",["悪かったり","悪くて","悪いことと","悪さで"],2,"Ertalabdan beri o'zimni yomon his qilyapman, shuning uchun bugun sayrga chiqolmayman.",expl="〜くて = sabab (te-shakli)"),
         q("t4-g1-5","この子ねこは、見れば（　）かわいい。",["見ようほど","見ないほど","見るほど","見たほど"],3,"Bu mushukcha qancha qarasang, shuncha yoqimli.",expl="〜ば〜ほど = qancha ...sa, shuncha ..."),
         q("t4-g1-6","来年の試験を受けるなら、今から勉強を（　）ほうがいい。",["始めて","始めた","始めよう","始め"],2,"Kelasi yilgi imtihonni topshiradigan bo'lsang, hozirdan o'qishni boshlaganing ma'qul.",expl="〜たほうがいい = ...gani ma'qul (maslahat)"),
         q("t4-g1-7","この店の料理は、多すぎて（　）。",["食べきってない","食べきらない","食べきれない","食べきりがない"],3,"Bu restoranning taomi shunchalik ko'pki, yeb tugatib bo'lmaydi.",expl="〜きれない = oxirigacha ...ib bo'lolmaslik"),
         q("t4-g1-8","先生は、4時ごろに（　）。",["帰ってまいりました","お帰りになりました","帰っておりました","お帰りいたしました"],2,"O'qituvchi soat 4 larda uyiga qaytdilar.",expl="お〜になる = hurmat shakli (o'qituvchining harakati). 1·3·4 = kamtarlik shakllari (noto'g'ri)"),
         q("t4-g1-9","1週間で外国語を話せるようになるなんて（　）。",["あり得よう","あり得ない","あり得る","あり得た"],2,"Bir haftada chet tilida gapira oladigan bo'lib qolish — bo'lishi mumkin emas.",expl="あり得ない = bo'lishi mumkin emas, aql bovar qilmaydi"),
         q("t4-g1-10","佐藤「高尾山に行ったんでしょ。込んでいなかった？」鈴木「うーん、（　）人が少なくて、ゆっくり観光できたよ。」",["思っていたよりも","思わなかったより","思っていたほど","思うほどには"],1,"Sato: «Takao tog'iga borgansiz-a. Gavjum emasmidi?» Suzuki: «Hmm, o'ylaganimdan kamroq odam edi, shoshmasdan sayr qildim.»",expl="〜よりも = ...dan ko'ra (taqqoslash). 思っていたよりも = o'ylaganimdan ko'ra"),
         q("t4-g1-11","部長「もう時間が遅いので、仕事を終わりにして（　）。」部下「はい、わかりました。」",["帰ることもいいですよ","帰るだけですよ","帰ってもいいですよ","帰ったところですよ"],3,"Boshliq: «Vaqt kech bo'ldi, ishni tugatib uyga ketsangiz ham bo'ladi.» Xodim: «Xo'p, tushundim.»",expl="〜てもいい = ...sa bo'ladi (ruxsat)"),
         q("t4-g1-12","彼は毎日遊んでいる。このままでは次の試験に（　）。",["落ちないかもしれない","落ちかねない","落ちたかもしれない","落ちようがない"],2,"U har kuni o'ynaydi. Shu zayilda davom etsa, keyingi imtihondan yiqilib qolishi mumkin.",expl="〜かねない = ...ib qo'yishi mumkin (yomon natija ehtimoli)"),
         q("t4-g1-13","今日はとても暑いので、冷たいジュースが（　）。",["飲むことにならない","飲んでもしょうがない","飲まなくはない","飲みたくてたまらない"],4,"Bugun juda issiq, shuning uchun sovuq sharbat ichgim kelib chidab bo'lmayapti.",expl="〜たくてたまらない = ...gisi kelib, chiday olmaslik"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t4-g2-14",None,["ため","延期に","来週に","台風の"],3,"To'g'ri tartib: «Bugunga rejalashtirilgan sport bayrami tayfun tufayli keyingi haftaga qoldirildi.»",
           prefix="今日予定されていた運動会は、",suffix="なりました。",starPos=3,order=[4,1,3,2],expl="To'g'ri tartib: 台風のため来週に延期に (なりました)"),
         q("t4-g2-15",None,["教えて","そこに","いいか","行けば"],4,"To'g'ri tartib: «Qachon u yerga borsam bo'lishini aytib bera olmaysanmi?» — «Keyingi juma kuni kela olasanmi?»",
           prefix="中山「いつ",suffix="くれない？」",starPos=2,order=[2,4,3,1],expl="To'g'ri tartib: そこに行けばいいか教えて (くれない)"),
         q("t4-g2-16",None,["さえ","1冊の","あれば","本"],1,"To'g'ri tartib: «Agar do'stim umuman bo'lmasa ham, bittagina kitobim bo'lsa, men baxtni his qila olaman.»",
           prefix="もし、友だちが1人もいなくても、私は",suffix="幸せを感じることができます。",starPos=3,order=[2,4,1,3],expl="To'g'ri tartib: 1冊の本さえあれば"),
         q("t4-g2-17",None,["最中に","調べている","ついて","くわしく"],2,"To'g'ri tartib: «Detektiv o'sha ish yuzasidan batafsil tergov qilib turgan paytida boshqa hodisa yuz berdi.»",
           prefix="刑事がその事件に",suffix="別の事件が起こった。",starPos=3,order=[3,4,2,1],expl="To'g'ri tartib: ついてくわしく調べている (最中に)"),
         q("t4-g2-18",None,["大きく","ともなう","ますます","環境問題も"],4,"To'g'ri tartib: «Bu shahar sanoat shahri sifatida juda rivojlandi, biroq shunga hamroh atrof-muhit muammolari ham tobora kattalashib bormoqda.»",
           prefix="この町は、工業都市として大きく発展したが、それに",suffix="なっている。",starPos=2,order=[2,4,3,1],expl="To'g'ri tartib: ともなう環境問題もますます (大きく)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "「時間がない」",
       "passage": (
         "私たちは、「時間がない」とよく言う。しかし、本当に「時間がない」のだろうか。"
         "本当は「時間がある」のにいそがしいふりをしたり、自分をいそがしい状態にしていることも{{19}}。\n"
         "たとえば、こんなことがあった。何日か前、私は仕事へ行くために電車に乗った。急いでいたので、"
         "携帯電話も音楽プレーヤーも本もすべて忘れてしまった。いつもは、電車に{{20}}イヤフォンを耳に押し込み、"
         "かばんから本や新聞を取り出して、読むことにしている。携帯電話や携帯ゲームプレーヤーでゲームを"
         "始めることもある。{{21}}この日は何も持たずに電車に乗ってしまったので、何もすることがなくなってしまった。\n"
         "仕方がないので、電車に乗っているあいだ、何もしないで前の席に座る人の動作や窓の外をずっと見ていた。"
         "そうしたら、とてもリラックスができたのだ。{{22}}、私たちには何もしない時間が必要なのかもしれない。"
         "私たちは、わざわざ{{23}}用事を作り、生活をいそがしくしてしまっているような気がする。"
         "本当に「時間がない」のか考えてみるだけで、もっと充実した時間を取りもどすことができるのではないだろうか。"
       ),
       "passage_tr": (
         "Biz tez-tez «vaqt yo'q» deymiz. Lekin haqiqatan ham «vaqt yo'q»mi? Aslida «vaqt bor» bo'la turib, "
         "band bo'lganga olishimiz yoki o'zimizni band holatga solib qo'yishimiz ham bordir. "
         "Masalan, mana bunday voqea bo'lgan. Bir necha kun oldin ishga borish uchun poyezdga chiqdim. "
         "Shoshib qolganim uchun telefon ham, musiqa pleyeri ham, kitob ham — hammasini unutib qoldirdim. "
         "Odatda poyezdga chiqishim bilanoq quloqchinni qulog'imga tiqaman, sumkamdan kitob yoki gazeta olib "
         "o'qiyman. Telefon yoki o'yin pleyerida o'yin boshlab yuborishim ham bor. Biroq bu kuni hech narsasiz "
         "poyezdga chiqib qolganim uchun qiladigan ishim qolmadi. "
         "Iloji yo'qligidan, poyezdda ketayotganimda hech narsa qilmay, ro'paramda o'tirgan odamning harakatlarini "
         "va deraza ortini uzoq tikilib kuzatib o'tirdim. Shunda juda yengil tortdim (relaks bo'ldim). "
         "Bu narsa ko'rsatganidek, bizga hech narsa qilmaydigan vaqt ham kerakdir. Biz atayin, qilmasa ham "
         "bo'ladigan yumushlarni o'ylab topib, hayotimizni o'zimiz band qilib qo'yayotganga o'xshaymiz. "
         "Rostdan «vaqt yo'q»mi deb bir o'ylab ko'rishning o'ziyoq, yanada to'kis (mazmunli) vaqtni qaytarib "
         "olishimizga yordam berishi mumkin."
       ),
       "questions": [
         q("t4-g3-19",None,["ないのではないだろうか","なくてもよいのだろうか","あるのではないだろうか","あってもよいのだろうか"],3,
           "...していることも[あるのではないだろうか] = ...holatlar ham bordir, shunday emasmi?",blankNo="19",expl="〜のではないだろうか = ...emasmikan (yumshoq taxmin/xulosa)"),
         q("t4-g3-20",None,["乗ったすえに","乗ったとたん","乗れば乗るほど","乗ったばかりに"],2,
           "電車に[乗ったとたん]イヤフォンを = poyezdga chiqishim bilanoq quloqchinni.",blankNo="20",expl="〜たとたん = ...ishi bilanoq (darhol)"),
         q("t4-g3-21",None,["たとえば","または","しかも","ところが"],4,
           "[ところが]この日は何も持たずに = biroq bu kuni hech narsasiz.",blankNo="21",expl="ところが = biroq, lekin (kutilmagan qarama-qarshilik)"),
         q("t4-g3-22",None,["このことが示す通り","このことからはわからないが","このことが言うには","このことでよければ"],1,
           "[このことが示す通り]、何もしない時間が必要 = bu narsa ko'rsatganidek, hech narsa qilmaydigan vaqt kerak.",blankNo="22",expl="このことが示す通り = bu narsa ko'rsatganidek"),
         q("t4-g3-23",None,["してもいい","しなくてもいい","したほうがいい","すればいい"],2,
           "わざわざ[しなくてもいい]用事を作り = atayin qilmasa ham bo'ladigan yumush o'ylab topib.",blankNo="23",expl="〜なくてもいい = ...masa ham bo'ladi"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test04.json yozildi. Jami savol:", tot)
