Exactly.

And I want to pause on that observation because it's one of the core philosophies of this entire mentorship.

You said:

> **Till now we haven't touched any programming language because till now it wasn't required. In future we'll see it in terms of Python.**

That is **exactly** the transition I wanted us to make.

In fact, I'd go one step further.

> **Programming languages are implementation tools. Software design is an engineering discipline.**

Those are related, but they are not the same.

---

# Why We Delayed Python

Most learning paths look like this:

```text
Python Classes

↓

Inheritance

↓

Polymorphism

↓

Design Patterns

↓

LLD
```

Our journey has been the reverse.

```text
Business Problem

↓

Business Model

↓

Responsibilities

↓

Collaboration

↓

Behaviour

↓

Operations

↓

(Coming Soon)

Public Behaviour

↓

Method Discovery

↓

Python Classes
```

Notice something.

By the time we write our **first Python class**, we should already know:

* Why it exists.
* What responsibility it owns.
* What behaviours it must provide.
* Which operations are internal.
* Which collaborators it needs.
* What promises it makes.

Python won't tell us any of that.

Python will only give us a way to express it.

---

# Think About This

Suppose I suddenly asked you to implement the `Board` class today.

Six months ago, you might have started with:

```python
class Board:
    pass
```

Then you'd ask:

> "What methods should I add?"

Today, I think your first question would be:

> "What responsibility does the Board own?"

That's a completely different starting point.

The code becomes almost inevitable after that.

---

# What Will Change When We Introduce Python?

Right now, we've been talking in business language.

For example:

> "Accept a valid placement."

Later, in Python, that behaviour may become something like:

```python
class Board:
    def place_symbol(...):
        ...
```

Notice what happened.

We didn't invent `place_symbol()`.

We **discovered** it.

That's the difference.

---

# Our Python Philosophy

When we eventually reach Python, we'll follow this sequence for every class:

```text
Business Responsibility

↓

Business Behaviour

↓

Software Operations

↓

Python Method

↓

Python Code
```

Then we'll ask questions like:

* Should this be a public method?
* Should this be a private helper?
* Should this return something or just change state?
* Should this raise an exception or return a result?
* Is this method doing too much?
* Does this method belong here?

Those are **design questions** expressed through Python.

Not Python questions.

---

# This Will Also Make You Language-Independent

One of the biggest advantages of our approach is that you'll never be locked into Python.

If tomorrow someone asks you to implement the same design in:

* Java
* C#
* Go
* Kotlin
* TypeScript

the thinking won't change.

Only the syntax will.

That's why experienced engineers can switch languages much faster than beginners. Their design skills transfer.

---

# 🚀 Step 7 — Day 3

# Public Behaviour vs Internal Behaviour

Yesterday we discovered that one behaviour often becomes multiple operations.

Today we ask a new question:

> **Should every operation be visible to other objects?**

At first, that sounds like a programming-language question.

It isn't.

It's actually a **business trust** question.

---

# A Hotel Analogy

Imagine you're staying at a hotel.

As a guest, you can:

* Check in.
* Check out.
* Request room service.
* Ask for a wake-up call.

Those are services the hotel intentionally exposes.

But should you also be able to:

* Update the booking database?
* Assign yourself a room?
* Change housekeeping schedules?
* Override payment records?

Of course not.

Those activities happen inside the hotel.

They are necessary operations.

But they are **not part of the hotel's public behaviour**.

Interesting...

The hotel performs far more work than it allows customers to request.

Objects behave the same way.

---

# Back to Tic-Tac-Toe

Consider the Board.

Yesterday we decomposed one behaviour into operations:

```text
Accept Placement

↓

Locate Position

↓

Validate Position

↓

Locate Cell

↓

Update Cell

↓

Protect Consistency
```

Now ask yourself:

Should the `Game` be allowed to say:

> "Board, give me Cell (2,2)."

Or:

> "Board, skip validation."

Or:

> "Board, update this Cell directly."

Something feels dangerous.

Why?

Because the Game is trying to interfere with work the Board is responsible for protecting.

---

# The Hidden Discovery

We're beginning to distinguish between two kinds of behaviour.

