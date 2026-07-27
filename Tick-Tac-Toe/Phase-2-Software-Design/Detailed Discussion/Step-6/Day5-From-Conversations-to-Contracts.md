Aditya...

I think today is the day where everything starts coming together.

We've spent four days talking about collaboration.

Some people might ask:

> "Why didn't we just draw the sequence diagram on Day 1?"

Because if I had...

You would have drawn arrows.

Today...

You're about to understand **why those arrows exist.**

That difference matters.

---

# 🎬 Step 6 — Day 5

## From Conversations to Contracts

Let's revisit yesterday.

We discovered this:

```text
Player

↓

Game

↓

Board

↓

Cell

↓

WinningCondition
```

And we also discovered:

* what information travels,
* what information should not travel.

Now I want to ask something deeper.

---

## Imagine This Conversation

Game says to Board:

> "Please apply this move."

Question.

How does the Board know what **"apply this move"** means?

It doesn't.

Unless...

Both objects have agreed on **how they communicate**.

Interesting.

---

# A Real-World Analogy

Imagine you call customer support.

You say:

> "I need help."

The agent replies:

> "Please tell me your order number."

Why?

Because there is an agreed way of starting the conversation.

Imagine instead you said:

> "Blue elephant."

The agent wouldn't know what to do.

Not because they're incapable.

Because there is **no shared agreement** about what that message means.

Communication requires an agreement.

---

Software is exactly the same.

---

# Another Analogy

Suppose you're plugging a charger into your phone.

The charger doesn't ask:

> "How is your battery implemented internally?"

The phone doesn't ask:

> "How do you generate electricity?"

They simply agree on:

* connector shape,
* voltage,
* protocol.

Neither side needs to understand the other's internals.

They only agree on **how to interact**.

---

# The Hidden Discovery

Yesterday we discovered messages.

Today we ask:

> **What makes those messages reliable?**

Answer:

They follow an agreement.

Let's call that agreement a **contract**.

Don't think "Java interface" yet.

Forget programming.

Think only about collaboration.

---

# Tic-Tac-Toe

Game wants the Board to help.

Question.

Does the Game need to know:

* how the Board stores Cells?
* how it validates positions?
* whether it uses arrays?
* whether it uses a hash map?

No.

Then what does the Game need to know?

Only this:

> "If I ask you to apply a move, you'll either apply it or tell me why you can't."

That's the agreement.

Not the implementation.

---

# Another Example

Imagine you hire a carpenter.

You say:

> "Please build this table."

Do you also tell the carpenter:

* which muscles to move,
* which angle to hold the hammer,
* how to breathe?

Of course not.

You care about the **result**.

Not the implementation.

The carpenter owns the implementation.

You both agree on the expected outcome.

That's another contract.

---

# Something Beautiful Is Happening

Let's look at our discoveries.

Step 5:

Who owns responsibility?

↓

Step 6 Day 2:

Who participates?

↓

Day 3:

Who coordinates?

↓

Day 4:

What information travels?

↓

Today:

What agreement allows the collaboration?

Do you see it?

We're peeling software apart layer by layer.

---

# 🎯 Assignment — Day 5

Today we're going to discover collaboration contracts.

---

## Part A — The Agreements Between Objects

For each collaboration below, answer:

### Collaboration 1

**Game → Board**

What does the Game expect from the Board?

Not implementation.

The outcome.

What promises should the Board make?

---

### Collaboration 2

**Board → Cell**

What agreement exists between the Board and a Cell?

What should the Board be allowed to expect?

---

### Collaboration 3

**Game → WinningCondition**

What should the Game expect?

What should it never need to know?

---

## Part B — Thinking About Contracts

### Question 1

Complete the sentence:

> **A collaboration works well when both objects agree...**

---

### Question 2

Suppose the Board completely changes its internal implementation.

Under what condition should the Game remain completely unaffected?

---

### Question 3

