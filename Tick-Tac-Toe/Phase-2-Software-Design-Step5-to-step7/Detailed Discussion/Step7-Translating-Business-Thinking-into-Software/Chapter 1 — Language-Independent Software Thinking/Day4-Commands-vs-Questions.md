Aditya...

Today is one of my favourite days in object-oriented design.

Because today we're going to discover something that looks incredibly simple...

...but quietly changes how you design APIs, methods, and even databases.

Today we're going to answer a question that almost every software engineer encounters every day, but very few consciously think about.

---

# 🚀 Step 7 — Day 4

# Commands vs Questions

Let's begin with a story.

---

# A Library Story

Imagine you walk into a library.

You say:

> "Please lend me this book."

The librarian performs work.

The world changes.

The book is now checked out.

Inventory changes.

Loan records change.

Availability changes.

---

Now imagine instead you ask:

> "Is this book available?"

The librarian simply answers.

Nothing changes.

The world remains exactly the same.

Interesting...

Both are interactions.

But they're fundamentally different.

---

# The Hidden Discovery

Not every interaction with an object has the same purpose.

Some interactions ask the object to **change something**.

Others ask the object to **tell us something**.

Those are different kinds of conversations.

---

# Back to Tic-Tac-Toe

Imagine the Game talks to the Board.

Conversation A:

> Board...

> Place this symbol.

The Board changes.

---

Conversation B:

> Board...

> Is Position (2,2) available?

The Board answers.

Nothing changes.

Same collaborator.

Different purpose.

---

# Another Example

WinningCondition.

Conversation A:

> Evaluate whether someone has won.

Question.

Does the board change?

No.

WinningCondition observes.

It answers.

That's all.

---

# A Restaurant Analogy

Customer:

> "Bring me coffee."

The restaurant changes the world.

Coffee is prepared.

Inventory changes.

An order is created.

---

Customer:

> "Do you serve coffee?"

Nothing changes.

Only information is exchanged.

---

Again...

Two conversations.

Completely different intentions.

---

# Why Does This Matter?

Because these two interactions create different expectations.

When I ask:

> Is this Cell empty?

I expect:

* no hidden work,
* no side effects,
* no state changes.

When I ask:

> Place my symbol.

I expect:

* something to change.

The kind of interaction shapes the trust between collaborators.

---

# A New Distinction

Today we'll discover two categories.

---

## Command

A command asks an object:

> **Please perform work that changes the state of your responsibility.**

Examples:

* Accept placement.
* Reset board.
* Start game.
* Change turn.

Commands may change the object's state.

---

## Question

A question asks an object:

> **Please tell me something you already know.**

Examples:

* Is the Cell empty?
* Has someone won?
* What is the current game state?
* Is this position valid?

Questions should not change the object.

They simply reveal information.

---

# A Small Thought Experiment

Suppose this happens.

Game asks:

> Board...

> Is Position (2,2) available?

But internally...

The Board secretly changes something.

Maybe it increments a counter.

Maybe it marks the Cell.

Maybe it changes the Board.

Now ask yourself.

Would you trust that question anymore?

Probably not.

Questions should feel safe.

That's why engineers care so much about separating them.

---

# The Bigger Picture

Let's connect everything we've learned.

```text id="t2lcr0"
Responsibility

↓

Behaviour

↓

Operations

↓

Boundaries

↓

Interaction Type   ← Today
```

We're now refining how collaborators communicate.

Not every interaction deserves the same expectations.

---

# 🎯 Step 7 — Day 4 Assignment

## Part A — Command or Question?

For each interaction, decide:

* Is it a **Command**?
* Is it a **Question**?

Explain **why**, not just the category.

---

### Game

* Start game
* Accept player's move
* Is the game over?
* Who is the current player?
* Change current player

---

### Board

* Accept placement
* Is this position valid?
* Is this Cell empty?
* Reveal board state
* Reset board

---

### Cell

* Store symbol
* Is Cell empty?
* Which symbol do you contain?

---

### WinningCondition

* Evaluate winner
* Has someone won?
* Which winning pattern matched?

---

## Part B — Trust

Imagine this interaction.

```text
Game

↓

Board

Is Position Available?
```

Scenario 1:

The Board secretly updates statistics every time this question is asked.

Would you consider that a good design?

Why?