## Public Behaviour

Capabilities that collaborators are allowed to request.

Examples:

* Accept a placement.
* Reveal the current board state.
* Check whether a position is available.

These are part of the Board's agreement with other objects.

---

## Internal Behaviour

Work the object performs to fulfil its own responsibilities.

Examples:

* Locate a Cell.
* Validate internal consistency.
* Traverse rows.
* Evaluate diagonals.
* Update bookkeeping.

These operations exist.

But only the object itself should decide when to use them.

---

# Why Does This Matter?

Imagine the Game could update Cells directly.

Then the Board could no longer guarantee that:

* moves are valid,
* state remains consistent,
* business rules are respected.

In other words...

The Board would still have the responsibility...

...but no longer have control over it.

That would be poor design.

---

# A New Design Principle

Here's a sentence I want you to think about:

> **The object that owns the responsibility should control how that responsibility is fulfilled.**

That one sentence is the business reason behind what programming languages later call encapsulation.

Notice...

We still haven't mentioned `public` or `private`.

Because those are solutions.

We're discovering the problem first.

---

# 🎯 Step 7 — Day 3 Assignment

## Part A — Public or Internal?

For each operation below, decide whether it should be:

* **Public behaviour** (available to collaborators), or
* **Internal behaviour** (used only by the object itself).

Explain **why**, not just your choice.

### Game

* Accept player's move
* Change current player
* Determine next game state
* End the game

### Board

* Accept placement
* Locate Cell
* Validate position
* Maintain board consistency
* Reveal board state

### WinningCondition

* Evaluate winner
* Evaluate rows
* Evaluate columns
* Evaluate diagonals

---

## Part B — The Trust Question

Answer these scenarios.

### Scenario 1

Should the Game ever be allowed to modify a Cell directly?

Why?

---

### Scenario 2

Should the Board expose an operation that lets another object bypass validation?

Why?

---

### Scenario 3

Suppose tomorrow we support a 5×5 board instead of 3×3.

Which object should absorb most of the change?

Why?

---

## Part C — Reflection

Complete these sentences.

> **Public behaviour exists because...**

> **Internal behaviour exists because...**

Then answer:

> **How does separating public and internal behaviour protect responsibilities?**

---

# 🌟 Engineering Checkpoint

This is today's most important question.

> **If another object can freely perform your internal operations, do you still truly own the responsibility? Why or why not?**

Don't answer in terms of `private` or `public`.

Answer in terms of ownership, trust, and business responsibilities.

---

# 🌟 One Sentence to Carry Forward

> **An object fulfils its responsibility not only by what it does, but also by controlling how others are allowed to interact with it.**

---

And finally...

You said something that made me genuinely happy:

> **"In future we'll see in terms of Python."**

Yes.

We absolutely will.

But when we finally write something like:

```python
class Board:
    ...
```

I don't want you to think:

> "I'm writing a Python class."

I want your first thought to be:

> **"I'm giving software form to a business responsibility."**

If that becomes your instinct, Python becomes just a language.

The design becomes the real skill.

Let's see what you discover in today's assignment. 🚀


--------------------------------------------------------------------------------------------------------------------
## My answers
---------------------------------------------------------------------------------------------------------------------

Excellent.

Today we're discovering something deeper than "public vs private."

If we stop at the programming language level, we'll think:

> "Public means `public`."
> "Internal means `private`."

But that's not what we're learning.

Today's real question is:

> **"Which business capabilities should other collaborators be allowed to rely on, and which pieces of work should remain the object's own concern?"**

This is really about **trust and ownership**.

---

# Part A — Public or Internal?

## Game

### Behaviour: Accept player's move

**Decision:** Public behaviour

### Why?

This is one of the Game's core business capabilities.

Other collaborators (such as the Player or a higher-level controller) interact with the Game by asking it to process a move.

This is part of the Game's contract with the outside world.

---

### Behaviour: Change current player

**Decision:** Internal behaviour

### Why?

Changing turns is part of *how* the Game fulfils the larger behaviour of processing a move.

Nobody outside the Game should decide when the turn changes.

That would violate the Game's ownership of the game flow.

---

