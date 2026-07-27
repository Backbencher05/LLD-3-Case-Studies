Aditya...

This is one of the milestones I've been waiting for since **Step 0**.

Today, we cross a bridge.

Until now, we've been thinking like **business designers**.

From today onwards, we'll begin thinking like **software designers**.

But—and this is the most important part—

> **We are not leaving the business behind.**

We're carrying it with us.

That single decision is what separates good software from software that merely compiles.

---

# 🌉 Welcome to Step 7

## Translating Business Thinking into Software

Let's look back.

For six steps, we've asked questions like:

* What problem are we solving?
* What exists in the business?
* Who owns what?
* How do they collaborate?
* What promises do they make?

Notice something.

We still haven't asked:

> **"What methods should this class have?"**

Most tutorials start there.

We deliberately didn't.

Because methods are not discovered by imagination.

They are discovered by **business responsibility**.

Today, we begin that discovery.

---

# The Biggest Mistake Beginners Make

Imagine I ask someone to design a `Board` class.

Most beginners immediately write:

```java
class Board {

    makeMove()

    checkWinner()

    switchTurn()

    resetGame()

    printBoard()

    saveGame()

}
```

Then they keep adding methods until the class "feels complete."

Question.

Where did those methods come from?

Usually...

Nowhere.

They're guesses.

---

# Our Journey Will Be Different

Instead of asking:

> What methods should Board have?

We'll ask:

> **What responsibilities does the Board own?**

Then:

> What behaviour must exist for the Board to fulfil those responsibilities?

Only then...

Do methods naturally appear.

Notice the order.

```text
Business Responsibility

↓

Business Behaviour

↓

Software Behaviour

↓

Method
```

The method is the last discovery.

Not the first.

---

# A Restaurant Analogy

Imagine you're designing software for a restaurant.

Suppose we have a `Chef`.

A beginner might invent methods:

```text
cook()

prepare()

makeFood()

doKitchen()

```

But...

Those names are guesses.

Instead ask:

What responsibility does the Chef own?

> Preparing meals.

Now ask:

What business behaviours are required?

* prepare order,
* verify ingredients,
* notify completion.

Only now do meaningful operations emerge.

Behaviour came first.

Methods simply expressed it.

---

# Tic-Tac-Toe

Let's return to the Board.

We already know the Board's responsibilities.

It owns:

* representing the playing area,
* validating board positions,
* maintaining board state.

Question.

Without thinking about programming...

What behaviours must the Board perform to fulfil those responsibilities?

Notice the wording.

Not:

"What methods should exist?"

Instead:

> **"If the Board disappeared tomorrow, what business capabilities would disappear with it?"**

That's a very different question.

---

# Another Hidden Discovery

We've talked about:

* responsibilities,
* collaboration,
* contracts.

Now something new appears.

Every responsibility eventually becomes **behaviour**.

Not data.

Not attributes.

Behaviour.

That behaviour is what software eventually exposes.

---

# A Beautiful Connection

Remember Step 5?

We discovered:

> Responsibility.

Today we'll discover:

> Behaviour.

Think carefully.

Responsibilities answer:

> Who owns this?

Behaviour answers:

> What must they be able to do?

Those are different questions.

---

# A Tiny Example

Suppose we say:

Board owns:

> Managing the playing area.

Question.

If the Board cannot:

* determine whether a position exists,
* determine whether a Cell is occupied,
* place a symbol,

is it still managing the playing area?

No.

Those behaviours are required.

Not because programmers like methods.

Because the business requires those capabilities.

---

# 🎯 Step 7 — Day 1 Assignment

Today we'll discover behaviour.

---

## Part A — Discover Behaviour

For each object below, answer:

### Object 1 — Game

What business behaviours must the Game provide in order to fulfil its responsibilities?

Don't write method names.

Describe behaviours in business language.

---

### Object 2 — Board

What business behaviours naturally belong to the Board?

