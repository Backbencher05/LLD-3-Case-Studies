Excellent. This is where design starts becoming **architecture**.

In Step 3, we asked:

> **"What exists in this domain?"**

Now Step 4 asks something much deeper:

> **"How does reality connect these things together?"**

That is a fundamentally different question.

Many engineers think LLD is about classes.

Senior engineers know:

> **LLD is actually about relationships. Classes are only containers. Relationships describe the system.**

---

# Before We Begin Step 4

I don't want to immediately draw a class diagram.

That would be the same mistake many engineers make.

Instead, let's understand **why relationships exist at all.**

---

# Step 4 — Discovering Relationships

Let's forget software for a few minutes.

Imagine I ask you to describe your family.

You could list:

* Father
* Mother
* Brother
* Sister

Have I understood your family?

No.

Because I only know the **objects**.

I don't know how they are connected.

The real understanding comes from statements like:

* Father is married to Mother.
* Brother is child of Father.
* Sister is sibling of Brother.

Notice something interesting.

The people already existed.

Relationships created the **system**.

Without relationships...

...they're just isolated objects.

---

## This is exactly what happened in Step 3.

We discovered:

* Game
* Board
* Player
* Bot
* Cell
* Position
* Move
* WinningCondition

Right now they are like strangers standing in a room.

Step 4 introduces them to one another.

---

# The Biggest Shift in Thinking

A junior engineer often thinks:

> "Now that I have classes, I'll connect them."

A senior architect asks:

> **"Does reality itself say these two things are connected?"**

This sounds like a tiny wording difference.

It isn't.

It changes everything.

---

Imagine these two classes:

```
Player

Board
```

Should they have a relationship?

Many beginners immediately answer:

"Yes."

Why?

Because both appear in the game.

But simply existing together doesn't imply a direct relationship.

That assumption creates unnecessary coupling.

---

# Engineering Principle #1

> **Objects should not know each other merely because they exist in the same system.**

This principle alone prevents countless poor designs.

---

# Why Step 4 Is Difficult

Because relationships are invisible.

Objects are easy.

You can see them.

Relationships require reasoning.

Consider a company.

Objects:

* Employee
* Department
* Salary
* Manager
* Office

Easy.

But now ask:

Who owns whom?

Who references whom?

Who should know about whom?

Should Salary know Employee?

Should Employee know Salary?

Should Department know Manager?

Should Manager know Department?

Suddenly...

Design begins.

---

# The Real Goal of Step 4

Notice something important.

We are **not** trying to draw arrows.

We are trying to answer:

> **Who is responsible for whom?**

That question eventually determines:

* ownership
* lifecycle
* coupling
* navigation
* responsibilities

Long before UML.

---

# Our Process for Step 4

Just like Step 3 had a repeatable discovery process...

Step 4 will have one too.

We will never randomly connect objects.

We'll investigate each possible relationship using the same engineering process.

---

## Relationship Discovery Framework

For every pair of objects, we'll ask:

### Question 1

**Do these two concepts actually interact in the business?**

If no...

No relationship.

Simple.

---

### Question 2

If they interact...

Who starts the interaction?

---

### Question 3

Who owns whom?

Ownership matters because it often determines lifecycle.

---

### Question 4

Can one exist without the other?

This tells us whether the relationship is strong or weak.

---

### Question 5

Would future requirements likely change this relationship?

If yes...

Avoid tight coupling.

---

### Question 6

Does one merely use the other...

...or permanently contain it?

Huge difference.

---

### Question 7

Who should know about whom?

This is probably the most important design question in LLD.

---

These seven questions can be reused in almost every object-oriented design interview, regardless of the domain.

---

# The Relationships We Will Eventually Discover

Without deciding them yet, these are the candidate pairs we'll examine:

| Candidate               | Should They Be Related? |
| ----------------------- | ----------------------- |
| Game ↔ Board            | ?                       |
| Game ↔ Player           | ?                       |
| Board ↔ Cell            | ?                       |
| Player ↔ Move           | ?                       |
| Move ↔ Position         | ?                       |
| Game ↔ WinningCondition | ?                       |
| Bot ↔ Player            | ?                       |
| Board ↔ Position        | ?                       |
| Cell ↔ Position         | ?                       |
| Player ↔ Symbol         | ?                       |
| Game ↔ Move             | ?                       |

Some will become strong relationships.

Some weak.

Some will disappear entirely.

And that's perfectly fine.

---

# A New Habit We Will Build

From now on, every time you propose a relationship, I will ask you one question first:

> **Why should these two objects know each other?**

Not

> "Can they?"

But

> "Should they?"

That single word—**should**—is what distinguishes thoughtful design from accidental coupling.

---

# Junior Engineer vs Senior Architect

| Junior Engineer                    | Senior Architect                         |
| ---------------------------------- | ---------------------------------------- |
| Connects everything that interacts | Connects only what must interact         |
| Thinks in terms of classes         | Thinks in terms of responsibilities      |
| Focuses on implementation          | Focuses on ownership and lifecycle       |
| Starts with UML                    | Starts with business reality             |
| Optimizes for convenience          | Optimizes for maintainability and change |

---

# Interview Perspective

Interviewers are rarely checking whether you know UML notation by heart.

They are evaluating whether you can justify your design choices.

A strong answer sounds like:

> "I related `Game` and `Board` because the board's lifecycle is governed by the game. A board doesn't make sense independently in this system, so `Game` should own it."

A weaker answer is:

> "I connected them because every game has a board."

The first explains the **reasoning**. The second only states a fact.

---

# Biggest Engineering Lesson

**Objects describe what exists. Relationships describe how the system behaves. A good design is defined less by the number of classes and more by the quality of the relationships between them.**

---

# Common Interview Mistakes

* Drawing relationships before understanding business interactions.
* Connecting every pair of objects that interacts.
* Ignoring ownership and lifecycle.
* Assuming bidirectional references are always needed.
* Confusing "uses" with "owns."

---

# One Sentence That Changed My Thinking

> **A class becomes part of a system not because it exists, but because of the responsibilities it shares through carefully chosen relationships.**

---

# 🎯 Engineering Checkpoint (Your Turn)

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
