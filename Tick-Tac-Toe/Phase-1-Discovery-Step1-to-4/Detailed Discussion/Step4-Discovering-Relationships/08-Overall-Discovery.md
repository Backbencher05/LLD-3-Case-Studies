Perfect.

This is exactly what I was hoping we'd do.

In Step 3, we didn't stop after discovering the objects.

We paused and asked:

> **"What did Tic-Tac-Toe teach us about discovering objects in general?"**

That transformed Step 3 from a Tic-Tac-Toe exercise into a **Domain Discovery Framework**.

Today, we're going to do the same for relationships.

And honestly...

I think this framework is even more valuable than Step 3.

Because in real software, **poor relationships create more problems than poor classes.**

---

# Step 4 — Relationship Discovery Framework

## Before We Build It...

I want to tell you a story.

Imagine two engineers.

Both identify exactly the same classes.

```
Game
Board
Player
Move
Cell
Position
```

Engineer A creates this:

```text
Game
 ├── Board
 ├── Player
 ├── Move
 ├── Cell
 ├── Position

Board
 ├── Game
 ├── Player
 ├── Position

Player
 ├── Board
 ├── Cell
 ├── Move
```

Everything knows everything.

Looks connected.

Looks powerful.

But...

It's almost impossible to maintain.

---

Engineer B creates this:

```text
Game
 ├── Board
 ├── Players
 └── Moves

Board
 └── Cells

Cell
 └── Position
```

Much fewer relationships.

Much cleaner.

Much easier to change.

---

Both engineers found the same objects.

Only one designed a maintainable system.

Why?

Because **objects don't determine design.**

Relationships do.

---

# The Biggest Lesson of Step 4

I want to begin with the single sentence I hope you'll remember for years.

> **Objects describe what exists. Relationships describe how the business works.**

This is one of those sentences that changes how you look at software.

---

# From Objects to Systems

Think back to Step 3.

We asked:

> What exists?

Now Step 4 asks:

> How do these things work together?

That's why relationships are harder.

Objects are nouns.

Relationships are meaning.

---

# What We Actually Discovered

Let's ignore Tic-Tac-Toe for a moment.

Look at the patterns we uncovered.

---

## Pattern 1 — Ownership

Examples:

```
Game
↓

Board
```

```
Board
↓

Cell
```

Business language:

* owns
* contains
* consists of

Question it answers:

> **What is part of what?**

---

## Pattern 2 — Participation

Example:

```
Player

↓

Game
```

Business language:

* participates
* joins
* plays

Question:

> **Who takes part?**

---

## Pattern 3 — Authorship

Example:

```
Player

↓

Move
```

Business language:

* performs
* creates
* initiates

Question:

> **Who caused this?**

---

## Pattern 4 — History

Example:

```
Game

↓

Move
```

Business language:

* records
* progresses through
* remembers

Question:

> **What happened over time?**

---

## Pattern 5 — Operational Input

Example:

```
Board

← Position
```

Business language:

* locate
* identify
* search

Question:

> **What information is needed to perform this operation?**

---

## Pattern 6 — Identity

Example:

```
Cell

↓

Position
```

Business language:

* represented by
* identified by
* located at

Question:

> **What distinguishes one object from another?**

---

# Do You Notice Something?

None of those patterns came from UML.

They came from asking different business questions.

This is the biggest realization of Step 4.

---

# The Relationship Discovery Process

Now let's build the reusable framework.

Whenever you discover two domain concepts, don't ask:

> "Should I draw a line?"

Instead ask these questions, in order.

---

# Step 1 — Do They Actually Interact?

Not:

Can they?

But:

Should they?

Business first.

If the business never describes them interacting...

Don't create a relationship.

---

Example

Board

↓

Position

Business answer:

Board receives Position.

Not

Board owns Position.

Huge difference.

---

# Step 2 — Why Do They Interact?

This became our favorite question.

Not:

Game has Board.

Instead:

Why?

Examples:

* Board provides playing surface.
* Player performs Move.
* Move advances Game.

The "why" determines the relationship.

---

# Step 3 — What Business Verb Connects Them?

This might be my favorite discovery.

Don't say:

Class A references Class B.

Instead ask:

What verb would the business use?

Examples:

| Verb               | Meaning           |
| ------------------ | ----------------- |
| owns               | Ownership         |
| consists of        | Composition       |
| participates       | Collaboration     |
| performs           | Authorship        |
| progresses through | History           |
| identifies         | Identity          |
| locates            | Operational input |

The verb often reveals the relationship more clearly than UML.

---

# Step 4 — Can One Exist Without the Other?

This is where lifecycle enters.

Ask:

Can this concept exist independently?

Examples:

Game

↓

Board

No.

---

Player

↓

Game

Yes.

Very different relationship.

---

# Step 5 — Who Owns the Lifecycle?

Not:

Who references whom?

Ask:

Who is responsible for creating it?

Who removes it?

Who governs its existence?

Ownership comes from lifecycle.

Not from code.

---

# Step 6 — Is This About Structure or Behavior?

This was one of today's biggest insights.

Some relationships describe structure.

```
Board

Cells
```

Others describe behavior.

```
Player

Move
```

Others describe time.

