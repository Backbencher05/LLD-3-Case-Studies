This is exciting.

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
