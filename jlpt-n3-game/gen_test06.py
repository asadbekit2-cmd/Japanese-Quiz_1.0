# -*- coding: utf-8 -*-
"""test06.json — 第6回 模擬テスト (PDF betlari 58-67, javob 199)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test06.json")

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
  "id": 6, "title_jp": "第6回 模擬テスト", "title_uz": "6-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t6-v1-1","箱が【壊れ】ました。",["われ","おれ","こわれ","はなれ"],3,"Quti singan.",reading="こわれ",expl="壊れる → こわれる (sinmoq, buzilmoq)"),
         q("t6-v1-2","【各地】で雨が降り始めました。",["かくじ","かくち","きゃくじ","きゃくち"],2,"Har joyda yomg'ir yog'a boshladi.",reading="かくち",expl="各地 → かくち (har joy, turli joylar)"),
         q("t6-v1-3","あの店の【主人】は働き者だ。",["しゅにん","じゅにん","しゅじん","じゅじん"],3,"U do'konning egasi mehnatkash.",reading="しゅじん",expl="主人 → しゅじん (xo'jayin, eg)"),
         q("t6-v1-4","このシャツは、もう【洗って】あります。",["きって","さわって","ぬって","あらって"],4,"Bu ko'ylak allaqachon yuvilgan.",reading="あらって",expl="洗う → あらう (yuvmoq)"),
         q("t6-v1-5","アパートは通学に【不便】なところにある。",["ふべん","ふだん","ふまん","ふしん"],1,"Kvartira o'qishga borish uchun noqulay joyda.",reading="ふべん",expl="不便 → ふべん (noqulay)"),
         q("t6-v1-6","久しぶりに【仲間】が集まった。",["ながま","なかま","ちゅうかん","ちゅうげん"],2,"Ancha vaqtdan keyin do'stlar (sheriklar) yig'ildi.",reading="なかま",expl="仲間 → なかま (sherik, do'st, hamroh)"),
         q("t6-v1-7","あの人は、【肌】がきれいだ。",["ゆび","ひふ","はだ","つめ"],3,"U odamning terisi toza (chiroyli).",reading="はだ",expl="肌 → はだ (teri)"),
         q("t6-v1-8","書類を【郵送】しておきました。",["はっそう","はいそう","ゆそう","ゆうそう"],4,"Hujjatlarni pochta orqali jo'natib qo'ydim.",reading="ゆうそう",expl="郵送 → ゆうそう (pochta orqali jo'natish)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t6-v2-9","【ふせいな】取引を禁じる。",["不生","不性","不正","不成"],3,"G'irrom (nohaq) savdoni taqiqlash.",expl="ふせい → 不正 (nohaqlik, g'irromlik)"),
         q("t6-v2-10","長い【きゅうか】を取る。",["休憩","休息","休養","休暇"],4,"Uzoq ta'til olaman.",expl="きゅうか → 休暇 (ta'til)"),
         q("t6-v2-11","親に【たのんで】、車を買ってもらった。",["頼んで","願んで","望んで","希んで"],1,"Ota-onamdan iltimos qilib, menga mashina sotib oldirdim.",expl="たのむ → 頼む (iltimos qilmoq)"),
         q("t6-v2-12","生活で【こまる】ことは何ですか。",["苦る","迷る","因る","困る"],4,"Hayotda qiynaladigan narsangiz nima?",expl="こまる → 困る (qiynalmoq, mushkul ahvolga tushmoq)"),
         q("t6-v2-13","ホテルに【とまる】ことにした。",["止まる","留まる","停まる","泊まる"],4,"Mehmonxonada tunashga qaror qildim.",expl="とまる → 泊まる (tunamoq, qo'nmoq)"),
         q("t6-v2-14","敵と【みかた】にわかれて争う。",["見方","味方","見形","味形"],2,"Dushman va tarafdorlarga bo'linib kurashamiz.",expl="みかた → 味方 (tarafdor, o'z tomon)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t6-v3-15","音楽なら、（　）は関係なく、何でも聞きます。",["ケース","クラス","ステージ","ジャンル"],4,"Musiqa bo'lsa, janridan qat'i nazar, hamma narsani tinglayman.",expl="ジャンル = janr, tur"),
         q("t6-v3-16","明日は、先生を（　）するつもりです。",["質問","訪問","問答","返答"],2,"Ertaga o'qituvchimni ziyorat qilmoqchiman.",expl="訪問 = tashrif, ziyorat"),
         q("t6-v3-17","新しい仕事を（　）することになった。",["出社","通勤","出張","担当"],4,"Yangi ishni zimmamga olishimga to'g'ri keldi.",expl="担当 = mas'ul bo'lish, zimmasiga olish"),
         q("t6-v3-18","彼女を（　）コーヒーを飲みに行った。",["語って","誘って","論じて","遊んで"],2,"Uni taklif qilib, kofe ichgani bordik.",expl="誘う = taklif qilmoq, birga olib bormoq"),
         q("t6-v3-19","山田さんは、私の（　）の友だちだ。",["唯一","単一","同一","万一"],1,"Yamada-san mening yagona do'stim.",expl="唯一 = yagona, bittagina"),
         q("t6-v3-20","ちゃんと勉強していれば、テストを（　）よい。",["かなしまなくても","おそれなくても","さびしがらなくても","にげなくても"],2,"Yaxshilab o'qigan bo'lsang, imtihondan qo'rqmasang ham bo'ladi.",expl="おそれる = qo'rqmoq; おそれなくてもよい = qo'rqmasa ham bo'ladi"),
         q("t6-v3-21","仕事中に大きな（　）が起きた。",["アクセス","ストップ","ヒット","トラブル"],4,"Ish vaqtida katta muammo yuz berdi.",expl="トラブル = muammo, nizo"),
         q("t6-v3-22","使用（　）のものは、ここに捨ててください。",["止め","済み","終わり","切り"],2,"Ishlatib bo'lingan narsalarni shu yerga tashlang.",expl="使用済み = ishlatilgan, foydalanib bo'lingan"),
         q("t6-v3-23","私は、両親のおかげで（　）できました。",["保育","前後","成長","発展"],3,"Men ota-onam tufayli ulg'aya oldim.",expl="成長 = o'sish, ulg'ayish"),
         q("t6-v3-24","（　）お宅に遊びに行くうちに、田中さんと親しくなった。",["ちかぢか","まるまる","たびたび","いちいち"],3,"Tez-tez uyiga borib turib, Tanaka-san bilan yaqinlashib qoldim.",expl="たびたび = tez-tez, qayta-qayta"),
         q("t6-v3-25","なんとなく体が（　）だ。",["調子","調整","低調","不調"],4,"Negadir tanamda nochorlik (mazasizlik) bor.",expl="不調 = noso'z, nochor holat, mazasizlik"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t6-v4-26","この本は、とても【やさしい】。",["安い","高い","簡単だ","難しい"],3,"Bu kitob juda oson.",expl="やさしい = oson → 簡単だ"),
         q("t6-v4-27","彼女は、電車の中で【ささやいた】。",["大きな声で話した","小さな声で話した","たくさん眠った","少し眠った"],2,"U poyezdda pichirladi.",expl="ささやく = pichirlamoq → 小さな声で話した (past ovozda gapirdi)"),
         q("t6-v4-28","私のことは、あまり【気にしないで】ください。",["怒らないで","笑わないで","心配しないで","驚かないで"],3,"Men haqimda ko'p tashvishlanmang.",expl="気にする = e'tibor bermoq, tashvishlanmoq → 心配しないで"),
         q("t6-v4-29","先生は子どもたちを【しかった】。",["命令した","監督した","注意した","評価した"],3,"O'qituvchi bolalarni urishdi (tanbeh berdi).",expl="しかる = koyimoq, urishmoq → 注意した (ogohlantirdi, tanbeh berdi)"),
         q("t6-v4-30","あの人は、とても【ていねいに】話す。",["大きな声で","親切そうに","きれいな発音で","礼儀正しく"],4,"U odam juda odob bilan gapiradi.",expl="ていねいに = ehtiyotkorlik/odob bilan → 礼儀正しく (odobli)"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t6-v5-31","すれ違う",["さっき、知り合いが乗った車とすれ違った。","左右の靴をすれ違ってはいていた。","本の名前をすれ違って、他の本を買ってしまった。","今度のテストでは、たくさん答えをすれ違った。"],1,
           "すれ違う = bir-birining yonidan o'tib ketmoq (qarama-qarshi yo'nalishda).",optsTr=["Hozir tanishim o'tirgan mashina bilan yonma-yon o'tib ketdik. (to'g'ri)","Chap-o'ng oyoq kiyimni 'aralashtirib' kiygan edim (noto'g'ri — 間違える kerak).","Kitob nomini 'adashtirib', boshqa kitob sotib oldim (noto'g'ri).","Bu testda ko'p javoblarni 'adashtirdim' (noto'g'ri)."]),
         q("t6-v5-32","わかす",["たまごをわかして食べるとおいしい。","トースターでパンをわかして食べた。","なべで野菜をわかして料理を作った。","お茶を飲むために、お湯をわかした。"],4,
           "わかす = (suvni) qaynatmoq.",optsTr=["Tuxumni 'qaynatib' yegan mazali (noto'g'ri — ゆでる kerak).","Tosterda nonni 'qaynatib' yedim (noto'g'ri).","Qozonda sabzavotni 'qaynatib' taom qildim (noto'g'ri — 煮る kerak).","Choy ichish uchun suv qaynatdim. (to'g'ri)"]),
         q("t6-v5-33","タイミング",["タイミングがなくて、試験の問題が全部できませんでした。","上手なタイミングをして、会議の時間に会社に着いた。","駅に着いたら、タイミングよく電車が来た。","長いタイミングがあったら、ぜひまた旅行に行きましょう。"],3,
           "タイミング = vaqt-payt, qulay lahza.",optsTr=["'Vaqt-payt' bo'lmagani uchun imtihon savollarini bajara olmadim (noto'g'ri — 時間 kerak).","'Yaxshi tayming qilib', yig'ilish vaqtida yetib keldim (noto'g'ri).","Bekatga yetganimda, ayni paytida poyezd keldi. (to'g'ri)","'Uzoq tayming' bo'lsa, yana sayohatga boraylik (noto'g'ri — 時間 kerak)."]),
         q("t6-v5-34","しろうと",["彼はこの分野のしろうとなので、何でも質問してください。","彼はしろうとの運転手なので、かなり運転が上手だ。","この病院には、しろうとの病人がたくさんいる。","私は映画のしろうとなので、映画のことはよくわかりません。"],4,
           "しろうと(素人) = havaskor, mutaxassis bo'lmagan odam.",optsTr=["U bu sohaning 'havaskori', shuning uchun istalgan narsani so'rang (noto'g'ri — 専門家 kerak).","U 'havaskor' haydovchi, shuning uchun juda yaxshi haydaydi (noto'g'ri/ziddiyat).","Bu kasalxonada 'havaskor' bemorlar ko'p (noto'g'ri).","Men kino bo'yicha havaskorman, kino haqida yaxshi bilmayman. (to'g'ri)"]),
         q("t6-v5-35","豊か",["あの男の人が着ているシャツやネクタイの色は豊かだ。","この国は、気候も温暖だし、資源も豊かだ。","今晩は時間が豊かなので、電話してください。","たくさん運動して、筋肉を豊かにしようと思う。"],2,
           "豊か = boy, mo'l, serob.",optsTr=["U erkak kiygan ko'ylak va galstuk rangi 'boy' (noto'g'ri — 派手 kerak).","Bu davlatning iqlimi ham issiq, resurslari ham boy. (to'g'ri)","Bugun kechqurun vaqtim 'boy' (noto'g'ri — たっぷり kerak).","Ko'p sport qilib, mushaklarni 'boy' qilmoqchiman (noto'g'ri)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t6-g1-1","もし時間があったら、あそこでお茶（　）飲みませんか。",["ほど","でも","から","きり"],2,"Agar vaqting bo'lsa, anavi yerda choy-poy ichmaymizmi?",expl="〜でも = ...-poy (misol keltirib, yengil taklif)"),
         q("t6-g1-2","よけいなことを言った（　）、母が怒ってしまった。",["たびに","ところに","ばかりに","ごとに"],3,"Ortiqcha gap aytganim uchun, onam jahli chiqib qoldi.",expl="〜たばかりに = faqat ...ganim sababli (yomon natija)"),
         q("t6-g1-3","私は25歳なので、もう（　）以上、背は高くならないだろう。",["どこ","それ","どれ","これ"],4,"Men 25 yoshdaman, shuning uchun bundan ortiq bo'yim o'smasa kerak.",expl="これ以上 = bundan ortiq, bundan ziyod"),
         q("t6-g1-4","一度にバナナを20本も食べられる（　）。",["ようがない","ものがない","ことがない","わけがない"],4,"Bir o'tirishda 20 dona bananni yeb bo'lmaydi (mumkin emas).",expl="〜わけがない = ...bo'lishi mumkin emas"),
         q("t6-g1-5","高橋「山田さん、英語がお上手ですね。」山田「いいえ、（　）上手じゃありません。」",["めったに","たいして","やたらに","ほんの"],2,"Takaxashi: «Yamada-san, ingliz tilini yaxshi bilarkansiz.» Yamada: «Yo'q, uncha yaxshi emasman.»",expl="たいして〜ない = uncha ...emas"),
         q("t6-g1-6","この食品は、味がいいのに（　）、値段も安いです。",["加えずに","加えないで","加えて","加えたら"],3,"Bu mahsulot mazasi yaxshi bo'lishiga qo'shimcha, narxi ham arzon.",expl="〜に加えて = ...ga qo'shimcha, bundan tashqari"),
         q("t6-g1-7","病気になってから、もうたばこは（　）まいと思った。",["吸う","吸い","吸おう","吸って"],2,"Kasal bo'lganimdan keyin, endi tamaki chekmaslikka qaror qildim.",expl="〜まい = ...maslikka (qat'iy inkor niyat). 吸い+まい"),
         q("t6-g1-8","卒業するときに、先生からプレゼントを（　）。",["あげました","さしあげました","やりました","いただきました"],4,"Bitirayotganimda, o'qituvchidan sovg'a oldim.",expl="いただく = もらう ning kamtarlik shakli (oldim)"),
         q("t6-g1-9","社員「社長の来月の予定を教えていただけますか。」課長「もうしわけありませんが、社長の予定は（　）。」",["わかります","わかりました","わかりかねます","わかりかねました"],3,"Xodim: «Rahbarning keyingi oylik rejasini ayta olasizmi?» Bo'lim boshlig'i: «Kechirasiz, rahbarning rejasini bila olmayman.»",expl="〜かねる = ... qila olmaslik (xushmuomala rad). わかりかねます = bila olmayman"),
         q("t6-g1-10","日本では、新しい学年は4月に始まる（　）。",["ものとなっている","こととなっている","わけになっている","ほどになっている"],2,"Yaponiyada yangi o'quv yili aprelda boshlanadigan qilib belgilangan.",expl="〜こととなっている = ...qilib belgilangan (qoida/qaror)"),
         q("t6-g1-11","彼は何も準備をしていないのだから、明日の試験に（　）。",["落ちるに決めている","落ちるところに決めている","落ちるに決まっている","落ちるところに決まっている"],3,"U hech qanday tayyorgarlik ko'rmagan, shuning uchun ertangi imtihondan albatta yiqiladi.",expl="〜に決まっている = albatta ...bo'ladi (ishonch)"),
         q("t6-g1-12","小さい子どもは、たばこを（　）。",["吸ってもらいません","吸うわけではありません","吸わなくしてください","吸ってはいけません"],4,"Kichik bolalar tamaki chekmasligi kerak.",expl="〜てはいけない = ...maslik kerak (taqiq)"),
         q("t6-g1-13","店員「いらっしゃいませ。」客「すみません。この服を（　）。」",["着てみたらいいでしょうか","着てみるのもいいですか","着てみるのがいいでしょうか","着てみてもいいですか"],4,"Sotuvchi: «Xush kelibsiz.» Mijoz: «Kechirasiz. Bu kiyimni kiyib ko'rsam bo'ladimi?»",expl="〜てみてもいいですか = ...ib ko'rsam bo'ladimi (ruxsat so'rash)"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t6-g2-14",None,["せいで","甘い","大好きな","ものが"],3,"To'g'ri jumla: «Shokolad va tort kabi shirin narsalarni juda yaxshi ko'rganim sababli, semirib ketdim.»",
           prefix="チョコレートやケーキなど",suffix="太ってしまった。",starPos=3,order=[2,4,3,1],expl="To'g'ri tartib: 甘いものが大好きなせいで"),
         q("t6-g2-15",None,["ことを","おけば","決まった","申し上げて"],1,"To'g'ri jumla: «Bo'lim boshlig'iga yig'ilishda hal qilingan narsani aytib qo'ysam bo'ladimi?»",
           prefix="では、部長には、会議で",suffix="よろしいでしょうか。",starPos=2,order=[3,1,4,2],expl="To'g'ri tartib: 決まったことを申し上げておけば"),
         q("t6-g2-16",None,["と","している","しよう","ところへ"],2,"To'g'ri jumla: «Aynan uy vazifasini qilmoqchi bo'lib turganimda, do'stim kelib qoldi.»",
           prefix="ちょうど宿題を",suffix="友だちがやって来た。",starPos=3,order=[3,1,2,4],expl="To'g'ri tartib: しようとしているところへ"),
         q("t6-g2-17",None,["に","行く","旅行に","たび"],4,"To'g'ri jumla: «Men qo'g'irchoqlarni yoqtirganim uchun, har safar sayohatga borganimda o'sha mamlakat qo'g'irchog'ini sotib olib kelaman.»",
           prefix="私は、人形が好きなので、",suffix="その国の人形を買ってきます。",starPos=3,order=[3,2,4,1],expl="To'g'ri tartib: 旅行に行くたびに"),
         q("t6-g2-18",None,["動物たちが","はじめ","かわいい","とする"],3,"To'g'ri jumla: «U hayvonot bog'ida pandani boshlab, ko'plab yoqimtoy hayvonlar bor.»",
           prefix="その動物園には、パンダを",suffix="たくさんいる。",starPos=3,order=[2,4,3,1],expl="To'g'ri tartib: はじめとするかわいい動物たちが (Aを はじめとする = A boshchiligida)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "初めての銭湯（ピエール・マルタン）",
       "passage": (
         "あなたは、日本のお風呂といえば何を思いうかべますか。温泉でしょうか、銭湯でしょうか。"
         "いろいろありますが、私の場合は「銭湯」です。\n"
         "私の故郷には、毎日お風呂に入るという習慣はありません。{{19}}、日本へ来たばかりのときは、"
         "日本人が毎日お風呂に入るということを知って、とても驚きました。\n"
         "家にお風呂がある人は、家のお風呂に毎日入りますし、家にお風呂がない場合も、"
         "毎日のように家の近所にある「銭湯」に行きます。{{20}}習慣を持っている民族は、"
         "広い世界の中でもあまりないと思います。\n"
         "初めて銭湯に行ったときに、驚いたことがたくさんありました。{{21a}}、建物がお寺や神社のような"
         "とても古い建物だったこと。第二に、入口が「男湯」と「女湯」に分かれていたこと。"
         "第三に、ほかの人の前で服を全部脱いでお風呂に入らなければならなかったこと。"
         "{{21b}}、お風呂のお湯の温度がとても高かったことです。\n"
         "しかし、今では日本の銭湯にも{{22}}。なにも気にせずに熱いお湯にゆっくり入れるようになりました。"
         "私もかなり「日本人」に近づいてきたという{{23}}。"
       ),
       "passage_tr": (
         "Yaponiyaning hammomi (お風呂) deyilsa, nima ko'z oldingizga keladi? Issiq buloqmi (onsen), "
         "jamoa hammomimi (sento)? Turlichasi bor, mening holatimda esa — «sento». "
         "Mening vatanimda har kuni hammomga tushish odati yo'q. SHUNING UCHUN, Yaponiyaga endi kelganimda, "
         "yaponlar har kuni cho'milishini bilib, juda hayron bo'ldim. "
         "Uyida hammomi bor odamlar har kuni o'z hammomida cho'miladi; hammomi yo'qlar ham deyarli har kuni "
         "uy yaqinidagi «sento»ga boradi. BUNDAY odatga ega xalq keng dunyoda ham kam uchraydi deb o'ylayman. "
         "Birinchi marta sento'ga borganimda, hayron qoldirgan narsalar ko'p edi. AVVALO, bino ibodatxona yoki "
         "ziyoratgohga o'xshash juda eski bino edi. Ikkinchidan, kirish «erkaklar hammomi» va «ayollar hammomi»ga "
         "ajratilgan edi. Uchinchidan, boshqalar oldida kiyimni butunlay yechib cho'milish kerak edi. "
         "ENG AVVALO (yana bir muhimi), suvning harorati juda yuqori edi. "
         "Ammo endilikda yapon sento'siga ham KO'NIKIB BORYAPMAN. Hech narsadan tashvishlanmay, issiq suvga "
         "bemalol tusha oladigan bo'ldim. Men ham ancha «yaponlar»ga yaqinlashib qolganim SHU bo'lsa kerak."
       ),
       "questions": [
         q("t6-g3-19",None,["なぜなら","または","ですから","ただし"],3,
           "習慣はありません。[ですから]日本へ来たばかりのとき…驚きました = odat yo'q. SHUNING UCHUN kelganimda hayron bo'ldim.",blankNo="19",expl="ですから = shuning uchun, demak (sabab-natija)"),
         q("t6-g3-20",None,["あの","このような","ああした","それほどの"],2,
           "[このような]習慣を持っている民族 = BUNDAY odatga ega xalq.",blankNo="20",expl="このような = bunday, shunaqa (yaqinda aytilganga ishora)"),
         q("t6-g3-21",None,["まずは ／ 最初に","まずは ／ 最後に","最初に ／ まずは","最後に ／ まずは"],3,
           "21-a [最初に]…第二に…第三に…21-b [まずは] = ro'yxatni 最初に boshlab sanaydi.",blankNo="21",expl="最初に = avvalo/birinchi (a-o'rin); ro'yxat: 最初に・第二に・第三に"),
         q("t6-g3-22",None,["慣れてつつあります","慣れてつついます","慣れつつあります","慣れつついます"],3,
           "今では銭湯にも[慣れつつあります] = endi ko'nikib boryapman.",blankNo="22",expl="〜つつある = asta-sekin ...ib bormoqda. ます-shakl: 慣れ+つつある"),
         q("t6-g3-23",None,["限りでしょうか","どころでしょうか","上でしょうか","ことでしょうか"],4,
           "「日本人」に近づいてきたという[ことでしょうか] = ...ga yaqinlashganim shu bo'lsa kerak.",blankNo="23",expl="〜ということでしょうか = ...degani shudir/shu bo'lsa kerak (yumshoq xulosa)"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test06.json yozildi. Jami savol:", tot)
