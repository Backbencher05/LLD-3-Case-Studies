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
