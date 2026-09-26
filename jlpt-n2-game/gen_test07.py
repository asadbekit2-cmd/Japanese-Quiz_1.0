# -*- coding: utf-8 -*-
"""
test07.json generatori — 第7回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.8, Savollar p.68-77
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test07.json")

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
  "id": 7,
  "title_jp": "第7回 模擬テスト",
  "title_uz": "7-test",
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
            q("t7-v1-1", "こんなに食費がかかるとは【勘定】に入れてなかった。",
              ["かんてい", "かんじょう", "かんでい", "かんしょう"], 2,
              "Bunchalik oziq-ovqat xarajati ketishini hisob-kitobga (rejamga) kiritmagan edim.",
              reading="かんじょう", expl="勘定 → かんじょう (hisob-kitob, hisobga olish)"),
            q("t7-v1-2", "飛行機事故の原因を【徹底的】に調査する。",
              ["てっていてき", "てつていてき", "てつでいてき", "てっていてき"], 4,
              "Samolyot halokati sabablarini tubdan (to'liq va atroflicha) tekshirmoqdalar.",
              reading="てっていてき", expl="徹底的 → てっていてき (tubdan, har tomonlama, izchil)"),
            q("t7-v1-3", "太陽光に【干した】野菜は、ビタミンDが増える。",
              ["かわかした", "さらした", "みたした", "ほした"], 4,
              "Quyosh nurida quritilgan sabzavotlarda D vitamini ko'payadi.",
              reading="ほした", expl="干す → ほす (quritmoq, oftobda quritmoq)"),
            q("t7-v1-4", "あの会社の経営状況はここ数年【下降】している。",
              ["げこう", "げごう", "かこう", "かごう"], 3,
              "U kompaniyaning moliyaviy ahvoli so'nggi bir necha yilda pasayib (tushib) bormoqda.",
              reading="かこう", expl="下降 → かこう (pasayish, pastga qarab ketish)"),
            q("t7-v1-5", "休んでも取れない疲れを【抱えて】いる現代人が多くなった。",
              ["かかえて", "おぼえて", "たくわえて", "おさえて"], 1,
              "Dam olsa ham ketmaydigan charchoqni o'zida ko'tarib yurgan zamonaviy insonlar ko'payib qoldi.",
              reading="かかえて", expl="抱える → かかえる (ko'tarib/tutib yurmoq, yuk/muammoni o'zida saqlamoq)")
          ]
        },
        {
          "id": "v2", "type": "orthography",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zning to'g'ri kanji yozuvini tanlang.",
          "questions": [
            q("t7-v2-6", "心から【やまう】オペラ歌手の初来日が決定して、今からわくわくしている。",
              ["敬う", "尊う", "仰う", "拝う"], 1,
              "Chin dildan hurmat qiladigan opera xonandamning Yaponiyaga ilk bor kelishi belgilandi, hozirdanoq hayajondaman.",
              reading="やまう", expl="敬う → うやまう (e'zozlamoq, hurmat qilmoq)"),
            q("t7-v2-7", "新人作家のデビュー作はサイトで厳しく【ひひょう】された。",
              ["非評", "比評", "品評", "批評"], 4,
              "Yangi yozuvchining debyut asari saytda qattiq tanqid qilindi (baholandi).",
              reading="ひひょう", expl="批評 → ひひょう (tanqid, taqriz, baho)"),
            q("t7-v2-8", "あくびはなぜ他人に【でんせん】するのかは、まだ学問的にわかっていない。",
              ["電染", "伝染", "伝線", "電線"], 2,
              "Esnash nega boshqalarga yuqishi hali ilmiy jihatdan aniqlanmagan.",
              reading="でんせん", expl="伝染 → でんせん (yuqish, infeksiya/ta'sir o'tishi)"),
            q("t7-v2-9", "生きている時間に限りがあると考えると、【きちょう】な時間を無駄にはできない。",
              ["貴重", "希重", "貴調", "希調"], 1,
              "Yashayotgan vaqtimiz cheklanganligini o'ylasak, qimmatli vaqtni bekorga o'tkazib bo'lmaydi.",
              reading="きちょう", expl="貴重 → きちょう (qimmatli, nodir, qadrli)"),
            q("t7-v2-10", "近くのコンビニで、アルバイト店員を【ぼしゅう】している。",
              ["慕集", "暮集", "募集", "墓集"], 3,
              "Yaqin atrofdagi qulaylik do'konida (kombini) yarim kunlik sotuvchi xodimlar qabul qilinmoqda (ishga chaqirilmoqda).",
              reading="ぼしゅう", expl="募集 → ぼしゅう (yollash, qabul qilish, to'plash)")
          ]
        },
        {
          "id": "v3", "type": "context",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'z/affiksni tanlang.",
          "questions": [
            q("t7-v3-11", "自動車に代表される製造（　）が日本の貿易をリードしてきた。",
              ["性", "権", "行", "業"], 4,
              "Avtomobillar bilan ifodalangan ishlab chiqarish sohasi (sanoati) Yaponiya savdosini yetaklab kelgan.",
              expl="製造業 (せいぞうぎょう) = ishlab chiqarish sanoati/tarmog'i"),
            q("t7-v3-12", "（　）成年の人と運転手は、お酒を飲んではいけませんよ。",
              ["未", "非", "不", "来"], 1,
              "Voyaga yetmagan shaxslar va haydovchilar spirtli ichimlik ichishi taqiqlanadi.",
              expl="未成年 (みせいねん) = voyaga yetmagan shaxs"),
            q("t7-v3-13", "シェイクスピアの作品には数々の（　）文句がある。",
              ["明", "美", "名", "大"], 3,
              "Shekspirning asarlarida juda ko'plab mashhur iqtiboslar (mashhur iboralar) mavjud.",
              expl="名文句 (めいもんく) = mashhur ibora, ajoyib iqtibos"),
            q("t7-v3-14", "最近、テニスのサーブに安定（　）が出てきた。",
              ["化", "心", "感", "面"], 3,
              "Yaqinda tennisda to'p uzatishimda (servis) barqarorlik hissi/sifati paydo bo'ldi.",
              expl="安定感 (あんていかん) = barqarorlik hissi, ishonchlilik"),
            q("t7-v3-15", "腕のいい料理（　）を雇う。",
              ["人", "者", "工", "士"], 1,
              "Qo'li shirin (mahoratli) oshpazni ishga yollamoqchimiz.",
              expl="料理人 (りょうりにん) = oshpaz")
          ]
        },
        {
          "id": "v4", "type": "paraphrase",
          "instruction_jp": "（　）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga eng mos keladigan so'zni tanlang.",
          "questions": [
            q("t7-v4-16", "彼は日本一の数学者なのに、決していばらない（　）な人柄だ。",
              ["堅実", "謙虚", "地味", "丁寧"], 2,
              "U Yaponiyadagi birinchi raqamli matematik bo'lishiga qaramay, aslo kibrlanmaydigan kamtarin shaxsdir.",
              reading="けんきょ", expl="謙虚 (けんきょ) = kamtar, xokisor"),
            q("t7-v4-17", "マラソン大会で、腰やひざの痛みを（　）、経験の浅いランナーが多い。",
              ["訴える", "止める", "治める", "捕らえる"], 1,
              "Marafon musobaqasida bel yoki tizza og'rig'idan shikoyat qilayotgan tajribasi kam yuguruvchilar ko'p.",
              reading="うったえる", expl="（痛みを）訴える = og'riqdan shikoyat qilmoq/arz qilmoq"),
            q("t7-v4-18", "飲み会の日、友だちと居酒屋で（　）。",
              ["立ち合った", "取り合った", "張り合った", "落ち合った"], 4,
              "O'tirish kuni do'stlar bilan izakaya (restoran)da uchrashdik (belgilangan joyda to'plandik).",
              reading="おちあった", expl="落ち合う (おちあう) = kelishilgan joyda uchrashmoq"),
            q("t7-v4-19", "駅前の広場で通行人に（　）中のジュースを無料で配っていた。",
              ["キャンペーン", "コンテスト", "ショッピング", "キャンプ"], 1,
              "Vokzal oldidagi maydonda o'tkinchilarga aksiya (targ'ibot)dagi sharbatni bepul tarqatishayotgan edi.",
              expl="キャンペーン (campaign) = aksiya, reklama kompaniyasi"),
            q("t7-v4-20", "（　）家には子どもがそのまま大人になったような人が多いと思う。",
              ["学者", "芸能", "冒険", "競技"], 3,
              "Sarguzashtsevarlar (sayyoh-sarguzashtchilar) orasida go'yo bola ulg'aymasdan katta bo'lib qolgandek insonlar ko'p deb o'ylayman.",
              reading="ぼうけん", expl="冒険家 (ぼうけんか) = sarguzashtsevar, sayyoh"),
            q("t7-v4-21", "仕事を始める前に（　）お茶でも飲んで、疲れをとってください。",
              ["いまに", "しきりに", "いくぶん", "ひとまず"], 4,
              "Ishni boshlashdan oldin hozircha (vaqtincha) choy ichib, charchoqni chiqaring.",
              reading="ひとまず", expl="ひとまず = hozircha, avvalambor, vaqtincha"),
            q("t7-v4-22", "平気でうそをつくあの男が政治家になるだなんて、（　）話だ。",
              ["すまない", "やむを得ない", "とんでもない", "やかましい"], 3,
              "Hech narsa bo'lmagandek yolg'on gapiradigan u odamning siyosatchi bo'lishi aqlga sig'maydigan (bema'ni) gapdir.",
              reading="とんでもない", expl="とんでもない = aqlga sig'mas, bo'lmag'ur, asossiz")
          ]
        },
        {
          "id": "v5", "type": "usage",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t7-v5-23", "ライバルは自信に【あふれていた】。",
              ["欠けていた", "満ちていた", "輝いていた", "甘えていた"], 2,
              "Raqibim o'ziga bo'lgan ishonchga to'lib-toshgan edi.",
              reading="あふれていた", expl="あふれる ≈ 満ちる (to'lib-toshmoq)"),
            q("t7-v5-24", "事件の【裏を】こっそり調べる。",
              ["その後", "犯人", "隠れた事情", "被害"], 3,
              "Hodisaning yashirin sabablarini (orqa tomonini) bildirmasdan tekshirmoqda.",
              reading="うらを", expl="裏 ≈ 隠れた事情 (parda ortidagi / yashirin holatlar)"),
            q("t7-v5-25", "犯人はあの人です。【現に】私はこの目で見たんですから。",
              ["その場で", "一瞬", "本来", "実際に"], 4,
              "Jinoyatchi anavi kishi. Haqiqatan ham (amalda) men o'z ko'zim bilan ko'rganman.",
              reading="げんに", expl="現に ≈ 実際に (amalda, fakt sifatida, haqiqatan ham)"),
            q("t7-v5-26", "先生が自ら【手を取って】生徒を指導した。",
              ["丁寧に", "進んで", "無理に", "適切に"], 1,
              "Ustoz shaxsan o'zi juda erinmay (sinchkovlik/muloyimlik bilan) o'quvchiga yo'l-yo'riq ko'rsatdi.",
              reading="てをとって", expl="手を取って ≈ 丁寧に (juda sinchkovlik va g'amxo'rlik bilan)"),
            q("t7-v5-27", "システムの【エラー】で、大事なメールを送れなかった。",
              ["更新", "誤り", "破壊", "変更"], 2,
              "Tizim xatoligi (error) tufayli muhim xatni jo'nata olmadim.",
              reading="えらー", expl="エラー ≈ 誤り (xatolik, nosozlik)")
          ]
        },
        {
          "id": "v6", "type": "usage_special",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'zning gapda eng to'g'ri ishlatilgan variantini tanlang.",
          "questions": [
            q("t7-v6-28", "【加減】の使い方として最もよいものを選びなさい。",
              [
                "この料理を作るときは、ときどき火の強さを加減しなさい。",
                "加減の悪いことに、出かけようとしたときに雨が降り出してきた。",
                "あの男の常識の加減はその程度のものだよ。",
                "風邪をひいて、すっかり加減ができなくなった。"
              ], 1,
              "加減 (kagen) = me'yoriga keltirish, moslashtirish, holat.",
              expl="「火の強さを加減する」= olov balandligini me'yoriga keltirmoq (to'g'ri ishlatilish)."),
            q("t7-v6-29", "【ねらい】の使い方として最もよいものを選びなさい。",
              [
                "優勝という大きなねらいに向かってがんばる。",
                "税金を下げた政府のねらいは、今度の選挙に勝つことだ。",
                "この道路は来年までの完成をねらいにしている。",
                "今日の買い物のねらいは冬の洋服です。"
              ], 2,
              "ねらい (nerai) = maqsad, ko'zlangan reja/muddao.",
              expl="「政府のねらいは〜」= hukumatning ko'zlagan maqsadi... (to'g'ri ishlatilish)."),
            q("t7-v6-30", "【陽気】の使い方として最もよいものを選びなさい。",
              [
                "会社は法律に陽気な人を求めています。",
                "あの子は陽気にふるまっているが、両親の離婚にとても傷ついている。",
                "しっかり勉強すれば若い君たちの将来は陽気だ。",
                "今日は母親の陽気がいつになくいい。"
              ], 2,
              "陽気 (youki) = quvnoq, xushchaqchaq, ob-havo holati.",
              expl="「陽気にふるまう」= o'zini xushchaqchaq va quvnoq tutmoq (to'g'ri ishlatilish)."),
            q("t7-v6-31", "【気配】の使い方として最もよいものを選びなさい。",
              [
                "彼女はとても気配のいい人だ。",
                "被災地の人々の気配をレポートする。",
                "故郷の町はすっかり気配が変わってしまった。",
                "この家は人の住んでいる気配がまったくない。"
              ], 4,
              "気配 (kehai) = alomat, belgi, sharpasi.",
              expl="「人の住んでいる気配がない」= odam yashayotganlik belgisi/sharpasi sezilmaydi (to'g'ri ishlatilish)."),
            q("t7-v6-32", "【引用】の使い方として最もよいものを選びなさい。",
              [
                "西洋の小説には、聖書から引用された言葉が多い。",
                "秘密の情報がこっそり国外に引用されてしまった。",
                "教授の本を1週間引用させていただいた。",
                "他人の力をいつも引用するわけにはいかない。"
              ], 1,
              "引用 (in'you) = iqtibos keltirish, sitata olish.",
              expl="「聖書から引用された言葉」= Injildan iqtibos olingan so'zlar (to'g'ri ishlatilish).")
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
            q("t7-g1-33", "お客様のご希望（　）、夜8時まで営業することにしました。",
              ["にそなえて", "に対して", "に際して", "に応えて"], 4,
              "Mijozlarning istaklariga binoan (javoban), soat 20:00 gacha xizmat ko'rsatishga qaror qildik.",
              expl="「〜に応えて」= ...ga javoban, istak/talabni qondirish maqsadida."),
            q("t7-g1-34", "電車を降りる（　）、傘を忘れないようにしてください。",
              ["前に", "後に", "際に", "間に"], 3,
              "Poyezddan tushayotganda soyabonni unutib qoldirmaslikka e'tibor bering.",
              expl="「〜に際して / 際(に)」= ...aynan shu vaziyatda / paytida (rasmiy uslub)."),
            q("t7-g1-35", "きのう雨にぬれた（　）、今日はなんとなく熱っぽい。",
              ["せいか", "ことか", "わけか", "ものか"], 1,
              "Kecha yomg'irda qolib iviganim sababli bo'lsa kerak, bugun nimagadir isitmalayapman.",
              expl="「〜せい（で/か）」= ...yomon natijaning sababi bo'lib (tufayli)."),
            q("t7-g1-36", "動物たちのかわいい動きに、（　）はいられませんでした。",
              ["笑って", "笑うどころで", "笑わずには", "笑わなくて"], 3,
              "Hayvonchalarning yoqimli harakatlariga kulmasdan tura olmadim.",
              expl="「〜ずにはいられない」= ...qilmasdan tura olmaslik."),
            q("t7-g1-37", "上司とけんかして会社を辞めた彼女は、新しい職場で生き生きと（　）働いている。",
              ["楽しいらしく", "楽しげに", "楽しいように", "楽しいそうに"], 2,
              "Boshlig'i bilan urishib kompaniyadan ketgan u qiz yangi ish joyida zavq bilan (quvnoq qiyofada) ishlamoqda.",
              expl="「〜げ（に）」= ...kayfiyat/ko'rinish bilan (－げ)."),
            q("t7-g1-38", "A「この計画について、なにか意見がありますか。」\\nB「そうですね、（　）と言ってありません。」",
              ["これ", "それ", "あれ", "どれ"], 1,
              "A: «Bu reja bo'yicha biron fikringiz bormi?» — B: «Xo'sh, aytarli (alohida) biror fikrim yo'q.»",
              expl="「これと言って（〜ない）」= aytarli hech narsa yo'q."),
            q("t7-g1-39", "助けてくれた人に、感謝の気持ちを（　）手紙を書いた。",
              ["詰めて", "入れて", "注いで", "込めて"], 4,
              "Menga yordam bergan meribon insonga minnatdorchilik tuyg'usini jo qilib xat yozdim.",
              expl="「〜を込めて」= chin ko'ngildan tuyg'u/mehr bilan qo'shib."),
            q("t7-g1-40", "田舎で（　）車が必要なので、自動車学校に行くことにした。",
              ["生活する最中に", "生活する上では", "生活しようとするために", "生活することには"], 2,
              "Qishloqda yashash nuqtai nazaridan (yashash uchun) mashina zarur bo'lgani uchun haydovchilik maktabiga borishga qaror qildim.",
              expl="「〜上では」= ...nuqtai nazaridan, ...jihatdan qaraganda."),
            q("t7-g1-41", "新しい料理を覚えたので、さっそく作って母に（　）と思う。",
              ["食べさせてあげよう", "食べてあげよう", "食べさせてしまおう", "食べてしまおう"], 1,
              "Yangi taomni o'rganganim sababli, darhol tayyorlab oyimga yegizib (tatitib) ko'ray deb o'ylayapman.",
              expl="「食べさせてあげる」= yegizib bermoq / taomdan bahramand qilmoq."),
            q("t7-g1-42", "がんばって書類を作ったのに、ミスがたくさん見つかってしまった。確認（　）よ。",
              ["しておけばよかった", "しないでおけばよかった", "したままでよかった", "しないままでよかった"], 1,
              "Astoydil hujjatni tayyorlagan bo'lsam-da, ko'p xatolar chiqib qoldi. Oldindan tekshirib qo'ysam bo'lar ekan!",
              expl="「〜ておけばよかった」= ...qilib qo'yganimda yaxshi bo'lardi (afsus ifodasi)."),
            q("t7-g1-43", "前田君は有名な大学の文学部を（　）、よく言葉を間違えて使う。",
              ["出ただけあって", "出ているにしては", "出ただけあっては", "出ているにしろ"], 2,
              "Maeda mashhur universitetning filologiya fakultetini bitirganiga qaramasdan (nisbatan olganda), so'zlarni tez-tez noto'g'ri ishlatadi.",
              expl="「〜にしては」= ...deb hisoblaganda unga xos bo'lmagan tarzda / kutilganidan boshqacha."),
            q("t7-g1-44", "私は音楽大学に行きたいのだが、我が家の経済状態では（　）だろう。",
              ["あきらめざるを得ない", "あきらめるわけにいかない", "あきらめられない", "あきらめかねる"], 1,
              "Men musiqa universitetiga kirishni istayman, lekin oilamizning moliyaviy ahvolida voz kechishga majbur bo'laman shekilli.",
              expl="「〜ざるを得ない」= ...qilishdan boshqa iloji yo'q / majbur bo'lmoq.")
          ]
        },
        {
          "id": "g2", "type": "sentence_order",
          "instruction_jp": "次の文の＿★＿に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keladigan eng to'g'ri variantni tanlang.",
          "questions": [
            q("t7-g2-45", None,
              ["ことには", "使って", "実際に", "みない"], 4,
              "U mahsulot qanchalik ajoyib bo'lmasin, amalda ishlatib ko'rilmaguncha ishonib bo'lmaydi.",
              prefix="その製品がどんなにすばらしくても、", suffix="信用できない。",
              starPos=3, order=[3, 2, 4, 1],
              expl="Tartib: 実際に(3) 使って(2) みない(4) ことには(1) → 「〜てみないことには (ishlatib ko'rmaguncha)」"),
            q("t7-g2-46", None,
              ["遠足は", "とっての", "大人に", "とって"], 1,
              "Kichik bolalar uchun ekskursiya kattalar uchun xorijiy sayohat kabi katta quvonchdir.",
              prefix="小さな子どもに", suffix="の海外旅行くらい大きな楽しみだ。",
              starPos=2, order=[2, 1, 3, 4],
              expl="Tartib: とっての(2) 遠足は(1) 大人に(3) とって(4) → Yulduzcha 2-o'rinda: 遠足は(1)"),
            q("t7-g2-47", None,
              ["ないが", "わけでも", "許さない", "なら"], 2,
              "Chin dildan pushaymon bo'layotgan bo'lsa kechirmayman ham emas-ku, ammo durustroq uzr so'rashini xohlayman.",
              prefix="心から反省している", suffix="ちゃんと謝ってほしい。",
              starPos=3, order=[4, 3, 2, 1],
              expl="Tartib: なら(4) 許さない(3) わけでも(2) ないが(1) → Yulduzcha 3-o'rinda: わけでも(2)"),
            q("t7-g2-48", None,
              ["考え", "思い切って", "末", "抜いた"], 3,
              "Uch kun davomida chuqur o'ylab bo'lgach, nihoyat qat'iy qarorga kelib ishdan bo'shashga qaror qildim.",
              prefix="3日間、", suffix="会社を辞めることにしました。",
              starPos=3, order=[1, 4, 3, 2],
              expl="Tartib: 考え(1) 抜いた(4) 末(3) 思い切って(2) → 「〜考え抜いた末 (chuqur o'ylash natijasida)」"),
            q("t7-g2-49", None,
              ["思い出そう", "何だっ", "と", "たっけ"], 4,
              "Anavi xonandaning ismi nima edi deb eslashga qancha urinmayin, aslo eslay olmayapman.",
              prefix="あの歌手の名前は", suffix="としても、どうしても思い出せない。",
              starPos=2, order=[2, 4, 3, 1],
              expl="Tartib: 何だっ(2) たっけ(4) と(3) 思い出そう(1) → Yulduzcha 2-o'rinda: たっけ(4)")
          ]
        },
        {
          "id": "g3", "type": "text_grammar",
          "instruction_jp": "次の文章を読んで、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlarga eng mos keluvchi javobni tanlang.",
          "passage": "現代の日本人の30〜34歳の人でまだ結婚していない人は、男性が50%近く、女性が約30%で、これは30年前に比べて男性は3倍、女性は4倍になっている。\n　結婚しない理由は、1つには長引く不景気で、経済的に家庭を持つ自信のない【 50-a 】が増えたことがある。また、世間も「人は絶対、結婚するべきだ」という考え方が薄くなってきた。【 50-b 】でも、コンビニや電化製品のおかげで、家事をしてくれる人が必要なくなった。女性も仕事を持つ人が多くなり、生活のために【 51 】ことも理由の1つだ。\n　しかし親【 52 】「若いうちはいいけれど、年を取ってから1人ではさびしい」と心配でたまらず、「何とか結婚してほしい」と悩む人が多い。\n　そこである会社が親同士の「代理お見合いパーティー」を開いたところ、多くの申し込みがあったそうだ。\n　親たちは子どもの写真と仕事や趣味を書いた紙を持ち、それを異性の子どもを持つ親に見せて自分の子どもを売り込む。自分の娘や息子もすでに【 53 】、親も必死である。「大人ならば、結婚相手【 54 】、親に頼らず自分で見つけたらどうだ」と言う人も多い。\n　しかし考えれば、日本ではちょっと前までは子どもの結婚相手を、親、特に父親が決めたものだ。そう考えれば、それほど新しいことではないのかもしれない。",
          "questions": [
            q("t7-g3-50", None,
              ["a 独身者 ／ b 独身", "a 既婚者 ／ b 既婚", "a 独身者 ／ b 既婚", "a 既婚者 ／ b 独身"], 1,
              "a: 独身者 (bo'ydoqlar/turmush qurmaganlar), b: 独身 (bo'ydoqlik holati).",
              blankNo=50, expl="50-a bo'sh joyga «独身者» (oila qurmagan insonlar), 50-b ga esa «独身でも» (oila qurmasdan yolg'iz bo'lsa ham) mos keladi."),
            q("t7-g3-51", None,
              ["結婚しなくてはならなかった", "結婚せざるを得なくなった", "結婚しなくてもよくなった", "結婚してはいられなくなった"], 3,
              "...ayollar ham ishli bo'lib, tirikchilik uchun turmush qurish shart bo'lmay qolganligi...",
              blankNo=51, expl="「〜しなくてもよくなった」= ...qilishga hojat qolmay qoldi / shart bo'lmay qoldi."),
            q("t7-g3-52", None,
              ["によっては", "からすると", "でさえ", "については"], 2,
              "Lekin ota-onalar nuqtai nazaridan qaralganda...",
              blankNo=52, expl="「親からすると」= ota-onalar nuqtai nazaridan / ota-onalar qarashi bo'yicha."),
            q("t7-g3-53", None,
              ["若いからといって", "若いからこそ", "若くないとはいえ", "若くないとあって"], 4,
              "O'zlarining qiz yoki o'g'illari allaqachon yosh emasligi ma'lum bo'lgani sababli, ota-onalar ham jon-jahdi bilan harakat qilmoqda.",
              blankNo=53, expl="「〜とあって」= ...vaziyat bo'lganligi sababli."),
            q("t7-g3-54", None,
              ["のみは", "くらいは", "さえ", "こそ"], 2,
              "«Katta odam bo'lgandan keyin, hech bo'lmaganda turmush o'rtog'ini ota-onaga tayanmasdan o'zi topishi kerak emasmi...»",
              blankNo=54, expl="「結婚相手くらいは」= hech bo'lmaganda umr yo'ldoshini bo'lsa ham.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK! test07.json yaratildi: {len(data['sections'][0]['problems'])} vocab + {len(data['sections'][1]['problems'])} grammar bo'limlari.")