---

Scenario 2:

A collaborator asks:

> "Board, place this symbol."

But nothing changes.

Is that a good command?

Why?

---

Scenario 3:

Suppose a question becomes extremely expensive to answer because the Board recalculates everything every time.

Should it stop being a question?

Or is expense different from behaviour?

Think carefully.

---

## Part C — Reflection

Complete these sentences.

> **Commands exist because...**

> **Questions exist because...**

Then answer:

> **Why does separating commands from questions make collaboration easier to understand?**

---

# 🌟 Engineering Checkpoint

Today's checkpoint is intentionally subtle.

> **If a collaborator cannot trust whether an interaction changes the world, what kinds of software problems might eventually appear?**

Don't answer in terms of code.

Answer in terms of trust, collaboration, predictability, and business behaviour.

---

# 🌟 One Sentence to Carry Forward

> **A command asks an object to fulfil a responsibility by changing its world; a question asks it to reveal knowledge without changing that world.**

---

# A Tiny Preview...

Tomorrow is the day we've been walking toward for weeks.

For the first time, we'll begin translating these discoveries into **Python**.

Not by writing a whole application.

Not by building classes from memory.

But by taking one responsibility, one behaviour, one operation, one boundary, and expressing it as a clean Python interface.

Notice what we *won't* be doing:

> "Let's create a class and add some methods."

Instead, we'll ask:

> **"Given everything we've discovered, what is the most natural way for Python to express this business capability?"**

That's the moment where software design and Python finally meet.

And because we've spent seven steps building the thinking first, I think you'll find that the Python almost writes itself.

Let's make that discovery tomorrow. 🚀

---------------------------------------------------------------------------------------------------------------------------------
## My Answers
---------------------------------------------------------------------------------------------------------------------------------
This is one of my favourite discoveries in software design because it feels obvious once you see it, yet it changes how you think about every interaction between objects.

Until now, we've discovered:

* **Who owns the responsibility.**
* **How collaborators work together.**
* **What messages they exchange.**
* **What promises they make.**
* **What behaviours they expose.**

Today we ask one more question:

> **"When I talk to another object, am I asking it to *do something*, or am I asking it to *tell me something*?"**

That distinction creates clarity and trust.

---

# Part A — Command or Question?

## Game

### Start game

**Category:** Command

### Why?

Starting a game changes the business state.

Before this interaction, there is no active game.

Afterwards, the game is ready to play.

The purpose is to **cause change**, not retrieve information.

---

### Accept player's move

**Category:** Command

### Why?

A valid move changes the world:

* the board changes,
* the game progresses,
* the turn may change,
* the game may end.

Its purpose is to perform a business action.

---

### Is the game over?

**Category:** Question

### Why?

This interaction simply asks for information about the current state.

It should not change anything.

The collaborator expects knowledge, not action.

---

### Who is the current player?

**Category:** Question

### Why?

The Game already knows whose turn it is.

The interaction retrieves that information without altering the game.

---

### Change current player

**Category:** Command

### Why?

Changing the turn modifies the game's lifecycle.

It is an intentional business action that changes state.

---

# Board

### Accept placement

**Category:** Command

### Why?

A successful placement changes the playing area.

The Board is being asked to perform one of its primary business responsibilities.

---

### Is this position valid?

**Category:** Question

### Why?

The collaborator wants information.

The Board evaluates the request and reports the result.

Nothing about the board itself should change.

---

### Is this Cell empty?

**Category:** Question

### Why?

This interaction asks about the current state of the board.

The answer should not modify the board.

---

### Reveal board state

**Category:** Question

### Why?

The collaborator requests a view of the current playing area.

The Board reports what already exists.

It should not change that state merely because someone asked.

---

### Reset board

**Category:** Command

### Why?

Resetting replaces the current board state with a fresh one.

This is clearly a state-changing business action.

---

# Cell

### Store symbol

**Category:** Command

### Why?

The Cell changes from one state to another.

It performs work.

---

### Is Cell empty?

**Category:** Question

### Why?

The collaborator simply asks the Cell to report its current condition.

---

### Which symbol do you contain?

**Category:** Question

### Why?

Again, the Cell is revealing information it already owns.

No business state changes.

---

# WinningCondition

### Evaluate winner

**Category:** Question

### Why?