Why is it dangerous if one object depends on *how* another object performs its work instead of *what* it promises to do?

Try to reason from the business, not from programming languages.

---

## Part C — Looking Back

We've now discovered:

* responsibilities,
* collaboration,
* coordination,
* messages.

Where do contracts fit into that journey?

Write a few paragraphs explaining how today's discovery connects with everything we've already learned.

---

# 🌟 Engineering Checkpoint

Today I want you to think about one question.

> **If two objects trust each other's promises instead of each other's implementation, what becomes easier to change in the future?**

Don't answer quickly.

Think about everything we've built since Step 3.

---

# 🌟 One Sentence to Carry Into Today

> **Good collaboration is built not on knowing another object's implementation, but on trusting the promises it makes.**

---

## One Small Hint...

I'm going to tell you something that I intentionally hid until today.

Many people think software design starts with:

```java
interface Board {
    ...
}
```

I disagree.

That `interface` is just **one possible expression** of something much older.

The real idea isn't an interface.

The real idea is:

> **A trustworthy agreement between collaborators.**

Programming languages simply give us ways to express that agreement.

Just like sequence diagrams express collaboration.

Just like class diagrams express structure.

The notation came later.

The engineering idea came first.

And I think that's one of the biggest themes of our entire mentorship.

Let's discover it together. 🚀


-----------------------------------------------------------------------------------------------------------------------------
## My Answers
-----------------------------------------------------------------------------------------------------------------------------

Excellent.

Today is one of those days where the word **"contract"** can sound technical, but the idea is actually something we experience every day.

Think about ordering food at a restaurant.

You don't tell the chef:

* which pan to use,
* how long to cook,
* where the vegetables came from.

You care about one thing:

> **"If I order this meal, I expect to receive this meal."**

That's a contract.

Software collaboration works the same way.

Objects don't collaborate because they know each other's internals.

They collaborate because they trust each other's **promises**.

---

# Part A — The Agreements Between Objects

---

# Collaboration 1

## Game → Board

### What does the Game expect from the Board?

The Game expects the Board to correctly manage the playing area.

When the Game asks the Board to validate or apply a move, it expects an outcome such as:

* the move can be applied, or
* the move cannot be applied.

If the move is accepted, the Game expects the Board's state to accurately reflect that change.

### What promises should the Board make?

The Board promises:

* it will correctly represent the playing area,
* it will enforce board-related rules,
* it will maintain a consistent board state,
* it will not allow impossible board states to exist.

Notice what the Game is **not** promised.

The Game is not promised:

* how the Board stores information,
* whether it uses Cells,
* whether it uses arrays,
* whether it uses another internal structure.

Those implementation choices belong entirely to the Board.

---

# Collaboration 2

## Board → Cell

### What agreement exists?

The Board expects each Cell to manage its own state correctly.

If the Board asks a Cell whether it is empty, it expects a truthful answer.

If the Board asks a Cell to update itself, it expects the Cell to update only its own state while remaining valid.

### What should the Board be allowed to expect?

The Board should be able to rely on the Cell to:

* know its own state,
* protect that state,
* respond consistently.

The Board should **not** need to know how the Cell stores its value internally.

---

# Collaboration 3

## Game → WinningCondition

### What should the Game expect?

The Game expects the WinningCondition to correctly evaluate the current game state and determine whether a winning condition has been satisfied.

The Game doesn't need to understand the algorithm.

It only needs a reliable answer.

### What should it never need to know?

The Game should never depend on:

* whether rows are checked first,
* whether diagonals are checked first,
* whether the implementation uses loops, recursion, or any other technique.

Those are implementation details.

The promise is simple:

> "Given the current board state, tell me whether someone has won."

---

# Part B — Thinking About Contracts

---

# Question 1

### Complete the sentence.

> **A collaboration works well when both objects agree on the outcome they expect from each other while remaining independent of how that outcome is achieved.**

---

# Question 2

### Suppose the Board completely changes its internal implementation.