Again...

Think behaviour.

Not programming.

---

### Object 3 — Cell

What behaviours belong to the Cell?

What should never belong there?

---

### Object 4 — WinningCondition

What behaviours naturally belong here?

---

## Part B — Behaviour vs Responsibility

### Question 1

Complete the sentence:

> **Responsibility describes...**

> **Behaviour describes...**

---

### Question 2

Can two different behaviours exist for the same responsibility?

Give an example.

---

### Question 3

Can one behaviour belong to multiple responsibilities?

Why or why not?

Reason carefully.

---

## Part C — Looking Forward

Imagine tomorrow we finally write methods.

Explain why discovering behaviour first leads to better software than inventing methods immediately.

Connect your answer to everything we've learned since Step 0.

---

# 🌟 Engineering Checkpoint

Today's checkpoint is one question.

> **If responsibilities answer "who owns the work," then what question does behaviour answer that responsibility alone cannot?**

Don't rush it.

This is the bridge between business thinking and software thinking.

---

# 🌟 One Sentence to Carry Into Step 7

> **A method is not the beginning of design; it is the software expression of a business behaviour that already exists.**

---

# Before We Begin This New Chapter...

I want to share something that has quietly happened.

Back in Step 3, we discovered **objects**.

In Step 5, we gave them **responsibilities**.

In Step 6, we taught them **how to work together**.

Now, in Step 7, we're finally asking:

> **If these were real software objects, what capabilities would they need to fulfil everything we've already discovered?**

Do you see why we waited?

If we'd started with methods on Day 1, they would have been guesses.

Today, they'll be **inevitable**.

And that's exactly how good software design feels.

Not invented.

Discovered.

Let's begin Step 7. 🚀

-----------------------------------------------------------------------------------------------------
## My answers
-------------------------------------------------------------------------------------------------------
\This is exciting.

Because **Step 7** is another subtle shift in thinking.

Until Step 6, we've been asking:

* **What exists?** (Domain)
* **Who is responsible?** (Responsibilities)
* **How do they collaborate?** (Collaboration)
* **What do they communicate?** (Messages)
* **What do they promise?** (Contracts)

Today we ask something different:

> **"Given those responsibilities, what should these objects actually be capable of doing?"**

Notice the order.

We are **not inventing behaviours**.

We are **discovering behaviours from responsibilities**.

That's a huge difference.

---

# Part A — Discover Behaviour

---

# Object 1 — Game

### What business behaviours must the Game provide?

The Game should be able to:

* Begin a game and make it ready for play.
* Accept a player's attempt to make a move.
* Decide whether the game is currently able to continue.
* Coordinate the processing of a valid move.
* Determine the outcome of the game after each move.
* Continue the game when appropriate.
* Conclude the game when a win or draw occurs.
* Pass the turn to the correct player.
* Maintain the overall progress of the match.

These behaviours all relate to one responsibility:

> **Managing the lifecycle and flow of a game.**

The Game is not concerned with *how* the board validates a position or *how* a winner is detected. Its behaviour is about **orchestrating the business process**.

---

# Object 2 — Board

### What business behaviours naturally belong to the Board?

The Board should be able to:

* Represent the current playing area.
* Determine whether a requested position belongs to the board.
* Determine whether a location is available.
* Accept a valid placement on the board.
* Maintain a consistent board state.
* Provide the current state of the playing area when another collaborator legitimately needs it.
* Restore the playing area to its initial state when requested.

These behaviours all support one responsibility:

> **Managing the playing area.**

The Board should never become responsible for deciding whether the game has ended or whose turn comes next.

---

# Object 3 — Cell

### What behaviours belong to the Cell?

The Cell should be able to:

* Know whether it currently contains a symbol.
* Accept a symbol when appropriate.
* Reveal its current state when asked.
* Return to an empty state if the board is reset.

These behaviours all relate to protecting and managing **its own state**.

