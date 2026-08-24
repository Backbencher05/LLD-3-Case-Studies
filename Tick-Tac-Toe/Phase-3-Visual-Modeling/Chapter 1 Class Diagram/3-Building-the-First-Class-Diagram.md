Excellent.

Today is one of the biggest milestones in our entire Tic-Tac-Toe journey.

For the first time, **we are going to draw software**.

But I want you to notice something.

We're not starting with a UML tool.

We're not even starting with boxes.

We're starting with an engineering question.

That has been our philosophy from Day 1, and it won't change now.

---

# Phase 3 — Visual Modelling

## Chapter 1 — Building the First Class Diagram

## Business Question

Imagine you are standing in front of a whiteboard.

You already know everything about the Tic-Tac-Toe system.

Now someone asks:

> **"Which class do you draw first?"**

This sounds like a simple question.

It isn't.

---

# The Beginner's Approach

Most beginners start randomly.

Sometimes they draw `Board` first.

Sometimes `Player`.

Sometimes `Game`.

Sometimes whichever class they remember first.

That tells us something.

They think:

> Drawing order doesn't matter.

But architects rarely work that way.

---

# Let's Return to First Principles

We already discovered that our software has these major objects:

```text
Game
Board
Player
Cell
Move
WinningCondition
```

Now ask yourself:

> **Are all of these equally important?**

Or...

Does one object naturally become the centre of the model?

---

# Think About the Business

Forget software.

Imagine two people are playing Tic-Tac-Toe.

What actually exists?

Do they play a "Board"?

No.

Do they play a "Player"?

No.

Do they play a "WinningCondition"?

No.

They play **a game**.

Everything else exists because the game exists.

That observation is not about UML.

It is about the business.

---

# Discovery 1 — The Root of the Model

Earlier, we discovered lifecycle ownership.

Remember?

We asked:

* Who creates the Board?
* Who owns the Players?
* Who owns the Moves?
* Who owns the WinningCondition?

Again and again, our answer pointed to the same object.

**Game.**

That means something profound.

---

## Final Discovery

> **The first class we draw should usually be the root of the object graph—the object that represents the business system and owns the overall lifecycle.**

For Tic-Tac-Toe...

That class is:

```text
+----------------------+
|        Game          |
+----------------------+
```

Notice something.

We have drawn exactly one box.

No attributes.

No methods.

No relationships.

And yet...

This is already an engineering decision.

---

# Why Start With Game?

Let's justify it.

From our earlier discoveries:

* The game cannot exist without a board.
* The game cannot exist without players.
* The game controls turns.
* The game knows its state.
* The game asks the winning condition to evaluate outcomes.
* The game decides when play starts and ends.

Every major business capability flows through `Game`.

That makes it our orchestration point.

---

# Important Distinction

Be careful with the word "orchestrator."

`Game` is **not** a "God Object."

It doesn't do everything.

It coordinates everything.

Remember our responsibility assignment:

* `Board` manages the grid.
* `WinningCondition` evaluates victory.
* `Player` decides moves.
* `Cell` stores symbols.

`Game` delegates.

That's healthy architecture.

---

# Discovery 2 — Before Adding Relationships, Complete the Class

Now here's another question.

We have a box.

What should be the **next** thing we add?

Most UML books immediately add:

* attributes,
* methods,
* relationships.

But let's think.

What information does our Software Discovery Framework tell us belongs **inside** the class?

Earlier we discovered four structural elements:

1. Identity
2. Knowledge (Attributes)
3. Work (Operations)
4. Relationships (outside the class)

Relationships connect classes, so we can't add them until we have another class.

That leaves us with:

* Name
* Attributes
* Operations

---

# Should We Add Attributes First?

Let's reason.

Imagine I show you this.

```text
+----------------------+
|        Game          |
+----------------------+
| status               |
| currentTurn          |
| board                |
| players              |
+----------------------+
```

Could another engineer understand it?

Partially.

Now imagine I show this instead.

```text
+----------------------+
|        Game          |
+----------------------+
|                      |
+----------------------+
| start()              |
| makeMove()           |
| switchTurn()         |
+----------------------+
```

Again...

Partially.

Neither is complete.