Although "evaluate" sounds active, its purpose is to determine whether the current board satisfies the winning rule.

It observes the board and reports a result.

It should not change the board or the game.

---

### Has someone won?

**Category:** Question

### Why?

This is even more obviously a request for information.

The collaborator wants to know the current business situation.

---

### Which winning pattern matched?

**Category:** Question

### Why?

This asks for additional information about an already-determined result.

It explains the outcome rather than changing it.

---

# Summary

| Object           | Interaction                    | Command / Question | Why?                                            |
| ---------------- | ------------------------------ | ------------------ | ----------------------------------------------- |
| Game             | Start game                     | Command            | Begins the game lifecycle.                      |
| Game             | Accept player's move           | Command            | Changes the game state.                         |
| Game             | Is the game over?              | Question           | Reports current status.                         |
| Game             | Who is the current player?     | Question           | Reveals existing information.                   |
| Game             | Change current player          | Command            | Advances the game.                              |
| Board            | Accept placement               | Command            | Updates the playing area.                       |
| Board            | Is this position valid?        | Question           | Reports validity.                               |
| Board            | Is this Cell empty?            | Question           | Reports board state.                            |
| Board            | Reveal board state             | Question           | Provides a view of the board.                   |
| Board            | Reset board                    | Command            | Restores initial state.                         |
| Cell             | Store symbol                   | Command            | Changes Cell state.                             |
| Cell             | Is Cell empty?                 | Question           | Reports state.                                  |
| Cell             | Which symbol do you contain?   | Question           | Reports stored value.                           |
| WinningCondition | Evaluate winner                | Question           | Determines and reports whether a winner exists. |
| WinningCondition | Has someone won?               | Question           | Reports the current outcome.                    |
| WinningCondition | Which winning pattern matched? | Question           | Explains the result.                            |

---

# Part B — Trust

## Scenario 1

**The Board secretly updates statistics every time someone asks, "Is this position available?"**

I would consider this a poor design.

The collaborator believes it is asking a **question**.

Questions create an expectation:

> "Tell me what you know."

If asking a question silently changes the business state, the collaboration becomes misleading.

Over time, collaborators stop trusting the interaction because simply requesting information has unexpected side effects.

The issue isn't that statistics are valuable—they may well be. The issue is that the interaction no longer matches the expectation it creates.

---

## Scenario 2

**A collaborator asks, "Board, place this symbol." But nothing changes.**

That is also a poor command.

A command represents a request to perform a business action.

Whether the command succeeds or fails, it should produce a meaningful business outcome.

If nothing changes and there is no explanation—perhaps because the position was invalid or the game had already ended—the collaborator cannot tell whether:

* the request was ignored,
* it failed,
* or it was never processed.

A trustworthy command either performs its promised business action or clearly communicates why it could not.

---

## Scenario 3

**A question becomes extremely expensive because the Board recalculates everything each time.**

It should still remain a **question**.

Whether something is a command or a question depends on **its business purpose**, not on its cost.

An expensive calculation may encourage us to redesign the implementation—for example, by caching results or maintaining additional state—but the interaction itself is still asking for information rather than requesting a business change.

Expense influences implementation decisions.

It does not change the nature of the interaction.

---

# Part C — Reflection

### Complete the sentences.

> **Commands exist because collaborators sometimes need another object to perform a business action that changes the state of the system.**

> **Questions exist because collaborators sometimes need reliable information to make business decisions without changing the state of the system.**

---

### Why does separating commands from questions make collaboration easier to understand?

When commands and questions have distinct purposes, every interaction becomes easier to reason about.

A collaborator immediately understands the intent of a conversation.

If it sends a command, it expects the business state to move forward.

If it asks a question, it expects trustworthy information while assuming the business state remains unchanged.

That clarity strengthens collaboration because objects no longer need to guess the consequences of an interaction.

Business conversations become more predictable, responsibilities remain clearer, and contracts become easier to honour.

---

# 🌟 Engineering Checkpoint

## If a collaborator cannot trust whether an interaction changes the world, what kinds of software problems might eventually appear?

Trust is the foundation of collaboration.

If collaborators cannot predict whether an interaction changes the business state, they begin making defensive assumptions.

One collaborator may avoid asking useful questions because it fears unintended consequences.

