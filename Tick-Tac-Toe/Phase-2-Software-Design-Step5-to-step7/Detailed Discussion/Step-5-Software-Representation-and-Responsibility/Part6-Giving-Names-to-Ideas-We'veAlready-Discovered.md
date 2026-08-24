You're welcome. 😊

And before we move forward...

I want to tell you something that I honestly didn't expect when we started this project.

## When We Started

I thought I was going to teach you:

* OOP
* LLD
* Design Patterns
* SOLID

Now I realize...

We're actually building something much bigger.

We're building a **Software Engineering Thinking Framework**.

Tic-Tac-Toe is just the laboratory.

Parking Lot will be another laboratory.

BookMyShow another.

Splitwise another.

Eventually, you'll stop asking:

> "How do I design Tic-Tac-Toe?"

You'll start asking:

> **"What kind of software problem is this?"**

That's exactly how senior architects think.

---

# Today Is a Milestone

Today we're not learning a new design idea.

Today we're going to connect everything we've discovered.

For the first time...

I'm going to reveal that almost everything we've "discovered" over the last week already exists in software engineering literature.

Not because we copied it.

Because great engineers, over decades, observed the same patterns we did.

---

# Phase 2 — Software Representation

# Step 5 — Day 6

# Giving Names to Ideas We've Already Discovered

Most courses begin like this:

> Today we learn GRASP.

Then they list nine principles.

Students memorize them.

Forget them two weeks later.

We're going to do the opposite.

We're going to ask:

> **What problems have we already solved?**

And then discover what those solutions are called.

---

# Let's Look Back

## Discovery 1

When we asked:

> Who should know whether a Cell is empty?

You answered:

> Cell.

Why?

Because...

> Cell owns its own state.

At the time we called it:

> The object that owns the knowledge should own the responsibility.

The software engineering community gave this idea a name.

# Information Expert (GRASP)

> **Assign a responsibility to the object that has the information needed to fulfill it.**

Notice something.

You've been using this principle for days.

You just didn't know its official name.

---

# Discovery 2

When we discussed:

Game

↓

Board

↓

Cell

Instead of

Game

↓

Cell

↓

Symbol

You said:

> The Game shouldn't know Board internals.

Why?

Because we wanted objects to know as little as necessary about each other.

That idea has a name.

# Low Coupling (GRASP)

> **Reduce unnecessary dependencies between objects.**

Notice how many of your answers naturally applied this:

* Game delegates to Board.
* Board delegates to Cell.
* Game delegates to Bot.
* Game delegates to WinningCondition.

Each delegation reduced coupling.

---

# Discovery 3

Remember when we grouped responsibilities?

Game:

* start
* end
* switch turns

Board:

* place symbol
* validate position

WinningCondition:

* evaluate rules

Player:

* choose move

We said:

Each object has one focused purpose.

The software engineering community calls this:

# High Cohesion (GRASP)

> **Keep related responsibilities together within the same object.**

Notice:

We never said:

> One method.

We said:

> One related purpose.

That's a much better way to think about cohesion.

---

# Discovery 4

When we discussed:

WinningCondition

We asked:

Should this become its own abstraction?

Your answer was:

Only if business rules are expected to vary.

That's exactly the motivation behind:

* Open–Closed Principle
* Strategy Pattern

But notice...

Neither OCP nor Strategy came first.

The business pressure came first.

---

# Discovery 5

Yesterday you wrote:

> Game shouldn't print the board.

Instead...

Game should ask a presentation component.

That reasoning leads toward another GRASP principle.

# Pure Fabrication

Wait...

What's that?

Let's discover it.

---

# The Strange Problem

Question.

Does:

```text
ConsoleView
```

exist in the business?

No.

The customer never said:

> There is a ConsoleView.

The business said:

Players play Tic-Tac-Toe.

So why invent:

```text
ConsoleView
```

Because...

We need somewhere to place presentation logic.

Interesting.

---

# A New Kind of Class

Until now, almost every class we've discussed came from the business.

Game

Board

Player

Cell

Position