### Behaviour: Determine next game state

**Decision:** Internal behaviour

### Why?

This is part of the Game's internal decision-making.

Whether the next state is:

* ongoing,
* won,
* drawn,

is something the Game determines while coordinating the business process.

Collaborators care about the outcome—not the internal step itself.

---

### Behaviour: End the game

**Decision:** Internal behaviour

### Why?

Ending the game is not an independent service that collaborators request.

It is something the Game performs when the business rules require it.

The Game owns the lifecycle.

Therefore it also owns deciding when that lifecycle ends.

---

# Board

### Behaviour: Accept placement

**Decision:** Public behaviour

### Why?

This is the Board's primary business capability.

The Game collaborates with the Board through this behaviour.

It forms part of the Board's contract.

---

### Behaviour: Locate Cell

**Decision:** Internal behaviour

### Why?

How the Board finds a Cell is entirely its own concern.

Today it might use Cells.

Tomorrow it might use another structure.

No collaborator should depend on this operation.

---

### Behaviour: Validate position

**Decision:** Public behaviour

### Why?

Validation is a board-related business capability.

The Game legitimately needs to know whether a requested placement is allowed.

The Game asks for the outcome.

The Board decides how validation happens.

---

### Behaviour: Maintain board consistency

**Decision:** Internal behaviour

### Why?

Consistency is something the Board continuously protects while performing its responsibilities.

Nobody should request:

> "Please maintain consistency."

That is simply part of being a reliable Board.

---

### Behaviour: Reveal board state

**Decision:** Public behaviour

### Why?

Other collaborators—such as the WinningCondition—may legitimately need to observe the current playing area.

Providing a representation of the board is therefore part of the Board's external contract.

However, the Board decides **how** that state is represented.

---

# WinningCondition

### Behaviour: Evaluate winner

**Decision:** Public behaviour

### Why?

This is the reason the object exists.

The Game collaborates with WinningCondition through this behaviour.

---

### Behaviour: Evaluate rows

**Decision:** Internal behaviour

### Why?

Checking rows is merely one strategy used to fulfil the public behaviour.

Collaborators should never depend on this step.

---

### Behaviour: Evaluate columns

**Decision:** Internal behaviour

Exactly the same reasoning.

It contributes to the public behaviour but is not itself a business capability.

---

### Behaviour: Evaluate diagonals

**Decision:** Internal behaviour

Again, this is implementation detail hidden behind the public contract.

---

# Summary

| Object           | Behaviour                 | Public / Internal | Why?                                        |
| ---------------- | ------------------------- | ----------------- | ------------------------------------------- |
| Game             | Accept player's move      | Public            | Primary business capability others rely on. |
| Game             | Change current player     | Internal          | Part of coordinating game flow.             |
| Game             | Determine next game state | Internal          | Internal decision-making step.              |
| Game             | End the game              | Internal          | Lifecycle management belongs to Game.       |
| Board            | Accept placement          | Public            | Core board capability.                      |
| Board            | Locate Cell               | Internal          | Storage detail.                             |
| Board            | Validate position         | Public            | Legitimate board service.                   |
| Board            | Maintain consistency      | Internal          | Continuous internal responsibility.         |
| Board            | Reveal board state        | Public            | Needed by trusted collaborators.            |
| WinningCondition | Evaluate winner           | Public            | Core business capability.                   |
| WinningCondition | Evaluate rows             | Internal          | Helper operation.                           |
| WinningCondition | Evaluate columns          | Internal          | Helper operation.                           |
| WinningCondition | Evaluate diagonals        | Internal          | Helper operation.                           |

---

# Part B — The Trust Question

## Scenario 1

### Should the Game ever be allowed to modify a Cell directly?

No.

The Game is responsible for managing the overall business flow.

The Cell is responsible for managing its own state.

Between them sits the Board, which owns the playing area.

If the Game modifies a Cell directly, it bypasses the Board's responsibility.

That weakens the Board's ownership because another object starts performing work inside the Board's domain.

Instead of collaborating with the Board, the Game begins reaching into the Board's internals.

That's no longer collaboration.

It's interference.

---

## Scenario 2

