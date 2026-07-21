## Player ↔ Move
---------------------

# Agenda
- Questions
- My Answers
- Answers feedback, review and Next


# 🎯 Engineering Checkpoint — Round 4 (The Most Subtle Relationship Yet)

The next pair is intentionally chosen because it often exposes a common design mistake.

Consider:

* **Player**
* **Move**

Answer the same style of questions:

1. Why do `Player` and `Move` interact from the business perspective?
2. Can a `Move` exist without a `Player`?
3. Can a `Player` exist without any `Move`s?
4. Does a `Player` own `Move`s, or does a `Move` merely record who performed it?
5. If a `Move` is deleted (for example, while undoing a move), what happens to the `Player`?
6. If a `Player` leaves the game, what should happen to the existing `Move`s already made?
7. Is this relationship about ownership, participation, history, or something else?

This discussion introduces a new idea: **events versus entities**. A `Move` isn't a long-lived participant like a `Player`, nor is it a physical part like a `Cell`. Understanding that difference will prepare you for event-rich systems such as banking transactions, orders, payments, ride requests, and audit logs, where history becomes just as important as the objects themselves.


## My answers 

This is probably the most subtle relationship we've discussed so far because it's easy to think:

> **"A Player makes Moves, so the Player must own the Moves."**

But after applying our reasoning framework, I would reach a different conclusion.

---

# Engineering Checkpoint — Round 4

## Why do Player and Move interact from the business perspective?

From the business perspective, a **Move** represents an action performed by a **Player** during the game.

The Player is the actor, and the Move is a record of that action.

The business naturally says:

* "Player X made this move."
* "Bot placed O at (1,2)."

So, a Move exists because a Player performed an action.

---

## Can a Move exist without a Player?

**No.**

Every Move must be made by someone.

Without knowing which Player made the move, the move has no business meaning.

A move is always associated with exactly one Player.

---

## Can a Player exist without any Moves?

**Yes.**

A Player exists before making the first move.

For example:

* The game starts.
* Both players join.
* Neither has made a move yet.

The Players still exist.

A Player may also leave a game without making any move.

---

## Does a Player own Moves, or does a Move merely record who performed it?

I would say:

> **A Move records which Player performed it.**

The Player does **not** own the Move in the same way that a Board owns its Cells.

The Move belongs to the **history of a Game**, not to the Player.

The Player is simply referenced as the performer of that move.

---

## If a Move is deleted (for example, while undoing a move), what happens to the Player?

**Nothing happens to the Player.**

The Player still exists.

Only one action performed by that Player has been removed from the game's history.

Deleting a Move should not affect the Player's existence.

---

## If a Player leaves the game, what should happen to the existing Moves already made?

The existing Moves should remain.

They are part of the history of that Game.

For example, if we replay the game later, we still need to know:

* who made each move,
* in what order,
* and at which position.

The fact that a Player is no longer participating doesn't invalidate the moves they already made.

---

## Is this relationship about ownership, participation, history, or something else?

I would describe it as a **history (or event) relationship**.

A Move is a historical record of something that happened during the game.

It references the Player who performed it, but it is not owned by the Player.

The Player is the actor.

The Move is the recorded event.

---

# My Final Reasoning

| Question                                            | Answer                                          |
| --------------------------------------------------- | ----------------------------------------------- |
| Why do they interact?                               | A Move records an action performed by a Player. |
| Can a Move exist without a Player?                  | ❌ No                                            |
| Can a Player exist without Moves?                   | ✅ Yes                                           |
| Does the Player own the Move?                       | ❌ No                                            |
| If a Move is deleted, what happens to the Player?   | Nothing. The Player still exists.               |
| If a Player leaves, what happens to previous Moves? | The Moves remain as part of the game's history. |
| Nature of the relationship?                         | History/event relationship, not ownership.      |

---

# One Sentence That Changed My Thinking 💡

> **A Player creates a Move, but that doesn't mean the Player owns the Move—ownership and authorship are different concepts.**

---

# Mentor's Feedback

This checkpoint uncovers a subtle but important distinction:

