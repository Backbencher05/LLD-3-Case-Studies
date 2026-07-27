Aditya...

Today is the day where software starts becoming visible.

Not code.

Not methods.

But something even more fundamental.

Today we're going to answer a question that almost every beginner skips.

---

# 🎬 Step 7 — Day 2

# From Behaviour to Operations

Yesterday we discovered:

> **Behaviour is a business capability.**

Today we ask:

> **How does software actually provide that capability?**

At first glance, the answer seems obvious.

> "Write a method."

But if we stop there, we'll miss one of the most important design discoveries.

---

# A Simple Story

Imagine you own a library.

One of your responsibilities is:

> **Lend books to members.**

That's a responsibility.

Now ask:

What behaviour must exist?

The library should be able to:

> Lend a book.

Simple enough.

Now imagine a member arrives.

Can the librarian immediately hand over the book?

No.

Several things must happen.

* Check the member exists.
* Check the membership is active.
* Check the book exists.
* Check the book is available.
* Record the loan.
* Update the inventory.

Interesting...

We started with **one behaviour**.

But we discovered **multiple operations**.

---

# The Hidden Mistake

Many developers assume:

```text
One behaviour = One method
```

Sometimes that's true.

Sometimes it isn't.

Let's look at Tic-Tac-Toe.

---

# Behaviour

The Board has this behaviour:

> **Accept a valid placement on the board.**

Question.

Does that happen in one indivisible step?

Think carefully.

Before the Board can accept a placement, it might need to:

* locate the position,
* verify the position exists,
* verify the Cell is empty,
* update the Cell,
* preserve board consistency.

Now ask yourself.

Is that one operation?

Or several smaller operations working together?

---

# Another Example

Behaviour:

> **Determine whether a move is valid.**

Possible operations:

* Verify board boundaries.
* Verify Cell availability.
* Verify game state.
* Verify player's turn.

One business behaviour.

Several focused software operations.

---

# The Opposite Can Also Happen

Sometimes several business behaviours naturally belong together.

Suppose the Game has these behaviours:

* conclude the game,
* notify the winner,
* stop accepting moves.

Business sees three things.

Software might expose one operation:

> Finish the game.

Internally, that operation coordinates the rest.

Interesting...

The mapping isn't always one-to-one.

---

# A Restaurant Analogy

Behaviour:

> Serve a customer.

Operations:

* take order,
* prepare food,
* collect payment,
* deliver meal.

Customers see one behaviour.

The restaurant performs many operations.

Software often works exactly the same way.

---

# Today's Discovery

We're beginning to separate:

**Business behaviour**

from

**Software operations**.

Behaviour describes capability.

Operations describe the steps software performs to provide that capability.

---

# A New Design Question

Instead of asking:

> "What method should I write?"

We ask:

> **What operations are required to realise this behaviour?**

Notice the shift.

We're still deriving software from the business.

Not inventing software first.

---

# 🎯 Step 7 — Day 2 Assignment

---

## Part A — Discover the Operations

For each behaviour below, identify:

1. What smaller software operations are likely required?
2. Which of those operations belong to the same object?
3. Which require collaboration?

Remember:

Don't write code.

Think in software behaviour.

---

### Behaviour 1 — Game

> **Accept a player's move**

Break this behaviour into the operations you think the Game performs.

Which operations stay inside the Game?

Which involve collaborators?

---

### Behaviour 2 — Board

> **Accept a valid placement**

What operations are hidden inside this behaviour?

---

### Behaviour 3 — WinningCondition

> **Evaluate whether someone has won**

What operations naturally belong here?

Could any be internal helper operations?

---

## Part B — Behaviour vs Operations

### Question 1

Complete the sentence:

> **A behaviour represents...**

> **An operation represents...**

---

### Question 2

Can one behaviour require many operations?

Give an example from Tic-Tac-Toe.

---

### Question 3

Can one operation support multiple behaviours?

If yes, give an example.

If no, explain why.