WinningCondition

All business concepts.

Now suddenly...

ConsoleView appears.

It's **not** a business concept.

It's a software concept.

Why?

To keep the design clean.

---

# The Software Community Gave This a Name

# Pure Fabrication (GRASP)

> **Sometimes we create a class that doesn't exist in the business because it improves the software design.**

That sounds almost wrong...

Until you think about it.

Examples:

* Repository
* Service
* Logger
* Cache
* EmailSender
* ConsoleView
* FileWriter

None of these exist in the business domain.

Yet they are incredibly useful.

---

# This Is a Huge Discovery

Remember Step 5 Day 1?

We said:

> Software represents reality.

Today we refine it.

> **Software represents reality—but it may introduce new abstractions when they improve the design.**

That's a very important distinction.

Software is not a photograph.

It's an engineering model.

---

# Our Journey So Far

Look how naturally everything fits together.

```text
Business Reality

↓

Business Concepts

↓

Software Representation

↓

Responsibilities

↓

Delegation

↓

Coupling

↓

Cohesion

↓

Software Abstractions
```

Notice something.

Nothing appeared randomly.

Each idea emerged because the previous one created a new question.

That's why I wanted us to learn this way.

---

# Why This Matters

Imagine two interview candidates.

Candidate A:

> GRASP has nine principles.

Candidate B:

> I separated winner detection because the rule changes independently of board representation. Later I learned this aligns with Information Expert, High Cohesion, and Low Coupling.

Who sounds like an engineer?

Exactly.

---

# One More Surprise

We've actually discovered four different categories of classes.

## 1. Domain Classes

Represent the business.

Examples:

* Game
* Board
* Player

---

## 2. Value Objects

Represent values.

Examples:

* Position
* Coordinate

---

## 3. Policy / Rule Objects

Represent business rules.

Examples:

* WinningCondition

---

## 4. Fabricated Classes

Exist only to improve software.

Examples:

* ConsoleView
* Repository
* Logger

This classification will become incredibly valuable in larger systems.

---

# 🎯 Assignment

I don't want you to memorize GRASP.

Instead, I want you to map our discoveries.

## Part A

For each GRASP principle below, explain:

1. What problem does it solve?
2. Which discussion from Tic-Tac-Toe helped you discover it?
3. Give one example from our design.

Principles:

* Information Expert
* Low Coupling
* High Cohesion
* Pure Fabrication

---

## Part B

Classify each of these into one of the four categories:

* Game
* Board
* Player
* Cell
* Position
* Symbol
* GameStatus
* WinningCondition
* ConsoleView
* Logger
* Repository
* EmailSender

Categories:

* Domain Class
* Value Object
* Policy / Rule Object
* Pure Fabrication

Explain **why**, not just the category.

---

# 🌟 Engineering Checkpoint

Today wasn't about learning new principles.

It was about realizing something powerful:

> **The best software principles are not arbitrary rules—they are names given to design decisions that repeatedly solved real problems.**

That's why they have lasted for decades.

---

# 🌟 One Sentence That Changed My Thinking

I think today's sentence is one that every software engineer should remember:

> **Great engineers don't memorize principles—they rediscover them every time they solve a design problem.**

And I genuinely believe that's what you've been doing throughout Step 5.

---

## Before We End...

I want to share one thought about the journey itself.

When we eventually study SOLID, Design Patterns, or Clean Architecture, I don't want them to feel like separate subjects.

I want them to feel like the **natural vocabulary** of a language you're already speaking.

Right now, you're learning to think in that language.

Later, we'll simply learn the names of its grammar.



## My Answers

This is one of the best assignments you've done so far.

Why?

Because until now, we've been **discovering good design naturally**.

Now we're looking back and realizing:

> **"Oh... these ideas already have names."**

That's exactly how GRASP should be learned.

Not:

> Learn Principle → Apply

But:

> Discover Good Design → Recognize the Principle

Let's do that.

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


------------------------------------------------------------------------------------------------------------------------------------
## Answer feedback and Next
----------------------------------------------------------------------------------------------------------------------------------

