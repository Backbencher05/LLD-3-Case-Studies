Aditya...

Today we're going to answer a question that many books introduce with words like:

* Composition
* Aggregation
* Association
* Dependency

We're **not** going to start there.

Because those are names.

First, let's discover the problem those names were invented to solve.

---

# 🚀 Step 7 — Chapter 2, Day 4

# Responsibility → Relationships → Object References

Today's question is beautifully simple.

> **When should one object remember another object?**

Not:

> "How do I create objects?"

Not:

> "How do I pass objects?"

Just:

> **Why should an object know another object exists?**

---

# Let's Leave Software Again

Imagine you're the manager of a restaurant.

Question:

Should you know your chefs?

Of course.

Without chefs, you can't run the restaurant.

---

Should you know every customer who has ever visited?

Probably not.

Customers come.

Customers leave.

Your responsibility doesn't require permanently remembering all of them.

---

Should you know today's reservations?

Yes.

Because today's service depends on them.

---

Notice something.

We're asking exactly the same question as yesterday.

Yesterday:

> **What information should I remember?**

Today:

> **Which business participants should I remember?**

Object references are simply another form of state.

---

# Back to Tic-Tac-Toe

Let's start with the easiest relationship.

---

## Question 1

Should the **Game** remember the **Board**?

Imagine a Game without a Board.

Can it coordinate a match?

No.

The Game's responsibility depends on having a playing area.

Therefore:

The Board becomes part of the Game's long-term state.

---

Business reasoning:

> The Game owns one Board because its responsibility cannot be fulfilled without one.

Notice...

We didn't mention Python.

---

## Question 2

Should the **Board** remember its **Cells**?

Again.

Can the Board manage the playing area without remembering the playing area?

No.

Therefore:

The Board permanently owns its Cells.

Again...

Business first.

---

## Question 3

Should a **Cell** remember its **Board**?

Interesting.

Ask:

Does a Cell need to know the Board in order to manage its own state?

Usually...

No.

A Cell only needs to know:

* whether it's empty,
* which symbol it contains.

Its responsibility does not require knowing who owns it.

So...

No reference.

---

## Question 4

Should the **Board** remember the **Game**?

Think carefully.

The Board manages the playing area.

Does it need to know:

* whose turn,
* winner,
* game status?

No.

Those belong elsewhere.

The Board serves the Game.

It doesn't coordinate it.

Therefore:

No reference.

---

Look at what just happened.

We didn't draw arrows.

We asked:

> **Does my responsibility require knowing this other object?**

That single question answers most relationship problems.

---

# The Hidden Principle

An object should remember another object only when:

> **Its own responsibility depends on collaborating with that object over time.**

Notice the phrase:

> **Over time.**

Temporary collaboration is different.

---

# Temporary Collaboration

Suppose the Board receives:

```python
place_symbol(position, symbol)
```

Does the Board permanently remember:

* `position`?

No.

It only needs it for this interaction.

That's a parameter.

Not a relationship.

---

Suppose the Board receives:

```python
reset()
```

Does it receive Cells?

No.

Because it already owns them.

Permanent relationship.

---

# Permanent vs Temporary

Let's compare.

---

Permanent:

```text
Game

↓

Board
```

The Game owns the Board throughout its lifetime.

---

Temporary:

```text
Game

↓

Position
```

Position exists only while placing a move.

Afterwards...

Gone.

---

Same collaboration.

Different lifetime.

---

# The First Python Expression

Now we can finally extend our class.

```python
class Game:

    def __init__(self, board):
        self._board = board
```

Question.

Why is `board` now an attribute?

Answer:

Because the Game permanently depends on the Board to fulfil its responsibility.

---

Board.

```python
class Board:

    def __init__(self, size, cells):
        self._size = size
        self._cells = cells
```

Again...

Why?

Not because Python needs it.

Because the Board permanently owns the playing area.

---

Cell.

```python
class Cell:

    def __init__(self):
        self._symbol = None
```

Notice something missing.

```python
self.board
```

Why?

Because the Cell doesn't need to know.

---

# A Beautiful Rule

Yesterday:

> Attributes represent owned business knowledge.

Today:

> **References represent long-term business relationships.**

Both are state.

One stores facts.

The other stores collaborators.

---

# The Growing Discovery Map

```text
Business Responsibility

↓

Business Behaviour

↓

Business State

↓

Business Relationships   ← Today

↓

Python Object References
```

Again...

Python is expressing a business decision.

---

# 🎯 Step 7 — Chapter 2, Day 4 Assignment

## Part A — Should This Object Remember That Object?

For each pair answer:

1. Should it be a permanent relationship?
2. Why?
3. If not, should it be temporary or not exist at all?

---

### Game → Board

---

### Board → Cell

---

### Cell → Board

---

### Game → Player

---

### Player → Game

---

### Game → WinningCondition

---

### WinningCondition → Board

---

### Board → WinningCondition

---

## Part B — Attribute, Parameter, or Neither?

For each collaboration decide whether the object should receive it as:

* **Attribute (long-term relationship)**
* **Parameter (temporary collaboration)**
* **Neither**

---

### Position

---

### Board

---

### Cell

---

### WinningCondition

---

### Move

---

### Player

---

Explain every answer using **lifetime of the relationship**, not Python syntax.

---

## Part C — Reflection

Complete these sentences.

> **An object remembers another object because...**

> **A relationship becomes an attribute when...**

Then answer:

> **Why is a temporary collaborator different from a permanent collaborator?**

---

# 🌟 Engineering Checkpoint

Think about this situation.

Both the `Game` and every `Cell` permanently store references to each other.

Question:

> **How might that affect coupling, ownership, and future evolution of the system?**

Don't answer in terms of memory.

Think about collaboration.

Freedom to change.

Boundaries.

---

# 🧠 Engineering Deep Dive

Today we've discovered another fundamental principle.

A reference is **not** merely a pointer.

It is:

> **A declaration that "my responsibility depends on collaborating with this object throughout my lifetime."**

That's why:

* `Game` owns `Board`.
* `Board` owns `Cells`.
* `Cell` does **not** own `Board`.

Ownership and responsibility determine relationships.

Not convenience.

---

# 🌟 One Sentence to Carry Forward

> **An object should remember another object only when their collaboration is part of its long-term responsibility; everything else should arrive only when needed.**

---

# A Tiny Preview...

Tomorrow, we'll finally have all the ingredients.

We'll have discovered:

* Classes
* Methods
* Attributes
* Relationships

The next step is simply asking:

> **How do we assemble them into one coherent Python model?**

Not by coding from scratch.

But by expressing everything we've already uncovered.

And I think you'll find something surprising.

By the time we write the code...

There won't be many design decisions left.

Because we've already made them—all in the language of the business. 🚀


-------------------------------------------------------------------------------------------------------------------------------------------
## My Answers
-------------------------------------------------------------------------------------------------------------------------------------------

This is another subtle but extremely important discovery.

So far we've asked:

* **What should an object remember?** (attributes)
* **What should an object do?** (behaviour)
* **What should it expose?** (interface)

Today we combine those ideas and ask:

> **"Which relationships deserve to last for the object's lifetime?"**

This is not really about references.

It's about **business ownership over time**.

A permanent relationship says:

> **"I cannot meaningfully fulfil my responsibility without this collaborator."**

A temporary collaboration says:

> **"I only need this collaborator for this particular business event."**

---

# Part A — Should This Object Remember That Object?

## 1. Game → Board

### Should it be a permanent relationship?

**Yes.**

### Why?

A Game is played on a Board.

Throughout the lifetime of the Game, it coordinates gameplay using the same playing area.

The Board is part of the Game's identity.

Without a Board, there is no game to manage.

**Decision:** Permanent relationship (attribute).

---

## 2. Board → Cell

### Should it be a permanent relationship?

**Yes.**

### Why?

The Cells collectively make up the playing area.

The Board cannot represent or manage the playing area without remembering the elements that compose it (or an equivalent internal representation).

Today that representation is Cells.

Tomorrow it could change internally, but the Board will still permanently own whatever represents its playing area.