### Under what condition should the Game remain completely unaffected?

The Game should remain unaffected as long as the **Board continues to fulfill the same business promises**.

From the Game's perspective, the Board still represents the playing area.

If the Board can still:

* validate moves,
* apply valid moves,
* provide the current board state when needed,

then the Game shouldn't care whether the Board uses Cells, symbols, bitboards, or any other representation internally.

The contract has remained the same, even though the implementation has changed.

---

# Question 3

### Why is it dangerous if one object depends on how another object performs its work instead of what it promises to do?

From the business perspective, collaboration is about **results**, not procedures.

Imagine a customer orders a pizza.

The customer expects:

> "Deliver me a pizza."

The customer should not need to know:

* which oven is used,
* how many cooks are involved,
* which knife slices it.

If tomorrow the restaurant buys a better oven, customers shouldn't need to change how they place orders.

The same applies in software.

If one object depends on another object's internal process instead of its promise, then every internal improvement becomes a breaking change.

Objects stop being independent collaborators and become tightly connected.

That makes the entire system harder to evolve because improvements in one place unexpectedly ripple into many others.

---

# Part C — Looking Back

When we started this journey, we first asked:

> **What exists in the business?**

That gave us our domain model.

We discovered concepts such as the Game, Board, Player, Cell, Position, and WinningCondition.

The focus was on understanding the business before thinking about software.

Next, we asked:

> **How should software represent these concepts?**

That helped us distinguish between Domain Classes, Value Objects, Policy Objects, and concepts that didn't deserve their own class at all.

Then we asked:

> **Who should own each responsibility?**

Instead of assigning behavior randomly, we looked for the object that naturally had the knowledge and authority to perform it.

After that, we explored:

> **How do these objects work together?**

We stopped thinking about isolated classes and started thinking about collaboration.

Each object contributed its own expertise rather than trying to perform every responsibility itself.

Then we examined:

> **What information should travel between collaborators?**

We realized that collaboration isn't just about talking—it's about communicating only the information necessary for another object to fulfill its responsibility while protecting internal knowledge.

Today's discovery completes that picture.

Now we ask:

> **What do collaborators promise each other?**

Responsibilities tell us **who owns the work**.

Collaboration tells us **who works together**.

Messages tell us **what information is exchanged**.

Contracts tell us **what each collaborator can reliably expect from the others**.

That final piece allows objects to evolve independently while continuing to work together.

Instead of depending on each other's internal implementation, they depend on shared business expectations.

To me, that's the biggest lesson of today:

A good software system isn't held together by knowledge of internal details.

It's held together by **trustworthy agreements between focused collaborators**.

---

# 🌟 One Sentence That Changed My Thinking

> **Objects collaborate successfully not because they know how each other works, but because they trust the promises each other makes.**

---

# Mentor's Feedback

This day completes a beautiful progression:

* **Step 5** taught us to assign the right responsibilities.
* **Step 6 (Days 1–2)** showed us how those responsible objects collaborate to fulfill a business story.
* **Step 6 (Days 3–4)** refined that collaboration by identifying where it begins and what information should flow.
* **Today** adds the final layer: **trust**.

The most valuable realization is that collaboration isn't just communication—it's **communication built on stable expectations**.

When two objects collaborate through clear contracts:

* each object remains focused on its own responsibilities,
* internal improvements stay local,
* the rest of the system continues to work because the promises haven't changed.

That way of thinking scales far beyond Tic-Tac-Toe. Whether you're designing a payment system, an e-commerce platform, or a distributed service, the same progression applies:

> **Understand the business → assign responsibilities → collaborate → exchange only necessary information → rely on stable promises rather than internal details.**

That's not just an object-oriented technique; it's a general engineering mindset for building systems that can grow without becoming fragile.

-----------------------------------------------------------------------------------------------------
## Answers Feedback and Next
-------------------------------------------------------------------------------------------------
Aditya...

I had to read your Part C twice.

Not because it was complicated.

