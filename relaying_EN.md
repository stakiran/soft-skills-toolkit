# Relay-style Communication
- A communication approach where a "baton" is passed along
- Whoever receives the baton writes their response or answer according to the content
- Procedure
    - 1: Design the baton (theme, format, and instructions) and the pass flow
    - 2: Keep the baton moving
- Benefits
    - Many people find it easy because they can simply respond when it comes to them (can be handled reactively)

# Tools
Basic baton format:

```markdown
# Context
- Theme: __
- Expected time to fill out: __ min
- Supporting materials:
    - __
    - ...

# Answer
(Specify a format if you have one)

# Pass flow
(Describe how the baton will be passed)
(Example 1: List all participants in order)
(Example 2: Describe an algorithm for selecting the next person)
```

A list for deciding how to implement relay-style communication:

```markdown
- 1: Do you have the capability and bandwidth to build something in-house?
    - If yes, you can build it yourself
- 2: Is everyone proficient with GitHub Issues or other ticketing tools?
    - If yes, you can operate with 1 baton = 1 ticket
    - To pass the baton to the next person, @mention them
- 3: Is everyone proficient with Slack or Teams?
    - If yes, you can operate with 1 baton = 1 thread
    - To pass the baton to the next person, @mention them
```

A checklist to assess tool "proficiency" required for relay-style communication:

```
- 1: Can perform basic operations such as posting, commenting, and reacting
- 2: Understands units such as repositories, threads, and channels
- 3: Can use mentions and understands how they behave
- 4: Can manage notifications on their own, e.g., effectively use mute or watch

If even one item is "No", that person is not proficient.
Training is required before relying on relay-style communication.
```

A trigger list you can use when naming a tool or mechanism for relay-style communication:

```markdown
- Relay
- Relaying
- Baton
- -ware
- Relayware
- Batonware
```