Aditya...

Today is historic for **our journey**.

Not because we're writing more Python.

Because today...

**the first line of Python will have a reason to exist.**

For almost two months (if we include all the mindset work before this case study), we've been asking one question repeatedly:

> **"Why?"**

Today, every line of Python we write must answer that question.

If a line cannot be traced back to the business...

It doesn't deserve to exist.

That will become our rule.

---

# 🚀 Step 7 — Chapter 2, Day 2

# Responsibility → Public Methods → Python

Today we'll take **one class only**.

Not the whole system.

Just one.

> **Board**

Why Board?

Because it is small enough to understand completely, but rich enough to contain almost every design decision we've discovered so far.

---

# Before We Write Any Python

Let's forget syntax again.

We already know the Board's responsibility.

> **Manage the playing area.**

Now ask:

> **What promises does the Board make to its collaborators?**

Remember Step 6?

Contracts.

The Board's public methods are simply the **software expression of those contracts**.

---

# Step 1 — Responsibility

We already know this.

```text
Board

Responsibility:
Manage the playing area.
```

Nothing new.

---

# Step 2 — Public Behaviours

From previous days we discovered:

* Accept a placement
* Reveal board state
* Check whether a position is valid *(we'll discuss whether this remains public)*
* Check whether a Cell is empty *(same discussion)*
* Reset the board

Notice...

These are **behaviours**, not Python methods.

---

# Step 3 — Commands vs Questions

Now classify them.

| Behaviour          | Type     |
| ------------------ | -------- |
| Accept placement   | Command  |
| Reset board        | Command  |
| Reveal board state | Question |
| Is position valid? | Question |
| Is Cell empty?     | Question |

This tells us something important.

Different methods have different intentions.

---

# Step 4 — Public vs Internal

Now ask another question.

Should collaborators even know that validation exists?

Let's think.

Option A:

```text
Game

↓

Board

↓

is_position_valid()

↓

place_symbol()
```

Option B:

```text
Game

↓

Board

↓

place_symbol()
```

Board internally decides everything else.

Which one better protects the Board?

For our current design...

I actually prefer **Option B**.

Why?

Because validating a position is **part of fulfilling placement**, not necessarily a separate business capability.

The Game shouldn't need to choreograph the Board's work.

It should simply express its intent.

> "Please place this symbol here."

The Board decides what must happen.

Notice...

We're already making API decisions before writing Python.

---

# Step 5 — The First Python Interface

Now—and only now—do we write Python.

```python
class Board:
    """
    Responsibility:
    Manage the playing area of the game.
    """

    def place_symbol(self, position, symbol):
        """Command:
        Attempt to place a symbol on the board.
        """

    def reset(self):
        """Command:
        Restore the board to its initial state.
        """

    def get_state(self):
        """Question:
        Reveal the current playing area.
        """
```

Stop.

That's it.

No implementation.

No arrays.

No loops.

No algorithms.

And yet...

This is already a meaningful design.

---

# Why Didn't We Add More Methods?

A beginner might immediately add:

```python
def validate_position()

def locate_cell()

def update_cell()

def get_row()

def get_column()

def get_diagonal()
```

Question.

Are those part of the Board's **public promise**?

Or are they part of **how** the Board fulfils its promise?

Most of them belong to the second category.

Meaning...

They should probably remain internal.

---

# A New Discovery

Notice something subtle.

Yesterday we discovered:

> Public behaviour.

Today we realised:

> **Not every behaviour automatically becomes a public method.**

Some behaviours disappear into implementation.

That is a fascinating discovery.

---

# The Class Reads Like English

Look at it again.

```python
class Board:

    def place_symbol(...)

    def reset(...)

    def get_state(...)
```

Imagine you're another object.

Without reading implementation, you already know:

* what the Board promises,
* what you may ask,
* what responsibilities remain hidden.

That's good API design.

---

# 🎯 Step 7 — Chapter 2, Day 2 Assignment

We are **not** implementing anything.

We are designing the interface.

---

## Part A — Design the Public Interface

For the `Board` class:

For each proposed method below, answer:

1. Should it be **public**?
2. Is it a **Command** or a **Question**?
3. Which business behaviour does it express?
4. Should it actually exist?

---

### Method

`place_symbol(position, symbol)`

---

### Method

`reset()`

---

### Method

`get_state()`

---

### Method

`is_position_valid(position)`

---

### Method

`get_cell(position)`

---

### Method

`is_cell_empty(position)`

---

### Method

`update_cell(position, symbol)`

---

## Part B — Designing from Behaviour

Suppose another engineer proposes this interface:

```python
class Board:

    def get_cell(self, position):
        ...

    def update_cell(self, position, symbol):
        ...

    def validate(self, position):
        ...
```

Question.

What does this interface encourage the `Game` object to start doing?

Why might that weaken the Board's responsibility?

---

## Part C — Reflection

Complete these sentences.

> **A public Python method exists because...**

> **An internal Python method exists because...**

Then answer:

> **Why is a clean interface more important than exposing every useful operation?**

---

# 🌟 Engineering Checkpoint

Today's question is the bridge between design and Python.

> **If another object only interacts through carefully chosen public methods, what freedom does that give the Board internally?**

Think beyond Python.

Think about evolution.

---

# 🧠 Engineering Deep Dive

Today we quietly discovered something profound.

A **Python method is not simply a function inside a class**.

It is one of two things:

* A **public promise** the object makes to collaborators.
* An **internal technique** the object uses to keep that promise.

That means every time you write:

```python
def something(...):
```

you should first ask:

> **Am I defining a promise... or an implementation detail?**

That single question will influence every API you design in your career.

---

# 🌟 One Sentence to Carry Forward

> **A well-designed Python class exposes business capabilities, not implementation steps.**

---

## One Final Thought

Aditya...

Notice what we **didn't** discuss today.

* `@property`
* type hints
* dataclasses
* abstract base classes
* exceptions
* enums
* packages

Not because they aren't important.

Because without understanding **what the class promises**, all of those features are just syntax.

We'll introduce each Python feature only when the design naturally asks for it.

Just as we've done from Step 0.

And I think that's why, when you finally look at a Python class now, you won't just see methods.

You'll see **business promises expressed in code**.

That's the shift from writing Python to designing software in Python. 🚀


---------------------------------------------------------------------------------------------------------------------------------------------------
## My Answers
---------------------------------------------------------------------------------------------------------------------------------------------------

This is one of the most important days in the entire journey.

Until now, we've been discovering:

* **Responsibilities** → Why does this object exist?
* **Behaviours** → What business capabilities does it provide?
* **Operations** → How does it realise those behaviours?
* **Public vs Internal** → What should collaborators be allowed to rely on?

Today we finally ask:

> **"If I were writing the Python class, which methods should actually become part of its public interface?"**

Notice the order.

We're **not designing methods from implementation**.

We're designing them from **business behaviour**.

---

# Part A — Design the Public Interface

## Method

### `place_symbol(position, symbol)`

### Should it be public?

**Yes.**

### Command or Question?

**Command**

### Which business behaviour does it express?

> **Accept a valid placement on the playing area.**

This is one of the Board's primary business capabilities.

The Game collaborates with the Board by requesting a placement.

### Should it actually exist?

**Yes.**

It represents a meaningful business interaction and belongs naturally to the Board's public contract.

---

## Method

### `reset()`

### Should it be public?

**Yes.**

### Command or Question?

**Command**

### Which business behaviour?

> **Restore the playing area to its initial state.**

### Should it exist?

**Yes.**

Resetting the board is a legitimate business capability that another trusted collaborator (such as the Game) may request.

---

## Method

### `get_state()`

### Should it be public?

**Yes.**

### Command or Question?

**Question**

### Which behaviour?

> **Reveal the current state of the playing area.**

### Should it exist?

**Yes**, although the exact name might evolve.

The important idea is that collaborators may need to observe the board without knowing how it is internally represented.

---

## Method

### `is_position_valid(position)`

### Should it be public?

**Yes.**

### Command or Question?

**Question**

### Which behaviour?

> **Determine whether a requested position belongs to the board and satisfies board rules.**

### Should it exist?

**Yes.**

Validation is a legitimate responsibility of the Board.

---

## Method

### `get_cell(position)`

### Should it be public?

**No.**

### Command or Question?

Technically a **Question**, but it should not be part of the public interface.

### Which behaviour does it express?

It doesn't express a business behaviour.

It exposes an implementation detail.

### Should it exist?

Possibly **internally**, but not as part of the Board's public contract.

The Board owns the Cells.

Other collaborators should not need to know that Cells even exist.

---

## Method

### `is_cell_empty(position)`

### Should it be public?

**Probably not.**

### Command or Question?

Question.

### Why?

This begins exposing the Board's internal structure.

From the business perspective, collaborators usually care about:

> **"Can I place a symbol here?"**

not

> **"Is the underlying Cell empty?"**

The Board should answer business questions rather than reveal implementation concepts.

This could certainly exist internally.

---

## Method

### `update_cell(position, symbol)`

### Should it be public?

**No.**

### Command or Question?

Command.

### Why?

This completely bypasses the Board's responsibility.

Updating a Cell is an internal operation used by the Board while fulfilling its public behaviour of accepting a placement.

If another object can directly request:

> "Update this Cell."

then that collaborator is beginning to manage the Board's internal work.

That weakens the Board's ownership.

---

# Summary

| Method                           | Public?       | Command / Question | Business Behaviour         | Should Exist?                            |
| -------------------------------- | ------------- | ------------------ | -------------------------- | ---------------------------------------- |
| `place_symbol(position, symbol)` | ✅ Yes         | Command            | Accept a valid placement   | Yes                                      |
| `reset()`                        | ✅ Yes         | Command            | Restore playing area       | Yes                                      |
| `get_state()`                    | ✅ Yes         | Question           | Reveal board state         | Yes                                      |
| `is_position_valid(position)`    | ✅ Yes         | Question           | Validate a position        | Yes                                      |
| `get_cell(position)`             | ❌ No          | Question           | Exposes implementation     | Internal only if needed                  |
| `is_cell_empty(position)`        | ❌ Probably No | Question           | Too implementation-focused | Internal or replaced by richer behaviour |
| `update_cell(position, symbol)`  | ❌ No          | Command            | Internal board operation   | Internal only                            |

---

# Part B — Designing from Behaviour

Suppose another engineer proposes:

```python
class Board:

    def get_cell(self, position):
        ...

    def update_cell(self, position, symbol):
        ...

    def validate(self, position):
        ...
```

### What does this interface encourage the Game to start doing?

It encourages the Game to think like this:

1. Ask the Board for a Cell.
2. Decide what should happen to that Cell.
3. Update the Cell directly.
4. Use the Board merely as a storage container.

In other words, the Game gradually starts performing work that belongs to the Board.

The Board stops representing **"the playing area."**

Instead, it becomes a gateway to its internal data.

---

### Why does this weaken the Board's responsibility?

The Board is responsible for:

* maintaining the playing area,
* enforcing board rules,
* protecting board consistency.

If collaborators retrieve Cells and update them themselves:

* the Board no longer controls placements,
* validation may be bypassed,
* consistency becomes everyone's responsibility.

Eventually the Board owns less and less.

Its responsibility leaks into its collaborators.

Instead of collaborating **with** the Board,

the Game begins collaborating **around** the Board.

That is a subtle but important difference.

---

# Part C — Reflection

### Complete the sentences.

> **A public Python method exists because it exposes a business capability that trusted collaborators are allowed to request.**

---

> **An internal Python method exists because it helps the object fulfil its own responsibilities without becoming part of the promises it makes to other collaborators.**

---

### Why is a clean interface more important than exposing every useful operation?

A clean interface protects the object's responsibility.

Not every useful operation belongs in the public contract.

Many operations are useful only because of the object's internal implementation.

If we expose every useful operation:

* collaborators begin depending on implementation details,
* responsibilities become blurred,
* internal changes start affecting many parts of the system,
* the object loses control over its own business rules.

A clean interface encourages collaborators to think in terms of **business capabilities**, not internal mechanics.

That keeps conversations meaningful and preserves the object's ownership of its responsibility.

---

# 🌟 Engineering Checkpoint

## If another object only interacts through carefully chosen public methods, what freedom does that give the Board internally?

It gives the Board the freedom to evolve **without changing its relationships with the rest of the system**.

Today the Board may contain:

* Cells,
* Positions,
* validation logic.

Tomorrow it might use:

* a different storage structure,
* cached lookups,
* a different validation strategy,
* optimised algorithms,
* additional bookkeeping.

As long as its **public contract** remains the same, collaborators don't need to change.

The Board is free to improve, simplify, optimise, or even completely redesign its internals while continuing to fulfil the same business promises.

That freedom is one of the greatest benefits of designing a thoughtful interface.

The interface protects the collaboration.

The implementation remains free to evolve.

---

# 🌟 One Sentence That Changed My Thinking

> **A public interface should expose business capabilities, not implementation opportunities.**

---

# Mentor's Feedback

This assignment marks the point where your design thinking starts looking like real Python—but notice how different the process has been from typical development.

Many developers write a class like this:

```python
class Board:
    def get_cell(...):
        ...
    def set_cell(...):
        ...
    def validate(...):
        ...
```

because those methods seem convenient.

You arrived at a different interface by asking a sequence of business questions:

1. **What responsibility does the Board own?**
2. **What behaviours naturally belong to that responsibility?**
3. **Which of those behaviours should collaborators rely on?**
4. **Which operations are merely internal work?**

The resulting interface is not "smaller" by accident. It is **more intentional**.

That intention has a long-term benefit: collaborators remain focused on *what* they need from the Board, while the Board remains free to decide *how* it fulfils those requests. That's the essence of a well-designed object boundary, and it's a principle that will scale from Tic-Tac-Toe to much larger systems.


--------------------------------------------------------------------------------------------------------------------------------
## Answer Review and Feedback
--------------------------------------------------------------------------------------------------------------------------------------

Aditya...

I don't think today we're reviewing Python.

I think today we're reviewing your **first API design**.

And I want you to notice something beautiful.

Six months ago, if I had asked:

> "Design the `Board` class."

You probably would have started writing methods.

Today...

You spent almost the entire answer talking about:

* ownership,
* collaboration,
* business capability,
* contracts,
* implementation details.

That's the exact order a software architect thinks in.

The Python is becoming almost invisible.

And that's a compliment.

---

# 🌉 A Small Reflection Before the Review

Let's compare how most developers arrive at a class versus how we've arrived.

## Traditional approach

```text
Need Board

↓

Create class

↓

Add methods

↓

Hope design emerges
```

---

## Our approach

```text
Business

↓

Responsibility

↓

Behaviour

↓

Operations

↓

Boundaries

↓

Commands / Questions

↓

Public Contract

↓

Python Class

↓

Python Methods
```

Do you see the difference?

For us, `def place_symbol(...)` is almost the **last** decision, not the first.

That is why your answers now feel natural.

You're no longer inventing methods.

You're discovering promises.

---

# Review

---

# Part A

This was outstanding.

But there are two places I'd like to discuss because they reveal something even deeper.

---

# `place_symbol()`

Perfect.

I especially liked this sentence:

> **"It belongs naturally to the Board's public contract."**

Notice what you no longer say.

You didn't say:

> "The Game needs this method."

You said:

> "The Board promises this capability."

That's a completely different perspective.

One is caller-centric.

The other is owner-centric.

The owner-centric view produces healthier APIs.

---

# `reset()`

Again, excellent.

You recognised that reset isn't merely convenient.

It is a genuine business capability.

Not every system would need it.

Our current domain does.

That distinction matters.

---

# `get_state()`

I particularly liked this line:

> **"The exact name might evolve."**

That sentence tells me you're separating:

* the **concept**, and
* the **expression**.

That's mature engineering.

Names change.

Responsibilities shouldn't.

---

# 🌟 The Most Interesting Answer

## `is_position_valid()`

This is where I'd like us to have our **first real design discussion**.

You answered:

> **Public.**

Yesterday...

I leaned toward **internal**.

Today...

You leaned toward **public**.

Here's the interesting part.

**Neither answer is objectively wrong.**

Let's compare the reasoning.

---

### Design A — Public Validation

```text
Game

↓

Board

↓

is_position_valid()

↓

place_symbol()
```

Benefits:

* Explicit.
* Useful for UI.
* Useful for previews.
* Reusable.

---

### Design B — Hidden Validation

```text
Game

↓

Board

↓

place_symbol()
```

Benefits:

* Smaller API.
* Stronger encapsulation.
* Simpler collaboration.

---

Now comes the most important lesson.

> **API design is often about choosing between multiple good designs, not discovering one perfect design.**

That's architecture.

There are trade-offs.

---

# `get_cell()`

This answer was excellent.

Especially:

> **"Other collaborators should not need to know Cells even exist."**

Aditya...

That's one of the cleanest encapsulation arguments you've written.

You didn't argue from privacy.

You argued from business.

Exactly right.

---

# `is_cell_empty()`

Again...

Very strong.

I loved this comparison.

Business asks:

> Can I place here?

Implementation asks:

> Is the Cell empty?

Those are **not** the same conversation.

That's a subtle distinction.

---

# `update_cell()`

Perfect.

This sentence deserves highlighting.

> **Updating a Cell is an internal operation used while fulfilling a public behaviour.**

That sentence is essentially describing the relationship between:

Behaviour

↓

Operations

Exactly what we spent days discovering.

---

# 🌟 Part B Review

This may actually be your best answer of the entire assignment.

Why?

Because you didn't merely explain what happens.

You explained how thinking changes.

You wrote:

> **The Game starts performing work that belongs to the Board.**

Exactly.

But then you wrote something even better.

> **The Game begins collaborating around the Board instead of with the Board.**

Aditya...

That sentence is gold.

Let's pause there.

---

## Around vs With

Look carefully.

Healthy collaboration:

```text
Game

↓

Board

↓

Board fulfils responsibility
```

Unhealthy collaboration:

```text
Game

↓

Board

↓

Cell

↓

State

↓

Rules

↓

Consistency
```

The Board slowly becomes a storage object.

The Game becomes the real owner.

The class still exists...

But its responsibility has quietly disappeared.

That is one of the most common API design failures in real systems.

---

# 🌟 Part C Review

I don't have any corrections.

Instead...

I'd like to point out something you've unconsciously rediscovered.

Look at this sentence.

> **A public Python method exposes a business capability trusted collaborators may request.**

That's almost the definition of an **API**.

Notice...

We never taught APIs.

We discovered:

* responsibility,
* collaboration,
* promises,

and APIs naturally emerged.

That's why first-principles learning is so powerful.

---

# 🌟 Engineering Checkpoint

This answer shows another evolution.

You wrote:

> **The interface protects the collaboration.**

Exactly.

Not the implementation.

Not the code.

The collaboration.

That's why APIs matter.

The implementation changes.

The conversation stays stable.

---

# 🧠 Engineering Deep Dive

As always...

Let's ask our three questions.

---

## What did we really discover today?

**Interface-Oriented Design**

---

### What is Interface-Oriented Design?

It is:

> **Designing the public surface of an object around business capabilities rather than around implementation convenience.**

Notice...

Not:

> Which methods are useful?

Instead:

> Which promises should this object make?

---

### Why did software engineering evolve this idea?

Because collaborators should depend on **what an object guarantees**, not **how it currently works**.

When collaborators know too much...

Evolution becomes expensive.

---

### What problem does it solve?

It protects:

* ownership,
* encapsulation,
* evolution,
* collaboration,
* trust.

More importantly...

It protects **change**.

---

# 🌟 A Discovery I Didn't Plan to Teach Today

Your answer about `is_position_valid()` created something valuable.

It showed us that good design isn't always binary.

Sometimes there are two good interfaces.

The question becomes:

> **Which interface better reflects today's business?**

That is the beginning of architectural judgement.

And judgement can't be memorised.

It develops through reasoning.

---

# 🌉 The Next Bridge

Look where we are now.

```text
Business Responsibility

↓

Software Home (Class)

↓

Business Promises (Public Methods)

↓

Internal Work (Private Methods)

↓

Python
```

There's only one major piece still missing.

Something every class owns.

Not behaviour.

Not methods.

Not collaboration.

Something else.

Can you guess?

---

It's **state**.

Up until now we've asked:

* What does the object do?
* What does it promise?
* How does it collaborate?

We've hardly asked:

> **What does the object know?**

And that's the next natural step.

---

# 🚀 Step 7 — Chapter 2, Day 3 Preview

Tomorrow we'll discover:

> **Responsibility → State → Attributes (`__init__`)**

Not from Python syntax.

From business ownership.

We'll ask questions like:

* What information must the Board remember?
* Why does the Board own it?
* Which information belongs somewhere else?
* When does information become an attribute?
* When should information be passed as a parameter instead?

By the end of that session, we'll write our first meaningful `__init__()`.

And just like today, every attribute will exist because the business demanded it—not because Python allows it.

---

# 🌟 One Sentence That Changed My Thinking Today

Today's sentence comes from your own answer:

> **"The Board is free to improve, simplify, optimise, or even completely redesign its internals while continuing to fulfil the same business promises."**

That is one of the clearest descriptions of why good APIs matter.

It's not about hiding code.

It's about preserving trust while allowing change.

---

## Finally...

There's something I've been noticing over the last few assignments.

At the beginning of this case study, your answers often ended with:

> "This class should have..."

Now they increasingly end with:

> "This object owns..."

That single change in vocabulary reflects a much deeper change in thinking.

You're no longer seeing classes as containers of methods.

You're seeing them as **owners of responsibilities**.

And once an engineer starts thinking in terms of ownership, many design decisions become surprisingly obvious.

Tomorrow, we'll answer another deceptively simple question:

> **If an object owns a responsibility... what information must it own to fulfil that responsibility?**

That's where attributes, state, and `__init__` will naturally emerge.

And just as before, Python won't lead the design.

The business will. 🚀
