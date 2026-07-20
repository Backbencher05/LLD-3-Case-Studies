This is exactly why I agreed to change our review style.

Earlier, we were building the **thinking framework**.

Now we're **applying** that framework.

Notice what you just said:

> **"I completely understand and also agree with this table."**

That's the milestone I was waiting for.

If you had simply accepted the table because *I* said so, we would have failed.

Instead, you've reached the point where you can say:

> **"Yes, this classification makes sense because of the reasoning we've already built."**

That means we don't need to repeat the entire discussion for every remaining concept.

We can review them like architects in a design review.

---

# Step 3 — Part C Review

# Reviewing Your Enums

This was your original submission.

```text
Game Status

Player Type

Bot Difficulty

Cell State

Direction

Turn Status

Game Mode
```

---

# Overall Review

## ⭐⭐⭐⭐⭐ Rating: **9.8/10**

This is an even stronger section than your original Value Objects.

Probably because, as you mentioned, you were already familiar with Enums from backend development.

However...

Knowing `enum` in Java/Python is different from understanding **why the business needs an Enum**.

After our earlier discussions, we can now review these from a **domain perspective**, not a programming-language perspective.

---

# Candidate 1 — Game Status

Your values:

```text
NOT_STARTED
IN_PROGRESS
DRAW
WON
ENDED
```

## Review

Excellent candidate for an Enum.

The business defines a **finite set of allowed states**.

However, I'd make one small refinement.

Notice this list:

```text
NOT_STARTED
IN_PROGRESS
DRAW
WON
ENDED
```

There is a slight overlap.

`DRAW` and `WON` are actually **terminal outcomes**, while `NOT_STARTED`, `IN_PROGRESS`, and `ENDED` describe the **lifecycle state**.

There are two clean ways to model this.

### Option 1 (Simple Tic-Tac-Toe)

```text
NOT_STARTED
IN_PROGRESS
DRAW
WON
```

No need for `ENDED`, because `DRAW` and `WON` already imply the game has ended.

### Option 2 (Larger systems)

Separate them.

Game Status

```text
NOT_STARTED
IN_PROGRESS
ENDED
```

Game Outcome

```text
DRAW
PLAYER_X
PLAYER_O
```

For our current scope, I'd recommend **Option 1**.

---

# Candidate 2 — Player Type

```text
HUMAN
BOT
```

## Review

Perfect.

No changes.

The business explicitly restricts the allowed participant types.

Strong Enum.

---

# Candidate 3 — Bot Difficulty

```text
EASY
MEDIUM
HARD
```

## Review

Excellent.

Exactly what Enums are for.

If one day the business allows users to define custom AI difficulty levels, this could evolve into a managed concept.

But for the current domain:

✅ Enum.

---

# Candidate 4 — Cell State

Your values:

```text
EMPTY
OCCUPIED
FILLED
```

You even added:

> Or simply derive it from the presence of a symbol.

👏

That sentence is the important part.

I actually agree with your own note.

Let's think.

A Cell already contains:

```text
Position

Symbol
```

If Symbol exists:

Cell is occupied.

If Symbol is absent:

Cell is empty.

Do we really need another Enum?

Probably not.

Otherwise we risk storing the same fact twice.

Example:

```text
Symbol = X

CellState = EMPTY
```

Impossible.

Now we've introduced inconsistency.

---

## Final Decision

I'd avoid `CellState` entirely.

Instead:

```text
Cell.symbol == null

↓

EMPTY

otherwise

↓

OCCUPIED
```

Much cleaner.

---

# Candidate 5 — Direction

```text
ROW
COLUMN
MAIN_DIAGONAL
ANTI_DIAGONAL
```

Excellent.

This is a classic Enum.

Business defines a finite set.

No changes.

---

# Candidate 6 — Turn Status

```text
CURRENT
WAITING
```

Interesting.

Let's ask:

> Does the business actually talk about Turn Status?

Or does it simply know:

```text
Current Player
```

In Tic-Tac-Toe, the game already tracks whose turn it is.

If I know:

```text
Current Player = Aditya
```

then everyone else is automatically waiting.

So introducing another Enum adds little value.

---

## Final Decision

I'd remove it.

The Game already knows whose turn it is.

---

# Candidate 7 — Game Mode

```text
HUMAN_VS_HUMAN
HUMAN_VS_BOT
BOT_VS_BOT
```

Excellent.

Strong Enum.

Finite business-defined choices.

No changes.

---

# Final Reviewed Enum List

| Concept          | Final Classification | Notes                                                                             |
| ---------------- | -------------------- | --------------------------------------------------------------------------------- |
| ✅ Game Status    | Enum                 | Prefer `NOT_STARTED`, `IN_PROGRESS`, `DRAW`, `WON` for this scope.                |
| ✅ Player Type    | Enum                 | Human or Bot.                                                                     |
| ✅ Bot Difficulty | Enum                 | Easy, Medium, Hard.                                                               |
| ❌ Cell State     | Remove               | Can be derived from whether a Symbol is present.                                  |
| ✅ Direction      | Enum                 | Fixed set of traversal directions.                                                |
| ❌ Turn Status    | Remove               | Current player already represents this information.                               |
| ✅ Game Mode      | Enum                 | Human vs Human, Human vs Bot, Bot vs Bot.                                         |
| ✅ Symbol         | Enum                 | Moved here from Value Objects because the business restricts the allowed symbols. |

---

# Have We Missed Any Enums?

For the current domain, I don't think we've missed any essential Enums.

Some optional additions in an expanded game might include:

* Starting Player (`PLAYER_X`, `PLAYER_O`, `RANDOM`)
* Win Type (`ROW`, `COLUMN`, `DIAGONAL`) if you wanted to explicitly represent how a game was won—but that depends on whether the business needs it.

---

# Final Enum Summary

One thing I want to emphasize is that you've now internalized the key difference:

* **Value Object:** "The business cares about the value itself."
* **Enum:** "The business restricts the value to a predefined set."

That distinction is much more important than the syntax of an `enum` keyword.

---

# One Sentence That Changed My Thinking

I'd add this to our collection:

> **"An Enum exists because the business says, 'These are the only valid choices.'"**

---

## 🎯 Mentor's Reflection

Compared to your original submission, I made only a few refinements:

* Moved **Symbol** from Value Objects to Enums.
* Removed **Cell State** because it's derived.
* Removed **Turn Status** because it's already represented by the current player.
* Slightly refined **Game Status** to avoid overlapping concepts.

Everything else held up well.

That tells me something encouraging:

By the time you wrote the Enum section, your intuition about the domain was already much closer to a mature design than when you first wrote the Entity section.

And that's exactly the progression I'd expect as someone moves from recognizing programming constructs to modeling the business itself.

---

We now have:

* ✅ **Part A — Entities** (reviewed and finalized)
* ✅ **Part B — Value Objects** (reviewed and refined)
* ✅ **Part C — Enums** (reviewed and refined)

Only one major section remains:

**Part D — Supporting Concepts.**

Interestingly, I think that discussion will tie together everything we've learned so far, because Supporting Concepts are where the **behavior and rules of the domain** begin to emerge before we ever write a class.
