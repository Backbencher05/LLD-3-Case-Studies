Aditya...

I think today is the last missing puzzle piece before we assemble the complete model.

Up to now, we've answered:

* **Who exists?**
* **Who owns what?**
* **Who remembers what?**
* **Who collaborates with whom?**

But we've quietly ignored one question.

> **Who brings all of these objects into existence?**

Most tutorials jump straight to this:

```python
game = Game(Board(3), WinningCondition(), players)
```

Nobody asks:

> **Why is `Game` creating a `Board`?**

or

> **Should it?**

Today we'll discover that.

---

# 🚀 Step 7 — Chapter 2, Day 5

# Object Creation → Who Builds the Object Graph?

Let's leave software once more.

---

# A Restaurant Story

Imagine a new restaurant opens tomorrow.

Question.

Does the Restaurant Manager build the restaurant?

Does the manager:

* hire the architect,
* pour the concrete,
* install the kitchen,
* buy the furniture?

No.

When the manager arrives...

The restaurant already exists.

The manager's responsibility is:

> **Run the restaurant.**

Not:

> **Construct the restaurant.**

Interesting...

---

# Another Story

Imagine a football match.

Question.

Does the referee create the stadium?

Choose the players?

Paint the lines?

Install the goalposts?

No.

Someone else prepares the environment.

The referee simply begins managing the match.

---

# The First Discovery

Running something...

and creating something...

are different responsibilities.

That's true in business.

It should also be true in software.

---

# Back to Tic-Tac-Toe

Let's ask a dangerous question.

Should `Game` do this?

```python
class Game:

    def __init__(self):
        self.board = Board(3)
        self.players = [
            HumanPlayer("A"),
            BotPlayer()
        ]
        self.winning_condition = WinningCondition()
```

At first glance...

This feels convenient.

Everything is created automatically.

But let's think like engineers.

---

# What Has Just Happened?

The Game now knows:

* how to create a Board,
* which Board size,
* which WinningCondition,
* which Player types,
* how many Players.

Question.

Is creating those objects part of:

> **Managing a match?**

Or is it a different responsibility?

---

# Imagine the Business Changes

Tomorrow the business says:

> Support:

* 5×5 board,
* Human vs Human,
* Human vs AI,
* AI vs AI,
* Different winning strategies.

Now who changes?

The Game.

Again.

And again.

And again.

Not because its own responsibility changed.

Because construction changed.

That's a smell.

---

# A Better Way

Imagine instead.

Someone else prepares everything.

```text
Board

↓

Players

↓

WinningCondition

↓

Game
```

The Game simply receives collaborators.

Now ask:

Has the Game become simpler?

Yes.

Why?

Because it only manages the match.

It no longer worries about building the world.

---

# A Restaurant Again

Restaurant Manager.

When the manager starts work:

* chefs already exist,
* kitchen already exists,
* tables already exist.

The manager receives collaborators.

Exactly like the Game.

---

# The Second Discovery

An object should create another object only if:

> **Creating that object is naturally part of fulfilling its own responsibility.**

Notice.

Not because it is convenient.

Because the business says so.

---

# Let's Test This Rule

---

## Should Game create Board?

Business question.

Is constructing the playing area part of managing the match?

Usually...

No.

Someone prepares the board before the match begins.

Better:

Receive Board.

---

## Should Board create Cells?

Interesting.

Who owns the playing area?

Board.

Can a Board exist without its internal representation?

No.

Creating Cells is naturally part of becoming a valid Board.

This feels different.

Here...

Creation supports the Board's own responsibility.

Much more reasonable.

---

## Should WinningCondition create Board?

Definitely not.

It evaluates Boards.

It doesn't manufacture them.

---

## Should Cell create Symbol?

Think carefully.

Initially...

Every Cell starts empty.

Does it need to create a Symbol?

No.

It simply begins empty.

Interesting.

Not every attribute needs an object.

---

# The Hidden Principle

There are two kinds of collaborators.

---

## Owned Internals

The object naturally creates them.

Example:

```text
Board

↓

Cells
```

---

## External Collaborators

The object receives them.

Example:

```text
Game

↓

Board
```

Different relationships.

Different creation rules.

---

# Our Python Changes Again

Instead of this:

```python
class Game:

    def __init__(self):
        self.board = Board(3)
        self.winning_condition = WinningCondition()
```

We now prefer:

