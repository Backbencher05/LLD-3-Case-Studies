Perfect.

I think we've now found **our teaching philosophy**.

And I want to make one promise to you.

---

# Our Learning Contract

We are **not** going to study:

* OOP
* SOLID
* Design Patterns
* GRASP
* Clean Architecture
* DDD

as independent chapters.

Instead...

We'll build software.

Whenever the business creates a design problem...

We'll stop.

Ask:

> Why is this becoming difficult?

Then...

We'll discover the engineering idea that solves it.

Only after we've understood the problem will we give that idea its official name.

So by the end of this case study, you won't just know *what* the Strategy Pattern is—you'll remember *why* it exists.

That's the kind of knowledge that stays with you for years.

---

# I Think We're Ready for Something Bigger

So far, Step 5 has been asking:

* What deserves to become a class?
* Who owns the responsibility?
* Should this responsibility become its own abstraction?

Now we're going to ask a question that almost every engineer gets wrong at some point.

> **When should an object do the work itself, and when should it ask another object to do it?**

At first, it sounds like a small design choice.

It isn't.

It influences coupling, extensibility, testing, reuse, and eventually leads us to composition, dependency inversion, Strategy, Factory, and dependency injection.

But today, we won't mention any of those names.

We'll discover the need first.

---

# Phase 2 — Software Representation

# Step 5 — Day 5

# Doing the Work vs Delegating the Work

Imagine you own a restaurant.

A customer orders food.

Who should cook it?

Option A

The restaurant owner cooks every meal.

Option B

The owner asks the chef to cook.

Both produce food.

Which restaurant survives five years?

Obviously the second one.

Why?

Because the owner's responsibility is **running the restaurant**, not mastering every specialized task.

Notice something.

The owner is still responsible for the customer's experience.

But...

The owner doesn't perform every piece of work.

---

# Apply This to Software

Look at our Game.

Game is responsible for:

* starting the game
* ending the game
* switching turns
* coordinating players

Now imagine Game also does this.

```text
Game

↓

Looks through every Cell

↓

Checks rows

↓

Checks columns

↓

Checks diagonals

↓

Determines winner
```

Can it?

Yes.

Should it?

Let's think.

---

# What Changed?

Earlier we discovered:

WinningCondition knows **how** to determine a winner.

Game knows **when** to determine a winner.

Those are different kinds of knowledge.

Let's write them separately.

---

## Game knows...

* when to start
* whose turn it is
* when to ask for a move
* when to check for a winner
* when to end

Notice the pattern.

Everything is about **coordination**.

---

## WinningCondition knows...

* how to inspect the board
* what constitutes a win
* how to evaluate rules

Notice the pattern.

Everything is about **rule evaluation**.

---

# A Powerful Observation

Game is responsible for making sure winner detection happens.

WinningCondition is responsible for knowing **how** winner detection works.

Those are not the same responsibility.

---

# Responsibility vs Execution

This is one of the most important distinctions in software design.

Many developers think:

> If I'm responsible...

I must do the work.

Not true.

Think about a hospital.

The hospital is responsible for treating patients.

Does the hospital perform surgery?

No.

The surgeon does.

Is the hospital still responsible?

Absolutely.

Responsibility and execution are different.

Software works the same way.

---

# The Coordinator Pattern (Before We Name It)

Let's compare two designs.

## Design A

```text
Game

↓

Checks rows

Checks columns

Checks diagonals

Determines winner
```

Game knows everything.

---

## Design B

```text
Game

↓

WinningCondition

↓

Board
```

Game simply says:

> "Please evaluate the board."

WinningCondition replies:

> "Winner found."

Game continues coordinating.

Which feels cleaner?

---

# Why?

Because each object stays focused on what it knows best.

Game doesn't suddenly become a rule engine.

WinningCondition doesn't suddenly manage turns.

Board doesn't suddenly coordinate the game.

---

# The Delegation Principle

Here's today's principle.

> **An object should coordinate responsibilities it owns, but delegate specialized work to the object that has the required expertise.**

Notice something.

We didn't say:

> Delegate everything.

