Excellent.

From this point onward, the relationships become less obvious.

The first few relationships (Game → Board, Board → Cell) were mostly about **structure**.

Now we enter relationships that are about **behavior**.

This is where many LLD interviews are won or lost.

---

# Step 4 — Discovering Relationships

# Engineering Checkpoint — Round 5

## Game ↔ Move

---

# Before Thinking About UML...

I don't want you to think:

> Does Game have a list of Moves?

Forget implementation.

Instead ask yourself:

> **Why does the business even care that Moves happened?**

That is the real question.

---

# Phase 1 — Understand the Business

Let's start with a real-world analogy.

Imagine a football match.

There are:

* Match
* Players
* Goals

Now ask yourself:

Does a Match care about Goals?

Of course.

Why?

Because Goals determine:

* current score
* winner
* match progression
* final result

Now replace those words.

Football:

```text
Match
Goal
```

Tic-Tac-Toe:

```text
Game
Move
```

Very similar.

---

## What is a Move from the Game's perspective?

Notice the wording carefully.

Earlier we asked:

> What is a Move from the Player's perspective?

Answer:

> An action performed by a Player.

Today we ask:

> What is a Move from the Game's perspective?

Different question.

Different answer.

A Move is no longer just an action.

It becomes something else.

Think carefully.

---

# Thought Experiment

Suppose we completely remove the concept of `Move`.

Our Game has only:

* Board
* Players

Whenever someone plays:

The Board immediately changes.

Question:

Can the game still work?

Think about it.

Some answers might be:

* Maybe yes...
* Maybe no...

Don't answer quickly.

Instead ask:

What capabilities disappear?

---

Imagine Product keeps adding features.

Version 1

* Basic gameplay.

Version 2

* Undo last move.

Version 3

* Replay game.

Version 4

* Show move history.

Version 5

* Export game.

Version 6

* Spectator mode.

Version 7

* AI analysis.

Question:

Which one of these becomes difficult if Moves don't exist?

Which ones still work?

---

# Engineering Discussion

Now let's challenge another assumption.

Suppose someone says:

> "Moves belong to Players."

Does that sound right?

Maybe.

Now another engineer says:

> "Moves belong to the Game."

Also sounds reasonable.

Who is correct?

Or...

Could both be partially correct for different reasons?

That's exactly the kind of ambiguity senior architects learn to resolve.

---

# Another Thought Experiment

Imagine a completed game.

We delete one Move from the middle.

What happens?

Does it affect:

* the Board?
* the winner?
* the replay?
* the history?
* the Game itself?

Think carefully.

What does that tell us about the relationship between Game and Move?

---

# Questions for You

Take your time and reason from the business, just as you've done in previous rounds.

## 1. Why do `Game` and `Move` interact from the business perspective?

Not from the Player's perspective—specifically from the **Game's** perspective.

---

## 2. Can a `Game` exist without any `Move`s?

Think about the moment immediately after a game starts.

---

## 3. Can a `Move` exist without a `Game`?

If someone simply says:

> "Move #5"

Does that have business meaning?

---

## 4. Who owns the lifecycle?

Does the Game own the Moves?

Or does it merely reference them?

Or is there another way to think about it?

Don't rush to answer based on previous composition examples.

---

## 5. If a `Game` is deleted, what should happen to its `Move`s?

Should they disappear?

Should they remain?

Why?

---

## 6. If one `Move` is deleted from the middle of the game history, what business consequences follow?

Think beyond data deletion.

Think about the rules of Tic-Tac-Toe.

---

## 7. Is this relationship about:

* Ownership?
* History?
* State progression?
* Something else?

Or perhaps a combination?

---

# One Hint (Not the Answer)

Notice the progression we've built so far:

| Relationship  | Business Question         |
| ------------- | ------------------------- |
| Game → Board  | Where is the game played? |
| Board → Cell  | What makes up the board?  |
| Game ↔ Player | Who participates?         |
| Player ↔ Move | Who performed the action? |
| Game ↔ Move   | **?**                     |

The last row intentionally doesn't ask:

> "Who made the move?"

You've already answered that.

Instead, ask yourself:

> **"Why does the Game care that a Move occurred?"**

That single change in perspective is the key to discovering this relationship.