```python
class Game:

    def __init__(self, board, players, winning_condition):
        self._board = board
        self._players = players
        self._winning_condition = winning_condition
```

Question.

Did Python become better?

No.

Our design became better.

Python simply reflects it.

---

# What About Board?

Now compare.

```python
class Board:

    def __init__(self, size):
        self._size = size
        self._cells = self._create_cells()
```

Notice something.

Here...

The Board creates Cells.

Because:

Cells are part of its own internal structure.

That feels natural.

---

# The Growing Discovery Map

```text
Business Responsibility

↓

Business Behaviour

↓

Business State

↓

Business Relationships

↓

Object Creation   ← Today

↓

Python Constructors
```

Again...

Python follows business.

---

# 🎯 Step 7 — Chapter 2, Day 5 Assignment

## Part A — Who Should Create It?

For each relationship answer:

1. Who should create the object?
2. Why?
3. Should it be created internally or received from outside?

---

### Board

(Who should create it for the Game?)

---

### Cells

(Who should create them?)

---

### WinningCondition

---

### Players

---

### Symbol

---

## Part B — Internal Creation or External Collaboration?

For each pair decide whether the second object should usually be:

* **Created internally**
* **Received externally**

Explain using **business responsibility**, not Python convenience.

---

### Game → Board

---

### Game → WinningCondition

---

### Board → Cells

---

### Game → Players

---

### Cell → Symbol

---

## Part C — Reflection

Complete these sentences.

> **An object creates another object because...**

> **An object receives another object because...**

Then answer:

> **Why is construction a different responsibility from coordination?**

---

# 🌟 Engineering Checkpoint

Imagine the following design.

```python
Game

↓

creates Board

↓

creates Cells

↓

creates WinningCondition

↓

creates Players
```

Question.

> **If the business later changes how any one of those collaborators should be created, which object will keep changing?**

What does that tell you about responsibility?

---

# 🧠 Engineering Deep Dive

Today we've quietly discovered another cornerstone of software design.

A constructor (`__init__`) is **not** merely a place to initialise attributes.

It is the place where an object enters the world in a **valid state**.

But there is another question hidden inside it:

> **Should this object build its own world, or should the world be prepared before it arrives?**

That decision is one of the foundations behind ideas like:

* Dependency Injection
* Composition Root
* Factory Pattern

We won't use those names yet.

Today we're discovering the business reasoning that made those ideas necessary.

---

# 🌟 One Sentence to Carry Forward

> **An object should create only the parts that naturally belong to itself; everything else should arrive as a trusted collaborator.**

---

# A Tiny Preview...

Tomorrow, we'll finally do what we've been patiently preparing for since Step 0.

We'll assemble the complete Tic-Tac-Toe Python domain model.

But this time, every single line of the model will answer a business question we've already solved:

* Why does this class exist?
* Why does this method exist?
* Why is this an attribute?
* Why is this relationship here?
* Why is this collaborator received instead of created?

Nothing will be arbitrary.

We'll simply give Python to the business model we've spent all this time discovering.

And I think you'll notice something remarkable.

The code won't feel like something we're inventing.

It will feel like something we're revealing. 🚀


----------------------------------------------------------------------------------------------------------------------------------------
## My Answers
----------------------------------------------------------------------------------------------------------------------------------------

Excellent.

Today's assignment introduces one of the most misunderstood ideas in object-oriented design.

Many developers ask:

> **"Where should I write `new`?"**

But that's an implementation question.

The real design question is:

> **"Who is responsible for bringing this collaborator into existence?"**

Creation is a business decision before it becomes a programming decision.

Sometimes an object should create another object because it **owns** it.

Sometimes it should receive another object because it merely **collaborates** with it.

That distinction is what we'll discover today.

---

# Part A — Who Should Create It?

## 1. Board

### Who should create it for the Game?

The **Game should receive the Board from outside**.

### Why?

The Game is responsible for **using** a Board to coordinate gameplay.

It is not fundamentally responsible for deciding **how a Board comes into existence**.

Imagine future requirements:

* Standard Board
* 5×5 Board
* Hexagonal Board
* Loaded from a saved game

The Game's responsibility hasn't changed.

Only board creation has.

Therefore, creation is better handled outside the Game, and the Game receives a ready-to-use Board.

---

## 2. Cells

### Who should create them?

The **Board**.

### Why?

Cells are not independent collaborators.

They are part of the Board's internal representation.

The Board owns the playing area, so constructing that playing area naturally belongs to the Board.

