# Ma'lumotlar sxemasi (JLPT N3 o'yin)

Har bir test alohida `testNN.json` faylda. `meta.json` — 15 levelning ro'yxati.

## meta.json
```jsonc
{
  "title": "JLPT N3 — 直前対策",
  "levelsCount": 15,
  "levels": [
    { "id": 1, "file": "test01.json", "title_jp": "第1回", "title_uz": "1-bosqich", "minutes": 50 }
    // ... 15 tagacha
  ]
}
```

## testNN.json
```jsonc
{
  "id": 1,
  "title_jp": "第1回 模擬テスト",
  "title_uz": "1-test",
  "minutes": 50,
  "sections": [
    {
      "id": "vocab",            // "vocab" | "grammar"
      "name_jp": "文字・語彙",
      "name_uz": "Kanji va lug'at",
      "problems": [ /* Problem[] */ ]
    }
  ]
}
```

## Problem
```jsonc
{
  "id": "v-mondai1",
  "type": "kanji_reading",     // turlardan biri (pastda)
  "instruction_jp": "___ のことばの読み方として よいものを、1・2・3・4 から ひとつ えらびなさい。",
  "instruction_uz": "Tagiga chizilgan so'zning o'qilishi sifatida to'g'risini tanlang.",
  "passage": null,             // faqat text_grammar uchun: umumiy matn (HTML, {{NN}} = bo'sh joy)
  "questions": [ /* Question[] */ ]
}
```

## Question
```jsonc
{
  "id": "t1-v1-q1",
  "stem": "りんごが地面に【落ちて】いる。",  // 【...】 = tagiga chizilgan/nishon so'z
  "reading": "おちて",            // ixtiyoriy: nishon so'zning o'qilishi (furigana yordami / kanji_reading javobi konteksti)
  "blankNo": null,                // text_grammar uchun: passage dagi bo'sh joy raqami (masalan 19)
  "options": ["ついて", "ならんで", "つつんで", "しずんで"],
  "answer": 4,                    // 1 dan boshlab indeks (1..4)
  "explanation_jp": "..."         // ixtiyoriy: 解説 dan
}
```

## Savol turlari (type)
| type | JP | Tavsif |
|------|----|--------|
| `kanji_reading`   | 漢字読み      | Tagiga chizilgan kanji so'zning o'qilishini tanlash |
| `orthography`     | 表記          | Tagiga chizilgan kana so'z uchun to'g'ri kanji yozuvini tanlash |
| `context`         | 文脈規定      | ( ) ga eng mos so'zni tanlash |
| `paraphrase`      | 言い換え類義  | Gapga eng yaqin ma'noli variantni tanlash |
| `usage`           | 用法          | Berilgan so'z to'g'ri ishlatilgan gapni tanlash |
| `grammar_form`    | 文法形式      | ( ) ga eng mos grammatik shaklni tanlash |
| `sentence_order`  | 文の組み立て  | Gap bo'laklarini tartiblash; ★ o'rniga tushadigan variant |
| `text_grammar`    | 文章の文法    | Matndagi raqamli bo'sh joyga eng mos variant |

### Maxsus: sentence_order
`stem` da bo'sh joylar `_1_ _2_ ★ _4_` ko'rinishida (★ — javob talab qilinadigan pozitsiya).
`options` — 4 ta bo'lak. `answer` — ★ ga tushadigan bo'lak indeksi.
Foydalanuvchi to'g'ri tartibni yig'adi; ★ pozitsiyasidagi bo'lak tekshiriladi.

### Maxsus: text_grammar
`problem.passage` — to'liq matn, ichida `{{19}}`, `{{20}}` ... bo'sh joylar.
Har bir `question.blankNo` mos bo'sh joy raqami; `options`/`answer` o'sha joy uchun.