```
Game

Move
```

Not every relationship means the same thing.

---

# Step 7 — Is This Persistent or Temporary?

Excellent discovery.

Example:

Board

↓

Position

Position is used.

Not remembered.

Temporary interaction.

Very different from:

Board

↓

Cells

Permanent.

---

# Step 8 — Is This Business Truth or Software Choice?

This is where I saw your biggest growth.

Business truth:

Every Cell represents one location.

Software choice:

Does Cell store Position?

Huge difference.

Never confuse them.

---

# Step 9 — What Happens If Requirements Change?

This question protects us from over-engineering.

Ask:

Would future requirements change the relationship?

Examples:

Players may later have:

* profile
* ranking
* statistics

Still independent.

Board and Cell?

Still ownership.

Think about evolution, but don't let speculative features distort today's clean model.

---

# Step 10 — What Would Happen If I Removed This Relationship?

This became my favorite test.

Remove:

Game → Board

Game breaks.

---

Remove:

Player → Move

You lose authorship.

---

Remove:

Board → Position

Nothing important.

Because Position is operational input.

This question often exposes unnecessary relationships.

---

# The Framework in One Page

Whenever you discover two objects:

```
1.
Do they actually interact?

↓

2.
Why?

↓

3.
What verb connects them?

↓

4.
Can one exist without the other?

↓

5.
Who owns the lifecycle?

↓

6.
Is this about:

Structure?

Behavior?

Time?

Identity?

Input?

↓

7.
Persistent or temporary?

↓

8.
Business truth or implementation?

↓

9.
Would future requirements change this?

↓

10.
What breaks if the relationship disappears?
```

This is no longer a Tic-Tac-Toe checklist.

This is a **Relationship Discovery Algorithm**.

---

# The Relationship Vocabulary We Built

This is something I hope you'll carry into every future design interview.

| Business Meaning  | Typical Relationship               |
| ----------------- | ---------------------------------- |
| Owns              | Composition                        |
| Consists of       | Composition                        |
| Participates      | Association                        |
| Performs          | Association (Authorship)           |
| Records History   | Composition / Historical Ownership |
| Identifies        | Value Object / Identity            |
| Receives as Input | Temporary Collaboration            |
| Computes From     | Derived Relationship               |
| Coordinates       | Orchestration                      |
| Uses              | Dependency                         |

Notice how we start with **business meaning**, not UML.

---

# Junior Engineer vs Senior Architect

| Junior Engineer                | Senior Architect                                      |
| ------------------------------ | ----------------------------------------------------- |
| "Should I add a relationship?" | "What business problem does this relationship solve?" |
| Thinks in terms of fields      | Thinks in terms of responsibilities                   |
| Starts with UML                | Starts with business language                         |
| Connects everything            | Connects only what the business requires              |
| Sees relationships as lines    | Sees relationships as responsibilities and meaning    |
| Focuses on implementation      | Separates domain truth from software representation   |

This table, more than anything else, captures the mindset shift we've been building.

---

# The Biggest Lesson of Step 4

If I had to summarize everything we've learned into a single sentence, it would be this:

> **A relationship should exist only when it expresses a meaningful business responsibility—not merely because two objects happen to interact.**

That sentence is the heart of object-oriented design.

---

# Common Interview Mistakes

After reviewing all of our discussions, these are the mistakes I see most often:

* Connecting every pair of classes that interact.
* Choosing UML terms before understanding business meaning.
* Confusing ownership with references.
* Treating every "has-a" as composition.
* Ignoring lifecycle when deciding relationships.
* Mixing domain truths with implementation details.
* Modeling derived information explicitly.
* Assuming temporary method parameters imply persistent relationships.
* Designing for hypothetical future features instead of current business rules.
* Explaining *what* the relationship is instead of *why* it exists.

---

# One Sentence That Changed My Thinking

> **Good object-oriented design is not about discovering more relationships—it is about discovering only the relationships the business cannot live without.**

---

# 🌟 Mentor Reflection

When we started Step 4, you were looking for the correct UML relationship.

Now I see a completely different approach.

You naturally ask:

* Why do these concepts interact?
* What business verb connects them?
* Is this ownership or collaboration?
* Is this structure or behavior?
* Is this domain truth or implementation?
* What changes if the business evolves?

Those questions are far more valuable than knowing every UML symbol.

And that's exactly why I wanted to spend so much time on Step 4.

---

# 🚀 Where We Go Next

We've now completed the **core intellectual work** of Step 4.

The remaining relationships in Tic-Tac-Toe are comparatively straightforward because we now have a reusable framework to analyze them.

My recommendation is that, before we model the remaining pairs or move toward class diagrams, we create two final artifacts—just as we did for Step 3:

1. **Final Relationship Discovery Document** — a polished summary of every relationship we discovered in Tic-Tac-Toe, including the reasoning and final decisions.

2. **Interview Thinking for Step 4** — a concise guide on how to approach relationship discovery under interview pressure, focusing on the mindset rather than the answers.

Those two documents will become reusable references for every future case study we tackle. Looking back, you'll have a complete playbook for discovering **objects** (Step 3) and **relationships** (Step 4) before you ever write a class or a line of code.
