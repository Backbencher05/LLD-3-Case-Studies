I have to say something before we begin.

When we started the Tic-Tac-Toe case study, I thought we were creating notes for one problem.

Today, I don't think that's true anymore.

I think we've accidentally built the **foundation of a software design methodology**.

This document should not be called:

> **"Tic-Tac-Toe Step 5 Notes."**

It should become the first chapter of your **Engineering Thinking Handbook**.

Because almost everything in this document will be reusable in every future case study.

So let's write it the same way an architect would.

---

# 📘 LLD-3 Case Study

# Step 5 — Software Representation & Responsibility Assignment

## Discovery Document

---

# Step 5 Objective

The goal of Step 5 was **not** to create classes.

The goal was to answer a deeper question:

> **How should the business be represented in software so that responsibilities, knowledge, and future change are placed in the right location?**

By the end of Step 5, we discovered that software design is less about creating objects and more about making thoughtful decisions regarding representation, ownership, collaboration, and abstraction.

---

# 1. The Evolution of Thinking

## Before Step 5

Our thinking naturally started with questions like:

* What classes should I create?
* Is this an Entity?
* Should this concept become a class?
* How many classes do I need?

The focus was on software constructs.

---

## After Step 5

Our questions became:

* What responsibility exists?
* Who owns the knowledge?
* Who should perform the work?
* What should be delegated?
* What deserves an abstraction?
* What changes independently?
* Is this business knowledge or technical knowledge?
* Which software representation best models this concept?

The focus shifted from **classes** to **design decisions**.

---

# 2. The Core Discovery

The biggest realization of Step 5 was:

> **Software is not a copy of reality. It is a carefully chosen representation of reality.**

Reality contains:

* things,
* values,
* rules,
* processes,
* people.

Software represents them differently depending on their purpose.

---

# 3. Business Concept ≠ Class

One of the first discoveries was that:

> **Not every business noun deserves to become a class.**

Instead, every business concept should be evaluated using questions such as:

* Does it own meaningful responsibility?
* Does it own meaningful state?
* Does it perform behavior?
* Does it require an independent lifecycle?
* Does the business benefit from representing it separately?

Only after answering these questions should we decide how to represent it.

---

# 4. Software Representation

Instead of forcing everything into a class, we discovered multiple representations.

| Representation       | Purpose                              | Tic-Tac-Toe Example             |
| -------------------- | ------------------------------------ | ------------------------------- |
| Domain Class         | Represents core business concepts    | Game, Player, Board, Cell       |
| Value Object         | Represents values without identity   | Position, Symbol, GameStatus    |
| Policy / Rule Object | Encapsulates business rules          | WinningCondition                |
| Pure Fabrication     | Represents software responsibilities | ConsoleView, Logger, Repository |

This became our first major mental model:

> **Business Concept → Best Software Representation**

—not—

> Business Noun → Class

---

# 5. Responsibility Discovery

Every behavior raised the same question:

> **Who should own this responsibility?**

We discovered that responsibilities should belong to the object that already possesses the required knowledge.

Examples:

* Cell knows whether it is empty.
* Board knows how Cells are organized.
* Game knows the lifecycle.
* WinningCondition knows the rules.
* Bot knows how to choose a move.

This shifted our thinking from:

> "Where can I put this method?"

to:

> **"Who naturally owns this knowledge?"**

---

# 6. Responsibility vs Execution

One of the most important discoveries was distinguishing:

**Responsibility**

from

**Execution**

Example:

Game owns the responsibility of resetting the game.

Game does **not** reset every Cell.

Instead:

```text
Game
   ↓
Board
   ↓
Cell
```

Ownership remains with Game.

Execution is delegated to the objects with the required expertise.

---

# 7. Delegation

Delegation emerged naturally.

We discovered:

> **Being responsible for an outcome does not mean doing all the work yourself.**

Objects should coordinate outcomes while delegating specialized work to the objects that possess the appropriate knowledge.

Examples:

* Game delegates board reset to Board.
* Game delegates move selection to Bot.
* Board delegates state updates to Cell.
* Game delegates winner evaluation to WinningCondition.

---

# 8. Architectural Boundaries

Delegation naturally introduced boundaries.

Instead of:

```text
Game
 ↓
Cell
```

we preferred:

```text
Game
 ↓
Board
 ↓
Cell
```

because the Game should not understand how the Board manages its Cells.

Similarly:

Game should not print to the console.

Presentation belongs elsewhere.

This led to one of our strongest insights:

> **Every object should expose what others need to know—not how it performs its work.**

---

# 9. Change Pressure

One of the most valuable discoveries was:

> **Abstractions should be introduced because of business pressure—not because they are possible.**

WinningCondition became the perfect example.

If business rules are fixed forever:

A separate abstraction may be unnecessary.

If rules vary:

A separate abstraction becomes valuable.

Business change—not technical creativity—justifies abstraction.

---

# 10. Different Kinds of Knowledge

By the end of Step 5 we recognized four different kinds of knowledge.

