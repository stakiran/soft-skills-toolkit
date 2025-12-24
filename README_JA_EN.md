# Soft Skills Toolkit (sstk)

## 👉️[Access here](index.md)

## What is this?
Welcome. I'm building Soft Skills Engineering, and I cover the theory and concepts on [sta - DEV Community](https://dev.to/stakiran). This is where I publish **tools** that help you practice and apply soft skills.

## Notes
- "Tools" here do not mean software; they refer to things like templates, checklists, and procedures
- Everything is written in Markdown, so readers can copy and use it immediately
    - Of course, you can also use them together with AI agents
- Supported languages are:
    - Japanese
    - English (files ending with `_EN`)

# ====

# From here on: developer-facing topics

## Natural language used
- 1: **Japanese**
- 2: English translations are created using generative AI

## Tool development
- Creating tools
    - Write them in Markdown. The template is `_new.md`
- Translating tools
    - Use `translator.py`. You can invoke it quickly as a task in VSCode
    - It uses the OpenAI API
- Deploying tools
    - For now, the assumption is that people will view this directly on GitHub
    - ★I'd also like to consider a static site. GitHub Pages should be sufficient

## Entrance pages
- `README` and `index.md` are treated as special "entrance" pages
- For how to update them, see `cmd_paste_to_main.md`

## How to work with Cline
- Used when creating scripts:
    - Write the spec under `.clinerules/`, then ask Cline "create ~~~" to have it build it
    - This does not follow SDD; `.clinerules/` is only input

## Repository operations
- There is only one branch: `master`
    - Because sstk is "always unfinished"
    - If something is wrong in the latest version, just go back to an earlier point
- Issues are welcome
- Pull requests are not accepted
    - Because this sstk is my work
    - 🐰 I'd like to create a separate repository someday for a "sstk built by everyone"—maybe something like `awesome-sstk`?

## License
[MIT](LICENSE)