Aditya...

I'm going to do something a little different today.

Usually I review your assignment.

Today...

I want to review **your thinking**.

Because I think something significant has changed.

---

# The Biggest Change

When we started Step 5, you used to answer questions like this:

> Board should do this because it makes sense.

Today your answers look like this:

> This responsibility belongs to Board because Board owns this knowledge, which reduces coupling and preserves cohesion.

That isn't just better wording.

It's a different way of reasoning.

You've started using **engineering arguments** instead of **intuition**.

That is exactly what I wanted Step 5 to achieve.

---

# Let's Review Deeply

## Part A — GRASP Mapping

### 1. Information Expert

This is excellent.

But I want to polish one sentence because I think it can become one of your permanent mental models.

You wrote:

> "Who has the information needed to perform this responsibility?"

I would evolve it into:

> **Assign behavior to the object that already owns the knowledge required to perform it.**

Why this wording?

Because "information" can sound like data.

But in software, **knowledge** includes:

* state
* invariants
* rules
* relationships

For example:

A `Board` doesn't just *contain* Cells.

It **knows**:

* how they're organized,
* how to find one,
* whether a position is valid.

That's more than information.

That's knowledge.

This distinction becomes important later when we discuss Domain-Driven Design.

---

## 2. Low Coupling

Your example is perfect.

But here's something interesting.

You wrote:

> Game → Board → Cell

At first glance, people think:

> "That's more calls. Isn't that *more* coupled?"

This is where I want to sharpen your intuition.

Coupling isn't measured by:

> Number of method calls.

It's measured by:

> **How much one object needs to know about another's internals.**

Game calling:

```java
board.reset()
```

is one dependency.

Game iterating through:

```java
board.getCells()[0][1].setValue(...)
```

creates many knowledge dependencies.

So a design with *more delegation* can actually have **less coupling**.

That's a subtle but powerful insight.

---

## 3. High Cohesion

This answer is one of your best.

Especially this sentence:

> Board manages board state.

WinningCondition evaluates rules.

That sentence demonstrates something deeper than cohesion.

It shows you're separating:

* **state** from **policy**.

That's a recurring architectural theme.

You'll see it again in:

* validation,
* pricing,
* authorization,
* discount engines,
* tax engines.

You don't know it yet, but you've already started thinking in those terms.

---

## 4. Pure Fabrication

Excellent.

But let me add one refinement.

You wrote:

> "Nowhere in the domain."

That's true.

But I think there's an even stronger way to think about it.

Pure Fabrication isn't:

> "A fake class."

It's:

> **A software responsibility that deserves a home, even though the business never named it.**

That wording matters.

Because it prevents a common misconception:

> "Pure Fabrication means unnecessary classes."

No.

They're often some of the most valuable classes in the system.

`Repository`, `Logger`, `Cache`, `ConsoleView`, `EmailSender`...

They're fabricated.

But they're essential.

---

# Part B — Classification

Honestly...

This is one of the cleanest classifications we've done in the entire case study.

There are only two places I'd like to deepen the discussion.

---

## Cell

You classified it as a Domain Class.

I agree.

But let's revisit something we discovered in Step 3.

Remember when we asked:

> Is Cell an Entity?

Our answer was:

> No.

Then today we classify it as a Domain Class.

Is that a contradiction?

No.

And this is a subtle distinction that many people miss.

---

### Entity vs Domain Class

A **Domain Class** is simply a class that models the business domain.

An **Entity** is a specific kind of Domain Class with its own identity and lifecycle.

Every Entity is a Domain Class.

Not every Domain Class is an Entity.

For Tic-Tac-Toe:

| Concept | Domain Class?     | Entity?                      |
| ------- | ----------------- | ---------------------------- |
| Game    | ✅                 | ✅                            |
| Player  | ✅                 | ✅                            |
| Board   | ✅ (owned by Game) | Debatable depending on model |
| Cell    | ✅                 | ❌                            |

That's why there isn't a contradiction.

This distinction will become incredibly useful when we eventually study Domain-Driven Design.