Because I wanted to convince myself that the person writing it is the same person who, a few weeks ago, asked:

> "Should this be a class?"

There is a visible transformation in your thinking.

And today, I want to show you **where it happened.**

---

# Before the Review...

Let's zoom out.

When we started Step 6, we had only one sentence.

> **Player makes a move.**

Look at what that single sentence has unfolded into.

```text
Business Event
        │
        ▼
Participants
        │
        ▼
Coordinator
        │
        ▼
Messages
        │
        ▼
Contracts
```

Think about this.

We still haven't written a single line of production code.

Yet...

The architecture is already beginning to exist.

That's why experienced engineers spend so much time thinking before typing.

---

# Review

## Collaboration 1

### Game → Board

Your answer is excellent.

But one sentence deserves to become permanent.

You wrote:

> **The Game expects the Board to correctly manage the playing area.**

Exactly.

Notice what you did **not** write.

You didn't say:

> "The Game expects the Board to use a 2D array."

Or:

> "The Game expects a list of Cells."

You described the expectation in **business language**.

That matters.

Contracts should be stable because businesses change more slowly than implementations.

---

### Here's Something Beautiful

You wrote:

> The Board promises it will not allow impossible board states to exist.

That sentence is stronger than you may realize.

It means the Board isn't just storing data.

It is protecting an **invariant**.

We haven't introduced that word yet.

So let's discover it.

---

## A New Discovery

Imagine a Cell containing both `X` and `O`.

Could that ever happen?

No.

Imagine the Board accepting a move outside its boundaries.

No.

Why?

Because some states should **never exist**.

Every responsible object protects those truths.

That's another hidden responsibility.

Not just doing work.

Protecting correctness.

We'll return to this in a future step.

---

# Collaboration 2

Board → Cell

This answer shows something subtle.

You wrote:

> **The Board should rely on the Cell to know and protect its own state.**

Notice the word **protect**.

Earlier in our journey, we kept asking:

> Who owns this?

Today you're naturally asking:

> Who protects this?

Ownership and protection are deeply connected.

If you own something, you're responsible for keeping it valid.

---

# Collaboration 3

Game → WinningCondition

You wrote:

> **The Game only needs a reliable answer.**

That sentence...

That's the essence of a contract.

Imagine hiring a lawyer.

You care that they give sound legal advice.

You don't care whether they used five books, ten cases, or a search engine.

The value is in the outcome.

The implementation belongs to the expert.

---

# Part B

## Question 1

You completed:

> **...agree on the outcome they expect while remaining independent of how that outcome is achieved.**

Perfect.

Notice how many discoveries came together.

* responsibilities,
* collaboration,
* messages,
* boundaries,
* implementation hiding.

All inside one sentence.

---

## Question 2

This answer contains a principle that appears in almost every architecture book.

But you reached it without the name.

You wrote:

> **The contract has remained the same, even though the implementation has changed.**

That sentence explains why good software survives years of evolution.

Not because implementations never change.

Because promises stay stable.

---

## Question 3

Your pizza analogy is excellent.

But I want to show you why.

You explained it entirely from the customer's perspective.

Exactly.

A contract is always defined by the **consumer's expectation**.

Not by the producer's internal process.

That perspective is remarkably important.

---

# Part C

Aditya...

This is where I stopped reading as a reviewer.

And started reading as someone watching an engineer emerge.

Look at how you summarized the journey.

You didn't write:

> Step 3...

> Step 4...

> Step 5...

Instead...

You wrote the questions.

> What exists?

> Who owns what?

> How do they collaborate?

> What information travels?

> What do they promise?

That's exactly how experienced designers think.

Not in chapter names.

In design questions.

---

# The Biggest Discovery Today

Today wasn't really about contracts.

It was about **trust**.

Let's imagine a football team.

The goalkeeper trusts the defenders.

The defenders trust the midfield.

The striker trusts that the ball will arrive.

