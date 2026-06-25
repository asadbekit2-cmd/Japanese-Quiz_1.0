# -*- coding: utf-8 -*-
import json
fp = r"D:/TEST JDU/jlpt-n3-game/data/test01.json"
d = json.load(open(fp, encoding="utf-8"))

TR = {
 "t1-v1-1":"Olmalar quti ichida terilib turibdi.",
 "t1-v1-2":"U odam eson-omon ekan, rostdan ham xotirjam bo'ldim.",
 "t1-v1-3":"Ikki hodisa bir vaqtda yuz berdi.",
 "t1-v1-4":"U mening - otamga o'xshaydi.",
 "t1-v1-5":"Do'stimdan konsert chiptasini oldim.",
 "t1-v1-6":"Uning fe'l-atvori samimiy (soddadil).",
 "t1-v1-7":"Bu yerga stolni olib keling.",
 "t1-v1-8":"Bu do'kon yil bo'yi dam olmasdan ishlaydi.",
 "t1-v2-9":"U baxtli hayot kechirardi.",
 "t1-v2-10":"Hayotni yaxshilash.",
 "t1-v2-11":"Katta daryo bo'ylab yuradi.",
 "t1-v2-12":"Uy sotib olmoqchi bo'lganlarga pul qarz beradi.",
 "t1-v2-13":"Shuni imkoniyat qilib, chekishni tashlamoqchiman.",
 "t1-v2-14":"Narsalar haqida chuqur o'ylash muhim.",
 "t1-v3-15":"Yangi ish uchun hammamiz birga ( ) o'rtaga tashladik.",
 "t1-v3-16":"Kuchli yomg'ir tufayli musobaqaning ( ) belgilandi.",
 "t1-v3-17":"Katta uyni ( ) qilish juda mashaqqatli.",
 "t1-v3-18":"Baliqni ( ), taom tayyorladim.",
 "t1-v3-19":"Bugun uyda bo'lmayman, shuning uchun aloqani ertaga ( ) qiling.",
 "t1-v3-20":"Kasallik tez tuzalishini ( )man.",
 "t1-v3-21":"Ota-ona va bola o'rtasida ( ) o'rnatish muhim.",
 "t1-v3-22":"Gazetaning ( )ni o'qib, hayron bo'ldim.",
 "t1-v3-23":"( ) qilmasdan, ko'proq tanovul qiling.",
 "t1-v3-24":"Jon-jahdim bilan ishlayotgan edim, ( ) tush bo'lib qoldi.",
 "t1-v3-25":"Katta ( )ga uchragan bo'lsam-da, amallab omon qoldim.",
 "t1-v4-26":"U doim ayollarga yumshoq (kechirimli) munosabatda bo'ladi.",
 "t1-v4-27":"Ko'p mashq qildim, shuning uchun tomog'im qup-quruq.",
 "t1-v4-28":"Bu lug'at ancha qulay.",
 "t1-v4-29":"Rejani birinchi bo'lib aytgan — Inoue.",
 "t1-v4-30":"Ortiqcha gaplarni gapirmang.",
 "t1-g1-1":"Qora bulutlar chiqqan, ( ) yomg'ir yog'adiganga o'xshaydi.",
 "t1-g1-2":"Go'shtni yoqtirmasangiz, baliq ( ) qanday bo'ladi?",
 "t1-g1-3":"Men Hayashi-san bilan ( ) uchrashganimda, uni ajoyib inson deb o'ylayman.",
 "t1-g1-4":"Tushlik yegan ( ), mazali qahva ichdim.",
 "t1-g1-5":"Isrofgarchilik qilib, oyligimni endigina ( ) bo'lsam-da, allaqachon pulim yo'q.",
 "t1-g1-6":"Hech qanday do'stim yo'q joyga ( ) yoqmaydi.",
 "t1-g1-7":"O'g'lim o'qimaydi, shuning uchun test ballari ( ) (pasayaveradi).",
 "t1-g1-8":"Boshqalardan qarz olgan pulni albatta ( ) kerak deb o'ylayman.",
 "t1-g1-9":"Bu ishni tugatgan ( ), keyingi ishni boshlaylik.",
 "t1-g1-10":"Mijoz: «Bu qayerning kiyimi?» Sotuvchi: «Bu kiyim Fransiyaniki ( ).»",
 "t1-g1-11":"Tanaka-san yoshligida Amerikada yashagan deb ( ), bu rostmi?",
 "t1-g1-12":"Atayin uzoqqacha ( ), lekin u qiz bilan ko'risha olmadim.",
 "t1-g1-13":"Mast holda mashina haydab avariya qildim, bundan keyin hech qachon ( ) deb qasam ichdim.",
 "t1-g2-14":"To'g'ri tartib: «Uchrashuvni tushdan keyinga belgilab bera olmaysizmi?»",
 "t1-g2-15":"To'g'ri tartib: «Katta derazani ochsam, yarqirab turgan dengiz yoyilib yotardi.»",
 "t1-g2-16":"To'g'ri tartib: «Bu ishni zimmangizga olsangiz, juda katta yordam bo'ladi.»",
 "t1-g2-17":"To'g'ri tartib: «...ovqatni yeb bo'lar-bo'lmas...» (idiom: endigina tugatishi bilan).",
 "t1-g2-18":"To'g'ri tartib: «Hayotimdagi shu paytgacha bo'lgan eng zo'r kun deganim...»",
 "t1-g3-19":"( ) do'konning daftar bo'limida...",
 "t1-g3-20":"( ), daftar deganda qora muqovali oddiy daftarlar ko'p edi...",
 "t1-g3-21":"...yosh ayollarga mo'ljallangan mahsulotlar ( ).",
 "t1-g3-22":"( a ) ... ( b ) ... (yosh ayollar yoqtiradigan narsalar muhayyo).",
 "t1-g3-23":"...mahsulotlar juda ko'p bo'lib, ( ).",
}

