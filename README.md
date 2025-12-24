# Soft Skills Toolkit (sstk)

## 👉️[Access from here](index.md)

## What is this?
Welcome. I'm building Soft Skills Engineering, and I cover the underlying theories and concepts on [sta - DEV Community](https://dev.to/stakiran). This is where I publish **tools** that help you put soft skills into practice.

## Notes
- "Tools" here do not mean software; they refer to things like templates, checklists, and procedures
- Everything is written in Markdown, so readers can start using it immediately by copy/pasting
    - Of course, you can also integrate it with AI agents
- Supported languages are:
    - Japanese
    - English (files with `_EN` at the end of the filename)

# ====

# The topics below are for developers

## Tool development
- Creating tools
    - Write them in Markdown. The template is `_new.md`
- Translating tools
    - The original is Japanese
    - For Japanese-to-English translation, use `translator.py` (you can run it immediately as a VSCode task)
    - Translation uses the OpenAI API
- Deploying tools
    - For now, the assumption is that people will view the repository directly on GitHub
    - I'd like to consider a static site too. GitHub Pages should be sufficient

## Entrance pages
- `README` and `index.md` are special: they serve as entrance pages
- For how to update them, see `cmd_paste_to_main.md`

## How to work with Cline
- Use it when creating scripts:
    - Write the spec under `.clinerules/`, then ask Cline to "create ~~"
    - This does not follow SDD; `.clinerules/` is only input

## Repository operations
- There is only one branch: `master`
    - Because sstk is "always unfinished"
    - If the latest version has issues, just go back to an earlier commit as needed
- Issues are welcome
- Pull requests are not accepted
    - Because this sstk is my work
    - I'd like to create a separate repository at some point for a "community-built sstk" (maybe `awesome-sstk`?)

## License
[MIT](LICENSE)