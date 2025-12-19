# Soft Skills Toolkit (sstk)

## Current status: Under development
- Expanding the toolkit
- Tasks:
    - 👉️ Expand the tools (at least 10+)
    - Create a tool index/list
    - ...

---

## What is this?
Welcome. I'm launching Soft Skills Engineering, and I cover the theory and concepts on [sta - DEV Community](https://dev.to/stakiran). This is where I publish **tools** that help you apply soft skills in practice.

## For users: How to use
- "Tools" here do not mean software; they refer to things like templates, checklists, and procedures
- Everything is written in Markdown, so you can use it immediately via copy-and-paste
    - Of course, you can also integrate it with AI agents
- Supported languages:
    - Japanese
    - English (files with the `_EN` suffix)

## For developers: Development
About the tools:

- Creating tools
    - Write them in Markdown. The template is `_new.md`
- Translating tools
    - The original is in Japanese
    - Use `translator.py` to translate into English. You can run it quickly as a VSCode task
    - Translation uses the OpenAI API
- Deploying tools
    - For now, the assumption is that people will browse the repository directly on GitHub
    - I'd like to consider a static site as well. GitHub Pages should be sufficient

About repository operations:

- There is only one branch: `master`
    - Because sstk is "always unfinished"
    - If the latest version has issues, please roll back to an earlier point as appropriate
- Issues are welcome
- Pull requests are not accepted
    - Because this sstk is my work
    - I'd like to create a separate repository later for a "sstk built by everyone"
        - Something like `awesome-sstk`, maybe?

## License
[MIT](LICENSE)