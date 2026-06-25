# -*- coding: utf-8 -*-
"""test11.json — 第11回 模擬テスト (PDF betlari 108-117, javob 204)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test11.json")

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
  "id": 11, "title_jp": "第11回 模擬テスト", "title_uz": "11-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t11-v1-1","天気がいいので、洗たく物がよく【乾いた】。",["ひらいた","うごいた","みがいた","かわいた"],4,"Havo yaxshi bo'lgani uchun kir yaxshi quridi.",reading="かわいた",expl="乾く → かわく (qurimoq)"),
         q("t11-v1-2","この道がとなりの市との【境界】です。",["きょかい","きょうかい","きょがい","きょうがい"],2,"Bu yo'l qo'shni shahar bilan chegara.",reading="きょうかい",expl="境界 → きょうかい (chegara)"),
         q("t11-v1-3","【以後】は、別々に行動しましょう。",["いこ","いこう","いご","いごう"],3,"Bundan keyin alohida harakat qilaylik.",reading="いご",expl="以後 → いご (bundan keyin, keyinchalik)"),
         q("t11-v1-4","もえないごみを土に【埋めて】はいけません。",["こめて","ためて","とめて","うめて"],4,"Yonmaydigan axlatni tuproqqa ko'mish mumkin emas.",reading="うめて",expl="埋める → うめる (ko'mmoq)"),
         q("t11-v1-5","【例】をあげて説明してください。",["え","れい","ず","けん"],2,"Misol keltirib tushuntiring.",reading="れい",expl="例 → れい (misol)"),
         q("t11-v1-6","美しい【風景】が広がっている。",["ふうけい","ふうげい","ふけい","ふげい"],1,"Go'zal manzara yoyilib yotibdi.",reading="ふうけい",expl="風景 → ふうけい (manzara, ko'rinish)"),
         q("t11-v1-7","甘いものは【骨】によくない。",["こつ","ごつ","ほね","ぼね"],3,"Shirinlik suyak uchun yaxshi emas.",reading="ほね",expl="骨 → ほね (suyak)"),
         q("t11-v1-8","ある人から【奇妙】な話を聞いた。",["びりょう","びみょう","きちょう","きみょう"],4,"Bir odamdan g'alati gap eshitdim.",reading="きみょう",expl="奇妙 → きみょう (g'alati, ajabtovur)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t11-v2-9","【しぜん】の中で運動するのは、気持ちがよい。",["仕然","事然","自然","私然"],3,"Tabiat qo'ynida sport qilish yoqimli.",expl="しぜん → 自然 (tabiat)"),
         q("t11-v2-10","【きょうじゅ】の指導のもとで、論文を書いた。",["教師","教示","教受","教授"],4,"Professor rahbarligida ilmiy ish yozdim.",expl="きょうじゅ → 教授 (professor)"),
         q("t11-v2-11","この川は、あの川より【あさい】。",["深い","浅い","太い","細い"],2,"Bu daryo u daryodan sayozroq.",expl="あさい → 浅い (sayoz)"),
         q("t11-v2-12","この木は、冬に【かれて】しまう。",["枝れて","朽れて","枯れて","相れて"],3,"Bu daraxt qishda qurib qoladi.",expl="かれる → 枯れる (qurimoq — o'simlik)"),
         q("t11-v2-13","自分の考えを【しゅちょう】する。",["手長","手張","主長","主張"],4,"O'z fikrini qat'iy bildiraman (talab qilaman).",expl="しゅちょう → 主張 (qat'iy fikr bildirish, da'vo)"),
         q("t11-v2-14","コンサートホールに【おおぜい】の人が集まった。",["大勢","多勢","大盛","多盛"],1,"Konsert zaliga ko'p odam yig'ildi.",expl="おおぜい → 大勢 (ko'p odam, anchagina)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t11-v3-15","デジカメの写真の（　）をコンピューターに保存してください。",["マウス","キーボード","カバー","データ"],4,"Raqamli kamera suratlari ma'lumotini kompyuterga saqlang.",expl="データ = ma'lumot, data"),
         q("t11-v3-16","友だちから、メールの（　）が来ないので、心配だ。",["電信","配布","返信","到着"],3,"Do'stimdan elektron xat javobi kelmagani uchun xavotirdaman.",expl="返信 = javob (xat/xabarga)"),
         q("t11-v3-17","ヨーロッパの歴史あるホテルに（　）しました。",["滞在","存在","停留","停滞"],1,"Yevropaning tarixiy mehmonxonasida turdim (yashadim).",expl="滞在 = vaqtincha turish, qolish"),
         q("t11-v3-18","自転車を（　）、前へ進む。",["おして","こいで","にぎって","とめて"],2,"Velosiped pedalini bosib (haydab), oldinga yuraman.",expl="(自転車を)こぐ = pedal bosmoq, velosiped haydamoq"),
         q("t11-v3-19","テストに向けて（　）の準備をした。",["全長","全盛","万人","万全"],4,"Testga to'liq (mukammal) tayyorgarlik ko'rdim.",expl="万全 = to'la-to'kis, mukammal (tayyorgarlik)"),
         q("t11-v3-20","オレンジを（　）、ジュースを作る。",["ぬって","かんで","こんで","しぼって"],4,"Apelsinni siqib, sharbat tayyorlayman.",expl="しぼる = siqmoq, siqib olmoq"),
         q("t11-v3-21","（　）を取りながら、発表を聞いてください。",["レポート","メモ","ペーパー","ディベート"],2,"Qayd (eslatma) olib turib, taqdimotni tinglang.",expl="メモを取る = qayd qilmoq, eslatma yozmoq"),
         q("t11-v3-22","私の夢は、3階（　）の家に住むことです。",["作り","建て","重ね","乗せ"],2,"Mening orzuim — 3 qavatli uyda yashash.",expl="〜階建て = ...qavatli (bino)"),
         q("t11-v3-23","私は、2人の意見を聞いて、彼の意見が正しいと（　）した。",["行","成立","判断","実現"],3,"Men ikki kishining fikrini eshitib, uning fikri to'g'ri deb hukm qildim (qaror qildim).",expl="判断 = hukm, baho, qaror"),
         q("t11-v3-24","髪を短く切って、（　）した気分になった。",["すっきり","こっそり","すっかり","たっぷり"],1,"Sochni kalta qildirib, yengillashgan (tetik) holatga keldim.",expl="すっきりする = yengil tortmoq, tiniqlashmoq"),
         q("t11-v3-25","新しい仕事についたばかりで、少し（　）だ。",["不正","不安","不運","不明"],2,"Yangi ishga endi kirganim uchun, biroz xavotirdaman.",expl="不安 = xavotir, tashvish, bezovtalik"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t11-v4-26","あなたに、本当に【すまない】と思います。",["相談したい","会いたい","もうしわけない","何もしたくない"],3,"Sizdan rostdan ham uzr so'rayman (afsusdaman).",expl="すまない = kechirasiz, uzr → もうしわけない"),
         q("t11-v4-27","土曜日はデートなので、とても【わくわく】しています。",["幸せになって","楽しみにして","緊張して","心配して"],2,"Shanba kuni uchrashuv, shuning uchun juda intiqman (kutaman).",expl="わくわくする = hayajon bilan kutmoq → 楽しみにして"),
         q("t11-v4-28","明日、予定が【重なって】しまいました。",["急に予定が入って","同時に予定が入って","大切な予定が入って","難しい予定が入って"],2,"Ertaga rejalar bir-birining ustiga tushib qoldi.",expl="予定が重なる = rejalar to'qnash kelmoq → 同時に予定が入って"),
         q("t11-v4-29","休みがとれず、【ダウンして】しまった。",["けがして","眠って","逃げて","倒れて"],4,"Dam ololmay, holdan toyib (yiqilib) qoldim.",expl="ダウンする = holdan toymoq, yiqilmoq → 倒れて"),
         q("t11-v4-30","机の上が【ごちゃごちゃ】なので、かたづけてください。",["汚い","せまい","くさい","黒い"],1,"Stol usti tartibsiz (alag'-chalag') bo'lgani uchun, yig'ishtiring.",expl="ごちゃごちゃ = tartibsiz, alag'-chalag' → 汚い"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t11-v5-31","つぶれる",["強い風で、その木はまん中からつぶれてしまった。","急に雨がつぶれ、急いで近くのお店に入った。","先日の大きな地震で、たくさんの家がつぶれた。","前から使っていた時計がつぶれて、動かなくなった。"],3,
           "つぶれる(潰れる) = ezilmoq, qulamoq, vayron bo'lmoq.",optsTr=["Kuchli shamoldan o'sha daraxt o'rtasidan 'ezildi' (noto'g'ri — 折れる kerak).","To'satdan yomg'ir 'ezildi', do'konga kirdim (noto'g'ri — 降る kerak).","Yaqindagi katta zilzilada ko'p uy quladi (vayron bo'ldi). (to'g'ri)","Eski soat 'ezilib', ishlamay qoldi (noto'g'ri — 壊れる kerak)."]),
         q("t11-v5-32","増す",["台風のため、風の強さが増している。","1日3時間勉強したので、彼の日本語はいきなり増した。","社長に、給料を増してくださいとお願いした。","大学に入ってから、友だちが増してうれしい。"],1,
           "増す(ます) = ko'paymoq, kuchaymoq, ortmoq.",optsTr=["Tayfun tufayli shamol kuchi ortib boryapti. (to'g'ri)","Kuniga 3 soat o'qigani uchun, uning yaponchasi birdan 'ortdi' (noto'g'ri — 上達 kerak).","Rahbarga maoshni 'oshiring' deb so'radim (noto'g'ri — 上げる kerak).","Universitetga kirgach, do'stim 'ortib' xursandman (noto'g'ri — 増える kerak)."]),
         q("t11-v5-33","におい",["この料理は、おいしそうなにおいがする。","黒いにおいを見て、マンションの火事に気がついた。","昨晩は、となりの家の大きなにおいが聞こえてきた。","今朝はいい天気で、空にいくつか白いにおいが出ている。"],1,
           "におい = hid, is.",optsTr=["Bu taomdan mazali hid keladi. (to'g'ri)","Qora 'hid'ni ko'rib, yong'inni payqadim (noto'g'ri — 煙 kerak).","Kecha qo'shni uyning katta 'hidi' eshitildi (noto'g'ri — 音 kerak).","Bugun havo yaxshi, osmonda bir nechta oq 'hid' bor (noto'g'ri — 雲 kerak)."]),
         q("t11-v5-34","声",["車の声がうるさくて、テレビの音が聞こえない。","駅まで走ったら、声が切れてしまった。","風邪をひいて、きのうから声が止まらない。","もっと他人の声に耳をかたむけたほうがよい。"],4,
           "声(こえ) = ovoz (odam/jonzot tovushi).",optsTr=["Mashina 'ovozi' shovqinli, televizor eshitilmaydi (noto'g'ri — 音 kerak).","Bekatga yugursam, 'ovozim' uzilib qoldi (noto'g'ri — 息 kerak).","Shamollab, kechadan beri 'ovozim' to'xtamayapti (noto'g'ri — せき kerak).","Boshqalarning ovoziga (fikriga) ko'proq quloq solgan ma'qul. (to'g'ri)"]),
         q("t11-v5-35","あやしい",["今日は寒いので、あやしいものが食べたい。","帰宅すると、家の前にあやしい男が立っていた。","彼女は、親切であやしいので、みんなに人気がある。","この手帳は、なんでも書くことができて、とてもあやしい。"],2,
           "あやしい(怪しい) = shubhali, gumonli, g'alati.",optsTr=["Bugun sovuq, 'shubhali' narsa yegim keladi (noto'g'ri — あたたかい kerak).","Uyga qaytsam, uy oldida shubhali erkak turardi. (to'g'ri)","U mehribon va 'shubhali', hammaga yoqadi (noto'g'ri — やさしい kerak).","Bu daftarga hammasini yozsa bo'ladi, juda 'shubhali' (noto'g'ri — 便利 kerak)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t11-g1-1","台風が来て、昨日は沖縄では大雨だった（　）。",["のは","とを","のを","とか"],4,"Tayfun kelib, kecha Okinavada kuchli yomg'ir bo'libdi (deyishadi).",expl="〜とか = ...emish, ...deyishadi (eshitilgan, noaniq)"),
         q("t11-g1-2","妻「明日からたばこを吸うのをやめてちょうだい。」夫「（　）厳しいことを言わないでよ。」",["こんなに","そんなに","あんなに","どんなに"],2,"Xotin: «Ertadan tamaki chekishni tashla.» Er: «Unaqa qattiq gaplarni aytma-da.»",expl="そんなに = unaqa, shunaqa (suhbatdosh aytganiga ishora)"),
         q("t11-g1-3","私は昨日から風邪（　）で、熱が少しある。",["っぱい","ほど","げ","気味"],4,"Men kechadan beri shamollaganga o'xshab, ozroq isitmam bor.",expl="〜気味 = ...ga moyil, ...nishonasi bor. 風邪気味 = shamollaganga o'xshash"),
         q("t11-g1-4","近所へ散歩に行った（　）、スーパーで牛乳を買ってきました。",["かたがた","ついでに","かわりに","ままに"],2,"Yaqin atrofga sayrga borgan paytim, zaodan sut ham olib keldim.",expl="〜ついでに = ...gan paytda birga, zayli bilan"),
         q("t11-g1-5","学校から家へ帰る（　）彼女に会ったので、道で少し話しました。",["途中まで","途中へ","途中で","途中から"],3,"Maktabdan uyga qaytayotib yo'lda uni uchratdim, ko'chada ozroq gaplashdik.",expl="〜途中で = ...yo'lda, ...yo'l-yo'lakay"),
         q("t11-g1-6","この町は、駅を（　）発展してきた。",["中心とともに","中心として","中心において","中心にかけて"],2,"Bu shahar bekatni markaz qilib rivojlanib kelgan.",expl="〜を中心として = ...ni markaz qilib, ...atrofida"),
         q("t11-g1-7","毎朝私は、ベランダの花に水を（　）。",["くれます","もらいます","やります","さしあげます"],3,"Har kuni ertalab men balkondagi gullarga suv quyaman (beraman).",expl="やる = (pastga/o'simlik-hayvonga) bermoq. 水をやる = suv quymoq"),
         q("t11-g1-8","彼女に会うのは、卒業以来3年（　）。",["よりだ","ながらだ","からだ","ぶりだ"],4,"Uni ko'rishim — bitirganimdan beri 3 yildan keyin (3 yil o'tib).",expl="〜ぶり = ...dan keyin (vaqt o'tib qaytadan). 3年ぶり = 3 yildan keyin"),
         q("t11-g1-9","弟は先生に何と（　）。",["お話しなさいましたか","話されましたか","おっしゃいましたか","申しましたか"],4,"Ukam o'qituvchiga nima dedi?",expl="申す = 言う ning kamtarlik shakli (ukam — o'z guruh a'zosi). 申しましたか"),
         q("t11-g1-10","あの子は、小さい子ども（　）、とてもかしこい。",["にしては","のあまり","であるからには","からして"],1,"U bola kichkina bola bo'lishiga qaramay, juda aqlli.",expl="〜にしては = ...ga qaraganda (kutilganidan farqli)"),
         q("t11-g1-11","男の学生「ペンを忘れちゃった。」女の学生「私（　）、これを使ってよ。」",["のもよければ","のでよければ","がよいから","でよいから"],2,"O'g'il bola: «Ruchkamni unutibman.» Qiz bola: «Meniki bo'lsa ham bo'lsa, mana buni ishlat.»",expl="〜でよければ = ...bo'lsa ham bo'lsa, ...rozimisan. 私の(ペン)でよければ"),
         q("t11-g1-12","あまり時間がないから、食事を（　）、簡単なものにするつもりだ。",["するとしては","するとしようと","するとしても","するとしようなら"],3,"Vaqt kam, shuning uchun ovqatlansak ham, oddiy narsa qilmoqchiman.",expl="〜としても = ...sa ham, ...bo'lgan taqdirda ham"),
         q("t11-g1-13","私はアイスクリームが大好きなので、お店で見かけると（　）。",["買おうとしています","買おうとはしません","買わないでいられます","買わないではいられません"],4,"Men muzqaymoqni juda yaxshi ko'raman, shuning uchun do'konda ko'rsam, sotib olmay turolmayman.",expl="〜ないではいられない = ...masdan turolmaslik (chiday olmay qilib qo'yish)"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t11-g2-14",None,["反して","予想に","人々の","多くの"],2,"To'g'ri jumla: «Kechagi o'yin ko'pchilik odamlarning bashoratiga zid ravishda A jamoa yutdi.»",
           prefix="きのうのゲームは",suffix="Aチームが勝った。",starPos=3,order=[4,3,2,1],expl="To'g'ri tartib: 多くの人々の予想に反して (〜に反して = ...ga zid)"),
         q("t11-g2-15",None,["ものですが","お菓子を","こちらの","いただいた"],3,"To'g'ri jumla: «Agar mayli bo'lsa, mana bu — menga berilgan shirinlikdan, oling.»",
           prefix="よろしければ、",suffix="どうぞ。",starPos=3,order=[4,1,3,2],expl="To'g'ri tartib: いただいたものですがこちらのお菓子を (いただく = «olmoq» kamtarlik)"),
         q("t11-g2-16",None,["会議で","かまわない","進めても","決まったように"],3,"To'g'ri jumla: «Demak, bu loyihani o'tgan kungi yig'ilishda hal qilingandek davom ettirsak bo'ladimi?»",
           prefix="では、このプロジェクトは、先日の",suffix="でしょうか。",starPos=3,order=[1,4,3,2],expl="To'g'ri tartib: 会議で決まったように進めてもかまわない"),
         q("t11-g2-17",None,["一方","なる","前より","下手に"],2,"To'g'ri jumla: «Ilgari har kuni pianino mashq qilardim, lekin yaqinda qilmayapman, shuning uchun avvalgidan yomonlashib boryapman.»",
           prefix="以前は毎日ピアノの練習をしていましたが、最近はしていないので、",suffix="です。",starPos=3,order=[3,4,2,1],expl="To'g'ri tartib: 前より下手になる一方 (〜一方だ = tobora ...bo'lib bormoqda)"),
         q("t11-g2-18",None,["なんと","土地を","争いは","めぐる"],4,"To'g'ri jumla: «O'sha qishloq aholisining yer ustidagi janjali nima-niki, o'nlab yillar davom etdi.»",
           prefix="その村の人たちの",suffix="数十年間も続いた。",starPos=2,order=[2,4,3,1],expl="To'g'ri tartib: 土地をめぐる争いはなんと (〜をめぐる = ...yuzasidan, ...haqidagi)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "富士山のこと（張拓）",
       "passage": (
         "土曜、日曜日に、日本に来て初めて、富士山に行きました。日本に来る前は、日本のイメージを"
         "代表するものは富士山でした。富士山に{{19}}、前の日の夜はうれしくて、よく眠れませんでした。\n"
         "私が友だちと一緒に参加したツアーは、朝早くバスで出発し、まずバスで五合目まで行き、その後、"
         "ガイドさんに従って、八合目までのぼり、山小屋にとまって、次の日の朝、頂上を目指すというものです。"
         "とても天気がよかったので、頂上で「ご来光」と呼ばれる朝日を{{20}}。本当にきれいでした。\n"
         "ただ、残念だったのは、ごみがたくさん捨てられていたことです。{{21}}、友だちと下りるときに"
         "ごみを拾うことにしました。もっていた袋に、見つけたごみを入れていくと、五合目に戻るころには、"
         "ごみ袋がいっぱいでした。遠くから見るとあんなに{{22a}}富士山も、実際はこんなに{{22b}}ことが"
         "わかって、悲しい気持ちになりました。ガイドさんも、富士山のごみは問題になっている、と言っていました。\n"
         "帰ってきてから、パソコンで{{23}}、山を登りながらごみを拾うツアーもあるようです。"
         "富士山をきれいにするために、今度はこのようなツアーに参加したいと思いました。"
       ),
       "passage_tr": (
         "Shanba-yakshanba kunlari, Yaponiyaga kelganimdan beri birinchi marta Fuji tog'iga bordim. "
         "Yaponiyaga kelishimdan oldin, Yaponiya obrazini eng yaxshi ifodalovchi narsa — Fuji tog'i edi. "
         "Fuji tog'iga CHIQA OLAMAN deb o'ylaganimdan, oldingi kechasi xursandligimdan yaxshi uxlay olmadim. "
         "Do'stim bilan qatnashgan turimiz ertalab erta avtobusda jo'nab, avval avtobusda 5-bekatgacha "
         "borib, so'ng gid ortidan 8-bekatgacha chiqib, tog' kulbasida tunab, ertasi ertalab cho'qqini "
         "ko'zlash edi. Havo juda yaxshi bo'lgani uchun, cho'qqida «goraikou» deb ataladigan tong quyoshini "
         "KO'RA OLDIK. Rostdan ham go'zal edi. "
         "Faqat, afsuski, juda ko'p axlat tashlangani edi. SHUNING UCHUN, do'stim bilan tushayotganda axlat "
         "terishga qaror qildik. Olib yurgan xaltamizga topgan axlatni solib borib, 5-bekatga qaytar "
         "chog'imizda axlat xaltasi to'lib ketgandi. Uzoqdan qaraganda shunchalik GO'ZAL ko'rinadigan Fuji "
         "aslida shunchalik IFLOSLANGANini bilib, hafa bo'ldim. Gid ham Fuji axlati muammoga aylangan deb "
         "aytdi. "
         "Qaytib kelgach, kompyuterdan QIDIRIB KO'RGANIMDA, tog'ga chiqa turib axlat teradigan turlar ham "
         "bor ekan. Fujini toza qilish uchun, keyingi safar shunday turga qatnashmoqchiman."
       ),
       "questions": [
         q("t11-g3-19",None,["登れると思うと","登れたと思うと","登れたと思ったら","登れと思ったら"],1,
           "富士山に[登れると思うと]、前の日…眠れませんでした = Fujiga CHIQA OLAMAN deb o'ylasam, oldingi kechasi uxlay olmadim.",blankNo="19",expl="〜と思うと = ...deb o'ylasa (...ni o'ylab hayajon). 登れる = chiqa olish"),
         q("t11-g3-20",None,["見られそうでした","見ることでした","見ることができました","見たいと思いました"],3,
           "朝日を[見ることができました] = tong quyoshini KO'RA OLDIK.",blankNo="20",expl="〜ことができる = ...a olmoq (imkoniyat). 見ることができました"),
         q("t11-g3-21",None,["ところで","そこで","ところが","それが"],2,
           "ごみが…捨てられていた。[そこで]、ごみを拾うことにしました = axlat tashlangan. SHUNING UCHUN, axlat terishga qaror qildik.",blankNo="21",expl="そこで = shuning uchun, shu sababli (harakatga o'tish)"),
         q("t11-g3-22",None,["きたない ／ よごれている","きたない ／ よごれていない","きれいな ／ よごれていない","きれいな ／ よごれている"],4,
           "遠くからあんなに[きれいな]富士も、実際はこんなに[よごれている] = uzoqdan GO'ZAL, aslida IFLOSLANGAN.",blankNo="22",expl="22-a きれいな (go'zal) ↔ 22-b よごれている (ifloslangan) — qarama-qarshilik"),
         q("t11-g3-23",None,["調べるものの","調べようと","調べるにしたら","調べたところ"],4,
           "パソコンで[調べたところ]、ツアーもあるようです = kompyuterdan QIDIRIB KO'RGANIMDA, turlar ham bor ekan.",blankNo="23",expl="〜たところ = ...gan paytda, ...gach (ma'lum bo'ldi)"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test11.json yozildi. Jami savol:", tot)