They don't inspect each other's training methods before every pass.

They rely on agreed responsibilities and expected outcomes.

Software is the same.

Objects don't collaborate because they know each other's internals.

They collaborate because they **trust each other's promises**.

That's a profound shift in thinking.

---

# Engineering Deep Dive

As always...

Let's ask:

Why?

---

## What did we really discover today?

**Collaboration Contracts**

---

### What is a Contract?

A contract is:

> **A shared agreement about what one object can expect from another without needing to know how it fulfills that expectation.**

Notice.

Not a Java interface.

Not an API.

Those are ways to express a contract.

The contract itself is the engineering idea.

---

### Why were Contracts invented?

Imagine every collaborator depending on another object's internal logic.

Now every improvement becomes a breaking change.

Contracts separate:

Expectation

from

Implementation.

---

### What problem do they solve?

They allow independent evolution.

One object can improve itself without forcing every collaborator to change.

---

### How did Tic-Tac-Toe reveal this?

Game doesn't care:

* how Board stores state,
* how WinningCondition checks patterns,
* how Cell stores values.

It cares only that they fulfill their promises.

---

# And Now...

I'm going to reveal something.

We've quietly built a complete chain.

```text
Business Event

↓

Responsibility

↓

Collaboration

↓

Coordination

↓

Message

↓

Contract
```

Read that chain again.

Every arrow answers one engineering question.

If someone handed you a blank editor today and said:

> "Implement Tic-Tac-Toe."

You wouldn't start with classes anymore.

You'd start asking these questions.

That is the mindset we've been trying to build since Step 0.

---

# The Surprise

Remember how you expected to reach class diagrams after Step 5?

Now ask yourself honestly.

If we had drawn a class diagram back then...

Would it have contained:

* responsibilities?
* collaboration?
* coordination?
* message boundaries?
* contracts?

No.

It would have been a picture of boxes and lines.

Today, if we draw one, every line has meaning.

That's the difference.

---

# So... What Comes Next?

You might think:

> "Now we finally draw the sequence diagram."

Almost.

But there is one final discovery inside Step 6.

And I think it's the one that transforms collaboration into implementation.

We've answered:

* Who talks?
* What they say?
* What they promise?

Now there's one last question:

> **How do we keep these conversations from becoming chaotic as the system grows?**

Because today we only have:

* Game
* Board
* Cell
* WinningCondition

Tomorrow we might have:

* MoveHistory
* ScoreBoard
* Timer
* Achievements
* AI
* Replay
* Notifications
* Analytics

The conversations can explode.

Engineers had to invent ways to keep those collaborations manageable.

And just like every previous topic...

We're going to discover **why** before we ever learn **what**.

---

# 🌟 Engineering Checkpoint

Today I asked:

> **If two objects trust each other's promises instead of each other's implementation, what becomes easier to change?**

Your entire assignment answered it.

Not just the Board.

The entire system.

Because change stops propagating through implementation details.

It stays contained behind trusted agreements.

---

# 🌟 One Sentence That Changed My Thinking

Today's sentence comes directly from your own conclusion.

> **A software system stays flexible not because its objects know each other well, but because they trust each other's promises.**

I don't think there could have been a better ending to today's discovery.

---

# Before We Move to the Final Day of Step 6

I want to leave you with one reflection.

Back in Step 3, we discovered **objects**.

Today, we discovered something much more important.

Not objects.

**Relationships between minds.**

Think about that.

Every object in our system represents a focused responsibility.

Every collaboration represents a conversation.

Every contract represents trust.

That means software isn't really about objects.

It's about designing a society where each member:

* knows its role,
* communicates clearly,
* keeps its promises,
* and trusts others to keep theirs.

That's why object-oriented design often feels surprisingly human.

Because, at its heart, it's about designing good teams.

And after watching your answers over the last few days, I think you're no longer just learning object-oriented design.

You're learning to think like the person who designs those teams.

Let's finish Step 6 together. 🚀