---

## 🎯 Interview Thinking

A common interview trap is to answer every relationship from the same viewpoint.

Strong candidates change perspective.

For `Move`:

* From the **Player's** viewpoint: it is an action they performed.
* From the **Game's** viewpoint: it has a completely different meaning.

The ability to shift viewpoints is what interviewers often look for when evaluating object-oriented design maturity.

I'm looking forward to your reasoning. Don't worry about naming the UML relationship yet—derive it from the business, just as you've been doing.


## My Answers

This is my favorite checkpoint so far because it forces us to think beyond "who references whom" and instead ask:

> **What role does this concept play in the business?**

Here's how I would answer after applying the same reasoning framework.

---

# Engineering Checkpoint — Game ↔ Move

## 1. Why do Game and Move interact from the business perspective?

From the business perspective, a **Game** progresses through a sequence of **Moves**.

A move is not just an action—it changes the state of the game.

Every valid move:

* updates the board,
* changes whose turn it is,
* may produce a winner,
* may produce a draw,
* or allows the game to continue.

Without moves, the game cannot progress.

So, the Game interacts with Moves because **Moves represent the progression of the Game**.

---

## 2. Can a Game exist without any Moves?

**Yes.**

Immediately after a game starts:

* the board exists,
* players exist,
* the game is in progress (or ready to start),
* but no moves have been made yet.

The Game is still a valid business concept.

A game begins before the first move.

---

## 3. Can a Move exist without a Game?

**No.**

If someone says:

> "Move #5"

the first question is:

> **"Move #5 of which Game?"**

A move has meaning only within the context of a specific game.

The same position `(1,1)` in two different games represents two different moves.

A Move is always part of one Game's history.

---

## 4. Who owns the lifecycle?

This is the subtle part.

I would say:

> **The Game owns the lifecycle of its Moves.**

Here's why:

* A Move is created only because a Game is being played.
* A Move cannot move from one Game to another.
* A Move has no purpose outside its Game.
* The sequence of Moves belongs to that Game.

Unlike Players, Moves are **not independent business concepts** that can participate in multiple Games.

They exist only as part of one Game's history.

---

## 5. If a Game is deleted, what should happen to its Moves?

The Moves should also disappear.

The move history belongs to that Game.

Once the Game no longer exists, its history has no business meaning.

Keeping the Moves without the Game would leave orphaned business records.

---

## 6. If one Move is deleted from the middle of the game history, what business consequences follow?

This is much more serious than simply removing one record.

Deleting a move from the middle of the game changes the entire progression of the game.

For example:

```text
Move 1 → X
Move 2 → O
Move 3 → X
Move 4 → O
Move 5 → X (Winning move)
```

If Move 3 is removed:

* the board state changes,
* later moves may no longer be valid,
* the winner may change,
* the turn sequence becomes incorrect,
* the replay becomes inconsistent.

So a Move is not an isolated event. Every move depends on the moves before it and influences the moves after it.

The move history forms a consistent sequence.

---

## 7. Is this relationship about ownership, history, state progression, or something else?

I think it's a combination, but the strongest business interpretation is:

### Ownership

The Game owns its move history.

---

### History

The Moves collectively record everything that happened during the Game.

---

### State Progression

Each Move transforms one valid game state into the next.

Without Moves, there is no progression from:

* empty board,
* to partially filled board,
* to final result.

So Moves are both:

* **the history of the Game**, and
* **the mechanism by which the Game progresses**.

---

# My Final Reasoning

| Question                             | Answer                                              |
| ------------------------------------ | --------------------------------------------------- |
| Why do they interact?                | Moves drive and record the progression of the Game. |
| Can a Game exist without Moves?      | ✅ Yes, before the first move.                       |
| Can a Move exist without a Game?     | ❌ No. A move only has meaning within a Game.        |
| Who owns the lifecycle?              | ✅ Game.                                             |
| If the Game is deleted?              | Its Moves should also be deleted.                   |
| What happens if one Move is removed? | The game's history and state become inconsistent.   |
| Nature of the relationship?          | Ownership + History + State Progression.            |

---

# One Sentence That Changed My Thinking 💡

> **A Move is not just something that happened in a Game—it is the sequence of Moves that *becomes* the Game's history and drives its state from beginning to end.**