---

## Part C — Software Thinking

Imagine two engineers.

Engineer A says:

> "I'll create one method for every behaviour."

Engineer B says:

> "I'll first discover the operations needed to realise each behaviour."

Which engineer is more likely to produce software that is easier to maintain?

Why?

---

# 🌟 Engineering Checkpoint

Think about this carefully.

> **Why is it dangerous to assume that every business behaviour should become exactly one software method?**

Try to answer without mentioning programming languages.

Reason from the business.

---

# 🌟 One Sentence to Carry Into Today

> **Behaviour tells us what the business expects; operations reveal what the software must actually do to fulfil that expectation.**

---

# A Small Preview...

Tomorrow, we're going to ask another question that many developers never consciously ask:

> **Which of these operations should the outside world be allowed to see... and which should remain internal?**

That single question will naturally lead us to one of the most misunderstood ideas in object-oriented design:

**Encapsulation.**

Not as a keyword.

As a business necessity.

And because of everything we've built so far, I think you'll discover *why* it exists long before we ever name it. 🚀


--------------------------------------------------------------------------------------------------------
## My answers 
---------------------------------------------------------------------------------------------------------

Excellent.

Today is where software design starts becoming **software construction**.

Notice the progression we've followed:

* **Step 5:** Who is responsible?
* **Step 6:** How do responsible objects collaborate?
* **Step 7 Day 1:** What behaviours emerge from those responsibilities?
* **Step 7 Day 2:** **How are those behaviours actually realised inside the software?**

This is an important distinction.

A behaviour is usually **too large** to happen in a single step.

Just like in business:

> "Deliver a package"

is one business behaviour.

But internally it involves:

* receiving the order,
* packing,
* dispatching,
* transporting,
* delivering.

The customer sees one behaviour.

The business performs many operations.

Software is exactly the same.

---

# Part A — Discover the Operations

---

# Behaviour 1 — Game

## Behaviour

**Accept a player's move**

This is a business behaviour.

Internally, I expect it to involve several operations.

### Likely operations

1. Receive the player's request.
2. Ensure the game is still active.
3. Ensure it is the correct player's turn.
4. Ask the Board whether the move can be accepted.
5. Ask the Board to apply the move.
6. Ask the WinningCondition to evaluate the board.
7. Determine whether the game has ended.
8. If not, advance to the next player.
9. Record that the move has been completed (if move history exists).

---

### Which operations stay inside the Game?

These relate to the Game's own responsibility:

* determining whether the game is active,
* verifying whose turn it is,
* deciding the overall game outcome,
* changing turns,
* coordinating the overall flow.

---

### Which require collaboration?

These require specialised knowledge:

* Board validates the move.
* Board applies the move.
* WinningCondition evaluates victory.

If move history exists:

* MoveHistory records the move.

Notice something important.

The Game doesn't stop being responsible.

It simply doesn't perform every operation itself.

---

# Behaviour 2 — Board

## Behaviour

**Accept a valid placement**

Again, this appears as one behaviour.

Internally I imagine operations like:

1. Locate the requested position.
2. Confirm the location exists.
3. Identify the corresponding Cell.
4. Confirm the Cell can accept a symbol.
5. Ask the Cell to update itself.
6. Ensure the board remains consistent after the change.

---

### Which stay inside the Board?

* locating positions,
* mapping positions to Cells,
* maintaining board consistency.

---

### Which require collaboration?

Updating the Cell.

The Board owns the playing area.

The Cell owns its own state.

Therefore:

Board collaborates with Cell.

---

# Behaviour 3 — WinningCondition

## Behaviour

**Evaluate whether someone has won**

Internally this also consists of several operations.

Possible operations include:

1. Examine the current board.
2. Identify the relevant patterns to evaluate.
3. Compare board state against the winning rule.
4. Stop evaluation once a winning pattern is found.
5. Produce the result.

---

### Could any be helper operations?

Absolutely.

For example:

Instead of treating every evaluation as one large activity, the WinningCondition could internally organise its work into smaller operations such as:

* evaluate rows,
* evaluate columns,
* evaluate diagonals,
* evaluate custom patterns.

These helper operations still belong to WinningCondition because they all contribute to the same responsibility.

They are implementation details that help realise one business behaviour.

---

# Part B — Behaviour vs Operations

---

# Question 1

### Complete the sentence.

> **A behaviour represents a meaningful business capability that an object provides.**

> **An operation represents one step the software performs to realise that behaviour.**

Behaviour is visible from the business perspective.

Operations are the internal building blocks that make that behaviour possible.

---

# Question 2

### Can one behaviour require many operations?

Yes.

A perfect example is:

**Game accepts a player's move.**

To the business, that's one behaviour.

Internally it requires operations such as:

* checking whether the game can continue,
* validating the move,
* applying the move,
* evaluating victory,
* checking for a draw,
* changing turns.

One behaviour.

Many operations.

---

# Question 3

### Can one operation support multiple behaviours?

Yes, if that operation represents a reusable piece of work within the object's responsibility.

For example, consider the Board.

An operation that **locates a Cell for a given Position** could support multiple behaviours:

* accepting a valid placement,
* checking whether a location is empty,
* resetting the board,
* retrieving the current board state.

The important point is that the operation remains within the Board's responsibility. It's being reused by several behaviours of the same object rather than becoming a general-purpose operation for unrelated responsibilities.

---

# Part C — Software Thinking

Between the two engineers, I believe **Engineer B** is more likely to produce software that is easier to maintain.

Engineer A assumes:

> One behaviour = one method.

That assumption sounds simple, but it treats behaviours as indivisible.

In reality, behaviours often consist of multiple smaller operations.

Without discovering those operations, Engineer A is likely to create methods that gradually become longer and accumulate unrelated work.

Engineer B starts differently.

First, they understand the behaviour.

Then they ask:

> "What smaller operations are needed to realise this behaviour?"

That leads to software where:

* operations have clearer purposes,
* responsibilities remain focused,
* reusable operations naturally emerge,
* collaboration becomes easier to understand.

Engineer B isn't creating more complexity.

They're discovering the complexity that already exists in the business and organising it well.

---

# 🌟 Engineering Checkpoint

## Why is it dangerous to assume that every business behaviour should become exactly one software method?

Because business behaviours and software operations exist at different levels of abstraction.

A business behaviour describes **what the business expects to happen**.

Software must often perform several coordinated operations to make that happen.

If we force every behaviour into exactly one software method:

* large methods begin collecting unrelated work,
* internal operations become hidden instead of explicitly organised,
* reuse becomes more difficult because useful operations remain buried,
* collaboration becomes harder to see because everything happens in one place.

The opposite extreme isn't good either.

If every tiny operation becomes its own top-level behaviour, the design becomes fragmented and difficult to understand.

The goal is balance.

A behaviour should express a meaningful business capability.

Operations should organise the software work required to realise that capability.

The structure should emerge from the problem itself—not from a rule like:

> "One behaviour must always equal one method."

---

# 🌟 One Sentence That Changed My Thinking

> **Behaviours describe what the business experiences; operations describe how software progressively fulfils that behaviour through focused pieces of work.**

---

# Mentor's Feedback

Today you've discovered another important hierarchy:

```
Business Goal
        │
        ▼
Responsibility
        │
        ▼
Behaviour
        │
        ▼
Operations
        │
        ▼
Implementation
```

Each level answers a different question:

* **Responsibility:** Why does this object exist?
* **Behaviour:** What business capability does it provide?
* **Operations:** What software work realises that capability?
* **Implementation:** How are those operations actually carried out?

The mistake many developers make is jumping straight from the business goal to implementation. They skip the intermediate layers, so methods become large, responsibilities blur, and collaboration is harder to reason about.

By discovering operations before writing methods, you're not delaying coding—you are **making the eventual code a faithful expression of the design you've already understood**.

