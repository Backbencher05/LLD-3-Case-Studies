
---

# 🎯 Step 1 — Scope Clarification (Interview Thinking)

> After understanding the problem, I'd like to clarify the scope so that we design the correct system.

For this discussion, I'll assume we're designing the **core Tic-Tac-Toe Game Engine**, not the complete application.

My assumptions are:

* The game logic will be independent of the user interface.
* The first version will use an in-memory implementation.
* We'll use a CLI only to drive the game during development.
* The engine should be reusable by future clients such as a REST API, desktop application, or mobile application.
* We'll initially support Human and Bot players through a common abstraction.

For Version 1, I'll intentionally keep the following out of scope:

* Online multiplayer
* Database persistence
* Authentication
* Leaderboards
* Tournament mode

> With the scope finalized, I'd proceed to gathering the functional and non-functional requirements.

---

# 🧠 Interview Tips

Notice something interesting.

The interviewer never asked:

> "Tell me your scope."

You voluntarily brought it up.

This shows that you have a structured design process.

Interviewers love candidates who drive the discussion instead of waiting to be led.

---