If the internal representation changes tomorrow, only the Board should need to change.

### Created internally or received?

**Created internally.**

---

## 3. WinningCondition

### Who should create it?

The **Game should receive it from outside**.

### Why?

The Game collaborates with a winning rule.

It doesn't own the responsibility of deciding which winning rule exists.

Future possibilities include:

* Classic Tic-Tac-Toe
* Connect Four
* Gomoku
* Custom tournament rules

Those are different collaborators, not different Games.

So the Game should receive the appropriate WinningCondition.

---

## 4. Players

### Who should create them?

The **Game should usually receive them from outside**.

### Why?

Players exist independently of any particular game.

They may be:

* Human
* Easy Bot
* Hard Bot
* Remote Player

The Game coordinates whoever participates.

It shouldn't decide how those participants are constructed.

---

## 5. Symbol

### Who should create it?

Usually, **it should be provided externally or represented as a value**, not constructed by the Cell.

### Why?

The Cell doesn't invent symbols.

It simply stores the symbol assigned during a move.

The symbol belongs to the move or player context, not to the Cell's construction process.

---

# Summary

| Object           | Who creates it?    | Internal or External? | Reason                                                                    |
| ---------------- | ------------------ | --------------------- | ------------------------------------------------------------------------- |
| Board            | Outside the Game   | Received              | Game collaborates with a Board but shouldn't decide how one is built.     |
| Cells            | Board              | Internal              | Cells are part of the Board's internal representation.                    |
| WinningCondition | Outside the Game   | Received              | Different rule implementations may be supplied without changing the Game. |
| Players          | Outside the Game   | Received              | Players are independent participants.                                     |
| Symbol           | Outside (or value) | Received              | Cell stores it but doesn't create it.                                     |

---

# Part B — Internal Creation or External Collaboration?

The key question is:

> **"Does the first object own the second object as part of its internal structure, or does it simply collaborate with it?"**

---

## Game → Board

### Decision

**Received externally**

### Why?

The Board is a collaborator.

The Game depends on a Board, but the details of constructing one are separate from coordinating gameplay.

---

## Game → WinningCondition

### Decision

**Received externally**

### Why?

The Game collaborates with a rule evaluator.

Different business rules can be introduced without changing the Game.

Receiving the collaborator keeps those concerns separate.

---

## Board → Cells

### Decision

**Created internally**

### Why?

Cells form the Board's internal structure.

No other object should need to know how the Board builds or organises them.

---

## Game → Players

### Decision

**Received externally**

### Why?

The Game coordinates players but does not define who they are or how they are created.

That allows different player types without changing the Game.

---

## Cell → Symbol

### Decision

**Received externally**

### Why?

The Cell's responsibility is to store the assigned symbol.

It shouldn't decide which symbol exists.

---

# Summary

| Relationship            | Created Internally / Received Externally | Why                                               |
| ----------------------- | ---------------------------------------- | ------------------------------------------------- |
| Game → Board            | Received                                 | Board is a collaborator.                          |
| Game → WinningCondition | Received                                 | Rule evaluator is a collaborator.                 |
| Board → Cells           | Created internally                       | Cells are part of the Board's internal structure. |
| Game → Players          | Received                                 | Players participate independently.                |
| Cell → Symbol           | Received                                 | Cell stores the symbol rather than creating it.   |

---

# Part C — Reflection

### Complete the sentences.

> **An object creates another object because that object is part of its own internal responsibility or representation.**

---

> **An object receives another object because it needs to collaborate with it, not own the responsibility of constructing it.**

---

### Why is construction a different responsibility from coordination?

Construction answers:

> **"How does this collaborator come into existence?"**

Coordination answers:

> **"How do existing collaborators work together to achieve a business goal?"**

Those are different concerns.

If we mix them together, one object becomes responsible for both assembling the system and running the business process.

That makes it change for unrelated reasons.

A change in **how a Board is built** is different from a change in **how a Game is played**.

Keeping those responsibilities separate allows each to evolve independently.

---

# 🌟 Engineering Checkpoint

## If the Game creates the Board, Cells, WinningCondition, and Players, which object will keep changing?

The **Game**.

Every change to the construction of any collaborator would require changes to the Game, even when the Game's own business responsibility hasn't changed.

For example:

* A new type of Board → Game changes.
* A different WinningCondition → Game changes.
* A new Player type → Game changes.
* A different way of building Cells → if the Game is involved, it changes too.