So which should come first?

---

# Let's Think Like an Architect

Remember our SDF:

> What knowledge must it remember?

comes before

> What work must it perform?

Why?

Because...

An object can only perform behaviour using the knowledge it owns.

Its behaviour depends on its state.

This isn't a programming rule.

It's an engineering reasoning rule.

---

# Discovery 3 — Knowledge Before Behaviour

So, for our first class, we naturally discover this order:

```text
+----------------------+
|        Game          |
+----------------------+
| status               |
| board                |
| players              |
| currentPlayer        |
| winningCondition     |
+----------------------+
| ...operations later...|
+----------------------+
```

Notice that I intentionally wrote:

> `...operations later...`

Why?

Because I don't want us to guess.

Every operation we place inside this class must already have been justified by the responsibilities we assigned in Step 7.

---

# Stop Here

Most tutorials would now fill in every method.

We're not going to.

Because we haven't asked an important engineering question yet.

---

# The Next Discovery

Look at these attributes:

```text
status
board
players
currentPlayer
winningCondition
```

They don't all feel the same.

Some are simple values.

Some are references to other objects.

Some are collections.

Some are strategies.

Some represent ownership.

Some represent state.

We cannot simply list them.

We need to understand **why each attribute exists**, **what kind of knowledge it represents**, and **how that influences our design**.

---

# 🎯 Your Assignment

Take the `Game` class only.

We already know its responsibilities.

Now analyse each of these attributes:

* `status`
* `board`
* `players`
* `currentPlayer`
* `winningCondition`

For **each** attribute, answer:

1. **Why does `Game` need to remember this?**
2. **Could this knowledge live in another class instead? Why or why not?**
3. **Is it a simple value, a reference to another object, or a collection?**
4. **What business problem would arise if `Game` did not remember it?**

Don't think about Java or Python fields.

Think about **knowledge ownership**.

This is the last major discovery before we complete our first class. Once we've justified every piece of knowledge, the attributes in our class diagram will no longer be "fields"—they will be **business knowledge owned by the `Game`**. That is the difference between drawing a class and engineering one.

------------------------------------------------------------------------------------------------------------------------------------------------------
## My Answers
-----------------------------------------------------------------------------------------------------------------------------------------------------
Excellent. This is where we stop thinking in terms of **"attributes"** and start thinking in terms of **"knowledge ownership."**

This is exactly the mindset behind the **Information Expert (GRASP)** principle, although we're going to rediscover it ourselves instead of starting with the principle.

---

# First Principle

An object should remember something **only if that knowledge is essential for it to perform its responsibilities.**

So the question is never:

> "Should Game have a `board` field?"

The real question is:

> **"Who is the rightful owner of this knowledge?"**

Let's examine each piece of knowledge.

---

# 1. `status`

Examples:

* Not Started
* In Progress
* Draw
* Won

---

## Why does Game need to remember this?

The Game is responsible for the **lifecycle of the match**.

Questions like:

* Has the game started?
* Can another move be made?
* Has someone already won?
* Is the match over?

are all questions about the **game itself**, not the board or the players.

Therefore, Game must know its current state.

---

## Could this knowledge live somewhere else?

### Board?

No.

The Board only represents the playing surface.

It has no concept of:

* starting
* pausing
* finishing
* draw

A board can exist even before a game begins.

---

### Player?

No.

Each player only knows about themselves.

Neither player can truthfully answer:

> "Has the entire game ended?"

---

### WinningCondition?

No.

WinningCondition only evaluates whether someone has satisfied the winning rule.

It doesn't decide whether the overall game is finished.

---

### Conclusion

Game is the natural owner.

---

## Type of knowledge

Simple value.

An abstract state describing the game's lifecycle.

---

## Business problem if Game didn't remember it

Every move would require recomputing or guessing the game's lifecycle.

Worse:

The system might allow moves after the game has already ended because no single object knows that the game is finished.

---

# 2. `board`

---

## Why does Game need to remember this?

A game happens **on** a board.

Every move,

every validation,

every win check,

depends on the current board.

The Game orchestrates gameplay, so it must know **which board** the match is using.

---

## Could this knowledge live elsewhere?

### Player?

No.