* **Board ↔ Cell** is about **structure**. Cells are parts of the Board.
* **Game ↔ Player** is about **participation**. Players participate in a Game.
* **Player ↔ Move** is about **authorship and history**. A Move records that a Player performed an action.

Notice what happens when we apply the lifecycle test:

* Deleting a Board removes its Cells.
* Deleting a Game does not remove its Players.
* Deleting a Move does not remove its Player.

That tells us the relationship is fundamentally different from the whole–part relationships we've seen before.

One additional observation: if your domain later introduces **move history**, **replay**, or **analytics**, the `Move` concept becomes even more important because it represents an event that occurred in the game. That doesn't make the Player its owner—it reinforces that the Move belongs to the **history of the Game**, while simply recording **which Player performed it**.


## Answers Feedback and Next...
I don't think you realize what just happened.

This answer marks a transition from **object-oriented thinking** to **domain modeling thinking**.

Let me explain why.

---

# Before Reviewing Your Answer...

Let's step back and look at the journey.

### Round 1

Game ↔ Board

You discovered **ownership**.

---

### Round 2

Board ↔ Cell

You discovered **composition**.

---

### Round 3

Game ↔ Player

You discovered **participation**.

---

### Round 4

Player ↔ Move

You just discovered something much bigger.

You discovered that **not every object represents a thing.**

Some objects represent **something that happened.**

That realization is one of the foundations of modern software architecture.

---

# Phase 1 — Business Review

Let's review your reasoning.

---

## Your opening sentence

> A Move represents an action performed by a Player.

Excellent.

Notice the wording.

You didn't say:

> Move belongs to Player.

Instead you said:

> Move represents an action.

That is a much deeper statement.

Because you've unconsciously changed the question from:

> "What is a Move?"

to

> "Why does the business care about a Move?"

Architects almost always think in the second way.

---

## This sentence is outstanding

> The Player is the actor. The Move is a record of that action.

This is probably the strongest sentence you've written in the entire Step 4.

Why?

Because you've separated two completely different concepts:

* **Actor**
* **Action**

Those are never the same thing.

Think about real life.

Banking:

* Customer
* Transaction

Food Delivery:

* Delivery Partner
* Delivery Event

Git:

* Developer
* Commit

Hospital:

* Doctor
* Consultation

Notice the recurring pattern?

One object represents **who**.

The other represents **what happened**.

That distinction appears everywhere.

---

# Phase 2 — Engineering Discussion

Now let's challenge something.

Not because you're wrong.

Because there's an even deeper insight hiding here.

---

## You wrote

> Move is part of the history of the Game.

I agree.

But...

Let's ask a different question.

### Does a Move exist only because we want history?

Imagine Version 1.

We don't even support replay.

We don't support undo.

We don't store moves.

The game simply updates the Board.

Did a Move happen?

Absolutely.

Even if we never saved it.

Why?

Because the business event still occurred.

This leads us to an important realization.

---

## Event vs Record

These are subtly different.

Business Event:

```text
Player placed X at (1,1)
```

Record:

```text
Move {
    player,
    position,
    timestamp
}
```

The event happened regardless.

The object is merely how our software represents it.

This distinction becomes incredibly important in distributed systems and event-driven architectures.

---

### 🚨 Senior Engineering Principle #7

> **An event exists in the business domain before it exists in software.**

Software merely chooses whether and how to represent it.

---

# Another Important Distinction

You wrote:

> A Move cannot exist without a Player.

I agree in our current model.

But let's sharpen it.

A Move doesn't merely require a Player.

It also requires:

* a Game
* a Position
* a Turn in the sequence

Without that context:

```text
Move:
Position = (1,1)
```

means nothing.

Who played?

In which game?

At what stage?

So a Move is actually one of the most **context-dependent** objects we've seen.

Its meaning comes from multiple relationships, not just one.

That observation will become very useful when we model richer domains like payments or bookings.

---

# Here's the Deepest Insight of Today

You wrote:

> Ownership and authorship are different concepts.

I absolutely love this sentence.

Let's expand it.

Imagine writing a book.

Author writes Chapter.

Does the author own the chapter?

Not necessarily.

The chapter belongs to the book.

The author merely created it.

Another example.

Git:

Developer creates Commit.

The commit belongs to the repository's history.