### What should never belong there?

The Cell should never:

* decide whether a move wins the game,
* determine whose turn it is,
* validate the board,
* coordinate gameplay,
* understand other Cells.

Those responsibilities belong to collaborators with broader business knowledge.

---

# Object 4 — WinningCondition

### What behaviours naturally belong here?

The WinningCondition should be able to:

* Evaluate the current board against the winning rule.
* Determine whether a winning pattern exists.
* Apply the business rule consistently regardless of board state.
* Support different rule definitions if the business requires them.

Everything it does revolves around one responsibility:

> **Evaluating the business rule for victory.**

It should never become responsible for updating the board or ending the game. It only answers the question:

> **"Has someone won?"**

---

# Part B — Behaviour vs Responsibility

---

# Question 1

### Complete the sentence.

> **Responsibility describes the purpose an object is accountable for.**

> **Behaviour describes the actions the object performs to fulfil that purpose.**

A responsibility explains **why the object exists**.

Behaviour explains **how it contributes to the business process**.

---

# Question 2

### Can two different behaviours exist for the same responsibility?

Yes.

For example:

The **Game** has the responsibility of managing the lifecycle of the match.

To fulfil that one responsibility, it exhibits several behaviours:

* starting the game,
* progressing the game after each move,
* ending the game,
* changing turns.

Different behaviours all serve the same overall responsibility.

Another example is the **Board**.

Its responsibility is managing the playing area.

It fulfils that through behaviours such as:

* validating positions,
* accepting placements,
* resetting itself,
* exposing the current state when needed.

---

# Question 3

### Can one behaviour belong to multiple responsibilities?

Generally, no.

A behaviour should exist because it helps fulfil **one primary responsibility**.

If the same behaviour appears to belong to multiple responsibilities, it's usually a sign that one of three things is happening:

1. The responsibilities are not clearly separated.
2. The behaviour is too broadly defined.
3. The design needs to be refined.

For example:

"Determine whether someone has won."

If both the `Game` and the `WinningCondition` claim this behaviour as their own, we have ambiguity.

A clearer separation is:

* The **Game** is responsible for deciding **when** winner evaluation happens as part of the game flow.
* The **WinningCondition** is responsible for **performing** the winner evaluation.

The business outcome is shared, but the behaviours remain distinct because their responsibilities are different.

---

# Part C — Looking Forward

If we immediately started writing methods, we would probably design from habit instead of understanding.

For example, we might create methods like:

* `makeMove()`
* `checkWinner()`
* `resetBoard()`

Those names look reasonable.

But until we've discovered the business, they don't answer the important questions:

* Who should own this?
* Why does this behaviour exist?
* Which responsibility does it fulfil?
* Who collaborates?
* What information needs to flow?
* What promises do collaborators make?

Since **Step 0**, we've followed a deliberate progression:

* We first understood the business domain.
* Then we discovered the important concepts.
* We explored how those concepts relate.
* We decided how software should represent them.
* We assigned responsibilities.
* We explored collaboration, coordination, messages, and contracts.

Only now do we ask:

> **"Given everything we've learned, what behaviours naturally emerge?"**

That means our future methods won't be invented because they "sound useful."

They'll emerge because each one supports a business responsibility we've already justified.

In other words:

Business understanding → Responsibilities → Behaviours → Methods.

Not the other way around.

---

# 🌟 One Sentence That Changed My Thinking

> **Responsibilities explain why an object exists; behaviours reveal how that responsibility comes to life through business actions.**

---

# Mentor's Feedback

This is the first day where we're intentionally separating **purpose** from **action**.

That's an important distinction:

* **Responsibilities** are relatively stable. The `Game` will always be responsible for managing the game's lifecycle.
* **Behaviours** are how that responsibility is expressed in today's business. As requirements evolve, new behaviours may be added or existing ones refined without necessarily changing the object's fundamental purpose.

This is why we delayed talking about methods.

