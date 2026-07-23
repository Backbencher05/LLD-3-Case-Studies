# GRASP: (General Responsibility Assignment Software Patterns) is a set of nine core principles in object-oriented design. 
---

# Part A — Mapping Our Discoveries to GRASP

---

# 1. Information Expert

## What problem does it solve?

Information Expert answers a simple question:

> **"Who has the information needed to perform this responsibility?"**

Instead of assigning behavior randomly, we give it to the object that already owns the relevant knowledge.

This leads to natural, maintainable designs.

---

## Which Tic-Tac-Toe discussion helped us discover it?

Almost every responsibility assignment.

Especially:

* Who should check whether a Cell is empty?
* Who should validate a position?
* Who should reset the Board?
* Who should update a Cell?

Every one of those discussions started with:

> Who already knows enough to do this?

---

## Example

### Behavior

Check if a Cell is empty.

### Wrong

Game checks the Cell's internal value.

### Better

Cell answers:

> "Yes, I'm empty."

Why?

Because the Cell owns that information.

That is **Information Expert**.

---

# 2. Low Coupling

## What problem does it solve?

Low Coupling reduces unnecessary dependencies between objects.

The fewer implementation details one object knows about another, the easier the system is to change.

---

## Which Tic-Tac-Toe discussion helped us discover it?

The delegation exercises.

Especially:

Game resets Board.

Instead of:

Game looping through every Cell.

We chose:

Game → Board

Board → Cell

---

## Example

Instead of:

Game manipulating every Cell directly,

Game simply asks:

> "Board, reset yourself."

Now Game doesn't care how the Board stores Cells.

That is Low Coupling.

---

# 3. High Cohesion

## What problem does it solve?

High Cohesion keeps related responsibilities together.

Each object should focus on one well-defined purpose.

---

## Which Tic-Tac-Toe discussion helped us discover it?

Our discussions around:

* Board
* WinningCondition
* ConsoleView

Especially:

Should Board determine winners?

We eventually said:

No.

Board manages board state.

WinningCondition evaluates rules.

---

## Example

Board:

* stores Cells
* validates positions
* places symbols

WinningCondition:

* checks rows
* checks columns
* checks diagonals

Each object has one focused responsibility.

That is High Cohesion.

---

# 4. Pure Fabrication

## What problem does it solve?

Sometimes the best place for a responsibility is...

**Nowhere in the domain.**

If forcing it into a domain object would increase coupling or reduce cohesion, we invent a helper object that exists purely for software design.

---

## Which Tic-Tac-Toe discussion helped us discover it?

Scenario:

Game prints the board.

Initially:

Game prints everything.

Then we realized:

Printing isn't part of the business.

It belongs somewhere else.

---

## Example

ConsoleView.

The business has no "ConsoleView."

We created it because software needs presentation.

That's Pure Fabrication.

---

# Summary

| GRASP Principle    | Problem It Solves                                             | Tic-Tac-Toe Discovery                     | Example                                               |
| ------------------ | ------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------- |
| Information Expert | Assign behavior to the object with the necessary knowledge    | Responsibility assignment                 | Cell checks if it is empty                            |
| Low Coupling       | Reduce dependencies between objects                           | Delegation instead of direct manipulation | Game asks Board to reset                              |
| High Cohesion      | Keep related responsibilities together                        | Separating Board and WinningCondition     | Board manages state; WinningCondition evaluates rules |
| Pure Fabrication   | Avoid forcing non-domain responsibilities into domain objects | Separating presentation from game logic   | ConsoleView prints the board                          |

---

# Part B — Classification

---

# Game

## Category

**Domain Class**

### Why?

The Game represents a core business concept.

It has identity, state, and responsibilities related to the lifecycle of a Tic-Tac-Toe game.

---

# Board

## Category

**Domain Class**

### Why?

The Board exists in the business domain.

It represents the playing surface and manages its Cells.

---

# Player

## Category

**Domain Class**