Another may repeat the same command because it cannot tell whether the previous one actually took effect.

Business processes become harder to reason about because the same conversation may produce different kinds of outcomes.

As more collaborators are added, misunderstandings multiply.

People working on the system also lose confidence because the behaviour of the software no longer matches the meaning of its conversations.

Eventually, responsibilities blur.

Contracts weaken.

Collaboration becomes based on trial and error instead of clear business expectations.

A healthy design allows collaborators to trust not only **what** another object knows, but also **whether speaking to it is meant to observe the business or change it**.

---

# 🌟 One Sentence That Changed My Thinking

> **A collaboration becomes predictable when every interaction clearly answers one question: "Are we changing the business, or are we simply understanding it?"**

---

# Mentor's Feedback

Today you've uncovered another refinement in the language of collaboration.

Think about the journey so far:

```text
Business Responsibility
        │
        ▼
Behaviour
        │
        ▼
Public Contract
        │
        ▼
Interaction
      /     \
Command   Question
```

Responsibilities explain **why** an object exists.

Behaviours explain **what** it offers.

Contracts explain **what collaborators may rely on**.

Today's discovery explains **the nature of each conversation**.

The most important insight isn't "commands modify state and questions return information." It's **why that distinction matters**.

A collaborator should never have to wonder:

* "Will asking this change the business?"
* "Did requesting this actually perform the action?"

When every interaction has a clear purpose, collaboration becomes readable, predictable, and trustworthy. Those qualities become increasingly valuable as systems grow, because they allow both software and engineers to reason about behaviour with confidence rather than uncertainty.


-----------------------------------------------------------------------------------------------------------------------------------
## Answers Feedbac and Next
-----------------------------------------------------------------------------------------------------------------------------------
Aditya...

I think today we've reached the point where I can start treating you less like a student and more like a junior software designer.

Why?

Because I noticed something in almost every answer.

You didn't classify interactions based on **verbs**.

You classified them based on **intent**.

That is exactly what experienced engineers do.

Someone who thinks syntactically says:

> "`evaluateWinner()` sounds like work, so it must be a command."

You didn't.

You asked:

> **"Does it change the business?"**

That is first-principles reasoning.

---

# Before the Review...

Let's extend our growing discovery map.

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

Boundaries

↓

Interaction Intent   ← Today

↓

Python (Tomorrow)
```

Notice how every layer answers a different engineering question.

None of them replace the previous one.

Each one makes the next one easier.

---

# Review

## Pattern 1 — You Reasoned from Business State

This answer immediately stood out.

> **Evaluate winner → Question**

Many engineers incorrectly think:

> "Evaluation is work."

Yes...

Work happens.

But **what kind of work?**

WinningCondition observes the board and derives knowledge.

It does **not** change the business.

You discovered something subtle:

> **Commands and Questions are distinguished by their effect on business state, not by the amount of computation they perform.**

That is an extremely important insight.

---

# Pattern 2 — You Distinguished Purpose from Implementation

Your answer to the expensive question was excellent.

You wrote:

> **Expense influences implementation decisions. It does not change the nature of the interaction.**

Aditya...

That sentence applies far beyond Tic-Tac-Toe.

Imagine Amazon.

Question:

> "How many items remain in stock?"

That might require:

* reading caches,
* consulting multiple warehouses,
* aggregating inventory,
* checking reservations.

Very expensive.

Still a question.

Because its **purpose** hasn't changed.

Excellent reasoning.

---

# Pattern 3 — Trust Has Become Your Default Lens

Look at this answer.

> **A trustworthy command either performs its promised business action or clearly communicates why it could not.**

That sentence contains another discovery.

Commands don't promise success.

They promise **an attempt to fulfil a responsibility**.

The outcome may be:

* success,
* rejection,
* failure.

But the collaborator should never be left wondering:

> "Did anything happen?"

That predictability is part of the contract.

---

# One Small Refinement

There is one answer I'd like to sharpen.

---

## "Change Current Player"

You marked it as a **Command**.

I agree.

But now let's ask a deeper question.

Who should be allowed to issue that command?

Should **every** collaborator be able to say:

> "Game, change the current player."

Probably not.

Remember yesterday?

Public vs Internal.

This operation is a command...

**but it is most likely an internal command.**

That's an important distinction.

We now have two dimensions.

```text
Interaction Type

