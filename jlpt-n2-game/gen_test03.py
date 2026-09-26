# -*- coding: utf-8 -*-
"""
test03.json generatori — 第3回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.4
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test03.json")

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
  "id": 3,
  "title_jp": "第3回 模擬テスト",
  "title_uz": "3-test",
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
            q("t3-v1-1", "ボランティア活動を【選択科目】に取り入れている大学が多くなっている。",
              ["せんだく", "ぜんだく", "せんたく", "ぜんたく"], 3,
              "Ko'ngillilik (volontyorlik) faoliyatini tanlov fanlariga kiritayotgan universitetlar ko'paymoqda.",
              reading="せんたく", expl="選択 → せんたく (tanlov) (選択科目 = tanlov fani)"),
            q("t3-v1-2", "飛行場を建設するには【膨大な】費用がかかる。",
              ["ほうだい", "ちょうだい", "ばくだい", "じんだい"], 1,
              "Aeroport qurish uchun juda ulkan (behiseb) xarajat ketadi.",
              reading="ぼうだい", expl="膨大 → ぼうだい (ulkan, bepoyon, behad ko'p)"),
            q("t3-v1-3", "軽く言ったつもりの【冗談】が友人を傷つけてしまった。",
              ["しょうだん", "じょだん", "じょうたん", "じょうだん"], 4,
              "Oddiy aytmoqchi bo'lgan hazilim do'stimning ko'nglini og'ritib qo'ydi.",
              reading="じょうだん", expl="冗談 → じょうだん (hazil, mutoyiba)"),
            q("t3-v1-4", "このまま人口が増え続ければ、世界中で食糧や水の【奪い合い】になるであろう。",
              ["きそい", "うばい", "あらそい", "うかがい"], 2,
              "Shu tarzda aholi o'sishda davom etsa, butun dunyoda oziq-ovqat va suv talashuvi (tortishuvi) yuzaga kelishi mumkin.",
              reading="うばいあい", expl="奪う → うばう (tortib olmoq) (奪い合い = tortishuv, talashuv)"),
            q("t3-v1-5", "最近は【防犯】性能が高いマンションや住宅を作るさまざまな取り組みが進んでいる。",
              ["ぜいのう", "しょうのう", "すうのう", "せいのう"], 4,
              "So'nggi paytlarda jinoyatchilikdan himoyalanish xususiyati (samaradorligi) yuqori bo'lgan uylarni barpo etish rivojlanmoqda.",
              reading="せいのう", expl="性能 → せいのう (ishchanlik qobiliyati, samaradorlik, unumdorlik)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t3-v2-6", "あのコーチは選手の【かくれた】能力を引き出すのがうまい。",
              ["隠れた", "陰れた", "隆れた", "隔れた"], 1,
              "U murabbiy sportchilarning yashiringan (ichki) qobiliyatini yuzaga chiqarishda juda mohir.",
              reading="かくれた", expl="隠れる → かくれる (yashirinmoq, pinhon bo'lmoq)"),
            q("t3-v2-7", "火山灰は電気けいとうに入り込み、さまざまな誤作動を起こすことがある。",
              ["計統", "形統", "系統", "経統"], 3,
              "Vulqon kuli elektr tizimiga (tarmoqqa) kirib borib, turli nosozliklarni keltirib chiqarishi mumkin.",
              reading="けいとう", expl="系統 → けいとう (tizim, tarmoq)"),
            q("t3-v2-8", "これから先、都市の建築物はますます【こうそう】化が進むであろう。",
              ["構想", "高層", "後送", "効相"], 2,
              "Bundan buyon shahar binolari tobora ko'p qavatli (baland qavatli) bo'lib borsa kerak.",
              reading="こうそう", expl="高層 → こうそう (baland qavatli, osmono'par)"),
            q("t3-v2-9", "人間は一生悩むことから【かいほう】されないのだと思う。",
              ["解倣", "解封", "解報", "解放"], 4,
              "Inson butun umr tashvishlardan aslo qutulolmasa (ozod bo'lolmasa) kerak deb o'ylayman.",
              reading="かいほう", expl="解放 → かいほう (ozod bo'lish, qutulish)"),
            q("t3-v2-10", "野菜や果物の栄養価は昔のものと【くらべて】低くなっている。",
              ["並べて", "比べて", "列べて", "対べて"], 2,
              "Sabzavot va mevalarning to'yimlilik darajasi ilgarigisi bilan solishtirganda pasayib bormoqda.",
              reading="くらべて", expl="比べる → くらべる (solishtirmoq, taqqoslamoq)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t3-v3-11", "（　）事情により今回のイベントは中止する。",
              ["多", "複", "重", "諸"], 4,
              "Turli holatlar (sabablar) tufayli ushbu tadbir bekor qilinadi.",
              expl="諸事情 (しょじじょう) = turli sabablar/sharoitlar"),
            q("t3-v3-12", "日曜日は家族で（　）帰りの旅行を楽しんだ。",
              ["日", "泊", "行", "出"], 1,
              "Yakshanba kuni oilaviy bir kunlik (borib-kelinadigan) sayohatdan zavqlandik.",
              expl="日帰り (ひがえり) = bir kunlik sayohat (tunab qolmasdan qaytish)"),
            q("t3-v3-13", "道路工事は（　）年度から始まる。",
              ["末", "来", "数", "真"], 2,
              "Yo'l qurilishi kelasi (moliyaviy) yildan boshlanadi.",
              expl="来年度 (らいねんど) = kelasi moliyaviy/o'quv yili"),
            q("t3-v3-14", "最新の機器を備えた近代（　）なビルが建設された。",
              ["風", "式", "的", "性"], 3,
              "Eng zamonaviy uskunalar bilan jihozlangan zamonaviy bino qad ko'tardi.",
              expl="近代的 (きんだいてき) = zamonaviy uslubdagi"),
            q("t3-v3-15", "的確な質問をよくしてくる彼には将来（　）を感じる。",
              ["感", "性", "化", "風"], 2,
              "Doim aniq-tiniq savollar beradigan bu yigitda kelajak porloqligini (potensialni) his qilaman.",
              expl="将来性 (しょうらいせい) = istiqbol, kelajak imkoniyatlari")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ( ) ga ma'no jihatidan eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t3-v4-16", "試験の出来ですか。すごくよくはなかったけど（　）だったと思います。",
              ["せいぜい", "そろそろ", "ゆうゆう", "まあまあ"], 4,
              "Imtihon qanday o'tdimi? Juda zo'r bo'lmadi-yu, ammo o'rtacha (yomon emas) bo'ldi deb o'ylayman.",
              expl="まあまあ = o'rtacha, durustgina, qoniqarli"),
            q("t3-v4-17", "彼女を動物に（　）と、気まぐれなところがネコっぽいね。",
              ["例える", "比べる", "たたえる", "こたえる"], 1,
              "Uni hayvonga qiyoslasak (o'xshatsak), injiq fe'l-atvori mushukka o'xshaydi.",
              expl="例える (たとえる) = o'xshatmoq, qiyoslamoq"),
            q("t3-v4-18", "なんでもすぐ行動に移す彼は、気が短い人間だと（　）されている。",
              ["評判", "結論", "誤解", "決定"], 3,
              "Har narsani darrov amalga oshiradigan u kishini hovliqma odam deb noto'g'ri tushunishadi (adashishadi).",
              expl="誤解 (ごかい) = noto'g'ri tushunish, yanglish xulosa"),
            q("t3-v4-19", "昔は貴族以外のまずしい人々は、小さくて（　）な家に住んでいた。",
              ["不利", "不幸", "地味", "粗末"], 4,
              "Ilgari zodagonlardan tashqari kambag'al insonlar kichik va abgor (oddiy/g'aribona) uylarda yashashgan.",
              expl="粗末 (そまつ) = oddiy, g'aribona, abgor"),
            q("t3-v4-20", "新入社員は、（　）な魅力にあふれている。",
              ["オープン", "フレッシュ", "ダイレクト", "ショック"], 2,
              "Yangi ishga kirgan xodimlar yangicha, jo'shqin (fresh) jozibaga to'ladir.",
              expl="フレッシュ (fresh) = yangi, jo'shqin, navqiron"),
            q("t3-v4-21", "この運動靴は歩きやすさとデザインのよさを（　）備えている。",
              ["持ち", "造り", "取り", "兼ね"], 4,
              "Bu sport poyabzali yurishga qulaylik va chiroyli dizaynni o'zida birgalikda mujassam etgan.",
              expl="兼ね備える (かねそなえる) = o'zida ikkala xususiyatni ham jamlamoq"),
            q("t3-v4-22", "この商店街で生活（　）はすべてそろう。",
              ["季節品", "必需品", "付属品", "消耗品"], 2,
              "Ushbu savdo ko'chasida hayot uchun zarur barcha kundalik ehtiyoj mollari topiladi.",
              expl="生活必需品 (せいかつひつじゅひん) = hayotiy zarur vositalar/tovarlar")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin sinonimni tanlang.",
          "questions": [
            q("t3-v5-23", "姉はいらないものまで【やたらに】買い込んでしまう。",
              ["考えなしに", "思いっきり", "絶えず", "大量に"], 1,
              "Opam keraksiz narsalargacha o'ylab-netmasdan (ketma-ket, pala-partish) sotib olaveradi.",
              reading="やたらに", expl="やたらに = 考えなしに (o'ylamasdan, duch kelganicha)"),
            q("t3-v5-24", "彼女は【隙のない】人だ。",
              ["余裕", "夢", "油断", "特徴"], 3,
              "U aslo bo'shashmaydigan (g'ofillik qilmaydigan, ehtiyotkor) inson.",
              reading="すきのない", expl="隙のない = 油断がない (ehtiyotkor, hushyor)"),
            q("t3-v5-25", "新しい法案作りを【慎重に】進める。",
              ["容易に", "計画的に", "注意深く", "素早く"], 3,
              "Yangi qonun loyihasini ishlab chiqishni ehtiyotkorlik bilan (sinchiklab) olib bormoqda.",
              reading="しんちょうに", expl="慎重に → 注意深く (diqqat va ehtiyotkorlik bilan)"),
            q("t3-v5-26", "事故を起こした会社の社長はマスコミに【叩かれた】。",
              ["質問された", "称賛された", "注目された", "非難された"], 4,
              "Avariya keltirib chiqargan kompaniya rahbari OAV tomonidan qattiq tanqid qilindi (qoralandi).",
              reading="たたかれた", expl="叩く (たたく) = 非難された (tanqid qilinmoq, qoralanmoq)"),
            q("t3-v5-27", "このギターは限定生産の【レアな】ものだ。",
              ["新しい", "めずらしい", "高い", "すばらしい"], 2,
              "Bu gitara cheklangan miqdorda chiqarilgan noyob (kamyob) buyumdir.",
              expl="レアな (rare) = めずらしい (noyob, kamyob)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Quyidagi so'zning eng to'g'ri ishlatilgan gapini tanlang.",
          "questions": [
            q("t3-v6-28", "恩恵", [
                "この祭りは自然の恩恵に浴する感謝を表している。",
                "お世話になった人に恩恵返しをする。",
                "この神社のお守りは恩恵があると評判だ。",
                "先生の恩恵で、無事卒業することができた。"], 1,
              "恩恵 (おんけい) = inoyat, ne'mat, foyda/naf.",
              optsTr=[
                "Bu festival tabiat ne'matlaridan bahramand bo'lganlik minnatdorchiligini bildiradi. (to'g'ri)",
                "Qaragan odamga 'ne'mat qaytaraman' (noto'g'ri — 恩返し).",
                "Bu tumor 'ne'matli' (noto'g'ri — ご利益).",
                "Ustozning 'ne'mati' bilan bitirdim (noto'g'ri — おかげ)."]),
            q("t3-v6-29", "素人", [
                "税金が上がって、素人の生活は苦しくなった。",
                "これはとても素人には作れない料理だ。",
                "どこの素人かわからない男に娘を嫁にやるわけにはいかない。",
                "彼女は素人だけあって、とても美しい。"], 2,
              "素人 (しろうと) = havaskor, nohaqiqiy mutaxassis.",
              optsTr=[
                "Soliq oshib, 'havaskorlar' turmushi qiyinlashdi (noto'g'ri — 庶民).",
                "Bu taomni havaskor (oddiy odam) aslo tayyorlay olmaydi. (to'g'ri)",
                "Qaysi 'havaskor' ekani noma'lum yigitga qizimni bermayman (noto'g'ri — 馬の骨).",
                "U 'havaskor' bo'lgani uchun chiroyli (noto'g'ri)."]),
            q("t3-v6-30", "だらしない", [
                "夫に家事を手伝ってもらったが、ちょっとだらしない。",
                "こんなつまらない仕事、だらしなくてやっていられない。",
                "そんなことで落ちこむなんて、だらしないやつだ。",
                "彼女はきちんと家計簿をつけていて、とてもお金にだらしない。"], 3,
              "だらしない = irodasiz, bo'sh, o'zini tutolmaydigan, betartib.",
              optsTr=[
                "Erim yordam berdi, lekin 'irodasiz' (noto'g'ri).",
                "Bunday zerikarli ishda 'irodasiz bo'lib' ishlab bo'lmaydi (noto'g'ri — ばかばかしい).",
                "Shunaqa arzimagan narsaga tushkunlikka tushadigan bo'sh, irodasiz ekansan-a! (to'g'ri)",
                "U hisob-kitobni aniq yuritadi va pulga 'pala-partish' (noto'g'ri — ziddiyat)."]),
            q("t3-v6-31", "重点", [
                "日本では、話すことより読む勉強に重点を置く学校がいまだ多い。",
                "この計画の成功の重点は君の活躍にかかっている。",
                "彼は長年財界の重点だった。",
                "あの作家の重点のある言葉が気に入っている。"], 1,
              "重点 (じゅうてん) = asosiy e'tibor, urg'u (重点を置く).",
              optsTr=[
                "Yaponiyada gapirishdan ko'ra o'qishga ko'proq urg'u beradigan (e'tibor qaratadigan) maktablar hali ham ko'p. (to'g'ri)",
                "Muvaffaqiyatning 'asosiy e'tibori' senga bog'liq (noto'g'ri — 鍵).",
                "U moliyaviy sohaning 'urg'usi' edi (noto'g'ri — 重鎮).",
                "Yozuvchining 'urg'uli' so'zlari (noto'g'ri — 重み)."]),
            q("t3-v6-32", "支給", [
                "このコース修了者には資格を支給する。",
                "客は店員に品物の代金を現金で支給した。",
                "海外旅行をするなら旅券の支給手続きをしてください。",
                "この会社は、給料のほかに家族手当が支給される。"], 4,
              "支給 (しきゅう) = to'lab berish, beriladigan nafaqa/to'lov.",
              optsTr=[
                "Kursni bitirganlarga malaka 'to'lanadi' (noto'g'ri — 付与/授与).",
                "Mijoz tovarni naqd pulda 'to'lab berdi' (noto'g'ri — 支払う).",
                "Pasportni 'to'lash' arizasi (noto'g'ri — 発行).",
                "Bu kompaniyada oylikdan tashqari oilaviy nafaqa ham to'lab beriladi (beriladi). (to'g'ri)"])
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
          "instruction_uz": "Gapdagi ( ) ga qo'yish uchun eng mos grammatik shaklni tanlang.",
          "questions": [
            q("t3-g1-33", "いったん仕事を引き受けた（　）、何があっても完成させなければならない。",
              ["上から", "上で", "上に", "上は"], 4,
              "Bir marta ishni zimmangga olgan ekansan, nima bo'lsa ham oxiriga yetkazishing shart.",
              expl="〜上は (うえは) = ...ekansan / modomiki ... qilar ekansan (qatiy burch)"),
            q("t3-g1-34", "財布を忘れたが、クレジットカードを持っていた（　）、何とか買い物ができた。",
              ["せいで", "くせに", "ものの", "おかげで"], 4,
              "Hamyonimni unutib qoldirgan bo'lsam-da, kredit kartam borligi sharofati bilan arang xarid qila oldim.",
              expl="〜おかげで = ...ning sharofati / yaxshiligi tufayli"),
            q("t3-g1-35", "けちな彼女（　）、本物のダイヤモンドなんか買うはずがない。",
              ["のことから", "のことだから", "のこととはいえ", "のことにしては"], 2,
              "Xasis bo'lgan u kishini bilganimiz uchun, asl brilliant sotib olishi aslo mumkin emas.",
              expl="〜のことだから = ...ning fe'lini bilganimiz sababli"),
            q("t3-g1-36", "A社はライバルだが、条件（　）は合併の交渉をしてもよい。",
              ["以前では", "次第では", "程度では", "事情では"], 2,
              "A kompaniyasi raqib bo'lsa-da, shartlarga qarab birlashish muzokaralarini olib borsa bo'ladi.",
              expl="〜次第では (しだいでは) = ...ga qarab, holatga bog'liq ravishda"),
            q("t3-g1-37", "大地震（　）、地図で家までの帰り道を確認しておこう。",
              ["に応じて", "に向かって", "に備えて", "に関して"], 3,
              "Katta zilzilaga tayyorgarlik ko'rib, xarita orqali uygacha qaytish yo'lini tekshirib qo'yaylik.",
              expl="〜に備えて (にそなえて) = ...ga tayyorgarlik ko'rish maqsadida"),
            q("t3-g1-38", "「さくらが咲いた」とニュースになるくらい、日本の春はさくら（　）語れない。",
              ["だけでは", "ぬきには", "ほどには", "のみでは"], 2,
              "«Gilos gulladi» deb yangiliklarda aytiladigan darajada, Yaponiyaning bahorini sakurasiz tasavvur etib (gapirib) bo'lmaydi.",
              expl="〜ぬきには = ...siz, ...bo'lmasa (amalga oshmaydi)"),
            q("t3-g1-39", "A「もしもし、山下社長はいらっしゃいますか。」\nB「ただいま、席を（　）、折り返しご連絡差し上げます。」",
              ["はずされておりますので", "はずしていらっしゃいますので", "はずしておりますので", "はずしてしまいますので"], 3,
              "A: «Allo, Yamashita prezident shu yerdamilar?»\nB: «Hozir joylarida yo'q edilar (席を外しております), qayta qo'ng'iroq qildiraman.»",
              expl="席を外しております = joyida yo'q (kamtarin nutq / kenjougo)"),
            q("t3-g1-40", "急いで論文を書いているが、このままでは締め切りには（　）。",
              ["間に合いそうもない", "間に合わないはずがない", "間に合うわけでもない", "間に合うほかない"], 1,
              "Shoshib maqola yozyapman, ammo bunday ketishda muddatiga aslo ulgura olmasam kerak.",
              expl="〜そうもない = ulgura oladiganga o'xshamaydi (ehtimoli juda kam)"),
            q("t3-g1-41", "私がここの決まりを（　）、みなさんにご迷惑をおかけしました。",
              ["知っていただけに", "知らなかっただけに", "知っていたばかりに", "知らなかったばかりに"], 4,
              "Men bu yerdagi qoidani bilmaganim oqibatidagina barchangizga tashvish tug'dirdim.",
              expl="〜ばかりに = faqatgina ... tufayli (yomon natija keltirib chiqardi)"),
            q("t3-g1-42", "あなたがしゃべらない限り、このことを知っている（　）。",
              ["人がいるはずだ", "人はいないはずだ", "人がいるということだ", "人がいないということだ"], 2,
              "Agar siz og'iz ochmasangiz, bu ishni biladigan hech kim bo'lmasligi kerak.",
              expl="〜はずだ = ...bo'lishi aniq/tabiiy (知っている人はいないはずだ)"),
            q("t3-g1-43", "食べ物は新鮮であればあるほど（　）、少し古いほうがおいしい食品もある。",
              ["おいしいはずで", "おいしいわけではなく", "おいしくないはずで", "おいしくないわけではなく"], 2,
              "Taom qancha yangi bo'lsa shuncha mazali bo'ladi degani emas, biroz saqlangani shirinroq bo'ladigan ozuqalar ham bor.",
              expl="〜わけではなく = mutlaqo shunday degani emas"),
            q("t3-g1-44", "現代の日本では、長男だからといって必ず家を（　）。",
              ["つぐわけではない", "つがないではいられない", "ついではならない", "つがざるを得ない"], 1,
              "Zamonaviy Yaponiyada to'ng'ich o'g'il bo'lgani bilan oila vorisligini olishi shart emas.",
              expl="〜わけではない = doim ham shart/shunday degani emas")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi ★ o'rniga tushadigan eng to'g'ri bo'lakni tanlang.",
          "questions": [
            q("t3-g2-45", None, ["助けて", "しては", "いるなら", "私と"], 2,
              "To'g'ri tartib: あなたが困っているなら、私としては助けてあげたいのだが……。",
              prefix="あなたが困って", suffix="あげたいのだが……。", starPos=2, order=[3, 4, 2, 1],
              expl="To'g'ri tartib: 困って[いるなら][私と][★しては][助けて] (3 → 4 → 2 → 1)"),
            q("t3-g2-46", None, ["平気", "10円を", "一方で", "節約する"], 3,
              "To'g'ri tartib: 私の妻は10円を節約する一方で、平気で高い服を買うことがある。",
              prefix="私の妻は", suffix="で高い服を買うことがある。", starPos=3, order=[2, 4, 3, 1],
              expl="To'g'ri tartib: 妻は[10円を][節約する][★一方で][平気] (2 → 4 → 3 → 1)"),
            q("t3-g2-47", None, ["もちろん", "甘すぎないので", "女性は", "男性に"], 1,
              "To'g'ri tartib: この店のケーキは甘すぎないので女性はもちろん、男性にも人気がある。",
              prefix="この店のケーキは", suffix="も人気がある。", starPos=3, order=[2, 3, 1, 4],
              expl="To'g'ri tartib: [甘すぎないので][女性は][★もちろん][男性に] (2 → 3 → 1 → 4)"),
            q("t3-g2-48", None, ["こと", "また", "どこか", "だから"], 4,
              "To'g'ri tartib: 時間にだらしない山下さんのことだから、またどこかでさぼっているのだろう。",
              prefix="時間にだらしない山下さんの", suffix="でさぼっているのだろう。", starPos=2, order=[1, 4, 2, 3],
              expl="To'g'ri tartib: 山下さんの[こと][★だから][また][どこか] (1 → 4 → 2 → 3)"),
            q("t3-g2-49", None, ["流れに", "進むと", "沿って", "歩く"], 3,
              "To'g'ri tartib: 人の歩く流れに沿って進むと、その先にイベント会場があった。",
              prefix="人の", suffix="その先にイベント会場があった。", starPos=3, order=[4, 1, 3, 2],
              expl="To'g'ri tartib: 人の[歩く][流れに][★沿って][進むと] (4 → 1 → 3 → 2)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh joylariga eng to'g'ri variantni tanlang.",
          "passage_title": "父子家庭への支援",
          "passage": (
            "妻と離婚、または死別して20歳以下の子どもを育てている男性の家庭を「父子家庭」と言います（これに対し、母親と児童の家庭を「母子家庭」と言います）。最近の20年、離婚の増加により父子家庭の数は過去最高になりました。\n"
            "母子家庭には、その収入 {{50}} 、児童扶養手当という子どもを育てるためのお金が支給され、ほかにもさまざまな制度があります。日本は「夫が外でお金を稼ぎ、妻が家庭で家事・育児をする」という考えが強かったので、 {{51-a}} は経済的に苦しい家が多かったためです。\n"
            "一方、「 {{51-b}} と比べて {{51-c}} には経済的な問題はないだろう」と思われていたので、児童扶養手当は支給されていませんでした。\n"
            "ところが父子家庭の収入は、母子家庭ほど {{52}} 、平均に比べたらずいぶん低いことがわかりました。 {{53}} 、日本では男性は長い残業も休日出勤もやるのが当たり前で、「保育園に子どもを迎えに行くから、5時には帰らなければならない」という男性を雇ってくれる会社は、あまり多くないのです。すでに働いていても、正社員でなくアルバイトになったり、男性であっても、 {{54}} 。\n"
            "そして、厚生労働省は低収入の父子家庭にも児童扶養手当を支給することを決定しました。この制度は2010年の年末から施行されることになり、約10万所帯が給付の対象になります。"
          ),
          "passage_tr": (
            "Xotini bilan ajrashgan yoki xotini vafot etib, 20 yoshdan kichik bolani tarbiyalayotgan erkakning oilasi «otasiz oila» (fusikatei) deb ataladi. So'nggi 20 yilda ajrimlar ko'payishi bilan bunday oilalar soni tarixdagi eng yuqori darajaga yetdi.\n"
            "Onalik oilalariga ularning daromadiga qarab bola tarbiyasi nafaqasi to'lanadi. Yaponiyada «er tashqarida pul topadi, ayol esa uyda ro'zg'or va bola tarbiyasi bilan shug'ullanadi» degan tushuncha kuchli bo'lgani sababli, onalik oilalari moddiy jihatdan qiynalgan oilalar ko'p bo'lgan.\n"
            "Boshqa tomondan esa «onali oilalarga nisbatan otali oilalarda iqtisodiy muammo bo'lmasa kerak» deb hisoblangani bois, bolalar nafaqasi berilmas edi.\n"
            "Vaholanki otali oilalarning daromadi onalarnikidek past bo'lmasa ham, o'rtacha ko'rsatkichdan ancha pastligi ma'lum bo'ldi. Buning ustiga, Yaponiyada erkaklar uzoq vaqt qo'shimcha ishlashi va dam olish kunlari ham ishlashi tabiiy hol bo'lib, «bolani bog'chadan olishim kerak, soat 5 da ketishim shart» degan erkakni ishga oladigan kompaniyalar juda kam. Hatto ishlab turgan bo'lsa ham, doimiy emas, balki soatbay ishchiga aylanib qolishadi.\n"
            "Shuning uchun Sog'liqni saqlash vazirligi kam ta'minlangan otali oilalarga ham bolalar nafaqasini to'lashga qaror qildi."
          ),
          "questions": [
            q("t3-g3-50", None, ["に伴った", "に応じた", "に比べた", "に沿った"], 2,
              "その収入[に応じた]児童扶養手当 = o'sha daromadiga mos keladigan nafaqa.",
              blankNo="50", expl="〜に応じた (におうじた) = ...ga mos, muvofiq"),
            q("t3-g3-51", None, [
                "a 父子家庭 ／ b 母子家庭 ／ c 母子家庭",
                "a 父子家庭 ／ b 父子家庭 ／ c 母子家庭",
                "a 母子家庭 ／ b 母子家庭 ／ c 父子家庭",
                "a 母子家庭 ／ b 父子家庭 ／ c 父子家庭"], 3,
              "a 母子家庭 (onali oila) qiynalgan; b 母子家庭 ga qaraganda c 父子家庭 da muammo yo'q deb o'ylangan.",
              blankNo="51", expl="Tartib: a 母子家庭 / b 母子家庭 / c 父子家庭"),
            q("t3-g3-52", None, ["低いにしても", "低いわけがなく", "低くはないものの", "低いと思ったら"], 3,
              "母子家庭ほど[低くはないものの]、平均に比べたらずいぶん低い = unchalik past bo'lmasa-da, o'rtachadan ancha past.",
              blankNo="52", expl="〜ものの = ...bo'lsa-da, qaramasdan"),
            q("t3-g3-53", None, ["というのも", "だからといって", "にもかかわらず", "とはいえ"], 1,
              "[というのも]、日本では男性は長い残業もやるのが当たり前で = Negaki, Yaponiyada...",
              blankNo="53", expl="というのも = sababi shundaki, negaki"),
            q("t3-g3-54", None, ["高収入になりかねません", "高収入にならざるを得ません", "低収入になり得ないのです", "低収入になり得るのです"], 4,
              "男性であっても、[低収入になり得るのです] = Erkak kishi bo'lsa ham kam daromadli bo'lib qolishi mumkin.",
              blankNo="54", expl="〜得る (うる) = bo'lishi mumkin, ehtimoli bor")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = sum(len(p["questions"]) for s in data["sections"] for p in s["problems"])
print(f"OK! test03.json yaratildi: {total} ta savol.")
