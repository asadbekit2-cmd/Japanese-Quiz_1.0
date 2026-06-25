#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Berilgan test raqami uchun savol betlari (juftlab) va javob kaliti ustunlarini rasmga chiqaradi.
Foydalanish:  python render_test.py N
Test N -> savol betlari PDF 8+(N-1)*10 .. 17+(N-1)*10 ; javob kaliti PDF 193+N
"""
import sys, os, pymupdf

PDF = r"D:/TEST JDU/517823763-Chokuzen-Taisaku-N3-Moji-Goi-Bunpou.pdf"
OUT = r"D:/TEST JDU/_work"
os.makedirs(OUT, exist_ok=True)

def render(n):
    doc = pymupdf.open(PDF)
    first = 8 + (n - 1) * 10          # 1-based printed/pdf page of 第N回
    idxs = [first - 1 + k for k in range(10)]   # 0-based indices, 10 pages
    keyidx = 193 + n - 1              # 0-based index of answer page (194 -> idx193 for N=1)

    # --- savol betlari: yakka bet, aniq o'qish uchun 3.5x ---
    m = pymupdf.Matrix(3.5, 3.5)
    for k, ix in enumerate(idxs, start=1):
        doc[ix].get_pixmap(matrix=m).save(os.path.join(OUT, f"t{n:02d}_p{k:02d}.png"))

    # --- javob kaliti ustunlari (yuqori zoom, ikki ustun, ikki yarim) ---
    p = doc[keyidx]; mk = pymupdf.Matrix(8, 8)   # baland bo'lib ketmasligi uchun 8x
    def crop(x0, y0, x1, y1, name):
        clip = pymupdf.Rect(p.rect.width * x0, p.rect.height * y0, p.rect.width * x1, p.rect.height * y1)
        p.get_pixmap(matrix=mk, clip=clip).save(os.path.join(OUT, name))
    # chap ustun (lug'at 問題1-4)
    crop(0.015, 0.13, 0.205, 0.55, f"t{n:02d}_keyL_top.png")
    crop(0.015, 0.53, 0.205, 0.95, f"t{n:02d}_keyL_bot.png")
    # o'rta ustun (lug'at 問題5 + 文法 問題1-3)
    crop(0.20, 0.13, 0.40, 0.55, f"t{n:02d}_keyM_top.png")
    crop(0.20, 0.53, 0.40, 0.95, f"t{n:02d}_keyM_bot.png")
    print(f"Test {n}: savol betlari PDF {first}-{first+9}, javob PDF {keyidx+1} -> rasmlar tayyor")

if __name__ == "__main__":
    render(int(sys.argv[1]))