---

## WinningCondition

You classified it as:

> Policy / Rule Object.

I think that's exactly right.

And here's why I'm happy you chose that instead of "Pure Fabrication."

A beginner might say:

> "WinningCondition isn't a real thing."

Therefore:

> Pure Fabrication.

But notice...

WinningCondition *does* come from the business.

The business says:

> "A player wins when..."

That's a business rule.

It doesn't represent a physical object.

But it absolutely represents business knowledge.

That's why "Policy / Rule Object" is the better classification.

Excellent reasoning.

---

# Something Beautiful Happened

Let's look at the classes we've discovered.

```
Game
Player
Board
Cell
Position
WinningCondition
ConsoleView
```

Notice something.

We didn't invent these because of OOP.

We discovered them because of different kinds of responsibility.

Some represent:

* Things

Some represent:

* Values

Some represent:

* Rules

Some represent:

* Software services

That is exactly how mature systems evolve.

---

# The Hidden Lesson

I don't think today's lesson was GRASP.

I think today's lesson was:

> **Not every class exists for the same reason.**

That's profound.

Because beginners often think:

> "Everything is just a class."

Experienced engineers ask:

> **Why does this class exist?**

That's a much better question.

---

# I Want to Add One More Layer

I think we've reached another milestone in our methodology.

So far we have:

```
Business Requirement
        ↓
Business Concepts
        ↓
Software Representation
        ↓
Responsibility Assignment
        ↓
Delegation
        ↓
Architectural Boundaries
```

Today, I'd like to extend it.

```
Business Requirement
        ↓
Business Concepts
        ↓
Kinds of Knowledge
        ↓
Software Representation
        ↓
Responsibility Assignment
        ↓
Delegation
        ↓
Architectural Boundaries
```

Why?

Because today's assignment quietly revealed four different kinds of knowledge:

* **Domain knowledge** → Game, Board, Player
* **Value knowledge** → Position, Symbol, GameStatus
* **Business policy** → WinningCondition
* **Technical knowledge** → ConsoleView, Logger, Repository

That classification will help us reason about much larger systems later.

---

# Now... I Want to Tell You Something

I think Step 5 is complete.

Not because we've exhausted every possible discussion.

But because we've achieved its objective.

Let's compare where you started and where you are now.

### Before Step 5

You asked:

* What classes should I create?
* Should Cell be an Entity?
* Should Position be a class?

### After Step 5

You're asking:

* Who owns this knowledge?
* Is this business knowledge or technical knowledge?
* Should this become its own abstraction?
* Is this increasing coupling?
* Is this preserving cohesion?
* Should this object perform the work or delegate it?
* Is this a Domain Class, Value Object, Policy Object, or Pure Fabrication?

That transformation is exactly what Step 5 was meant to accomplish.

---

# My Proposal

I don't want to rush into Step 6 immediately.

I think Step 5 deserves a proper conclusion.

Just like we did for Step 3.

I'd like our next session to be:

# 🎤 Interview Thinking for Step 5

Not another lesson.

A synthesis.

We'll answer questions like:

* Why did we create `WinningCondition`?
* Why isn't `ConsoleView` part of the domain?
* Why doesn't `Game` update `Cell` directly?
* When would you intentionally violate Information Expert?
* When is a Pure Fabrication justified?
* Why isn't every business noun a class?

And then...

We'll produce a final **Step 5 Discovery Document**.

Not a notes document.

A document that captures the engineering thinking we've built.

Because I genuinely think it's worth preserving.

---

# 🌟 One Sentence That Changed My Thinking

I don't want to write this one.

I think **you've earned it.**

If I had to summarize your growth through Step 5 in a single sentence, it would be:

> **Good software design is not about creating classes—it is about placing knowledge, responsibilities, and change in the right place.**

I actually think that sentence captures everything we've discovered over the past six days.

And I have a feeling that when we begin Step 6, you'll notice something interesting:

You'll no longer be designing *classes*.

You'll be designing *collaborations between objects*.

That's the natural next step in your journey as a software designer.
