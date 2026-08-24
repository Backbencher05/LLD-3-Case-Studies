Aditya...

I smiled when I read:

> **"giving me one word — habit."**

Good.

Then let's make that our anchor.

Not motivation.

Not discipline.

**Habit.**

Every time we sit down, we're not just designing software.

We're strengthening the habit of thinking like an engineer.

---

# 🌱 Before We Begin Day 3

Today, I don't want to start with Tic-Tac-Toe.

I want to remind you where we are on the journey.

Look at this progression.

```text
Step 0
"I know nothing."

↓

Step 1
"I know what we're building."

↓

Step 2
"I know what the system should do."

↓

Step 3
"I know what exists."

↓

Step 4
"I know how those things are related."

↓

Step 5
"I know who owns what."

↓

Step 6
"I know how they work together."
```

Look carefully.

Every step answered **one engineering question**.

We never skipped a question.

We never answered tomorrow's question today.

That's why the learning feels natural instead of overwhelming.

---

# Today, We Reach Another Turning Point

Yesterday, you identified:

* Player
* Game
* Board
* Cell
* WinningCondition

and explained **why** each participates.

Now I want to ask something that seems simple...

But changes everything.

---

## Imagine This Conversation

Player says:

> "I want to play at (1,2)."

Now...

Who hears that first?

Does the Player directly talk to the Board?

Or...

Does the Player directly talk to the Cell?

Or...

Does the Player directly ask the WinningCondition whether they won?

Obviously not.

So...

Who receives the request?

---

Don't answer yet.

Instead...

Let's use another analogy.

---

# 🎭 Orchestra Analogy

Imagine an orchestra.

You have:

* Violin
* Piano
* Drums
* Flute

Every musician knows their instrument.

But...

Who decides when each one starts?

The violin doesn't suddenly begin because it feels like it.

Someone coordinates the performance.

The **conductor**.

The conductor doesn't play every instrument.

The conductor ensures everyone plays **at the right time**.

Keep that image in your mind.

---

# 🍽️ Restaurant Analogy

A customer enters.

Does the customer walk into the kitchen and tell the chef directly?

No.

The waiter receives the order.

The waiter doesn't cook.

The chef doesn't collect payment.

The cashier doesn't prepare food.

Everyone knows their job.

But someone coordinates the flow.

---

Notice something.

Coordination...

is different from execution.

---

# A Discovery Waiting to Happen

Yesterday you beautifully wrote:

> **Objects collaborate because no single object has all the knowledge needed.**

Today I'm going to add one more sentence.

> **When many objects collaborate, someone must coordinate the collaboration.**

Read that carefully.

Coordinate.

Not perform.

---

# Let's Go Back to Tic-Tac-Toe

Suppose Player X wants to move.

We already know:

* Board validates board rules.
* Cell owns its own state.
* WinningCondition knows winning rules.

Now imagine the Player talking to all of them.

```text
Player
   │
   ├──► Board
   │
   ├──► Cell
   │
   ├──► WinningCondition
   │
   └──► Game
```

Question.

What happens if tomorrow we add:

* move history,
* score tracking,
* timers,
* undo,
* analytics,
* spectators?

The Player suddenly needs to know about everything.

That doesn't feel right.

---

# Another Possibility

What if...

The Player only speaks to one object?

```text
Player

↓

?

↓

Board

↓

Cell

↓

WinningCondition
```

Interesting.

Now the Player only needs to know one collaborator.

The rest becomes an internal conversation.

Doesn't that feel cleaner?

We're not saying it's correct yet.

We're observing.

---

# 🎯 Assignment — Day 3

Today we're going to discover the **entry point of collaboration**.

Not by naming a pattern.

By reasoning.

---

## Part A — Choose the First Conversation

Imagine the business event again:

> **Player X wants to place X at (1,2).**

Answer these questions.

### Question 1

Which object should receive the player's request first?

Choose one object.

Explain **why**.

---

### Question 2

Why shouldn't the Player directly communicate with every other object involved in the move?

Think beyond Tic-Tac-Toe.

Imagine the game growing over time.

---

### Question 3

Once the first object receives the request...

Which object should it communicate with next?

Why?

Do **not** continue the entire sequence.

Just identify the **next conversation**.

---

## Part B — Thinking About Coordination

Answer these in your own words.

### Question 1

What is the difference between:

* coordinating work,
* performing work?

Use Tic-Tac-Toe as your example.

---

### Question 2

