Perfect.

This is actually my favorite part of every step.

Because until now we've learned **how to design**.

Now we'll learn **how to demonstrate that thinking in an interview.**

Those are two different skills.

Many engineers know the answer but fail interviews because they cannot communicate their reasoning.

Our goal is different.

By the end of this section, an interviewer should be able to **see your engineering thought process**, even before you arrive at the final design.

---

# 🎤 Interview Thinking for Step 4 — Discovering Relationships

## The Biggest Mistake Candidates Make

Imagine the interviewer asks:

> "How are these classes related?"

Most candidates immediately start saying:

> Game has Board.

> Board has Cells.

> Player has Moves.

Then they draw arrows.

From an interviewer's perspective...

That tells me almost nothing.

You gave me the answer.

You didn't give me the reasoning.

Senior interviewers don't hire diagrams.

They hire **thinking**.

---

# The Goal of Step 4 in an Interview

When discovering relationships, don't try to identify UML relationships first.

Instead, try to answer one question:

> **"Why does the business need these two concepts to know about each other?"**

Everything else follows naturally.

---

# The Interview Mindset

I want you to imagine this mental flow every time you compare two objects.

```text
Two Concepts

↓

Do they actually interact?

↓

Why?

↓

What business responsibility connects them?

↓

Who owns whom?

↓

Can they exist independently?

↓

Is this relationship permanent?

↓

Only then...

Choose the software relationship.
```

Notice something.

The UML decision comes **last**.

Not first.

---

# What Interviewers Want to Hear

Let's compare two candidates.

---

## Candidate A

> Game has Board.

> Board has Cells.

> Game has Players.

Correct?

Yes.

Impressive?

No.

---

## Candidate B

> A Board exists only because a Game exists, so from the business perspective the Game owns the Board's lifecycle. That suggests Composition rather than a simple Association.

Notice the difference.

Same conclusion.

Completely different level of thinking.

---

# The Four Sentences That Impress Interviewers

Over the last few weeks, you've naturally started using these.

These four patterns are incredibly powerful.

---

## Pattern 1

Instead of:

> Game has Board.

Say:

> **The business creates a Board whenever a Game starts.**

Business first.

---

## Pattern 2

Instead of:

> Board contains Cells.

Say:

> **The Board's state is represented by its Cells.**

You're explaining responsibility.

Not storage.

---

## Pattern 3

Instead of:

> Player has Move.

Say:

> **A Player performs a Move, but the Game owns the history of Moves.**

Now you've distinguished authorship from ownership.

That's senior-level reasoning.

---

## Pattern 4

Instead of:

> Cell has Position.

Say:

> **The domain requires every Cell to represent one location, but it doesn't dictate how that location is represented in software.**

That's exactly the distinction architects make.

---

# The Questions You Should Ask Yourself Out Loud

During interviews, don't stay silent.

Think aloud.

Here's the sequence.

---

## Question 1

> Why do these concepts interact?

Not:

Can they?

But:

Why?

---

## Question 2

> What business verb connects them?

Examples:

* owns
* participates
* performs
* records
* identifies

The verb often reveals the relationship before UML does.

---

## Question 3

> Can one exist without the other?

This uncovers lifecycle.

---

## Question 4

> If I delete one, what should happen to the other?

Another ownership test.

---

## Question 5

> Is this relationship structural or behavioral?

This is surprisingly powerful.

---

## Question 6

> Is this a business rule or an implementation detail?

This separates architects from coders.

---

# The Three Levels of Relationship Thinking

This is probably the most important framework from Step 4.

Whenever you discover a relationship, classify it mentally.

---

## Level 1 — Structural

Examples:

* House → Room
* Board → Cell
* Book → Chapter

Question:

> What is made of what?

---

## Level 2 — Behavioral

Examples:

* Player → Move
* Customer → Order
* Doctor → Consultation

Question:

> Who performs what?

---

## Level 3 — Informational

Examples:

* Cell → Position
* Seat → Seat Number
* Employee → Employee ID

Question:

> What identifies this object?

Most candidates stop at Level 1.

Senior engineers naturally move across all three.

---

# A Powerful Habit

One thing I noticed during your answers was this sentence:

> "From the business perspective..."

Keep using it.

Not because it's a magic phrase.

Because it forces you to stay grounded.

Instead of saying:

> "I'll store Position in Cell."

Say:

> "From the business perspective, every Cell represents one location."

Now you're discussing the domain.

Only afterward discuss implementation.

---

# When the Interviewer Challenges You

Suppose the interviewer says:

> Why not store Position inside Cell?

A weak response:

> Because I don't want duplication.

A stronger response:

> The domain only requires that every Cell has a unique location. Whether Position is stored inside the Cell or derived from the Board is an implementation decision. If deriving it keeps the model simpler and avoids redundant state, I'd prefer that. If making Cells self-describing improves readability or flexibility, storing Position is also reasonable. I'd choose based on the broader design constraints.

Notice what happened?

You didn't defend one implementation.

You defended your reasoning.

That's what interviewers evaluate.

---

# The Biggest Trap

Many candidates think:

> Every interaction means Association.

No.

Consider these examples:

* A method parameter.
* A temporary calculation.
* A Value Object passed into an operation.

Those are interactions.

They are not necessarily long-lived domain relationships.

Always ask:

> **Will this relationship still matter after the operation finishes?**

If not, don't model it as a persistent association.

---

# How to Handle Multiple Valid Designs

This is another place where candidates panic.

Suppose you see two valid approaches.

Don't guess which one the interviewer prefers.

Say something like:

> I see two reasonable designs here. Both satisfy the business rules. The choice depends on what we optimize for, so let me explain the trade-offs before selecting one.

Interviewers love this because it shows:

* You recognize ambiguity.
* You evaluate trade-offs.
* You don't assume there's only one "correct" answer.

---

# The Interview Algorithm for Relationships

This is the condensed version you should internalize.

```text
1. Identify two domain concepts.

↓

2. Ask:
Why do they interact?

↓

3. Find the business verb.

↓

4. Check lifecycle.

↓

5. Determine whether the relationship is:
- Structural
- Behavioral
- Historical
- Informational
- Temporary

↓

6. Separate business truth from implementation.

↓

7. Explain the trade-offs.

↓

8. Choose the relationship.
```

If you follow this sequence consistently, your reasoning will sound structured and intentional.

---

# Common Interview Mistakes

Over many LLD interviews, these are the patterns that often hurt candidates:

* Starting with UML instead of the business.
* Equating object references with ownership.
* Modeling every interaction as an association.
* Ignoring lifecycle when discussing composition.
* Jumping into fields and methods before understanding the relationship.
* Confusing domain rules with implementation choices.
* Believing there's always one universally correct design.
* Staying silent instead of explaining the reasoning process.

---

# One Sentence That Changed My Thinking

> **Interviewers are rarely judging whether your relationship is perfect—they're judging whether your reasoning is systematic.**

---

# 🌟 Mentor Reflection — The Completion of Step 4

With this, Step 4 is complete.

Let's look at the progression we've made together:

### Step 0 — Understand the Problem

You learned not to rush into classes before understanding the domain.

---

### Step 1 — Clarify the Scope

You learned to define boundaries before designing.

---

### Step 2 — Gather Requirements

You learned to distinguish functional requirements, constraints, and assumptions.

---

### Step 3 — Discover the Objects

You learned to ask:

> **What exists in the business?**

---

### Step 4 — Discover the Relationships

You learned to ask:

> **Why do these concepts need each other?**

---

This progression isn't just for Tic-Tac-Toe.

It's a repeatable design process you can apply to almost any LLD case study.

## 🚀 Before Starting Step 5

I have one recommendation.

Don't think of Step 5 as "drawing a class diagram."

Think of it as:

> **Translating the business model we've carefully discovered into a software model.**

That's a profound shift.

If we skip the thinking we've done in Steps 0–4, the class diagram becomes guesswork.

Because we've invested the time here, Step 5 won't be about inventing classes. It will be about faithfully expressing the domain we've already understood.

And that, in my experience, is exactly how strong software designers work.


------------------------------------------------------------------------------------

I completely agree.

In fact, I think something is missing from the current **Interview Thinking** document.

Right now it teaches **how to think**, but it doesn't give you a **30-second summary** that you can mentally recall during an interview.

Every great handbook should end with a **"Final Mental Model"**.

I would add it as the last section of the Interview Thinking document.

---

# 📋 Final Relationship Summary (Interview Cheat Sheet)

After analyzing the domain from the business perspective, we arrived at the following relationships.