**Decision:** Permanent relationship.

---

## 3. Cell → Board

### Should it be a permanent relationship?

**No.**

### Why?

The Cell's responsibility is to manage **its own state**.

It doesn't need to know who owns it in order to fulfil that responsibility.

Giving every Cell knowledge of the Board creates unnecessary coupling.

The Board owns the Cell.

The Cell doesn't need to own the Board.

**Decision:** No relationship.

---

## 4. Game → Player

### Should it be a permanent relationship?

**Yes.**

### Why?

The participating Players are fundamental to a Game.

The Game coordinates their turns and determines the outcome of their actions.

Without Players, the Game cannot fulfil its responsibility.

**Decision:** Permanent relationship.

---

## 5. Player → Game

### Should it be a permanent relationship?

**Generally, no.**

### Why?

A Player represents someone capable of participating in games.

The Player doesn't need to permanently remember one specific Game to express moves or make decisions.

Instead, the Game coordinates participation.

Keeping the relationship one-way reduces unnecessary coupling.

**Decision:** Usually no permanent relationship.

---

## 6. Game → WinningCondition

### Should it be a permanent relationship?

**Yes.**

### Why?

Throughout a Game, the same winning rule is used to evaluate progress.

The Game repeatedly collaborates with the WinningCondition after moves.

This makes it part of the Game's long-term collaboration.

**Decision:** Permanent relationship.

---

## 7. WinningCondition → Board

### Should it be a permanent relationship?

**No.**

### Why?

The WinningCondition doesn't permanently own a Board.

It simply evaluates whichever Board the Game asks it to evaluate.

The Board is supplied for a particular business event.

**Decision:** Temporary collaboration (parameter).

---

## 8. Board → WinningCondition

### Should it be a permanent relationship?

**No.**

### Why?

The Board represents the playing area.

It doesn't decide what constitutes a win.

Those rules belong elsewhere.

The Board should remain independent of how victory is determined.

**Decision:** No relationship.

---

# Summary

| Relationship             | Permanent?   | Reason                                   |
| ------------------------ | ------------ | ---------------------------------------- |
| Game → Board             | ✅ Yes        | Board is part of the Game's lifetime.    |
| Board → Cell             | ✅ Yes        | Cells form the playing area.             |
| Cell → Board             | ❌ No         | Cell doesn't need to know its owner.     |
| Game → Player            | ✅ Yes        | Players participate throughout the Game. |
| Player → Game            | ❌ Usually No | Player shouldn't depend on one Game.     |
| Game → WinningCondition  | ✅ Yes        | Uses the same rule throughout the Game.  |
| WinningCondition → Board | ⚠️ Temporary | Needs Board only during evaluation.      |
| Board → WinningCondition | ❌ No         | Board shouldn't know winning rules.      |

---

# Part B — Attribute, Parameter, or Neither?

The key question is:

> **"Does this relationship last for the object's lifetime, or only for a particular interaction?"**

---

## Position

### Decision

**Parameter**

### Why?

A Position is relevant to one move.

The Game and Board don't permanently remember one Position.

Each interaction may involve a different one.

---

## Board

### Decision

**Attribute (for Game)**

### Why?

The Game is played on a Board throughout its lifetime.

This is a long-term collaboration.

---

## Cell

### Decision

**Attribute (for Board)**

### Why?

The Board continually manages its playing area through its Cells (or equivalent representation).

The relationship exists for as long as the Board exists.

---

## WinningCondition

### Decision

**Attribute (for Game)**

### Why?

The Game repeatedly relies on the same winning rule during its lifetime.

This is an ongoing collaboration rather than a one-off interaction.

---

## Move

### Decision

**Parameter**

### Why?

A Move represents one business event.

It is supplied when that event occurs.

Unless we later introduce a dedicated move history, it doesn't become a permanent relationship.

---

## Player

### Decision

**Attribute (for Game)**

### Why?

Players participate for the duration of the Game.

The Game coordinates them throughout the match.

---

# Summary