The Game becomes responsible not only for coordinating gameplay, but also for assembling the entire system.

That's a signal that multiple responsibilities have accumulated in one place.

The lesson is not that the Game should never create anything. In fact, it is reasonable for the **Board** to create its **Cells**, because they are part of the Board's own internal representation.

The broader principle is this:

> **An object should construct what it truly owns, and collaborate with what it merely uses.**

That keeps construction aligned with ownership and coordination aligned with business flow.

---

# 🌟 One Sentence That Changed My Thinking

> **Creation follows ownership; collaboration follows responsibility.**

---

# Mentor's Feedback

This assignment completes another important layer of the design journey.

We've now discovered four distinct kinds of relationships between objects:

```text
Business Responsibility
        │
        ├── Owns Information
        ├── Owns Behaviour
        ├── Owns Long-term Relationships
        └── Owns Internal Construction
```

Notice the pattern:

* The **Board** owns the playing area, so it reasonably creates the objects that make up that playing area.
* The **Game** owns the lifecycle of the match, but it does not own the creation of every participant or rule it collaborates with.

A useful question to ask yourself in future designs is:

> **"If the way this object is created changes, whose business responsibility has actually changed?"**

If the answer is **"not mine"**, that's a strong indication the object should probably be **received**, not **constructed**.

That way of thinking scales well beyond Tic-Tac-Toe. Whether you're designing a payment system, an e-commerce platform, or a microservice architecture, separating **construction** from **coordination** helps each responsibility remain focused and adaptable.



----------------------------------------------------------------------------------------------------------------------------------------
## Answers Feedback and Next
----------------------------------------------------------------------------------------------------------------------------------------

Aditya...

I had a feeling this would happen.

Today's assignment wasn't really about constructors.

It was about something much deeper.

You discovered the difference between:

> **Owning a responsibility**

and

> **Depending on a responsibility.**

That distinction sits at the heart of clean software architecture.

---

# 🌉 Let's Review What You Actually Did

Most people answer today's assignment like this:

> "Game receives Board because Dependency Injection."

or

> "Board creates Cells because Composition."

Those answers use terminology.

Your answers used **reasoning**.

For example, you wrote:

> **"The Game collaborates with a Board, but shouldn't decide how one is built."**

That is exactly how experienced architects think.

Notice what's missing.

You never mentioned:

* SOLID
* Dependency Injection
* IoC
* Factory

Yet your reasoning naturally leads to all of them.

That's the goal of this mentorship.

Discover the idea before learning the name.

---

# Part A Review

---

## Board

This answer is excellent.

You wrote:

> **"The Game is responsible for using a Board."**

That single verb matters.

Not:

> owning

Not:

> constructing

But:

> **using**

Let's compare.

### Wrong mindset

```text
Game owns Board

↓

Therefore Game creates Board.
```

Seems logical.

---

### Better mindset

```text
Game collaborates with Board

↓

Someone prepares Board

↓

Game uses Board
```

Ownership of the relationship does **not** automatically imply ownership of construction.

That is a subtle but extremely important distinction.

---

## Cells

This is one of your strongest answers.

You recognised that Cells are not peers.

They're part of the Board's internal representation.

That means:

```text
Board

↓

Internal Structure

↓

Cells
```

This is fundamentally different from:

```text
Game

↓

External Collaborator

↓

WinningCondition
```

One is part of the object's identity.

The other is part of its collaboration.

Those deserve different creation strategies.

---

## WinningCondition

Excellent.

You gave future examples:

* Gomoku
* Connect Four
* Tournament rules

Notice what you're doing now.

You're testing your design against future business variation.

That's exactly how architects validate designs.

You didn't change Game.

You changed collaborators.

That's a healthy design.

---

## Players

Perfect.

One sentence stood out.

> **"Players exist independently of any particular game."**

That's an excellent business observation.

Because they exist independently...

The Game shouldn't be responsible for bringing them into existence.

Business reasoning.

Not framework reasoning.

---

## Symbol

Very nice.

You also avoided an easy trap.

You didn't say:

> Cell creates Symbol.

Instead you recognised:

The Cell receives a value.

It doesn't invent one.

That's exactly right.

---

# 🌟 Part B Review

Every answer was consistent.

That's something I pay attention to.

A lot of students answer correctly...

but inconsistently.

You didn't.

Every explanation returned to the same question:

> **Is this part of my internal structure, or an external collaborator?**

