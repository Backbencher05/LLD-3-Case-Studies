This is one of the most important exercises in software architecture.

You're no longer asking:

> **"How do I draw a class diagram?"**

You're asking:

> **"What is the minimum information required to transfer the architecture of a system?"**

That is exactly how experienced architects think.

---

# First Principle

Imagine your whiteboard has **very little space**.

Every word you write has a cost.

So before writing anything, ask:

> **"If I remove this piece of information, will the engineer misunderstand the architecture?"**

If the answer is **yes**, it's **essential**.

If the answer is **no**, it's **optional** for the first explanation.

So our whiteboard should contain only the information that defines the system's **structure**, not every implementation detail.

---

# Essential Information

These are the pieces I would absolutely write.

## 1. The Core Software Objects

Without knowing the main objects, there is no mental model of the system.

For Tic-Tac-Toe:

* Game
* Board
* Player
* Cell
* Move
* WinningCondition

### Why is this essential?

Because these are the building blocks of the software.

Without them, the engineer cannot even answer:

> "What exists in this system?"

Everything else depends on knowing these objects.

---

## 2. Responsibility of Each Object

Merely listing object names is not enough.

Each object exists to solve a specific problem.

For example:

| Object           | Responsibility                 |
| ---------------- | ------------------------------ |
| Game             | Controls the overall game flow |
| Board            | Manages the playing grid       |
| Player           | Decides and performs moves     |
| Cell             | Holds one symbol               |
| Move             | Represents a player's action   |
| WinningCondition | Determines if someone has won  |

### Why is this essential?

Because software architecture is fundamentally about **responsibility assignment**.

If the engineer doesn't know who is responsible for what, they cannot reason about the design.

---

## 3. Relationships Between Objects

Now we connect the building blocks.

For example:

* Game owns Board
* Game manages Players
* Board contains Cells
* Game uses WinningCondition
* Player creates Moves

### Why is this essential?

Objects without relationships are just isolated boxes.

The relationships explain how the software is assembled.

---

## 4. Ownership and Lifetime

Some relationships are stronger than others.

For example:

* Board exists only because Game exists.
* Cells exist only because Board exists.

This tells the engineer:

> "These objects are part of a larger whole."

### Why is this essential?

Because ownership influences creation, destruction, and responsibility.

It prevents misunderstandings about object lifecycles.

---

## 5. Collaboration Flow

Without implementation details, show the typical collaboration:

```text
Player
   │
   ▼
Game
   │
   ▼
Board
   │
   ▼
WinningCondition
   │
   ▼
Game State Updated
```

### Why is this essential?

Because architecture is not only about static structure.

It's also about how objects cooperate to accomplish work.

This bridges the gap between structure and behaviour.

---

## 6. System Boundaries

Clearly indicate what each object should **not** do.

Examples:

* Cell does not decide winners.
* Player does not modify the Board directly.
* Board does not manage turns.
* WinningCondition does not change game state.

### Why is this essential?

Good architecture is defined as much by **what objects don't do** as by what they do.

Clear boundaries reduce coupling and prevent responsibility leakage.

---

## 7. Design Philosophy

Finally, write the guiding principles behind the design.

For example:

* Single Responsibility
* High Cohesion
* Low Coupling
* Information Expert
* Composition over unnecessary inheritance

### Why is this essential?

These principles explain *why* the structure looks the way it does.

Without them, the diagram becomes a picture instead of an architectural decision.

---

# Optional Information (Initially)

These are valuable, but they are not required for someone to grasp the architecture.

---

## 1. Attributes

For example:

```
Game
---------
status
currentTurn
winner
```

### Why is this optional?

Attributes affect implementation, not the architectural structure.

The engineer can understand the system without knowing every field.

---

## 2. Methods

For example:

```
makeMove()
switchTurn()
checkWinner()
```

### Why is this optional?

Method names describe implementation details.

Responsibilities already communicate the behaviour at a higher level.

---

## 3. Data Types

Examples:

* int
* String
* Boolean
* List<Cell>

### Why is this optional?

These are language-specific details.

Architecture should remain understandable regardless of whether it's implemented in Python, Java, or C#.

---

## 4. Visibility

Examples:

* private
* public
* protected

### Why is this optional?

Encapsulation is important in code, but it does not change the system's conceptual structure.

---

## 5. Multiplicity

Examples:

* 1..*
* 0..1
* *

### Why is this optional?

Knowing that a `Board` contains many `Cells` is enough initially.

The exact notation can wait until the design is refined.

---

## 6. Constructor Details

For example:

* Dependency injection
* Internal object creation
* Factory methods

### Why is this optional?

These are implementation choices.

They don't change the conceptual architecture.

---

## 7. Enumerations and Value Objects

Examples:

* Symbol
* GameStatus
* PlayerType
* Position

### Why is this optional?

They support the core objects but do not define the primary structure.

Once the engineer understands the main objects and their relationships, these become easy to introduce.

---

## 8. Algorithms

For example:

* Minimax
* Win detection logic
* Turn validation

### Why is this optional?

Algorithms describe **how** responsibilities are fulfilled.

The whiteboard's first job is to explain **who** owns those responsibilities.

---

# A Useful Rule of Thumb

When deciding whether something belongs on the whiteboard, ask:

| Question                                       | If the answer is "Yes"... |
| ---------------------------------------------- | ------------------------- |
| Does it define what exists?                    | Essential                 |
| Does it define who is responsible?             | Essential                 |
| Does it define how objects collaborate?        | Essential                 |
| Does it define ownership or boundaries?        | Essential                 |
| Does it explain implementation details?        | Optional (initially)      |
| Does it describe language syntax?              | Optional                  |
| Does it describe algorithms or internal logic? | Optional                  |

---

# The Whiteboard Test

If I had only one whiteboard and five minutes, I would draw only:

1. **The core objects** (What exists?)
2. **Each object's responsibility** (Why does it exist?)
3. **Their relationships** (How are they connected?)
4. **Their collaboration flow** (How do they work together?)
5. **The design principles** (Why is it structured this way?)

Everything else—attributes, methods, visibility, multiplicity, constructors, algorithms, and language-specific details—can be layered on later without changing the engineer's understanding of the architecture.

---

# One Sentence That Changes the Thinking

> **An architect's first diagram is not meant to describe the software completely; it is meant to communicate the smallest possible set of truths that allows another engineer to reconstruct the system's mental model correctly.**