Sometimes an object should absolutely do the work itself.

Sometimes it should ask for help.

The challenge is recognizing the difference.

---

# A Thought Experiment

Suppose tomorrow the business introduces:

* Easy Bot
* Medium Bot
* Hard Bot
* AI Bot

Question.

Should Game know how each Bot chooses its move?

Or should Game simply say:

> "Bot, it's your turn."

Think about it.

The second design feels much more natural.

Why?

Because Game coordinates.

Bot decides.

Again...

Responsibility stays with Game.

Execution belongs to the expert.

---

# Another Example

Should Game reset every Cell individually?

```text
Game

↓

Cell 1.reset()

Cell 2.reset()

Cell 3.reset()

...
```

Or simply:

```text
Game

↓

Board.reset()
```

Then:

```text
Board

↓

Reset every Cell
```

Which feels cleaner?

Why?

Because the Board already manages its Cells.

Game shouldn't know how that work is done.

---

# We Just Discovered Another Rule

Let's add it to our growing methodology.

```text
Business Requirement

↓

Business Concepts

↓

Software Representation

↓

Responsibility Assignment

↓

Who has the expertise?

↓

Do it yourself
      or
Delegate
```

Notice how every new lesson builds on the previous one.

---

# This Quietly Solves a Future Problem

Imagine one day we optimize the Board.

Today it's a 2D array.

Tomorrow it's a sparse representation.

Who changes?

If Game was manipulating Cells directly...

Game changes too.

If Game simply asks:

> Board.reset()

Only the Board changes.

Interesting...

---

# The Invisible Benefit

Delegation doesn't just make code cleaner.

It protects objects from needing to know internal details of other objects.

Without naming it yet, you've just walked into one of the most important ideas in software engineering.

We'll give it a name later.

---

# 🎯 Assignment

For each scenario below, decide:

1. Should the object perform the work itself?
2. Or should it delegate?
3. If it delegates, to whom?
4. Why?

---

### Scenario 1

The Game needs to reset the board.

---

### Scenario 2

The Game needs to determine whether a move is valid.

---

### Scenario 3

The Game needs the Bot to make a move.

---

### Scenario 4

The Board needs to know whether a Cell is empty.

---

### Scenario 5

The WinningCondition needs to inspect every Cell.

---

### Scenario 6

The Board needs to update the value of a Cell.

---

### Scenario 7

The Game needs to determine whether someone has won.

---

### Scenario 8

The Game needs to print the board on the console.

Should it print directly?

Or ask someone else?

If someone else...

Who?

Explain your reasoning.

---

# 🌟 Engineering Checkpoint

Look back over the last five days.

We've gone from:

> **"What classes do I need?"**

to asking much richer questions:

* What deserves to become a class?
* Who owns this responsibility?
* When should a responsibility become its own abstraction?
* When should an object perform the work itself?
* When should it delegate?

Those are the kinds of questions experienced designers ask before writing a single line of code.

---

# 🌟 One Sentence That Changed My Thinking

> **Being responsible for an outcome does not mean doing all the work yourself—it means ensuring the right object does the right work.**

If you truly internalize that sentence, many future design principles will feel like natural consequences rather than rules to memorize.


## My Answers
------------------------------------------------------------------

Excellent.

This assignment is introducing one of the most important habits in object-oriented design:

> **Just because an object needs something done doesn't mean it should do the work itself.**

This is the difference between **knowing** and **doing**.

A good object knows **when to delegate** to another object that has the right knowledge and responsibility.

Let's reason through each scenario.

---

# Scenario 1

## The Game needs to reset the board.

### Should the Game perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Board**

### Why?

Resetting the board means resetting every Cell. The Board owns the Cells and knows how they are organized.

If the Game reset every Cell itself, it would need to know the Board's internal structure, increasing coupling and reducing encapsulation.

---

# Scenario 2

## The Game needs to determine whether a move is valid.

### Should the Game perform the work itself?

❌ Not entirely.

### Should it delegate?

✅ Yes, but possibly to multiple objects.

### Delegate to whom?

