## Step 2 — Requirement Gathering (Interview Version)

# Flow 

Product Definition
        │
        ▼
Functional Requirements
        │
        ▼
Non-Functional Requirements
        │
        ▼
Business Rules
        │
        ▼
Constraints
        │
        ▼
Out of Scope


### Product Definition

For Version 1, we are building:

* A Tic-Tac-Toe Game Engine.
* Core business logic only.
* Independent of UI.
* Independent of persistence.
* In-memory implementation.
* CLI used only for demonstration.
* Supports Human and Bot players.
* Supports configurable board dimensions.
* Supports configurable player symbols.
* Supports configurable bot difficulty.
* Starting player selected randomly.




### Functional Requirements

> I'd first identify the core functional requirements.

* Create a new game.
* Initialize the board and players.
* Assign unique symbols to players.
* Decide the starting player.
* Allow players to make moves.
* Validate every move.
* Update the board after a valid move.
* Alternate turns.
* Determine whether the game continues, ends with a winner, or ends in a draw.
* Allow starting a new game after completion.

---

### Non-Functional Requirements

> From a design perspective, I'd keep the following in mind:

* The design should be modular.
* The game engine should be independent of the UI.
* The system should be easily extensible.
* Components should be independently testable.
* The board size should be configurable.

---

### Constraints

* Only valid moves should modify the board.
* Each player must have a unique symbol.
* Only one player moves at a time.
* A completed game should not accept further moves.

---

### Out of Scope

For the initial version, I'd exclude:

* Online multiplayer
* Database
* Authentication
* Leaderboards
* Tournament mode
* Chat
* Save/Load functionality

---

### Final Statement

> With these requirements finalized, I'd move on to identifying the core domain objects before thinking about classes or implementation.

---

See the difference?

This isn't just a shorter version.

It sounds like someone speaking in an interview.

---

# Here's another realization.

The interview version is **not fixed**.

It depends on the interviewer.

Suppose the interviewer interrupts after Functional Requirements.

You stop.

You don't continue.

Suppose they ask:

> "Don't worry about non-functional requirements."

You skip them.

So the Interview Version is actually your **mental checklist**, not a script to memorize.


--------------------------------------------------------------------------------

Absolutely.

And I actually think **Step 2 benefits even more** from this format than Steps 3 and 4.

Why?

Because one of the biggest mistakes candidates make is treating **requirements gathering as just making a list**.

But that's not what senior engineers do.

Senior engineers classify requirements.

After everything we've built, I think Step 2 should end like this.

---

# 📋 Final Requirement Discovery Summary (Interview Cheat Sheet)

After discussing the business problem, we classified the requirements into the following categories.

| Requirement Category        | What We Discovered                                                                           | Why It Matters                                         |
| --------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Functional Requirements     | Start game, make move, validate move, switch turns, detect winner, detect draw, restart game | Defines what the system must do.                       |
| Non-Functional Requirements | Maintainable, extensible, readable, testable                                                 | Defines how well the system should perform and evolve. |
| Constraints                 | N × N board, one move per turn, no overwriting occupied cells                                | Defines business rules that cannot be violated.        |
| Assumptions                 | CLI interaction, in-memory storage, no authentication                                        | Simplifies the current design scope.                   |
| Out of Scope                | Networking, persistence, multiplayer over internet, leaderboard                              | Prevents unnecessary over-engineering.                 |

---

# 🧠 The Business Questions Each Requirement Answered

One realization from Step 2 was that **every requirement answers a different business question**.

| Business Question                      | Requirement Category        |
| -------------------------------------- | --------------------------- |
| What should the system do?             | Functional Requirements     |
| How good should the system be?         | Non-Functional Requirements |
| What rules can never be broken?        | Constraints                 |
| What are we assuming for this version? | Assumptions                 |
| What are we deliberately not building? | Out of Scope                |

Notice how much easier this is to remember than a random list of requirements.

---

# 🎯 The Interview Story (30-Second Version)

If the interviewer asks:

> "How did you gather the requirements?"

You can answer:

> "I first separated the problem into functional and non-functional requirements. Functional requirements describe the system's behavior, while non-functional requirements define qualities like maintainability and extensibility. Next, I identified business constraints that the implementation must always respect. Then I documented assumptions to keep the scope realistic for the interview. Finally, I explicitly identified what was out of scope to avoid over-engineering. That gave me clear boundaries before moving into domain modeling."

