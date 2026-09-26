# -*- coding: utf-8 -*-
"""
test09.json generatori — 第9回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.10, Savollar p.88-97
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test09.json")

def q(qid, stem, options, answer, tr, reading=None, expl=None, optsTr=None,
      prefix=None, suffix=None, starPos=None, order=None, blankNo=None):
    d = {"id": qid, "options": options, "answer": answer, "tr": tr}
    if stem is not None: d["stem"] = stem
    if reading: d["reading"] = reading
    if expl: d["explanation_uz"] = expl
    if optsTr: d["optsTr"] = optsTr
    if prefix is not None: d["prefix"] = prefix
    if suffix is not None: d["suffix"] = suffix
    if starPos is not None: d["starPos"] = starPos
    if order is not None: d["order"] = order
    if blankNo is not None: d["blankNo"] = blankNo
    return d

data = {
  "id": 9,
  "title_jp": "第9回 模擬テスト",
  "title_uz": "9-test",
  "minutes": 45,
  "sections": [
    {
      "id": "vocab",
      "name_jp": "文字・語彙",
      "name_uz": "Kanji va lug'at",
      "problems": [
        {
          "id": "v1", "type": "kanji_reading",
          "instruction_jp": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida eng to'g'risini tanlang.",
          "questions": [
            q("t9-v1-1", "【標準的】な体重なのに、太っていると悩む女性が多い。",
              ["すいじゅん", "すいしゅん", "ひょうじゅん", "ひょうしゅん"], 3,
              "Vazni me'yoriy (standart) bo'lsa ham, semizman deb xavotirlanadigan ayollar ko'p.",
              reading="ひょうじゅん", expl="標準的 → ひょうじゅんてき (me'yoriy, standart)"),
            q("t9-v1-2", "国会では、与党と野党の【攻防】が続いている。",
              ["せいぼう", "こうぼう", "せいほう", "こうほう"], 2,
              "Parlamentda hukmron partiya va muxolifat partiyasi o'rtasida hujum va mudofaa (keskin kurash) davom etmoqda.",
              reading="こうぼう", expl="攻防 → こうぼう (hujum va himoya, keskin kurash)"),
            q("t9-v1-3", "人間ドックは医師から1対1で検査結果の【詳しい】説明が受けられる。",
              ["とぼしい", "ただしい", "くわしい", "きびしい"], 3,
              "To'liq tibbiy ko'rikda (Ningen Dock) shifokordan yakkama-yakka tekshiruv natijalarining batafsil tushuntirishini olish mumkin.",
              reading="くわしい", expl="詳しい → くわしい (batafsil, mufassal)"),
            q("t9-v1-4", "大学生の学力低下の原因は入試制度の【欠陥】だと主張する人は多い。",
              ["けっかん", "けってん", "けっぽう", "けつらく"], 1,
              "Talabalar bilim darajasi pasayishining sababi qabul imtihonlari tizimidagi nuqson (kamchilik) deb hisoblaydiganlar ko'p.",
              reading="けっかん", expl="欠陥 → けっかん (nuqson, kamchilik, defekt)"),
            q("t9-v1-5", "国道沿いの【立て看板】にはかなりの広告効果がある。",
              ["だてかんばん", "たてかんばん", "たてがんばん", "だてがんはん"], 2,
              "Magistral yo'l bo'yidagi o'rnatma reklama taxtasi (shit) ancha yuqori reklama samarasiga ega.",
              reading="たてかんばん", expl="立て看板 → たてかんばん (tik turuvchi reklama taxtasi/shiti)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t9-v2-6", "受験する大学を決めたものの、これで本当にいいのかと気持ちが【ゆらぐ】。",
              ["緩らぐ", "揺らぐ", "震らぐ", "振らぐ"], 2,
              "Imtihon topshiradigan universitetni tanlagan bo'lsam-da, rostdan ham shu to'g'rimi deb ko'nglim ikkilanmoqda (chayqalmoqda).",
              reading="ゆらぐ", expl="揺らぐ → ゆらぐ (chayqalmoq, ikkilanmoq, beqaror bo'lmoq)"),
            q("t9-v2-7", "人生は【よき】せぬことの連続なんだから、あまりくよくよしないほうがいいよ。",
              ["与期", "余期", "世期", "予期"], 4,
              "Hayot kutilmagan hodisalarning ketma-ketligidan iborat, shuning uchun ko'p ham siqilmaslik kerak.",
              reading="よき", expl="予期 → よき (oldindan kutish/rejalash; 予期せぬ = kutilmagan)"),
            q("t9-v2-8", "この本は内容が【こくて】満足した。",
              ["濃くて", "巧くて", "厚くて", "密くて"], 1,
              "Bu kitobning mazmuni juda boy (mazmundor/to'laqonli) bo'lib, meni qoniqtirdi.",
              reading="こくて", expl="濃い → こい (quyug', boy, mazmundor)"),
            q("t9-v2-9", "地雷は長期にわたって無差別に人々を【ねらい】続ける、恐ろしい兵器だ。",
              ["盗い", "襲い", "狙い", "追い"], 3,
              "Mina uzoq vaqt davomida insonlarni farqsiz nishonga olib keluvchi dahshatli quroldir.",
              reading="ねらい", expl="狙う → ねらう (mo'ljalga olmoq, nishonga olmoq)"),
            q("t9-v2-10", "帰宅【とちゅう】にバイクに乗った男にバッグをひったくられた。",
              ["避中", "途中", "道中", "逐中"], 2,
              "Uyga qaytish yo'lida mototsikldagi kishi sumkamni yulqib qochdi.",
              reading="とちゅう", expl="途中 → とちゅう (yo'l ustida, o'rtasida)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t9-v3-11", "私の料理はだれかに習ったのではなく、まったくの自己（　）です。",
              ["風", "法", "流", "様"], 3,
              "Mening taom pishirishim birovdan o'rganilgan emas, butunlay o'zimning uslubimdir (o'zicha o'rgangan).",
              expl="自己流 (じこりゅう) = o'ziga xos shaxsiy uslub"),
            q("t9-v3-12", "現代人は1日に1万歩歩くだけの運動（　）が必要だそうだ。",
              ["料", "量", "力", "性"], 2,
              "Zamonaviy insonlarga kuniga 10 000 qadam yurishga teng jismoniy harakat miqdori zarur emish.",
              expl="運動量 (うんどうりょう) = jismoniy mashq / harakat hajmi"),
            q("t9-v3-13", "おもしろい記事が地方（　）に載っていた。",
              ["判", "系", "番", "紙"], 4,
              "Qiziqarli maqola mahalliy gazetada chop etilgan ekan.",
              expl="地方紙 (ちほうし) = mahalliy gazeta/nashr"),
            q("t9-v3-14", "予想（　）の人物が新社長になった。",
              ["末", "下", "済", "外"], 4,
              "Kutilmagan (taxminlardan tashqari) shaxs yangi prezident (bosh direktor) bo'ldi.",
              expl="予想外 (よそうがい) = kutilmagan, taxmindan tashqari"),
            q("t9-v3-15", "一人っ子の彼は依頼（　）が強い。",
              ["心", "性", "力", "内"], 1,
              "Yakka-yagona farzand bo'lgan u yigitda boshqalarga suyanish hissi (qaramlik) kuchli.",
              expl="依頼心 (いらいしん) = boshqalarga suyanish/tayanib yashash tuyg'usi")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t9-v4-16", "母は（　）てよく財布を持たずに買い物に行ってしまう。",
              ["そそっかしく", "にぶく", "おしく", "ずうずうしく"], 1,
              "Oyim shoshqaloqlik qilib ko'pincha hamyonini olmasdan bozorga ketib qoladi.",
              reading="そそっかしい", expl="そそっかしい = shoshqaloq, parishonxotir"),
            q("t9-v4-17", "睡眠のリズムが（　）しまい、最近眠れなくなってしまった。",
              ["失って", "狂って", "送って", "違って"], 2,
              "Uyqu tartibim buzilib ketib, so'nggi paytlarda uxlay olmaydigan bo'lib qoldim.",
              reading="くるって", expl="（リズムが）狂う = ritm/tartib izdan chiqmoq, buzilmoq"),
            q("t9-v4-18", "この場合、特殊な（　）なので保険金は支払われません。",
              ["レース", "ペース", "リース", "ケース"], 4,
              "Ushbu holatda bu maxsus holat (vaziyat) bo'lgani uchun sug'urta to'lovi to'lanmaydi.",
              expl="ケース (case) = holat, vaziyat, hodisa"),
            q("t9-v4-19", "今の若者は給料が（　）上がりに増えたバブルの時代を知らない世代である。",
              ["盛り", "成り", "右肩", "仕立"], 3,
              "Hozirgi yoshlar maosh muttasil o'sib borgan ko'tarilish (babbl) davrini bilmaydigan avloddir.",
              reading="みぎかた", expl="右肩上がり (みぎかたあがり) = muntazam o'sish/ko'tarilish"),
            q("t9-v4-20", "（　）あなたの携帯電話を見たのではなく、私のと間違えてしまったのです。",
              ["うっかり", "わざと", "まさか", "ふと"], 2,
              "Qasddan (atayin) telefoningizga qaraganim yo'q, o'zimniki bilan adashtirib qo'ydim.",
              reading="わざと", expl="わざと = qasddan, atayin"),
            q("t9-v4-21", "なかなか取れない疲労は、体の（　）を示すことが多い。",
              ["非常", "異常", "救急", "休息"], 2,
              "Hech ketmaydigan surunkali charchoq tanadagi anomaliya / nosozlikdan dalolat berishi ko'p uchraydi.",
              reading="いじょう", expl="異常 (いじょう) = noodatiy holat, anomaliya, nosozlik"),
            q("t9-v4-22", "親の経済力に関係なく、能力のある生徒が大学に進学できるよう（　）の制度を拡大すべきだ。",
              ["奨学金", "保証金", "手付金", "入学金"], 1,
              "Ota-onasining moddiy ahvolidan qat'i nazar, iqtidorli o'quvchilar universitetga kira olishi uchun stipendiya (grant) tizimini kengaytirish kerak.",
              reading="しょうがくきん", expl="奨学金 (しょうがくきん) = stipendiya, grant")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t9-v5-23", "彼は電話を切ると【あわただしく】部屋を出ていった。",
              ["さっさと", "うろうろと", "そうっと", "ゆうゆうと"], 1,
              "U telefonni qo'yishi bilanoq shoshilinch ravishda (chaqqon) xonadan chiqib ketdi.",
              reading="あわただしく", expl="あわただしく ≈ さっさと (tezda, shoshilib)"),
            q("t9-v5-24", "語順を【さかさまにして】、表現を強調する。",
              ["変更", "考慮", "逆に", "無視"], 3,
              "So'z tartibini teskari qilib (almashtirib), ifodani kuchaytirmoqda.",
              reading="さかさまにして", expl="さかさまに ≈ 逆に (teskari qilib, o'rnini almashtirib)"),
            q("t9-v5-25", "オリンピックの準備は、【着々と】進んでいる。",
              ["順調に", "徐々に", "急速に", "意外に"], 1,
              "Olimpiada o'yinlariga tayyorgarlik bir maromda (muvaffaqiyatli) davom etmoqda.",
              reading="ちゃくちゃくと", expl="着々と ≈ 順調に (rejaga muvofiq, bir maromda o'ngidan kelib)"),
            q("t9-v5-26", "たかが風邪だと言って、【甘く見て】はいけません。",
              ["中断して", "停止して", "変更して", "油断して"], 4,
              "Oddiy shamollash deb e'tiborsiz (beparvo) qaramaslik kerak.",
              reading="あまくみて", expl="甘く見る ≈ 油断する (mensimaslik, beparvo/hushyorsiz qarash)"),
            q("t9-v5-27", "最近のテレビドラマは【マンネリ化している】。",
              ["評判が悪い", "新鮮味がない", "人気がある", "いい加減だ"], 2,
              "So'nggi paytlardagi teleseriallar bir xillik botqog'iga botgan (hech qanday yangiligi yo'q).",
              reading="まんねりかしている", expl="マンネリ化 ≈ 新鮮味がない (yangilik yo'q, bir xil zerikarli qolipga tushib qolgan)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'zning gapda eng to'g'ri ishlatilgan variantini tanlang.",
          "questions": [
            q("t9-v6-28", "【推定】の使い方として最もよいものを選びなさい。",
              [
                "子どもを失った親の悲しみはとても推定できない。",
                "病院で毎月血圧を推定しています。",
                "電話の声から推定すると、犯人は若い男性だ。",
                "人の秘密を推定するのはやめなさい。"
              ], 3,
              "推定 (suitei) = taxmin qilish, chamalash, xulosa chiqarish.",
              expl="「声から推定すると〜」= ovozidan taxmin qilinganda... (to'g'ri ishlatilish)."),
            q("t9-v6-29", "【ごぶさた】の使い方として最もよいものを選びなさい。",
              [
                "遅くなったので、そろそろごぶさたします。",
                "病気のため、会議はごぶさたさせてもらう。",
                "先日は突然お宅にごぶさたし、失礼いたしました。",
                "大学を卒業以来、先生にはすっかりごぶさたしている。"
              ], 4,
              "ごぶさた (gobusata) = uzoq vaqt xabar olmaslik / ko'rishmaslik.",
              expl="「先生にはすっかりごぶさたしている」= ustozdan ancha vaqt xabar ololmay uzrli holatdaman (to'g'ri ishlatilish)."),
            q("t9-v6-30", "【単純】の使い方として最もよいものを選びなさい。",
              [
                "たとえ単純な食事でもいいから朝食は食べなさい。",
                "思ったよりも単純に運転免許が取れた。",
                "彼は単純な性格だから、細かいことは気にしないと思う。",
                "まさか1回戦で単純に負けてしまうとはだれも思わなかった。"
              ], 3,
              "単純 (tanjun) = sodda, jo'n, samimiy.",
              expl="「単純な性格」= sodda/samimiy fe'l-atvor (to'g'ri ishlatilish)."),
            q("t9-v6-31", "【足元】の使い方として最もよいものを選びなさい。",
              [
                "お互いこんな足元に住んでいるとは知らなかった。",
                "お酒を飲みすぎて足元がふらつき、ひとりで歩けない。",
                "親の足元を離れてからもうだいぶたった。",
                "買い物は足元の店で済ますことが多い。"
              ], 2,
              "足元 (ashimoto) = qadam bosish holati, oyoq osti.",
              expl="「足元がふらつき」= mastlikdan qadamlari chayqalib... (to'g'ri ishlatilish)."),
            q("t9-v6-32", "【超過】の使い方として最もよいものを選びなさい。",
              [
                "最近はうつ病患者が超過している。",
                "タクシー会社は深夜の料金を超過する。",
                "家を建てたのだが、最初の予算をかなり超過してしまい大変だ。",
                "薬を超過するときは必ず医師に相談してください。"
              ], 3,
              "超過 (chouka) = me'yordan / limitdan oshib ketish.",
              expl="「予算をかなり超過してしまい」= byudjetdan ancha oshib ketib... (to'g'ri ishlatilish).")
          ]
        }
      ]
    },
    {
      "id": "grammar",
      "name_jp": "文法",
      "name_uz": "Grammatika",
      "problems": [
        {
          "id": "g1", "type": "grammar_form",
          "instruction_jp": "次の文の（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi qavs ichiga eng mos keluvchi grammatik shaklni tanlang.",
          "questions": [
            q("t9-g1-33", "ずっと昔から、この川の流れ（　）町が発展してきた。",
              ["に連れて", "に沿って", "に並べて", "に並んで"], 2,
              "Juda qadimdan bu daryo oqimi bo'ylab shahar rivojlanib kelgan.",
              expl="「〜に沿って」= ...yoqalab, bo'ylab."),
            q("t9-g1-34", "村にダムを作るかどうか（　）、住民の意見は2つにわかれた。",
              ["を通じて", "をもとにして", "をまわって", "をめぐって"], 4,
              "Qishloqda to'g'on qurish-qurmaslik masalasi atrofida aholining fikri ikkiga bo'lindi.",
              expl="「〜をめぐって」= ...mavzusi atrofida / borasida (tortishuv)."),
            q("t9-g1-35", "できない子を教えること（　）、彼以上にうまい先生はいなかった。",
              ["にかけては", "にかかっては", "にかかわっては", "につけては"], 1,
              "O'zlashtirishi sust bolalarga dars berish bobida undan mohirroq ustoz yo'q edi.",
              expl="「〜にかけては」= ...sohasi/borasida eng zo'ri (mahorat ifodasi)."),
            q("t9-g1-36", "もし海外旅行に行ける（　）、ぜひエジプトのピラミッドを見たいものだ。",
              ["となると", "としても", "とすると", "としたら"], 4,
              "Agar chet elga sayohatga chiqa oladigan bo'lsam, albatta Misr ehromlarini ko'rishni orzu qilaman.",
              expl="「〜としたら」= agar ...bo'lsa (faraz qilish)."),
            q("t9-g1-37", "最後までだれも脱落する（　）、全員が卒業できました。",
              ["ことなく", "わけなく", "しかなく", "ほかなく"], 1,
              "Oxirigacha hech kim safdan chiqmasdan (tashlab ketmasdan), hamma bitirib chiqdi.",
              expl="「〜ことなく」= ...qilmasdan (rasmiy inkor)."),
            q("t9-g1-38", "結果は決まってしまった。今さらあれこれ（　）はじまらない。",
              ["言ったら", "言っても", "言うなら", "言わなくても"], 2,
              "Natija aniq bo'ldi. Endi bundan keyin u-bu deb gapirgan bilan foydasi yo'q.",
              expl="「〜て（も）はじまらない」= ...qilgan bilan foydasi yo'q / kech bo'ldi."),
            q("t9-g1-39", "たとえお金があっても、健康（　）人生は楽しめない。",
              ["ならでは", "なかぎり", "なくして", "ないでは"], 3,
              "Hatto puling ko'p bo'lsa ham, salomatliksiz hayotdan lazzatlanib bo'lmaydi.",
              expl="「〜なくして（は）」= ...siz, ...mavjud bo'lmasa."),
            q("t9-g1-40", "いつも小社のホームページを（　）、ありがとうございます。",
              ["ごらんになられていただき", "見させてくださり", "ごらんいただき", "見られてくださり"], 3,
              "Har doim bizning veb-saytimizni ko'rib borganingiz uchun tashakkur.",
              expl="「ご覧いただき」= ko'rib berganingiz / tomosha qilganingiz uchun (hurmat shakli)."),
            q("t9-g1-41", "この木の実（　）、あまりおいしくはない。",
              ["食べられたくもないが", "食べられなくもないが", "食べたくもないが", "食べたこともないが"], 2,
              "Bu daraxt mevasini yesa bo'ladi-ku (yeb bo'lmaydigan darajada emas), biroq unchalik mazali emas.",
              reading="たべられなくもないが", expl="「〜なくもない」= ...emas ham emas (qisman tasdiq)."),
            q("t9-g1-42", "部下が病気で休んでいる以上、私が代わりに彼の仕事を（　）。",
              ["するわけない", "するほかない", "しないわけない", "しないほかない"], 2,
              "Qo'l ostimdagi xodim kasallik sababli kelmagan ekan, uning o'rniga ishini bajarishdan boshqa ilojim yo'q.",
              expl="「〜以上（は） ...ほかない」= ...ekan, boshqa chora yo'q."),
            q("t9-g1-43", "A「健康のために何かしていますか。」\\nB「そうですね、毎日散歩に（　）。」",
              ["行くようになっています", "行ったようになっています", "行くことにしています", "行ったことにしています"], 3,
              "A: «Salomatlik uchun biron narsa qilasizmi?» — B: «Ha, har kuni sayr qilishni odat qilganman.»",
              expl="「〜ことにしている」= ...qilishni odat/qoida qilganman (shaxsiy qaror)."),
            q("t9-g1-44", "東京は土地がせまいから家が（　）、一生真面目に働いても買えないなんておかしい。",
              ["高くてもかまわないが", "高くてもしかたがないとはいえ", "高くてはかまわないが", "高くてはしかたがないとしても"], 2,
              "Tokioda yer maydoni torligi tufayli uy narxi qimmat bo'lishi tabiiy bo'lsa-da, butun umr halol ishlab ham sotib ololmaslik aqlga sig'maydi.",
              expl="「〜とはいえ」= ...bo'lishiga qaramasdan / bo'lsa ham.")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の＿★＿に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keladigan eng to'g'ri variantni tanlang.",
          "questions": [
            q("t9-g2-45", None,
              ["子どもがいる", "生活が苦しくなる", "からこそ", "というけれど"], 4,
              "Bolalar ko'p bo'lsa turmush qiyinlashadi deyishsa-da, bolalarim borligi uchungina astoydil ishlashga kuch paydo bo'ladi.",
              prefix="子どもがたくさんいると", suffix="仕事をがんばる力が出る。",
              starPos=2, order=[2, 4, 1, 3],
              expl="Tartib: 生活が苦しくなる(2) というけれど(4) 子どもがいる(1) からこそ(3) → Yulduzcha 2-o'rinda: というけれど(4)"),
            q("t9-g2-46", None,
              ["助け合いの気持ちが", "なるにつれ", "豊かに", "薄く"], 2,
              "Jamiyat boyib borgani sayin o'zaro bir-biriga yordam berish hissi so'nib bordi.",
              prefix="世の中が", suffix="なってきた。",
              starPos=2, order=[3, 2, 1, 4],
              expl="Tartib: 豊かに(3) なるにつれ(2) 助け合いの気持ちが(1) 薄く(4) → Yulduzcha 2-o'rinda: なるにつれ(2)"),
            q("t9-g2-47", None,
              ["とともに", "ときは", "とき", "きれいだったが"], 3,
              "Ushbu uy qurilgan vaqtda chiroyli bo'lgan bo'lsa-da, vaqt o'tishi bilan u yer-bu yerini ta'mirlash zarurati tug'ildi.",
              prefix="この家も建てた", suffix="あちこち修理が必要になってきた。",
              starPos=3, order=[2, 4, 3, 1],
              expl="Tartib: ときは(2) きれいだったが(4) とき(3) とともに(1) → Yulduzcha 3-o'rinda: とき(3)"),
            q("t9-g2-48", None,
              ["普通のカレー", "いっても", "じゃなくて", "と"], 2,
              "A: «Bugungi kechki ovqatga nima?» B: «Kari. Kari deganim bilan oddiy kari emas, hindcha uslubdagisi.»",
              prefix="A「今日の夕食は何かな。」\\nB「カレーよ。カレー", suffix="インド風のものよ。」",
              starPos=2, order=[4, 2, 1, 3],
              expl="Tartib: と(4) いっても(2) 普通のカレー(1) じゃなくて(3) → Yulduzcha 2-o'rinda: いっても(2)"),
            q("t9-g2-49", None,
              ["ほか", "より", "ない", "借りる"], 1,
              "Pulingiz yetishmayotgan bo'lsa, ota-onangizdan qarz olishdan boshqa ilojingiz yo'qdir.",
              prefix="お金が足りないなら、親に", suffix="だろうね。",
              starPos=3, order=[4, 2, 1, 3],
              expl="Tartib: 借りる(4) より(2) ほか(1) ない(3) → Yulduzcha 3-o'rinda: ほか(1)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlarga eng mos keluvchi javobni tanlang.",
          "passage": "日本では、電車やバスなど公共交通機関でのケータイの通話を禁止している。しかし、ときどき緊急の用事で通話している人を見かける事がある。手短に（注1）すむのならよいが、長々と話をしている人を見るとついイライラしてしまう。これと似たような経験をお持ちの方も多いだろう。\n　電車やバスで聞こえてくる会話はまったく【 50 】のに、ケータイは不快に感じてしまう。なぜかケータイは気になって仕方がない。この疑問をアメリカの心理学者が解明し、このほど科学誌に発表した。（中略）\n　電車内でのケータイ会話について研究を行ったのは、コーネル大学の心理学者ローレン・エンバーソン博士のチームだ。研究チームは対面会話とケータイを比較し、周りの人が受ける影響について実験を行った。\n　それによると、周りの人は聞こえてくる会話の内容が把握（注2）できないと、ストレスを感じるという。対面会話であれば、話の流れがなんとなくでも【 51-a 】、不必要な情報であれば【 51-b 】ことができる。一方、ケータイの場合は電話の向こうの声が聞き取れないため、話の流れが見えず、内容が気になって無視できなくなってしまうというのだ。「人間は簡単に想像のつくものに対して、無視することができる。しかし次に何が起こるか【 52 】に対しては、常に注意を払ってしまう。ケータイは話が【 53 】聞こえるために、無意識に話の全体像をつかもうと脳は緊張した状態を持続することになる」と、ローレン博士は説明している。\n　つまりケータイは、話している声だけでなく、その内容も周りのイライラの原因になっているようだ。公共交通機関でのケータイ使用は【 54 】。\n（ロケットニュース24　2010年9月20日付）",
          "questions": [
            q("t9-g3-50", None,
              ["気にならない", "気がつかない", "気にする", "気にいらない"], 1,
              "Poyezd yoki avtobusdagi oddiy suhbatlar aslo g'ashga tegmasa-da...",
              blankNo=50, expl="「気にならない (e'tibor tortmaydi/g'ashga tegmaydi)」"),
            q("t9-g3-51", None,
              ["a 無視でき ／ b 無視する", "a 理解でき ／ b 無視する", "a 理解でき ／ b 理解する", "a 無視でき ／ b 理解する"], 2,
              "a: 理解でき (tushunish mumkin bo'lib), b: 無視する (e'tibor bermay qo'yish).",
              blankNo=51, expl="51-a ga «理解でき» (tushunib olinib), 51-b ga esa «無視する» (keraksiz bo'lsa e'tiborsiz qoldirish) mos tushadi."),
            q("t9-g3-52", None,
              ["想像できるもの", "理解できるもの", "無視できるもの", "わからないもの"], 4,
              "...ammo keyin nima bo'lishi noma'lum bo'lgan narsaga nisbatan doimo miya diqqat qaratadi.",
              blankNo=52, expl="「何が起こるかわからないもの」= nima bo'lishi tushunarsiz/noma'lum bo'lgan narsa."),
            q("t9-g3-53", None,
              ["全部", "全然", "半分だけ", "半分しか"], 3,
              "Telefon suhbatida gapning faqat yarmi eshitilgani sababli...",
              blankNo=53, expl="「半分だけ」= faqat yarmi (bir tomonlama ovoz)."),
            q("t9-g3-54", None,
              ["控えてはならない", "控えるものではない", "控えるべきだろう", "控えるわけだろう"], 3,
              "Jamoat transportida telefon orqali gaplashishni cheklash lozim bo'lsa kerak.",
              blankNo=54, expl="「控えるべきだろう」= o'zini tiyish / cheklash lozim bo'lsa kerak.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK! test09.json yaratildi: {len(data['sections'][0]['problems'])} vocab + {len(data['sections'][1]['problems'])} grammar bo'limlari.")