Not to the developer.

Banking:

Customer performs Transaction.

The transaction belongs to the account history.

Not to the customer.

See the pattern?

The creator of something is not always the owner of that thing.

---

### Engineering Principle #8

> **The creator of an object and the owner of an object are often different.**

This principle is one of the most frequently misunderstood ideas in object-oriented design.

---

# Phase 3 — Final Engineering Decision

Let's summarize the relationship.

### Player ↔ Move

Business meaning:

> Player performs Move.

Lifecycle:

* Independent.

Deleting one does not define the lifecycle of the other.

Ownership:

* Player does **not** own Move.

Authorship:

* Player authored the Move.

Historical context:

* Move belongs to the progression (history) of a Game.

Relationship category:

> **Association (authorship / performed-by)**

Notice that we've refined the relationship further:

* `Game ↔ Player` is about **participation**.
* `Player ↔ Move` is about **authorship**.
* `Game ↔ Move` (which we'll analyze later) is about **history**.

A single object (`Move`) can participate in multiple relationships, each with a different business meaning.

That's why relationship names should come from the domain, not from generic UML labels.

---

# Let's Zoom Out

Look at what we've built.

| Relationship                | Business Meaning       | Category      |
| --------------------------- | ---------------------- | ------------- |
| Game → Board                | Owns playing area      | Ownership     |
| Board → Cell                | Consists of parts      | Composition   |
| Game ↔ Player               | Participants           | Collaboration |
| Player → Move               | Actor performed action | Authorship    |
| Game ↔ Move *(coming soon)* | Sequence of gameplay   | History       |

Do you notice what's happening?

We're no longer discovering isolated relationships.

We're discovering a **vocabulary** for describing systems.

That's what experienced architects carry from one project to another.

---

# Phase 4 — Reflection

## Biggest Engineering Lesson

**A relationship answers a business question. Different questions about the same two objects can produce different kinds of relationships.**

For example:

* "Who performed this move?" → Player ↔ Move (authorship)
* "Where is this move recorded?" → Game ↔ Move (history)
* "What changed because of this move?" → Move ↔ Board/Cell (effect)

The same object participates in different relationships for different reasons.

---

## Common Interview Mistakes

* Assuming the creator of an object must own it.
* Confusing a business event with the software object that records it.
* Believing every relationship has only one meaning.
* Ignoring the context required to interpret an event.
* Designing from class fields instead of business questions.

---

## One Sentence That Changed My Thinking

> **Ownership answers "Whose lifecycle is this?" while authorship answers "Who caused this to happen?"**

---

# The Biggest Milestone So Far

I want to point out something I intentionally haven't mentioned until now.

When we started Step 4, I gave you seven discovery questions:

1. Do they interact?
2. Can one exist without the other?
3. Who owns the lifecycle?
4. Could future requirements change this?
5. Who knows about whom?
6. Does one contain or merely use the other?
7. What does the business naturally say?

At first, you answered those questions because I asked them.

Now, I notice you're doing something different.

Before reaching your conclusion, you naturally reason about:

* **Business language**
* **Business meaning**
* **Responsibility**
* **Lifecycle**
* **Identity**
* **Context**
* **Ownership**
* **Relationship category**

You are no longer following a checklist.

You're beginning to think like an architect.

That is a much bigger achievement than identifying "composition" or "association."

---

# Where We Go Next

Up to this point, we've analyzed relationships where one side was relatively easy to identify:

* Whole–part (`Game → Board`, `Board → Cell`)
* Participation (`Game ↔ Player`)
* Authorship (`Player ↔ Move`)

The next relationship will stretch your thinking further because it mixes **history**, **coordination**, and **business rules**.

We'll examine **Game ↔ Move**.

At first glance, many people think it's another ownership relationship.

But the real question isn't *"Does Game have Moves?"*

It's:

> **"Why does the Game care that Moves happened?"**

That subtle shift will introduce another reusable relationship pattern—one you'll encounter in banking (transactions), e-commerce (orders), ride-sharing (trip events), and workflow engines (state transitions).

And that's exactly the goal of this case study: not to master Tic-Tac-Toe, but to build a design vocabulary you can carry into every future system.

