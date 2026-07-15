Perfect.

This is one of my favorite steps because **most LLD mistakes originate here**.

People think they fail in the class diagram.

**No.**

They fail because they misunderstood or skipped the requirements.

---
# this file include
-------------------------------

# 1. Requirement Gathering Overview 

```
Requirements
      │
      ├── Functional
      ├── Non-Functional
      ├── Constraints
      └── Out of Scope
```
# 2. The Exercise based on 
      │
      ├── Functional
      ├── Non-Functional
      ├── Constraints
      └── Out of Scope

# 3. My Answers 




# Step 2 — Requirement Gathering

## 🎯 Goal

By the end of this step, we should be able to answer:

> **"What should the system do?"**

Notice...

Not

> "How will we implement it?"

Implementation comes much later.

---

# An Important Lesson

Imagine someone tells you:

> Build a house.

You immediately start drawing walls.

A good architect asks:

* How many people will live there?
* How many bedrooms?
* Is there parking?
* Is it earthquake resistant?
* What's the budget?

Requirements first.

Design second.

Exactly the same applies here.

---

# Requirement Categories

I always divide requirements into four categories.

```
Requirements
      │
      ├── Functional
      ├── Non-Functional
      ├── Constraints
      └── Out of Scope
```

We'll follow this structure for every future case study.

---

# Part A — Functional Requirements

These answer:

> **What should the system do?**

Examples:

* A player should be able to join the game.
* A player should make a move.
* The system should validate the move.
* The system should update the board.
* The system should detect a winner.
* The system should detect a draw.

Notice these are behaviors.

Not implementation details.

---

# Part B — Non-Functional Requirements

These answer:

> **How should the system behave?**

Examples:

* Easy to extend.
* Easy to test.
* Maintainable.
* UI independent.
* Low coupling.
* High cohesion.
* Configurable board size.

These are qualities.

---

# Part C — Constraints

These are rules we must obey.

Examples:

* Exactly two players.
* One move at a time.
* Players cannot change symbols after the game starts.
* Every symbol must be unique.
* Only valid moves are accepted.

Constraints often become validations in the software.

---

# Part D — Out of Scope

This is equally important.

For Version 1:

* Online multiplayer
* Database
* Authentication
* Leaderboards
* Tournament mode
* Chat
* Save/Load
* Spectator mode

Being explicit prevents unnecessary complexity.

---

# The Exercise

I don't want you to write 5–6 requirements.

I want you to think like a Product Manager and an Engineer together.

Prepare the following:

## 1. Functional Requirements

Write every behavior the system should support.

Don't worry if there are 10 or 20.

Think carefully.

