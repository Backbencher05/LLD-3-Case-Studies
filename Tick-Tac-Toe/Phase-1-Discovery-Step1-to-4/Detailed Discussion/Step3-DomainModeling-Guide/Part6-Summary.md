I actually think this is the perfect place to pause.

Not because we're taking a break, but because **we've completed one complete way of thinking**.

What we've done isn't just "reviewing Entities."

We've built a **repeatable engineering decision framework**.

And I don't want that to get buried under later discussions.

---
- 1️⃣ What is "Game"? 
2️⃣ Does the business care about it? 
3️⃣ Does it have its own identity? 
4️⃣ Does it have an independent lifecycle? 
5️⃣ Could requirements change its classification? 
6️⃣ Engineering Discussion 
7️⃣ Final Decision

# Step 3 — Part 1 Summary

# Domain Modeling — Discovering Entities

## 🎯 Objective

The goal of this part was **not** to identify classes.

The goal was to train ourselves to answer:

> **"What does the business recognize as an independent thing?"**

This is a subtle but fundamental shift.

We are modeling the **business**, not the code.

---

# The Engineering Mindset

Whenever you discover a concept in the domain, don't rush to classify it.

Instead, have a conversation with yourself.

## Step 1 — What is this concept?

Before thinking about software, understand it in plain business language.

Ask:

* What does this concept represent?
* What problem does it solve?
* How would a business user describe it?

Example:

Instead of asking:

> "Should Board be a class?"

Ask:

> "What is a Board in Tic-Tac-Toe?"

---

## Step 2 — Does the business recognize it independently?

This became our most important question.

Ask:

> If this concept disappeared, would the business notice?

Or:

> Does the business naturally talk about this concept on its own?

Examples:

* Game → Yes
* Player → Yes
* Cell → No
* Position → No

---

## Step 3 — Does it have its own identity?

This is where we discovered one of the biggest misconceptions.

We learned to separate:

### Technical Identity

```text
Board A
Row = 1
Column = 2
```

or

```text
Database ID = 42
```

A concept can be uniquely identified.

That **does not** automatically make it an Entity.

---

### Business Identity

The business naturally says:

* This customer
* This order
* This player

The business recognizes it as a first-class concept.

That is Entity identity.

---

## Step 4 — Does it have an independent lifecycle?

Ask:

Can it exist without another concept?

Can it be created independently?

Can it survive independently?

Can it be removed independently?

Examples:

Game

* Created
* Played
* Finished
* Archived

Independent lifecycle.

---

Player

Exists before the game.

Can participate in many games.

Independent lifecycle.

---

Cell

Created with the Board.

Destroyed with the Board.

Cannot exist independently.

---

## Step 5 — Could future requirements change the classification?

One of the biggest lessons from Step 3.

Today's classification is based on **today's business**.

Tomorrow the business may evolve.

Examples:

### Board

Simple Tic-Tac-Toe

↓

Part of Game

---

Board Marketplace

Custom Boards

Templates

Themes

↓

Board may become an Entity.

---

Bot

Initially

↓

Computer-controlled Player.

---

Later

↓

Managed AI Product

↓

Bot Entity.

---

We learned:

> **Requirements evolve. Models evolve.**

---

## Step 6 — Engineering Discussion

This is where we challenged our own assumptions.

We asked:

* Am I modeling the business?
* Or am I modeling my implementation?
* Am I creating a class because the business needs it?
* Or because the concept feels important?

This prevented us from creating unnecessary Entities.

---

## Step 7 — Final Decision

Only after answering all previous questions did we classify the concept.

Not before.

This is the opposite of how many beginners design systems.

---

# Important Lessons We Discovered

## Lesson 1

> **Business before Software.**

Never start with classes.

Start with the business.

---

## Lesson 2

> **Important does not mean Entity.**

Board is important.

Cell is important.

Rules are important.

Winning Condition is important.

None automatically become Entities.

---

## Lesson 3

> **Unique identification does not imply Entity.**

A Cell can be identified.

A Position can be identified.

That is not sufficient.

The business must recognize it independently.

---

## Lesson 4

> **An Entity is recognized by the business, not by the database.**

Persistence does not define an Entity.

