# -*- coding: utf-8 -*-
"""test12.json — 第12回 模擬テスト (PDF betlari 118-127, javob 205)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test12.json")

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
  "id": 12, "title_jp": "第12回 模擬テスト", "title_uz": "12-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t12-v1-1","木の枝が【折れて】います。",["かれて","われて","おれて","きれて"],3,"Daraxt shoxi singan.",reading="おれて",expl="折れる → おれる (singmoq — uzun narsa)"),
         q("t12-v1-2","現金と野菜を【交換】する。",["こうさい","こうかん","こうりゅう","こうたい"],2,"Naqd pul va sabzavotni almashtiramiz.",reading="こうかん",expl="交換 → こうかん (almashtirish)"),
         q("t12-v1-3","新しい【図書】を注文した。",["としょ","とじょ","とうしょ","とうじょ"],1,"Yangi kitob buyurtma qildim.",reading="としょ",expl="図書 → としょ (kitob, adabiyot)"),
         q("t12-v1-4","この国では、【老人】がどんどん増えている。",["のうじん","のうにん","ろうじん","ろうにん"],3,"Bu mamlakatda keksalar tez ko'paymoqda.",reading="ろうじん",expl="老人 → ろうじん (keksa, qariya)"),
         q("t12-v1-5","その【缶】は金曜日に捨ててください。",["かん","びん","きん","ほん"],1,"U bankani juma kuni tashlang.",reading="かん",expl="缶 → かん (banka, quti — metall)"),
         q("t12-v1-6","南は、あちらの【方向】です。",["ほうく","ほうこ","ほうくう","ほうこう"],4,"Janub — anavi tomonda (yo'nalishda).",reading="ほうこう",expl="方向 → ほうこう (yo'nalish, tomon)"),
         q("t12-v1-7","この料理は、とても【苦い】です。",["からい","にがい","すっぱい","あまい"],2,"Bu taom juda achchiq (totuvi taxir).",reading="にがい",expl="苦い → にがい (achchiq, taxir)"),
         q("t12-v1-8","公園の【辺り】を散歩します。",["となり","ひだり","まわり","あたり"],4,"Bog' atrofini aylanaman.",reading="あたり",expl="辺り → あたり (atrof, tevarak)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t12-v2-9","【ふうん】なことに、事故にあった。",["不運","無運","負運","未運"],1,"Baxtsizlikka — avariyaga uchradim.",expl="ふうん → 不運 (baxtsizlik, omadsizlik)"),
         q("t12-v2-10","学者としての【じっせき】を上げる。",["実責","実積","実績","実席"],3,"Olim sifatidagi yutuqlarni (natijalarni) oshiraman.",expl="じっせき → 実績 (amaliy natija, yutuq)"),
         q("t12-v2-11","森の中で【まよって】、一晩中歩き続けた。",["悩って","困って","寄って","迷って"],4,"O'rmonda adashib, tun bo'yi yurdim.",expl="まよう → 迷う (adashmoq, yo'l yo'qotmoq)"),
         q("t12-v2-12","この動物園では、動物に【さわる】ことができます。",["採る","触る","解る","探る"],2,"Bu hayvonot bog'ida hayvonlarga tegish mumkin.",expl="さわる → 触る (tegmoq, ushlamoq)"),
         q("t12-v2-13","実家は【のうぎょう】を営んでいます。",["漁業","林業","工業","農業"],4,"Ota uyim dehqonchilik (qishloq xo'jaligi) bilan shug'ullanadi.",expl="のうぎょう → 農業 (dehqonchilik, qishloq xo'jaligi)"),
         q("t12-v2-14","この店には、よい【しなもの】が置いてある。",["商品","商者","品物","品者"],3,"Bu do'konda yaxshi mol (buyum) bor.",expl="しなもの → 品物 (mol, buyum, narsa)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t12-v3-15","彼の日曜日のすごし方は、いつも同じ（　）だ。",["フォーム","カラー","ライン","パターン"],4,"Uning yakshanbani o'tkazish tarzi doim bir xil andoza (qolip).",expl="パターン = qolip, andoza, naqsh"),
         q("t12-v3-16","どのようにして事故が起きたのか、細かく（　）した。",["等分","分析","分担","配分"],2,"Avariya qanday yuz berganini batafsil tahlil qildim.",expl="分析 = tahlil"),
         q("t12-v3-17","食事を全部食べないで捨てるのは（　）。",["うらやましい","めんどうくさい","こまかい","もったいない"],4,"Ovqatni to'liq yemay tashlash — isrofgarchilik (achinarli).",expl="もったいない = isrof, achinarli, behuda ketkazish"),
         q("t12-v3-18","夏休みは、いつも海外の別荘で（　）います。",["住んで","過ごして","離れて","戻って"],2,"Yozgi ta'tilni doim chet eldagi dala hovlida o'tkazaman.",expl="過ごす = (vaqt) o'tkazmoq"),
         q("t12-v3-19","コーヒーを（　）飲みに行きませんか。",["一口","一杯","一個","一枚"],2,"Bir piyola kofe ichgani bormaymizmi?",expl="一杯 = bir piyola/stakan (ichimlik sanog'i)"),
         q("t12-v3-20","この1年で身長が10センチも（　）。",["太った","得た","ふくらんだ","伸びた"],4,"Shu bir yilda bo'yim 10 santimetr o'sdi.",expl="伸びる = o'smoq, cho'zilmoq (bo'y)"),
         q("t12-v3-21","荷物を受け取るときに、（　）を求められた。",["マーク","ポスト","サイン","クレーム"],3,"Yukni olayotganda imzo (sayn) so'rashdi.",expl="サイン = imzo"),
         q("t12-v3-22","私（　）の手紙が来ていませんか。",["行き","向き","届け","あて"],4,"Menga atalgan (mening nomimga) xat kelmadimi?",expl="〜あて = ...ga atalgan, ...nomiga (manzil)"),
         q("t12-v3-23","他の会社に送る書類の（　）をするよう、部下に指示した。",["提示","作成","集合","設定"],2,"Boshqa kompaniyaga yuboriladigan hujjatni tayyorlashni xodimimga topshirdim.",expl="作成 = tuzish, tayyorlash (hujjat)"),
         q("t12-v3-24","いそがしい1日だったので、家に帰ると（　）した。",["はっと","さっと","ほっと","ざっと"],3,"Band kun bo'lgani uchun, uyga qaytsam yengil tortdim (tinchlandim).",expl="ほっとする = yengil tortmoq, tinchlanmoq"),
         q("t12-v3-25","その文章は、（　）なことばで書かれていた。",["不足","丈夫","明確","優秀"],3,"U matn aniq (ravshan) so'zlar bilan yozilgan edi.",expl="明確 = aniq, ravshan"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t12-v4-26","その旅館の部屋はとても【清潔だ】。",["古い","かわいい","きれいだ","明るい"],3,"U mehmonxona xonasi juda toza.",expl="清潔 = toza, ozoda → きれいだ"),
         q("t12-v4-27","仕事の準備が【整った】。",["続行した","停止した","開始した","終了した"],4,"Ish tayyorgarligi yakunlandi (bitdi).",expl="整う = tartibga tushmoq, tayyor bo'lmoq → 終了した (yakunlandi)"),
         q("t12-v4-28","彼は、友だちを【ぶって】しまった。",["手で打って","足でけって","体をぶつけて","悪口を言って"],1,"U do'stini urib qo'ydi (qo'li bilan).",expl="ぶつ = urmoq (qo'l bilan) → 手で打って"),
         q("t12-v4-29","映画館は【がらがらだ】。",["広い","汚い","こんでいる","すいている"],4,"Kinoteatr huvillab yotibdi (bo'm-bo'sh).",expl="がらがら = bo'm-bo'sh, huvillagan → すいている"),
         q("t12-v4-30","デパートの【向かい】に本屋があります。",["正面","手前","先","後ろ"],1,"Univermag ro'parasida kitob do'koni bor.",expl="向かい = ro'para, qarshi tomon → 正面"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t12-v5-31","合わせる",["毎朝、彼女と駅で合わせて一緒に学校へ行く。","友だちと声を合わせて、歌を歌った。","私の趣味は、外国の切手を合わせることです。","父と母は、学生のころに合わせて、結婚した。"],2,
           "合わせる = moslashtirmoq, qo'shmoq, birlashtirmoq.",optsTr=["Har kuni u bilan bekatda 'moslashib' maktabga boraman (noto'g'ri — 待ち合わせる kerak).","Do'stim bilan ovozni qo'shib, qo'shiq aytdik. (to'g'ri)","Mening sevimli mashg'ulotim — chet el markalarini 'moslashtirish' (noto'g'ri — 集める kerak).","Ota-onam talabalik chog'ida 'moslashib', turmush qurishdi (noto'g'ri — 出会う kerak)."]),
         q("t12-v5-32","いきおい",["この魚は、とてもいきおいがよくておいしい。","パソコンのいきおいが悪いので、修理をすることにした。","今日は体のいきおいがいいので、とても元気です。","その子どもたちは、いきおいよく走りだした。"],4,
           "いきおい(勢い) = shiddat, kuch, jadallik.",optsTr=["Bu baliq 'shiddati' yaxshi va mazali (noto'g'ri — 新鮮 kerak).","Kompyuter 'shiddati' yomon, ta'mirlaydigan bo'ldim (noto'g'ri — 調子 kerak).","Bugun tana 'shiddati' yaxshi, juda tetikman (noto'g'ri — 調子 kerak).","O'sha bolalar shiddat bilan yugurib ketishdi. (to'g'ri)"]),
         q("t12-v5-33","坂",["長い坂を渡って、家に帰りました。","ここは、日本でいちばん高い坂です。","私の学校は、急な坂の上に建っています。","強い風で坂がすべって、たくさんの人がけがをしました。"],3,
           "坂(さか) = qiyalik, do'nglik, qir yo'l.",optsTr=["Uzun qiyalikni 'kechib' uyga qaytdim (noto'g'ri — のぼる kerak).","Bu yer Yaponiyadagi eng baland 'qiyalik' (noto'g'ri — 山 kerak).","Mening maktabim tik qiyalik ustida joylashgan. (to'g'ri)","Kuchli shamoldan 'qiyalik sirpanib', ko'p odam jarohatlandi (noto'g'ri — 道 kerak)."]),
         q("t12-v5-34","すがた",["この音楽は、すがたがとてもいいので好きです。","私の兄と弟は、声のすがたがよく似ています。","有名なレストランで、肉のすがたを食べました。","さっき駅前で、彼女のすがたを見かけました。"],4,
           "すがた(姿) = qiyofa, ko'rinish, gavda.",optsTr=["Bu musiqaning 'qiyofasi' yaxshi, yoqadi (noto'g'ri — メロディー kerak).","Akam va ukam 'ovoz qiyofasi' o'xshash (noto'g'ri — 声 kerak).","Mashhur restoranda 'go'sht qiyofasi'ni yedim (noto'g'ri — 料理 kerak).","Hozir bekat oldida uning qiyofasini ko'rib qoldim. (to'g'ri)"]),
         q("t12-v5-35","はげしい",["歩いていたら、雨がはげしくふり出した。","彼の日本語は、この数カ月でとてもはげしくなった。","この紅茶ははげしくておいしいので、おかわりをください。","今日は、朝から何も食べていないので、おなかがはげしい。"],1,
           "はげしい(激しい) = qattiq, shiddatli, kuchli.",optsTr=["Yurib ketayotsam, yomg'ir qattiq yog'a boshladi. (to'g'ri)","Uning yaponchasi shu oylarda juda 'shiddatli' bo'ldi (noto'g'ri — 上達 kerak).","Bu choy 'shiddatli' va mazali, yana quying (noto'g'ri — 濃い kerak).","Bugun ertalabdan yemadim, qornim 'shiddatli' (noto'g'ri — すく kerak)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t12-g1-1","男性「どんなマンガが好きですか。」女性「私はマンガ（　）は読みません。時間のむだですから。」",["しか","ほど","から","など"],4,"Erkak: «Qanday manga yoqadi?» Ayol: «Men manga-panga o'qimayman. Vaqtni behuda ketkazadi.»",expl="〜など = ...-panga (mensimaslik, pisanda)"),
         q("t12-g1-2","私の息子は、まだ10歳の子どもの（　）、高いものをほしがる。",["ものに","ところに","くせに","きりに"],3,"O'g'lim hali 10 yoshli bola bo'la turib, qimmat narsalarni xohlaydi.",expl="〜くせに = ...bo'la turib (norozilik, ayb qo'yish)"),
         q("t12-g1-3","一生けん命走った（　）、電車に間に合わなかった。",["からには","からといって","あげく","あまり"],3,"Jon-jahdim bilan yugurdim-u, oqibatda poyezdga ulgurmadim.",expl="〜あげく = ...gan oqibatda (ko'pincha yomon natija)"),
         q("t12-g1-4","大事な会議の（　）、また後で電話してください。",["最中として","最中なので","最中であって","最中ながら"],2,"Muhim yig'ilishning ayni qizg'in payti bo'lgani uchun, keyinroq telefon qiling.",expl="〜最中なので = ayni ...ayotgan payt bo'lgani uchun"),
         q("t12-g1-5","家族と食事をしている（　）、学校の友だちが遊びに来た。",["ところで","ところは","ところが","ところへ"],4,"Oila bilan ovqatlanib o'tirgan paytimga maktab do'stim o'ynagani keldi.",expl="〜ているところへ = ayni ...ayotgan paytga (kimdir keladi)"),
         q("t12-g1-6","母「手術が成功するか心配で…」娘「手術（　）すぐに終わるし、心配しないで。」",["というと","といえば","といっても","といったら"],3,"Ona: «Operatsiya muvaffaqiyatli bo'ladimi deb tashvishlanyapman…» Qiz: «Operatsiya desa ham tez tugaydi, xavotir olma.»",expl="〜といっても = ...desa ham, ...deyilsa-da"),
         q("t12-g1-7","もし外国に（　）のなら、フィンランドに住んでみたい。",["住む","住み","住んで","住んだ"],1,"Agar chet elda yashaydigan bo'lsam, Finlyandiyada yashab ko'rmoqchiman.",expl="〜のなら = ...adigan bo'lsa (shart). 住むのなら"),
         q("t12-g1-8","田中「ぼくはカレーライス。」鈴木「私はとんかつ（　）。」",["にします","をします","としています","でしています"],1,"Tanaka: «Men karri guruch.» Suzuki: «Men tonkatsu olaman (tanladim).»",expl="〜にする = ...ga qaror qilmoq, ...ni tanlamoq"),
         q("t12-g1-9","社長は何かスポーツを（　）。",["まいりますか","なさいますか","いたしますか","いらっしゃいますか"],2,"Rahbar biror sport bilan shug'ullanadilarmi?",expl="なさる = する ning hurmat shakli (qiladilar)"),
         q("t12-g1-10","小学生のころ、父は私に勉強を教えて（　）。",["やりました","あげました","さしあげました","くれました"],4,"Boshlang'ich sinfda otam menga darsni o'rgatib berardi.",expl="〜てくれる = (boshqa kishi menga) ...ib bermoq. 教えてくれました"),
         q("t12-g1-11","自分がいじめられたから、友だちをいじめていい（　）。",["というはずではない","といったものだ","ということにはならない","というわけだ"],3,"O'zing zo'ravonlikka uchraganing uchun, do'stingni xafa qilsang bo'ladi degani emas.",expl="〜ということにはならない = ...degani bo'lmaydi"),
         q("t12-g1-12","これが、みんながずっと探していた宝物に（　）。",["ほかなります","ほかなりません","ほかにあります","ほかにありません"],2,"Mana shu — hamma uzoq izlagan xazinaning aynan o'zginasi.",expl="〜にほかならない = aynan ...ning o'zi, boshqa narsa emas"),
         q("t12-g1-13","子どものころ、病気で苦しむ私に、母は「（　）代わりたい」と言って泣いていた。",["代わったならば","代わりたいけれど","代わるものでも","代われるものなら"],4,"Bolaligimda kasallikdan azob chekayotganimda, onam «iloji bo'lsa o'rningga o'tardim» deb yig'lardi.",expl="〜ものなら = iloji bo'lsa (amalga oshishi qiyin istak). 代われるものなら"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t12-g2-14",None,["一生けん命","こたえて","がんばろうと","期待に"],3,"To'g'ri jumla: «Barchangizning umidingizni oqlab, jon-jahdim bilan harakat qilmoqchiman.»",
           prefix="みなさまの",suffix="思います。",starPos=4,order=[4,2,1,3],expl="To'g'ri tartib: 期待にこたえて一生けん命がんばろうと (〜にこたえる = ...ni oqlamoq)"),
         q("t12-g2-15",None,["でしたら","めしあがりたい","お酒を","の"],2,"To'g'ri jumla: «Faqat choy tayyorlaganman, lekin agar o'qituvchi ichimlik ichmoqchi bo'lsalar, buyurtma beraman.»",
           prefix="お茶しか用意していませんが、先生がもし",suffix="注文します。",starPos=2,order=[3,2,4,1],expl="To'g'ri tartib: お酒をめしあがりたいのでしたら (めしあがる = «yemoq/ichmoq» hurmat shakli)"),
         q("t12-g2-16",None,["からで","確かめて","ないと","なんとも"],3,"To'g'ri jumla: «Aytmoqchimanki, mas'ul xodimdan tasdiqlamasdan turib, hech narsa deya olmayman.»",
           prefix="三上「そのことなんですが、担当者に",suffix="言えないんですよ。」",starPos=3,order=[2,1,3,4],expl="To'g'ri tartib: 確かめてからでないと (〜てからでないと = ...gandan keyingina)"),
         q("t12-g2-17",None,["かねない","病気が","なり","悪く"],3,"To'g'ri jumla: «Shu zayilda davolanmasangiz, kasallik kuchayib ketishi mumkin deb shifokor aytdi.»",
           prefix="このまま治療をしないと、",suffix="と医者に言われました。",starPos=3,order=[2,4,3,1],expl="To'g'ri tartib: 病気が悪くなりかねない (〜かねない = ...ib qolishi mumkin, yomon ehtimol)"),
         q("t12-g2-18",None,["ある事件を","有名な","歴史上","もとに"],1,"To'g'ri jumla: «Men hozir o'qiyotgan kitob tarixdagi mashhur bir voqeaga asoslanib yozilgan.»",
           prefix="私が今、読んでいる本は、",suffix="書かれている。",starPos=3,order=[3,2,1,4],expl="To'g'ri tartib: 歴史上有名なある事件をもとに (〜をもとに = ...ga asoslanib)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "片づけは必要か",
       "passage": (
         "「そうじ」「片づけ」「整理」をテーマにした本がたくさん出版されているのを{{19}}。"
         "「そうじ名人になるには」「あなたも片づけられる人になろう！」「お部屋の整理術」……"
         "書店に行くと、このようなタイトルの本を{{20}}。著者は、有名人のこともあれば一般人のことも"
         "ある。どちらにしても「片づけ名人」が書いた本であることはまちがいない。また、このような種類の"
         "本は、よく売れているようだ。{{21}}、それだけ「片づけられない人」「整理が苦手な人」が世の中に"
         "たくさんいるということだろう。\n"
         "実は、私自身も「片づけられない人間」の1人である。部屋はいつも汚い。机の引き出しの中も物が"
         "たくさんつまっているし、部屋のあちこちに、本や服などいろいろなものが積み重なっている。\n"
         "しかし、私自身について言えば、そうであっても{{22a}}身の回りを整理しよう、片づけよう{{22b}}。"
         "たぶん、すべてが整理された、とてもきれいな部屋は、逆に気持ちが落ちつかないことと、片づけを"
         "する時間が十分にとれないことが理由だろう。私は今のところ、整理や片づけの本を読んでまで"
         "部屋を片づけようと{{23}}。"
       ),
       "passage_tr": (
         "«Tozalash», «yig'ishtirish», «tartibga solish» mavzusidagi kitoblar juda ko'p chop etilayotganini "
         "BILASIZMI? «Tozalash ustasi bo'lish uchun», «Siz ham yig'ishtira oladigan inson bo'ling!», «Xona "
         "tartibi san'ati»… kitob do'koniga borsangiz, shunday sarlavhali kitoblarni KO'RMAY ILOJINGIZ YO'Q "
         "(albatta ko'rasiz). Mualliflar goh mashhur, goh oddiy odamlar bo'ladi. Qaysidir bo'lsa-da, «tartib "
         "ustasi» yozgan kitob ekani aniq. Bunday kitoblar yaxshi sotilayotganga o'xshaydi. QISQASI, demak "
         "dunyoda «yig'ishtira olmaydigan», «tartibga qiynaladigan» odamlar shunchalik ko'p degani. "
         "Aslida, men ham «yig'ishtira olmaydigan odam»lardan biriman. Xonam doim kir. Stol tortmasi ham "
         "narsaga to'la, xonaning hamma yog'ida kitob, kiyim kabilar uyilib yotadi. "
         "Lekin, o'zim haqimda aytsam, shunday bo'lsa ham, ATAYIN atrofni tartibga solay, yig'ishtiray DEGAN "
         "FIKR KELMAYDI. Ehtimol, hammasi tartibli, juda toza xona aksincha ko'nglimni g'ash qilishi va "
         "yig'ishtirishga vaqt yetarli topa olmasligim sabab bo'lsa kerak. Men hozircha, tartib-tozalik "
         "kitobini o'qibgacha xonamni yig'ishtiray deb O'YLAMAYMAN."
       ),
       "questions": [
         q("t12-g3-19",None,["うかがっただろうか","おうかがいしただろうか","存じているだろうか","ご存じだろうか"],4,
           "本が…出版されているのを[ご存じだろうか] = …chop etilayotganini BILASIZMI? (o'quvchiga hurmat).",blankNo="19",expl="ご存じだろうか = bilasizmi (知っている ning hurmat shakli)"),
         q("t12-g3-20",None,["見かけたものだ","見かけることなどない","見かけないといってよい","見かけないことはない"],4,
           "書店で…本を[見かけないことはない] = ...kitoblarni KO'RMAY ILOJING yo'q (albatta ko'rasan).",blankNo="20",expl="〜ないことはない = ...masdan iloji yo'q (albatta shunday). Ikki inkor = tasdiq"),
         q("t12-g3-21",None,["要するに","それどころか","とはいうものの","だからといって"],1,
           "よく売れている。[要するに]、…人がたくさんいる = yaxshi sotiladi. QISQASI, ...odamlar ko'p.",blankNo="21",expl="要するに = qisqasi, xullas (xulosa)"),
         q("t12-g3-22",None,["わざと ／ ということになっている","わざと ／ という気にならない","わざわざ ／ ということになっている","わざわざ ／ という気にならない"],4,
           "[わざわざ]整理しよう…[という気にならない] = ATAYIN tartibga solay degan FIKR KELMAYDI.",blankNo="22",expl="22-a わざわざ (atayin, ovora bo'lib) + 22-b という気にならない (...gisi kelmaydi)"),
         q("t12-g3-23",None,["思わないでもない","思うことは思う","思う","思わない"],4,
           "本を読んでまで…片づけようと[思わない] = ...kitob o'qibgacha yig'ishtiray deb O'YLAMAYMAN.",blankNo="23",expl="思わない = o'ylamayman (sodda inkor)"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test12.json yozildi. Jami savol:", tot)
