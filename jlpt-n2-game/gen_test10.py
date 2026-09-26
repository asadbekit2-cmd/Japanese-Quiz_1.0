# -*- coding: utf-8 -*-
"""
test10.json generatori — 第10回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.11, Savollar p.98-107
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test10.json")

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
  "id": 10,
  "title_jp": "第10回 模擬テスト",
  "title_uz": "10-test",
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
            q("t10-v1-1", "発売日より1日早く、新商品が【入荷】した。",
              ["にゅうに", "にゅうか", "にゅうこ", "にゅうひん"], 2,
              "Sotuvga chiqish kunidan 1 kun oldin yangi tovar omborga kelib tushdi (qabul qilindi).",
              reading="にゅうか", expl="入荷 → にゅうか (tovarning kelishi, qabul qilinishi)"),
            q("t10-v1-2", "我が社は採用の際、コミュニケーション能力の【有無】を重視します。",
              ["ありむ", "ゆうぶ", "うむ", "うぶ"], 3,
              "Bizning kompaniya xodimlarni ishga olishda muloqot qobiliyatining bor-yo'qligiga katta e'tibor beradi.",
              reading="うむ", expl="有無 → うむ (mavjudligi yoki yo'qligi)"),
            q("t10-v1-3", "ダブルのスーツはお年寄りには【懐かしく】、若者の目には新鮮にうつるようだ。",
              ["なつかしく", "はずかしく", "ちかしく", "ふるめかしく"], 1,
              "Ikki bortli kostyum keksalar uchun qadrdon/xotirali, yoshlar nigohida esa yangicha tuyuladi.",
              reading="なつかしく", expl="懐かしい → なつかしい (qadrdon, sog'inch uyg'otuvchi)"),
            q("t10-v1-4", "就職が決まらず落ち込む友人をどう【慰めて】よいのか、言葉が見つからない。",
              ["なだめて", "いましめて", "おさめて", "なぐさめて"], 4,
              "Ish topolmay tushkunlikka tushgan do'stimga qanday tasalli berishni bilmay, so'z topolmayapman.",
              reading="なぐさめて", expl="慰める → なぐさめる (tasalli bermoq, ko'nglini ko'tarmoq)"),
            q("t10-v1-5", "父親が亡くなり、家や土地などの財産を【相続】した。",
              ["しょうぞく", "そうぞく", "しょうそく", "そうそく"], 2,
              "Otam vafot etgach, uy va yer kabi mol-mulkni meros qilib oldim.",
              reading="そうぞく", expl="相続 → そうぞく (meros qilib olish, vorislik)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t10-v2-6", "あの2人の作家の作品は【たいしょう】的である。",
              ["対象", "対称", "対照", "対症"], 3,
              "U ikki yozuvchining ijodiy asarlari bir-biriga mutlaqo qarama-qarshi (kontrast) xarakterga ega.",
              reading="たいしょう", expl="対照的 → たいしょうてき (keskin farq qiluvchi, kontrast)"),
            q("t10-v2-7", "彼女は日本のテレビドラマで、楽しく言葉を【おぼえて】いる。",
              ["覚えて", "学えて", "賞えて", "覚へて"], 1,
              "U yapon teleseriallari orqali maroq bilan so'zlarni yod olmoqda.",
              reading="おぼえて", expl="覚える → おぼえる (yodlamoq, esda saqlamoq)"),
            q("t10-v2-8", "この数学の問題の【かいとう】がわからないので、教えてください。",
              ["会答", "快答", "解答", "改答"], 3,
              "Bu matematika masalasining to'g'ri yechimini (javobini) bilmaganim sababli tushuntirib bering.",
              reading="かいとう", expl="解答 → かいとう (masala yechimi, javob)"),
            q("t10-v2-9", "父の誕生日に家族全員が久しぶりに集まって、ビールで【かんぱい】した。",
              ["乾杯", "観杯", "幹杯", "換杯"], 1,
              "Otamning tavallud ayyomida butun oila ancha vaqtdan so'ng yig'ilib, pivo bilan qadah urishtirdik.",
              reading="かんぱい", expl="乾杯 → かんぱい (qadah ko'tarish, tost)"),
            q("t10-v2-10", "時代の流れには【さからえず】、公衆電話の数が減っている。",
              ["反らえず", "敵らえず", "抗らえず", "逆らえず"], 4,
              "Zamon talabiga (oqimiga) qarshi borolmay, taksafonlar soni qisqarib bormoqda.",
              reading="さからえず", expl="逆らう → さからう (qarshi bormoq, bo'ysunmaslik)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t10-v3-11", "社長の（　）時代的な考え方をなんとかしてほしい。",
              ["古", "同", "先", "前"], 4,
              "Bosh direktorning eskirgan (zamondan orqada qolgan) qarashlariga bir chora ko'rishsa yaxshi bo'lardi.",
              expl="前時代的 (ぜんじだいてき) = o'tmishdan qolgan, eskirgan"),
            q("t10-v3-12", "人は税金を払うときは文句を言うが、その使い道には（　）関心だ。",
              ["未", "非", "無", "不"], 3,
              "Odamlar soliq to'layotganda norozilik bildirishadi-yu, lekin uning qayerga sarflanishiga mutlaqo beparvodir.",
              expl="無関心 (むかんしん) = beparvo, qiziqmaydigan"),
            q("t10-v3-13", "厳しすぎるしつけが（　）効果となってしまった。",
              ["逆", "反", "非", "悪"], 1,
              "Haddan ortiq qattiqqo'l tarbiya teskari natija (aksincha samara) keltirib chiqardi.",
              expl="逆効果 (ぎゃくこうか) = teskari samara / kutilmagan salbiy natija"),
            q("t10-v3-14", "保護者たちは交代（　）で、通学路をパトロールしている。",
              ["制", "型", "系", "形"], 1,
              "Ota-onalar navbatma-navbat (navbatchilik tizimi asosida) maktab yo'lini nazorat qilib chiqmoqdalar.",
              expl="交代制 (こうたいせい) = navbatchilik tizimi"),
            q("t10-v3-15", "スケジュールは相手（　）の都合で決めます。",
              ["向", "側", "型", "様"], 2,
              "Jadvalni ikkinchi tomonning (sherikning) qulayligiga qarab belgilaymiz.",
              expl="相手側 (あいてがわ) = qarshi tomon, sherik tomon")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t10-v4-16", "自転車は地球にやさしい（　）手段として期待されている。",
              ["異動", "進行", "運用", "移動"], 4,
              "Velosiped ekologiyaga foydali harakatlanish vositasi sifatida katta umid uyg'otmoqda.",
              reading="いどう", expl="移動 (いどう) = harakatlanish, ko'chish"),
            q("t10-v4-17", "イベントは期待通りの成功を（　）。",
              ["詰めた", "収めた", "治めた", "努めた"], 2,
              "Tadbir kutilganidek katta muvaffaqiyat qozondi.",
              reading="おさめた", expl="（成功を）収める = muvaffaqiyatga erishmoq/qozonmoq"),
            q("t10-v4-18", "パーティーの料理が出されると、（　）皿が空になってしまった。",
              ["あちこち", "しばしば", "のろのろ", "たちまち"], 4,
              "Ziyofat taomlari tortilishi bilanoq, likopchalar bir zumda (ko'z ochib yumguncha) bo'shab qoldi.",
              reading="たちまち", expl="たちまち = bir zumda, ko'z ochib yumguncha"),
            q("t10-v4-19", "40代の女性を（　）にしたファッション誌が発売される。",
              ["リーダー", "ターゲット", "プログラム", "サービス"], 2,
              "40 yoshlardagi ayollarni nishon (maqsadli auditoriya) qilib olgan moda jurnali sotuvga chiqmoqda.",
              expl="ターゲット (target) = nishon, mo'ljallangan auditoriya"),
            q("t10-v4-20", "スーパー間の激しい（　）競争は買う側にとってはありがたいことだ。",
              ["価格", "値札", "過剰", "強化"], 1,
              "Supermarketlar o'rtasidagi keskin narx raqobati xaridorlar uchun quvonarli holatdir.",
              reading="かかく", expl="価格競争 (かかくきょうそう) = narxlar borasidagi raqobat"),
            q("t10-v4-21", "子どもは大人が思う以上に、はるかに想像力に（　）いる。",
              ["恵まれて", "揺れて", "触れて", "与えられて"], 1,
              "Bolalar kattalar o'ylaganidan ko'ra ancha boy tasavvur qobiliyatiga ega bo'ladilar.",
              reading="めぐまれて", expl="（〜に）恵まれている = ...jihatdan boy/in'om etilgan"),
            q("t10-v4-22", "世界各地の神話は互いに（　）するテーマが多い。",
              ["交流", "共通", "合流", "共同"], 2,
              "Dunyo afsona va miflarida o'zaro mushtarak (umumiy) bo'lgan mavzular ko'p uchraydi.",
              reading="きょうつう", expl="共通する (きょうつうする) = mushtarak bo'lmoq, o'xshash bo'lmoq")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t10-v5-23", "ネットで最新の【トピック】を検索する。",
              ["課題", "問題", "例題", "話題"], 4,
              "Internetda eng so'nggi dolzarb mavzularni (yangiliklarni) qidirmoqdaman.",
              expl="トピック ≈ 話題 (dolzarb mavzu, yangilik)"),
            q("t10-v5-24", "花火大会当日、【あいにく】雨が降り出してきた。",
              ["激しく", "急に", "運悪く", "予想通り"], 3,
              "Mushakbozlik kuni baxtga qarshi yomg'ir yog'a boshladi.",
              reading="あいにく", expl="あいにく ≈ 運悪く (baxtga qarshi, noqulay tarzda)"),
            q("t10-v5-25", "口のうまいあの男に【担がれた】。",
              ["だまされた", "断られた", "誘われた", "馬鹿にされた"], 1,
              "Tili shirin anavi yigitning tuzog'iga tushdim (aldanib qoldim).",
              reading="かつがれた", expl="担がれる ≈ だまされる (laqillatilib aldanmoq)"),
            q("t10-v5-26", "あの人、ああ見えても【根は】まじめなんですよ。",
              ["仕事ぶり", "普段", "学習態度", "性質"], 4,
              "U odam tashqi ko'rinishidan shunday tuyulsa-da, asl tabiatida (ich-ichida) juda jiddiy inson.",
              reading="ねは", expl="根は ≈ 性質・本性 (asl tabiati, ichki xarakteri)"),
            q("t10-v5-27", "【結構なもの】をいただき、ありがとうございます。",
              ["めずらしい", "すばらしい", "おいしい", "なつかしい"], 2,
              "Ajoyib va qimmatbaho sovg'angiz uchun katta rahmat.",
              reading="けっこうなもの", expl="結構なもの ≈ すばらしいもの (ajoyib, a'lo darajadagi tuhfa)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'zning gapda eng to'g'ri ishlatilgan variantini tanlang.",
          "questions": [
            q("t10-v6-28", "【調整】の使い方として最もよいものを選びなさい。",
              [
                "みなの都合を聞いて次の会議の日程を調整する。",
                "都会の農地のほとんどが、住宅地に調整されてしまった。",
                "部屋の冷房の強弱は自由に調整できます。",
                "荒れた土地を調整して、野菜畑にした。"
              ], 1,
              "調整 (chousei) = muvofiqlashtirish, tartibga solish, jadvalni kelishish.",
              expl="「日程を調整する」= kun tartibi va vaqtini muvofiqlashtirmoq (to'g'ri ishlatilish)."),
            q("t10-v6-29", "【すきずき】の使い方として最もよいものを選びなさい。",
              [
                "何もこんな大変な仕事すきずきですることない。",
                "だれがいちばん美人かって？ それはすきずきだよ。",
                "娘は食べ物のすきずきが多くて困っています。",
                "この洋服のデザインは私のすきずきに合わない。"
              ], 2,
              "すきずき (sukizuki) = har kimning o'z didiga bog'liq bo'lishi.",
              expl="「それはすきずきだよ」= bu har kimning o'z didi va qarashiga bog'liq (to'g'ri ishlatilish)."),
            q("t10-v6-30", "【透明】の使い方として最もよいものを選びなさい。",
              [
                "何かわからないが透明な不安を感じる。",
                "あの人は政治的には透明なので、意見を聞いてみよう。",
                "歌手の透明な歌声がコンサート会場に響き渡った。",
                "嫌な仕事が片付いて気持ちが透明になった。"
              ], 3,
              "透明 (toumei) = tiniq, shaffof, mayin.",
              expl="「透明な歌声」= musaffo, tiniq jarangdor ovoz (to'g'ri ishlatilish)."),
            q("t10-v6-31", "【見当】の使い方として最もよいものを選びなさい。",
              [
                "明日の雨が降る見当は50パーセントです。",
                "優勝候補が相手では勝てる見当はない。",
                "彼女のトランプ占いの見当は気味が悪いほどよく当たる。",
                "断りの理由は言わないが、彼の表情で大体の見当がついた。"
              ], 4,
              "見当 (kentou) = taxmin, mulohaza; 見当がつく = taxmin qila olmoq.",
              expl="「大体の見当がついた」= umumiy taxmini oydinlashdi (to'g'ri ishlatilish)."),
            q("t10-v6-32", "【申請】の使い方として最もよいものを選びなさい。",
              [
                "両親に借金を申請してみようと思う。",
                "海外旅行に行くのでパスポートを申請した。",
                "恋人に思い切って結婚を申請した。",
                "飛行機を予約するときはいつも窓際の席を申請する。"
              ], 2,
              "申請 (shinsei) = rasmiy ariza topshirish, murojaat qilish.",
              expl="「パスポートを申請した」= pasport olish uchun rasmiy ariza berdim (to'g'ri ishlatilish).")
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
            q("t10-g1-33", "夏の日照不足（　）秋の長雨で、米の不作が心配されます。",
              ["に増し", "に反し", "にかけ", "に加え"], 4,
              "Yozda quyosh nuri yetishmaganiga qo'shimcha ravishda kuzdagi uzoq yog'ingarchilik sababli sholi hosili xarob bo'lishidan xavotir olinmoqda.",
              expl="「〜に加え（て）」= ...ga qo'shimcha ravishda."),
            q("t10-g1-34", "まず政治家（　）、自分のおこないを正すべきだ。",
              ["すら", "ほど", "こそ", "さえ"], 3,
              "Avvalo aynan siyosatchilarning o'zi o'z xulq-atvorini to'g'rilashi lozim.",
              expl="「〜こそ」= aynan ...ning o'zi (ta'kidlash)."),
            q("t10-g1-35", "車でお迎えに行きますから、駅に（　）お電話をください。",
              ["着く際", "着き次第", "着く途中", "着いたとたん"], 2,
              "Mashinada kutib olgani boraman, shuning uchun vokzalga yetib borishingiz bilanoq qo'ng'iroq qiling.",
              expl="「動詞ます形 ＋ 次第」= ...qilishi bilanoq darhol."),
            q("t10-g1-36", "先生は私が発音を（　）、何度も繰り返させる。",
              ["間違えるたびに", "間違えるにつけ", "間違えるかたわら", "間違えながら"], 1,
              "Ustoz har gal talaffuzda xato qilganimda, qayta-qayta takrorlattiradi.",
              expl="「〜たびに」= har gal ...qilganda."),
            q("t10-g1-37", "出発に（　）、あらかじめホテルを予約しておいた。",
              ["前もって", "関して", "先立って", "先がけて"], 3,
              "Safarga jo'nashdan oldin oldindan mehmonxonani band qilib qo'ydim.",
              expl="「〜に先立って」= ...dan oldin, muqaddam (rasmiy reja/faoliyatda)."),
            q("t10-g1-38", "（会社で）\\nA「近くに打ち合わせをするためのいい場所を知らないか。」\\nB「会社の裏のレストランなら、落ち着いて（　）と思います。」",
              ["お話しになれる", "話してくださる", "話していただく", "お話しになさる"], 1,
              "A: «Yaqin atrofda yig'ilish o'tkazish uchun yaxshi joy bilmaysanmi?» — B: «Kompaniya ortidagi restoranda xotirjam gaplasha olasiz deb o'ylayman.»",
              expl="「お話しになれる」= suhbatlasha olmoq (hurmat + imkoniyat shakli)."),
            q("t10-g1-39", "サッカーの日本チームが負けたので、くやしくて（　）。",
              ["たえられない", "なれない", "しょうがない", "しょうもない"], 3,
              "Yaponiya futbol terma jamoasi yutqazgani sababli alamdan chiday olmayapman (ichim yonmoqda).",
              expl="「〜てしょうがない」= ...tufayli chidab bo'lmaydigan darajada kuchli."),
            q("t10-g1-40", "3日でこれだけの仕事をするなんて（　）と思ったが、がんばってやり終えた。",
              ["できないはずがない", "できるはずがない", "できないかもしれない", "できるかもしれない"], 2,
              "3 kunda shuncha ishni bajarish aslo imkoni yo'q deb o'ylagandim, lekin astoydil ishlab tugatdim.",
              expl="「できるはずがない」= uddalashning mutlaqo iloji yo'q."),
            q("t10-g1-41", "夫は医者から、「あまりたまごを（　）」と注意されたそうだ。",
              ["食べないようにしたほうがいい", "食べないようにしたい", "食べるようにしたほうがいい", "食べるようにしたい"], 1,
              "Erim shifokordan «tuxumni ko'p yemaslikka harakat qilganingiz ma'qul» degan ogohlantirish olgan emish.",
              expl="「〜ないようにしたほうがいい」= ...qilmaslikka harakat qilganingiz ma'qul."),
            q("t10-g1-42", "相手から（　）、電話番号を教えないことにしている。",
              ["聞かれたかぎりでは", "聞かれたかぎり", "聞かれないかぎりでは", "聞かれないかぎり"], 4,
              "Qarshi tomon so'ramaguncha telefon raqamimni bermaslikni o'zimga qoida qilganman.",
              expl="「〜ないかぎり」= ...bo'lmaguncha / ...qilinmasa."),
            q("t10-g1-43", "林があったところにマンションが建った。少しずつ街から緑が（　）。",
              ["消えつつある", "消えつついる", "消しつつある", "消しつついる"], 1,
              "To'qayzor bo'lgan joyda ko'p qavatli uy qurildi. Shahardan yashillik asta-sekin yo'qolib bormoqda.",
              expl="「〜つつある」= ...jarayon davom etmoqda (sekin-asta sodir bo'lish)."),
            q("t10-g1-44", "病気の子どもたちを（　）、病院で楽しい劇が行われた。",
              ["笑われようと", "笑われようとして", "笑わされようと", "笑わせようとして"], 4,
              "Bemor bolajonlarni kuldirish maqsadida shifoxonada qiziqarli spektakl namoyish etildi.",
              expl="「笑わせようとして」= kuldirish, quvontirish niyatida (orttirma nisbat).")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の＿★＿に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keladigan eng to'g'ri variantni tanlang.",
          "questions": [
            q("t10-g2-45", None,
              ["された", "どんなに", "反対", "ところで"], 1,
              "Menga qanchalik qarshilik qilishmasin, men baribir unga uylanish niyatidaman.",
              prefix="たとえ", suffix="、私は彼女と結婚するつもりだ。",
              starPos=3, order=[2, 3, 1, 4],
              expl="Tartib: どんなに(2) 反対(3) された(1) ところで(4) → Yulduzcha 3-o'rinda: された(1)"),
            q("t10-g2-46", None,
              ["なら", "泣く", "くやしくて", "くらい"], 2,
              "Bahosi yomonligidan alam qilib yig'lagandan ko'ra, ko'proq dars qilsa bo'lardi-ku!",
              prefix="成績が悪いのが", suffix="もっと勉強すればよいのに。",
              starPos=2, order=[3, 2, 4, 1],
              expl="Tartib: くやしくて(3) 泣く(2) くらい(4) なら(1) → Yulduzcha 2-o'rinda: 泣く(2)"),
            q("t10-g2-47", None,
              ["ニュースを", "大きさを", "通じて", "地震の被害の"], 4,
              "Radio xabarlari orqali zilzila keltirgan zararning ko'lamini ilk bor angladim.",
              prefix="ラジオの", suffix="はじめて知った。",
              starPos=3, order=[1, 3, 4, 2],
              expl="Tartib: ニュースを(1) 通じて(3) 地震の被害の(4) 大きさを(2) → Yulduzcha 3-o'rinda: 地震の被害の(4)"),
            q("t10-g2-48", None,
              ["と", "手伝える", "なると", "人がいない"], 1,
              "Kimdan so'rasam ham yordamlashadigan odam yo'q ekan, bir o'zim bajarishdan boshqa ilojim qolmaydi.",
              prefix="だれに聞いても", suffix="、私1人でやるしかない。",
              starPos=3, order=[2, 4, 1, 3],
              expl="Tartib: 手伝える(2) 人がいない(4) と(1) なると(3) → Yulduzcha 3-o'rinda: と(1)"),
            q("t10-g2-49", None,
              ["でも", "では", "食べない", "ダイエット中"], 3,
              "Ko'z o'ngimda noz-ne'matlar tursa, qanchalik parhezda bo'lmayin, yemasdan turolmayman.",
              prefix="目の前にごちそうを出されたら、いくら", suffix="いられない。",
              starPos=3, order=[4, 1, 3, 2],
              expl="Tartib: ダイエット中(4) でも(1) 食べない(3) では(2) → Yulduzcha 3-o'rinda: 食べない(3)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlarga eng mos keluvchi javobni tanlang.",
          "passage": "花を愛する人は【 50 】。そのため、たくさんの客に来てほしい観光地では、花を植えてお客を呼ぼうとするところが増えました。\n　しかし花にとって、本当に来てほしいのは人間ではなく、自分の花粉（注1）を運んで実を結ばせてくれる虫や鳥たちです。来てほしい生物は花【 51 】違い、花は色や形や匂いで自分の花粉を運ぶ生物を呼び寄せます。\n　夜に咲く花に白が多いのも、冬に咲く花に黄色が多いのも、夜や冬に飛ぶ虫がその色を好むからです。\n　赤が見えない虫と違って、鳥は赤い色が【 52 】。鳥を誘おうとする花には、赤い色が多いと言われています。\n　「ハナバチ」は名前のとおり、花をまわり、花粉やミツを集め、幼虫に与えるハチです。ハナバチだけに来てほしい花は、深い筒型（注2）の形のものが多いそうです。ちょうどハナバチの重さと大きさで開く、【 53 】「自動ドア」があり、その奥にミツがあるというわけです。\n　匂いも大事です。花は大体よい香りがしますが、中にはくさった肉のような匂いの花もあります。世界最大の花のラフレシアもそうです。そして、このラフレシアが誘っているのはハエなのです。ハエは【 54 】を好むからです。\n　こういう花の工夫を見ると、「いったい花の脳みそはどこにあるんだろう」とふしぎな気がしませんか。",
          "questions": [
            q("t10-g3-50", None,
              ["多くはありません", "少なくありません", "少ししかいません", "めったにいません"], 2,
              "Gullarni sevadigan insonlar kam emas (juda ko'p).",
              blankNo=50, expl="「少なくありません」= kam emas (ko'pchilikni tashkil qiladi)."),
            q("t10-g3-51", None,
              ["によって", "にとって", "について", "にあたって"], 1,
              "Gullar jalb qilmoqchi bo'lgan tirik mavjudotlar gul turiga qarab har xil bo'ladi...",
              blankNo=51, expl="「花によって（違い）」= gulning turiga qarab har xil bo'lishi."),
            q("t10-g3-52", None,
              ["見ます", "見えません", "見えます", "見られません"], 3,
              "Qizil rangni ko'ra olmaydigan hasharotlardan farqli o'laroq, qushlar qizil rangni ko'ra oladilar.",
              blankNo=52, expl="「赤い色が見えます」= qushlar qizil rangni yaxshi ko'ra oladilar."),
            q("t10-g3-53", None,
              ["たとえ", "いわば", "いわゆる", "なぜならば"], 2,
              "Xuddi arining og'irligi va o'lchami bilan ochiladigan go'yo «avtomatik eshik» mavjud bo'lib...",
              blankNo=53, expl="「いわば (go'yo, aytish mumkinki)」"),
            q("t10-g3-54", None,
              ["ラフレシア", "大きい花", "よい香り", "いやな匂い"], 4,
              "Chunki pashshalar badbo'y (yoqimsiz) hidni xush ko'radilar.",
              blankNo=54, expl="「いやな匂い」= yoqimsiz badbo'y hid.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK! test10.json yaratildi: {len(data['sections'][0]['problems'])} vocab + {len(data['sections'][1]['problems'])} grammar bo'limlari.")