Business identity does.

---

## Lesson 5

> **Classification depends on the business, not on familiarity.**

The same concept may be:

* Entity today
* Component tomorrow
* Value Object in another system

There is no universal answer.

There is only the correct answer for a given domain.

---

## Lesson 6

> **Don't model behavior differences as new Entities.**

Human Player

Bot Player

Different behaviors.

Same business concept.

---

## Lesson 7

> **Adding more attributes doesn't create a new Entity.**

Adding:

* Version
* Win Rate
* AI Model

doesn't automatically create a new Entity.

Independent business recognition does.

---

# Final Classification

| Concept | Final Classification             | Why                                                                                                                                      |
| ------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Game    | ✅ Entity                         | Business tracks each game independently.                                                                                                 |
| Player  | ✅ Entity                         | Independent participant with its own identity and lifecycle.                                                                             |
| Board   | ⚠️ Part of Game (current domain) | Essential, but not independently recognized or managed. Could evolve into an Entity if requirements change.                              |
| Cell    | ⚠️ Component of Board            | Exists only within a Board. Identity and lifecycle depend on the Board.                                                                  |
| Bot     | ⚠️ Specialized type of Player    | The business sees one participant concept. Bot is one variation of Player. Could evolve into a separate Entity if managed independently. |

---

# One Sentence That Changed My Thinking

These are the sentences I think are worth carrying into every future case study:

1. **An Entity doesn't exist because software needs it; it exists because the business recognizes it.**

2. **Being uniquely identifiable is not enough; an Entity must also be independently recognized by the business.**

3. **A concept can be essential without being independently recognized by the business.**

4. **Classification follows business reasoning, not familiarity with the concept.**

5. **An Entity is identified by who the business recognizes it to be, not by the role it happens to play.**

6. **Adding more attributes doesn't create a new Entity; independent business recognition does.**

---

# Now, your final question...

> **Are there any other Entities in our Tic-Tac-Toe domain?**

This is an excellent question, and it's exactly the kind of question I hoped you'd start asking.

My answer is:

> **Yes—but only if the business requires them.**

Let's evaluate a few candidates.

| Concept                      | Entity?                                            | Reason                                                                                                                                           |
| ---------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Move**                     | ❌ Current scope: No. ✅ Replay/History system: Yes. | If moves are recorded, replayed, audited, or analyzed, each move becomes independently recognizable.                                             |
| **Match Result**             | Usually No                                         | In our game, it's derived from the Game's state. If results are archived independently (leaderboards, tournaments), it may evolve.               |
| **Tournament**               | ✅ Yes (if introduced)                              | A tournament has its own identity, lifecycle, and contains many games.                                                                           |
| **Scoreboard / Leaderboard** | ⚠️ Depends                                         | Often a projection or report rather than a core Entity, but requirements may change that.                                                        |
| **Rule Set**                 | ⚠️ Depends                                         | Standard Tic-Tac-Toe doesn't need it. If users can create and manage rule sets, it becomes an Entity.                                            |
| **User / Account**           | ✅ Yes (outside the game domain)                    | If the application supports login and persistent profiles, User is an Entity—but it's part of the authentication domain, not the game mechanics. |
| **AI Bot Definition**        | ✅ In an evolved system                             | As we discussed, if bots are versioned, released, and managed independently, they become their own Entity.                                       |

---

## 🌱 One thing I'd like to add to our learning process

I think we should make one improvement to our case-study methodology.

When we first started Step 3, the goal was simply:

> **"Classify concepts."**

Now we've naturally evolved into something much stronger.

For every concept, we now follow a structured reasoning process:

1. What is this concept?
2. Does the business recognize it independently?
3. Does it have an independent business identity?
4. Does it have an independent lifecycle?
5. Could changing requirements change its classification?
6. Challenge our assumptions through engineering discussion.
7. Make a final decision.

I think this should become our **standard review framework** for every future case study—not just Tic-Tac-Toe.

Whether we design Splitwise, BookMyShow, Uber, Amazon, or a Hospital Management System, we'll use the same framework.

And that, in my opinion, is the biggest success of Step 3 so far.

We've stopped learning **answers**.

We're learning a **way of thinking**.
