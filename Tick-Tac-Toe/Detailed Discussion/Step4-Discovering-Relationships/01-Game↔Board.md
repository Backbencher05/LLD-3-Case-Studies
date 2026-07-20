# Game ↔ Board

# Agenda
- Questions
- My Answers
- Answers feedback, review and Next

## 🎯 Engineering Checkpoint (Your Turn)

Let's begin discovering relationships the same way a senior architect would—through reasoning, not diagrams.

## Question 1

Look at these two domain objects:

* **Game**
* **Board**

Without thinking about Java classes or UML, answer from the **business perspective**:

1. Why do these two concepts interact?
2. Could a `Game` exist without a `Board` in our current Tic-Tac-Toe scope?
3. Could a `Board` exist without a `Game`?
4. Which one is responsible for the other's lifecycle?
5. If a game ends and is deleted, what should happen to the board?
6. Based on that reasoning, what kind of relationship do you think they should have?

Don't worry about the UML name (association, composition, aggregation, etc.) yet. I want to understand **your reasoning first**.

Once you've answered, we'll review it together and only then introduce the formal relationship type. That way, you'll learn to derive design from business reality instead of memorizing UML terminology.


# My Answer

Excellent. This is exactly how a senior architect thinks—**before naming the relationship, they understand why the relationship exists.**

Here's how I would answer.

---

# Engineering Checkpoint — Discovering Relationships

## Question 1

### Why do Game and Board interact?

From the business perspective, a **Game** is the complete experience of playing Tic-Tac-Toe, while the **Board** is the place where that game is played.

The Game needs the Board because every move, validation, and winning condition depends on the current state of the Board.

The Board, on the other hand, doesn't make decisions on its own. It simply represents the playing area and maintains its current state.

So, the Game interacts with the Board because the Board is an essential part of how the Game progresses.

---

## Could a Game exist without a Board in our current Tic-Tac-Toe scope?

**No.**

A Tic-Tac-Toe game cannot start or continue without a board.

Without a board:

* Players cannot make moves.
* There is no game state.
* Winning cannot be determined.
* Draws cannot be determined.

A Game without a Board is an incomplete concept in this domain.

---

## Could a Board exist without a Game?

In our current scope, **No.**

The Board has no independent business purpose.

The business never says:

> "Create a Board."

Instead, it says:

> "Start a new Game."

When a game starts, a board is created as part of that game.

The Board exists only to support a specific Game.

---

## Which one is responsible for the other's lifecycle?

The **Game** is responsible for the **Board's lifecycle**.

When a new Game is created:

* A new Board is created.

During the Game:

* The Board is updated after each move.

When the Game ends:

* The Board is no longer needed.

The Board never manages the Game.

The Game owns the Board.

---

## If a Game ends and is deleted, what should happen to the Board?

The Board should also be removed.

Since the Board has no independent existence in our current business domain, there is no reason to keep it once the Game no longer exists.

Deleting the Game should naturally delete its Board as well.

---

## Based on that reasoning, what kind of relationship do you think they should have?

Based on the business reasoning, I would say:

* The Board is an integral part of the Game.
* The Board cannot exist independently in this domain.
* The Game owns the Board and controls its lifecycle.

This is a **strong ownership relationship**, where the Board is part of the Game rather than an independent object shared with other Games.

I won't name the UML relationship yet, but the characteristics strongly suggest a relationship where one object completely owns the lifecycle of the other.

---

# My Final Reasoning

| Question                               | Answer                                                          |
| -------------------------------------- | --------------------------------------------------------------- |
| Why do they interact?                  | The Game uses the Board to represent and manage gameplay.       |
| Can a Game exist without a Board?      | ❌ No                                                            |
| Can a Board exist without a Game?      | ❌ No (in our current scope)                                     |
| Who owns the lifecycle?                | ✅ Game                                                          |
| What happens when the Game is deleted? | The Board should also be deleted.                               |
| Nature of the relationship?            | Strong ownership; the Board is an inseparable part of the Game. |

---

# One Sentence That Changed My Thinking 💡

> **Relationships are discovered by asking who owns whom, who depends on whom, and whose lifecycle controls the other—not by memorizing UML symbols.**

---

# Mentor's Feedback

This is exactly the mindset I want you to develop.

Notice that we **never started with**:

> "Game has a Board."

Instead, we asked:

1. **Why do they interact?**
2. **Can one exist without the other?**
3. **Who owns the lifecycle?**
4. **What happens if one disappears?**

Only after answering those business questions do we arrive at the relationship.

That's the difference between **drawing diagrams** and **discovering relationships**. The diagram is just a way to communicate the reasoning you've already done.


# Mentor feedback and Next
-------------------------------

This is genuinely excellent.

Not because you arrived at the "correct" relationship, but because I can see a change in **how you're reasoning**.

A few weeks ago, your answer might have been:

> "Game has a Board."

Today your answer is:

* Why they interact
* Why one cannot exist without the other
* Who owns the lifecycle
* What happens when one is deleted
* What the business actually says
* Why the ownership is strong

That is exactly the progression from thinking about **objects** to thinking about **systems**.

Now let's review this as if we were in a senior design review.

---

# Phase 1 — Business Review

Let's first ignore UML completely.

I want to evaluate only your reasoning.

---

## Your first statement

> The Game needs the Board because every move, validation, and winning condition depends on the current state of the Board.

This is very good.

Notice something subtle.

You didn't say:

> "Game contains Board."

You explained **why**.

Senior engineers almost always explain *why* before *what*.