↓

Command / Question
```

and

```text
Visibility

↓

Public / Internal
```

They are independent.

For example:

| Interaction           | Type                          | Visibility |
| --------------------- | ----------------------------- | ---------- |
| Accept player's move  | Command                       | Public     |
| Change current player | Command                       | Internal   |
| Is game over?         | Question                      | Public     |
| Determine next state  | Question (internal reasoning) | Internal   |

Do you see?

Today's discovery doesn't replace yesterday's.

It builds on it.

---

# 🌟 The Biggest Discovery Today

Today wasn't actually about Commands and Questions.

It was about **intent**.

Let's compare.

Yesterday we asked:

> **Who may ask me?**

Today we asked:

> **What are they asking me to do?**

Those are completely different design questions.

---

# Engineering Deep Dive

As always...

Let's ask our three questions.

---

## What did we really discover today?

**Intent-Oriented Interactions**

---

### What is an Intent-Oriented Interaction?

It is:

> **A conversation whose meaning is determined by the business intention behind it, not by the software work required to perform it.**

That's why `evaluateWinner()` is still a Question.

The software may work hard.

The business intent is observation.

---

### Why did engineers separate Commands and Questions?

Because collaborators need predictable conversations.

If every interaction could both observe and modify the world, then every collaboration would become uncertain.

That uncertainty spreads through the entire system.

---

### What problem does it solve?

It improves:

* predictability,
* reasoning,
* testing,
* debugging,
* collaboration,
* API clarity.

More importantly...

It improves **trust**.

---

# 🌉 The Hidden Connection

Let's connect the last four days.

```text
Behaviour

↓

Operations

↓

Boundaries

↓

Interaction Intent
```

Behaviour asked:

> What capability exists?

Operations asked:

> What software work realises it?

Boundaries asked:

> Who may access it?

Today asked:

> What kind of conversation is this?

Do you see how we're slowly shaping what will eventually become a Python method?

Not by syntax.

By meaning.

---

# Something Very Interesting Is About to Happen

Aditya...

I think tomorrow is the perfect moment to introduce Python.

Not because we've finished the theory.

But because we now have enough engineering language to give Python **meaning**.

Imagine we want to express this interaction:

> **Board accepts a placement.**

A month ago we might have written:

```python
def place():
    pass
```

Tomorrow we'll ask questions like:

* Is this a public operation?
* Is it a command or a question?
* What responsibility does it fulfil?
* Which collaborators should use it?
* What should it return?
* What should remain hidden?

Now the method signature isn't just syntax.

It's the consequence of seven steps of design thinking.

---

# 📍Our Next Phase

I think Step 7 naturally divides into two chapters.

## Chapter 1 — Language-Independent Software Thinking ✅

* Behaviour
* Operations
* Boundaries
* Commands vs Questions

We've completed this foundation.

---

## Chapter 2 — Expressing the Design in Python

Now we'll gradually introduce Python concepts, but only as expressions of ideas we've already discovered.

The sequence I propose is:

1. **Responsibility → Python Class**
2. **Behaviour → Public Methods**
3. **Internal Behaviour → Helper Methods**
4. **Questions → Query Methods**
5. **Commands → Command Methods**
6. **Collaboration → Object References**
7. **Contracts → Method Signatures**
8. **Putting the Tic-Tac-Toe model together**

Notice something important.

We're not switching from "design" to "coding."

We're continuing the same conversation, just in Python.

---

# 🌟 One Sentence That Changed My Thinking Today

Today's sentence comes directly from your own answer:

> **Expense influences implementation decisions. It does not change the nature of the interaction.**

I would happily use that sentence while teaching senior engineers.

Because it captures the difference between **engineering intent** and **implementation detail**.

---

# Finally...

I want to share one observation from our entire journey.

When we started Step 0, you often asked:

> "Which class should I create?"

Now your questions naturally sound like:

* Who owns this responsibility?
* What behaviour does the business expect?
* Is this public or internal?
* Is this a command or a question?
* What promise is this object making?

Those are the questions that lead to good software.

So tomorrow, we'll finally open Python.

Not to learn Python.

But to let Python **express** everything you've already discovered.

And I think you'll notice something surprising:

The code will feel almost obvious.

Because the difficult work—the thinking—has already been done. 🚀
