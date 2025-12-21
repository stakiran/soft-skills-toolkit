#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def main():
    # プロジェクトルートの Markdown ファイル一覧取得
    entries = [f for f in os.listdir('.') if f.lower().endswith('.md')]
    # README* と index* は除外
    files = [
        f for f in entries
        if not re.search(r'README', f, re.IGNORECASE)
        and not re.search(r'index', f, re.IGNORECASE)
    ]
    # 日本語版（xxxx.md）と英語版（xxxx_EN.md）のペア抽出
    ja_files = [f for f in files if not f.endswith('_EN.md')]
    pairs = []
    for ja in ja_files:
        base = ja[:-3]
        en = f"{base}_EN.md"
        if en in files:
            pairs.append((ja, en))
    # ファイル名昇順ソート
    pairs.sort(key=lambda x: x[0])

    # tools.md 用コンテンツ生成
    lines = []
    for ja, en in pairs:
        # タイトル抽出（先頭の "# " を除去）
        title = ''
        try:
            with open(ja, encoding='utf-8') as rf:
                for raw in rf:
                    raw = raw.strip()
                    if raw.startswith('#'):
                        title = raw.lstrip('#').strip()
                        break
        except Exception as e:
            title = ja  # 読み込み失敗時はファイル名をタイトルに

        lines.append(f"- {title}: [JA]({ja}) [EN]({en})")
        lines.append("    - T: ")
        lines.append("    - E: ")
        lines.append("    - A: ")

    # tools.md に書き出し
    with open('tools.md', 'w', encoding='utf-8') as wf:
        wf.write('\n'.join(lines))
        wf.write('\n')

    print(f"Generated tools.md with {len(pairs)} entries.")

if __name__ == '__main__':
    main()
