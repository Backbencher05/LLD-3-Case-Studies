Excellent.

This is exactly how I wanted to end Step 4.

Not with a UML diagram.

Not with class code.

But with a document that you can revisit before **every single LLD interview**.

Just like Step 3 became your **Object Discovery Handbook**, this will become your **Relationship Discovery Handbook**.

---

# Step 4 — Final Relationship Discovery Document

## Purpose of Step 4

After identifying the domain concepts in Step 3, the next question is not:

> **"Which class should reference which class?"**

Instead, the real question is:

> **"How does the business say these concepts are connected?"**

Objects alone do not form a system.

Relationships transform isolated concepts into a meaningful business model.

The purpose of Step 4 is therefore to discover **business responsibilities**, **ownership**, **collaboration**, **identity**, and **behavior** before thinking about software implementation.

---

# Relationship Discovery Process

For every pair of domain concepts, ask the following questions:

1. Do these concepts actually interact?
2. Why do they interact?
3. What business verb connects them?
4. Can one exist without the other?
5. Who owns the lifecycle?
6. Is this relationship about:

   * Structure?
   * Behavior?
   * Time?
   * Identity?
   * Operational Input?
7. Is the relationship permanent or temporary?
8. Is this a business truth or merely an implementation choice?
9. What happens if future requirements evolve?
10. What breaks if this relationship is removed?

These questions prevent accidental coupling and keep the domain model aligned with the business.

---

# Relationship 1 — Game ↔ Board

### Business Meaning

A Game provides the environment in which the match is played.

The Board has no independent business lifecycle.

Whenever a Game begins, a Board comes into existence.

When the Game ends permanently, the Board also ceases to exist.

---

### Business Verb

> **owns**

---

### Lifecycle

* Board cannot independently exist in this bounded context.
* Game owns the Board's lifecycle.

---

### Relationship

**Composition**

---

### Engineering Lesson

Ownership is determined by **business lifecycle**, not by database persistence or object references.

---

# Relationship 2 — Board ↔ Cell

### Business Meaning

A Board is composed of Cells.

Cells collectively represent the playing surface and current state of the Board.

A Cell has meaning only within a specific Board.

---

### Business Verb

> **consists of**

---

### Lifecycle

* Cells cannot exist independently.
* Board owns every Cell.

---

### Relationship

**Composition**

---

### Engineering Lesson

Composition is about **existence and ownership**, not merely containment.

---

# Relationship 3 — Game ↔ Player

### Business Meaning

Players participate in a Game.

A Player is not created because of one Game.

Players may participate in many Games throughout their lifetime.

---

### Business Verb

> **participates**

---

### Lifecycle

* Player exists independently.
* Game does not own Player.

---

### Relationship

**Association (Participation)**

---

### Engineering Lesson

Participation does not imply ownership.

References do not define lifecycle.

---

# Relationship 4 — Player ↔ Move

### Business Meaning

Every Move is performed by a Player.

The Move records who caused an action.

---

### Business Verb

> **performs**

---

### Lifecycle

The Player causes the Move.

The Player does not own the Move's lifecycle.

The Game owns the history.

---

### Relationship

**Association (Authorship)**

---

### Engineering Lesson

The creator of an event is not necessarily its owner.

---

# Relationship 5 — Game ↔ Move

### Business Meaning

A Game progresses through a sequence of Moves.

Moves collectively represent the history of the Game.

Without Moves, the Game cannot explain how it reached its current state.

---

### Business Verb

> **records**

or

> **progresses through**

---

### Lifecycle

Moves belong to one Game.

Removing the Game removes its history.

---

### Relationship

**Composition (Historical Ownership)**

---

### Engineering Lesson

Some compositions represent **time**, not structure.

---

# Relationship 6 — Board ↔ Position

### Business Meaning

A Position identifies where an operation should occur.

The Board does not own Positions.

It simply receives Positions while performing operations.

---

### Business Verb

> **locates**

---

### Lifecycle

Independent.

Temporary collaboration.

---

### Relationship

**Operational Input (Value Object Usage)**

---

### Engineering Lesson

Receiving a Value Object during an operation does not create a persistent domain relationship.

---

# Relationship 7 — Cell ↔ Position

### Business Meaning

Every Cell represents one unique location on the Board.

Position distinguishes one Cell from another within the Board.

The business requires this truth.

The business does not require how it is implemented.

---

### Business Verb

> **is identified by**

