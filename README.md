# Soft Skills Toolkit (sstk)

## Current status: Under development
- Expanding the set of tools
- Tasks:
    - 👉️Expand the tools (at least 10)
    - 👉️Create a tools list -> [index](index.md)
    - ...

---

## What is this?
Welcome. I'm building Soft Skills Engineering, and I cover the theory and concepts on [sta - DEV Community](https://dev.to/stakiran). This is where I publish **tools** that help you practice and apply soft skills.

## For users: How to use

### 👉️[Start here](index.md)

### Notes
- "Tools" here are not software; they refer to things like templates, checklists, and procedures
- They're written in Markdown, so you can use them immediately by copy/paste
    - Of course, you can also integrate them with AI agents
- Supported languages:
    - Japanese
    - English (filenames ending with `_EN`)

## For developers: Development
About the tools:

- Creating tools
    - Write them in Markdown. The template is `_new.md`
- Translating tools
    - The original is in Japanese
    - Use `translator.py` to translate into English. You can run it immediately as a task in VSCode
    - Translation uses the OpenAI API
- Deploying tools
    - For now, the assumption is that people will view them directly on GitHub
    - I'd like to consider a static site as well. GitHub Pages should be sufficient

About the entrance pages:

- `README` and `index.md` are treated as special (entrance) pages
- For how to update them, see `cmd_paste_to_main.md`

About Cline:

- Used when creating scripts:
    - Write the spec under `.clinerules/` and ask Cline "Build ~~" to generate it
    - This does not follow SDD; the contents under `.clinerules/` are just inputs

About repository operations:

- There is only one branch: `master`
    - Because sstk is "always incomplete"
    - If the latest state has issues, please roll back as you see fit
- Issues are welcome
- Pull requests are not accepted
    - Because this sstk is my work
    - I'd like to create a separate repository later for a "community-built sstk"
        - Something like `awesome-sstk`?

## License
[MIT](LICENSE)