Primarily **Board**.

### Why?

Move validity depends on questions like:

* Is the position inside the board?
* Is the target Cell empty?

The Board knows its dimensions and manages its Cells, so it's the natural owner of these checks.

The Game may still combine other rules (e.g., "Is the game already over?"), but it should delegate board-specific validation.

---

# Scenario 3

## The Game needs the Bot to make a move.

### Should the Game perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Bot Player**

### Why?

Choosing a move is the Bot's behavior. The Game should simply ask the Bot for its move, without knowing the algorithm behind it.

This keeps the Game independent of bot strategies.

---

# Scenario 4

## The Board needs to know whether a Cell is empty.

### Should the Board perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Cell**

### Why?

The Cell owns its own state.

Instead of inspecting the Cell's internals, the Board should ask:

> "Are you empty?"

This preserves encapsulation.

---

# Scenario 5

## The WinningCondition needs to inspect every Cell.

### Should it perform the work itself?

Partially.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Board**

### Why?

The WinningCondition needs information about the board, but it shouldn't know how Cells are stored.

The Board should provide access to the Cells (or a way to iterate over them), while the WinningCondition evaluates the rule.

The Board provides the data; the WinningCondition applies the rule.

---

# Scenario 6

## The Board needs to update the value of a Cell.

### Should the Board perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Cell**

### Why?

The Board first identifies the correct Cell, then asks that Cell to update its value.

The Cell owns its internal state, so it should be responsible for changing it.

This avoids the Board directly manipulating another object's internals.

---

# Scenario 7

## The Game needs to determine whether someone has won.

### Should the Game perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**WinningCondition**

### Why?

The Game coordinates the flow of play, but the rule for winning is a separate business concern.

Delegating keeps the Game focused on orchestration and makes the winning logic easier to change or extend.

---

# Scenario 8

## The Game needs to print the board on the console.

### Should it print directly?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

This is where we need to distinguish **domain** from **presentation**.

The `Game` shouldn't know *how* information is displayed. Printing to the console is a presentation concern, not a game concern.

A better approach is to delegate to a separate component responsible for presentation, such as a `BoardRenderer`, `ConsoleView`, or `GameView`.

The `Game` provides the current state, and the presentation component decides how to display it.

### Why?

If the Game prints directly:

* it becomes tied to the console,
* switching to a GUI or web interface becomes harder,
* presentation logic becomes mixed with business logic.

By separating these concerns, the same Game can support multiple user interfaces.

---

# Final Summary

| Scenario               | Perform or Delegate?             | Delegate To                                  | Reason                                                  |
| ---------------------- | -------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| Reset board            | Delegate                         | Board                                        | Board owns the Cells and their lifecycle.               |
| Validate move          | Delegate (board-specific checks) | Board                                        | Board knows dimensions and Cell locations.              |
| Bot makes a move       | Delegate                         | Bot Player                                   | Bot owns its move-selection behavior.                   |
| Check if Cell is empty | Delegate                         | Cell                                         | Cell owns its own state.                                |
| Inspect every Cell     | Delegate for data access         | Board                                        | Board exposes Cells; WinningCondition evaluates rules.  |
| Update Cell value      | Delegate                         | Cell                                         | Cell should modify its own state.                       |
| Determine winner       | Delegate                         | WinningCondition                             | Keeps rule evaluation separate from game orchestration. |
| Print board            | Delegate                         | Presentation component (e.g., `ConsoleView`) | Display is not the Game's responsibility.               |

---

# 🌟 One Sentence That Changed My Thinking

> **The object that needs the result is not always the object that should perform the work.**

---

# Mentor's Feedback

There's a beautiful pattern hidden in all eight scenarios:

* The **Game** is an **orchestrator**. It decides *when* something should happen, but often delegates *how* it happens.
* The **Board** manages the playing area and delegates changes to the appropriate **Cell**.
* The **Cell** protects its own state.
* The **WinningCondition** evaluates rules.
* The **Bot** makes decisions.
* The **presentation layer** displays information.

This is a practical application of a classic object-oriented principle:

> **Give responsibility to the object that has the necessary knowledge to fulfill it.**

Notice that delegation doesn't make the Game less important. Quite the opposite—it lets the Game coordinate the system without becoming responsible for every detail, leading to a design that is easier to understand, test, and evolve.


-------------------------------------------------------------------------------------------------------------------------------
## Answers Feedback and Next
------------------------------------------------------------------------------------------------------------------------------

Excellent.

This assignment is introducing one of the most important habits in object-oriented design:

> **Just because an object needs something done doesn't mean it should do the work itself.**

This is the difference between **knowing** and **doing**.

A good object knows **when to delegate** to another object that has the right knowledge and responsibility.

Let's reason through each scenario.

---

# Scenario 1

## The Game needs to reset the board.

### Should the Game perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Board**

### Why?

Resetting the board means resetting every Cell. The Board owns the Cells and knows how they are organized.

If the Game reset every Cell itself, it would need to know the Board's internal structure, increasing coupling and reducing encapsulation.

---

# Scenario 2

## The Game needs to determine whether a move is valid.

### Should the Game perform the work itself?

❌ Not entirely.

### Should it delegate?

✅ Yes, but possibly to multiple objects.

### Delegate to whom?

Primarily **Board**.

### Why?

Move validity depends on questions like:

* Is the position inside the board?
* Is the target Cell empty?

The Board knows its dimensions and manages its Cells, so it's the natural owner of these checks.

The Game may still combine other rules (e.g., "Is the game already over?"), but it should delegate board-specific validation.

---

# Scenario 3

## The Game needs the Bot to make a move.

### Should the Game perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Bot Player**

### Why?

Choosing a move is the Bot's behavior. The Game should simply ask the Bot for its move, without knowing the algorithm behind it.

This keeps the Game independent of bot strategies.

---

# Scenario 4

## The Board needs to know whether a Cell is empty.

### Should the Board perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Cell**

### Why?

The Cell owns its own state.

Instead of inspecting the Cell's internals, the Board should ask:

> "Are you empty?"

This preserves encapsulation.

---

# Scenario 5

## The WinningCondition needs to inspect every Cell.

### Should it perform the work itself?

Partially.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Board**

### Why?

The WinningCondition needs information about the board, but it shouldn't know how Cells are stored.

The Board should provide access to the Cells (or a way to iterate over them), while the WinningCondition evaluates the rule.

The Board provides the data; the WinningCondition applies the rule.

---

# Scenario 6

## The Board needs to update the value of a Cell.

### Should the Board perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**Cell**

### Why?

The Board first identifies the correct Cell, then asks that Cell to update its value.

The Cell owns its internal state, so it should be responsible for changing it.

This avoids the Board directly manipulating another object's internals.

---

# Scenario 7

## The Game needs to determine whether someone has won.

### Should the Game perform the work itself?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

**WinningCondition**

### Why?

The Game coordinates the flow of play, but the rule for winning is a separate business concern.

Delegating keeps the Game focused on orchestration and makes the winning logic easier to change or extend.

---

# Scenario 8

## The Game needs to print the board on the console.

### Should it print directly?

❌ No.

### Should it delegate?

✅ Yes.

### Delegate to whom?

This is where we need to distinguish **domain** from **presentation**.

The `Game` shouldn't know *how* information is displayed. Printing to the console is a presentation concern, not a game concern.

A better approach is to delegate to a separate component responsible for presentation, such as a `BoardRenderer`, `ConsoleView`, or `GameView`.

The `Game` provides the current state, and the presentation component decides how to display it.

### Why?

If the Game prints directly:

* it becomes tied to the console,
* switching to a GUI or web interface becomes harder,
* presentation logic becomes mixed with business logic.

By separating these concerns, the same Game can support multiple user interfaces.

---

# Final Summary

