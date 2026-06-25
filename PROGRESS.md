# JLPT N3 o'yin — testlarни to'ldirish (resume yo'riqnomasi)

## Maqsad
test02.json … test15.json fayllarini test01.json formatida yaratish, so'ng `build_bundle.py`.
Manba: skanлangan PDF `517823763-Chokuzen-Taisaku-N3-Moji-Goi-Bunpou.pdf` (matn qatlami YO'Q → rasмdan o'qiladi).
Interfeys o'zbekcha; har savolga: yapon matni + variantlar + `answer` + `tr` (o'zbekcha) + `explanation_uz`; usage uchun `optsTr`.

## HOLAT (2026-06-17)
- ✅ test01–test15 — HAMMASI TO'LIQ, tekshirilgan, bundle'da (15/15 jonli, jami 870 savol).
- bundle.js `?v=20260617` versiya tagi bilan yangilangan (cache muammosi hal qilindi).
- MUHIM: foydalanuvchi test06-15 SAVOLLARI + JAVOB KALITLARINI (解説 bilan) chatda yubordi (transcript JSONL'da). Rasmlardan o'qish SHART EMAS.
- Kalitlar: vocab javoblari o'z-o'zini tekshiradi. Grammatika = 解説 boxed raqam + grammatik nuqta. sentence_order: order = 解説'dagi to'liq jumla; answer = boxed (★ slot har xil — 3 deb farazlama, boxed'ni ol; starPos=order.index(answer)+1).
- Tekshiruv skripti: `python _work/verify_test.py data/testNN.json` (answer∈1..len, sentence_order'da answer==order[starPos-1], text_grammar'da passage {{n}} == blankNo).

## PIPELINE (har test uchun)
1. `python render_halves.py N`  → `_work/rNN_p01a..p10b.png` (yarim betlar, 3.5x) + `_work/rNN_kA.png`,`rNN_kB.png` (javob kaliti, 5x). Hammasi <2000px.
   - Python: `C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe` (pymupdf shu yerda). `PYTHONUTF8=1`.
2. Javob kalitini o'qi (kA=yuqori yarim, kB=pastki yarim). Ikki javob ustuni: lug'at 1-30 (chap), lug'at5+grammatika (o'ng). Agar ustun chetga tushsa, alohida tor krop rendrla.
3. Bet yarimlarини o'qib, har savolни ko'chir. **O'qish/yozuv (問題1-2) javoblari o'z-o'zini tekshiradi** (so'zning to'g'ri o'qilishi/kanjisi = javob) — kalit bilan solishtir.
4. `gen_testNN.py` yoz (gen_test03.py ni namuna qil) → `python gen_testNN.py`.
5. `python build_bundle.py` → 116+ savol.

## SXEMA eslatmalari
- Bo'limlar: vocab (kanji_reading 8, orthography 6, context 11, paraphrase 5, usage 5) + grammar (grammar_form 13, sentence_order 5, text_grammar 5) = 58 savol.
- `kanji_reading`/`orthography`/`context`/`paraphrase`/`grammar_form`: `stem` (【…】=nishon, （　）=bo'sh), `options`, `answer`(1-4), `tr`, `explanation_uz`. kanji_reading'da `reading` ham.
- `usage`: `stem`=so'z, `options`=4 gap, `optsTr`=4 tarjima.
- `sentence_order`: `prefix`,`suffix`,`options`(4 bo'lak),`order`(to'g'ri tartib, 1-asosli),`answer`(★ bo'lak),`starPos`(★ slot). MUHIM: `answer == order[starPos-1]`. Hisoblash: to'g'ri jumlani tuz → order; ★ pozitsiyasi = javob bo'lagining order'dagi o'rni.
- `text_grammar`: `passage_title`,`passage`(ichida `{{19}}`,`{{22a}}`/`{{22b}}`),`passage_tr`; savollarда `blankNo`,`options`,`answer`. a/b qo'shma savolда variant = "a-matn ／ b-matn".

## SAHIFA XARITASI
- test N savol betlari: PDF (1-asosli) `8+(N-1)*10` .. `17+(N-1)*10`  (idx = -1).
- test N javob kaliti: PDF `194+(N-1)` (idx `193+(N-1)`).

## TEKSHIRUV (har testдан keyin)
```python
# answer==order[starPos-1]; answer 1..len; passage {{n}} == blankNo lar to'plami
```
(gen_test03.py dan keyingi tekshiruv snippet'iga qara.)