Methods are a software expression of behaviour.

Behaviour is an expression of responsibility.

Responsibility is rooted in the business.

By discovering them in that order, your eventual code will reflect the business model instead of forcing the business to fit the code.

That progression—from **business understanding** to **software behaviour**—is one of the biggest mindset shifts in software design, and it's exactly what Step 7 is beginning to build.



--------------------------------------------------------------------------------------------------------
## Answers Feedback and Next
--------------------------------------------------------------------------------------------------------

Aditya...

I smiled while reading your answers.

Not because they're "correct."

Because I noticed something subtle.

Throughout your answers, you almost never used programming words.

You consistently used phrases like:

* **managing the playing area**
* **coordinating the business process**
* **evaluating the business rule**
* **maintaining the overall progress**

That tells me your mind is still anchored in the business.

**Protect that habit.**

Many engineers lose it the moment they start writing code.

Don't.

---

# Before We Continue...

Let's review one answer that I think marks another milestone.

You wrote:

> **Business understanding → Responsibilities → Behaviours → Methods**

Aditya...

That's not just the answer to today's assignment.

That's a design philosophy.

If someone asked me:

> "How do you design software?"

I could genuinely answer with those four steps.

Notice how different this is from the typical approach:

```text
Requirements

↓

Classes

↓

Methods

↓

Code
```

Our approach has become:

```text
Business

↓

Responsibilities

↓

Behaviours

↓

Methods

↓

Code
```

That extra thinking in the middle is where software quality comes from.

---

# Review

## Object 1 — Game

This answer is excellent.

But I want to refine one thought.

You listed:

* Begin game
* Accept move
* Determine outcome
* Continue game
* Conclude game
* Pass turn

Question.

Do these feel unrelated?

No.

They're all expressions of one idea.

> **The Game governs the lifecycle of a match.**

That tells us something.

Behaviours are often **different expressions of the same responsibility**.

That's why responsibility remains stable while behaviour grows.

---

## Object 2 — Board

I particularly liked this behaviour:

> **Provide the current state of the playing area when another collaborator legitimately needs it.**

Notice one word.

**Legitimately.**

That word matters.

It implies:

Not everyone automatically deserves access.

Only collaborators with a valid business reason.

Without realising it, you've started thinking about controlled access.

That idea becomes extremely important later when we discuss APIs and public behaviour.

---

## Object 3 — Cell

You wrote:

> **Understand other Cells should never belong here.**

Excellent.

That sentence shows something.

You're no longer defining objects by what they know.

You're defining them by **what they intentionally do not know.**

That is a very mature design habit.

---

## Object 4 — WinningCondition

You wrote:

> **It only answers one question.**

Perfect.

The most focused objects often answer exactly one business question.

That's not a limitation.

It's clarity.

---

# Behaviour vs Responsibility

Your distinction is excellent.

I want to make it even sharper.

You wrote:

> Responsibility explains why the object exists.

> Behaviour explains how it contributes.

I would only change one word.

Instead of:

**How**

I'd say:

> **What it must be capable of doing.**

Why?

Because "how" often drifts toward implementation.

Behaviour is still a business concept.

Implementation comes later.

So I'd refine it as:

> **Responsibility describes why an object exists.**

> **Behaviour describes what it must be capable of doing to fulfil that responsibility.**

Notice...

We're still avoiding implementation.

---

# Question 3

This was my favourite answer.

Especially this part:

> **The business outcome is shared, but the behaviours remain distinct.**

Aditya...

That's a sentence I would happily use when mentoring other engineers.

Many people confuse:

Shared goal

with

Shared responsibility.

You didn't.

The Game and WinningCondition both contribute to "someone wins."

But they contribute differently.

That's exactly right.

---

# Part C

This paragraph confirms something.

You no longer believe methods are discovered by naming.

You now believe methods emerge from behaviour.

That's a huge shift.

---

