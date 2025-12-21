#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  
エントランスページの英語版（_JA_EN.md）から最終成果物（.md）へ内容をコピーするスクリプト  
実行: python paste_to_main.py  
標準出力なし  
"""

import os

def main():
    # 対象となるエントランスページのベース名
    bases = ['README', 'index']
    for base in bases:
        src = f"{base}_JA_EN.md"
        dst = f"{base}.md"
        if os.path.isfile(src):
            with open(src, 'r', encoding='utf-8') as f_src:
                content = f_src.read()
            with open(dst, 'w', encoding='utf-8') as f_dst:
                f_dst.write(content)

if __name__ == '__main__':
    main()
