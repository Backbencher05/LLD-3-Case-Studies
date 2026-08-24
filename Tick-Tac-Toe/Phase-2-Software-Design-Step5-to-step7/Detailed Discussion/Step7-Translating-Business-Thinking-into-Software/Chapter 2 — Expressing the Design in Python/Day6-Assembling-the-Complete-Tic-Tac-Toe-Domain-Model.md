Aditya...

I'm excited too.

But before we write a single line of the final model, I want you to realise something.

## We are **not designing** today.

That work is already finished.

Today we're doing something architects do all the time:

> **Reading the design that already exists.**

Think of an architect building a house.

They don't stand at the construction site asking:

> "Should this house have a kitchen?"

That decision was made months ago.

Construction is simply expressing the blueprint.

That's exactly where we are.

---

# 🚀 Step 7 — Chapter 2, Day 6

# Assembling the Complete Tic-Tac-Toe Domain Model

Let's remind ourselves of everything we've discovered.

---

# Step 1 — Business Responsibilities

| Object           | Responsibility                     |
| ---------------- | ---------------------------------- |
| Game             | Coordinate the entire match.       |
| Board            | Manage the playing area.           |
| Cell             | Manage one square.                 |
| Player           | Decide and perform moves.          |
| WinningCondition | Determine whether someone has won. |
| Position         | Represent a location on the board. |
| Move             | Represent one move in the game.    |

Notice...

These were discovered from the business.

Not Python.

---

# Step 2 — Public Behaviour

Now ask:

> What promise does each object make?

## Game

Commands

* start()
* make_move()
* switch_turn()

Questions

* is_over()
* current_player()

---

## Board

Commands

* place_symbol()

Questions

* state()
* is_full()

Notice something.

We **didn't** expose:

```python
update_cell()

get_cells()

set_cell()

validate_internal_state()
```

Because those are implementation details.

---

## Cell

Commands

* place_symbol()

Questions

* is_empty()
* symbol()

---

## WinningCondition

Questions

* has_winner()

Notice.

No command.

It evaluates.

It doesn't change business state.

---

# Step 3 — State Ownership

Now ask:

> What must each object permanently remember?

## Game

```text
Board

Players

WinningCondition

Current Player

Game Status
```

---

## Board

```text
Size

Cells
```

---

## Cell

```text
Symbol
```

---

## WinningCondition

Perhaps nothing.

Or perhaps:

```text
Winning Pattern
```

depending on future flexibility.

Interesting.

Not every object must remember lots of state.

---

# Step 4 — Relationships

Now ask:

Who must remember whom?

```text
Game

↓

Board

Players

WinningCondition
```

Board

↓

Cells

---

Notice what is **missing**.

```text
Cell

↓

Board
```

No.

---

```text
Board

↓

Game
```

No.

---

```text
WinningCondition

↓

Game
```

No.

---

Everything follows responsibility.

---

# Step 5 — Creation

Now ask:

Who creates whom?

Game

receives

* Board
* Players
* WinningCondition

Board

creates

* Cells

Cell

starts empty

Exactly as we discovered yesterday.

---

# The Entire Design

Now...

Let's finally express all of this in Python.

Notice something important.

We're deliberately **not implementing algorithms**.

Today we're expressing design.

---

```python
from abc import ABC, abstractmethod


# -----------------------------
# Value Objects
# -----------------------------

class Position:

    def __init__(self, row, col):
        self.row = row
        self.col = col


class Move:

    def __init__(self, player, position):
        self.player = player
        self.position = position


# -----------------------------
# Entity
# -----------------------------

class Cell:

    def __init__(self):
        self._symbol = None

    def is_empty(self):
        ...

    def place_symbol(self, symbol):
        ...

    def symbol(self):
        ...


# -----------------------------
# Entity
# -----------------------------

class Board:

    def __init__(self, size):
        self._size = size
        self._cells = self._create_cells()

    def place_symbol(self, position, symbol):
        ...

    def is_full(self):
        ...

    def state(self):
        ...

    def _create_cells(self):
        ...


# -----------------------------
# Strategy
# -----------------------------

class WinningCondition(ABC):

    @abstractmethod
    def has_winner(self, board):
        pass


# -----------------------------
# Entity
# -----------------------------

class Player(ABC):

    def __init__(self, symbol):
        self._symbol = symbol

    @abstractmethod
    def make_move(self, board):
        pass


# -----------------------------
# Root Entity
# -----------------------------

class Game:

    def __init__(
        self,
        board,
        players,
        winning_condition
    ):
        self._board = board
        self._players = players
        self._winning_condition = winning_condition

        self._current_player = None
        self._status = None

    def start(self):
        ...

    def make_move(self):
        ...

    def switch_turn(self):
        ...

    def is_over(self):
        ...

    def current_player(self):
        ...
```

Read this slowly.