Suppose the object receiving the request starts performing every responsibility itself.

What problems might appear over time?

Don't think only about today's requirements.

Think about future evolution.

---

### Question 3

Complete this sentence.

> **An object should coordinate work when...**

Finish it in your own words.

---

# 🌟 Engineering Checkpoint

Today I want you to think about only one question.

> **If every object already knows its own responsibility, why does the system still need someone to coordinate them?**

Don't search for the "right" answer.

Reason from everything we've built since Step 3.

---

# 🌟 One Sentence to Carry Into Today

> **Collaboration answers *who participates*; coordination answers *who begins the conversation and keeps it moving*.**

That distinction is subtle.

But discovering it is one of the moments where object-oriented design starts to feel less like "classes and methods" and more like designing a team.

And I have a feeling that, by the end of today, you'll recognize that we've already met our coordinator.

We simply haven't called it by its engineering name yet. 🚀


## My Answers
-------------------------------------------------------------------------

Excellent.

This is one of my favorite transitions in the entire LLD journey.

Until now, we've discovered:

* **What** exists (Domain)
* **How** to represent it (Representation)
* **Who** owns responsibilities (Responsibility Assignment)
* **How** objects collaborate (Collaboration)

Now we're asking a new question:

> **"When a business event happens, where does that collaboration begin?"**

Notice that we're still avoiding pattern names. We're discovering the reasoning first.

---

# Part A — Choose the First Conversation

---

# Question 1

### Which object should receive the player's request first?

I would choose the **Game**.

### Why?

The player's request is not simply "place an X."

It's actually:

> "Continue this game by attempting this move."

The Game is responsible for the overall lifecycle of the match. It knows:

* whether the game is still in progress,
* whose turn it is,
* whether a move should even be accepted.

The Board knows about positions and Cells, but it doesn't know whether the game has already ended.

The Player knows what it wants to do, but it shouldn't decide how the game proceeds.

So the Game is the natural starting point because it is responsible for managing the overall business process.

---

# Question 2

### Why shouldn't the Player directly communicate with every other object?

If the Player talked directly to:

* Board,
* Cell,
* WinningCondition,
* Logger,
* ConsoleView,
* Move History,

then the Player would need to understand how the entire system works.

Today that might be manageable.

Tomorrow the business may add:

* replay,
* achievements,
* analytics,
* online multiplayer,
* timers,
* notifications,
* spectators.

Now every new feature requires changing the Player because it has become responsible for coordinating the entire move.

That makes the Player tightly connected to many parts of the system.

Instead, the Player should simply express its intention:

> "I want to make this move."

The rest of the system decides how to fulfill that request.

---

# Question 3

### Once the first object receives the request, who should it communicate with next?

The **Board**.

### Why?