### Why?

Players participate in the game.

They have identity and behavior.

---

# Cell

## Category

**Domain Class**

### Why?

Although not an independent business entity, the Cell models part of the playing board and owns meaningful state and behavior within that domain.

It isn't fabricated for software—it represents something real in the game.

---

# Position

## Category

**Value Object**

### Why?

A Position simply represents coordinates.

It has no identity and is compared by its values (row and column).

---

# Symbol

## Category

**Value Object** *(often implemented as an Enum)*

### Why?

A Symbol represents a value such as X or O.

It carries meaning but no independent identity.

Whether implemented as an enum or another immutable representation, it's still modeling a value rather than a domain object.

---

# GameStatus

## Category

**Value Object** *(often implemented as an Enum)*

### Why?

GameStatus represents the current state of the game (e.g., In Progress, Won, Draw).

It describes the Game but is not an independent object with behavior.

---

# WinningCondition

## Category

**Policy / Rule Object**

### Why?

WinningCondition doesn't represent a physical thing in the game.

It represents a **business rule**: how to determine a winner.

Its primary responsibility is evaluating policy.

---

# ConsoleView

## Category

**Pure Fabrication**

### Why?

The business domain contains no ConsoleView.

It exists purely to separate presentation from domain logic.

---

# Logger

## Category

**Pure Fabrication**

### Why?

Logging supports the software, not the business.

It improves observability without representing a business concept.

---

# Repository

## Category

**Pure Fabrication**

### Why?

The business doesn't talk about repositories.

A Repository exists to manage persistence and hide storage details from the domain model.

---

# EmailSender

## Category

**Pure Fabrication**

### Why?

Sending emails is an infrastructure concern.

The business may require notifications, but the technical mechanism for sending them is not part of the core domain.

---

# Final Classification

| Concept          | Category             | Why                                                         |
| ---------------- | -------------------- | ----------------------------------------------------------- |
| Game             | Domain Class         | Represents the game and coordinates its lifecycle.          |
| Board            | Domain Class         | Represents the playing area and manages board state.        |
| Player           | Domain Class         | Represents a participant with identity and behavior.        |
| Cell             | Domain Class         | Represents part of the board and owns its own state.        |
| Position         | Value Object         | Represents coordinates and is identified by its values.     |
| Symbol           | Value Object         | Represents the player's mark; identity is its value.        |
| GameStatus       | Value Object         | Represents the current state of the game.                   |
| WinningCondition | Policy / Rule Object | Encapsulates the business rule for winning.                 |
| ConsoleView      | Pure Fabrication     | Handles presentation, not domain behavior.                  |
| Logger           | Pure Fabrication     | Provides technical support for the application.             |
| Repository       | Pure Fabrication     | Manages persistence as an infrastructure concern.           |
| EmailSender      | Pure Fabrication     | Encapsulates email delivery, an external technical concern. |

---

# 🌟 One Sentence That Changed My Thinking

> **Good software design isn't about putting every responsibility into a business object—it's about putting every responsibility into the object that can own it for the right reason.**

---

# Mentor's Feedback

This assignment marks an important milestone in your learning.

At the beginning of the case study, you were asking:

> *"What classes should I create?"*

Now you're asking richer questions:

* *Who has the knowledge?* (Information Expert)
* *Who should depend on whom?* (Low Coupling)
* *Does this object have a focused purpose?* (High Cohesion)
* *Is this even a business concept, or is it just helping the software?* (Pure Fabrication)

One small refinement to keep in mind is the distinction between **domain modeling** and **software representation**. For example, `Cell` is a **domain class** because it models something that exists in the game world, even though it isn't an independent business entity. Likewise, `Symbol` and `GameStatus` are best thought of as **value concepts** in the domain, even if their software representation is an `enum`. The category describes *what they are conceptually*, while the implementation describes *how they're represented in code*.

That's the kind of distinction that separates someone who knows design patterns from someone who understands software design.