### Should the Board expose an operation that lets another object bypass validation?

No.

Validation is one of the Board's business responsibilities.

If another object can bypass it, then the Board is no longer guaranteeing the correctness of its own state.

Sooner or later, invalid board states become possible.

The Board stops being trustworthy.

A collaborator should never be able to ask the Board to violate the very responsibility the Board exists to protect.

---

## Scenario 3

### Tomorrow we support a 5×5 board.

Which object should absorb most of the change?

Primarily the **Board**.

The Board owns the representation and management of the playing area.

It understands:

* dimensions,
* positions,
* valid locations,
* organisation of the playing area.

The **WinningCondition** may also require changes because the business rules for victory could depend on the board size.

The **Game**, however, should change very little because its responsibility—coordinating the game lifecycle—has not fundamentally changed.

This is exactly why we separated responsibilities earlier in the journey.

---

# Part C — Reflection

### Complete the sentences.

> **Public behaviour exists because collaborators need a stable way to request business capabilities from an object.**

> **Internal behaviour exists because an object needs freedom to organise its own work while fulfilling those capabilities.**

---

### How does separating public and internal behaviour protect responsibilities?

Responsibilities define what an object owns.

Public behaviour tells collaborators:

> "This is what you may ask me to do."

Internal behaviour says:

> "This is how I choose to fulfil that promise."

By keeping those separate:

* collaborators depend only on stable business capabilities,
* implementation details remain free to evolve,
* ownership stays clear,
* unnecessary coupling is avoided.

The object remains responsible for *how* its work is accomplished.

Everyone else relies only on *what* it promises to achieve.

---

# 🌟 Engineering Checkpoint

## If another object can freely perform your internal operations, do you still truly own the responsibility?

No.

Ownership means more than being associated with a responsibility.

It means being the trusted authority that decides **how that responsibility is fulfilled**.

If other objects can freely perform your internal operations, they begin making decisions that belong to you.

Over time:

* your responsibility becomes shared,
* business rules become scattered,
* different collaborators may perform the work differently,
* no single object can guarantee the business outcome.

Eventually, nobody truly owns the responsibility because ownership has been diluted.

True ownership requires trust.

Other objects trust you to fulfil your responsibility correctly.

In return, they don't interfere with how you perform it.

That trust is what allows responsibilities to remain clear, collaborations to remain healthy, and the system to evolve without confusion.

---

# 🌟 One Sentence That Changed My Thinking

> **An object truly owns a responsibility only when other collaborators trust it to fulfil that responsibility without needing to reach inside and perform its internal work.**

---

# Mentor's Feedback

Today you've discovered another important layer in the design hierarchy:

```text
Business Responsibility
        │
        ▼
Public Behaviour (What others may ask for)
        │
        ▼
Internal Behaviour (How the object fulfils its promise)
        │
        ▼
Operations
        │
        ▼
Implementation
```

The key insight is that **ownership isn't just about having a responsibility written next to an object**. Ownership is meaningful only if other collaborators respect that boundary.

Think back over the journey:

* In **Step 5**, we discovered *who* should own business responsibilities.
* In **Step 6**, we discovered *how* those owners collaborate through messages and contracts.
* In **Step 7**, we're now refining *what* each owner exposes to others and *what* it keeps as its own concern.

These aren't separate topics—they're successive refinements of the same idea.

A well-designed object isn't one that does everything. It's one that clearly says:

> **"This is what you can depend on me for. Everything else is my responsibility to manage."**

That's a mindset you'll carry into much larger systems, where preserving those boundaries is often the difference between software that evolves gracefully and software that becomes increasingly fragile.


------------------------------------------------------------------------------------------------------------
## Answers Feedbacks and Next
---------------------------------------------------------------------------------------------------------------

Aditya...

I don't think you realise what happened in this assignment.

This wasn't an exercise about **public vs internal**.

It was your **first encounter with software boundaries**.

And that's one of the biggest ideas in software engineering.

---

# Before the Review...

Let me show you something.

Look at the progression we've built.

```text
Business Problem

↓

Business Concepts

↓

Responsibilities

↓

Collaboration

↓

Behaviour

↓

Operations

↓

Boundaries   ← Today
```

