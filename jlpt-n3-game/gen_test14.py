# -*- coding: utf-8 -*-
"""test14.json — 第14回 模擬テスト."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test14.json")

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
  "id": 14, "title_jp": "第14回 模擬テスト", "title_uz": "14-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t14-v1-1","その船は、太平洋に【沈んで】しまった。",["およんで","ころんで","きしんで","しずんで"],4,"U kema Tinch okeaniga cho'kib ketdi.",reading="しずんで",expl="沈む → しずむ (cho'kmoq, botmoq)"),
         q("t14-v1-2","彼はとても【幸運】な人だ。",["ごうん","ごううん","こうん","こううん"],4,"U juda baxtli odam.",reading="こううん",expl="幸運 → こううん (baxt, omad)"),
         q("t14-v1-3","いつもより遅く【昼食】をとった。",["ちゅうしょく","ちょうしょく","ちゅうじょく","ちょうじょく"],1,"Odatdagidan kechroq tushlik qildim.",reading="ちゅうしょく",expl="昼食 → ちゅうしょく (tushlik)"),
         q("t14-v1-4","川にたくさんのごみが【浮いて】いる。",["おいて","わいて","ういて","ついて"],3,"Daryoda juda ko'p axlat suzib yuradi.",reading="ういて",expl="浮く → うく (suzmoq, qalqmoq)"),
         q("t14-v1-5","引き出しの【奥】に会議の資料があります。",["すみ","おく","はし","なか"],2,"Tortmaning chuqur ichida yig'ilish hujjatlari bor.",reading="おく",expl="奥 → おく (ichki qism, tub, chuqur)"),
         q("t14-v1-6","【料金】が安いほうを選ぶ。",["よきん","りょきん","ようきん","りょうきん"],4,"Narxi arzonroq tomonni tanlayman.",reading="りょうきん",expl="料金 → りょうきん (to'lov, narx, tarifı)"),
         q("t14-v1-7","週末、【田舎】へ出かけた。",["たんぼ","はたけ","のはら","いなか"],4,"Dam olish kunlari qishloqqa chiqdim.",reading="いなか",expl="田舎 → いなか (qishloq, periferiya)"),
         q("t14-v1-8","その集会は、午後5時に【閉会】した。",["かいかい","かいがい","へいかい","へいがい"],3,"U yig'ilish kechqurun soat 5da yopildi.",reading="へいかい",expl="閉会 → へいかい (yig'ilishni yopish, yig'ilish tugashi)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t14-v2-9","【めんどう】な仕事をしなくてはいけない。",["面頭","面働","面倒","面動"],3,"Noqulay (zahmatli) ishni qilishim kerak.",expl="めんどう → 面倒 (noqulay, zahmatli, bezovta)"),
         q("t14-v2-10","昔の【きろく】を参考にする。",["紀錄","紀綠","記錄","記録"],4,"Qadimgi yozuvlarni (rekordlarni) ko'rib chiqaman.",expl="きろく → 記録 (yozuv, qayd, rekord)"),
         q("t14-v2-11","その小鳥を【とらえて】、かごの中に入れた。",["取らえて","担らえて","補らえて","捕らえて"],4,"U qushchani ushladi va qafasga solib qo'ydi.",expl="とらえる → 捕らえる (ushlash, tutib olmoq)"),
         q("t14-v2-12","その新聞と、この新聞の書き方を【くらべて】ください。",["批べて","比べて","調べて","対べて"],2,"O'sha gazeta va bu gazeta yozilishini solishtiring.",expl="くらべる → 比べる (solishtimoq, taqqoslamoq)"),
         q("t14-v2-13","この電話には、【きのう】がたくさん付いている。",["性能","効能","技能","機能"],4,"Bu telefonda juda ko'p funksiya bor.",expl="きのう → 機能 (funksiya, imkoniyat)"),
         q("t14-v2-14","新しい【こいびと】ができた。",["恋人","好人","愛人","来人"],1,"Yangi sevgilim paydo bo'ldi.",expl="こいびと → 恋人 (sevgili, yor)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t14-v3-15","この文法は、試験によく出る（　）だ。",["ポスト","ポイント","テンポ","ポジション"],2,"Bu grammatika imtihonda ko'p chiqadigan nuqta (ball).",expl="ポイント = nuqta, muhim jihat, imtihon bali"),
         q("t14-v3-16","車の調子が悪いので、（　）してください。",["修正","修理","調子","調理"],2,"Mashina buzilgan, ta'mirlab bering.",expl="修理 = ta'mirlash, tuzatish"),
         q("t14-v3-17","料理が足りないので、注文を（　）してください。",["追加","節約","合計","強化"],1,"Taom yetmayapti, buyurtmani qo'shing.",expl="追加 = qo'shimcha, qo'shish"),
         q("t14-v3-18","この病気は人に（　）ので、注意してください。",["移る","働く","渡る","動く"],1,"Bu kasallik odamga yuqadi, ehtiyot bo'ling.",expl="移る = ko'chmoq, yuqmoq (kasallik)"),
         q("t14-v3-19","どんな職業につくかは（　）の自由だ。",["別人","個人","数人","何人"],2,"Qanday kasb tanlash — shaxsiy erkinlik.",expl="個人の自由 = shaxsiy erkinlik"),
         q("t14-v3-20","ベランダにふとんを（　）出かけた。",["ほして","まいて","しいて","つるして"],1,"Balkonga ko'rpani yoyib (quritib) chiqib ketdim.",expl="ほす = quritmoq, yoymoq (ko'rpa, kiyim)"),
         q("t14-v3-21","今月から、新しい生活が（　）した。",["アップ","ダウン","スタート","ストップ"],3,"Bu oydan yangi hayot boshlandi.",expl="スタート = boshlash, start"),
         q("t14-v3-22","母に（　）のセーターをもらって、うれしかった。",["手立て","手ぬい","手さぐり","手作り"],4,"Onamdan qo'lda to'qilgan sviter olganim uchun xursand bo'ldim.",expl="手作り = qo'lda yasalgan, uy ishlab chiqarishi"),
         q("t14-v3-23","田中さんは、友人たちに（　）されています。",["自信","信頼","責任","達成"],2,"Tanaka janob do'stlari tomonidan ishonchga sazovor.",expl="信頼 = ishonch, e'timod"),
         q("t14-v3-24","会社に入って3年、仕事のおもしろさが（　）わかってきました。",["さっぱり","べつに","だんだん","あんまり"],3,"Kompaniyaga kirganiga 3 yil, ishning qiziqligini asta-sekin tushuna boshladim.",expl="だんだん = asta-sekin, sekin-asta"),
         q("t14-v3-25","クラスのみんなに（　）されて、悲しくなった。",["無欲","無味","無害","無視"],4,"Sinfdoshlarning hammasi e'tiborsiz qoldirgani uchun xafa bo'ldim.",expl="無視 = e'tiborsizlik, pisand qilmaslik"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t14-v4-26","午後は町を【ふらふら】していた。",["話しながら歩いて","考えながら歩いて","目的もなく歩いて","目標に向かって歩いて"],3,"Tushdan keyin shaharni maqsadsiz kezib yurdim.",expl="ふらふらする = laqillab yurmoq, maqsadsiz kezmoq → 目的もなく歩いて"),
         q("t14-v4-27","冬になって、よく【寝坊する】ようになりました。",["早く起きる","遅く起きる","早く寝る","遅く寝る"],2,"Qish kelishi bilan kech turadigan bo'ldim.",expl="寝坊する = kech turmoq, uyquni o'tkazib yubormoq → 遅く起きる"),
         q("t14-v4-28","野菜を【あげて】、料理を作りました。",["細かく切って","よく混ぜて","生のままで","油で調理して"],4,"Sabzavotlarni qovurib (yog'da) taom tayyorladim.",expl="あげる (揚げる) = yog'da qovurmoq → 油で調理して"),
         q("t14-v4-29","問題だと思うことを【書き出して】ください。",["みんなに伝えて","パソコンで入力して","大きな字で書いて","必要な部分をまとめて"],4,"Muammo deb o'ylaydigan narsalarni yozib chiqing (sanab chiqing).",expl="書き出す = yozib chiqmoq, ro'yxat tuzmoq → 必要な部分をまとめて"),
         q("t14-v4-30","今日は【ついている】1日だった。",["運がよい","運が悪い","体調がよい","体調が悪い"],1,"Bugun omadli kun bo'ldi.",expl="ついている = omidir kelmoq, baxtli → 運がよい"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t14-v5-31","横になる",["机の上に、ペンが横になっています。","川のとなりに、小さな家が横になっています。","ねむくなったので、ふとんに横になった。","空に白い雲が横になり、きれいだ。"],3,
           "横になる = yotmoq, gorizontal holatga kelmoq.",optsTr=["Stol ustida qalam 'gorizontal'da turibdi (noto'g'ri — 置いてある kerak).","Daryo yonida kichik uy 'gorizontal' (noto'g'ri — 建っている kerak).","Uyqum keldi va ko'rpaga yotdim. (to'g'ri)","Osmonda oq bulut 'gorizontal' bo'lib, chiroyli (noto'g'ri — 横に伸びて kerak)."]),
         q("t14-v5-32","転がる",["時間がなかったので、家から会社まで転がっていった。","男の子の投げたボールは、地面に転がった。","部屋から、空に飛行機が転がっているのが見えます。","駅から公園まで、バスが転がっているのでとても便利です。"],2,
           "転がる(ころがる) = dumalab yurmoq, ag'anab ketmoq.",optsTr=["Vaqt yo'q edi, uydan kompaniyagacha 'dumalab' ketdim (noto'g'ri — 急いで kerak).","Bola tashlagan to'p yerda dumaladi. (to'g'ri)","Xonadan osmonda samolyot 'dumalayotganini' ko'rish mumkin (noto'g'ri — 飛んでいる kerak).","Bekatdan parkgacha avtobus 'dumalayapti' (noto'g'ri — 走っている kerak)."]),
         q("t14-v5-33","底",["いすの底に、2匹のねこが寝ています。","スカートの底が地面につきそうです。","私の家は、大きな山の底にあります。","この魚は、深い海の底に住んでいます。"],4,
           "底(そこ) = tub, pastki qism, dib.",optsTr=["Stul 'tubida' 2 ta mushuk yotibdi (noto'g'ri — 下 kerak).","Yubkaning 'tubi' yerga tegay deyapti (noto'g'ri — 裾/すそ kerak).","Mening uyim katta tog'ning 'tubida' (noto'g'ri — ふもと kerak).","Bu baliq chuqur dengizning tubida yashaydi. (to'g'ri)"]),
         q("t14-v5-34","兼ねる",["あの人は、2つの仕事を兼ねている。","となりの家に兼ねて、なるべく静かに生活しています。","きれいな花をたくさん兼ねて、花束を作った。","家の鍵を兼ねないで、外出してしまった。"],1,
           "兼ねる(かねる) = bir vaqtda bajarmoq, birlashtirib olib bormoq.",optsTr=["U kishi 2 ta ishni birga olib boryapti. (to'g'ri)","Qo'shni uyga 'birlashtirib', imkon qadar jim yashamoqdaman (noto'g'ri — 遠慮して kerak).","Ko'p chiroyli gul 'birlashtirib', guldasta yasadim (noto'g'ri — 集めて kerak).","Uy kalitini 'birlashtirmasdan' chiqib ketdim (noto'g'ri — 忘れて kerak)."]),
         q("t14-v5-35","まずい",["私は、彼のようなまずいな人間はきらいです。","今日の天気は、暑いというよりはまずい。","学生なのだから授業に遅刻をするのはまずい。","このりんごは高いので、少しまずくしてください。"],3,
           "まずい = nosoz, noqulay; yomon (ta'm); uyatli, noo'rin.",optsTr=["Men u kabi 'nosoz' odamni yoqtirmayman (noto'g'ri — ひどい kerak).","Bugungi ob-havo issiq deysizmi, 'nosoz' (noto'g'ri — むしろ kerak).","Talaba bo'la turib darsga kech qolish — noo'rin (uyatli). (to'g'ri)","Bu olma qimmat, biroz 'nosoz' qiling (noto'g'ri — 安く kerak)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t14-g1-1","となりの人がどろぼうをして逮捕された。悪い人（　）見えなかったけど。",["より","では","でも","には"],4,"Qo'shni odam o'g'rilik qilib hibsga olindi. Yomon odam kabi ko'rinmasdi-da.",expl="〜には = ...ga (ko'rinish, baho berish kontekstida — 悪い人には見えない = yomon odam bo'lib ko'rinmaydi)"),
         q("t14-g1-2","朝、牛乳を飲んだ（　）、今まで何も食べていません。",["ところ","だけで","さえ","しか"],2,"Ertalab faqat sut ichib, hozirgacha hech narsa yemedim.",expl="〜だけで = faqat ...ingina bilan (yuklamasi — yetarlilik/cheklov)"),
         q("t14-g1-3","まったく勉強していない佐藤さんが、あの大学に合格できる（　）。",["もんか","ことか","ところか","はずか"],1,"Umuman o'qimagan Sato-san o'sha universitetga o'ta oladimi? (aslo mumkin emas!)",expl="〜もんか = aslo ...maslik (qat'iy inkor, retorik). 口語的."),
         q("t14-g1-4","彼は、彼女と何も話す（　）なく、帰って行った。",["ほど","ところ","もの","こと"],4,"U u bilan hech narsa gaplashmasdan ortiga qaytdi.",expl="何も〜ことなく = ...masdan, ...siz (ことなく = qilmasdan)"),
         q("t14-g1-5","このゲームは子どもに（　）、大人にも人気がある。",["限って","限らず","すぎて","すぎず"],2,"Bu o'yin nafaqat bolalar, balki kattalar orasida ham mashhur.",expl="〜に限らず = ...gina emas, ...dan tashqari ham"),
         q("t14-g1-6","大げんかした（　）、彼女と離婚しました。",["末は","末までが","末に","末から"],3,"Katta janjal qilgan natijasida u ayolidan ajrashdi.",expl="〜末に = ...dan keyin (uzoq/og'ir jarayon natijasida). 〜あげく bilan o'xshash."),
         q("t14-g1-7","息子「なんだか風邪をひいたみたい。」母「そういうときは、暖かくしてゆっくり（　）よ。」",["休むわけ","休むほう","休むはず","休むこと"],4,"O'g'il: «Shamolladim shekilli.» Ona: «Bunday paytda iliq kiyinib yaxshilab dam olish kerak.»",expl="〜こと = ...moq kerak (amir shakli — こと/のこと)"),
         q("t14-g1-8","先生「原子力をテーマにした映画を見て、どう思いましたか。」生徒「はい、これからのエネルギーについて考え（　）ました。」",["考えて","考えたまま","考えさせ","考えさせられ"],4,"O'qituvchi: «Atom energiyasi haqidagi filmni ko'rib nima deb o'yladingiz?» O'quvchi: «Ha, kelajakdagi energiya haqida o'ylanib qoldim (o'ylashga majbur bo'ldim).»",expl="〜させられる = majburiy bajarish (passiv-majburiy shakl). 考えさせられる = o'ylanishga majbur etilmoq."),
         q("t14-g1-9","明日、お宅へ（　）つもりですが、よろしいでしょうか。",["拝見する","お目にかかる","いただく","うかがう"],4,"Ertaga siznikiga borishni niyat qilgan edim, qulay bo'ladimi?",expl="うかがう = «bormoq/so'ramoq» ning kamtarlik shakli (謙譲語). 訪問する → うかがう."),
         q("t14-g1-10","女の学生「この新しいシューズ、歩く（　）、やせるらしいよ。」男の学生「本当かなあ。」",["歩くだけでも","歩いたままでも","歩くばかりで","歩くことより"],1,"Qiz talaba: «Bu yangi poyabzal, yurishning o'ziyoq ozaytirarmish.» O'g'il talaba: «Chinmi?»",expl="〜だけでも = faqat ...ingina bilan ham. 歩くだけでやせる = yurishning o'ziyoq ozaytiradi."),
         q("t14-g1-11","この町の昔と今を比較すると、その違いには驚く（　）。",["くらいがあります","ほどがあります","ものがあります","のがあります"],3,"Bu shaharning ilgari va hozirini solishtirsangiz, farqi hayratga soladi.",expl="〜ものがある = ...da biror narsa bor (hayrat, his-tuyg'u ifodalash). 驚くものがある = hayratlanarli jihat bor."),
         q("t14-g1-12","会議が始まると電話に（　）、メールを送って下さい。",["出ようとしないので","出られそうにないので","出るようなので","出るそうなので"],2,"Yig'ilish boshlanganida telefonga chiqolmay qolsam, elektron xat yuboring.",expl="〜そうにない = ...olishi dargumon, ...ib bo'lmaydi (ehtimollik yetarli emas)"),
         q("t14-g1-13","パク「キムさんって、とてもすてきな人だね。」木村「でも、キムさんは確か（　）。」",["結婚していそうだよ","結婚していっこないって","結婚しているわけだよ","結婚しているんだって"],4,"Pak: «Kim janob juda ajoyib odam ekan.» Kimura: «Lekin Kim janob turmush qurib bo'lgan deyishadi.»",expl="〜んだって = ...deyishadi, ...ekan (eshitish, rivoyat). 確か〜んだって = ishonchim komil emas, lekin eshitishimcha..."),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t14-g2-14",None,["あまり","夢中に","研究に","なる"],4,"To'g'ri jumla: «Olim Tanaka janob tadqiqotiga shu qadar berilib ketib, ba'zida ovqatlanishni ham unutib qo'yadi.»",
           prefix="科学者の田中さんは、",suffix="ときどき食事をするのを忘れてしまう。",starPos=3,order=[3,2,4,1],expl="研究に夢中になるあまり (〜あまり = juda ...ganidan, haddan ziyod ...gani sababli)"),
         q("t14-g2-15",None,["よろしければ","させて","お手伝いを","私で"],2,"To'g'ri jumla: «Kelin, men yordam berib tursammi?» (Agar kerak bo'lsa, yordam berishga ruxsat bering.)",
           prefix="大変そうですね。",suffix="いただけませんか。",starPos=4,order=[4,1,3,2],expl="私でよろしければお手伝いをさせていただけませんか (させていただく = hurmat bilan ruxsat so'rash)"),
         q("t14-g2-16",None,["パーティー","いない","なんて","前田さんが"],1,"To'g'ri jumla: «Eh, Maeda-san bo'lmagan ziyofat qiziq bo'lmaydi-ya.»",
           prefix="後藤「えー、",suffix="楽しくありませんよ。」",starPos=3,order=[4,2,1,3],expl="前田さんがいないパーティーなんて楽しくない (〜なんて = ... kabi narsa, mensimaslik yoki hayrat)"),
         q("t14-g2-17",None,["よかった","して","明日に","おけば"],2,"To'g'ri jumla: «Bugun havo yomon edi, shu sababli ko'rishuvni ertaga qoldirganim maqul ekan, afsusdaman.»",
           prefix="今日は1日天気が悪かったので、デートは",suffix="と後悔した。",starPos=2,order=[3,2,4,1],expl="明日にしておけばよかった (〜ておけばよかった = ...ib qo'yganim maqul edi, afsus)"),
         q("t14-g2-18",None,["気をつける","際に","べき","点を"],3,"To'g'ri jumla: «Chet elda ishlayotganingizda e'tibor berish kerak bo'lgan nuqtalarni o'rgating.»",
           prefix="外国で仕事をする",suffix="教えてください。",starPos=3,order=[2,1,3,4],expl="際に気をつけるべき点を (際に = paytida; 〜べき = ...ish kerak bo'lgan)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "秋の気配",
       "passage": (
         "8月の終わりごろといえば、まだとても暑い時期だ。太陽はぎらぎらと輝き、都会のアスファルトの上を"
         "歩いている人々は暑さで疲れている。毎日暑くて、元気がなくなる人も多いだろう。\n"
         "{{19}}、山の森の中に行ってみると、街にいるよりも空気が冷たく、早くも秋の気配が満ちているのに"
         "気がつくだろう。山に行き、おいしい空気を吸って、美しい景色を{{20}}、夏の暑さを忘れることができる。\n"
         "山まで遠いし、行く時間もない、という人も多いだろう。{{21}}、都会の中の森に出かけてみてはいかが"
         "だろうか。都会の中にある大きな公園の森に入ってみれば、街の中と気温が大きく違うことに驚くだろう。"
         "大きな公園でなくてもよい。家の近所にある小さな公園の中の森や、住宅地の中の歩道につくられた林でも{{22}}。"
         "きれいな色の小さな実がなっていたり、秋になって色が変わった草が、しずかに風に吹かれていたりするのを"
         "見つけられるだろう。そして、こんな目立たないところでも花や草はきちんと生きているのだと感じ、"
         "人より早く秋の気配を発見した喜びを{{23}}。"
       ),
       "passage_tr": (
         "Avgust oyi oxirlari deyilsa, hali juda issiq davr. Quyosh yaltirab nurini sochadi, shahardagi asfalt "
         "ustida yurayotgan odamlar issiqdan holdan toygan. Har kuni issiq bo'lib, kuchsizlanib qolgan odamlar ham "
         "ko'p bo'lsa kerak.\n"
         "BIROQ, tog'dagi o'rmonga borsangiz, shahardan ko'ra havo sovuqroq va allaqachon kuzning alomatlari "
         "to'la ekanini sezasiz. Tog'ga borib, toza havo tutatib, go'zal manzaraga QARAShNING O'ZI ham "
         "yozning issig'ini unutishga yetadi.\n"
         "Tog' uzoq, bora olmayman, deydiganlar ham ko'pdir. BUNDAY PAYTDA shahardagi o'rmonga chiqqan maqul. "
         "Shahardagi katta bog'dagi o'rmonga kirsangiz, shahardagidan havo harorati ancha farq qilishiga hayron "
         "qolasiz. Katta bog' bo'lishi shart emas. Uy yonidagi kichik bog'dagi o'rmon yoki turar-joy hududidagi "
         "yo'lakdagi daraxtlarzor ham YETARLI. Ko'p rangli kichik mevalar yoki kuz kelishi bilan rangi o'zgargan "
         "o'tlar sekin shamolda hilpiraganini topasiz. Va, bunday ko'zga tashlanmaydigan joyda ham gullar va "
         "o'tlar tirik ekanini his qilib, boshqalardan oldin kuzning alomatlarini topgan sevinchni "
         "his qilishingizga shubha yo'q."
       ),
       "questions": [
         q("t14-g3-19",None,["だから","けれども","つまり","その上"],2,
           "[けれども]、山の森の中に行ってみると… = BIROQ, tog'dagi o'rmonga borsangiz...",blankNo="19",expl="けれども = lekin, ammo (qarama-qarshilik bog'lovchisi)"),
         q("t14-g3-20",None,["見るからに","見たままで","見るだけでも","見ないまでも"],3,
           "美しい景色を[見るだけでも]、夏の暑さを忘れることができる = go'zal manzaraga QARASHNING O'ZI ham yozni unuttirar.",blankNo="20",expl="〜だけでも = faqat ...ingina ham (yetarlilik)"),
         q("t14-g3-21",None,["そんなときは","あんなときは","そちらのときは","あちらのときは"],1,
           "という人も多いだろう。[そんなときは]、都会の中の森に… = deydiganlar ko'p. BUNDAY PAYTDA shahardagi o'rmonga...",blankNo="21",expl="そんなときは = bunday paytda (yaqin kontekstga ishora)"),
         q("t14-g3-22",None,["十分だ","十分ではない","違っている","違っていない"],1,
           "住宅地の中の歩道の林でも[十分だ] = turar-joy yo'lakdagi daraxtlarzor ham YETARLI.",blankNo="22",expl="十分だ = yetarli, kifoya"),
         q("t14-g3-23",None,["感じかねない","感じるほかはない","感じることができかねる","感じられるにちがいない"],4,
           "秋の気配を発見した喜びを[感じられるにちがいない] = kuzni topgan sevinchni his qilishingizga SHUBHA YO'Q.",blankNo="23",expl="〜にちがいない = albatta, shubhasiz (ishonch)"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test14.json yozildi. Jami savol:", tot)