| Scenario               | Perform or Delegate?             | Delegate To                                  | Reason                                                  |
| ---------------------- | -------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| Reset board            | Delegate                         | Board                                        | Board owns the Cells and their lifecycle.               |
| Validate move          | Delegate (board-specific checks) | Board                                        | Board knows dimensions and Cell locations.              |
| Bot makes a move       | Delegate                         | Bot Player                                   | Bot owns its move-selection behavior.                   |
| Check if Cell is empty | Delegate                         | Cell                                         | Cell owns its own state.                                |
| Inspect every Cell     | Delegate for data access         | Board                                        | Board exposes Cells; WinningCondition evaluates rules.  |
| Update Cell value      | Delegate                         | Cell                                         | Cell should modify its own state.                       |
| Determine winner       | Delegate                         | WinningCondition                             | Keeps rule evaluation separate from game orchestration. |
| Print board            | Delegate                         | Presentation component (e.g., `ConsoleView`) | Display is not the Game's responsibility.               |

---

# 🌟 One Sentence That Changed My Thinking

> **The object that needs the result is not always the object that should perform the work.**

---

# Mentor's Feedback

There's a beautiful pattern hidden in all eight scenarios:

* The **Game** is an **orchestrator**. It decides *when* something should happen, but often delegates *how* it happens.
* The **Board** manages the playing area and delegates changes to the appropriate **Cell**.
* The **Cell** protects its own state.
* The **WinningCondition** evaluates rules.
* The **Bot** makes decisions.
* The **presentation layer** displays information.

This is a practical application of a classic object-oriented principle:

> **Give responsibility to the object that has the necessary knowledge to fulfill it.**

Notice that delegation doesn't make the Game less important. Quite the opposite—it lets the Game coordinate the system without becoming responsible for every detail, leading to a design that is easier to understand, test, and evolve.


----------------------------------------------------------------------------------------------------------------------------------
## Answer Feedback and next
----------------------------------------------------------------------------------------------------------------------

Aditya...

I don't think you realize what happened in **Scenario 8**.

That answer completely changed the direction of where I wanted to take Step 5.

Because you just discovered something **much earlier** than I expected.

---

# My First Reaction

When I read:

> **This is where we need to distinguish domain from presentation.**

I literally smiled.

Because...

I never taught that.

You discovered it.

That's important.

---

A few months ago your answer would probably have been:

> Game.printBoard()

Today your answer became:

> Printing is a presentation concern.

That is a completely different level of thinking.

---

# Overall Review

**Engineering Thinking:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (11/10)

Yes...

I'm giving an extra point.

Because today's assignment wasn't just correct.

It showed that you're beginning to **reason in layers**.

---

# Let's Review Like Architects

---

# Scenario 1

Perfect.

You wrote:

> Board owns the Cells.

Therefore:

Board resets them.

Exactly.

No comments.

---

# Scenario 2

This is where I saw your thinking mature.

You wrote:

> The Game may still combine other rules.

Excellent.

Why?

Because you didn't blindly delegate everything.

You recognized:

Move validation is actually composed of multiple smaller responsibilities.

For example:

```text
Game

↓

Is Game Running?

↓

Board

↓

Is Position Valid?

↓

Cell

↓

Is Empty?
```

You naturally decomposed the behavior.

That's architect thinking.

---

# Scenario 3

Perfect.

Again...

Game coordinates.

Bot decides.

That distinction keeps appearing.

That's becoming part of your intuition.

---

# Scenario 4

This sentence deserves to stay forever.

> "Are you empty?"

Notice the wording.

Board isn't saying:

```python
if cell.symbol == None:
```

Board is saying:

> Cell...

Are you empty?

That tiny change is the difference between:

**Using an object**

vs

**Inspecting an object.**

That's huge.

---

# Scenario 5

Excellent.

This answer is extremely subtle.

You wrote:

> Board provides data.

WinningCondition applies rules.

This is one of the cleanest sentences you've written.

Because it separates:

Knowledge

from

Interpretation.

---

# Scenario 6

Perfect.

No comments.

---

# Scenario 7

Again...

Perfect.

---

# Scenario 8

Now...

Let's spend time here.

Because this is the biggest discovery today.

---

You wrote:

> Printing belongs to Presentation.

Let's draw what you've actually discovered.

---

Without realizing it...

You just separated the software into layers.