That consistency tells me you've internalised the principle rather than memorised examples.

---

# 🌟 Part C Review

This sentence deserves to be highlighted.

> **"Construction answers 'How does this collaborator come into existence?' Coordination answers 'How do existing collaborators work together?'"**

Aditya...

That is an outstanding distinction.

Let's visualise it.

---

Construction:

```text
Board

↓

Cells

↓

Ready
```

---

Coordination:

```text
Game

↓

Board

↓

WinningCondition

↓

Players

↓

Match
```

Construction prepares.

Coordination performs.

Those are different responsibilities.

Exactly as you described.

---

# 🌟 Engineering Checkpoint

Your conclusion is excellent.

Especially this line:

> **"The Game becomes responsible not only for coordinating gameplay, but also for assembling the entire system."**

That sentence captures a common design smell.

When one object is responsible for:

* building everything,
* configuring everything,
* coordinating everything,

it becomes what we call a **God Object**.

Not because it's large.

Because it has accumulated unrelated reasons to change.

Notice how this connects back to our earliest discussions about responsibility.

---

# 🧠 Engineering Deep Dive

As always, let's ask our three questions.

---

# What did we really discover today?

## **Creation Ownership**

---

### What is Creation Ownership?

It is:

> **Deciding which object is responsible for bringing another object into existence based on business ownership rather than programming convenience.**

Notice...

Not:

> "Who calls `new`?"

But:

> **Whose responsibility naturally includes creating this thing?**

---

### Why was this idea necessary?

Because creation is work.

If every object creates all of its collaborators:

* coupling grows,
* testing becomes harder,
* variation becomes difficult,
* responsibilities mix together.

We need the same discipline for creation that we've already applied to behaviour, state, and relationships.

---

### What problem does it solve?

It separates:

* assembling the system,
* running the system.

Those are different concerns.

And they change for different reasons.

---

# 🌉 The Five Discoveries of Chapter 2

Let's step back and admire what we've built.

### 1. Responsibility → Class

> Where does this responsibility live?

↓

Class

---

### 2. Behaviour → Methods

> What promises does it make?

↓

Methods

---

### 3. State → Attributes

> What business knowledge must it remember?

↓

Attributes

---

### 4. Relationships → References

> Which collaborators must it remember?

↓

Object references

---

### 5. Creation → Constructors

> Which parts should it build itself?

↓

Construction strategy

---

Look at that progression.

Nothing came from Python.

Everything came from the business.

Python merely gave those discoveries a syntax.

---

# 🌟 One More Hidden Discovery

Over the past few days, we've quietly answered **five different ownership questions**.

| Question                      | Ownership Decision              |
| ----------------------------- | ------------------------------- |
| Who owns this responsibility? | Class                           |
| Who owns this behaviour?      | Method                          |
| Who owns this business fact?  | Attribute                       |
| Who owns this collaboration?  | Reference                       |
| Who owns this creation?       | Constructor / external assembly |

Do you see the pattern?

Every major design decision we've made has been an **ownership decision**.

That's why I often say:

> **Object-oriented design is less about objects than it is about placing ownership correctly.**

---

# 🌟 One Sentence That Changed My Thinking Today

Today's sentence comes from your own engineering checkpoint:

> **"An object should construct what it truly owns, and collaborate with what it merely uses."**

I genuinely love that sentence.

It ties together:

* state ownership,
* relationship ownership,
* creation ownership,

into one memorable principle.

---

# 🚀 Tomorrow Is a Milestone

Aditya...

Tomorrow is not "another lesson."

It's the culmination of everything we've done since **Step 0**.

We are going to build the **complete Tic-Tac-Toe domain model**.

But here's the important part:

We are **not** going to "design" it tomorrow.

We've already done that.

Tomorrow is more like an archaeologist uncovering a sculpture that's already buried.

We'll simply reveal it.

We'll assemble:

* every class,
* every responsibility,
* every attribute,
* every public method,
* every relationship,
* every constructor,
* every collaboration,

into one coherent Python model.

And for every single line of code, you'll be able to answer:

> **"Which business discovery justified this line?"**

If you can do that, you've achieved something far more valuable than finishing Tic-Tac-Toe.

You've learned a repeatable design process.

That's the mindset we'll carry into Amazon, Uber, Netflix, Airbnb, and every future case study. I think this is exactly the foundation we wanted before scaling up to real-world systems. 🚀