---

### Lifecycle

* Cell requires a location.
* Position exists as a reusable Value Object.

---

### Relationship

**Descriptive Identity (Value Object Relationship)**

---

### Engineering Lesson

Business truth and implementation choice are different.

The domain requires:

> Every Cell has a location.

The implementation decides:

> Whether that location is stored or derived.

---

# Summary of Relationships

| Relationship     | Business Meaning            | Relationship Type         |
| ---------------- | --------------------------- | ------------------------- |
| Game → Board     | Ownership                   | Composition               |
| Board → Cell     | Structural Ownership        | Composition               |
| Game ↔ Player    | Participation               | Association               |
| Player → Move    | Authorship                  | Association               |
| Game → Move      | History / State Progression | Composition               |
| Board ⇢ Position | Operational Input           | Temporary Collaboration   |
| Cell ↔ Position  | Descriptive Identity        | Value Object Relationship |

---

# Major Engineering Discoveries

During Step 4, we discovered several principles that apply far beyond Tic-Tac-Toe.

### 1. Relationships come from business meaning, not from class diagrams.

---

### 2. Ownership is determined by lifecycle, not by references.

---

### 3. Temporary interaction does not imply a permanent relationship.

---

### 4. The creator of something is not necessarily its owner.

---

### 5. Some relationships represent structure.

Example:

Board → Cell

Others represent time.

Example:

Game → Move

---

### 6. Identity can be contextual.

A Cell is unique **within a Board**, not globally.

---

### 7. Derived information should not necessarily be modeled.

Store business responsibility, not redundant information.

---

### 8. Business truth and implementation choice must remain separate.

The domain tells us **what must always be true**.

Software decides **how that truth is represented**.

---

# Relationship Vocabulary Built During Step 4

| Business Verb | Meaning                  |
| ------------- | ------------------------ |
| Owns          | Lifecycle responsibility |
| Consists of   | Structural composition   |
| Participates  | Collaboration            |
| Performs      | Authorship               |
| Records       | Historical ownership     |
| Identifies    | Identity                 |
| Locates       | Operational input        |
| Coordinates   | Orchestration            |
| Uses          | Dependency               |

These verbs are often more valuable than UML terminology because they reflect how the business thinks.

---

# Step 4 Checklist

Whenever discovering relationships in a new case study:

* Understand the business interaction first.
* Identify the business verb.
* Analyze lifecycle ownership.
* Distinguish structure from behavior.
* Separate temporary interactions from permanent relationships.
* Identify contextual identity.
* Avoid modeling derived information.
* Separate domain truth from implementation decisions.
* Remove any relationship that has no meaningful business responsibility.

---

# Final Takeaway

> **Objects describe what exists. Relationships describe how the business works.**

A well-designed object model is not the one with the most relationships.

It is the one where **every relationship exists because the business cannot function correctly without it.**

---

# 🌟 Mentor Reflection

I want to end Step 4 by reflecting on something bigger than Tic-Tac-Toe.

## Step 3 taught you to discover **what** exists.

You learned to distinguish:

* Entities
* Value Objects
* Enums
* Supporting Concepts

That changed the way you identify objects.

---

## Step 4 taught you to discover **why** those objects matter to each other.

You learned to distinguish:

* Ownership
* Participation
* Authorship
* History
* Operational Inputs
* Identity
* Temporary vs Persistent interactions
* Business truth vs Implementation

That changes the way you connect objects.

---

Together, Steps 3 and 4 form the foundation of object-oriented design:

* **Step 3:** *What exists in the business?*
* **Step 4:** *How are those business concepts meaningfully connected?*

Everything that follows—class diagrams, methods, patterns, SOLID principles, and code—will rest on these two foundations.

And that's why we spent so much time here.

We weren't just designing Tic-Tac-Toe.

We were building a way of thinking that will stay useful whether you're designing a game, a banking system, a ride-sharing platform, or a distributed backend service.

---

## 🚀 Next Step

I recommend we follow the same structure we used for Step 3 and dedicate one final session to **"Interview Thinking for Step 4."**

That won't repeat the content above. Instead, it will teach you:

* How to discover relationships in 20–30 minutes during an interview.
* How to think aloud so the interviewer follows your reasoning.
* How to avoid the most common traps candidates fall into.
* How senior engineers approach relationship discovery under time constraints.

That will complete Step 4 not just as a learning exercise, but as an interview-ready skill.