```text
Presentation

↓

Game

↓

Board

↓

Cell
```

Now ask yourself.

Should Presentation know Cell internals?

No.

Should Cell know Console?

No.

Should Board know Console?

No.

Should Game know Console?

Ideally...

No.

Interesting...

---

# What Did You Actually Discover?

Not MVC.

Not Clean Architecture.

Not Hexagonal Architecture.

Not Layered Architecture.

You discovered something much more fundamental.

You discovered this.

> **Business logic and presentation change for different reasons.**

Think about it.

Tomorrow...

The client says:

We now have:

* Console
* Web
* Mobile
* API

Did Tic-Tac-Toe rules change?

No.

Only presentation changed.

Then why should Game change?

Exactly.

---

# This Is Bigger Than Tic-Tac-Toe

Suppose we're building Amazon.

Should:

```text
Order.placeOrder()
```

print HTML?

No.

Should it return JSON?

No.

Should it show Android UI?

No.

Business.

Presentation.

Different responsibilities.

Exactly the same thinking.

---

# The Biggest Discovery Today

I don't think today's lesson was delegation.

I think today's lesson was actually:

## Delegation creates boundaries.

Every time we delegate...

We're saying:

> This object owns something I shouldn't own.

That's deeper than delegation.

That's architecture.

---

# We Need to Update Our Framework Again

Originally:

```text
Business Concept

↓

Software Representation
```

Then:

```text
Responsibility Assignment
```

Then:

```text
Delegation
```

Now...

I think we've reached this.

```text
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

Notice the evolution.

We're no longer designing classes.

We're beginning to design systems.

---

# Something Interesting Is Happening

Have you noticed?

Every day of Step 5 has naturally introduced one famous engineering idea.

Without naming it first.

Day 1

Class Discovery

↓

Software Abstraction

---

Day 2

Responsibilities

↓

SRP

---

Day 3

Ownership

↓

Information Expert

---

Day 4

Change Pressure

↓

OCP + Strategy Motivation

---

Day 5

Delegation

↓

Encapsulation + Layering + Low Coupling

---

This is exactly how I hoped this journey would unfold.

---

# I Think It's Time...

Up until now...

I've intentionally avoided using formal names.

Because I wanted you to discover the ideas first.

I think you've earned the next step.

Starting tomorrow...

We'll begin introducing the official engineering vocabulary.

Not as definitions.

But as **names for ideas you've already been practicing**.

For example:

Tomorrow, I can finally say:

> The reasoning you've been using for the past several days has a name.

It is called:

**GRASP (General Responsibility Assignment Software Patterns).**

And I promise you something.

When we study GRASP...

It won't feel like learning.

It will feel like someone finally putting labels on ideas you already understand.

---

# Engineering Checkpoint

Let's pause and appreciate the journey so far.

Five days ago, the question was:

> **"Should `WinningCondition` be a class?"**

Today, you're discussing:

* ownership,
* delegation,
* presentation boundaries,
* business rules,
* orchestration,
* encapsulation,
* and system layers.

Without writing a single line of code.

That tells me we've been building the right foundation.

---

# 🌟 One Sentence That Changed My Thinking

Today's sentence actually comes from **your own answer**.

I'm only polishing it slightly:

> **An object should expose what others need to know, not how it does its work.**

Think about how many of your answers relied on that idea:

* Board doesn't expose its internal storage.
* Cell doesn't expose its state directly.
* Bot doesn't expose its algorithm.
* WinningCondition doesn't expose its implementation.
* Game doesn't expose presentation details.

That one sentence quietly connects almost everything we've discovered so far.

---

# 🚀 What Comes Next

I think we're at the perfect moment to do something we've intentionally postponed.

Tomorrow won't be:

> "Let's learn GRASP."

Instead, it will be:

> **"Let's look back at everything we've discovered over the last five days and see what the software engineering community decided to call these ideas."**

I have a feeling tomorrow will be one of those satisfying moments where you'll keep saying:

> "Wait... we've already been doing this."

And my answer will be:

> **Exactly.** That's why understanding lasts longer than memorization.