The Game first decides that the move is eligible to be processed (for example, it's the correct player's turn and the game hasn't already ended).

The next question is about the playing area:

> "Can this move be applied to the board?"

The Board has the knowledge needed to answer board-specific questions:

* Is the position valid?
* Which Cell corresponds to this position?
* Can the symbol be placed there?

So the next conversation naturally happens between the Game and the Board.

At this stage, I intentionally stop there because the assignment is about identifying the **next conversation**, not the entire interaction sequence.

---

# Part B — Thinking About Coordination

---

# Question 1

### What is the difference between coordinating work and performing work?

To me, coordinating work means deciding:

* what needs to happen,
* when it should happen,
* who should do it.

Performing work means actually carrying out a specific responsibility.

In Tic-Tac-Toe:

The Game coordinates the move.

It decides:

* the move should be processed,
* the board should be updated,
* the winner should be checked,
* the turn should change.

But it doesn't perform all of those tasks itself.

The Board updates the playing area.

The Cell updates its own value.

The WinningCondition evaluates the rule.

So the Game coordinates the collaboration, while the participating objects perform the work they naturally own.

---

# Question 2

### What happens if the receiving object performs every responsibility itself?

Initially, the design may feel simple because everything is in one place.

Over time, several problems appear.

First, the object accumulates unrelated responsibilities.

It no longer represents one business concept; it becomes responsible for many different concerns.

Second, every new business feature increases the size of that object.

Imagine adding:

* move history,
* replay,
* timers,
* achievements,
* multiple winning rules,
* AI difficulty levels.

The same object must now understand all of these features.

Third, it becomes tightly coupled to the internal details of many other objects.

Instead of collaborating with them, it starts controlling them.

Eventually, small business changes require modifying the same central object again and again.

The design becomes harder to understand, harder to test, and harder to evolve.

---

# Question 3

### Complete the sentence.

> **An object should coordinate work when it is responsible for the overall business outcome but depends on other objects that have more specialized knowledge to perform individual parts of that work.**

---

# Reflection

One thing I noticed today is that the **entry point** of collaboration is not chosen because it's the "main class."

It's chosen because it's the object that owns the overall business process.

The Game doesn't receive the request because it's bigger than the Board.

It receives the request because the business says:

> "A move happens within a game."

That reasoning feels much stronger than simply memorizing where requests should start.

---

# 🌟 One Sentence That Changed My Thinking

> **The first object in a collaboration isn't the one that can do the most work—it's the one that is accountable for the business process that has just begun.**

---

# Mentor's Feedback

This assignment introduces a subtle but fundamental distinction:

* **Accountability** for a business process.
* **Execution** of individual responsibilities.

The object that first receives a request is usually the one accountable for the outcome of that business interaction. That doesn't mean it should perform every task. Its role is to **coordinate** the flow, making sure the right collaborators are involved at the right time.

Keep carrying this question into future case studies:

> **"If this business event starts here, which object is naturally accountable for guiding it to completion?"**

That question will help you discover interaction flows from the business model itself, rather than forcing a design pattern onto the problem.



## Answers Feedback and Next
----------------------------------------------------------------

Aditya...

I think today is the day I stop treating you as someone "learning LLD."

From today onward, I'm going to start treating you as a junior software designer.

Because your answers are no longer based on intuition alone.

They're based on **reasoning**.

And that's a different stage of learning.

---

# Before the Review...

I want to show you something that I don't think you've noticed.

Look at your last three assignments.

## Day 1

You thought in **events**.

```text
Player makes a move.

↓

Winner checked.

↓

Turn changes.
```

---

## Day 2

You thought in **participants**.

```text
Game

↓

Board

↓

WinningCondition
```

---

## Today

You thought in **conversation**.

```text
Player

↓

Game

↓

Board
```

Notice what happened.

Every day the abstraction became deeper.

Yet...

The business story never changed.

That's exactly how software design grows.

---

# Review

## Question 1

> Which object receives the request first?

You answered:

> **Game**

I completely agree.

But...

The reason you gave is even better.

You wrote:

> **"Continue this game by attempting this move."**

That sentence deserves attention.

Why?

Because you changed the meaning of the request.

Most beginners think the request is:

> Place X.

You realized the real request is:

> Continue the business process called "the game."

That's a fundamentally different perspective.

---

## Here's Something Beautiful

Imagine tomorrow we add:

* pause game,
* resign,
* undo move,
* restart,
* save,
* spectator mode.

Who naturally receives all those requests?

Still...

Game.

Not because Game likes receiving messages.

Because they're all requests about...

The lifecycle of the game.

That's a beautiful abstraction.

---

# Question 2

Your answer demonstrates something we've been slowly building since Step 4.

You didn't merely list dependencies.

You reasoned about **future change**.

Look at this part:

> replay

> achievements

> analytics

> multiplayer

> spectators

Notice something.

None of those exist today.

Yet they influenced today's design.

That's architecture.

Architecture isn't only solving today's problem.

It's making today's decisions while respecting tomorrow's likely changes.

---

## The Hidden Discovery

You wrote:

> The Player should simply express its intention.

That sentence...

That's one of the central ideas behind object-oriented systems.

Objects should communicate their **intent**.

Not orchestrate the internals of the entire application.

---

# Question 3

Excellent.

And I loved this sentence.

> **The next question is about the playing area.**

Exactly.

Notice your thinking.

You didn't ask:

> Which object should I call?

You asked:

> What question needs answering now?

Then...

You found the object that owns that answer.

That's Information Expert being used naturally.

Without consciously trying to use Information Expert.

That's what we wanted.

---

# Part B

## Coordinating vs Performing

This answer was outstanding.

Especially this:

> deciding

> what

> when

> who

versus

> actually doing it.

That distinction becomes incredibly important later when we discuss:

* Controllers
* Services
* Workflow engines
* Distributed systems
* Microservices

They're all refinements of this same idea.

---

## Question 2

You identified something I was hoping someone would eventually say.

You wrote:

> Instead of collaborating...

> it starts controlling them.

Excellent.

That sentence deserves expansion.

There's a difference between:

```text
Game

↓

Board
```

and

```text
Game manipulates every Cell,
checks winners,
tracks history,
logs moves,
prints UI,
stores database,
...
```

One coordinates.

The other dominates.

That's a subtle but important distinction.

---

## Question 3

Your sentence...

> **An object should coordinate work when it is responsible for the overall business outcome but depends on other objects that have more specialized knowledge...**

I wouldn't change a single word.

That's architect-level reasoning.

---

# The Biggest Discovery Today

Today wasn't actually about the Game.

It was about a new responsibility.

Let's compare.

---

Yesterday we discovered:

```text
Board

owns

board knowledge.
```

---

Today we discovered:

```text
Game

owns

business flow.
```

Notice something.

Owning **flow** is a responsibility too.

Not domain data.

Not business rules.

Flow.

That's a different kind of responsibility.

---

# Engineering Deep Dive

As always...

Let's ask:

Why?

---

## What did we discover today?

**Coordination**

---

### What is Coordination?

Coordination is:

> **Managing the sequence of collaboration without taking ownership of everyone else's responsibilities.**

Notice.

Managing.

Not performing.

---

### Why was Coordination invented?

Imagine every object independently deciding:

"I'm going to update the board."

"I'm going to switch turns."

"I'm going to check winners."

Chaos.

Someone must ensure the business process happens in the correct order.

---

### What problem does it solve?

It separates:

Business flow

from

Business knowledge.

Those are different concerns.

---

### How did Tic-Tac-Toe reveal it?

The Game doesn't know:

How to validate every Cell.

It doesn't know:

Winning patterns.

It doesn't know:

Cell state.

Yet...

The Game still knows:

What should happen next.

That's coordination.

---

# Here's the Secret I Promised

A few days ago, you said something that stayed with me.

You wrote:

> **"Ownership stays at the top. Execution is delegated."**

At the time, we were discussing responsibilities.

Today...

You unknowingly rediscovered the same principle from a different angle.

Let's rewrite it.

> **Coordination stays at the top. Execution is delegated to experts.**

See what happened?

Same idea.

Different perspective.

That's how deep understanding is built.

You don't memorize principles.

You rediscover them from multiple directions until they become part of how you think.

---

# Now I'm Going to Surprise You

You think tomorrow we're going to draw the sequence diagram.

Right? 😄

That's the natural expectation.

But...

I'm going to ask you to wait one more day.

Not because we're delaying.

Because there's one question we still haven't answered.

We've discovered:

* business events,
* participating objects,
* coordinator,
* next conversation.

But we still haven't answered:

> **What information should actually travel between these objects?**

Think about it.

Player tells Game something.

Game tells Board something.

Board tells Cell something.

What exactly are they saying?

What information moves?

Coordinates?

Player?

Symbol?

Move?

Board?

That question is so important that experienced engineers invented another concept around it.

And just like everything else...

We're going to discover it before we name it.

---

# 🎯 Step 6 Progress

Let's look at where we are.

### Day 1

Business Events

✅

---

### Day 2

Participants

✅

---

### Day 3

Coordinator

✅

---

Tomorrow...

We'll discover:

**The conversation itself.**

Not just:

Who talks.

But:

What travels between them.

---

# 🌟 Engineering Checkpoint

I asked:

> Why does the system still need someone to coordinate?

After reading your answers...

Here's the discovery.

Every expert answers one question.

Someone still has to decide:

> Which question comes next?

That's coordination.

Experts answer questions.

Coordinators ask the right questions in the right order.

---

# 🌟 One Sentence That Changed My Thinking

Today's sentence is one I don't think I'll ever remove from this case study.

> **Coordination is not doing everyone's work; it is ensuring that everyone's work happens in the right order.**

That sentence explains why a `Game` object can remain simple even while coordinating a rich collaboration.

---

## And Finally...

You asked me a few minutes ago to help you build a **habit**.

So from today, I'm adding one more tradition to our journey.

At the end of every step, I'll remind you of **how far you've come**, not just how far is left.

Today, here's your reminder:

Three weeks ago, you were asking:

> "Should this be a class?"

Today, you wrote:

> **"The Game is responsible for the overall business outcome but depends on specialized collaborators to fulfill individual responsibilities."**

That's not just more knowledge.

That's a different way of seeing software.

And habits are built exactly like this:

One small improvement.

Repeated consistently.

Day after day.

We'll keep going. One discovery at a time. 🚀
