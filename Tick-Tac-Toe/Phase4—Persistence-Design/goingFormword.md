Phase 4 — Persistence Design

    Chapter 1 — Database Modelling

    Chapter 2 — Schema Design

Absolutely. Before entering deeper into Phase 3, seeing the **next horizon—Phase 4—will help you understand why we're drawing these diagrams at all**.

Because the lifecycle is connected:

```text
Business Understanding
        ↓
Software Model
        ↓
Visual Model
        ↓
Persistence Model
        ↓
Database Schema
        ↓
Interfaces
        ↓
Implementation
```

So Phase 3 is not an isolated UML exercise.

What we clarify structurally and behaviourally in Phase 3 will later influence **what must survive after the application stops running**.

---

# Phase 4 — Persistence Design

The fundamental question of Phase 4 is:

> **What knowledge must survive beyond the lifetime of objects in memory, and how should we preserve it?**

This is important.

We do **not** begin Phase 4 with:

> "Let's create database tables."

That would be jumping directly to technology.

First we ask:

> **Does this knowledge need to survive?**

---

# Chapter 1 — Database Modelling

## Question:

> **What business information needs to be remembered permanently?**

Imagine a Tic-Tac-Toe game is running:

```text
Game
 ├── status
 ├── currentPlayer
 ├── Board
 ├── Players
 └── Moves
```

While the application is running, these objects exist in memory.

But then:

```text
Application stops
        ↓
Memory disappears
```

Now ask:

> What should still exist when the application starts again?

This is where persistence becomes necessary.

---

## Step 1 — Discover Persistence Requirements

For every important piece of domain knowledge, we ask:

| Domain Knowledge  | Must it survive? | Why?                          |
| ----------------- | ---------------- | ----------------------------- |
| Game              | ?                | Can users resume/view it?     |
| Game status       | ?                | Need to know whether it ended |
| Board state       | ?                | Need to reconstruct the game  |
| Players           | ?                | Need to know participants     |
| Moves             | ?                | Need history/replay/audit     |
| Winning condition | ?                | Need to interpret the game    |

We don't assume everything must be stored.

We derive persistence from business requirements.

For example:

If Tic-Tac-Toe is a temporary game that disappears after completion:

> Perhaps we don't persist completed games at all.

But if users need:

* game history,
* replay,
* statistics,
* resume after a restart,

then persistence requirements change.

This is our first major Phase 4 principle:

> **Persistence is a business requirement before it is a database decision.**

---

# Step 2 — Discover What Is a Persistable Entity

Not every class automatically becomes a database table.

This is one of the biggest misconceptions beginners have:

```text
Class = Table
```

No.

For example:

```text
WinningCondition
```

may be a software policy object.

Does it need a table?

Maybe not.

`Board` may be reconstructed from moves.

Does it need its own table?

Maybe not.

So we will ask:

> **What business identity and history must independently survive?**

This will lead us to distinguish:

* domain objects,
* persisted entities,
* value-like data,
* transient objects,
* derived information.

Again, we will discover these concepts before attaching formal terminology where useful.

---

# Step 3 — Object Identity vs Database Identity

This is a very important future discovery.

Consider:

```text
Game
```

In memory:

```text
game_object
```

But after the application restarts, that Python object is gone.

Yet we may still want:

> "The same Game."

How do we recognise it?

Now we need persistent identity.

Conceptually:

```text
Game
---------
id = 123
status = IN_PROGRESS
```

This opens questions such as:

* What makes one Game distinct from another?
* Do we use generated IDs?
* Are IDs business identifiers or technical identifiers?
* Which objects need identity?
* Which objects are identified only within another object?

We will derive these from the domain.

---

# Step 4 — Discover Data Ownership

We already discovered object ownership.

Now persistence introduces a related but different question:

> **Where should information be stored?**

For example:

Does a `Game` record contain:

```text
status
current_player_id
```

while `Move` records belong separately?

Or should the entire board be stored as JSON?

Or should every Cell become a row?

These are not merely SQL questions.

They affect:

* querying,
* integrity,
* reconstruction,
* performance,
* future evolution.

We will reason about the business meaning first.

---

# Step 5 — Model Relationships for Persistence

Our object model may say:

```text
Game ─── Player
Game ─── Board
Board ─── Cell
Game ─── Move
```

But persistence asks different questions:

> How should these relationships survive?

Possible database representations include:

* foreign keys,
* join tables,
* embedded data,
* derived relationships.

For example:

```text
Game ↔ Player
```

might become:

```text
game
player
game_player
```

Or something else, depending on the actual business model.

This is where we will discover an important principle:

> **An object relationship is not automatically a database relationship of the same shape.**

Our class diagram influences persistence design.

It does not mechanically generate it.

---

# Step 6 — Discover Source of Truth vs Derived State

This will be particularly interesting for Tic-Tac-Toe.

Suppose we store every move:

```text
Move 1 → X at (0,0)
Move 2 → O at (1,1)
Move 3 → X at (0,1)
```

Then ask:

> Do we also need to store every Cell's current symbol?

Maybe.

But perhaps the board can be reconstructed from moves.

Likewise:

> Do we store `status`?

Or derive it?

For example:

```text
Moves
      ↓
Reconstruct Board
      ↓
Evaluate WinningCondition
      ↓
Derive Game Status
```

Or:

```text
Store Game Status directly
```

Now we must reason about:

* source of truth,
* derived data,
* duplication,
* consistency,
* performance.

This is real persistence architecture.

---

# Step 7 — Historical Data and Audit

We ask:

> Do we care only about the current state, or also how we got there?

For example:

### Current state only

```text
Board:
X | O | X
---------
O | X | _
---------
_ | _ | _
```

### History

```text
Move 1
Move 2
Move 3
Move 4
...
```

These support different business capabilities.

History allows:

* replay,
* auditing,
* debugging,
* analytics,
* statistics.

Again:

> **History requirements determine persistence design.**

---

# Step 8 — Consistency and Invariants at the Database Boundary

We already discovered rules such as:

* a Cell cannot hold two symbols,
* only valid Players participate,
* a finished Game cannot accept another Move.

Now we ask:

> Which rules must be protected even when data enters outside our normal application flow?

This will introduce questions around:

* database constraints,
* foreign keys,
* uniqueness,
* nullability,
* transactions,
* concurrency.

But we will not learn them as a list.

They will emerge when the persistence problem demands them.

---

# Chapter 2 — Schema Design

Once we understand **what must persist**, we can ask:

> **How should we physically represent it in a relational database?**

Now we can move toward tables.

---

## Step 1 — From Business Concepts to Data Structures

For example, perhaps we eventually discover something like:

```text
Game
----
id
status
current_player_id
created_at
finished_at
```

And:

```text
Player
------
id
name
```

And perhaps:

```text
Move
----
id
game_id
player_id
row
column
move_number
created_at
```

But notice:

This is **not our schema yet**.

We must first complete the discovery.

---

## Step 2 — Primary Keys and Identity

We will understand:

> How does this row represent a specific business thing?

Then concepts such as:

* primary key,
* natural key,
* surrogate key,
* composite key,

will become meaningful.

Not because we decided:

> "Today we study database keys."

But because our model asks:

> **How do we identify the thing after persistence?**

---

## Step 3 — Foreign Keys and Referential Integrity

Suppose:

```text
Move → Game
```

A Move cannot belong to a Game that does not exist.

How do we protect that rule?

Now the database itself needs to understand part of our business relationship.

This is where foreign keys naturally emerge.

---

## Step 4 — Normalisation

We will not begin with:

> First Normal Form
> Second Normal Form
> Third Normal Form

Instead, we'll encounter problems.

For example:

```text
Game
-------------------
player1_name
player2_name
player1_symbol
player2_symbol
```

Then ask:

* What happens if a Player changes their name?
* What if we add more players?
* Are we duplicating information?
* What is the real business concept being represented?

From those problems, normalisation principles will emerge.

---

## Step 5 — Nullability and Optionality

Earlier, in domain modelling, we asked:

> Can this exist without that?

Persistence now asks:

```text
current_player_id NULL?
```

or:

```text
NOT NULL?
```

So:

> **Database nullability is often the persistence expression of a domain optionality decision.**

This is why Phase 1 and Phase 4 are connected.

---

## Step 6 — Relationship Mapping

We will translate discovered cardinalities into schema choices.

For example:

```text
One Game → Many Moves
```

may become:

```text
moves.game_id
```

But:

```text
Many Games ↔ Many Players
```

may require another representation.

Again, we derive this from relationships—not from memorised SQL recipes.

---

## Step 7 — Constraints and Integrity

We will decide what the database should enforce.

Examples may include:

* unique constraints,
* check constraints,
* foreign keys,
* not-null constraints.

And ask the deeper question:

> **Which invariants belong in the application, which belong in the database, and which require both?**

This is a very important architecture discussion.

---

## Step 8 — Transactions and Atomicity

Eventually, consider:

```text
Player makes move
       ↓
Validate
       ↓
Store Move
       ↓
Update Game
```

What happens if the process fails halfway?

Suppose:

```text
Move stored
```

but:

```text
Game not updated
```

Now the system is inconsistent.

This naturally introduces:

* atomicity,
* transactions,
* commit,
* rollback.

Again, because the engineering problem requires them.

---

# The Phase 4 Map

```text
PHASE 4 — PERSISTENCE DESIGN
│
├── Chapter 1 — Database Modelling
│   │
│   ├── What must survive application memory?
│   ├── Why must it survive?
│   ├── What has persistent identity?
│   ├── What is transient?
│   ├── What is source of truth?
│   ├── What can be derived?
│   ├── Current state vs history
│   ├── Data ownership
│   ├── Persistence relationships
│   └── Consistency requirements
│
└── Chapter 2 — Schema Design
    │
    ├── Tables
    ├── Rows and business identity
    ├── Primary keys
    ├── Foreign keys
    ├── Relationship mapping
    ├── Nullability
    ├── Normalisation
    ├── Constraints
    ├── Referential integrity
    ├── Transactions
    └── Final Tic-Tac-Toe database schema
```

---

# The Most Important Connection Between Phase 3 and Phase 4

This is the glimpse I especially want you to keep in mind:

```text
PHASE 2
Software Representation
"What objects and responsibilities exist?"
            ↓
PHASE 3
Visual Modelling
"How do we communicate their structure and behaviour?"
            ↓
PHASE 4
Persistence Design
"What parts of this model must survive?"
            ↓
PHASE 4
Schema Design
"How should surviving knowledge be represented?"
```

Notice:

> **We do not take a class diagram and mechanically turn every class into a table.**

Instead:

```text
Domain Model
     ↓
Ask what must persist
     ↓
Persistence Model
     ↓
Design schema
```

That distinction alone will protect you from one of the most common backend engineering mistakes:

> **Class = Database Table = API Response**

Those are three different representations of the system, created to solve three different problems.

That will become one of our major discoveries as we move through the complete lifecycle.