OPTS_TR = {
 "t1-v5-31":[
   "Shoshayotgandim, shuning uchun stol va stulni ag'darib yubordim.",
   "Ismimni chaqirishdi, shuning uchun orqaga qaytib qaradim.",
   "U bilan ajrashganimdan keyin, u haqida ko'p marta takrorladim.",
   "Mashq uchun o'qituvchi aytgan narsalarni ko'p marta takrorladim."],
 "t1-v5-32":[
   "Yangi o't-o'simliklar yerdan o'sib chiqdi.",
   "Soatlab o'ylagandan keyin yangi g'oya o'sib chiqdi.",
   "Uyim yonida yangi uy o'sib chiqdi.",
   "Haddan tashqari ishlaganim uchun kasallik o'sib chiqdi."],
 "t1-v5-33":[
   "Bizning davlat boshqa davlatlar bilan trenirovka qilmoqda.",
   "Kelasi yili o'sha qiyin imtihonga trenirovka qilmoqchiman.",
   "Ertalab va kechqurun, salomatlik uchun albatta mashq qilaman.",
   "Bu mashinaning nafaqat dizayni, balki trenirovkasi ham juda yaxshi."],
 "t1-v5-34":[
   "U odamda ajoyib harakat (qobiliyat) bor.",
   "Harakat qilib, orzu qilgan universitetimga kira oldim.",
   "Kasalxonaga yotib, harakatni tikladim.",
   "Albatta harakati yaxshi xodim kerak."],
 "t1-v5-35":[
   "Uy hayvonlarim — it va mushuk menga juda sog'inchli.",
   "Yaponiyaga kelganimga necha yil bo'lsa ham, baribir vatandagi oilam sog'iniladi.",
   "Do'stim kam, shuning uchun do'sti ko'p odam menga sog'inchli.",
   "Hammaning oldida xato qilib, juda sog'inchli bo'ldim."],
}

PASSAGE_TR = ("Kompyuter va mobil telefonlar keng qo'llanila boshlaganidan beri, o'z rejalarini boshqarish "
 "uchun ularni daftar o'rniga ishlatadiganlar ko'paygan. Shunga qaramay, qog'oz daftar ishlatmoqchi "
 "bo'lganlar ham ko'p-ku. Men ham shundayman. Bir do'konning daftar bo'limida yoz oxiridan kelasi yilgi "
 "daftarlar sotila boshlaydi. Shu paytgacha daftar deganda qora muqovali oddiy daftarlar ko'p edi, ammo "
 "do'kon xodimi aytishicha, so'nggi paytda, ayniqsa yosh ayollarga mo'ljallangan mahsulotlar ko'payayotgan "
 "emish. Ayollar uchun daftarlar ilgaridan sotilgan, lekin bu yil turlari juda ko'p ekan. Masalan, pushti "
 "kabi yorqin chiroyli ranglilar, chiroyli dizayndagilar, o'zi yoqtirgan ruchkani biriktirsa bo'ladigan "
 "turi, daftarni bog'lab turadigan tasma yoki lentasi borlari va hokazo — yosh ayollar yoqtiradigan narsalar "
 "muhayyo. Men ham ishda daftardan ko'p foydalanaman, shuning uchun bunday tanlash zavqi ko'payganidan "
 "xursandman. Ammo do'konda tanlamoqchi bo'lsam ham, mahsulot juda ko'p bo'lgani uchun tezda tanlay olmasam "
 "kerak. Qanday daftar xohlashimni o'ylab olgach, do'konga boraman deb o'ylayman.")

cnt = 0
for sec in d["sections"]:
    for pr in sec["problems"]:
        if pr["type"] == "text_grammar":
            pr["passage_tr"] = PASSAGE_TR
        for q in pr["questions"]:
            if q["id"] in TR:
                q["tr"] = TR[q["id"]]; cnt += 1
            if q["id"] in OPTS_TR:
                q["optsTr"] = OPTS_TR[q["id"]]; cnt += 1
json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("qo'shildi:", cnt, "tarjima")
