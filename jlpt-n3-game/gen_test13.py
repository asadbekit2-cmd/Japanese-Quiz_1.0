# -*- coding: utf-8 -*-
"""test13.json — 第13回 模擬テスト (PDF betlari 128-137, javob 206)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test13.json")

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
  "id": 13, "title_jp": "第13回 模擬テスト", "title_uz": "13-test", "minutes": 50,
  "sections": [
    {"id": "vocab", "name_jp": "文字・語彙", "name_uz": "Kanji va lug'at", "problems": [
      {"id": "v1", "type": "kanji_reading",
       "instruction_jp": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
       "questions": [
         q("t13-v1-1","プレゼントにリボンが【結んで】ありました。",["あんで","たたんで","はさんで","むすんで"],4,"Sovg'aga lenta bog'lab qo'yilgan edi.",reading="むすんで",expl="結ぶ → むすぶ (bog'lamoq)"),
         q("t13-v1-2","この病院は、【患者】の数が多い。",["かんしゃ","がんしゃ","かんじゃ","がんじゃ"],3,"Bu kasalxonada bemorlar soni ko'p.",reading="かんじゃ",expl="患者 → かんじゃ (bemor, kasal)"),
         q("t13-v1-3","そのやり方で、【効果】がありますか。",["きょか","きょうか","こか","こうか"],4,"U usul bilan natija bor (samara beradi)mi?",reading="こうか",expl="効果 → こうか (samara, natija)"),
         q("t13-v1-4","苦しいとき、クラスメートに【支えて】もらった。",["おしえて","ささえて","つかえて","かかえて"],2,"Qiyin paytda sinfdoshim menga tayanchlik qildi (qo'llab-quvvatladi).",reading="ささえて",expl="支える → ささえる (tayanch bo'lmoq, qo'llab-quvvatlamoq)"),
         q("t13-v1-5","この【城】はとても有名です。",["しろ","とう","てら","もん"],1,"Bu qal'a (shahar) juda mashhur.",reading="しろ",expl="城 → しろ (qal'a, qo'rg'on)"),
         q("t13-v1-6","用事があるので、お先に【失礼】します。",["つごう","しごと","ようじ","しょよう"],3,"Ishim bor, men oldin ketaman (uzr).",reading="ようじ",expl="用事 → ようじ (ish, yumush, vazifa)"),
         q("t13-v1-7","毎日、とても【退屈】だ。",["さいくつ","きゅうくつ","たいくつ","ていくつ"],3,"Har kuni juda zerikarlim (zerikarli).",reading="たいくつ",expl="退屈 → たいくつ (zerikish, zerikarlilik)"),
         q("t13-v1-8","新しい法案が【成立】した。",["せいりつ","ぜいりつ","しょうりつ","じょうりつ"],1,"Yangi qonun loyihasi qabul qilindi.",reading="せいりつ",expl="成立 → せいりつ (qabul qilinmoq, kuchga kirmoq — qonun/shartnoma)"),
       ]},
      {"id": "v2", "type": "orthography",
       "instruction_jp": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zni kanji bilan yozganda eng to'g'risini tanlang.",
       "questions": [
         q("t13-v2-9","日程については、メールで【つうち】します。",["通知","通告","報知","報告"],1,"Jadval haqida email orqali xabar beraman.",expl="つうち → 通知 (xabardor qilish, bildirish)"),
         q("t13-v2-10","彼は、必死に働いて、今の【ちい】についた。",["時位","自位","値位","地位"],4,"U jon-jahd ishlab, hozirgi maqomiga erishdi.",expl="ちい → 地位 (maqom, lavozim, o'rin)"),
         q("t13-v2-11","カップラーメンにお湯を【そそいで】、3分待った。",["主いで","注いで","往いで","往いで"],2,"Stakan lapmonga qaynoq suv quyib, 3 daqiqa kutdim.",expl="そそぐ → 注ぐ (quymoq — suyuqlik)"),
         q("t13-v2-12","友だちを家に【まねく】。",["積く","届く","描く","招く"],4,"Do'stimni uyga taklif qilaman.",expl="まねく → 招く (taklif qilmoq, chaqirmoq)"),
         q("t13-v2-13","見つけたお金を【けいさつ】に持っていった。",["警官","警察","検察","検事"],2,"Topgan pulni politsiyaga olib bordim.",expl="けいさつ → 警察 (politsiya)"),
         q("t13-v2-14","この国では、石油の【ゆしゅつ】が増えている。",["移出","移入","輸出","輸入"],3,"Bu mamlakatda neft eksporti o'sib bormoqda.",expl="ゆしゅつ → 輸出 (eksport, tashqariga chiqarish)"),
       ]},
      {"id": "v3", "type": "context",
       "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "( ) ga qo'yish uchun eng mos so'zni tanlang.",
       "questions": [
         q("t13-v3-15","父は、（　）の運転手だったのに、仕事中に事故を起こした。",["アマチュア","スマート","ベテラン","ピーク"],3,"Otam tajribali haydovchi bo'la turib, ish paytida avariya qildi.",expl="ベテラン = tajribali mutaxassis (veteran)"),
         q("t13-v3-16","英語の本を日本語に（　）した。",["違約","要約","通訳","翻訳"],4,"Inglizcha kitobni yaponchaga tarjima qildim.",expl="翻訳 = yozma tarjima (翻訳する = tarjima qilmoq)"),
         q("t13-v3-17","運動をしなくなってから、（　）がなくなってきた。",["人体","本体","体格","体力"],4,"Sport qilishni to'xtatganimdan beri jismoniy quvvatim (kuchim) yo'qoldi.",expl="体力 = jismoniy quvvat, chidamlilik"),
         q("t13-v3-18","洗たくに失敗し、シャツが（　）小さくなってしまった。",["冷えて","こげて","縮んで","伸びて"],3,"Kir yuvishda xato qilib, ko'ylak kichirayib qoldi.",expl="縮む → 縮んで = kichirayib (qisqarib) qolmoq"),
         q("t13-v3-19","彼女に秘密を（　）された。",["告白","宣言","会話","通話"],3,"U sirini menga aytib berdi (ichini to'kdi).",expl="会話 = suhbat; 秘密を会話された = siri haqida gaplashildi (aytib qo'yildi)"),
         q("t13-v3-20","この魚は、私の国では高級（　）です。",["物","者","品","体"],3,"Bu baliq mening mamlakatimda yuqori sinfli mahsulot.",expl="高級品 = yuqori sifatli mahsulot (品 = tovar, mahsulot)"),
         q("t13-v3-21","ドアを（　）したのに、だれも出て来なかった。",["ヒット","ノック","プレー","チャイム"],2,"Eshikni taqillatdim, ammo hech kim chiqmadi.",expl="ノック(する) = taqillatmoq (eshikni)"),
         q("t13-v3-22","車をもっと右（　）に止めてください。",["寄り","止め","置き","並べ"],1,"Mashinani o'ng tomonga surib to'xtating.",expl="右寄り = o'ng tomonga surilgan (寄り = tomonga)"),
         q("t13-v3-23","母は、（　）して私を育ててくれた。",["緊張","否定","苦労","要求"],3,"Onam qiyinchilik bilan meni tarbiyalab o'stirdi.",expl="苦労(する) = qiyinchilik chekmoq, mehnat qilmoq"),
         q("t13-v3-24","好きな人に顔を見つめられて、（　）した。",["ほかほか","ふらふら","どきどき","はらはら"],3,"Yoqtirgan odamim menga tikilganida, yuragim duk-duk urdi.",expl="どきどき(する) = yurak duk-duk urmoq (hayajonlanmoq)"),
         q("t13-v3-25","私のペットの犬は、とても（　）だ。",["快速","温暖","急速","利口"],4,"Uy itim juda aqlli.",expl="利口 = aqlli, ziyrak (hayvon uchun ham ishlatiladi)"),
       ]},
      {"id": "v4", "type": "paraphrase",
       "instruction_jp": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin variantni tanlang.",
       "questions": [
         q("t13-v4-26","くやしい気持ちを日記に書いた。",["うれしい","満足な","さびしい","残念な"],4,"Afsuslanish hissini kundalikka yozdim.",expl="くやしい = afsus, o'kinch → 残念な"),
         q("t13-v4-27","進足について、みんなの意見は【ばらばらだ】。",["全部同じ","全部ちがう","二つにわかれた","賛成でまとまった"],2,"Jadval haqida hammaning fikri turlicha (tarqoq).",expl="ばらばら = tarqoq, har xil → 全部ちがう"),
         q("t13-v4-28","このセーターは、あなたに【ぴったりです】。",["大きすぎます","小さすぎます","似合います","似合いません"],3,"Bu sviter sizga juda mos.",expl="ぴったり = aynan mos, to'g'ri kelmoq → 似合います"),
         q("t13-v4-29","意見を必ず【述べて】ください。",["話して","聞いて","出して","考えて"],1,"Fikringizni albatta bildiring (aytib bering).",expl="述べる = bayon etmoq, aytmoq → 話して"),
         q("t13-v4-30","山小屋にあったのは、【わずかな】食べ物だった。",["たくさんの","少しの","残りの","あまりの"],2,"Tog' kulbasida oz miqdorda ovqat bor edi.",expl="わずか = juda oz, kamchilik → 少しの"),
       ]},
      {"id": "v5", "type": "usage",
       "instruction_jp": "次のことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilishini tanlang.",
       "questions": [
         q("t13-v5-31","飼う",
           ["私の家では、子どもを2人飼っている。","花を飼いたいと思って、花屋へ行きました。","子どものころ、家で牛と馬を飼っていました。","木の上で、親鳥が子どもの鳥を飼っています。"],3,
           "飼う(かう) = (hayvon) boqmoq, parvarishlamoq.",
           optsTr=["Uyimizda 2 ta bola «boqilmoqda» (noto'g'ri — 育てる kerak).","Gul «boqmoq» istab gulchilikka bordim (noto'g'ri — 買う kerak).","Bolaligimda uyda sigir va ot boqardik. (to'g'ri) ✓","Daraxt ustida ota qush bolasini «boqmoqda» (noto'g'ri — 育てる kerak)."]),
         q("t13-v5-32","なぐる",
           ["怒った男性は、もう1人の男性を力いっぱいなぐった。","そのサッカー選手は、右足で思いきりボールをなぐった。","交差点で車と自転車がなぐって、大きな事故になった。","部屋に入る前には、ドアをなぐってください。"],1,
           "なぐる = musht urmoq, urib yubormoq (odamga).",
           optsTr=["Jahli chiqqan erkak boshqa erkakni bor kuchi bilan urdi. (to'g'ri) ✓","Futbolchi to'pni musht urdi (noto'g'ri — 蹴る kerak).","Chorrahada mashina va velosiped musht urib ketdi (noto'g'ri — ぶつかる kerak).","Xonaga kirish oldidan eshikni musht uring (noto'g'ri — ノックする kerak)."]),
         q("t13-v5-33","隅",
           ["授業の隅で、先生が大事なことを言いました。","部屋の隅に、小さないすが置いてあります。","もう12月なので、1年も隅ですね。","髪の毛の隅に、ごみがついていました。"],2,
           "隅(すみ) = burchak (xona, joy).",
           optsTr=["Darsning «burchagida» o'qituvchi muhim narsa aytdi (noto'g'ri — 隅 = jismoniy burchak).","Xona burchagida kichkina stul turadi. (to'g'ri) ✓","Dekabr bo'lgani uchun yil ham «burchag'i»... (noto'g'ri — 終わり kerak).","Sochning «burchagiga» axlat yopishdi (noto'g'ri — 先端 kerak)."]),
         q("t13-v5-34","背中",
           ["あの男の人は、とても背中が高い。","朝から何も食べていないので、背中がすきました。","田中さんの家は、私の家の背中にあります。","ずっとパソコンに向かって座っていたら、背中が痛くなった。"],4,
           "背中(せなか) = orqa (tana qismi).",
           optsTr=["U erkakning «orqasi» juda baland (noto'g'ri — 背が高い = bo'yi baland).","Yemadim, «orqam» och bo'ldi (noto'g'ri — おなかがすく kerak).","Tanakaning uyi mening uyimning «orqasida» (noto'g'ri — 後ろ kerak).","Uzoq kompyuter oldida o'tirdim, belim og'ridi. (to'g'ri) ✓"]),
         q("t13-v5-35","単純",
           ["その事件は、ある単純な夜に起こった。","この問題は、とても単純なので答えがすぐわかるでしょう。","地震のときは、単純なものを持って逃げてください。","すばらしい映画を見て、とても単純な気持ちになった。"],2,
           "単純(たんじゅん) = oddiy, sodda.",
           optsTr=["U voqea «oddiy» bir kechada bo'ldi (noto'g'ri — 文脈が不自然).","Bu masala juda oddiy, javob tez topilsa kerak. (to'g'ri) ✓","Zilzilada «oddiy» narsalar olib qoching (noto'g'ri — 必要な kerak).","Ajoyib film ko'rib, juda «oddiy» his-tuyg'uga keldim (noto'g'ri — 感動 kerak)."]),
       ]},
    ]},
    {"id": "grammar", "name_jp": "文法", "name_uz": "Grammatika", "problems": [
      {"id": "g1", "type": "grammar_form",
       "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
       "questions": [
         q("t13-g1-1","では、開会（　）あたり、代表よりあいさつがございます。",["に","を","と","が"],1,"Endi, yig'ilishni ochish munosabati bilan, vakil so'z so'zlaydi.",expl="〜にあたり/あたって = ...munosabati bilan, ...paytida (rasmiy)"),
         q("t13-g1-2","吉田「よろしくお願いします。」山崎「こちら（　）よろしく。」",["まで","ほど","こそ","から"],3,"Yoshida: «Iltimos, yaxshi munosabatda bo'ling.» Yamazaki: «Men ham sizga minnatdorman.»",expl="〜こそ = aynan..., men ham... (ta'kidlash/qaytarish iborasi)"),
         q("t13-g1-3","なんでもできるあの人の（　）、この仕事もちゃんとやってくれると思います。",["ことに","ことには","ことから","ことだから"],4,"Hamma narsani qila oladigan u odamning tabiatidan kelib chiqib, bu ishni ham to'g'ri bajaradi deb o'ylayman.",expl="〜ことだから = ...tabiatini yaxshi bilgandan, ...bo'lgani uchun (shaxsga xos xulq)"),
         q("t13-g1-4","林さん（　）、ゼミの発表をすることはできない。",["なく","抜きで","いないで","切りで"],2,"Hayashi janobsiz seminar taqdimotini qilish mumkin emas.",expl="〜抜きで = ...siz, ...ni istisno qilib (〜がない状態で)"),
         q("t13-g1-5","今年の夏は、天気予報がはずれ、暑い（　）とてもすずしい。",["に反して","どころか","にもかかわらず","にしては"],2,"Bu yilgi yoz ob-havo bashorati to'g'ri kelmadi: issiq emas, aksincha juda salqin.",expl="〜どころか = ...balki aksincha (kutilgan narsaning teskari ekanligi ta'kidlanadi)"),
         q("t13-g1-6","お金がかかる今までのやり方（　）、鈴木君の案なら費用がかからず安くできる。",["によって","に対して","につれて","にこたえて"],2,"Qimmat bo'lgan avvalgi usulga nisbatan, Suzuki janobning taklifi arzon amalga oshiriladi.",expl="〜に対して = ...ga nisbatan, ...bilan solishtirganda (qarama-qarshilik)"),
         q("t13-g1-7","友だちと別れてつらかったが、時間が（　）につれ、悲しい気持ちも消えていった。",["たつ","たって","たった","たてば"],1,"Do'stimdan ajralish og'ir bo'ldi, ammo vaqt o'tishi bilan qayg'u ham yo'qoldi.",expl="時間がたつにつれ = vaqt o'tgan sari (〜につれ = ...ga qarab, ...ga mos ravishda)"),
         q("t13-g1-8","客「すみませんが、こちらの電話を（　）いただいてもよろしいですか。」社員「はい、どうぞ。」",["使われて","使わせて","使ったら","使って"],2,"Mijoz: «Kechirasiz, bu telefondan foydalansam bo'ladimi?» Xodim: «Ha, marhamat.»",expl="〜(さ)せていただいてもよろしいでしょうか = ...qilsam bo'ladimi? (ruxsat so'rashning odobli shakli)"),
         q("t13-g1-9","ペンがないので先生のものを（　）。",["貸してもよろしいですか","返してもよろしいですか","貸してくださいませんか","返してくださいませんか"],3,"Qalamim yo'q, shuning uchun o'qituvchimnikini olar edim (bersangiz bo'ladimi)?",expl="〜てくださいませんか = iltimos ...ib bering (〜てくれる ning hurmatli shakli)"),
         q("t13-g1-10","五木「山下さんがまだ来ていないんですが。」小林「本当ですか？きのう電話で出席すると言っていたので、（　）。」",["来ないはずですよ","来ないことですよ","来ないはずがないですよ","来ないことがないですよ"],3,"Itsuki: «Yamashita hali kelmadi.» Kobayashi: «Rostdanmi? Kecha kelaman deb aytgan edi, albatta keladi (kelmasligi mumkin emas).»",expl="〜ないはずがない = ...masligi mumkin emas (ishonch ifodalaydi)"),
         q("t13-g1-11","イベントの準備に時間と費用がかかっているのだから、参加人数が少なくても、最後まで（　）。",["やるしかありません","やるわけがありません","やってはなりません","やるものではありません"],1,"Tadbir tayyorgarligiga vaqt va pul sarflangan, shuning uchun ishtirokchilar oz bo'lsa ham, oxirigacha davom ettirishdan boshqa iloj yo'q.",expl="〜しかない = ...dan boshqa iloj yo'q (qaror, belgilangan yo'l)"),
         q("t13-g1-12","日本料理ではすしが有名ですが、私はべつに（　）。",["好きなのです","好きなようです","好きなわけです","好きではありません"],4,"Yapon oshxonasida sushi mashhur, ammo men shaxsan uni yoqtirmayman.",expl="べつに〜ない = alohida...emas, xususan...emas (inkor)"),
         q("t13-g1-13","こんな寒い日には、あたたかいものを（　）。",["飲まないに限る","飲むに限る","飲まないに限らない","飲むに限らない"],2,"Bunday sovuq kunda issiq narsa ichish eng yaxshisi.",expl="〜に限る = ...eng yaxshisi, ...dan ustun yo'q"),
       ]},
      {"id": "g2", "type": "sentence_order",
       "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng mos bo'lakni tanlang.",
       "questions": [
         q("t13-g2-14",None,["に","ため","調査","かかった"],2,"To'g'ri jumla: «Bu hisobotni tuzish uchun sarflangan tadqiqot muddati to'rt oy bo'ldi.»",
           prefix="この報告書を作る",suffix="の期間は四か月だ。",starPos=1,order=[2,1,4,3],
           expl="To'g'ri tartib: ため→に→かかった→調査 (報告書を作るためにかかった調査)"),
         q("t13-g2-15",None,["どう","ご予定","これから","なさる"],4,"To'g'ri jumla: «Bugungi jadval tugadi, bundan keyin nima qilmoqchi edingiz?»",
           prefix="今日の予定はこれで終わりましたが、",suffix="ですか。",starPos=3,order=[3,1,4,2],
           expl="To'g'ri tartib: これから→どう→なさる→ご予定 (なさる = する ning hurmat shakli)"),
         q("t13-g2-16",None,["なんでも","ことには","なにが","成功させない"],4,"To'g'ri jumla: «Kompaniya uchun muhim bo'lgan bu ishni, har qanday holatda ham muvaffaqiyatli yakunlamasak, kompaniya bankrot bo'lib qoladi.»",
           prefix="会社にとって大事なこの仕事を、",suffix="会社が倒産してしまう。",starPos=3,order=[3,1,4,2],
           expl="To'g'ri tartib: なにが→なんでも→成功させない→ことには (〜ないことには = ...masdan bo'lmaydi)"),
         q("t13-g2-17",None,["ことに","いる","なって","食事をする"],3,"To'g'ri jumla: «Ertaga oila bilan ovqatlanish rejalashtirilgan, shuning uchun keyingi gal chaqir.»",
           prefix="明日は家族と",suffix="ので、また今度さそってくれるかな。",starPos=3,order=[4,1,3,2],
           expl="To'g'ri tartib: 食事をする→ことに→なって→いる (〜ことになっている = ...qilinishi belgilangan)"),
         q("t13-g2-18",None,["服を","ほしかった","ついでに","行った"],2,"To'g'ri jumla: «Uzoq vaqt bo'lgach Tokioga o'yingani borganim bahonasida, sotib olmоqchi bo'lgan kiyimni olib keldim.»",
           prefix="ひさしぶりに東京へ遊びに",suffix="買ってきた。",starPos=3,order=[4,3,2,1],
           expl="To'g'ri tartib: 行った→ついでに→ほしかった→服を (〜ついでに = ...bahonasida, ...paytida foydalanib)"),
       ]},
      {"id": "g3", "type": "text_grammar",
       "instruction_jp": "つぎの文章を読んで、19から23の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
       "instruction_uz": "Matnni o'qib, 19-23 bo'sh joylarga eng mos variantni tanlang.",
       "passage_title": "英語教育は本当に必要だろうか",
       "passage": (
         "日本では英語の教育はとても大事だという話を{{19}}。まず学校では、小学校から高校まで英語を"
         "学ぶ時間がある。また社会人になってからも、自分から、または会社に言われて英会話教室に通ったり、"
         "いろいろな検定試験を受けたりしている人はとても多い。\n"
         "まじめに勉強するのは、とてもいいことだと思うが、しかし、私の考えは少し違う。\n"
         "{{20}}、インターネットで海外の情報を集めるときや、海外旅行中、日本にいても外国人の観光客から"
         "道を聞かれたときなど、英語がわかると便利だと感じるときもある。しかし、目的もなく、「英語は"
         "大事だから」という理由で学習する必要があるのか、疑問を感じるのだ。\n"
         "{{21a}}、日本で生活し、日本の会社で働いているかぎり、英語を話さなければならない機会は"
         "ほとんどない{{21b}}。多くの日本人は、英語を話す人とつきあう機会も少ない。それなら、たとえば"
         "小学校では日本語を学ぶ時間をもっと増やしたり、会社員ならそれぞれの仕事に本当に必要なことを{{22}}。"
         "そうやって日本語の力や、{{23}}技術を身につけたほうが、自分のためになるのではないだろうか。"
       ),
       "passage_tr": (
         "Yaponiyadа ingliz tili ta'limi juda muhim degan gapni KO'P ESHITAMIZ. "
         "Avvalo maktablarda, boshlang'ichdan o'rta maktabgacha ingliz tili o'qitiladigan vaqt bor. "
         "Shuningdek, ishga kirganidan keyin ham o'zi ixtiyori bilan yoki kompaniya tavsiyasiga ko'ra "
         "ingliz tili kurslariga qatnaydiganlar, turli imtihon topshiradiganlar juda ko'p. "
         "Jiddiy o'qish yaxshi narsa, ammo mening fikrim biroz boshqacha. "
         "ALBATTA, internetdan xorijiy ma'lumot to'plaganda, xorijga sayohatda, Yaponiyada "
         "bo'lsada xorijiy sayyohlar yo'l so'raganda inglizcha bilish qulay bo'ladi. "
         "Biroq maqsadsiz, «ingliz tili muhim» degan sabab bilan o'rganish kerakmi, shunda shubha paydo bo'ladi. "
         "CHUNKI Yaponiyada yashab, yapon kompaniyasida ishlagancha inglizcha gapirish kerak bo'lgan "
         "holat deyarli yo'q, chunki shunday. Ko'pchilik yaponlar inglizcha gapiruvchilar bilan muloqot "
         "qilish imkoniyati ham kam. Shunday ekan, masalan, boshlang'ich maktabda yapon tili o'rganishga "
         "ko'proq vaqt ajratish yoki kompaniya xodimi bo'lsa har bir ishi uchun chinakam kerakli narsalarni "
         "O'RGANISH KERAK deb o'ylayman. Shunday qilib yapon tili kuchi va ZUDLIK BILAN FOYDALI bo'lgan "
         "ko'nikma egallash o'zi uchun foydali bo'lmaydi, deb o'ylamaysizmi."
       ),
       "questions": [
         q("t13-g3-19",None,["よく聞かれる","よく聞かせる","よく聞かされる","よく聞くようにさせる"],3,
           "英語教育は大事だという話を[よく聞かされる] = ...gapni KO'P ESHITAMIZ (majburiy eshitish — passiv).",
           blankNo="19",expl="よく聞かされる = passiv shaklda ko'p eshitiladigan (〜される = biror narsa qilinadi)"),
         q("t13-g3-20",None,["その後","確かに","だから","すると"],2,
           "[確かに]、インターネットで… = ALBATTA, internetda... (lekin keyin boshqacha fikr aytiladi).",
           blankNo="20",expl="確かに = albatta, to'g'ri (keyingi gapda «lekin» bilan ziddiyat ifodalanadi)"),
         q("t13-g3-21",None,["a ところが ／ b にきまっている","a ところで ／ b わけである","a なぜなら ／ b からである","a なぜ ／ b のだろうか"],3,
           "[なぜなら]…機会はほとんどない[からである] = CHUNKI...imkon deyarli yo'q, CHUNKI shunday.",
           blankNo="21",expl="なぜなら〜からである = chunki〜, sababi〜 (sabab-natija izohlovchi juft ibora)"),
         q("t13-g3-22",None,["学ばないほうがよいと思う","学ぶほうがよいと思わない","学ぶべきではないと思う","学ぶべきだと思う"],4,
           "仕事に必要なことを[学ぶべきだと思う] = ish uchun kerakli narsalarni O'RGANISH KERAK deb o'ylayman.",
           blankNo="22",expl="学ぶべきだと思う = o'rganish kerak deb o'ylayman (べき = ...lozim, ...kerak)"),
         q("t13-g3-23",None,["いつか役立つ","すぐに役立つ","ずっと役立たない","あまり役立たない"],2,
           "日本語の力や[すぐに役立つ]技術を… = yapon tili va ZUDLIK BILAN FOYDALI bo'lgan ko'nikmalar.",
           blankNo="23",expl="すぐに役立つ = darhol foydali bo'ladigan (zudlik bilan qo'l keladigan)"),
       ]},
    ]},
  ]
}

json.dump(data, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
tot = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print("test13.json yozildi. Jami savol:", tot)