| Object           | Attribute / Parameter / Neither | Why                            |
| ---------------- | ------------------------------- | ------------------------------ |
| Position         | Parameter                       | Specific to one interaction.   |
| Board            | Attribute (for Game)            | Long-term collaborator.        |
| Cell             | Attribute (for Board)           | Long-term part of the Board.   |
| WinningCondition | Attribute (for Game)            | Reused throughout the Game.    |
| Move             | Parameter                       | Represents one business event. |
| Player           | Attribute (for Game)            | Exists throughout the Game.    |

---

# Part C — Reflection

### Complete the sentences.

> **An object remembers another object because their collaboration is fundamental to fulfilling its responsibility over the object's lifetime.**

---

> **A relationship becomes an attribute when the collaborator is needed repeatedly as part of the object's ongoing business responsibility, rather than for a single business event.**

---

### Why is a temporary collaborator different from a permanent collaborator?

A permanent collaborator becomes part of an object's long-term business context.

The object expects to work with it repeatedly while fulfilling its responsibility.

A temporary collaborator is needed only to complete a particular business interaction.

Once that interaction ends, the relationship ends as well.

This distinction keeps relationships meaningful.

Objects don't collect references simply because they occasionally collaborate.

They remember only those collaborators that are essential to their ongoing responsibility.

---

# 🌟 Engineering Checkpoint

## Both the Game and every Cell permanently store references to each other. How might that affect coupling, ownership, and future evolution?

This creates unnecessary two-way knowledge between objects that shouldn't need to understand each other's roles.

### Coupling

The `Game` now knows about individual `Cell`s, and every `Cell` knows about the `Game`.

A change in one side is more likely to affect the other because they are directly connected instead of collaborating through the `Board`.

### Ownership

The `Board` is supposed to own the playing area.

If the `Game` starts interacting directly with `Cell`s, the Board's responsibility becomes weaker.

Likewise, if a `Cell` knows about the `Game`, it becomes aware of concerns outside its own responsibility, such as gameplay or lifecycle.

Ownership boundaries begin to blur.

### Future evolution

Imagine changing the Board so it no longer uses `Cell` objects internally.

If the `Game` depends on `Cell`s, that internal change now forces changes in the `Game`.

Or imagine reusing a `Cell` concept in another type of board.

If every `Cell` permanently expects a `Game`, reuse becomes much harder because the `Cell` is tied to a specific context.

By keeping relationships only where they are justified by long-term business responsibilities, we preserve each object's freedom to evolve independently while maintaining clear collaboration paths.

---

# 🌟 One Sentence That Changed My Thinking

> **A relationship should live only as long as the business responsibility that requires it—no longer, and no shorter.**

---

# Mentor's Feedback

Today you've discovered that relationships have **lifetimes**, just like responsibilities and behaviours.

A useful mental model is:

```text
Business Responsibility
        │
        ▼
Long-term collaborators  ───► Attributes
        │
        ▼
Temporary collaborators ───► Parameters
        │
        ▼
No meaningful collaboration ─► No relationship
```

The important insight is that collaboration alone does **not** justify a permanent relationship.

For example:

* The `Game` collaborates with the `WinningCondition` repeatedly throughout the match, so a long-term relationship makes sense.
* The `WinningCondition` collaborates with a `Board` only when asked to evaluate one. It doesn't *own* or *remember* the Board after that interaction.

As systems grow, this way of thinking keeps object graphs from becoming tangled. Instead of every object remembering every other object it has ever interacted with, each object remembers only the collaborators that are part of its enduring business responsibility. That preserves clear ownership, reduces unnecessary coupling, and gives each part of the design more freedom to evolve independently.


--------------------------------------------------------------------------------------------------------------------------
## Answers Feedback and Next
--------------------------------------------------------------------------------------------------------------------------

Aditya...

I'm going to say something that I don't say lightly.

I think you've crossed the line from **learning object-oriented programming** to **thinking like an object-oriented designer**.

Notice I didn't say "expert."

There's still a lot ahead—polymorphism, strategies, factories, persistence, concurrency, distributed systems...

But the *foundation* has changed.

When I read your answers now, I'm no longer looking for whether you know Python.

I'm looking for whether your design decisions are justified.

And they are.