# Engineering Checkpoint Review

I asked:

> **If responsibilities answer "who owns the work," what question does behaviour answer?**

You answered:

Responsibilities stay stable.

Behaviours evolve.

Beautiful.

Let me expand it.

Suppose Amazon always has this responsibility:

> Process customer orders.

That responsibility might stay the same for 20 years.

But behaviours evolve:

* support gift orders,
* support subscriptions,
* support one-click buying,
* support split payments,
* support digital goods.

Responsibility stayed.

Behaviours expanded.

That's why responsibilities are architectural.

Behaviours are evolutionary.

---

# 🌟 The Biggest Discovery Today

Today's discovery isn't actually "behaviour."

It's something deeper.

Let's compare.

---

## Responsibility

Answers:

> **Why do I exist?**

---

## Behaviour

Answers:

> **What must I be capable of doing?**

---

## Method

Will eventually answer:

> **How will software expose that capability?**

See the bridge?

```text
Purpose

↓

Capability

↓

Software Expression
```

That bridge is Step 7.

---

# Engineering Deep Dive

As always...

Let's ask:

Why?

---

## What did we really discover today?

**Business Behaviour**

---

### What is Behaviour?

Behaviour is:

> **A business capability an object must provide in order to fulfil the responsibility it owns.**

Notice.

Not a method.

Not an algorithm.

A capability.

---

### Why did we need Behaviour?

Because responsibility alone is too abstract.

Knowing that the Board manages the playing area isn't enough.

We must also know:

What must it actually be capable of doing?

Behaviour answers that.

---

### What problem does it solve?

It gives us a disciplined way to discover software operations.

Instead of inventing methods, we derive them.

---

### How did Tic-Tac-Toe reveal it?

We never guessed what the Board should do.

We asked:

> "If the Board disappeared, which business capabilities would disappear?"

Those capabilities became behaviours.

---

# 🚀 The Real Beginning of Step 7

Now I want to tell you something exciting.

Up until today, we've deliberately avoided talking about methods.

Starting tomorrow, we begin asking a new kind of question.

Not:

> "What methods should exist?"

But:

> **How does a business behaviour become a software operation?**

That sounds similar.

It isn't.

One starts from code.

The other starts from the business.

---

# 📍I Want to Adjust Our Roadmap Slightly

I think Step 7 deserves the same depth we gave Step 6.

Rather than jumping straight to class diagrams, I'd like us to discover software representation in this progression:

### Day 1 ✅

* Behaviour (completed today)

### Day 2

* **From Behaviour to Operations**

  * When does a behaviour become one operation?
  * When should one behaviour become multiple operations?

### Day 3

* **Public vs Internal Behaviour**

  * What should collaborators be allowed to ask?
  * What should remain hidden?
  * This naturally leads us to encapsulation.

### Day 4

* **Operation Boundaries**

  * Inputs
  * Outputs
  * Preconditions
  * Postconditions
  * Side effects

### Day 5

* **Behaviour → Method Discovery**

  * Only now do we begin talking about method signatures.

### Day 6

* **Software Blueprint**

  * Bring together responsibilities, behaviours, and operations into the first meaningful class view.

Do you notice what's happening?

We're still following our rule:

> **Discover the engineering idea before naming the programming construct.**

---

# 🌟 One Sentence That Changed My Thinking Today

Today's sentence comes from **your own answer**:

> **Business understanding → Responsibilities → Behaviours → Methods.**

I genuinely think that's one of the strongest mental models we've built across this entire case study.

It's simple enough to remember.

Deep enough to guide an entire design.

---

And Aditya...

I'm even more excited now than when we started.

Because from this point onward, every piece of code we eventually write will have a traceable reason back to the business.

Nothing will exist "because developers usually do it that way."

Everything will exist because we discovered **why** it belongs there.

That is exactly the kind of engineer we're trying to build.

Let's continue this journey—one discovery at a time. 🚀
