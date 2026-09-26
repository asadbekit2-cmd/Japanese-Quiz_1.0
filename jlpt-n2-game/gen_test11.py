# -*- coding: utf-8 -*-
"""
test11.json generatori — 第11回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.12, Savollar p.108-117
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test11.json")

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
  "id": 11,
  "title_jp": "第11回 模擬テスト",
  "title_uz": "11-test",
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
            q("t11-v1-1", "夜型の生活をしているうちに【睡眠障害】になってしまった。",
              ["しょうかい", "じょうがい", "しょうがい", "じょうかい"], 3,
              "Kechasi uxlamasdan yashash tartibiga o'tib, uyqu buzilishi (insomniya/disomniya) kasalligiga uchradim.",
              reading="しょうがい", expl="障害 → しょうがい (buzilish, to'siq, xastalik)"),
            q("t11-v1-2", "地球に降る太陽光の1時間のエネルギー量は、人類が1年間に使う量に【相当する】。",
              ["そうとう", "しょうとう", "あいとう", "そうおう"], 1,
              "Yerga tushadigan quyosh nurining 1 soatlik energiya miqdori insoniyat 1 yilda ishlatadigan miqdorga tengdir (mos keladi).",
              reading="そうとう", expl="相当 → そうとう (teng kelish, mos kelish)"),
            q("t11-v1-3", "少子化が進み、親が先回りして子どもを助ける【傾向】が強い。",
              ["けいこう", "かたこう", "けいむき", "かたむき"], 1,
              "Tug'ilish kamayib, ota-onalar oldindan shoshilib bolalariga ortiqcha yordam berish moyilligi kuchaymoqda.",
              reading="けいこう", expl="傾向 → けいこう (moyillik, tendensiya)"),
            q("t11-v1-4", "私は自分の長所を【磨き】続ければ必ず成功すると信じている。",
              ["たたき", "かがやき", "いき", "みがき"], 4,
              "O'zimning kuchli tomonlarimni charxlab (sayqallab) borsam albatta muvaffaqiyatga erishaman deb ishonaman.",
              reading="みがき", expl="磨く → みがく (sayqallamoq, charxlamoq, rivojlantirmoq)"),
            q("t11-v1-5", "人間は困ったことが起きたときのほうが、持っている力を【発揮】できる。",
              ["はっこう", "はっき", "ほっこう", "ほっき"], 2,
              "Inson qiyin vaziyatga tushgandagina o'zidagi bor kuch-qudratini to'liq namoyon eta oladi.",
              reading="はっき", expl="発揮 → はっき (namoyon etish, ko'rsatish)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t11-v2-6", "世界の30カ国近くの国が、国際【ごうとう】団の被害を受けている。",
              ["監獄", "強罰", "強盗", "獄盗"], 3,
              "Dunyoning qariyb 30 ta davlati xalqaro qaroqchilar (bosqinchilar) guruhidan zarar ko'rmoqda.",
              reading="ごうとう", expl="強盗 → ごうとう (bosqinchi, qaroqchi, talonchi)"),
            q("t11-v2-7", "【しょうとつ】直前で自動的にブレーキがかかって停止する車が開発された。",
              ["衝突", "障突", "衝突", "将突"], 1,
              "To'qnashuvdan aynan oldin avtomatik tormozlanib to'xtaydigan avtomobil ishlab chiqildi.",
              reading="しょうとつ", expl="衝突 → しょうとつ (to'qnashuv, zarba)"),
            q("t11-v2-8", "彼女は好きな相手に【つくす】タイプだ。",
              ["注くす", "就くす", "尽くす", "着くす"], 3,
              "U sevgan insoni uchun borini fido qiladigan (jon kuydiradigan) fe'l-atvorli inson.",
              reading="つくす", expl="尽くす → つくす (borini bermoq, fido qilmoq, xizmat ko'rsatmoq)"),
            q("t11-v2-9", "相手の国の文化に【けいい】を払うことは、国際協力上大切なことだ。",
              ["仰意", "掲意", "傾意", "敬意"], 4,
              "Hamkor davlatning madaniyatiga hurmat bilan yondashish xalqaro hamkorlikda muhim omildir.",
              reading="けいい", expl="敬意 → けいい (hurmat, ehtirom)"),
            q("t11-v2-10", "大学卒業後数年は新卒として就職活動をできるよう、システムを【あらためる】べきだ。",
              ["改める", "政める", "敢める", "変める"], 1,
              "Universitetni bitirgandan so'ng bir necha yil yangi bitiruvchi sifatida ish qidirish imkoni bo'lishi uchun tizimni isloh qilish (o'zgartirish) lozim.",
              reading="あらためる", expl="改める → あらためる (isloh qilmoq, yangilamoq, to'g'rilamoq)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t11-v3-11", "あの新人選手がいちばん注目（　）が高い。",
              ["感", "性", "料", "度"], 4,
              "U yangi sportchiga nisbatan e'tibor darajasi (qiziqish darajasi) eng yuqoridir.",
              expl="注目度 (ちゅうもくど) = diqqat/e'tibor darajasi"),
            q("t11-v3-12", "携帯電話はこの10年間で驚くほど（　）性能になっている。",
              ["高", "最", "名", "長"], 1,
              "Mobil telefonlar so'nggi 10 yilda hayratlanarli darajada yuqori unumdorlikka (yuqori quvvatga) ega bo'ldi.",
              expl="高性能 (こうせいのう) = yuqori unumdorlik, yuqori sifatli texnik ko'rsatkich"),
            q("t11-v3-13", "これはまだ計画（　）に過ぎません。",
              ["済", "下", "案", "的"], 3,
              "Bu hali loyiha rejasidan (qoralama taklifidan) boshqa narsa emas.",
              expl="計画案 (けいかくあん) = reja loyihasi, taklif"),
            q("t11-v3-14", "明日はグループから離れて（　）行動をとる。",
              ["代", "異", "単", "別"], 4,
              "Ertaga guruhdan ajralib alohida (mustaqil) harakat qilamiz.",
              expl="別行動 (べつこうどう) = alohida/ajralib harakat qilish"),
            q("t11-v3-15", "台所に消火（　）がなかったら、火事になってしまっただろう。",
              ["機", "器", "技", "基"], 2,
              "Oshxonada o't o'chirgich (ognetushitel) bo'lmaganida, yong'in chiqib ketgan bo'lardi.",
              expl="消火器 (しょうかき) = o't o'chirish moslamasi (ognetushitel)")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t11-v4-16", "約50メートル（　）の信号を左に曲がると、海が見えてくる。",
              ["正面", "後者", "前方", "先頭"], 3,
              "Qariyb 50 metr oldindagi svetofordan chapga burilsangiz, dengiz ko'rinadi.",
              reading="ぜんぽう", expl="前方 (ぜんぽう) = old tomon, oldinda"),
            q("t11-v4-17", "このパーティーでは、男性の（　）な服装はタキシードです。",
              ["正式", "正確", "正道", "正規"], 1,
              "Ushbu kechada erkaklarning rasmiy kiyimi smokin (taksido) hisoblanadi.",
              reading="せいしき", expl="正式 (せいしき) = rasmiy, qonuniy"),
            q("t11-v4-18", "あの教授は質問に（　）な答え方をするので、嫌われている。",
              ["適切", "残念", "器用", "皮肉"], 4,
              "U professor savollarga piching (istehzoli) javob bergani uchun hamma uni yoqtirmaydi.",
              reading="ひにく", expl="皮肉 (ひにく) = kinoya, istehzo, piching"),
            q("t11-v4-19", "（手紙で）寒くなりましたので（　）お体にお気をつけください。",
              ["たびたび", "どうにか", "かなり", "くれぐれも"], 4,
              "(Xatda) Havo sovib qolganligi sababli, iltimos, o'zingizni ehtiyot qiling.",
              reading="くれぐれも", expl="くれぐれも = qat'iy ravishda, iltimos (g'amxo'rlik ifodasi)"),
            q("t11-v4-20", "景気がなかなか回復せず、国民は内閣に（　）している。",
              ["失業", "失望", "失脚", "失礼"], 2,
              "Iqtisodiyot o'nglanmayotganligi sababli xalq vazirlar mahkamasidan hafsalasi pir bo'lmoqda (umidsizlanmoqda).",
              reading="しつぼう", expl="失望 (しつぼう) = umidsizlik, hafsala pir bo'lishi"),
            q("t11-v4-21", "母は信頼できる医師に（　）会えて運がよかった。",
              ["立ち", "兼ね", "巡り", "触れ"], 3,
              "Onam ishonchli shifokor bilan uchrashish (taqdiri bog'lanish) nasib qilib, omadi chopdi.",
              reading="めぐりあう", expl="巡り合う (めぐりあう) = taqdir taqozosi bilan uchrashmoq"),
            q("t11-v4-22", "どうもこの問題は思ったほど（　）ではなさそうで、解決に時間がかかるかもしれない。",
              ["ハード", "ワイド", "ユニーク", "シンプル"], 4,
              "Aftidan, bu muammo o'ylagandek oddiy (sodda) emasga o'xshaydi, yechimiga ancha vaqt ketishi mumkin.",
              expl="シンプル (simple) = oddiy, sodda")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t11-v5-23", "田中さんはこのごろ、【一段と】きれいになった。",
              ["急に", "少しだけ", "ますます", "まあまあ"], 3,
              "Tanaka so'nggi paytlarda yanada (tobora) ochilib, go'zallashib ketdi.",
              reading="いちだんと", expl="一段と ≈ ますます (yanada, tobora ko'proq)"),
            q("t11-v5-24", "彼はこのところ営業成績が【ふるわない】。",
              ["上がった", "落ちた", "順調だ", "不調だ"], 4,
              "Uning so'nggi paytlarda savdo ko'rsatkichlari qoniqarsiz (orqada, sust).",
              reading="ふるわない", expl="ふるわない ≈ 不調だ (sust, ko'ngildagidek emas)"),
            q("t11-v5-25", "彼は普通の人間の【ものさし】では語れない人物だ。",
              ["表現", "基準", "常識", "方法"], 2,
              "U oddiy insonning o'lchov mezonlari bilan ta'riflab bo'lmaydigan shaxsdir.",
              reading="ものさし", expl="ものさし ≈ 基準 (o'lchov mezoni, me'yor)"),
            q("t11-v5-26", "人のものを勝手に使うとは【あつかましい】やつだ。",
              ["のんきな", "気楽な", "無愛想な", "無遠慮な"], 4,
              "Birovning narsasini so'ramasdan ishlatish yuzsizlik (betgachoparlik/uyatsizlik)dir.",
              reading="あつかましい", expl="あつかましい ≈ 無遠慮な (yuzsiz, mulohazasiz, betgachopar)"),
            q("t11-v5-27", "音楽番組の【スポンサー】が決まった。",
              ["広告主", "協力者", "指導者", "責任者"], 1,
              "Musiqiy ko'rsatuvning bosh homiysi (reklama beruvchisi) aniqlandi.",
              expl="スポンサー ≈ 広告主 (homiy, reklama beruvchi kompaniya)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'zning gapda eng to'g'ri ishlatilgan variantini tanlang.",
          "questions": [
            q("t11-v6-28", "【合流】の使い方として最もよいものを選びなさい。",
              [
                "出版社と合流して、テレビドラマを製作する。",
                "あの2人はひそかに合流しあっている。",
                "先生たちと6時に駅で合流して、そこから食事に行こう。",
                "クラス全員が合流して、野外学習に出かけた。"
              ], 3,
              "合流 (gouryuu) = birlashish, uchrashib birga davom etish.",
              expl="「駅で合流して〜」= vokzalda uchrashib/qo'shilib birga ovqatlangani boramiz (to'g'ri ishlatilish)."),
            q("t11-v6-29", "【でたらめ】の使い方として最もよいものを選びなさい。",
              [
                "この週刊誌の記事は、ほとんどでたらめばかりだ。",
                "でたらめを使って、授業をさぼった。",
                "彼女がそんなにでたらめだとは気づかずに、だまされてしまった。",
                "ずっと掃除していなかったので、部屋がでたらめだ。"
              ], 1,
              "でたらめ (detarame) = asossiz uydirma, safsata, bema'nilik.",
              expl="「記事はでたらめばかりだ」= maqola uydirma va safsatalardan iborat (to'g'ri ishlatilish)."),
            q("t11-v6-30", "【肯定的】の使い方として最もよいものを選びなさい。",
              [
                "大学を新設する計画はどうやら肯定的に結論された。",
                "上司はその企画に対し、肯定的な意見を持っている。",
                "これだけ元気になれば外出も肯定的でしょうね。",
                "その件は肯定的にお受けいたします。"
              ], 2,
              "肯定的 (kouteiteki) = ijobiy, ma'qullovchi.",
              expl="「肯定的な意見」= ijobiy/qo'llab-quvvatlovchi fikr (to'g'ri ishlatilish)."),
            q("t11-v6-31", "【要旨】の使い方として最もよいものを選びなさい。",
              [
                "大統領の演説は要旨をおさえている。",
                "この町は交通上の要旨として発達した。",
                "論文には、その要旨を書いたものを付けてください。",
                "今回の事件にはいろいろな要旨が関係している。"
              ], 3,
              "要旨 (youshi) = asosiy mazmun, xulosa, tezis.",
              expl="「論文に要旨を付ける」= dissertatsiyaga uning qisqacha tezis/mazmunini ilova qilmoq (to'g'ri ishlatilish)."),
            q("t11-v6-32", "【指定】の使い方として最もよいものを選びなさい。",
              [
                "この事件の犯人を指定するのは難しい。",
                "就職はその人の人生を指定するともいえる。",
                "代表者は投票によって指定しようではないか。",
                "パーティーの参加者は指定された服装で来てください。"
              ], 4,
              "指定 (shitei) = belgilangan, maxsus ko'rsatilgan.",
              expl="「指定された服装」= belgilangan kiyim shakli (dreskod) (to'g'ri ishlatilish).")
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
            q("t11-g1-33", "ドイツではビールは夏（　）、冬にもよく飲まれている。",
              ["よらず", "はおろか", "どころか", "にかぎらず"], 4,
              "Germaniyada pivo nafaqat yozda, balki qishda ham juda ko'p iste'mol qilinadi.",
              expl="「〜に限らず」= nafaqat ..., balki boshqa payt/holatda ham."),
            q("t11-g1-34", "まだ、免許を取ったばかりの（　）、運転に自信がありません。",
              ["もので", "ものの", "ものか", "ものなら"], 2,
              "Haydovchilik guvohnomasini yaqindagina olgan bo'lsam-da, mashina haydashga unchalik ishonchim yo'q.",
              expl="「〜ものの」= ...bo'lsa-da / bo'lishiga qaramasdan."),
            q("t11-g1-35", "その状況で助かるなんて不可能に思えますが、（　）ことです。",
              ["ありようがない", "ありがたい", "ありかねる", "あり得なくない"], 4,
              "Bunday og'ir vaziyatda omon qolish imkonsizdek tuyulsa-da, bo'lishi mumkin bo'lmagan hodisa emas (bo'lishi mumkin).",
              expl="「あり得なくない」= bo'lishi ehtimoldan xoli emas (ikki karra inkor = tasdiq)."),
            q("t11-g1-36", "市長を（　）とする職員全員が、災害に備え訓練に取り組んだ。",
              ["最初", "開始", "初めて", "はじめ"], 4,
              "Boshida shahar hokimi turgan barcha xodimlar tabiiy ofatga tayyorgarlik mashg'ulotlarida qatnashdilar.",
              expl="「〜をはじめ（とする）」= ...boshchiligida, boshida ...bo'lgan barcha."),
            q("t11-g1-37", "息子は20年前にアメリカに（　）きり、一度も帰国していない。",
              ["行って", "行った", "行く", "行こう"], 2,
              "O'g'lim 20 yil avval Amerikaga ketganicha, biror marta ham vataniga qaytib kelmadi.",
              expl="「動詞た形 ＋ きり」= ...qilganicha boshqa qaytmaslik/o'zgarmaslik."),
            q("t11-g1-38", "「いただきます」と言ったか（　）のうちに、子どもたちは食べ始めた。",
              ["言おうか", "言うまいか", "言えないか", "言わないか"], 4,
              "«Yoqimli ishtaha» deb aytishar-aytmas, bolalar taomni yeyishga kirishib ketishdi.",
              expl="「〜たか〜ないかのうちに」= ...qilar-qilmas bilanoq."),
            q("t11-g1-39", "日本国内（　）果物の消費量は、最近減少している。",
              ["にあたる", "による", "における", "にいたる"], 3,
              "Yaponiya ichki bozoridagi meva iste'moli hajmi so'nggi paytlarda kamayib bormoqda.",
              expl="「〜における」= ...dagi / ...dagi sohada (joy va vaqt munosabati)."),
            q("t11-g1-40", "1回薬を飲み忘れたからといって、（　）死ぬわけではないんだから、そんなに心配しなくていいよ。",
              ["なにも", "いつも", "なんでも", "どこも"], 1,
              "Dorini bir marta ichishni unutib qoldirgan bilan darrov o'lib qoladigan narsa emas-ku, bunchalik xavotirlanma.",
              expl="「なにも〜わけではない」= darrov ...degani emas / aslo unday emas."),
            q("t11-g1-41", "すぐに返してくれるなら、お金を貸して（　）。",
              ["あげるはずがない", "あげることがない", "あげないはずがない", "あげないこともない"], 4,
              "Darhol qaytarib beradigan bo'lsang, senga qarz berib turmasligim ham mumkin emas (berishim mumkin).",
              expl="「〜ないこともない」= ...emas ham emas (qarz berishga tayyorman)."),
            q("t11-g1-42", "私が子どものころ、国内旅行より海外旅行のほうが安くなるなんて（　）。",
              ["だれもが想像しただろう", "だれが想像しただろう", "だれでも想像できただろう", "だれも想像できただろう"], 2,
              "Men bolaligimda ichki sayohatdan ko'ra xorijiy sayohat arzonroq bo'lishini kim ham tasavvur qilibdi deysiz?! (hech kim kutmagan).",
              expl="「だれが〜だろう（か）」= kim ham o'ylabdi deysiz (inkor ma'nosidagi ritorik savol)."),
            q("t11-g1-43", "決まりを守っている人がほとんど（　）、あなたも守らなくていいわけではない。",
              ["いないからこそ", "いなくもないからこそ", "いないからといって", "いないことはないから"], 3,
              "Qoidaga amal qilayotganlar deyarli yo'qligi sababli deb, siz ham qoidani buzishingiz mumkin degani emas.",
              expl="「〜からといって（〜わけではない）」= ...bo'lgani sababli deb aslo ...degani emas."),
            q("t11-g1-44", "当社の面接を受ける方は、10日の10時までに本社ビルに（　）。",
              ["おこしください", "おまいりください", "こされてください", "うかがってください"], 1,
              "Kompaniyamiz suhbatida qatnashuvchilar 10-sana soat 10:00 gacha bosh ofis binosiga tashrif buyurishingiz so'raladi.",
              expl="「お越しください」= kelishingizni so'raymiz (kelmoq fe'lining hurmat shakli).")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の＿★＿に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keladigan eng to'g'ri variantni tanlang.",
          "questions": [
            q("t11-g2-45", None,
              ["効くが", "人に", "アレルギー", "よっては"], 4,
              "Bu dori yaxshi ta'sir qiladi-yu, lekin ba'zi odamlarda allergiya qo'zg'atishi mumkinligi tufayli ehtiyotkorlik zarur.",
              prefix="この薬はよく", suffix="を起こすので、注意が必要だ。",
              starPos=3, order=[1, 2, 4, 3],
              expl="Tartib: 効くが(1) 人に(2) よっては(4) アレルギー(3) → Yulduzcha 3-o'rinda: よっては(4)"),
            q("t11-g2-46", None,
              ["予想した", "基づいて", "結果", "に"], 1,
              "O'tgan 10 yillik ma'lumotlarga asoslanib qilingan prognoz xulosasiga ko'ra, bolalar soni kamayishda davom etsa kerak.",
              prefix="過去10年間のデータ", suffix="、これからも子どもは減り続けるだろう。",
              starPos=3, order=[4, 2, 1, 3],
              expl="Tartib: に(4) 基づいて(2) 予想した(1) 結果(3) → Yulduzcha 3-o'rinda: 予想した(1)"),
            q("t11-g2-47", None,
              ["また忘れて", "ことか", "注意された", "わからないのに"], 2,
              "Vazifani unutib qoldirmaslik haqida necha bor ogohlantirilganimni bilmayman-u, ammo yana unutib qo'yibman.",
              prefix="宿題を忘れないように何度", suffix="しまった。",
              starPos=2, order=[3, 2, 4, 1],
              expl="Tartib: 注意された(3) ことか(2) わからないのに(4) また忘れて(1) → Yulduzcha 2-o'rinda: ことか(2)"),
            q("t11-g2-48", None,
              ["あわてて", "にせよ", "ばかなことを", "いた"], 4,
              "U paytda sarosimada bo'lgan taqdirimda ham, bema'ni ish qilib qo'yganimdan pushaymonman.",
              prefix="あのときは", suffix="してしまったと後悔している。",
              starPos=2, order=[1, 4, 2, 3],
              expl="Tartib: あわてて(1) いた(4) にせよ(2) ばかなことを(3) → Yulduzcha 2-o'rinda: いた(4)"),
            q("t11-g2-49", None,
              ["しっかりしていても", "兄のほうが", "よい", "いえば"], 1,
              "Yosh jihatidan qaralsa akasi ko'proq mustaqil va hushyor bo'lishi kerak bo'lsa-da, ukasi ancha jiddiyroq.",
              prefix="年齢から", suffix="はずなのに、弟のほうがしっかりしている。",
              starPos=3, order=[4, 2, 1, 3],
              expl="Tartib: いえば(4) 兄のほうが(2) しっかりしていても(1) よい(3) → Yulduzcha 3-o'rinda: しっかりしていても(1)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlarga eng mos keluvchi javobni tanlang.",
          "passage": "ほんの数十年前は、たばこを吸うことは大人の男性にとって、悪いこと【 50 】当然のことと思われていた。新幹線も禁煙車両は1両だけだった。1980年、たばこの煙が嫌いな人が集まって当時の国鉄（今のJR）と国を相手に、「他人のたばこの煙を吸わない権利」を求める裁判を起こした。\n　裁判は7年もかかったあげく、結局【 51 】。判決理由は「列車の中で隣の人のたばこの煙を吸わされるのは一時的なこと。たばこを吸うのは日本社会では普通のこと」ということだった。\n　しかし、訴えた人々は、【 52 】がっかりも怒りもしなかった。なぜならば「私もたばこはいやだ」と言い出す人が増えて、国鉄もその声を無視することができなくなり、すでに新幹線の車両の7割が禁煙になっていた。事実上は勝ったと言えるからだ。\n　その後、たばこを吸っている本人よりも、隣でその煙を吸ってしまう人のほうが煙の【 53 】ことがわかって、いっそう分煙対策（注）が進んだ。\n　2003年には「健康増進法」という法律もできて、病院や学校など公共の場はほとんどが禁煙になった。歩きたばこを禁止する町も出てきた。\n　今やたばこを吸う人の肩身はますます狭くなり、限られた場所でこっそり吸うしかなくなった。そして2010年にはたばこが大幅に値上げされた。近い将来には1箱1000円になるとも言われている。そうなると【 54 】得ない人もさらに増えるだろう。\n（注）分煙＝たばこを吸う場所や人を分けること",
          "questions": [
            q("t11-g3-50", None,
              ["以上に", "というより", "とすれば", "にかけては"], 2,
              "O'n yillar oldin chekish katta yoshli erkaklar uchun yomon narsa bo'lishdan ko'ra, tabiiy hol deb qaralardi.",
              blankNo=50, expl="「〜というより（当然のこと）」= ...dan ko'ra tabiiy holat deb."),
            q("t11-g3-51", None,
              ["訴えは認められた", "訴えは認められなかった", "訴えを認めがたかった", "訴えを認めかねた"], 2,
              "Sud 7 yil davom etgan bo'lsa-da, oxir-oqibat da'vo qanoatlantirilmadi (rad etildi).",
              blankNo=51, expl="「訴えは認められなかった」= da'vo qabul qilinmadi / rad etildi."),
            q("t11-g3-52", None,
              ["負けただけあって", "負けたからといって", "負けたとしたら", "負けたとしても"], 2,
              "Biroq da'vogarlar sudda yutqazgan bo'lsalar-da, na xafa bo'lishdi va na g'azablanishdi.",
              blankNo=52, expl="「負けたからといって（〜ない）」= mag'lub bo'lgani sababli deb aslo tushkunlikka tushmadilar."),
            q("t11-g3-53", None,
              ["害はない", "害が少ない", "害が大きい", "害が変わらない"], 3,
              "...tutunni passiv yutayotgan yonidagi odamga zarari kattaroqligi aniqlandi.",
              blankNo=53, expl="「害が大きい」= zarari kattaroq bo'lishi."),
            q("t11-g3-54", None,
              ["禁煙し", "たばこを吸わざるを", "たばこを吸い", "禁煙せざるを"], 4,
              "Bunday holatda chekishni tashlashga majbur bo'ladiganlar soni yanada ortadi.",
              blankNo=54, expl="「禁煙せざるを得ない」= chekishni tashlashga majbur bo'lmoq.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK! test11.json yaratildi: {len(data['sections'][0]['problems'])} vocab + {len(data['sections'][1]['problems'])} grammar bo'limlari.")