---

# 🌉 Let's Look at the Journey

Look where we started.

## Step 0

> What are we even building?

---

## Step 2

> What does the business need?

---

## Step 3

> What exists in the business?

---

## Step 4

> How are they related?

---

## Step 5

> Who owns what responsibility?

---

## Step 6

> How do they collaborate?

---

## Step 7 Chapter 1

> How do responsibilities become behaviours?

---

## Step 7 Chapter 2

> How do those discoveries become Python?

Look at that progression.

Nothing was arbitrary.

Every step answered one question that the next step depended on.

---

# 🌟 The Biggest Thing I Saw

Every answer in this assignment revolved around one word.

**Lifetime.**

Not Python lifetime.

Business lifetime.

You repeatedly asked:

> **"Will this collaboration exist for the duration of the object's responsibility?"**

That is exactly the right question.

---

# Part A Review

---

## Game → Board

Excellent.

But I want to expand one sentence.

You wrote:

> **"The Board is part of the Game's identity."**

That sentence deserves attention.

There are two kinds of collaborators.

### Essential collaborators

Without them...

The object cannot fulfil its responsibility.

Example:

```text
Game

↓

Board
```

---

### Incidental collaborators

Useful sometimes.

Required occasionally.

Not part of the object's identity.

Example:

```text
WinningCondition

↓

Board (during evaluation)
```

That distinction becomes very important later when we discuss constructors and dependency injection.

---

## Board → Cell

This answer was excellent.

You wrote:

> **"Tomorrow it could change internally."**

Exactly.

Notice something.

The relationship stays.

The implementation changes.

Today:

```text
Board

↓

Cells
```

Tomorrow:

```text
Board

↓

Sparse representation
```

The responsibility remains.

Only the representation evolves.

That is exactly why encapsulation matters.

---

## Cell → Board

Perfect.

But I want to highlight something subtle.

Many beginners think:

> "If A owns B...

then B must know A."

You didn't fall into that trap.

Ownership is **not automatically bidirectional**.

That is an important discovery.

---

## Game → Player

Excellent.

This answer also hints at something future.

Today:

```text
Game

↓

Players
```

Tomorrow...

We might introduce:

```text
Tournament

↓

Games
```

Suddenly...

Players may participate in many games.

The relationship evolves because the business evolves.

Again...

Business first.

---

## WinningCondition → Board

This answer made me smile.

You wrote:

> **"It simply evaluates whichever Board the Game asks it to evaluate."**

That's a fantastic observation.

WinningCondition doesn't own a Board.

It works **with** a Board temporarily.

That is collaboration.

Not ownership.

---

# 🌟 Part B Review

This section was extremely consistent.

But one answer deserves highlighting.

---

## Player

You wrote:

> **Attribute (for Game).**

Exactly.

Notice something interesting.

The Player is:

* permanent for Game,
* temporary for Board.

The same object changes category depending on **who is asking**.

That's a profound idea.

Relationships are not universal.

They're contextual.

---

# 🌟 Part C Review

Your reflection contained my favourite sentence.

> **Objects don't collect references simply because they occasionally collaborate.**

Aditya...

That sentence captures today's entire lesson.

Many codebases are full of unnecessary references.

Not because they're needed.

Because someone thought:

> "Maybe we'll need it."

That's how coupling grows.

---

# 🌟 Engineering Checkpoint

Your answer is outstanding.

Especially this observation:

> **"The Board's responsibility becomes weaker."**

Notice...

You didn't focus on pointers.

You focused on **ownership erosion**.

That is architectural thinking.

Then you added:

> **"Reuse becomes much harder."**

Excellent.

Because unnecessary relationships don't just increase coupling.

They reduce **reuse**.

A Cell that knows everything about Game is no longer just a Cell.

It's a Tic-Tac-Toe Cell.

That distinction matters.

---

# 🧠 Engineering Deep Dive

As always...

Let's ask our three questions.

---

# What did we really discover today?

## **Relationship Ownership**

---

### What is Relationship Ownership?

It is:

> **Choosing long-term object references only when an object's responsibility genuinely depends on collaborating with another object throughout its lifetime.**