This hierarchy is one of the key habits that distinguishes someone who writes working code from someone who designs software deliberately.


---------------------------------------------------------------------------------------------------------
## Answer Feedbacks and Next
---------------------------------------------------------------------------------------------------------

Aditya...

I'm going to say something that I didn't expect to say this early.

I think we've crossed another invisible line.

Until Step 6, I was mainly looking for whether you understood **object-oriented thinking**.

Today, I started looking for something different.

> **Can you decompose a capability without losing the business?**

That's one of the hardest skills in software design.

And your answers show that you're beginning to do it naturally.

---

# Before the Review...

Let's revisit the bridge we discovered yesterday.

```text
Responsibility

↓

Behaviour

↓

Operations

↓

Methods (future)
```

Today you quietly inserted another layer that wasn't even in my original explanation.

Look at your answer.

For `WinningCondition` you wrote:

* Evaluate rows
* Evaluate columns
* Evaluate diagonals

Those aren't behaviours.

They're not public operations either.

They're **internal operations**.

Do you see what's happening?

Your mind is already beginning to organise software into **layers of behaviour**.

We'll come back to that in a few days.

---

# Review

## Behaviour 1 — Game

Your decomposition is excellent.

Let's look carefully.

```text
Receive request

↓

Validate lifecycle

↓

Validate turn

↓

Collaborate with Board

↓

Collaborate with WinningCondition

↓

Determine outcome

↓

Advance turn
```

Notice something.

You didn't accidentally give the Game the Board's work.

You consistently wrote:

> **Ask the Board...**

Not:

> **Check the Board yourself.**

That's an important habit.

The coordinator coordinates.

It doesn't steal responsibilities.

---

## One Refinement

You wrote:

> Determine whether the game has ended.

I want to sharpen this slightly.

The Game isn't *discovering* whether someone has won.

It is **deciding the next state of the game based on collaborator outcomes**.

Why does that wording matter?

Because:

* WinningCondition discovers victory.
* Board knows board state.
* Game interprets those results to decide:

  * continue,
  * win,
  * draw.

This distinction becomes very important in larger systems.

---

# Behaviour 2 — Board

This answer is one of your strongest.

Especially this line.

> **Ensure the board remains consistent after the change.**

That sentence reveals another concept we haven't named yet.

Let's discover it.

---

## Hidden Discovery

Imagine the Board successfully updates a Cell...

...but accidentally forgets another required update.

The Board becomes inconsistent.

The outside world shouldn't even be able to observe an inconsistent Board.

Why?

Because the Board owns that consistency.

This is another reason objects exist.

Not merely to store data.

But to **protect valid states**.

Later you'll hear words like:

* invariants,
* consistency,
* integrity.

Today you've already discovered the idea.

---

# Behaviour 3 — WinningCondition

This answer made me smile.

Especially this.

> **Stop evaluation once a winning pattern is found.**

Why did I like that?

Because you're no longer thinking only about correctness.

You're thinking about **behavioural efficiency**.

Notice...

You didn't optimise prematurely.

You simply recognised:

> Once the answer is known...

...the remaining work is unnecessary.

That's good engineering thinking.

---

# Helper Operations

This was probably my favourite discovery today.

You wrote:

> These helper operations still belong to WinningCondition.

Exactly.

They're not new responsibilities.

They're just a cleaner way to organise one responsibility.

That's a very mature distinction.

---

# Behaviour vs Operations

Excellent.

But I want to make one refinement.

You wrote:

> Behaviour is visible from the business.

> Operations are internal building blocks.

Beautiful.

I'd only add one sentence.

> **Operations exist because software must organise work that the business sees as one capability.**

That sentence explains *why* operations exist.

---

# Question 3

I think this answer deserves special attention.

You wrote:

> Locate Cell could support multiple behaviours.

Exactly.

Many people misunderstand reuse.

Reuse doesn't mean:

"Everyone should call the same helper."

