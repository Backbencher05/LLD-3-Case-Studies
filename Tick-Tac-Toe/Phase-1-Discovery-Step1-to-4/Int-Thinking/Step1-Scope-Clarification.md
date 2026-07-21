
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



-----------------------------------------------------------------------------------------------------------------------

I love this idea.

In fact, I think we've accidentally discovered something much bigger than a Tic-Tac-Toe case study.

We're actually creating an **LLD Engineering Playbook**.

And if we're going to do it, we should do it consistently.

After thinking about all five completed steps, I would standardize **every step** using the same template:

1. **Final Discovery Document**
2. **Interview Thinking**
3. **Interview Cheat Sheet**
4. **Reusable Framework**

Let's complete **Step 1** and **Step 0** in the same style.

---

# 🎯 Step 1 — Scope Clarification (Interview Cheat Sheet)

## 📋 Final Scope Discovery Summary

After understanding the problem statement, we defined the boundaries of what we are designing.

| Scope Question         | Decision                                | Why?                                                                   |
| ---------------------- | --------------------------------------- | ---------------------------------------------------------------------- |
| What are we designing? | Entity System (Domain Model)            | The focus is on modeling the business, not distributed infrastructure. |
| User Interaction       | CLI                                     | Keeps the interview focused on domain design rather than UI.           |
| Data Storage           | In-Memory                               | Persistence is not required for this version.                          |
| Actors                 | Human Player, Bot                       | Covers the core gameplay while keeping scope manageable.               |
| Board Size             | Configurable (N × N)                    | Makes the design extensible beyond 3 × 3.                              |
| Bot Difficulty         | Easy / Medium / Hard (Future Extension) | Encourages extensibility without implementing AI now.                  |
| Turn Selection         | Random                                  | A simple business rule that affects gameplay.                          |

---

# 🧠 The Business Questions Each Scope Decision Answered

| Business Question                           | Scope Decision                                    |
| ------------------------------------------- | ------------------------------------------------- |
| What exactly are we building?               | Domain-focused Entity System                      |
| Who interacts with the system?              | Human and Bot                                     |
| How do users interact?                      | CLI                                               |
| Where does data live?                       | In Memory                                         |
| What assumptions simplify the interview?    | No networking, persistence, authentication        |
| What future flexibility should we preserve? | Configurable board size, pluggable bot strategies |

---

# 🎯 The Interview Story (30-Second Version)

If the interviewer asks:

> "How did you define the scope?"

You can answer:

> "Before thinking about objects or classes, I wanted to establish clear boundaries. I identified that this interview focuses on domain modeling rather than system infrastructure, so I chose a CLI with in-memory state. I identified the primary actors as Human and Bot, kept persistence and networking out of scope, and made a few business assumptions such as configurable board size and random turn selection. This gave me a well-defined design space before discussing the domain."

---

# 🏆 The Step 1 Mental Model

```text
          PROBLEM STATEMENT

                 │
                 ▼

      What exactly are we building?

                 │
                 ▼

     Who interacts with it?

                 │
                 ▼

     How do they interact?

                 │
                 ▼

     Where does data live?

                 │
                 ▼

     What assumptions simplify today?

                 │
                 ▼

     What flexibility should remain?
```

Notice something.

You're not making design decisions yet.

You're defining the **playing field**.

---

# 🌍 Scope Clarification Vocabulary

| Business Meaning     | Scope Decision                    | Examples                                  |
| -------------------- | --------------------------------- | ----------------------------------------- |
| System Focus         | Entity System / Management System | Tic-Tac-Toe, Parking Lot                  |
| Interaction Model    | CLI / REST API / GUI              | CLI, Mobile App                           |
| Storage Strategy     | In-Memory / Database              | RAM, SQL, NoSQL                           |
| Actors               | Users interacting with the system | Customer, Admin, Driver                   |
| Business Assumptions | Simplifications                   | Single User, No Login                     |
| Extension Points     | Future flexibility                | Configurable board size, Strategy Pattern |

---

# 💡 Scope Decision Matrix

| If the interviewer says... | Think about...             |
| -------------------------- | -------------------------- |
| "Design..."                | What type of system is it? |
| "Users can..."             | Who are the actors?        |
| "Build..."                 | Interaction model          |
| "Store..."                 | Persistence strategy       |
| "Ignore..."                | Out-of-scope decisions     |
| "Support later..."         | Extension points           |

---

# 🌟 Biggest Lesson of Step 1

> **Scope is not about limiting the design—it is about protecting the design from unnecessary complexity.**

---
