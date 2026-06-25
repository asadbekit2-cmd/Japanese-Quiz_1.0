# -*- coding: utf-8 -*-
import json, re, sys
fp = sys.argv[1] if len(sys.argv) > 1 else "data/test04.json"
t = json.load(open(fp, encoding="utf-8"))
errs = []
ok = 0
ids = set()
for s in t["sections"]:
    for p in s["problems"]:
        for q in p["questions"]:
            ok += 1
            qid = q["id"]
            if qid in ids:
                errs.append(qid + ": dublikat id")
            ids.add(qid)
            n = len(q["options"])
            if not (1 <= q["answer"] <= n):
                errs.append(qid + ": answer " + str(q["answer"]) + " out of range 1.." + str(n))
            if p["type"] == "sentence_order":
                o = q.get("order"); sp = q.get("starPos")
                if not o or sp is None:
                    errs.append(qid + ": order/starPos missing")
                else:
                    if sorted(o) != [1, 2, 3, 4]:
                        errs.append(qid + ": order " + str(o) + " not a 1..4 permutation")
                    if o[sp - 1] != q["answer"]:
                        errs.append(qid + ": answer " + str(q["answer"]) + " != order[starPos-1] " + str(o[sp - 1]))
            if p["type"] == "text_grammar":
                blanks = set(re.findall(r"\{\{(\d+)[ab]?\}\}", p["passage"]))
                qb = set(str(x["blankNo"]) for x in p["questions"])
                if blanks != qb:
                    errs.append(p["id"] + ": passage blanks " + str(sorted(blanks)) + " != blankNo " + str(sorted(qb)))
counts = {}
for s in t["sections"]:
    for p in s["problems"]:
        counts[p["type"]] = counts.get(p["type"], 0) + len(p["questions"])
print("Fayl:", fp)
print("Jami savol:", ok)
print("Turlar:", counts)
print("Unik id:", len(ids))
print("XATOLAR:", errs if errs else "YO'Q (OK)")