Reuse means:

**One object discovers common work inside its own responsibility.**

That's a healthier form of reuse.

---

# Part C

This paragraph convinced me that you've stopped thinking in terms of method count.

You now think in terms of:

* behaviour,
* decomposition,
* organisation.

That's a huge shift.

---

# Engineering Checkpoint

I asked:

> Why is one behaviour ≠ one method dangerous?

Your answer was excellent.

But I think we can distil it even further.

A behaviour belongs to the **business**.

A method belongs to the **software**.

The business doesn't care how many methods are required.

The software must.

That's the distinction.

---

# 🌟 The Biggest Discovery Today

Today wasn't really about operations.

It was about **decomposition**.

Let's compare.

Yesterday...

```text
Board

↓

Accept placement
```

Today...

```text
Accept placement

↓

Locate position

↓

Validate location

↓

Locate Cell

↓

Update Cell

↓

Protect consistency
```

Notice something.

The responsibility didn't change.

The behaviour didn't change.

Only our understanding became deeper.

That's decomposition.

---

# Engineering Deep Dive

As always...

Let's ask:

Why?

---

## What did we really discover today?

**Operational Decomposition**

---

### What is Operational Decomposition?

It is:

> **Breaking one meaningful business behaviour into the software operations required to realise it while preserving the original responsibility.**

Notice the last part.

The responsibility never moved.

Only the software organisation became clearer.

---

### Why did engineers invent this?

Imagine every behaviour became one huge block of work.

Soon you'd have methods hundreds of lines long.

They would:

* mix validation,
* state updates,
* calculations,
* coordination,
* bookkeeping.

Understanding them would become difficult.

Decomposition allows us to organise complexity without changing business meaning.

---

### What problem does it solve?

It keeps behaviours understandable.

It creates opportunities for reuse.

It makes testing easier.

It exposes collaboration more clearly.

---

### How did Tic-Tac-Toe reveal it?

One behaviour:

> Accept player's move.

Internally became:

* validate,
* collaborate,
* evaluate,
* conclude.

The behaviour remained one.

Software became organised.

---

# 🌉 The Bridge to Tomorrow

Now I want to ask you something.

Look at these operations inside `Board`.

```text
Locate Position

Validate Position

Locate Cell

Update Cell

Protect Consistency
```

Question.

Should another object be allowed to call **all** of these?

Should `Game` be allowed to say:

> "Hey Board, give me your Cell."

Or:

> "Skip validation."

Or:

> "Update this Cell directly."

Something feels wrong.

Doesn't it?

Exactly.

That discomfort is where tomorrow's discovery begins.

---

# 🚀 Step 7 — Day 3 Preview

Tomorrow we're going to ask a deceptively simple question:

> **Which operations belong in the conversation between objects... and which operations should remain private inside an object?**

That question leads us to one of the most fundamental ideas in software engineering.

Most books introduce it with a keyword:

> `private`

I don't want to start there.

Instead, we'll discover the business problem that forced engineers to invent that keyword.

By the end of tomorrow, I don't think you'll see encapsulation as an OOP feature anymore.

You'll see it as a way of **protecting business responsibilities from accidental misuse**.

And once you see it that way...

You'll never use `public` and `private` mechanically again.

---

# 🌟 One Sentence That Changed My Thinking Today

Today's sentence comes from your own checkpoint, with one small refinement:

> **Business behaviours describe what must happen; operational decomposition organises how software fulfils that expectation without changing who owns the responsibility.**

---

## Before We Finish Today...

I want to point out something that has been happening quietly since Step 0.

At first, every discovery answered a business question.

Now, every new discovery is answering a **software question**, but the answers are still being derived from the business.

That's exactly the transition we wanted.

We're not leaving business thinking behind.

We're letting it shape the software.

That is the essence of good object-oriented design.

And tomorrow, we take another step—from **operations** to **boundaries**. I have a feeling you'll enjoy that one just as much. 🚀