Players participate in the game.

They don't own the playing surface.

---

### WinningCondition?

No.

WinningCondition temporarily examines the board.

It should not own it.

---

### Board itself?

The Board obviously knows itself.

But the question is:

Who coordinates the match?

That's Game.

Game needs a reference to the board it controls.

---

### Conclusion

Game should remember the Board.

---

## Type of knowledge

Reference to another object.

---

## Business problem if Game didn't remember it

Whenever a move occurs, the Game wouldn't know:

* where to place it
* which board to validate
* which board to evaluate for a winner

The game loses its playing surface.

---

# 3. `players`

---

## Why does Game need to remember this?

A match consists of participants.

The Game must know:

* who is playing
* whose turn comes next
* who won

Without participants, there is no game.

---

## Could this knowledge live elsewhere?

### Board?

No.

The Board stores symbols.

It doesn't manage participants.

---

### Player?

One Player cannot own the list of all players.

That creates asymmetric knowledge.

---

### WinningCondition?

No.

WinningCondition only examines board positions.

It shouldn't know who is participating.

---

### Conclusion

The Game owns participant knowledge.

---

## Type of knowledge

Collection of object references.

Usually two players, but conceptually a collection.

---

## Business problem if Game didn't remember it

The system couldn't answer:

* Who plays next?
* Who won?
* Who is allowed to make a move?

The match would have no participants.

---

# 4. `currentPlayer`

---

## Why does Game need to remember this?

Turn management is a responsibility of the Game.

Every move depends on knowing:

> "Whose turn is it?"

The current player is part of the game's evolving state.

---

## Could this knowledge live elsewhere?

### Player?

Suppose each player stores:

"I am active."

Now imagine both players accidentally think they're active.

Or neither thinks they are.

Now we have inconsistent truth.

---

### Board?

The Board manages cells.

Turns are unrelated to board structure.

---

### WinningCondition?

Turn management has nothing to do with victory evaluation.

---

### Conclusion

Game should own turn information.

---

## Type of knowledge

Reference to one Player object.

---

## Business problem if Game didn't remember it

The system couldn't validate moves.

Anyone could play at any time.

The alternating turn rule disappears.

---

# 5. `winningCondition`

---

## Why does Game need to remember this?

The Game is responsible for deciding when a match ends.

But **how** victory is determined may vary.

Examples:

* Three in a row
* Four in a row
* Five in a row
* Diagonal only
* Custom tournament rules

Game doesn't need to know every algorithm.

It only needs to know **which rule** to use.

---

## Could this knowledge live elsewhere?

### Board?

No.

The Board stores positions.

It shouldn't embed rule logic.

---

### Player?

Players don't define victory.

---

### Static utility?

Possible, but then Game loses flexibility.

Changing rules becomes harder because the decision logic is fixed elsewhere.

---

### Conclusion

Game should keep a reference to the rule it uses, while the WinningCondition object owns the evaluation logic.

---

## Type of knowledge

Reference to another object (a policy/strategy).

---

## Business problem if Game didn't remember it

The Game wouldn't know:

* which rule determines victory
* when to stop
* how to support different game variants

Changing rules would require changing the Game itself instead of swapping the rule object.

---

# A Pattern Emerges

Notice something fascinating.

| Attribute          | What Game is really remembering            |
| ------------------ | ------------------------------------------ |
| `status`           | The **state** of the match                 |
| `board`            | The **environment** where the match occurs |
| `players`          | The **participants** in the match          |
| `currentPlayer`    | The **current responsibility** to act      |
| `winningCondition` | The **policy** that decides completion     |

None of these are random pieces of data.

Each represents a distinct kind of knowledge the Game must own to fulfil its responsibilities.

---

# The Knowledge Ownership Test

Before deciding whether something belongs inside a class, ask these questions:

1. **Does this object need this knowledge to fulfil its responsibilities?**
2. **Can another object answer this question more naturally?**
3. **Would moving this knowledge create duplication or inconsistent truth?**
4. **If this object forgot this knowledge, what business capability would be lost?**

If the object is the most natural and authoritative owner of that knowledge, then it belongs there.

---

# One Sentence That Changes the Thinking