Examples (don't stop here):

* Create a game
* Start a game
* Make a move
* Validate a move

Keep going until you think you've covered the complete gameplay.

---

## 2. Non-Functional Requirements

Think beyond coding.

Questions to guide you:

* Should the game logic know about the CLI?
* Should it be easy to replace the UI?
* Should it be easy to add AI later?
* Should the board size be configurable?
* Should it be testable?

---

## 3. Constraints

Write every rule that should always remain true.

Think about:

* Players
* Symbols
* Turns
* Board
* Game state

---

## 4. Out of Scope

Write everything we are intentionally not building in Version 1.

---

# One New Habit I Want You to Learn

This is something I learned after working on production systems.

Whenever you write a requirement, ask yourself:

> **Can I verify this?**

For example:

✅ Good requirement:

> The system shall reject moves made on an occupied cell.

Why?

Because you can test it.

---

❌ Weak requirement:

> The game should be user-friendly.

How do you verify that?

It's vague.

Strong requirements are specific and testable.

---

# Engineering Challenge 🧠

Before you start writing, think about this carefully:

> **Is "Check Winner" actually a functional requirement?**

Or is it merely one way to satisfy a higher-level requirement?

I'm **not** asking you to answer now. Just think about it while writing your requirements.

This is a subtle distinction that experienced engineers notice, and we'll discuss it after you share your list.



-----------------------------
## My Answers

Excellent. I also looked at the assumptions you made in the previous session. They already show that you're starting to think beyond a simple 3×3 game and toward a reusable game engine. That's exactly the direction we want for LLD.

Now, if I were writing the **Requirement Gathering** document for this case study, here's how I would structure it.

---

# Requirement Gathering — Tic-Tac-Toe (Version 1)

## Part A — Functional Requirements

These describe **what the system should do**.

### Game Lifecycle

1. The system should allow creating a new game.
2. The system should initialize the game board.
3. The system should create all players.
4. The system should assign a unique symbol to each player.
5. The system should randomly decide the first player.
6. The system should start the game.
7. The system should end the game when a winning or draw condition is met.
8. The system should allow starting a new game after the current game ends.

---

### Player Actions

9. A player should be able to make a move.
10. The system should accept input for a board position.
11. The system should validate the requested move.
12. The system should reject invalid moves.
13. The system should update the board after a valid move.
14. The system should switch the turn to the next player.
15. A bot player should automatically generate its move during its turn.

---

### Board Management

16. The system should maintain the current state of the board.
17. The system should display the board after every move.
18. The system should determine whether a cell is occupied or empty.

---

### Game Rules

19. The system should determine whether a player has achieved the winning condition.
20. The system should determine whether the game has resulted in a draw.
21. The system should announce the winner.
22. The system should announce a draw if no winner exists.

---

### Undo Feature

23. The system should allow undoing the previous move.
24. After an undo, the board should be restored to its previous state.
25. The turn should also be restored after an undo.

---

### Configuration

26. The system should support configurable board size (N × N).
27. The system should support configurable winning conditions based on the board size.
28. The system should support different bot difficulty levels (Easy, Medium, Hard).

---

## Part B — Non-Functional Requirements

These describe **how the system should behave**.

### Maintainability

* The design should be modular.
* The code should be easy to understand.
* Responsibilities should be clearly separated.

---

### Extensibility

* It should be easy to introduce new player types.
* It should be easy to introduce new bot strategies.
* It should be easy to support different board sizes.
* It should be easy to change the winning rules.
* It should be easy to add new game modes later.

---

### UI Independence

* The game logic should not depend on the CLI.
* The same game engine should work with a GUI, web application, or REST API.

---

### Testability

* Business logic should be independently testable.
* Individual components should be unit-test friendly.

---

### Flexibility

* Number of players should be configurable.
* Board dimensions should be configurable.
* Symbols should be configurable.
* Bot difficulty should be configurable.

---

### Design Quality

* High cohesion.
* Low coupling.
* Favor composition over inheritance where appropriate.
* Follow SOLID principles.

---

## Part C — Constraints

These are rules that must always remain true.

### Players

* Every player must have a unique symbol.
* Only one player can play at a time.
* A player cannot play twice consecutively.
* Players cannot change their symbol after the game starts.
* Human and bot players should behave uniformly from the game's perspective.

---

### Board

* A move must be inside the board boundaries.
* A move can only be made on an empty cell.
* Once placed, a symbol cannot be overwritten (unless an undo is performed).

---

### Game Flow

* Only valid moves should update the board.
* The game cannot continue after it has ended.
* Every valid move must update the board before the next turn begins.
* Only one winner can exist in a game.
* If no winning condition is met and all cells are occupied, the game ends in a draw.

---

### Configuration

* Board size must be greater than or equal to the minimum supported size.
* Winning condition must be compatible with the board size.
* At least two players are required to start a game.
* Every player must have a distinct symbol.

---

## Part D — Out of Scope (Version 1)

To keep Version 1 focused, the following features are intentionally excluded:

### Multiplayer

* Online multiplayer
* Networking
* Multiple concurrent games

---

### Persistence

* Database
* Save game
* Load game
* Replay previous games

---

### User Management

* Authentication
* User profiles
* Player statistics

---

### Competitive Features

* Leaderboards
* Tournament mode
* Match history
* Rankings

---

### Social Features

* Chat
* Spectator mode
* Invitations
* Friends list

---

### Advanced Gameplay

* Timers
* Move history visualization
* Redo functionality
* Custom game rules editor
* AI learning from previous games

---

# Engineering Discussion 🧠

You were asked to think about this question:

> **Is "Check Winner" actually a functional requirement?**

This is an important distinction.

I would say **no**.

A functional requirement describes **what the user or system is expected to accomplish**. "Check Winner" is an internal step the system performs to satisfy a broader requirement.

For example:

* **Functional Requirement:** The system should determine the outcome of the game after each valid move.
* Possible implementations:

  * Check rows.
  * Check columns.
  * Check diagonals.
  * Use counters.
  * Use bit masks.

"Check Winner" is one implementation approach among several. The real requirement is that the system correctly identifies whether the game has been won, drawn, or should continue.

This distinction becomes increasingly important in larger systems: requirements should describe **behavior and outcomes**, while the design and implementation decide **how** those outcomes are achieved.

---

## Feedback on Your Previous Assumptions

Your previous answers already show good architectural thinking:

* ✅ Configurable `N × N` board instead of hardcoding 3×3.
* ✅ Human and Bot as interchangeable player types.
* ✅ Randomly choosing the first player.
* ✅ Extensibility and flexibility as explicit goals.
* ✅ Bot difficulty levels, which naturally suggest applying the **Strategy Pattern** later.
* ✅ Undo support, which hints at maintaining move history and possibly using the **Memento** or **Command Pattern** in future iterations.

The only assumption I'd refine is **"number of players: (N-1)"**. For classic Tic-Tac-Toe, the game is inherently designed for **exactly two players**. If your goal is to build a generic board-game engine, it's better to phrase it as:

> **The game engine should support a configurable number of players (minimum 2), provided the game rules define how turns, symbols, and winning conditions work.**

That wording keeps the design flexible without tying the number of players directly to the board size, since those are independent concepts.




------------------------------------------------------
