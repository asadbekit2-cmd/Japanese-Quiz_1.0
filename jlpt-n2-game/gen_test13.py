# -*- coding: utf-8 -*-
"""
test13.json generatori — 第13回 模擬テスト (JLPT N2 直前対策)
Kitob manbasi: 別冊 解答 p.14, Savollar p.128-137
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "test13.json")

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
  "id": 13,
  "title_jp": "第13回 模擬テスト",
  "title_uz": "13-test",
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
            q("t13-v1-1", "太平洋高気圧に【覆われて】晴れる日が多く、各地で激しい暑さが続いている。",
              ["おおわれて", "ねらわれて", "みまわれて", "ためらわれて"], 1,
              "Tinch okeani yuqori bosimi bilan qoplanib, quyoshli kunlar ko'payib, har joyda kuchli jazirama davom etmoqda.",
              reading="おおわれて", expl="覆われる → おおわれる (qoplanmoq, qamrab olinmoq)"),
            q("t13-v1-2", "彼は運動神経が【抜群】にいい。",
              ["ばつくん", "ばっくん", "ばつぐん", "ばっぐん"], 3,
              "Uning harakat koordinatsiyasi (sport qobiliyati) ajoyib darajada yaxshi.",
              reading="ばつぐん", expl="抜群 → ばつぐん (ajoyib, tengsiz, ajralib turadigan)"),
            q("t13-v1-3", "博物館の鯨の【標本】を見上げて、その大きさを実感した。",
              ["びょうほん", "ひょうぽん", "ひょうほん", "びょうぽん"], 3,
              "Muzeydagi kit nusxasini (namunasini) tepaga qarab ko'rib, uning kattaligini his qildim.",
              reading="ひょうほん", expl="標本 → ひょうほん (namuna, eksponat, nusxa)"),
            q("t13-v1-4", "古いパソコンなので、動作が【鈍い】。",
              ["とろい", "はやい", "わるい", "にぶい"], 4,
              "Eski kompyuter bo'lgani sababli, ishlashi (reaksiyasi) sekin / sust.",
              reading="にぶい", expl="鈍い → にぶい (sekin, sust, o'tmas)"),
            q("t13-v1-5", "彼女は子どものころから、医者となって世の中に【貢献】したいと考えていた。",
              ["みつけん", "こうけん", "みつこん", "こうこん"], 2,
              "U bolaligidan shifokor bo'lib jamiyatga hissa qo'shishni xohlar edi.",
              reading="こうけん", expl="貢献 → こうけん (hissa qo'shish, xizmat qilish)")
          ]
        },
        {
          "id": "v2", "type": "kanji_writing",
          "instruction_jp": "＿＿の言葉を漢字で書くとき、最もよいものを1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zni kanjida yozish uchun eng to'g'risini tanlang.",
          "questions": [
            q("t13-v2-1", "自分を【かだい】評価している人は、ちょっとした失敗にも落ち込みやすい。",
              ["仮大", "加大", "過大", "課大"], 3,
              "O'ziga haddan tashqari yuqori baho beradigan odamlar kichik bir muvaffaqiyatsizlikdan ham tushkunlikka tushib qolishlari oson.",
              reading="かだい", expl="過大 → かだい (haddan tashqari katta/yuqori; 過大評価 = ortiqcha baholash)"),
            q("t13-v2-2", "世界記録をなんと0.5秒も【ちぢめる】好タイムで優勝した。",
              ["縮める", "減める", "損める", "短める"], 1,
              "Jahon rekordini naq 0.5 soniyaga qisqartirgan yaxshi natija bilan g'alaba qozondi.",
              reading="ちぢめる", expl="縮める → ちぢめる (qisqartirmoq, qisqartirish)"),
            q("t13-v2-3", "社長の【さいしゅう】決定は絶対に変わらない。",
              ["再終", "最終", "再修", "最修"], 2,
              "Prezidentning yakuniy qarori hech qachon o'zgarmaydi.",
              reading="さいしゅう", expl="最終 → さいしゅう (yakuniy, so'nggi)"),
            q("t13-v2-4", "彼女は家事や育児を夫と【ぶんたん】し、共働きを続けている。",
              ["分拍", "分拒", "分抽", "分担"], 4,
              "U uy ishlari va bola tarbiyasini eri bilan taqsimlab, birgalikda ishlashni davom ettirmoqda.",
              reading="ぶんたん", expl="分担 → ぶんたん (vazifalarni bo'lib olish, taqsimlash)"),
            q("t13-v2-5", "税金を【おさめる】のは国民の義務だ。",
              ["主める", "納める", "押める", "得める"], 2,
              "Soliq to'lash har bir fuqaroning burchidir.",
              reading="おさめる", expl="納める → おさめる (to'lamoq, topshirmoq)")
          ]
        },
        {
          "id": "v3", "type": "word_formation",
          "instruction_jp": "（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Qavs ichiga qo'yish uchun eng to'g'ri so'z yasovchi qo'shimchani tanlang.",
          "questions": [
            q("t13-v3-1", "このホールは（【多】）目的に使用できる。",
              ["多", "数", "複", "高"], 1,
              "Bu zaldan ko'p maqsadli (turli maqsadlarda) foydalanish mumkin.",
              expl="多目的 → たもくてき (ko'p maqsadli)"),
            q("t13-v3-2", "ハワイ出身の私が、雪を見た（【初】）体験は日本の北海道だった。",
              ["本", "現", "初", "新"], 3,
              "Gavayilik bo'lgan mening birinchi marta qor ko'rish tajribam Yaponiyaning Xokkaydo shahrida bo'lgan edi.",
              expl="初体験 → はつたいけん (ilk tajriba, birinchi marta boshdan kechirish)"),
            q("t13-v3-3", "新しい駅ビルの完成は年度（【末】）の予定です。",
              ["次", "後", "期", "末"], 4,
              "Yangi vokzal binosining qurib bitkazilishi moliya yilining oxiriga rejalashtirilgan.",
              expl="年度末 → ねんどまつ (moliya/o'quv yili oxiri)"),
            q("t13-v3-4", "あのアイドルグループのファンの年齢（【層】）は10代が中心だ。",
              ["別", "層", "間", "代"], 2,
              "U mashhur guruh muxlislarining yosh toifasi asosan o'smirlardan iborat.",
              expl="年齢層 → ねんれいそう (yosh qatlami/toifasi)"),
            q("t13-v3-5", "天気予報によると、雨は午後から（【本】）降りになる。",
              ["本", "上", "少", "総"], 1,
              "Ob-havo ma'lumotiga ko'ra, yomg'ir tushdan keyin jala/shiddatli yog'ishga aylanadi.",
              expl="本降り → ほんぶり (chinakam yog'ingarchilik, kuchli yomg'ir)")
          ]
        },
        {
          "id": "v4", "type": "context_vocab",
          "instruction_jp": "（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gap mazmuniga mos keluvchi eng to'g'ri so'zni tanlang.",
          "questions": [
            q("t13-v4-1", "植物は根から吸い上げた水分を（【蒸発】）させるとき、周囲から熱を奪うので暑さ対策に役立つ。",
              ["排水", "削除", "消費", "蒸発"], 4,
              "O'simliklar ildizidan tortib olgan namlikni bug'lantirganda atrofdagi issiqlikni o'ziga oladi, shuning uchun issiqqa qarshi foydalidir.",
              expl="蒸発 → じょうはつ (bug'lanish)"),
            q("t13-v4-2", "使わないものを思い切って捨てたら、部屋が（【すっきり】）して気持ちがいい。",
              ["すっきり", "はっきり", "すっかり", "しっかり"], 1,
              "Keraksiz narsalarni dadillik bilan tashlab yuborganimdan so'ng xona saranjom-ozoda bo'lib, kayfiyat ko'tarildi.",
              expl="すっきり (saranjom, toza, yengil)"),
            q("t13-v4-3", "あのお金持ちの夫婦は物質的には満たされていても、精神的には（【飢えて】）いる。",
              ["割れて", "濡れて", "飢えて", "逸れて"], 3,
              "U boy er-xotin moddiy jihatdan to'q bo'lsa-da, ma'naviy (ruhiy) jihatdan och (chanqoq).",
              expl="飢える → うえる (och qolmoq, chanqoq/tashna bo'lmoq)"),
            q("t13-v4-4", "エジプトの砂漠の真ん中には（【巨大】）なピラミッドがそびえている。",
              ["強大", "多大", "膨大", "巨大"], 4,
              "Misr sahrosining o'rtasida bahaybat (ulkan) piramida qad ko'tarib turibdi.",
              expl="巨大 → きょだい (ulkan, bahaybat)"),
            q("t13-v4-5", "彼はフランスでは人気があるが、日本ではまだ（【マイナー】）な歌手だ。",
              ["ハングリー", "ポピュラー", "マイナー", "フリー"], 3,
              "U Fransiyada mashhur bo'lsa-da, Yaponiyada hali uncha tanilmagan (kam taniqli) xonanda.",
              expl="マイナー (minor / kam tanilgan, kichik doiradagi)"),
            q("t13-v4-6", "大学や短大の教育（【課程】）に職業指導が義務化される。",
              ["課程", "練習", "過程", "活動"], 1,
              "Universitet va kollejlarning o'quv dasturiga (kurikulumiga) kasbiy yo'naltirish kiritilishi majburiy etib belgilanadi.",
              expl="課程 → かてい (o'quv kursi, ta'lim dasturi)"),
            q("t13-v4-7", "地震のとき大切なのは「生き残る」ことで、（【脱出】）経路が断たれなければあとのことはなんとかなる。",
              ["中断", "脱出", "出口", "出場"], 2,
              "Zilzila paytida eng muhimi 'omon qolish'dir, qochib chiqish yo'li to'silmasa, qolganini eplasa bo'ladi.",
              expl="脱出 → だっしゅつ (chiqib ketish, qutulish)")
          ]
        },
        {
          "id": "v5", "type": "paraphrase",
          "instruction_jp": "＿＿の言葉に意味が最も近いものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Tagiga chizilgan so'zga ma'nosi eng yaqin so'zni tanlang.",
          "questions": [
            q("t13-v5-1", "あの選手はもう【盛り】を過ぎた。",
              ["リミット", "ゴール", "ピーク", "チェックポイント"], 3,
              "U sportchi allaqachon o'zining eng cho'qqi davridan (ravnaq davridan) o'tib ketgan.",
              expl="盛り（さかり）＝ ピーク (eng avjiga chiqqan cho'qqi davri)"),
            q("t13-v5-2", "就職の際の学歴の【有効性】はまだいくぶんある。",
              ["効力", "意味", "評価", "損得"], 1,
              "Ishga kirishda diplomning samadorligi/kuchi (ta'siri) hali ham birmuncha bor.",
              expl="有効性（ゆうこうせい）＝ 効力（こうりょく） (kuch, ta'sir, yaroqlilik)"),
            q("t13-v5-3", "小学生の学力テストが全国で【いっせいに】行われた。",
              ["別々に", "続々と", "同時に", "突然に"], 3,
              "Boshlang'ich sinf o'quvchilarining bilim sinovi butun mamlakat bo'ylab bir vaqtda (birdaniga) o'tkazildi.",
              expl="いっせいに ＝ 同時に (bir paytda, birdaniga)"),
            q("t13-v5-4", "母親は息子の気持ちを【察している】。",
              ["予測して", "見抜いて", "受け取って", "尊重して"], 2,
              "Ona o'g'lining ko'nglini (hissiyotlarini) sezib/anglab turibdi.",
              expl="察する（さっする）＝ 見抜く（みぬく） (payqamoq, sezib tushunmoq)"),
            q("t13-v5-5", "会社の重要な情報を【リークする】。",
              ["口外する", "利用する", "制限する", "混乱させる"], 1,
              "Kompaniyaning muhim ma'lumotlarini tashqariga sizdirish (oshkor qilish).",
              expl="リークする ＝ 口外する (og'izdan chiqarmoq, sirni oshkor qilmoq)")
          ]
        },
        {
          "id": "v6", "type": "usage",
          "instruction_jp": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Berilgan so'z qaysi gapda eng to'g'ri ma'noda ishlatilganini tanlang.",
          "questions": [
            q("t13-v6-1", "【測定】",
              [
                "今、事故の原因を測定しているところです。",
                "この程度のトラブルは前もって測定していた。",
                "学者はこの地域に大地震が起こると測定した。",
                "子どもの運動能力を測定するためにテストを行う。"
              ], 4,
              "Bolalarning jismoniy qobiliyatini o'lchash uchun test o'tkaziladi.",
              expl="測定（そくてい）— asbob yoki standart mezon asosida o'lchash, aniqlash. 4-gap to'g'ri.",
              optsTr=[
                "Hozir falokat sababini o'lchashmoqda (xato, 調査/究明 ishlatiladi).",
                "Bu darajadagi muammoni oldindan o'lchagandim (xato, 想定 ishlatiladi).",
                "Olimlar bu hududda katta zilzila bo'lishini o'lchashdi (xato, 予測 ishlatiladi).",
                "Bolalarning jismoniy qobiliyatini o'lchash (aniqlash) uchun test o'tkaziladi."
              ]),
            q("t13-v6-2", "【筋】",
              [
                "彼女のすぐれた音感は生まれつきの筋である。",
                "あいつの言うことはめちゃくちゃで、筋が通っていない。",
                "上司とはことごとく筋が合わない。",
                "あんなことをする彼の筋は理解できない。"
              ], 2,
              "Uning gapi pala-partish bo'lib, mantiqqa to'g'ri kelmaydi (mantiqsiz).",
              expl="筋が通る（すじがとおる）— mantiqan to'g'ri, izchil bo'lmoq. 2-gap to'g'ri.",
              optsTr=[
                "Uning ajoyib musiqiy sezgisi tug'ma qobiliyatdir (xato, 才能/素質 ishlatiladi).",
                "Uning aytayotgan gapi chalkash bo'lib, hech qanday mantiqqa to'g'ri kelmaydi.",
                "Boshliq bilan butunlay mantiq mos kelmaydi (xato, 意見/気が合わない ishlatiladi).",
                "Bunday qilgan uning mantiqini tushunib bo'lmaydi (xato, 意図/理由 ishlatiladi)."
              ]),
            q("t13-v6-3", "【ひきょう】",
              [
                "彼なら途中で逃げ出すようなひきょうなことは絶対にしないはずだ。",
                "こんなひきょうなテレビ番組は子どもに見せたくない。",
                "若い女性が電車の中で化粧するなんてひきょうだ。",
                "酔っぱらったひきょうな姿を彼女に見られてしまって恥ずかしい。"
              ], 1,
              "U bo'lsa yarmida qochib ketadigan nomardlikni (pastkashlikni) aslo qilmaydi.",
              expl="ひきょう（卑怯）— nomard, pastkash, qo'rqoq. 1-gap to'g'ri.",
              optsTr=[
                "U yarmida qochib ketadigan nomardlikni aslo qilmaydi.",
                "Bunday nomard teleko'rsatuvni bolalarga ko'rsatgim kelmaydi (xato, くだらない ishlatiladi).",
                "Yosh ayol poyezdda bo'yanishi nomardlikdir (xato, マナー違反 ishlatiladi).",
                "Mast holatdagi nomard qiyofamni sevgilim ko'rib qolib uyaldim (xato, みっともない ishlatiladi)."
              ]),
            q("t13-v6-4", "【見解】",
              [
                "この件に関して、いい見解があったらぜひ教えてください。",
                "その考えには不満の見解が、あちこちであがった。",
                "今後、いっそうの努力をする見解でありますので、よろしくお願いします。",
                "この問題には、老人と若者の間に大きな見解の差がある。"
              ], 4,
              "Bu masalada keksalar va yoshlar qarashlari o'rtasida katta farq bor.",
              expl="見解（けんかい）— rasmiy yoki falsafiy nuqtai nazar, qarash. 4-gap to'g'ri.",
              optsTr=[
                "Bu masala bo'yicha yaxshi fikringiz bo'lsa ayting (xato, アイデア/意見 ishlatiladi).",
                "U fikrga nisbatan norozilik fikrlari ko'tarildi (xato, 不満の声 ishlatiladi).",
                "Bundan buyon yanada harakat qilish fikridamiz (xato, 所存/考え ishlatiladi).",
                "Bu masalada keksalar va yoshlar o'rtasida qarashlar/fikrlar borasida katta farq bor."
              ]),
            q("t13-v6-5", "【清書】",
              [
                "政治は今年度の清書を発表した。",
                "連絡先の電話番号を紙切れにさっと清書して彼女に渡した。",
                "作文の間違いを調べて、清書して出した。",
                "受付でご自分のお名前とご住所を清書してください。"
              ], 3,
              "Inshodagi xatolarni tekshirib, oqqa ko'chirib (toza yozib) topshirdim.",
              expl="清書（せいしょ）— qoralamani xatosiz, chiroyli qilib oqqa ko'chirish. 3-gap to'g'ri.",
              optsTr=[
                "Hukumat bu yilgi toza yozuvni e'lon qildi (xato, 白書/方針 ishlatiladi).",
                "Telefon raqamni qog'ozga tezda toza yozib unga berdim (xato, メモして ishlatiladi).",
                "Inshodagi xatolarni tekshirib, xatosiz oqqa ko'chirib topshirdim.",
                "Qabulxonada ismingiz va manzilingizni toza yozing (xato, 記入して ishlatiladi)."
              ])
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
          "id": "g1", "type": "grammar_sent_form",
          "instruction_jp": "次の文の（ ）に入れるのに最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi qavs ichiga qo'yish uchun eng to'g'ri grammatik shaklni tanlang.",
          "questions": [
            q("t13-g1-1", "消防士の新人隊員の訓練は、半年に（【渡って】）きびしく行われる。",
              ["かかって", "渡って", "続いて", "過ぎて"], 2,
              "Yangi o't o'chiruvchilarning mashg'ulotlari yarim yil davomida qat'iy o'tkaziladi.",
              expl="〜にわたって（渡って）— butun muddat yoki masofa davomida qamrab olish."),
            q("t13-g1-2", "犯人（【に関する】）情報をご存知の方は、お近くの警察にお知らせください。",
              ["に及ぶ", "に伴う", "に沿う", "に関する"], 4,
              "Jinoyatchiga oid (tegishli) ma'lumotni biladiganlar yaqin oradagi politsiya bo'limiga xabar bering.",
              expl="〜に関する（関する）— ...ga oid, ...haqida."),
            q("t13-g1-3", "赤ちゃんは今（【泣いていたか】）と思ったら、もうにこにこ笑っている。",
              ["泣いていたか", "泣こうか", "泣かないか", "泣くまいか"], 1,
              "Go'dak hozirgina yig'layotganmidi desam, allaqachon jilmayib kulib o'tiribdi.",
              expl="〜かと思ったら — ...qilgan edi hamki, darhol keyingi harakat sodir bo'ldi."),
            q("t13-g1-4", "あのレストランはさんざん待たせた（【あげく】）、出てきたのはメニューと違うものだった。",
              ["せいか", "ところ", "あげく", "どころか"], 3,
              "U restoran shuncha uzoq kuttirganining oqibatida, olib kelgan taomi menyudagidan boshqa narsa bo'lib chiqdi.",
              expl="〜あげく（に）— ko'p urinish/kutish oqibatida salbiy natija yuz berishi."),
            q("t13-g1-5", "日本人（【にしたら】）あたりまえの習慣が、他の国から見ておかしいことはたくさんある。",
              ["にしても", "にしたら", "においても", "において"], 2,
              "Yaponlar nuqtai nazaridan tabiiy tuyulgan odatlar boshqa mamlakatlar uchun g'alati bo'lgan holatlar ko'p.",
              expl="〜にしたら（にすれば）— ...ning nuqtai nazaridan qaraganda."),
            q("t13-g1-6", "コンピューターでの作業に（【伴う】）疲れには、休むよりむしろ運動したほうがよい。",
              ["基づく", "及ぼす", "伴う", "通じる"], 3,
              "Kompyuterda ishlash tufayli yuzaga keladigan charchoqqa dam olishdan ko'ra sport bilan shug'ullanish yaxshiroq.",
              expl="〜に伴う（ともなう）— ...bilan birga keladigan, hamrohlik qiladigan."),
            q("t13-g1-7", "平凡なサラリーマンに（【過ぎない】）私が、そんな大きな家を買えるわけがない。",
              ["変わらない", "ならない", "およばない", "過ぎない"], 4,
              "Oddiygina xizmatchi bo'lgan men shunday katta uyni sotib ola olmasligim aniq.",
              expl="〜にすぎない（過ぎない）— shunchaki ...dan boshqa narsa emas."),
            q("t13-g1-8", "ランナーは4時間かけて42.195キロを走り（【ぬいた】）。",
              ["かけた", "ぬいた", "通った", "去った"], 2,
              "Yuguruvchi 4 soat sarflab, 42.195 km masofani oxirigacha yugurib o'tdi.",
              expl="動詞マス形＋ぬく（抜く）— qiyinchiliklarga qaramay oxirigacha yetkazmoq."),
            q("t13-g1-9", "大変申し訳ございませんが、至急書類を（【送っていただけないでしょうか】）。明日の会議に必要なんです。",
              ["送っていただけたでしょうか", "送っていただけないでしょうか", "送ればよろしいでしょうか", "送ってよろしいでしょうか"], 2,
              "Ming bor uzr, zudlik bilan hujjatlarni yuborib bera olmaysizmi? Ertangi yig'ilish uchun kerak edi.",
              expl="〜ていただけないでしょうか — muloyim iltimos qilish shakli."),
            q("t13-g1-10", "この駅においてある傘は自由に借りて（【よいことになっている】）が、ちゃんと返してください。",
              ["よいことになっている", "よいはずはない", "よいことにもなっている", "よくないはずはない"], 1,
              "Ushbu bekatga qo'yilgan soyabonlarni erkin olib turish mumkin qilib belgilangan, ammo albatta qaytarib bering.",
              expl="〜てよいことになっている — qoida yoki tartib bo'yicha ruxsat etilgan."),
            q("t13-g1-11", "台風が近づいているこんなときに、海に（【出るべきではない】）。",
              ["出るよりほかない", "出ないべきだ", "出るべきではない", "出ないわけにいかない"], 3,
              "To'fon yaqinlashayotgan bunday paytda dengizga chiqmaslik kerak.",
              expl="〜べきではない — albatta ...qilmaslik kerak (qoidaga binoan)."),
            q("t13-g1-12", "写真では知っていたが、本物の富士山は（【見れば見るほど】）美しい山だ。",
              ["見たら見るほど", "見てもあると", "見れば見るほど", "見ようと見まいと"], 3,
              "Suratlar orqali bilar edim, ammo haqiqiy Fuji tog'i qaraganing sari go'zallashadigan tog'dir.",
              expl="〜ば〜ほど — ...qilganing sari, ...qilgan sari yanada.")
          ]
        },
        {
          "id": "g2", "type": "grammar_sentence_order",
          "instruction_jp": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Gapdagi yulduzcha (★) o'rniga keluvchi to'g'ri so'zni tanlang.",
          "questions": [
            q("t13-g2-1", None,
              ["大人に", "本の中には", "とって", "向けの"], 2,
              "Bolalar uchun mo'ljallangan kitoblar ichida kattalar uchun ham qiziqarli bo'lganlari juda ko'p.",
              prefix="子ども", suffix="おもしろいものもたくさんある。", starPos=2, order=[4, 2, 1, 3],
              expl="子ども【向けの】【★本の中には】【大人に】【とって】おもしろいものもたくさんある。"),
            q("t13-g2-2", None,
              ["値段も", "味も", "よい", "安ければ"], 4,
              "U restoran narxi ham arzon bo'lishi bilan birga taomi ham mazali, ammo doim odam ko'pligi noqulay.",
              prefix="あのレストランは", suffix="が、いつも込んでいるのが困る。", starPos=2, order=[1, 4, 2, 3],
              expl="あのレストランは【値段も】【★安ければ】【味も】【よい】が、いつも込んでいるのが困る。"),
            q("t13-g2-3", None,
              ["新しい", "新社長", "として", "体制"], 3,
              "Sobiq prezidentning o'g'lini yangi rahbar etib tayinlab, yangi tuzilmani boshlashmoqda.",
              prefix="前の社長の息子を", suffix="をスタートさせる。", starPos=2, order=[2, 3, 1, 4],
              expl="前の社長の息子を【新社長】【★として】【新しい】【体制】をスタートさせる。"),
            q("t13-g2-4", None,
              ["日本料理", "は", "ぬきにしては", "語れない"], 1,
              "Soya sousisiz yapon taomlarini tasavvur qilib bo'lmaydi.",
              prefix="しょうゆを", suffix="。", starPos=2, order=[3, 1, 2, 4],
              expl="しょうゆを【ぬきにしては】【★日本料理】【は】【語れない】。"),
            q("t13-g2-5", None,
              ["わかって", "笑う", "泣くやら", "やらで"], 2,
              "Qizining omon-esonligini bilib, yig'lash va kulish aralash oila to'polon bo'lib ketdi.",
              prefix="娘が無事と", suffix="家族は大騒ぎだった。", starPos=3, order=[1, 3, 2, 4],
              expl="娘が無事と【わかって】【泣くやら】【★笑う】【やらで】家族は大騒ぎだった。")
          ]
        },
        {
          "id": "g3", "type": "grammar_passage_context",
          "instruction_jp": "次の文章を読んで、文章全体の趣旨を踏まえて、50から54の中に入る最もよいものを、1・2・3・4から一つ選びなさい。",
          "instruction_uz": "Matnni o'qib, 50-54 bo'sh o'rinlar uchun kontekstga mos eng to'g'ri javobni tanlang.",
          "passage": "人間が考えるときは、右脳と左脳が同時に働いています。左脳は言葉や論理を、右脳は形、音などの感覚を受け持っています。[ 50 ]、考える力を高めるには、その両方をきたえる必要があります。\n歩いていると脳の働きが活発になり、いろいろな考えがわいてきます。このことは昔から経験的に知られていました。\n古代ギリシャの大哲学者プラトンは、弟子たちに[ 51 ]といわれます。18世紀ドイツの哲学者カントも、散歩する哲学者として知られています。彼が散歩に出るのはきっちり3時半で、夕方の6時に散歩を終えました。近所の人たちは、まったく変わらないカントの生活を見て時計代わりに使ったといいます。\n企業におけるアイデア生産は、ほとんど室内で行われています。狭い室内に閉じこもって、言葉で「あでもない、こうでもない」とやり合っているわけです。言葉によるアイデア生産を行っていると、論理的な左脳は活発になりますが、右脳は[ 52 ]。その結果、せっかく浮かんだアイデアも「現実的でない」と[ 53 ]ことが多くなります。\n一方、歩きながらアイデア生産を行ったら、どうなるでしょうか。\n歩くのは両手両足を動かす運動ですから、左脳にも右脳にも新鮮な血液が送られ、両方ともリフレッシュされます。歩くことに集中し始めると[ 54-a ]の考えが弱くなり、感覚的な[ 54-b ]が働きやすい状態になってきます。その結果、新鮮なアイデアが浮かびやすくなるわけです。会議を始める前に、みんなで歩いてみるのはどうでしょう。",
          "questions": [
            q("t13-g3-1", "［ 50 ］に入る最もよいものを選びなさい。",
              ["したがって", "とはいえ", "あるいは", "しかも"], 1,
              "［ 50 ］bo'sh o'rniga mos bog'lovchini tanlang.",
              blankNo=50, expl="Xulosa chiqarish uchun 「したがって (shuning uchun)」 mos keladi."),
            q("t13-g3-2", "［ 51 ］に入る最もよいものを選びなさい。",
              ["歩きながら講義した", "歩いたまま講義した", "歩く際に講義した", "歩くついでに講義した"], 1,
              "［ 51 ］bo'sh o'rniga mos iborani tanlang.",
              blankNo=51, expl="Yurib turgan holda ma'ruza qilganini ifodalash uchun 「歩きながら講義した」 to'g'ri."),
            q("t13-g3-3", "［ 52 ］に入る最もよいものを選びなさい。",
              ["活発になります", "生き生きとします", "休みがちになります", "休みそうになります"], 3,
              "［ 52 ］bo'sh o'rniga mos ifodani tanlang.",
              blankNo=52, expl="Faol bo'lmay dam olishga moyillikni ifodalash uchun 「休みがちになります」 to'g'ri."),
            q("t13-g3-4", "［ 53 ］に入る最もよいものを選びなさい。",
              ["賛成される", "肯定される", "反省される", "否定される"], 4,
              "［ 53 ］bo'sh o'rniga mos fe'lni tanlang.",
              blankNo=53, expl="G'oyalar inkor etilishi haqida borgani uchun 「否定される」 to'g'ri."),
            q("t13-g3-5", "［ 54-a ］ / ［ 54-b ］に入る組み合わせとして最もよいものを選びなさい。",
              ["a 左脳 / b 左脳", "a 右脳 / b 右脳", "a 左脳 / b 右脳", "a 右脳 / b 左脳"], 3,
              "［ 54-a ］va［ 54-b ］uchun to'g'ri juftlikni tanlang.",
              blankNo=54, expl="Mantiqiy chap miya fikri susayib, sezgir o'ng miya faollashadi: 「a 左脳 / b 右脳」.")
          ]
        }
      ]
    }
  ]
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK! test13.json yaratildi: 6 vocab + 3 grammar bo'limlari.")
