#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data/*.json fayllarini bitta data/bundle.js ga jamlaydi.
Shunda ilova local server'siz (file:// orqali) ham ishlaydi.
Ishga tushirish:  python build_bundle.py
"""
import json, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)

meta = load("meta.json")

tests = {}
for fp in sorted(glob.glob(os.path.join(DATA, "test*.json"))):
    try:
        t = json.load(open(fp, encoding="utf-8"))
        tests[t["id"]] = t
    except Exception as e:
        print("XATO:", fp, e)

# meta'da qaysi testlar tayyor ekanini belgilaymiz
ready = sorted(tests.keys())
for lv in meta["levels"]:
    lv["ready"] = lv["id"] in tests

out = os.path.join(DATA, "bundle.js")
with open(out, "w", encoding="utf-8") as f:
    f.write("// Avtomatik yaratilgan fayl. Tahrirlamang. (build_bundle.py)\n")
    f.write("window.JLPT_META = " + json.dumps(meta, ensure_ascii=False) + ";\n")
    f.write("window.JLPT_TESTS = " + json.dumps(tests, ensure_ascii=False) + ";\n")

total_q = sum(len(q["questions"]) for t in tests.values() for s in t["sections"] for q in s["problems"])
print(f"bundle.js yaratildi: {len(tests)} test ({ready}), jami {total_q} savol")