> **Attributes are not variables we add for convenience—they are pieces of business knowledge owned by the object because no other object can fulfil that responsibility more naturally or consistently.**



-------------------------------------------------------------------------------------------------------------------------------------------------------
## Answers feedback and Next
-------------------------------------------------------------------------------------------------------------------------------------------------------


Welcome back 😄 No problem at all. This is exactly a long-term journey—office work happens, and we continue **from the exact engineering point where we stopped**.

And your answer is strong. More importantly, you didn't treat attributes as:

> "These are fields inside a class."

You treated them as:

> **"These are pieces of knowledge the object must own to fulfil its responsibility."**

That is the exact mindset we wanted to build.

Let's now put your answer under the architect's microscope and make a few important refinements before we freeze the first structural representation of `Game`.

---

# 1. Your First Principle Is Correct

You started with:

> **An object should remember something only if that knowledge is essential for it to perform its responsibilities.**

Excellent.

This connects directly to our SDF:

> **What knowledge must it remember? → Attribute**

But there is an even sharper version we should add:

> **A class should own knowledge when that knowledge represents part of its state or when it must maintain a stable relationship with another object to fulfil its responsibility.**

Why add this?

Because not every attribute is the same.

Look at what we discovered:

| Attribute          | Why Game remembers it                           |
| ------------------ | ----------------------------------------------- |
| `status`           | Its own state                                   |
| `currentPlayer`    | Its own evolving state                          |
| `board`            | Stable collaboration with the match environment |
| `players`          | Stable collaboration with participants          |
| `winningCondition` | Stable collaboration with a policy              |

This is important.

`board` is not the same *kind* of knowledge as `status`.

Yet both may appear as attributes.

So:

> **An attribute does not always mean primitive data. Sometimes an attribute represents a relationship that the class must remember over time.**

That will become extremely important when we draw relationship lines.

---

# 2. Let's Validate Each Discovery

## `status` — Strongly belongs to Game

Your reasoning is exactly right.

The key question is:

> Who is the authority on whether this match can continue?

The answer is `Game`.

`Board` can tell us facts such as:

* a cell is occupied,
* positions are available,
* the grid is full.

But it cannot authoritatively say:

> "This game is currently in progress."

That is a different level of truth.

### Important distinction

A board may be **full**.

But a game may be:

* not started,
* in progress,
* won,
* drawn,
* finished.

Therefore:

> **Board state is not Game lifecycle state.**

This protects us from a common beginner mistake: deriving every business concept from the data structure that happens to contain related information.

---

# 3. `board` — Here We Reach a Subtle Point

Your conclusion is correct:

> `Game` needs to remember which `Board` belongs to this game.

But now look at the diagram problem this creates.

If we write:

```text
Game
----------------
board
```

and also draw:

```text
Game ───── Board
```

Have we communicated the same fact twice?

**Potentially, yes.**

This is our next important discovery.

An attribute such as:

```text
board
```

can be an **implementation-level representation** of a relationship.

While:

```text
Game ───── Board
```

is the **architectural representation** of that relationship.

This means we must be careful not to blindly put every object reference inside the attribute compartment *and* represent the same thing structurally.

We'll decide later what level of detail our first class diagram needs.

For now, keep this truth:

> `Game` must maintain a relationship with `Board`.

Whether we explicitly show `board: Board` inside the class box, the relationship line, or both depends on the diagram's level of abstraction.

---

# 4. `players` — Excellent Generalisation

I particularly like this part:

> "Usually two players, but conceptually a collection."

Exactly.

We are modelling the **concept**, not hardcoding today's assumption into the architecture.

But let's challenge one phrase:

> "The Game owns participant knowledge."

Correct.

But does it necessarily mean:

> **The Game owns the Player lifecycle?**

Not necessarily.

This takes us back to one of our earlier discoveries:

### Knowing an object ≠ owning its lifecycle.

`Game` must know which players participate.

But in a future application:

* users may already exist,
* users may join multiple games,
* the same player may play again tomorrow.

So the relationship may mean:

> **Game manages participation in this particular game**

rather than:

> **Game creates and destroys Player objects.**

This distinction will be extremely important when we decide between **association and composition**.