That habit becomes extremely valuable during interviews.

---

## Your second statement

> The Board doesn't make decisions on its own.

This is another important observation.

Many people think relationships are only about ownership.

They are not.

They're also about **responsibility**.

The Board is responsible for representing state.

The Game is responsible for orchestrating gameplay.

Those responsibilities naturally create the relationship.

---

## Your third statement

> Business never says "Create a Board."

I absolutely love this sentence.

This is exactly how domain-driven design encourages us to think.

The business language is:

> Start a Game.

Not

> Instantiate Board.

That tells us something important.

The Board is not a top-level business concept.

It is part of another concept.

That is powerful reasoning.

---

# A Small Refinement

There is one place where I want to make your thinking even stronger.

You wrote:

> The Board has no independent business purpose.

Instead, I'd phrase it as:

> **In our current bounded context, the Board has no independent lifecycle.**

Why is this wording stronger?

Because "purpose" can change in another system.

Imagine tomorrow we build:

* Board Editor
* Puzzle Generator
* Saved Board Analyzer
* AI Training Dataset

Now Boards suddenly *do* have an independent purpose.

The important point isn't purpose.

It's lifecycle.

Architects tend to reason in terms of lifecycle because that's what drives design decisions.

---

# Phase 2 — Engineering Discussion

Now let's challenge one of your assumptions.

This is exactly what happens in architecture reviews.

You said:

> A Board cannot exist without a Game.

I'll ask you something uncomfortable.

## Thought Experiment

Suppose tomorrow Product says:

> "Allow players to save unfinished games."

Now what happens?

The Game object is gone from memory.

But the Board still exists in storage.

Did we just prove your statement wrong?

At first glance...

It seems so.

But let's think carefully.

---

## What actually changed?

Did the business suddenly say:

> Boards are independent entities.

No.

It said:

> Games can now be resumed.

The Board is still owned by the Game.

It is simply being persisted as part of the Game's state.

So the ownership hasn't changed.

Only the storage strategy has.

This distinction is crucial.

---

### 🚨 Senior Engineering Principle #2

> **Persistence does not define ownership. Lifecycle does.**

This is one of those principles you'll reuse in almost every LLD and HLD discussion.

Many engineers mistakenly infer ownership from how data is stored.

Architects separate **domain relationships** from **storage mechanics**.

---

## Another Thought Experiment

Suppose we allow:

* Different board sizes
* Custom board themes
* Hexagonal boards
* Circular boards

Would `Board` suddenly become independent?

Not necessarily.

Those are additional properties of the Board, not evidence that it should outlive the Game or be shared across Games.

Again, the key question remains:

> **Who governs the Board's lifecycle?**

---

# Phase 3 — Formal Engineering Decision

Now that we've reasoned from the business and challenged our assumptions, we can finally introduce the formal relationship.

Your description matches **Composition**.

In UML and object-oriented design, composition is used when:

* The whole owns the part.
* The part has no independent lifecycle within the domain.
* Destroying the whole destroys the part.

For our current scope:

```
Game
 └── Board
```

Read it in business language:

> **A Game is composed of a Board.**

Not:

> A Game uses a Board.

Not:

> A Game references a Board.

But:

> **A Board is part of a Game.**

Notice how the UML term comes **after** the reasoning, not before it.

That's the habit we want to build.

---

# Why Not Aggregation?

A common alternative is aggregation, where the "whole" groups objects that can exist independently.

Think of a library and books:

* A library may own a collection of books.
* But a book can exist outside a particular library.

In our current Tic-Tac-Toe domain, that isn't true for the Board.

A Board isn't something we create, share, or move between Games.

So aggregation would communicate the wrong business meaning.

---

# Phase 4 — Reflection

## Biggest Engineering Lesson

**Ownership is determined by lifecycle, not by where data is stored or how classes reference each other.**

---

## Common Interview Mistakes

* Saying "Game has a Board" without explaining *why*.
* Choosing a relationship based on UML terminology instead of business rules.
* Confusing persistence with ownership.
* Assuming any object with configurable properties must become independent.
* Ignoring lifecycle when deciding relationships.

---

## One Sentence That Changed My Thinking

> **A relationship is strong not because two objects are always together, but because one object is responsible for the other's existence.**

---

# One More Observation About Your Growth

I noticed something in your answer that makes me very happy as a mentor.

Earlier in our journey, you often concluded with the design decision first.

Now your answer flows like this:

1. Business understanding
2. Constraints
3. Lifecycle
4. Ownership
5. Final relationship

That's the same order many experienced architects naturally follow.

You're beginning to derive design from reasoning instead of matching patterns you've seen before.

---

# 🎯 Engineering Checkpoint — Round 2

Now let's examine a relationship that is much more subtle than `Game ↔ Board`.

Consider these two domain objects:

* **Board**
* **Cell**

Answer the same style of questions:

1. Why do `Board` and `Cell` interact from the business perspective?
2. Can a `Board` exist without `Cell`s in our current scope?
3. Can a `Cell` exist without a `Board`?
4. Who owns the lifecycle?
5. If the `Board` is deleted, what should happen to its `Cell`s?
6. Is every `Cell` permanently tied to exactly one `Board`, or could future requirements reasonably change that?
7. Based on your reasoning, what kind of relationship do you think they should have?

This pair is intentionally more interesting than `Game ↔ Board`. The discussion will help us distinguish **physical parts of a structure** from **logical participants in a process**, a distinction you'll reuse in designs like Parking Lot, Chess, Hotel Management, and many others.

