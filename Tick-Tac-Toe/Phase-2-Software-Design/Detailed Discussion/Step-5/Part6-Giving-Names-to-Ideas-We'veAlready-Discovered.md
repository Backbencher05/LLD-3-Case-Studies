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