And we already discovered that lifecycle ownership must not be guessed from the existence of a reference.

---

# 5. `currentPlayer` — Excellent Single Source of Truth Reasoning

This was one of your strongest sections.

You correctly rejected this design:

```text
Player X → active = true
Player O → active = true
```

because we could get inconsistent truth.

That leads to a reusable principle:

> **When a system has one shared fact, identify the object that should be its single authority.**

For Tic-Tac-Toe:

> "Whose turn is it?"

is a fact about the **Game**, not an independent fact owned by each `Player`.

Therefore:

```text
Game → currentPlayer
```

is conceptually stronger than:

```text
Player → isMyTurn
```

because the latter distributes one global truth across multiple objects.

---

# 6. `winningCondition` — You Discovered Something Bigger

You wrote:

> Game remembers which rule it uses, while WinningCondition owns the evaluation logic.

Perfect.

Let's separate two responsibilities:

### Game decides:

> **When should I ask whether the game has ended?**

### WinningCondition decides:

> **Given the relevant game state, has someone won according to my rule?**

This is a critical boundary.

`Game` owns **game orchestration**.

`WinningCondition` owns **victory evaluation policy**.

And your future-change reasoning was excellent:

```text
Today:
3 in a row

Tomorrow:
4 in a row

Later:
Custom rule
```

We should not modify the central `Game` simply because the rule for winning changes.

So `winningCondition` represents something deeper than ordinary state.

It represents a **replaceable policy**.

We already discovered this object because the business problem demanded separation of stable orchestration from potentially changing rules.

Only later will we attach the industry names to the pattern.

---

# The Pattern You Found Is Very Important

You ended with this table:

| Attribute          | What Game remembers |
| ------------------ | ------------------- |
| `status`           | Match state         |
| `board`            | Match environment   |
| `players`          | Match participants  |
| `currentPlayer`    | Current actor       |
| `winningCondition` | Completion policy   |

This is excellent because now we can see `Game` not as a random collection of fields, but as a model of the information required to coordinate a match.

However, I would slightly refine one thing.

`Game` does not necessarily **own** every object it remembers.

So let's distinguish:

## Knowledge ownership vs lifecycle ownership

`Game` is the authority for:

* `status`
* whose turn it currently is

But it may simply maintain relationships with:

* `Board`
* `Player`
* `WinningCondition`

This gives us a more precise mental model:

```text
                    GAME

          Owns match state
                 │
        ┌────────┴────────┐
        │                 │
      status        current player


      Maintains relationships with
        │        │         │
        ▼        ▼         ▼
      Board    Players   WinningCondition
```

And this diagram reveals the next problem we need to solve.

---

# 🚨 The Next Architectural Question

We now have our first `Game` knowledge model.

But look at these two possible representations:

### Option A

```text
+---------------------------+
| Game                      |
+---------------------------+
| status                    |
| board                     |
| players                   |
| currentPlayer             |
| winningCondition          |
+---------------------------+
```

### Option B

```text
+---------------------------+
| Game                      |
+---------------------------+
| status                    |
| currentPlayer             |
+---------------------------+

       │
       ├──────── Board
       ├──────── Players
       └──────── WinningCondition
```

Both communicate some truth.

But they are **not communicating at the same abstraction level**.

And now we have reached a very important class-diagram discovery:

> **When does knowledge belong inside the class box, and when should it be represented as a relationship between classes?**

This is not merely a UML notation question.

It is an engineering modelling question.

---

# Your Next Challenge

Take these five pieces of knowledge:

* `status`
* `board`
* `players`
* `currentPlayer`
* `winningCondition`

For each one, decide:

### 1. Is this primarily:

* **internal state of Game**, or
* **a relationship Game maintains with another object**?

### 2. If we were creating a **high-level architectural class diagram**, would you show it:

* inside the `Game` box,
* as a relationship line,
* or both?

### 3. Why?

Don't worry about UML symbols yet.

We are about to discover one of the most common sources of confusion in class diagrams:

> **An object reference in code and a relationship in architecture may represent the same underlying truth—but they communicate it differently.**

Once you answer this, we will finally be ready to construct the actual first version of our `Game` representation and start connecting our system together.