---

# Mentor's Feedback

This relationship is richer than the others because it carries **three responsibilities at once**:

| Relationship  | Primary Meaning                         |
| ------------- | --------------------------------------- |
| Game ↔ Board  | Structure                               |
| Board ↔ Cell  | Composition                             |
| Game ↔ Player | Participation                           |
| Game ↔ Move   | History + State Progression + Lifecycle |

One subtle distinction is worth remembering. A `Board` represents the **current state** of the game at any moment. A collection of `Move`s represents **how the game reached that state**. Some implementations may never store move history and instead update only the board. Others (for replay, undo, or analytics) will treat move history as a first-class part of the domain. That's why requirements matter: the business decides whether moves are transient actions or persistent historical records.


## Answers Feedback andext
--------------------------------------

This is outstanding.

And today we're going to discover something that very few LLD tutorials ever teach.

You arrived at the correct conclusion, but there is a deeper architectural lesson hidden inside it.

This lesson will fundamentally change how you model systems like:

* Banking
* E-commerce
* Ride Sharing
* Workflow Engines
* Order Processing
* Event Sourcing

Let's unpack it.

---

# Phase 1 — Business Review

## Your first sentence

> A Game progresses through a sequence of Moves.

This is the most important sentence in your answer.

Notice what happened.

Earlier you described relationships like this:

```
Board
consists of
Cells
```

or

```
Player
participates in
Game
```

Now you've changed the verb.

You said:

> **Game progresses through Moves.**

That verb is different.

It doesn't describe **structure**.

It describes **time**.

And that's a huge leap in thinking.

---

## A Pattern You've Discovered

Let's compare all five relationships.

| Relationship  | Business Verb      | Dimension     |
| ------------- | ------------------ | ------------- |
| Board → Cell  | consists of        | Structure     |
| Game → Board  | owns               | Structure     |
| Game ↔ Player | participates with  | Collaboration |
| Player → Move | performs           | Action        |
| Game ↔ Move   | progresses through | **Time**      |

Did you notice?

This is the first relationship where **time** becomes part of the business meaning.

That makes it fundamentally different from everything we've discussed so far.

---

# Phase 2 — Engineering Discussion

Now I want to challenge one thing.

Not because it's wrong.

Because we can make it even more precise.

---

## You wrote

> Game owns the lifecycle of Moves.

I agree.

But...

Let's ask a strange question.

### What exactly does the Game own?

Is it...

```
Move
Move
Move
Move
```

Or is it...

```
Game Timeline

Move1
↓

Move2
↓

Move3
↓

Move4
```

Those are not the same thing.

---

## Why This Matters

Imagine I ask you:

> Tell me about Move #4.

You cannot answer without knowing:

* what happened before
* whose turn it was
* what the board looked like
* whether the game had already ended

A Move doesn't just belong to a Game.

A Move belongs to a **sequence**.

That sequence is where the real business meaning comes from.

---

### Senior Engineering Principle #9

> **Sometimes the relationship isn't just between objects—it is between an object and an ordered history.**

That distinction appears everywhere.

---

## Banking

A transaction means very little alone.

Its meaning depends on:

```
Opening Balance

↓

Transaction 1

↓

Transaction 2

↓

Transaction 3

↓

Current Balance
```

---

## Git

A commit alone isn't enough.

It belongs to a commit history.

---

## Chess

A move belongs to the sequence of moves.

---

## Ride Sharing

Trip Events

Driver Accepted

↓

Driver Arrived

↓

Ride Started

↓

Ride Finished

The order creates meaning.

---

# Your Sixth Answer Was Excellent

You wrote:

> Every move depends on the moves before it.

This is incredibly important.

Notice what you're really saying.

A Move doesn't merely reference previous moves.

The **business validity** of a Move depends on previous Moves.

For example:

```
Move 7
```

cannot exist unless

```
Move 6
```

already happened.

That's not an implementation dependency.

It's a business dependency.

That difference matters.

---

### Engineering Principle #10

> **Business dependencies are stronger than code dependencies.**

Code can compile without previous moves.

The business cannot.

---

# The Biggest Insight of Today

I want to introduce a concept that architects use frequently.

## State Transition

Earlier you said:

> A Move changes the state of the Game.

Exactly.

Let's visualize it.

```
Initial State

↓

Move

↓

New State

↓

Move

↓

New State

↓

Move

↓

Winner
```

Notice something.

The Game is not static.

It is continuously transforming.

Each Move is not merely data.

It is the **reason the Game changes state**.

This is a profound shift in perspective.

---

## Objects vs State Changes

Earlier relationships were about objects.

Now we're talking about transitions.

Many enterprise systems are actually modeled around transitions.

Examples:

### Order

```
Created

↓

Paid

↓

Packed

↓

Shipped

↓

Delivered
```

Each event changes the state.

---

### Bank Account

```
Balance

↓

Deposit

↓

New Balance

↓

Withdrawal

↓

New Balance
```

Again...

Events transform state.

---

### Workflow

```
Draft

↓

Submitted

↓

Approved

↓

Published
```

Same pattern.

You're beginning to see a universal design pattern that extends far beyond Tic-Tac-Toe.

---

# Phase 3 — Final Engineering Decision

Let's summarize the relationship.

### Game ↔ Move

Business meaning:

> A Game progresses through an ordered sequence of Moves.

Ownership:

* Yes, the Game owns its move history.

Lifecycle:

* Dependent.
* A Move has no business meaning outside its Game.

Historical meaning:

* A Move records what happened.

Behavioral meaning:

* A Move transitions the Game from one valid state to the next.

Relationship category:

> **Composition with historical/state-transition semantics.**

Notice that we're not saying:

> "It's just composition."

We're qualifying *why* it is composition in this domain.

That's the level of precision senior architects aim for.

---

# Something Beautiful Has Emerged

Let's look at the relationships one last time.

| Relationship  | Primary Meaning            |
| ------------- | -------------------------- |
| Game → Board  | Ownership                  |
| Board → Cell  | Composition                |
| Game ↔ Player | Participation              |
| Player → Move | Authorship                 |
| Game → Move   | History + State Transition |

This isn't just a list.

It's becoming a **relationship vocabulary**.

And that vocabulary is reusable.

---

# Phase 4 — Reflection

## Biggest Engineering Lesson

**Two composition relationships can look identical in UML yet represent very different business meanings.**

* `Game → Board` is about physical structure.
* `Game → Move` is about temporal progression and history.

The UML symbol may be the same, but the business semantics are different.

That's why architects never stop at the diagram—they explain the meaning behind it.

---

## Common Interview Mistakes

* Treating all composition relationships as identical.
* Ignoring that order can carry business meaning.
* Modeling a history as an unordered collection.
* Focusing on stored data instead of state transitions.
* Explaining relationships only in terms of class fields instead of business behavior.

---

## One Sentence That Changed My Thinking

> **A system is often defined not only by the objects it contains, but by the sequence of events that transform those objects over time.**

---

# 🎓 Mentor Reflection — A Bigger Milestone

I want to pause for a moment because something important has happened across Step 4.

When we started, I gave you a **Relationship Discovery Framework** with seven guiding questions. The goal was never for you to memorize those questions—it was to internalize the way of thinking behind them.

Today, I barely needed to refer to that framework.

Why?

Because your answers now naturally include:

* Business purpose
* Context
* Lifecycle
* Ownership
* Identity
* Collaboration
* History
* State progression
* Future implications

You're no longer filling out a checklist.

You're conducting a design review.

That's a significant shift.

---

# Before We Continue with More Relationships

I think this is the perfect point to **pause and consolidate** before moving on.

So far we've discovered **five distinct relationship patterns**:

1. **Whole–Part (Composition)** — `Game → Board`
2. **Whole–Part (Composition)** — `Board → Cell`
3. **Participation (Association)** — `Game ↔ Player`
4. **Authorship (Association)** — `Player → Move`
5. **History & State Transition (Composition with temporal meaning)** — `Game → Move`

Notice what we've actually built:

We haven't just solved Tic-Tac-Toe.

We've started building a **mental catalog of relationship archetypes** that you'll recognize in almost every future case study—whether it's a Parking Lot, Splitwise, BookMyShow, Hotel Management, Banking, or Ride Sharing.

And that's exactly the long-term objective you set at the beginning of this journey.