Almost every line should remind you of a previous discovery.

Nothing here is arbitrary.

---

# 🌉 Let's Reverse Engineer It

Imagine someone asks:

> **Why is `_board` an attribute?**

Your answer:

> Because the Game permanently collaborates with the Board.

---

Why is `position` a parameter?

Because it is temporary.

---

Why does `Board` create `Cells`?

Because they are part of its internal representation.

---

Why doesn't `Cell` know about `Board`?

Because its responsibility doesn't require it.

---

Why does `Game` receive `WinningCondition`?

Because it collaborates with it.

It doesn't own its construction.

---

Every answer traces back to a business decision.

---

# 🌟 The Biggest Discovery

I don't think today's lesson is actually the code.

It's this.

Look at the direction of our thinking.

Most developers learn like this:

```text
Python

↓

Classes

↓

Objects

↓

Business
```

We learned the opposite.

```text
Business

↓

Responsibilities

↓

Behaviour

↓

State

↓

Relationships

↓

Construction

↓

Python
```

That is the entire philosophy of this mentorship.

---

# 🧠 Engineering Deep Dive

Let's ask our three questions one last time for this chapter.

---

## What did we really build?

Not Tic-Tac-Toe.

We built a **repeatable object discovery process**.

---

## Why was this process necessary?

Because without it, every design decision becomes:

> "I think this class should..."

Instead of:

> "The business requires this responsibility."

That difference scales.

Whether you're building Tic-Tac-Toe...

or Amazon.

---

## What problem does it solve?

It replaces opinion with reasoning.

When someone asks:

> "Why is Board here?"

You don't answer:

> "Because that's how I like to code."

You answer:

> "Because the playing area is a distinct business responsibility."

That is a defendable design.

---

# 🌉 The Complete Discovery Journey

Look at what we've accomplished.

```text
Step 0
Understand the Problem

↓

Step 1
Clarify Scope

↓

Step 2
Gather Requirements

↓

Step 3
Discover the Domain

↓

Step 4
Discover Relationships

↓

Step 5
Assign Responsibilities

↓

Step 6
Discover Collaboration

↓

Step 7
Express the Design

    ↓

Class

↓

Methods

↓

Attributes

↓

Relationships

↓

Construction

↓

Python
```

This is no longer a Tic-Tac-Toe process.

It's an engineering process.

---

# 🎯 Final Assignment — Before We Close This Case Study

This isn't a coding assignment.

It's a reflection assignment.

## Part A — Reverse the Process

Choose **any one class** (Game, Board, Cell, Player, or WinningCondition).

Starting from the Python class, walk backwards and explain:

1. Why does this class exist?
2. Which business responsibility created it?
3. Why does it own these attributes?
4. Why do its methods exist?
5. Why does it know the collaborators it knows?
6. Why does it create (or receive) those collaborators?

The goal is to prove that every line of the class can be justified by business reasoning.

---

## Part B — The Most Important Question

Imagine I delete all the Python code.

But I leave you with:

* requirements,
* domain,
* responsibilities,
* collaborations.

Could you recreate the model?

Why?

---

## Part C — Looking Ahead

Answer these three questions.

1. What was the single biggest change in your thinking during this case study?
2. Which discovery do you think will help you most in future case studies like Amazon or Uber?
3. If you had started coding on Day 1, what mistakes do you think you would have made?

---

# 🌟 Engineering Checkpoint

Complete this sentence.

> **Good object-oriented design is not about writing classes. It is about ____________________.**

Don't look for a textbook answer.

Write the sentence that *you* now believe after everything we've done.

---

# 🧠 One Final Deep Insight

Aditya...

Do you remember something you said weeks ago?

You hoped that one day:

> "All the dots would start connecting."

I think this is the first time that has visibly happened.

Look at what we've used in one small case study:

* abstraction,
* encapsulation,
* ownership,
* composition,
* low coupling,
* high cohesion,
* single source of truth,
* command vs question,
* public vs internal behaviour,
* responsibility assignment,
* object lifetime,
* collaboration,
* construction.

Not because we set out to "learn patterns."

Because the business kept demanding better answers.

That is exactly how software architecture works in the real world.

---

# 🌟 One Sentence That Changed My Thinking

I'll leave you with the sentence that I think defines this entire journey:

> **We did not invent the software model; we discovered it by carefully listening to the business.**

And that's why I'm confident that when we start designing Amazon, Uber, Netflix, Airbnb, or any other complex system, you won't be starting from a blank page.

You'll start by asking the same questions we've been practising all along.

That is the real outcome of this Tic-Tac-Toe case study. 🚀



What Is Missing?

Although our model is strong, there are still engineering topics we haven't explored.

For example:

Method implementations
Business algorithms
Validation
Error handling
Extensibility
Design patterns
Testing
Persistence
APIs
Concurrency

Those are different layers of engineering