Notice what's happening.

We're no longer asking:

> "What should this object do?"

We're asking:

> **"What should the rest of the world be allowed to know?"**

That's a much deeper question.

---

# Review

I'm going to review this a little differently today.

Instead of reviewing each answer independently, I want to review **your thinking pattern**.

Because that's what is evolving.

---

# Pattern 1 — You Started Thinking in Terms of Contracts

Take this answer.

> **Accept player's move → Public**

You didn't say:

> "Because another class needs it."

You said:

> **"This forms part of the Game's contract."**

That single word...

**Contract**

...is becoming part of your natural vocabulary.

Remember Step 6?

Contracts were about trust.

Today they're becoming **software boundaries**.

Beautiful progression.

---

# Pattern 2 — Internal Doesn't Mean Unimportant

One mistake beginners make is thinking:

```text
Internal

↓

Less important
```

Your answers show the opposite.

For example:

> Maintain board consistency

You recognised something subtle.

Nobody asks for it.

But without it...

Nothing else works.

Internal behaviour often protects the most important business guarantees.

---

# Pattern 3 — You Didn't Confuse Visibility With Ownership

This was my favourite sentence.

> **"The Game owns the lifecycle. Therefore it owns deciding when that lifecycle ends."**

Exactly.

Many developers think:

> Public means important.

No.

Public simply means:

> **This is how others are allowed to collaborate with me.**

Ownership is a different concept.

You kept those separate.

---

# One Refinement

There is only one answer where I'd like to challenge your thinking slightly.

---

## Board — Validate Position

You marked it as **Public**.

That's a completely reasonable answer.

But now let's think like architects.

Imagine this interaction:

```text
Game

↓

Board

↓

Accept Placement
```

Inside the Board:

```text
Validate Position

↓

Locate Cell

↓

Update Cell
```

Now ask yourself:

Should the Game ever say:

> "Board, only validate this position."

Or should it simply say:

> "Board, place this symbol."

There are two possible designs.

---

### Design A

Expose validation publicly.

```text
Game

↓

validate()

↓

place()
```

---

### Design B

Expose only placement.

Validation remains internal.

```text
Game

↓

place()
```

Board decides everything else.

---

Which is better?

The answer is...

**It depends on the business.**

And that's today's hidden lesson.

Software design is rarely about absolute rules.

It's about trade-offs.

---

# Hidden Discovery #1

You have now encountered your **first API design decision**.

Without writing a single method.

Because that's exactly what API design is.

Deciding:

> **What should other objects be allowed to ask me to do?**

Not:

> How should I implement it?

We'll spend a lot more time on this later.

---

# Part B

These answers are outstanding.

Especially this.

> **Instead of collaborating with the Board, the Game begins reaching into the Board's internals.**

That sentence tells me something.

You no longer think collaboration means:

> Calling another object.

You now think collaboration means:

> Respecting another object's authority.

That is a huge shift.

---

# Scenario 3

This answer was excellent.

You naturally separated:

Board changes.

WinningCondition possibly changes.

Game barely changes.

Notice what happened.

You didn't reason from classes.

You reasoned from responsibilities.

Exactly the habit we wanted.

---

# Reflection

I think your two completed sentences are some of the strongest you've written.

> **Public behaviour exists because collaborators need a stable way to request business capabilities.**

Perfect.

And...

> **Internal behaviour exists because an object needs freedom to organise its own work.**

Aditya...

That sentence is incredibly important.

Freedom.

That's exactly why encapsulation exists.

Not secrecy.

Freedom.

Freedom to evolve.

Freedom to improve.

Freedom to reorganise.

Without breaking collaborators.

---

# Engineering Checkpoint

I asked:

> If others perform your internal work...

Do you still own the responsibility?

Your answer:

> Ownership becomes diluted.

I love that word.

**Diluted.**

Not broken.

Not destroyed.

Diluted.

That's exactly what happens in large systems.

Responsibilities don't disappear overnight.

They slowly leak into neighbouring objects.

Eventually...

Nobody knows who owns what.

That's how systems become difficult to maintain.

---

# 🌟 The Biggest Discovery Today

