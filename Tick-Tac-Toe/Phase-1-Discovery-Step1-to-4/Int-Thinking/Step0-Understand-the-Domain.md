
---

# 🎯 Step 0 — Understand the Domain (Interview Thinking)

> **Interviewer:** "Design Tic-Tac-Toe."

### My Response

> Before jumping into the design, I'd like to spend a minute understanding the problem to ensure we're solving the right one.

From my understanding:

* Tic-Tac-Toe is a turn-based strategy game.
* Players alternately place their unique symbols on the board.
* A move is allowed only on an empty cell.
* The game ends when a player satisfies the winning condition or when no valid moves remain, resulting in a draw.

Before moving forward, I'd like to clarify a few assumptions:

* Is the board always **3 × 3**, or should it be configurable?
* Will the game support only **Human vs Human**, or should we also support Bot players?
* Is the winning condition fixed, or should it be configurable for larger boards?
* Are we designing only the game logic, or the complete application?

> Once these assumptions are clear, I'd move on to defining the scope of the system.

---

## 💡 Why this is a good interview answer

Notice what you **didn't** do.

You didn't say:

> "I'll create Game, Board, Player..."

That's too early.

Instead, you demonstrated that you first understand the problem before designing it.

That immediately creates confidence in the interviewer.


-------------------------------------------------------------------------------------------------------


# 🚀 Step 0 — Problem Understanding (Interview Cheat Sheet)

This is probably the most overlooked step in LLD interviews.

Most candidates hear the problem statement and immediately start drawing classes.

Senior engineers pause.

---

# 📋 Final Problem Understanding Summary

Before making any design decisions, we answered a few fundamental questions.

| Discovery Question                 | Our Understanding                                      | Why It Matters                                                |
| ---------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------- |
| What is the business problem?      | Build a Tic-Tac-Toe game.                              | Defines the domain we are modeling.                           |
| What is the primary goal?          | Allow two participants to play according to the rules. | Keeps the design focused on business value.                   |
| Is this an infrastructure problem? | No                                                     | Avoids discussing scaling or distributed systems prematurely. |
| Is this a domain modeling problem? | Yes                                                    | Guides us toward discovering business concepts first.         |
| What should we avoid initially?    | Classes, patterns, databases                           | Prevents solution bias before understanding the problem.      |

---

# 🧠 The Business Questions Step 0 Answered

| Business Question                | Understanding                 |
| -------------------------------- | ----------------------------- |
| What problem are we solving?     | Tic-Tac-Toe gameplay          |
| Who benefits?                    | Players                       |
| What kind of design is expected? | Domain Model                  |
| What should I postpone?          | Implementation details        |
| What should I understand first?  | Business rules and objectives |

---

# 🎯 The Interview Story (30-Second Version)

If the interviewer asks:

> "What would you do first?"

You can answer:

> "Before discussing objects or classes, I'd make sure I understand the problem correctly. I'd clarify whether the interview is focused on domain modeling or distributed systems, identify the core business goal, and ensure we're solving the right problem. Only after confirming that understanding would I move on to defining the scope."

---

# 🏆 The Step 0 Mental Model

```text
        PROBLEM STATEMENT

                │
                ▼

      What is the business trying to achieve?

                │
                ▼

     What kind of system is this?

                │
                ▼

     What is NOT being asked?

                │
                ▼

     Do I understand the domain?

                │
                ▼

        Only then...

        Move to Scope
```

Notice the discipline.

You don't solve the problem.

You first **understand the problem**.

---

# 🌍 Problem Understanding Vocabulary

| Business Meaning   | Question                            |
| ------------------ | ----------------------------------- |
| Business Goal      | What problem are we solving?        |
| Domain             | What business are we modeling?      |
| System Type        | Entity System or Management System? |
| Success Criteria   | What makes this system successful?  |
| Hidden Assumptions | What needs clarification?           |
| Unknowns           | What should I ask before designing? |

---

# 💡 Problem Understanding Decision Matrix

| If the interviewer says... | First ask yourself...                             |
| -------------------------- | ------------------------------------------------- |
| "Design a Parking Lot"     | Am I modeling the domain or the entire ecosystem? |
| "Design Splitwise"         | What business problem does it solve?              |
| "Design Chess"             | What is the primary objective?                    |
| "Design BookMyShow"        | What is the system responsible for?               |
| "Design Elevator"          | What is inside the scope, and what is outside?    |

---

# 🌟 Biggest Lesson of Step 0

> **The first design decision is not choosing a class—it is making sure you're solving the right problem.**

# 🎓 Looking Back: The Complete LLD Design Methodology

Now look at the progression we've created:

| Step                | Core Question                               | Deliverable            |
| ------------------- | ------------------------------------------- | ---------------------- |
| **Step 0**          | *Am I solving the right problem?*           | Problem Understanding  |
| **Step 1**          | *What are the boundaries of this design?*   | Scope Clarification    |
| **Step 2**          | *What must this system do?*                 | Requirement Discovery  |
| **Step 3**          | *What exists in the business?*              | Domain Discovery       |
| **Step 4**          | *How do those concepts work together?*      | Relationship Discovery |
| **Step 5** *(Next)* | *How do I express this domain in software?* | Class Design           |

---

## 🌟 One Final Observation

I don't think we should call this process **"Tic-Tac-Toe LLD"** anymore.

What we've built is much more general.

We've created a repeatable engineering methodology that can be applied to **any object-oriented design problem**.

I would even give it a name:

> **The PEN LLD Methodology**

Where **PEN** stands for:

* **P — Problem & Planning** *(Steps 0–2)*

  * Understand the problem.
  * Define the scope.
  * Gather and classify requirements.

* **E — Explore the Domain** *(Steps 3–4)*

  * Discover business concepts.
  * Discover business relationships.

* **N — Normalize into Software** *(Steps 5 onward)*

  * Translate the business model into classes, interfaces, patterns, responsibilities, collaborations, and finally implementation.

This naming captures the evolution we've followed: first understand **why** the system exists, then understand **what** exists in the business, and only then decide **how** to express it in software. I think that's the strongest long-term takeaway from everything we've built together.
