# ツール一覧を作成するスクリプト
- markdown ファイルで書かれた sstk ツールを一覧表示する
- `python cmd_listup.py` にて実行すると、`tools.md` を生成する

## パースするファイル
- 日本語版(xxxx.md)と英語版(xxxx_EN.md)が用意されている Markdown ファイルのみパースする
- `*README*` と `*index*` はパースは行わず無視する

## パースする順番
ファイル名昇順で良い。

## sstk ツールのフォーマット
- _new.md を参照すること
- 特に一行目が `# (title)` となっている点を押さえよ

## tools.md のフォーマット
`%variable%` を埋めよ。

```markdown
- %title%: [JA](%filename%) [EN](%filename_EN%)
    - T: 
    - E: 
    - A: 
- ...
```

以下に例を示す。

```
- MAMA(Meeting As An AMA): [JA](mama_meeting_as_an_ama.md) [EN](mama_meeting_as_an_ama_EN.md)
    - T: 
    - E: 
    - A: 
- ...
```
