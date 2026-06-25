# -*- coding: utf-8 -*-
"""test09.json — 第9回 模擬テスト (PDF betlari 88-97, javob 202)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test09.json")

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
  "id": 9, "title_jp": "第9回 模擬テスト", "title_uz": "9-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t9-v1-1","パーティーを開くので、部屋をきれいに【飾って】おく。",["ぬって","しまって","かざって","あらって"],3,"Ziyofat o'tkazaman, shuning uchun xonani chiroyli bezab qo'yaman.",reading="かざって",expl="飾る → かざる (bezamoq)"),
         q("t9-v1-2","材料は、【各自】で用意してください。",["かくし","かくじ","きゃくし","きゃくじ"],2,"Materiallarni har kim o'zi tayyorlasin.",reading="かくじ",expl="各自 → かくじ (har kim o'zi, har biri)"),
         q("t9-v1-3","ここが世界一大きな【湖】です。",["みずうみ","いけ","ぬま","たき"],1,"Bu yer dunyodagi eng katta ko'l.",reading="みずうみ",expl="湖 → みずうみ (ko'l)"),
         q("t9-v1-4","家の外で猫が【鳴いて】いる。",["きいて","たたいて","ないて","さいて"],3,"Uy tashqarisida mushuk miyovlayapti.",reading="ないて",expl="鳴く → なく (sayramoq, miyovlamoq — hayvon ovozi)"),
         q("t9-v1-5","【屋上】から町がよく見えます。",["やしょう","やじょう","おくしょう","おくじょう"],4,"Tomdan shahar yaxshi ko'rinadi.",reading="おくじょう",expl="屋上 → おくじょう (tom, bino usti)"),
         q("t9-v1-6","ここを車が【通過】することはできません。",["つうか","つうが","とうか","とうが"],1,"Bu yerdan mashina o'tib keta olmaydi.",reading="つうか",expl="通過 → つうか (o'tib ketish)"),
         q("t9-v1-7","きのうからずっと【歯】が痛い。",["ば","は","し","じ"],2,"Kechadan beri tishim og'riyapti.",reading="は",expl="歯 → は (tish)"),
         q("t9-v1-8","大きな車輪が【回転】する。",["てんかい","てんがい","かいてん","かいでん"],3,"Katta g'ildirak aylanadi.",reading="かいてん",expl="回転 → かいてん (aylanish)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t9-v2-9","やり方は、【きそく】で決まっています。",["基則","規則","基測","規測"],2,"Tartib qoida bilan belgilangan.",expl="きそく → 規則 (qoida, tartib)"),
         q("t9-v2-10","あの2人の【ゆうじょう】は、すばらしい。",["有情","愛情","友情","真情"],3,"U ikki kishining do'stligi ajoyib.",expl="ゆうじょう → 友情 (do'stlik)"),
         q("t9-v2-11","赤ちゃんにセーターとマフラーを【あんだ】。",["編んだ","練んだ","絡んだ","結んだ"],1,"Chaqaloqqa sviter va sharf to'qidim.",expl="あむ → 編む (to'qimoq)"),
         q("t9-v2-12","わが社では、大事なことは【おもに】社長が決める。",["重に","面に","主に","思に"],3,"Bizning kompaniyada muhim narsalarni asosan rahbar hal qiladi.",expl="おもに → 主に (asosan, ko'pincha)"),
         q("t9-v2-13","仕事についての新しい【ちしき】を得た。",["意識","認識","常識","知識"],4,"Ish haqida yangi bilim oldim.",expl="ちしき → 知識 (bilim)"),
         q("t9-v2-14","犬と猫の【せわ】をする。",["世和","施和","世話","施話"],3,"It va mushukni parvarish qilaman.",expl="せわ → 世話 (parvarish, qarash)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t9-v3-15","がんばれば、私にも（　）はあると思います。",["トップ","ベスト","チェンジ","チャンス"],4,"Harakat qilsam, menda ham imkoniyat bor deb o'ylayman.",expl="チャンス = imkoniyat, fursat"),
         q("t9-v3-16","人を年齢などによって（　）してはいけない。",["別離","差別","対立","分別"],2,"Odamni yoshi va shu kabilarga qarab kamsitmaslik kerak.",expl="差別 = kamsitish, ajratish"),
         q("t9-v3-17","1日の仕事の内容を必ず上司に（　）してください。",["出席","結論","移転","報告"],4,"Kunlik ish mazmunini albatta boshliqqa hisobot qiling.",expl="報告 = hisobot, ma'lumot berish"),
         q("t9-v3-18","彼は、この町を（　）行ってしまった。",["拾って","去って","終えて","投げて"],2,"U bu shaharni tark etib ketib qoldi.",expl="去る = ketmoq, tark etmoq"),
         q("t9-v3-19","レポートを専門（　）にきちんとチェックしてもらってください。",["員","者","家","屋"],3,"Hisobotni mutaxassisga yaxshilab tekshirtiring.",expl="専門家 = mutaxassis (〜家 = ...shunos, kasb egasi)"),
         q("t9-v3-20","大きなバケツに水を（　）ください。",["ためて","のせて","置いて","投げて"],1,"Katta chelakka suv to'plang (yig'ing).",expl="ためる = to'plamoq, jamlamoq (suyuqlik)"),
         q("t9-v3-21","事故のニュースを聞いて、（　）を受けた。",["ダウン","チャレンジ","マイナス","ショック"],4,"Halokat xabarini eshitib, shok bo'ldim.",expl="ショックを受ける = shokka tushmoq"),
         q("t9-v3-22","出発する日、（　）にたくさんの人が来てくれた。",["見返し","見知り","見聞き","見送り"],4,"Jo'nash kunim kuzatgani ko'p odam keldi.",expl="見送り = kuzatish, kuzatib qo'yish"),
         q("t9-v3-23","先生に会ったので、（　）した。",["応援","指導","挨拶","尊重"],3,"O'qituvchini uchratganim uchun salomlashdim.",expl="挨拶 = salomlashish, ko'rishish"),
         q("t9-v3-24","その晩、私は、暖かいベッドで（　）眠った。",["あっさり","ぐっすり","さっぱり","ぐったり"],2,"O'sha kechasi men issiq karavotda qotib (maza qilib) uxladim.",expl="ぐっすり眠る = qotib uxlamoq, maza qilib uxlamoq"),
         q("t9-v3-25","このような（　）な資料をいただき、ありがとうございます。",["丈夫","貴重","地味","派手"],2,"Bunday qimmatli (qadrli) hujjatni berganingiz uchun rahmat.",expl="貴重 = qimmatli, qadrli, noyob"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t9-v4-26","彼女と家の近くで【再会】した。",["待ち合わせた","また会った","別れた","約束した"],2,"U bilan uy yaqinida qayta uchrashdim.",expl="再会 = qayta uchrashish → また会った"),
         q("t9-v4-27","子どもを見ていると、【はらはら】する。",["心配だ","幸福だ","期待する","感動する"],1,"Bolaga qarab tursam, yuragim hapriqadi (xavotirlanaman).",expl="はらはらする = hapriqmoq, xavotirlanmoq → 心配だ"),
         q("t9-v4-28","木村は、今、【席をはずして】おります。",["そうじして","とりかえて","離れて","戻ってきて"],3,"Kimura hozir joyida yo'q (joyidan uzoqlashgan).",expl="席をはずす = joyini bo'shatmoq, o'rnida bo'lmaslik → 離れて"),
         q("t9-v4-29","このホテルは【アクセス】がいい。",["目立つところにある","地図にのっている","とても人気がある","交通が便利だ"],4,"Bu mehmonxonaga borish qulay (transport qulay).",expl="アクセスがいい = borish qulay → 交通が便利だ"),
         q("t9-v4-30","あの人は【正直】な人だ。",["うそをつかない","とても優しい","勉強ができる","他人にきびしい"],1,"U odam halol (rostgo'y) odam.",expl="正直 = halol, rostgo'y → うそをつかない"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t9-v5-31","つつむ",["テントがとばされないように、ロープでつつんだ。","これはプレゼントなので、きれいな紙でつつんでください。","やぶれた紙をセロテープでつつみました。","雪が山の頂上をつつんでいる。"],2,
           "つつむ(包む) = o'ramoq, o'rab qo'ymoq.",optsTr=["Chodir uchib ketmasin deb, arqon bilan 'o'radim' (noto'g'ri — しばる kerak).","Bu sovg'a, shuning uchun chiroyli qog'ozga o'rang. (to'g'ri)","Yirtilgan qog'ozni skotch bilan 'o'radim' (noto'g'ri — はる kerak).","Qor tog' cho'qqisini 'o'rab' turibdi (noto'g'ri — おおう kerak)."]),
         q("t9-v5-32","こぼす",["急いでいたので、持っていたかばんをこぼしてしまった。","時計を床に落としたらこぼしてしまった。","電車の中にさいふをこぼしてしまい、後で取りに行った。","シャツにコーヒーをこぼしたので、すぐに着替えた。"],4,
           "こぼす = to'kib yubormoq (suyuqlik/donador).",optsTr=["Shoshganim uchun, ko'tarib turgan sumkani 'to'kib yubordim' (noto'g'ri — 落とす kerak).","Soatni polga tushirsam 'to'kildi' (noto'g'ri — 壊れる kerak).","Poyezdda hamyonni 'to'kib', keyin olgani bordim (noto'g'ri — 忘れる kerak).","Ko'ylakka kofe to'kib yuborganim uchun, darrov kiyim almashtirdim. (to'g'ri)"]),
         q("t9-v5-33","角",["部屋の角に植木が置いてあります。","橋のまん中ではなく、角を渡ってください。","転んだとき、テーブルの角で頭を打って、とても痛かった。","その書類は、机の角に入っています。"],3,
           "角(かど) = burchak, qirra (chiqib turgan).",optsTr=["Xona burchagiga (隅) tuvak qo'yilgan (noto'g'ri — 隅 kerak).","Ko'prik o'rtasidan emas, 'burchakdan' o'ting (noto'g'ri).","Yiqilganimda stol qirrasiga boshimni urib, juda og'ridi. (to'g'ri)","U hujjat stolning 'burchagiga' solingan (noto'g'ri — 引き出し kerak)."]),
         q("t9-v5-34","相手",["台所のテーブルの相手として、このいすを買いました。","天気のいい日には、公園にたくさん相手が歩いている。","さっきの電話の相手は、国の母親です。","からい料理は、ごはんの相手にちょうどいい。"],3,
           "相手(あいて) = suhbatdosh, qarama-qarshi tomon, sherik.",optsTr=["Oshxona stolining 'sherigi' sifatida bu stulni oldim (noto'g'ri).","Havo yaxshi kunlari bog'da ko'p 'sherik' yuradi (noto'g'ri — 人 kerak).","Hozirgi telefondagi suhbatdosh — yurtimdagi onam. (to'g'ri)","Achchiq taom guruchga 'sherik' bo'ladi (noto'g'ri — あう kerak)."]),
         q("t9-v5-35","夢中",["彼は、自分の仕事に夢中で取り組んでいる。","今朝は9時まで夢中で、目が覚めませんでした。","寝不足のまま、夢中で運転するのは危ないです。","試合に勝ったあとには、夢中で練習しないでください。"],1,
           "夢中 = berilib ketgan, qiziqib ketgan, mahliyo.",optsTr=["U o'z ishiga berilib ishlayapti. (to'g'ri)","Bugun ertalab 9 gacha 'berilib', uyg'onmadim (noto'g'ri — ぐっすり kerak).","Uyqusiz holda 'berilib' haydash xavfli (noto'g'ri — ぼんやり kerak).","O'yinda yutgandan keyin, 'berilib' mashq qilmang (noto'g'ri)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t9-g1-1","みんなが私の意見に反対していたが、彼女（　）応援してくれた。",["だけは","だけなら","だけに","だけど"],1,"Hamma mening fikrimga qarshi edi, lekin u (yolg'iz o'zi) qo'llab-quvvatladi.",expl="〜だけは = ...gina (ajratib ta'kidlash). 彼女だけは = u yolg'iz"),
         q("t9-g1-2","すみません、博物館へは（　）行けばいいか、教えてください。",["どう","どんなに","こう","こんなに"],1,"Kechirasiz, muzeyga qanday borsam bo'lishini ayting.",expl="どう = qanday (usul haqida savol)"),
         q("t9-g1-3","駅に着き（　）、電話をかけてください。",["通りに","しだい","ばかりに","とたん"],2,"Bekatga yetishingiz bilan, telefon qiling.",expl="動詞ます形+しだい = ...ishi bilanoq, darhol"),
         q("t9-g1-4","空に雲がたくさん出ているので、（　）雨が降るかもしれません。",["もしも","もしかしたら","もし","もはや"],2,"Osmonda bulut ko'p, shuning uchun ehtimol yomg'ir yog'ar.",expl="もしかしたら〜かもしれない = ehtimol ...bo'lishi mumkin"),
         q("t9-g1-5","あなたは、今までアメリカへ（　）ことがありますか。",["行き","行った","行くの","行ったの"],2,"Siz shu paytgacha Amerikaga borganmisiz?",expl="〜たことがある = ...gan tajriba bor (...ganmisiz)"),
         q("t9-g1-6","明日の勝負で優勝できるか決まるので、負ける（　）。",["わけではない","わけにはいかない","ことではない","ことにはいかない"],2,"Ertangi o'yinda g'olib bo'lish hal bo'ladi, shuning uchun yutqazib bo'lmaydi.",expl="〜わけにはいかない = ...ishning iloji yo'q (axloqiy/vaziyat majburiyati)"),
         q("t9-g1-7","テレビを5時間（　）つづけて、目が痛くなりました。",["見られ","見えて","見せた","見"],4,"Televizorni 5 soat ko'raverib, ko'zim og'rib qoldi.",expl="動詞ます形+つづける = ...ishda davom etmoq. 見+つづける"),
         q("t9-g1-8","私がこの国の首相（　）、政治をもっとよくするのに。",["だったからには","だったとしたら","にしたら","にしては"],2,"Agar men shu davlatning bosh vaziri bo'lganimda, siyosatni yaxshilagan bo'lardim.",expl="〜だったとしたら = agar ...bo'lganda (faraziy shart)"),
         q("t9-g1-9","明日、ひさしぶりの休みなので、町へ（　）思います。",["遊びに行くことに","遊びに行くのにしようと","遊びに行くほどだと","遊びに行こうと"],4,"Ertaga ko'pdan beri dam olish kunim, shuning uchun shaharga sayrga bormoqchiman.",expl="〜(よ)うと思う = ...moqchiman (niyat)"),
         q("t9-g1-10","お荷物の配送については、受付カウンターに（　）、お願いいたします。",["うかがってくださるよう","おたずねくださるよう","聞いてあげるよう","たずねてあげますよう"],2,"Yuk yetkazib berish bo'yicha, qabul stoliga murojaat qilishingizni so'raymiz.",expl="お〜くださる = (hurmat) siz ...qilishingizni. おたずねくださる = so'rashingiz"),
         q("t9-g1-11","この町には、バスも電車も通っていないのだから、（　）。",["歩くよりほかはある","歩くよりほかはない","歩くよりほかだ","歩くよりほかではない"],2,"Bu shaharda avtobus ham, poyezd ham yurmaydi, shuning uchun yurishdan boshqa iloj yo'q.",expl="〜よりほかはない = ...dan boshqa iloj yo'q"),
         q("t9-g1-12","この仕事は、とても大変そうに見えますが、がんばれば（　）と思います。",["ならないこともない","ならないこともある","できないこともない","できないこともある"],3,"Bu ish juda og'irday ko'rinadi, lekin harakat qilsa, qilsa bo'lmaydigan ish emas (eplasa bo'ladi).",expl="〜ないこともない = ...sa bo'ladi, eplasa bo'ladi (yumshoq imkon)"),
         q("t9-g1-13","明日は会社の面接に行く予定だ。絶対に遅刻（　）。",["するままにすると","しないようにすると","しないままにしないと","しないようにしないと"],4,"Ertaga kompaniya suhbatiga boraman. Mutlaqo kechikmaslikka harakat qilishim kerak.",expl="〜ないようにしないと = ...maslikka harakat qilishim kerak"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t9-g2-14",None,["できない","車の","ばかりに","運転が"],1,"To'g'ri jumla: «Oqibatda, mashina haydashni bilmaganim sababligina, yaxshi ish topilmadi.»",
           prefix="川本「それが結局、",suffix="、いいアルバイトが見つからなかったんだ。」",starPos=3,order=[2,4,1,3],expl="To'g'ri tartib: 車の運転ができないばかりに"),
         q("t9-g2-15",None,["て","教え","た","さしあげ"],4,"To'g'ri jumla: «Hozirgina o'qituvchiga zalga borish yo'lini o'rgatib bergan edim.»",
           prefix="ちょうど先生に、会場への行き方を",suffix="ところです。",starPos=3,order=[2,1,4,3],expl="To'g'ri tartib: 教えてさしあげたところ (〜てさしあげる = birovga qilib bermoq, kamtarona)"),
         q("t9-g2-16",None,["いるのは","ほうでは","間違って","あなたがたの"],4,"To'g'ri jumla: «Xulosa qilib aytsam, xato qilayotgani sizlar emasmikan deb o'ylayman.»",
           prefix="結論から言えば、",suffix="ないかと思います。",starPos=3,order=[3,1,4,2],expl="To'g'ri tartib: 間違っているのはあなたがたのほうでは"),
         q("t9-g2-17",None,["科学者","発明された","によって","機械は"],3,"To'g'ri jumla: «Bu yangi mashina olim tomonidan ixtiro qilingan narsadir.»",
           prefix="この新しい",suffix="ものです。",starPos=3,order=[4,1,3,2],expl="To'g'ri tartib: 機械は科学者によって発明された (〜によって = ...tomonidan)"),
         q("t9-g2-18",None,["資料に","かけて","もとづく","集めた"],1,"To'g'ri jumla: «Endi taqdim qiladigan mazmunim, 10 yildan ortiq sarflab to'plangan materialga asoslangan narsadir.»",
           prefix="これから発表する内容は、10年以上",suffix="ものだ。",starPos=3,order=[2,4,1,3],expl="To'g'ri tartib: かけて集めた資料にもとづく (〜にもとづく = ...ga asoslangan)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "新しいスタイルの雑誌",
       "passage": (
         "海外からやってきて、日本に住む人々の生活を紹介する雑誌、「Japanライフスタイル」が"
         "全国の書店で発売されました。\n"
         "これまで、新聞や雑誌などで、日本で生活する留学生たちや、日本で仕事をする外国の人々について"
         "簡単に紹介されることはありましたが、生活そのものをテーマとした雑誌が発行されるのは{{19}}ことです。\n"
         "表紙のデザインも明るく、楽しそうな雑誌です。たくさんのカラフルな写真やイラストを使って、"
         "彼らの生活の様子を生き生きと紹介しています。\n"
         "この雑誌は、毎月ではなく季刊{{20}}春、夏、秋、冬と、1年に4回発行される予定です。"
         "これまでは、インターネットで予約した読者に対し、通信販売のみを行ってきましたが、"
         "予想以上に売れ行きがよかったので、書店で売ることになった{{21}}。\n"
         "この雑誌を発売する出版社は、「この雑誌{{22}}、外国人たちがなやみや楽しみを、おたがいに"
         "聞いたり教えあったりして、彼らの日本での生活が少しでもよいものになればと思う。」と話しています。"
         "日本全国で行われる日本人との交流に関する情報も、{{23}}"
       ),
       "passage_tr": (
         "Chet eldan kelib Yaponiyada yashayotgan odamlarning hayotini tanishtiruvchi «Japan Lifestyle» "
         "jurnali butun mamlakat kitob do'konlarida sotuvga chiqdi. "
         "Shu paytgacha gazeta-jurnallarda Yaponiyada yashovchi chet ellik talabalar yoki ishlayotgan "
         "chet elliklar haqida qisqacha tanishtirilardi, biroq hayotning o'zini mavzu qilgan jurnal "
         "chiqarilishi JUDA KAM UCHRAYDIGAN hodisa. "
         "Muqova dizayni ham yorqin, quvnoq jurnal. Ko'plab rang-barang foto va rasmlardan foydalanib, "
         "ularning turmush tarzini jonli tasvirlaydi. "
         "Bu jurnal har oy emas, balki mavsumiy — YA'NI bahor, yoz, kuz, qish bo'lib, yiliga 4 marta "
         "chiqarilishi rejalashtirilgan. Shu paytgacha internet orqali oldindan buyurtma bergan "
         "o'quvchilarga faqat pochta orqali sotilardi, ammo kutilganidan ham yaxshi sotilgani uchun, "
         "kitob do'konlarida sotiladigan BO'LDI. "
         "Jurnalni chiqaruvchi nashriyot: «Bu jurnal ORQALI chet elliklar tashvish va quvonchlarini "
         "o'zaro so'rashib, o'rgatishib, ularning Yaponiyadagi hayoti ozgina bo'lsa-da yaxshilanса edi "
         "deb umid qilamiz», deydi. Yaponiya bo'ylab o'tkaziladigan yaponlar bilan muloqotга oid "
         "ma'lumotlarni ham TANISHTIRIB BORISH NIYATIDA EKAN."
       ),
       "questions": [
         q("t9-g3-19",None,["かなりよくある","ときどき見られる","きわめてまれな","ないこともない"],3,
           "生活そのものをテーマとした雑誌…[きわめてまれな]こと = hayotni mavzu qilgan jurnal JUDA KAM uchraydigan hodisa.",blankNo="19",expl="きわめてまれな = nihoyatda kam uchraydigan, juda noyob"),
         q("t9-g3-20",None,["ところで","つまり","しかし","それから"],2,
           "季刊[つまり]春夏秋冬…4回 = mavsumiy, YA'NI bahor-yoz-kuz-qish, 4 marta.",blankNo="20",expl="つまり = ya'ni, demak (izohlash)"),
         q("t9-g3-21",None,["というわけです","ものがあります","どころではありません","というばかりです"],1,
           "書店で売ることになった[というわけです] = kitob do'konida sotiladigan bo'ldi, MANA SHUNDAY.",blankNo="21",expl="〜というわけです = ...mana shunday/shu sababdan (xulosa-izoh)"),
         q("t9-g3-22",None,["にとって","に際して","につれて","を通じて"],4,
           "この雑誌[を通じて]…聞いたり教えあったり = bu jurnal ORQALI o'zaro so'rashib, o'rgatishib.",blankNo="22",expl="〜を通じて = ...orqali, ...vositasida"),
         q("t9-g3-23",None,["紹介するおそれがあるのです","紹介していきかねません","紹介していくつもりだそうです","紹介するかのようです"],3,
           "情報も[紹介していくつもりだそうです] = ma'lumotlarni ham tanishtirib borish NIYATIDA EKAN.",blankNo="23",expl="〜つもりだそうです = ...moqchi ekan (eshitilgan niyat)"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test09.json yozildi. Jami savol:", tot)
