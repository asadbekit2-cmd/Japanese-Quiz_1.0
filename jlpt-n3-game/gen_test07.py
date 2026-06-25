# -*- coding: utf-8 -*-
"""test07.json — 第7回 模擬テスト (PDF betlari 68-77, javob 200)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test07.json")

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
  "id": 7, "title_jp": "第7回 模擬テスト", "title_uz": "7-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t7-v1-1","道路に大きな木が【倒れて】いる。",["おれて","もたれて","われて","たおれて"],4,"Yo'lda katta daraxt qulab yotibdi.",reading="たおれて",expl="倒れる → たおれる (qulamoq, ag'darilmoq)"),
         q("t7-v1-2","あの【植物】の名前を知っていますか。",["しょくもの","しきもの","しょくぶつ","しきぶつ"],3,"Anavi o'simlikning nomini bilasizmi?",reading="しょくぶつ",expl="植物 → しょくぶつ (o'simlik)"),
         q("t7-v1-3","週末は、【知人】に会う約束がある。",["ちにん","ちじん","しにん","しじん"],2,"Dam olish kunlari tanishim bilan uchrashuv bor.",reading="ちじん",expl="知人 → ちじん (tanish odam)"),
         q("t7-v1-4","箱をいくつか【積んだ】。",["たたんだ","つつんだ","つんだ","ふんだ"],3,"Bir nechta qutini ustma-ust qaladim.",reading="つんだ",expl="積む → つむ (ustma-ust qo'ymoq, yuklamoq)"),
         q("t7-v1-5","【迷惑】なことをしないでください。",["めんどう","めいわく","じゃま","さいあく"],2,"Bezovta qiladigan (xalaqit beradigan) ish qilmang.",reading="めいわく",expl="迷惑 → めいわく (tashvish, ovoragarchilik berish)"),
         q("t7-v1-6","この【地域】には、スーパーがありません。",["ちたい","じたい","ちいき","じいき"],3,"Bu hududda supermarket yo'q.",reading="ちいき",expl="地域 → ちいき (hudud, mintaqa)"),
         q("t7-v1-7","きのう、【庭】のそうじをしました。",["にわ","へや","ゆか","かべ"],1,"Kecha hovlini tozaladim.",reading="にわ",expl="庭 → にわ (hovli, bog')"),
         q("t7-v1-8","わが社では、最近、社長が【交代】した。",["こうてい","こうたい","こうでい","こうだい"],2,"Bizning kompaniyada yaqinda rahbar almashdi.",reading="こうたい",expl="交代 → こうたい (almashinish, navbatlashish)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t7-v2-9","【あんいな】考えは捨てなさい。",["浅易","案易","暗易","安易"],4,"Yengil-elpi (o'ylamasdan qilingan) fikrni tashlang.",expl="あんい → 安易 (yengil-elpi, oson yo'l)"),
         q("t7-v2-10","建物の【こうぞう】を調べる。",["構造","溝造","購造","講造"],1,"Binoning tuzilishini tekshiraman.",expl="こうぞう → 構造 (tuzilish, struktura)"),
         q("t7-v2-11","それを【ひろって】ください。",["触って","拾って","放って","払って"],2,"Uni yerdan oling (terib oling).",expl="ひろう → 拾う (terib olmoq, yerdan olmoq)"),
         q("t7-v2-12","1人に3つずつわけると、2つ【あまる】。",["与る","残る","余る","甘る"],3,"Har kishiga 3 tadan bo'lsak, 2 ta ortib qoladi.",expl="あまる → 余る (ortib qolmoq, ortmoq)"),
         q("t7-v2-13","いろいろな仕事を【けいけん】する。",["実験","体験","経験","治験"],3,"Turli ishlarni tajriba qilaman (boshimdan kechiraman).",expl="けいけん → 経験 (tajriba)"),
         q("t7-v2-14","サルがすばやい【どうさ】で木にのぼる。",["働昨","動昨","働作","動作"],4,"Maymun chaqqon harakat bilan daraxtga chiqadi.",expl="どうさ → 動作 (harakat, xatti-harakat)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t7-v3-15","いつも帽子をかぶるのが、彼の（　）だ。",["スマート","タイトル","ペース","スタイル"],4,"Doim shlyapa kiyish — uning uslubi (stili).",expl="スタイル = uslub, stil"),
         q("t7-v3-16","わが国は、A国と（　）を行っている。",["表示","貿易","伝達","流行"],2,"Bizning davlat A davlat bilan savdo (tashqi savdo) olib boradi.",expl="貿易 = (tashqi) savdo"),
         q("t7-v3-17","できるかぎり（　）して仕事を進める。",["工夫","救助","心配","採用"],1,"Imkon qadar pux ta o'ylab (chora topib) ishni davom ettiraman.",expl="工夫する = chora-tadbir izlamoq, pux ta o'ylamoq"),
         q("t7-v3-18","雷がこわくて、（　）過ごした。",["しびれて","ゆれて","ふるえて","ひえて"],3,"Momaqaldiroqdan qo'rqib, qaltirab o'tirdim.",expl="ふるえる = qaltiramoq, titramoq"),
         q("t7-v3-19","テストで、今までで（　）の成績をおさめた。",["最善","最大","最多","最高"],4,"Testda hozirgacha eng yuqori natijani qo'lga kiritdim.",expl="最高 = eng yuqori, eng zo'r"),
         q("t7-v3-20","建物が台風から私たちを（　）くれた。",["守って","許して","負けて","認めて"],1,"Bino bizni tayfundan himoya qildi.",expl="守る = himoya qilmoq, asramoq"),
         q("t7-v3-21","コピー機に用紙が（　）されているかどうか、調べてください。",["スイッチ","プリント","インク","セット"],4,"Nusxa olish mashinasiga qog'oz qo'yilgan-qo'yilmaganini tekshiring.",expl="セットする = o'rnatmoq, joylashtirmoq, sozlamoq"),
         q("t7-v3-22","私のアパートの部屋は東（　）です。",["開け","行き","向き","沿い"],3,"Mening kvartiram xonasi sharqqa qaragan.",expl="〜向き = ...ga qaragan (tomon)"),
         q("t7-v3-23","音が大きすぎるので、（　）してください。",["減少","安定","調節","改定"],3,"Ovoz juda baland, shuning uchun moslang (sozlang).",expl="調節する = sozlamoq, moslamoq, tartibga solmoq"),
         q("t7-v3-24","きのうの夜、（　）おなかが痛くなったので、心配だ。",["やっと","せっかく","ちゃんと","急に"],4,"Kecha tunda to'satdan qornim og'rib qoldi, shuning uchun xavotirdaman.",expl="急に = to'satdan, birdan"),
         q("t7-v3-25","私にはこの絵の（　）が理解できない。",["原料","価値","金銭","物価"],2,"Men bu rasmning qadrini (qiymatini) tushunolmayman.",expl="価値 = qiymat, qadr"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t7-v4-26","【めずらしい】くだものを食べた。",["よくある","ときどきある","あまりない","どこにもない"],3,"Noyob (kam uchraydigan) mevani yedim.",expl="めずらしい = noyob, kam uchraydigan → あまりない"),
         q("t7-v4-27","テーブルの上の紙を【まとめた】。",["集めた","分けた","捨てた","破った"],1,"Stol ustidagi qog'ozlarni jamladim (bir joyga to'pladim).",expl="まとめる = jamlamoq, bir joyga to'plamoq → 集めた"),
         q("t7-v4-28","田中さんは、山田さんに【手を貸した】。",["握手した","助けた","手紙を書いた","お金を貸した"],2,"Tanaka-san Yamada-sanga yordam berdi.",expl="手を貸す = yordam bermoq (idioma) → 助けた"),
         q("t7-v4-29","あの2人は、【気が合う】ようだ。",["つき合っている","ときどき会っている","仲がよい","仲が悪い"],3,"U ikkovi til topishadiganga (chiqishadiganga) o'xshaydi.",expl="気が合う = til topishmoq, chiqishmoq → 仲がよい"),
         q("t7-v4-30","【おかしな】ことが続けて起こった。",["すばらしい","つまらない","平凡な","不思議な"],4,"G'alati narsalar ketma-ket yuz berdi.",expl="おかしな = g'alati, ajabtovur → 不思議な (sirli, g'aroyib)"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t7-v5-31","さけぶ",["電話で母に、きのうあった出来事についてさけんだ。","毎日、その日あったことを日記にさけんでいる。","前から歩いてきた犬が、私に向かってさけんできた。","遠くを歩いている友だちの名前を思いきりさけんだ。"],4,
           "さけぶ = baqirmoq, qichqirmoq.",optsTr=["Telefonda onamga kechagi voqea haqida 'baqirdim' (noto'g'ri — 話した kerak).","Har kuni kun voqealarini kundalikka 'baqiraman' (noto'g'ri — 書く kerak).","Oldindan kelayotgan it menga qarab 'baqirdi' (noto'g'ri — it uchun 吠える kerak).","Uzoqda ketayotgan do'stimning ismini bor ovozda baqirdim. (to'g'ri)"]),
         q("t7-v5-32","ふく",["よごれたシャツを洗たく機でふいた。","テーブルが汚いので、すぐにふいてください。","客が来るので、部屋を掃除機でふかなければなりません。","落ちているごみをごみ箱にふいてください。"],2,
           "ふく(拭く) = artmoq, surtib tozalamoq.",optsTr=["Kir ko'ylakni kir mashinada 'artdim' (noto'g'ri — 洗う kerak).","Stol kir, shuning uchun darrov arting. (to'g'ri)","Mehmon keladi, xonani changyutgich bilan 'artish' kerak (noto'g'ri — かける kerak).","Yerga tushgan axlatni axlat qutisiga 'arting' (noto'g'ri — 捨てる kerak)."]),
         q("t7-v5-33","ヒント",["景色にヒントをつけて、写真をとりました。","よいヒントを与えられ、この会社に入ることができました。","この店では、500円以上買い物しないとヒントがつきません。","この問題は難しすぎるので、解くためのヒントをください。"],4,
           "ヒント = ishora, yo'l-yo'riq, maslahat.",optsTr=["Manzaraga 'ishora' qo'yib, rasmga oldim (noto'g'ri).","Yaxshi 'ishora' berilib, bu kompaniyaga kira oldim (noto'g'ri — コネ kerak).","Bu do'konda 500 yendan ko'p xarid qilmasa 'ishora' qo'shilmaydi (noto'g'ri — ポイント kerak).","Bu masala juda qiyin, yechish uchun ishora (yo'l-yo'riq) bering. (to'g'ri)"]),
         q("t7-v5-34","お見舞い",["今日は私の誕生日なので、お見舞いをもらった。","日本では結婚式のお見舞いに、何をあげればいいですか。","夜遅くまで勉強していたら、母がお見舞いを持って来てくれた。","病院に入院している同僚に、お見舞いを持って行った。"],4,
           "お見舞い = (kasal/baxtsizlikka uchraganni) ko'rgani borish, ko'rgazma sovg'asi.",optsTr=["Bugun tug'ilgan kunim, 'ko'rgani sovg'a' oldim (noto'g'ri — プレゼント kerak).","Yaponiyada to'yga 'ko'rgani sovg'a' sifatida nima berish kerak? (noto'g'ri — ご祝儀 kerak).","Kech tungacha o'qiganimda, onam 'ko'rgani sovg'a' olib keldi (noto'g'ri — 夜食 kerak).","Kasalxonada yotgan hamkasbimni ko'rgani sovg'a olib bordim. (to'g'ri)"]),
         q("t7-v5-35","おしゃれ",["この部屋はそうじをしたばかりなので、おしゃれです。","あの人は頭はいいが、おしゃれなところがある。","祖母は今年80歳になるが、今でもとてもおしゃれだ。","授業中に友だちとおしゃれしていて、先生に注意されてしまった。"],3,
           "おしゃれ = shinam kiyinish, didli, zamonaviy ko'rinish.",optsTr=["Bu xona endi tozalangani uchun 'shinam' (noto'g'ri — きれい kerak).","U odam aqlli, lekin 'shinam' joyi bor (noto'g'ri — ぬけた kerak).","Buvim bu yil 80 yoshga kiradi, lekin hozir ham juda shinam kiyinadi. (to'g'ri)","Dars vaqtida do'stim bilan 'shinam' bo'lib, o'qituvchidan tanbeh oldim (noto'g'ri — おしゃべり kerak)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t7-g1-1","子ども（　）できる計算をまちがえてしまった。",["から","だけ","でも","しか"],3,"Hatto bola ham bajara oladigan hisobni xato qilib qo'ydim.",expl="〜でも = hatto ...ham (so'nggi darajani misol qilib)"),
         q("t7-g1-2","彼女の優しい言葉を聞いて、うれしくて涙が出る（　）だった。",["もの","こと","ほど","よう"],3,"Uning mehribon so'zlarini eshitib, xursandligimdan ko'z yoshim chiqquday bo'ldi.",expl="〜ほど = ...darajada (daraja ko'rsatadi)"),
         q("t7-g1-3","あの人は、2年前（　）ギターを習い始めたそうです。",["より","により","よりも","はより"],1,"U odam 2 yil avvaldan gitara o'rgana boshlagan ekan.",expl="〜より = ...dan (vaqt/o'rin boshlanish nuqtasi)"),
         q("t7-g1-4","今から私の言う（　）、ノートに書いてください。",["なりに","ほどに","通りに","そうに"],3,"Endi men aytganimday qilib, daftaringizga yozing.",expl="〜通りに = ...ganday, xuddi ...kabi"),
         q("t7-g1-5","広い道路（　）、まっすぐ10分くらい歩くと、会社に着きます。",["において","にかけて","に沿って","を通じて"],3,"Keng yo'l bo'ylab to'g'riga 10 daqiqacha yursangiz, kompaniyaga yetasiz.",expl="〜に沿って = ...bo'ylab, ...ga yondosh"),
         q("t7-g1-6","あの人があぶない運転を（　）なんて、信じられない。",["す","する","し","して"],2,"U odam xavfli haydash qiladi deganni ishonib bo'lmaydi.",expl="普通形+なんて = ...deganni (kutilmagan/ishonarsiz his). 運転をする+なんて"),
         q("t7-g1-7","学校の先生に、この教室には（　）と言われました。",["入らされるな","入るな","入らせるな","入られるな"],2,"Maktab o'qituvchisi menga: «Bu sinfga kirma» dedi.",expl="動詞辞書形+な = ...ma (qat'iy taqiq). 入るな"),
         q("t7-g1-8","1人で10人分の仕事をするなんて（　）。",["できかねない","できなくはない","できっこない","できないことはない"],3,"Yolg'iz 10 kishilik ishni qilish — aslo bo'lmaydi (imkonsiz).",expl="〜っこない = aslo ...bo'lmaydi (kuchli inkor). できっこない"),
         q("t7-g1-9","松本「今日はおじゃましました。」金子「いいえ、また（　）ください。」",["おはいりになって","おいきになって","おかえりになって","おいでになって"],4,"Matsumoto: «Bugun bezovta qildim.» Kaneko: «Yo'q, yana keling.»",expl="おいでになる = 来る/行く ning hurmat shakli (keling)"),
         q("t7-g1-10","秘書「部長、ワールド商事の青木様が（　）。」部長「会議室にご案内して。」",["参られました","参りました","見ました","見えました"],4,"Kotiba: «Boshliq, World Shoji'dan Aoki-sama keldilar.» Boshliq: «Yig'ilish xonasiga boshlab boring.»",expl="見える = 来る ning hurmat shakli (keldilar). お客様が見えました"),
         q("t7-g1-11","私は、ただの社員に（　）、大事なことを決めることはできません。",["あり得ますから","あり得ませんので","すぎますから","すぎませんので"],4,"Men oddiy xodimdan boshqa narsa emasman, shuning uchun muhim narsalarni hal qila olmayman.",expl="〜にすぎない = faqat ...xolos. ただの社員にすぎません"),
         q("t7-g1-12","このセーターはかわいいけれど（　）、着るときに注意しています。",["汚れやすいので","汚れてもいいので","汚れづらいので","汚れにくいので"],1,"Bu sviter chiroyli, lekin oson kirlanadigani uchun kiyganda ehtiyot bo'laman.",expl="〜やすい = oson ...bo'ladi. 汚れやすい = oson kirlanadigan"),
         q("t7-g1-13","この犬は、こわい顔をしていますが、本当は優しいので、（　）ください。",["こわくならないで","こわくしないで","こわがられないでいて","こわがらないで"],4,"Bu it qo'rqinchli ko'rinadi, lekin aslida yuvosh, shuning uchun qo'rqmang.",expl="〜がる = ...lik his qilmoq. こわがる = qo'rqmoq → こわがらないで"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t7-g2-14",None,["かわりに","私が","作る","晩ごはんを"],3,"To'g'ri jumla: «Bugun men kechki ovqat qilish o'rniga, sen uy yig'ishtir.»",
           prefix="今日は",suffix="あなたはそうじをしてよ。",starPos=3,order=[2,4,3,1],expl="To'g'ri tartib: 私が晩ごはんを作るかわりに"),
         q("t7-g2-15",None,["うれしく","かかれた","お目に","ことを"],2,"To'g'ri jumla: «Tanishganimdan xursandman (siz bilan ko'rishganimdan mamnunman).»",
           prefix="「はじめまして。",suffix="存じます。」",starPos=2,order=[3,2,4,1],expl="To'g'ri tartib: お目にかかれたことをうれしく (お目にかかる = «ko'rishmoq» ning kamtarlik shakli)"),
         q("t7-g2-16",None,["限り","ある","仕事が","としても"],2,"To'g'ri jumla: «Necha yoshga kirsam ham, ish bor ekan, ishlashda davom etgim keladi.»",
           prefix="私は、何歳になった",suffix="働き続けたいです。",starPos=3,order=[4,3,2,1],expl="To'g'ri tartib: としても仕事があるかぎり"),
         q("t7-g2-17",None,["上で","別れる","とうとう","話し合った"],1,"To'g'ri jumla: «Ikkovi ko'p marta gaplashib olgandan so'ng, oxir-oqibat ajrashishga qaror qilishdi.»",
           prefix="2人は、何度も",suffix="ことを決めた。",starPos=2,order=[4,1,3,2],expl="To'g'ri tartib: 話し合った上でとうとう別れる (〜上で = ...gandan keyin/asosida)"),
         q("t7-g2-18",None,["関する","資料","新しい","最も"],3,"To'g'ri jumla: «Bu — mamlakatimizning hozirgi ekologik muammolariga oid eng yangi hujjat (material).»",
           prefix="これは、現在のわが国の環境問題に",suffix="です。",starPos=3,order=[1,4,3,2],expl="To'g'ri tartib: 関する最も新しい資料 (〜に関する = ...ga oid)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "商店街の新しい名前が決まる",
       "passage": (
         "ある商店街が、商店街の新しい名前を募集した。すると約1000通{{19}}応募があった。"
         "その中から、商店街の店のオーナーたちが話し合って、いちばんいいものを選んで、"
         "商店街の新しい名前が決まった。\n"
         "その新しい名前は、「キウイ通り」という。今までは、その町の古い地名から、「古川通り」と"
         "呼ばれていたので、{{20a}}、古くからここに住んでいる人にとっては驚くような名前{{20b}}。"
         "若者も集まるような明るく元気のある名前にしようと、特産物であるくだもののキウイをもとにした"
         "今回の名前が決まった。\n"
         "この商店街は、約100年以上も前からあるという古い通りだ。{{21}}、最近建物や道路が古くなって"
         "きて、夜にはバイクに乗った若者たちが集まってさわいだり、犯罪が発生したりと様々な問題が"
         "起きるようになっていた。また、近くに大きなショッピングセンターができ、お客も減ってしまった。"
         "今回、商店街の人たちが{{22}}のは、昔のように活気がある通りにするための作戦の1つだという。"
         "お店の人々は新しい名前の効果ができるだけ早く出ることを{{23}}。"
       ),
       "passage_tr": (
         "Bir savdo rastasi (shopping street) o'ziga yangi nom uchun tanlov e'lon qildi. Shunda taxminan "
         "1000  taga YAQIN ariza keldi. Ular ichidan rasta do'konlari egalari maslahatlashib, eng yaxshisini "
         "tanlab, rastaning yangi nomi belgilandi. "
         "Yangi nom — «Kivi ko'chasi». Ilgari shaharning eski joy nomidan «Furukawa ko'chasi» deb atalardi, "
         "shuning uchun, EHTIMOL, azaldan shu yerda yashab kelayotganlar uchun bu hayratlanarli nom BO'LSA "
         "KERAK. Yoshlar ham yig'iladigan yorqin, quvnoq nom bo'lsin deb, mahalliy mahsulot — kivi mevasiga "
         "asoslangan bu nom tanlandi. "
         "Bu savdo rastasi 100 yildan ko'proq oldindan mavjud eski ko'cha. ASLIDA esa, so'nggi paytda bino va "
         "yo'llar eskirib, kechalari mototsiklli yoshlar yig'ilib shovqin solishi yoki jinoyat sodir bo'lishi "
         "kabi turli muammolar kelib chiqayotgan edi. Yana, yaqinda katta savdo markazi paydo bo'lib, "
         "mijozlar ham kamayib ketdi. Bu safar rasta ahli NOMNI O'ZGARTIRGANI — ilgarigiday gavjum ko'chaga "
         "aylantirish uchun qilingan rejalardan biri ekan. Do'kon egalari yangi nomning samarasi iloji boricha "
         "tezroq chiqishini TILAYOTGANIGA SHUBHA YO'Q."
       ),
       "questions": [
         q("t7-g3-19",None,["しか","もの","すら","さえ"],2,
           "約1000通[もの]応募 = ~1000 taga yaqin (shuncha ko'p) ariza.",blankNo="19",expl="数量+もの = ...cha (ko'plikni ta'kidlash)"),
         q("t7-g3-20",None,["もしも ／ だろう","もしかすると ／ かもしれない","もしや ／ だったのだ","もしかしたら ／ だということだ"],2,
           "[もしかすると]…驚くような名前[かもしれない] = EHTIMOL…hayratlanarli nom BO'LSA KERAK.",blankNo="20",expl="もしかすると〜かもしれない = ehtimol ...bo'lishi mumkin"),
         q("t7-g3-21",None,["だからといって","実は","それとも","または"],2,
           "[実は]、最近建物や道路が古くなって… = ASLIDA esa, yaqinda bino-yo'llar eskirib…",blankNo="21",expl="実は = aslida, rostini aytsa (ichki holatni ochish)"),
         q("t7-g3-22",None,["名前を変えた","名前が変わった","名前を変えずにいた","名前が変わっていた"],1,
           "商店街の人たちが[名前を変えた]のは…作戦の1つ = rasta ahli NOMNI O'ZGARTIRGANI…rejalardan biri.",blankNo="22",expl="名前を変えた = nomni o'zgartirdi (odamlar — o'timli fe'l, harakat egasi bor)"),
         q("t7-g3-23",None,["祈っているにちがいない","祈っている一方だ","祈りたいにすぎない","祈りたいものだ"],1,
           "効果が早く出ることを[祈っているにちがいない] = samara tez chiqishini TILAYOTGANIGA SHUBHA YO'Q.",blankNo="23",expl="〜にちがいない = ...ligi shubhasiz, albatta ...dir"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test07.json yozildi. Jami savol:", tot)
