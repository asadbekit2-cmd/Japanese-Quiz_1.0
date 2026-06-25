#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test N uchun savol betlarini yarim-yarim (variantlar aniq o'qiladigan) va
javob kalitini to'g'ri ustunlarda _work/ ga chiqaradi.
Foydalanish: python render_halves.py N
Sahifa xaritasi: test N -> PDF betlari 8+(N-1)*10 .. 17+(N-1)*10 (1-based),
                 javob kaliti PDF 194+(N-1).
"""
import sys, os, pymupdf

PDF = r"D:/TEST JDU/517823763-Chokuzen-Taisaku-N3-Moji-Goi-Bunpou.pdf"
OUT = r"D:/TEST JDU/_work"
os.makedirs(OUT, exist_ok=True)

def render(n):
    doc = pymupdf.open(PDF)
    first = 8 + (n - 1) * 10              # 1-based birinchi bet
    idxs = [first - 1 + k for k in range(10)]  # 0-based, 10 bet
    keyidx = 194 + (n - 1) - 1           # 0-based javob beti (N=1 -> idx193)

    # --- savol betlari: yuqori yarim + pastki yarim (3.5x -> <2000px) ---
    m = pymupdf.Matrix(3.5, 3.5)
    def crop(p, x0, y0, x1, y1, name):
        clip = pymupdf.Rect(p.rect.width*x0, p.rect.height*y0, p.rect.width*x1, p.rect.height*y1)
        p.get_pixmap(matrix=m, clip=clip).save(os.path.join(OUT, name))
    for k, ix in enumerate(idxs, start=1):
        p = doc[ix]
        crop(p, 0.04, 0.05, 0.99, 0.55, f"r{n:02d}_p{k:02d}a.png")
        crop(p, 0.04, 0.51, 0.99, 0.97, f"r{n:02d}_p{k:02d}b.png")

    # --- javob kaliti: ikki javob ustuni (lug'at + lug'at5/grammatika) keng tasma, 5x ---
    p = doc[keyidx]; mk = pymupdf.Matrix(5, 5)
    def kcrop(x0, y0, x1, y1, name):
        clip = pymupdf.Rect(p.rect.width*x0, p.rect.height*y0, p.rect.width*x1, p.rect.height*y1)
        p.get_pixmap(matrix=mk, clip=clip).save(os.path.join(OUT, name))
    kcrop(0.0, 0.10, 0.42, 0.56, f"r{n:02d}_kA.png")   # yuqori yarim (barcha javob ustunlari)
    kcrop(0.0, 0.54, 0.42, 0.98, f"r{n:02d}_kB.png")   # pastki yarim
    print(f"Test {n}: betlar PDF {first}-{first+9}, javob PDF {keyidx+1}. _work/r{n:02d}_* tayyor (xavfsiz o'lcham).")

if __name__ == "__main__":
    render(int(sys.argv[1]))