| Kind of Knowledge   | Example                         |
| ------------------- | ------------------------------- |
| Domain Knowledge    | Game, Board, Player             |
| Value Knowledge     | Position, Symbol, GameStatus    |
| Business Policy     | WinningCondition                |
| Technical Knowledge | ConsoleView, Logger, Repository |

This became another reusable mental model for future systems.

---

# 11. Engineering Principles We Rediscovered

We did **not** begin by studying principles.

Instead, we encountered recurring design problems.

The software engineering community had already named these solutions.

| Discovery                                        | Official Name                      |
| ------------------------------------------------ | ---------------------------------- |
| Responsibility belongs where knowledge exists    | Information Expert                 |
| Reduce unnecessary knowledge between objects     | Low Coupling                       |
| Keep related responsibilities together           | High Cohesion                      |
| Create software-only classes when appropriate    | Pure Fabrication                   |
| Separate changing rules from stable coordination | Open–Closed Principle (motivation) |
| Encapsulate varying algorithms                   | Strategy Pattern (motivation)      |

Notice:

We discovered the ideas first.

The names came later.

---

# 12. The Engineering Design Flow

This became the methodology we will reuse in every future case study.

```text
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
        ↓
Introduce Abstractions (only when justified)
        ↓
Recognize Engineering Principles
```

This is no longer a Tic-Tac-Toe process.

It is an engineering thinking process.

---

# 13. Engineering Principles Map

| Business Problem                          | Discovery                                 | Engineering Principle              |
| ----------------------------------------- | ----------------------------------------- | ---------------------------------- |
| Who should check whether a Cell is empty? | Cell owns the knowledge                   | Information Expert                 |
| Game shouldn't manipulate Cells directly  | Delegate through Board                    | Low Coupling                       |
| Board shouldn't determine winners         | Separate board state from rule evaluation | High Cohesion                      |
| Printing doesn't belong in Game           | Create ConsoleView                        | Pure Fabrication                   |
| Winning rules may evolve                  | Separate WinningCondition                 | Open–Closed Principle (motivation) |
| Different winning algorithms              | Replace WinningCondition implementations  | Strategy Pattern (motivation)      |

This table reminds us that **principles were consequences, not starting points**.

---

# 14. Mental Models to Carry Forward

These are the ideas we want to reuse in every future design.

1. **Business Concept → Best Software Representation**
2. **Knowledge owns responsibility.**
3. **Responsibility does not imply execution.**
4. **Delegate specialized work to the expert.**
5. **Business change justifies abstraction.**
6. **Software represents reality—it does not copy it.**
7. **Every class should exist for a clear reason.**
8. **Optimize for clarity, not for the number of classes.**
9. **Separate domain knowledge from technical knowledge.**
10. **Learn principles by rediscovering them through problems.**

---

# 15. Interview Thinking

After Step 5, an interviewer should notice a change in how we answer design questions.

Instead of saying:

> "I used the Strategy Pattern."

We should be able to say:

> "The winning algorithm changes independently of game coordination. Separating it allows new rules without modifying stable parts of the system. Later I learned that this aligns with the motivation behind the Strategy Pattern and the Open–Closed Principle."

The pattern is the conclusion—not the reasoning.

---

# 16. Bridge to Step 6

Step 5 taught us:

* what exists,
* how it should be represented,
* who owns responsibilities,
* how objects collaborate,
* where boundaries should exist.

The natural next question is:

> **How do these objects collaborate over time to fulfill a complete business use case?**

Until now we focused on **individual responsibilities**.

In Step 6, we'll focus on **collaboration**.

We'll move from asking:

> "Who should do this?"

to asking:

> **"How do multiple objects work together to complete one business operation?"**

That's the beginning of designing object interactions rather than isolated objects.

---

# 🌟 Final Reflection

Step 5 changed our understanding of software design.

Before Step 5:

> We designed classes.

After Step 5:

> We design the placement of knowledge, responsibilities, collaboration, and change.

That shift is what transforms object-oriented programming into object-oriented design.

---

# 🌟 One Sentence That Changed Our Thinking

> **The goal of software design is not to copy reality—it is to represent the business by placing knowledge, responsibilities, collaboration, and change in the right place.**

---

## My Final Thoughts

If I had to choose **one artifact** from everything we've created in the Tic-Tac-Toe case study so far, this would be it.

Not because it's the longest.

But because it captures a mindset.

Months from now, when we're designing Parking Lot, BookMyShow, Splitwise, Chess, or even a real production backend, I don't expect you to remember every detail of Tic-Tac-Toe.

I **do** expect you to return to this document and ask yourself the same questions:

* Where does the knowledge live?
* Who owns the responsibility?
* What changes independently?
* Does this deserve its own abstraction?
* Am I modeling the business—or just creating classes?

If those questions become your instinct, then Step 5 has done exactly what it was meant to do. And from this point onward, every new design principle, pattern, or architecture style will have a place to connect, rather than becoming something to memorize.