Notice how you're describing **a process**, not just listing features.

---

# 🏆 The Step 2 Mental Model

If you remember only one diagram from Step 2, let it be this:

```text
             BUSINESS NEED

                  │
                  ▼

      What should the system do?

                  │
                  ▼

     Functional Requirements

                  │
                  ▼

      How should it behave?

                  │
                  ▼

  Non-Functional Requirements

                  │
                  ▼

    What rules cannot be broken?

                  │
                  ▼

          Constraints

                  │
                  ▼

  What are we assuming today?

                  │
                  ▼

         Assumptions

                  │
                  ▼

 What are we intentionally NOT building?

                  │
                  ▼

          Scope Boundary
```

Notice something.

You're not collecting requirements.

You're **building boundaries**.

---

# 🌍 Requirement Discovery Vocabulary (Reusable Across Every LLD)

| Business Meaning   | Requirement Category       | Examples                                                 |
| ------------------ | -------------------------- | -------------------------------------------------------- |
| System behavior    | Functional Requirement     | Create Order, Cancel Booking, Make Move                  |
| Quality attribute  | Non-Functional Requirement | Scalability, Maintainability, Availability               |
| Business rule      | Constraint                 | Maximum players, One move per turn, Daily transfer limit |
| Simplification     | Assumption                 | CLI, In-memory, Single user                              |
| Boundary           | Out of Scope               | Payments, Notifications, Analytics                       |
| Future enhancement | Nice-to-Have               | AI hints, Replay, Statistics                             |

This vocabulary immediately transfers to **Parking Lot, Splitwise, BookMyShow, Banking, Ride Sharing**, and every other system.

---

# 📖 Final Requirement Classification

| Category                    | Tic-Tac-Toe Examples                                                                               |
| --------------------------- | -------------------------------------------------------------------------------------------------- |
| Functional Requirements     | Start Game, Make Move, Validate Move, Detect Winner, Detect Draw, Restart                          |
| Non-Functional Requirements | Extensible, Maintainable, Readable, Testable                                                       |
| Constraints                 | One move per turn, Valid positions only, Cannot overwrite occupied cells, Configurable N × N board |
| Assumptions                 | CLI, Hardcoded players, In-memory state, No login                                                  |
| Out of Scope                | Persistence, Networking, Leaderboards, Authentication, Spectators                                  |

---

# 💡 One More Improvement

I think Step 2 should also have a **Requirement Decision Matrix**, just like Step 3 had an Object Decision Matrix.

---

## Requirement Decision Matrix

Whenever you hear a requirement during an interview, ask:

| If the business says...   | It is probably...          |
| ------------------------- | -------------------------- |
| "The system should..."    | Functional Requirement     |
| "The system should be..." | Non-Functional Requirement |
| "It must never..."        | Constraint                 |
| "Assume..."               | Assumption                 |
| "We are not building..."  | Out of Scope               |
| "Maybe later..."          | Future Enhancement         |

This is incredibly useful because interviewers often mix these together intentionally.

---

# 🧭 Interview Checklist for Requirement Gathering

Before leaving Step 2, quickly verify:

* ✅ Did I capture all core user actions?
* ✅ Did I identify quality attributes (maintainability, extensibility, etc.)?
* ✅ Did I identify business rules that cannot be violated?
* ✅ Did I state my assumptions explicitly?
* ✅ Did I define what is intentionally out of scope?
* ✅ Did I avoid discussing classes or implementation?

---

# 🌟 The Biggest Lesson of Step 2

If I had to summarize everything from Step 2 into one sentence, it would be:

> **Good requirement gathering is not about collecting features—it is about building clear boundaries for the design.**

That sentence is the bridge to everything that follows.

* **Step 2** defines **what the system must achieve**.
* **Step 3** discovers **what exists to achieve it**.
* **Step 4** explains **how those concepts work together**.

You can see a beautiful progression emerging:

* **Step 0:** Understand the Problem
* **Step 1:** Define the Scope
* **Step 2:** Define the Boundaries *(Requirements)*
* **Step 3:** Discover the Building Blocks *(Objects)*
* **Step 4:** Connect the Building Blocks *(Relationships)*

We're no longer learning isolated LLD topics—we're constructing a complete engineering methodology. By the time we reach Step 5 (Class Design), it won't feel like inventing classes; it will feel like the natural translation of everything we've already discovered.