Today wasn't really about public behaviour.

It was about something deeper.

Let's compare.

Yesterday...

```text
Board

↓

Owns placement
```

Today...

```text
Board

↓

Owns placement

↓

Controls how placement happens
```

See the difference?

Ownership is not just about *doing* the work.

It's also about *protecting the path* to doing the work.

That's a profound shift.

---

# 🧠 Engineering Deep Dive

As always...

Let's ask our three questions.

---

## What did we really discover today?

**Boundary-Controlled Collaboration**

Not encapsulation.

Not visibility modifiers.

Those come later.

The engineering idea comes first.

---

## What is Boundary-Controlled Collaboration?

It is:

> **Allowing collaborators to request business capabilities while preventing them from interfering with the object's internal responsibility.**

Notice the balance.

Not isolation.

Not unrestricted access.

Controlled collaboration.

---

## Why did engineers invent this idea?

Imagine there were no boundaries.

Any object could:

* update Cells,
* change turns,
* modify Board state,
* skip validation.

Soon...

Responsibilities would become scattered.

Business rules would exist in multiple places.

Nobody could guarantee correctness anymore.

Boundaries keep responsibility meaningful.

---

## What problem does it solve?

Three major problems.

### 1. Protects Ownership

The responsible object remains the authority.

---

### 2. Reduces Coupling

Collaborators depend on capabilities.

Not implementation.

---

### 3. Enables Evolution

The object can improve internally without affecting everyone else.

This connects beautifully back to Step 6's discussion of **contracts**.

---

# 🌉 The Hidden Timeline

I want to show you something.

Without noticing it, you've rediscovered several famous OO principles.

Look at the path.

```text
Step 5

Responsibility

↓

Step 6

Collaboration

↓

Messages

↓

Contracts

↓

Step 7

Behaviour

↓

Operations

↓

Boundaries
```

Do you know what comes next?

Interfaces.

Method design.

Encapsulation.

Information hiding.

SOLID.

Design Patterns.

But here's the difference.

When we eventually name those ideas, they won't feel like new topics.

They'll feel like:

> **"Oh... this is the programming technique engineers invented to express the thinking we've already built."**

That's exactly the outcome I wanted from this mentorship.

---

# 📍I Want to Slightly Adjust Our Roadmap Again

After reading your answer, I think there's one missing bridge before we introduce methods.

I want to spend one day on something that almost nobody teaches explicitly.

## Step 7 — Day 4

### **Commands vs Questions**

Think about the operations we've discovered.

Some ask an object to **do** something.

Some ask it to **tell** us something.

For example:

```text
Board

Accept Placement
```

versus

```text
Board

Reveal Board State
```

They are fundamentally different interactions.

One changes the world.

One observes the world.

This distinction becomes incredibly important when we start designing Python methods.

It also naturally leads us to ideas like:

* side effects,
* return values,
* immutability,
* testing,
* Command–Query Separation (CQS).

Again, we'll discover the engineering need before we introduce the terminology.

I think it fits perfectly here.

---

# 🌟 One Sentence That Changed My Thinking Today

Today's sentence comes directly from **your own reflection**:

> **"The object remains responsible for how its work is accomplished. Everyone else relies only on what it promises to achieve."**

I genuinely think that's one of the strongest sentences you've written in this entire case study.

It captures:

* responsibility,
* contracts,
* collaboration,
* boundaries,

all in one idea.

---

# Finally...

Aditya, I want to share something I noticed over the last few days.

At the beginning of this case study, your answers often described **what happens**.

Now your answers explain **why the design is structured that way**.

That's a significant change.

An interviewer can teach syntax.

A company can teach frameworks.

It's much harder to teach someone to reason from first principles about ownership, collaboration, and boundaries.

That's the skill you're building.

And because you mentioned Python earlier, I think you'll appreciate this:

When we finally write our first Python method, we won't ask:

> **"Should this be `public`?"**

We'll ask:

> **"Is this part of the object's promise to the outside world, or is it part of how the object keeps that promise?"**

Once you can answer that, the Python keyword becomes almost obvious.

That's the kind of engineer we're aiming to build. 🚀
