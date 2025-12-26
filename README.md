# Soft Skills Toolkit (sstk)

## 👉️ [GitHub](index.md)

## 👉️ [Website](https://stakiran.github.io/soft-skills-toolkit/)

## What's this?
Welcome. I'm building "Soft Skills Engineering," and I cover the theory and concepts on [sta - DEV Community](https://dev.to/stakiran). This is the place where I publish **tools** that help you practice and apply soft skills.

## Notes
- "Tools" here do not mean software; they refer to things like templates, checklists, and procedures
- Everything is written in Markdown, so readers can start using it immediately via copy-and-paste
    - Of course, you can also integrate it with AI agents
- Supported languages are as follows
    - Japanese
    - English (filenames ending with `_EN`)

# ====

# The rest of this document is for developers

## Natural language to use
- 1: **Japanese**
- 2: For English translations, I use generative AI

## Developing tools
- Creating tools
    - Write them in Markdown. The template is `_new.md`
- Translating tools
    - Use `translator.py`. You can invoke it quickly as a task in VSCode
    - It uses the OpenAI API
- Deploying tools
    - For now, the assumption is that people will view the repository directly on GitHub
    - ★I'd like to consider a static site as well. GitHub Pages should be sufficient

## Entrance pages
- `README` and `index.md` are special; they serve as "entrance" pages
- For how to update them, see `cmd_paste_to_main.md`

## Working with Cline
- I use it when creating scripts:
    - Write the specs under `.clinerules/`, then ask Cline "create ~~" to generate them
    - This is not SDD-compliant; the content under `.clinerules/` is only input material

## Repository operations
- There's only one branch: `master`
    - Because sstk is "always unfinished"
    - If the latest version has issues, just go back to an earlier point as appropriate
- Issues are welcome
- Pull requests are not accepted
    - Because sstk is my work
    - 🐰 I'd like to create a separate repository someday for a "community-built sstk"—maybe something like `awesome-sstk`?

## License
[MIT](LICENSE)