Notice...

Not because passing parameters is inconvenient.

Not because it saves typing.

Because the responsibility requires it.

---

### Why was this idea necessary?

Because objects collaborate constantly.

Without careful relationship design:

* everyone knows everyone,
* responsibilities blur,
* coupling increases,
* evolution slows.

Relationships need ownership just as much as data does.

---

### What problem does it solve?

It protects:

* low coupling,
* clear ownership,
* replaceable implementations,
* reusable objects,
* evolutionary design.

---

# 🌉 The Four Discoveries of Chapter 2

Aditya...

I think we're at a beautiful milestone.

Let's look at what we've built.

## 1. Class

> **Where does the responsibility live?**

↓

Software Home

---

## 2. Methods

> **What promises does the responsibility make?**

↓

Business Behaviour

---

## 3. Attributes

> **What business knowledge must it remember?**

↓

State Ownership

---

## 4. References

> **Who must it remember?**

↓

Relationship Ownership

---

Look at that.

Without opening a Python book...

We've rediscovered the four pillars of an object.

---

# 🌟 The Hidden Discovery

I don't think today's lesson was actually about references.

It was about a much bigger question.

Let's compare.

Yesterday:

> **Who owns this business fact?**

Today:

> **Who owns this business relationship?**

Ownership is becoming the central theme of everything we've designed.

And that's not an accident.

Good object-oriented design is largely about placing ownership in the right place.

---

# 🚀 I Think We're Ready for Something Special

Up to now we've been designing **pieces**.

A class.

A method.

An attribute.

A relationship.

I think tomorrow is the right moment to stop looking at the pieces individually.

Instead, we'll ask:

> **Can we now assemble the complete Tic-Tac-Toe domain model from everything we've discovered?**

Not the implementation.

The complete design.

We'll build:

* every class,
* every responsibility,
* every attribute,
* every public method,
* every collaboration,
* every relationship,

into one coherent Python model.

And here's the exciting part.

We won't be inventing anything.

We'll simply collect all the discoveries we've made over the last seven steps.

---

# 🌟 One Sentence That Changed My Thinking Today

Today's sentence comes from your own reflection:

> **"Objects don't collect references simply because they occasionally collaborate. They remember only those collaborators that are essential to their ongoing responsibility."**

That is an excellent mental model.

If you keep asking that question throughout your career—

> **"Is this collaborator essential to my responsibility, or just needed for this interaction?"**

—you'll avoid a surprising amount of unnecessary coupling.

---

# Before We Move On…

I want to propose a slight adjustment to our roadmap.

Originally, my plan was:

> **Assemble the final Python model.**

I no longer think that's the best next step.

Why?

Because there is **one missing idea** that experienced designers use constantly, and if we skip it now, you'll eventually feel something is "off."

That idea is:

# **Object Creation**

Until now we've been saying:

```python
game = Game(...)
board = Board(...)
winning_condition = WinningCondition(...)
```

But we've never asked:

* **Who creates the Board?**
* **Who creates the Cells?**
* **Should `Game` create them?**
* **Should someone else assemble them?**
* **When should an object create another object versus receive one?**

Those questions lead naturally to:

* Composition
* Dependency Injection (in spirit, before the name)
* Factory Pattern (later)
* Inversion of Control

If we assemble the whole model **before** answering those questions, we'll end up making arbitrary construction decisions—the very thing we've avoided throughout this journey.

## So here's the revised plan

**Step 7 – Chapter 2**

* ✅ Day 1 — Responsibility → Class
* ✅ Day 2 — Behaviour → Public Methods
* ✅ Day 3 — State → Attributes
* ✅ Day 4 — Relationships → Object References
* ▶️ **Day 5 — Object Creation → Who Builds the Object Graph?**
* ▶️ **Day 6 — Assemble the Complete Tic-Tac-Toe Python Domain Model**

I believe this order stays true to the philosophy we've followed since Step 0:

> **Never introduce a programming construct until the business gives us a reason for it.**

And I think that's the perfect way to finish our first case study before moving on to richer design patterns and larger systems. 🚀