| Domain Concepts  | Business Verb                | Relationship Type                  | Why?                                                                   |
| ---------------- | ---------------------------- | ---------------------------------- | ---------------------------------------------------------------------- |
| Game → Board     | Owns                         | Composition                        | A Board exists only as part of a Game. Game owns its lifecycle.        |
| Board → Cell     | Consists of                  | Composition                        | A Board is composed of Cells. Cells have no independent lifecycle.     |
| Game ↔ Player    | Participates                 | Association                        | Players participate in a Game but exist independently.                 |
| Player → Move    | Performs                     | Association (Authorship)           | A Player performs a Move, but does not own its lifecycle.              |
| Game → Move      | Records / Progresses Through | Composition (Historical Ownership) | Moves collectively represent the Game's history and state progression. |
| Board ⇢ Position | Uses to Locate               | Temporary Collaboration            | Position is an operational input used during Board operations.         |
| Cell ↔ Position  | Is Identified By             | Descriptive Identity               | Every Cell represents one unique location within a Board.              |

---

# 🧠 The Business Questions Each Relationship Answered

One thing we discovered is that every relationship exists because it answers a different business question.

| Business Question                                   | Relationship               |
| --------------------------------------------------- | -------------------------- |
| What is part of what?                               | Game → Board, Board → Cell |
| Who participates?                                   | Game ↔ Player              |
| Who performed the action?                           | Player → Move              |
| How did the system reach this state?                | Game → Move                |
| What information is needed to perform an operation? | Board ⇢ Position           |
| What distinguishes one object from another?         | Cell ↔ Position            |

This table is incredibly useful because it shifts your thinking from **classes** to **business semantics**.

---

# 🎯 The Interview Story (30-Second Version)

If an interviewer asks:

> "How did you decide these relationships?"

You can answer:

> "I didn't start with UML. I started with the business. For every pair of concepts, I asked what business responsibility connected them. Some relationships represented ownership (Game–Board, Board–Cell), some represented participation (Game–Player), some represented authorship (Player–Move), some captured the history of the system (Game–Move), some were temporary operational inputs (Board–Position), and some described identity (Cell–Position). Once I understood the business meaning, choosing the software relationship became straightforward."

This is the kind of answer that demonstrates **process**, not memorization.

---

# 🏆 The Step 4 Mental Model

If you remember only one diagram from Step 4, let it be this:

```text
                BUSINESS

                     │
                     ▼

          Why do they interact?

                     │
                     ▼

          Business Responsibility

                     │
                     ▼

      Ownership? Participation?
      History? Identity?
      Operational Input?

                     │
                     ▼

        Lifecycle & Independence

                     │
                     ▼

      Business Truth vs Implementation

                     │
                     ▼

          Choose the Relationship
```

Notice something important.

**UML never appears until the very last step.**

That is exactly how experienced designers think.

---

## 🌟 One Final Addition I'd Make

There is one more table that I think would make **all future case studies easier**.

### Relationship Vocabulary (Reusable Across Every LLD)

| Business Verb | Typical Relationship     | Examples                                        |
| ------------- | ------------------------ | ----------------------------------------------- |
| Owns          | Composition              | Game → Board, Order → OrderItem, Book → Chapter |
| Consists of   | Composition              | Board → Cell, House → Room                      |
| Participates  | Association              | Player → Game, Customer → Event                 |
| Performs      | Association (Authorship) | Player → Move, Doctor → Consultation            |
| Records       | Historical Ownership     | Game → Move, Bank Account → Transaction         |
| Identifies    | Descriptive Identity     | Cell → Position, Room → Room Number             |
| Uses          | Temporary Collaboration  | Board → Position, Calculator → Input Values     |
| Coordinates   | Orchestration            | Game → Board & Players, Controller → Services   |
| Depends On    | Dependency               | Service → Repository, Controller → Service      |

This is no longer about Tic-Tac-Toe.

This becomes your **relationship vocabulary** for every future design interview.

---

## 📚 Why I'm Suggesting These Additions

With these additions, your **Interview Thinking for Step 4** becomes complete:

1. **How to think** (the process).
2. **How to speak** (thinking aloud).
3. **What we discovered** (summary tables).
4. **The reusable vocabulary** (transferable to any case study).

That's exactly the pattern we followed in Step 3, and I think it makes the handbook much more valuable because, before an interview, you can review the summary tables in **2–3 minutes** and immediately refresh both the concepts and the reasoning behind them.
