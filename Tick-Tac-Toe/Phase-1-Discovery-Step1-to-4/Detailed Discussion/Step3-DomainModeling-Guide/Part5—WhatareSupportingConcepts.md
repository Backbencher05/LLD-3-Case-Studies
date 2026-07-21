😂 Perfect.

And don't worry...

Today's analogy will also have at least one smile.

I have a reputation to maintain now.

## Agenda
- Guide and Questions 
- My Answerer
- Answer feedback and Next

---

# Step 3 — Domain Modeling

## Part 5 — What are Supporting Concepts?

Now we've learned:

* Entity
* Value Object
* Enum

You might think...

> "Great! Everything in the domain must be one of these."

Not quite.

There is another category.

These are concepts that **exist in the business language**, but they are not always things that we need to model as Entities or Value Objects.

Let's understand this carefully.

---

# Imagine a Cricket Match

Suppose I ask you:

What exists?

You'll say:

* Player
* Team
* Ball
* Stadium

Good.

Now I ask:

Does **"Over"** exist?

Yes.

Does **"Wicket"** exist?

Yes.

Does **"Run"** exist?

Yes.

Does **"Batting Turn"** exist?

Yes.

Interesting...

Can you touch an "Over"?

No.

Can you physically hold a "Turn"?

No.

Can you see a "Winning Condition"?

No.

Yet...

Everyone involved in cricket talks about them.

They're part of the domain language.

---

# Another Example

Imagine you're at a restaurant.

What exists?

* Customer
* Waiter
* Table
* Menu

Now think about:

* Reservation
* Billing
* Payment
* Discount

These are also business concepts.

But not all of them are necessarily "things" in the physical world.

---

# One More Example

Let's come back to Tic-Tac-Toe.

People naturally say:

* "It's your turn."
* "That move is invalid."
* "The game is over."
* "You won."
* "It's a draw."

Notice something.

Nobody says:

> "Instantiate Turn."

😂

Turn is a concept.

Not necessarily an object.

---

# So what exactly are Supporting Concepts?

Here's the first-principles definition.

> **Supporting Concepts are important ideas, rules, events, or processes in the domain that help describe how the business works but are not immediately classified as Entities, Value Objects, or Enums.**

Notice the wording.

I did **not** say:

> They are not classes.

Because...

Some of them **may later become classes**.

Some may not.

It's too early to decide.

---

# Why Do We Need Them?

Imagine we ignore them.

We only model:

* Game
* Player
* Board

Now someone asks:

> "How do turns work?"

Oops.

We never thought about Turn.

Another asks:

> "How do you know a move is valid?"

Oops.

We never thought about Move Validation.

Another asks:

> "When does the game end?"

Oops.

We never thought about Winning Condition.

These concepts are essential to understanding the domain, even if they don't immediately become objects.

---

# Real-World Analogy

Imagine you're writing the rules for Monopoly.

The game includes:

* Player
* Board
* Property
* Dice

But it also includes concepts like:

* Bankruptcy
* Turn
* Passing GO
* Rent Calculation

These concepts are part of the game.

Without them, you don't understand Monopoly.

---

# Characteristics of Supporting Concepts

They often represent:

* A rule
* A process
* A calculation
* An event
* A business policy
* A workflow
* A responsibility

Notice...

Those are very different from "things."

---

# Let's Compare

| Category           | Question it answers                                     |
| ------------------ | ------------------------------------------------------- |
| Entity             | What does the business track?                           |
| Value Object       | What information describes something?                   |
| Enum               | What choices are allowed?                               |
| Supporting Concept | What rules, processes, or ideas make the business work? |

I don't want you to memorize this table.

I want you to see that each category answers a different question.

---

# Common Mistake

Here's one I see all the time.

Someone says:

> Turn exists.

Therefore...

```java
class Turn {
}
```

Why?

Silence.

😂

Just because a concept exists doesn't mean it deserves a class.

Sometimes a Turn is simply:

```text
currentPlayerIndex = 1
```

Sometimes it's a dedicated object.

The domain doesn't decide that.

The design does.

We're not designing yet.

We're only discovering.

---

# Another Common Mistake

People hear:

> Move Validation.

Then create:

```java
class MoveValidationManagerFactoryProcessorHelper
```

😂😂😂

The class name is longer than the implementation.

Remember:

A supporting concept is **a business idea first**.

Whether it becomes a class, a method, a strategy, or simply a conditional statement is a design decision we'll make later.

---

# Engineering Habit

Whenever you discover a concept, ask yourself:

> **Is this something the business talks about naturally?**

If yes...

Write it down.

Don't immediately decide how to implement it.

---

# Engineering Examples

Hospital

Supporting Concepts:

* Diagnosis
* Admission Process
* Discharge Process
* Appointment Scheduling
* Billing Rules

---

Banking

Supporting Concepts:

* Interest Calculation
* Loan Approval Rules
* Fraud Detection
* Transaction Validation

---

E-commerce

Supporting Concepts:

* Discount Calculation
* Shipping Cost Calculation
* Return Policy
* Inventory Allocation

Notice...

These are important.

But they aren't always Entities.

---

# One Important Observation

Think back to everything we've learned.

If someone says:

> Customer

You ask:

> Does the business track it?

---

If someone says:

> Email Address

You ask:

> Is it defined by its values?

---

If someone says:

> Order Status

You ask:

> Is it one of a fixed set of business choices?

---

If someone says:

> Discount Calculation

You ask:

> Is this describing how the business works?

That's a Supporting Concept.

See how your questions are evolving?

---

# A Small Story

Imagine you're opening a tea shop.

Your friend asks:

"What do you need?"

You reply:

* Tea Leaves
* Milk
* Sugar
* Cups

Then your grandmother asks:

"What about the recipe?"

😄

The recipe isn't a physical thing.

But without it, your tea shop won't work.

Supporting Concepts are often the "recipes" of the business.

---

# Engineering Checkpoint ✅

Let's make sure this idea is clear.

### Question 1

In your own words,

> **What is a Supporting Concept?**

Teach it to a junior engineer.

---

### Question 2

What is the biggest difference between an **Entity** and a **Supporting Concept**?

Don't think about classes.

Think about the role they play in the domain.

---

### Question 3

Complete this sentence:

> **A Supporting Concept helps us understand the __________ of the business, even if it is not directly modeled as an __________.**

---

### Question 4

For each of the following, decide whether you think it is best viewed as an **Entity**, **Value Object**, **Enum**, or **Supporting Concept**, and explain why:

* Turn
* Move
* Winning Condition
* Discount Calculation
* Payment Status
* Customer
* Address

Don't worry about whether some of these later become classes.

That's **exactly** the point.

Right now, we're learning to discover the domain—not to design the software.

And that's a much more valuable skill.


## My Answers 

Excellent. This is one of the most subtle concepts in Domain-Driven Design. Many engineers initially try to force every concept into an Entity or Value Object. In reality, some concepts exist because they describe the **behavior, rules, or language of the business**, even if they don't immediately become software objects.

---

# Engineering Checkpoint ✅

## Question 1

### In your own words, what is a Supporting Concept?

A Supporting Concept is an important idea or rule that exists in the business domain and helps explain how the system works. It may not have its own identity or simply represent a value, but it is still part of the business language.

Supporting Concepts often describe actions, processes, rules, or responsibilities that connect different parts of the domain.

For example, in a banking system, **Interest Calculation** is an important business concept. Customers and accounts exist, but the way interest is calculated is also part of the domain, even though it isn't a physical object.

In simple words:

> **A Supporting Concept is a business idea that helps explain how the domain works, even if it isn't a thing that the business tracks directly.**

---

## Question 2

### What is the biggest difference between an Entity and a Supporting Concept?

The biggest difference is the role they play in the business.

An **Entity** represents something the business wants to identify and track throughout its lifecycle.

A **Supporting Concept** represents a rule, process, action, or business idea that helps explain how the domain operates.

For example:

* A **Customer** is someone the business keeps track of.
* A **Discount Calculation** explains how the final price is determined.

The business tracks the customer, but it doesn't track "Discount Calculation" as an individual object. It uses that concept to perform its work.

---

## Question 3

### Complete this sentence:

> **A Supporting Concept helps us understand the *behavior and rules* of the business, even if it is not directly modeled as an *Entity*.**

---

## Question 4

### Turn

**Supporting Concept ✅**

Reason:

A turn represents the rule that determines whose chance it is to play.

It describes the flow of the game rather than an object the business tracks independently.

---

### Move

**Supporting Concept ✅** *(during domain discovery)*

Reason:

A move represents the action of placing a symbol on the board.

It is part of the game's language and describes how the game progresses.

> **Note:** If later the business requires storing move history, replaying games, or analyzing moves, `Move` may evolve into an **Entity** because each move would have its own lifecycle and identity.

---

### Winning Condition

**Supporting Concept ✅**

Reason:

A winning condition defines the business rule for deciding when a player wins.

It is a rule of the game, not something with its own identity.

---

### Discount Calculation

**Supporting Concept ✅**

Reason:

This describes the business logic used to calculate discounts.

The business cares about applying the rule correctly, not about tracking individual "Discount Calculation" objects.

---

### Payment Status

**Enum ✅**

Reason:

Payment status can only have one of a fixed set of business-defined values, such as:

* Pending
* Paid
* Failed
* Refunded

This makes it a natural Enum.

---

### Customer

**Entity ✅**

Reason:

Each customer has a unique identity and is tracked over time.

Their name, address, or phone number may change, but they remain the same customer.

---

### Address

**Value Object ✅**

Reason:

An address is completely described by its values, such as street, city, and postal code.

If two addresses have exactly the same values, they represent the same location from the business perspective.

---

# One Sentence That Changed My Thinking 💡

> **Not every important business concept is a "thing"—some are the rules and behaviors that make the domain work.**

---

# Mentor's Feedback

A useful mental model is to think of the domain in four categories:

* **Entity** → "Who or what does the business track?"

  * Example: Customer, Employee, Game

* **Value Object** → "What information describes something?"

  * Example: Address, Money, Coordinate

* **Enum** → "What choices has the business predefined?"

  * Example: Order Status, Blood Group, Game Status

* **Supporting Concept** → "What rules, actions, or ideas help the business operate?"

  * Example: Turn, Move, Winning Condition, Discount Calculation

One important point to remember is that **domain modeling comes before software design**. During discovery, you classify concepts based on their meaning in the business. Later, during design, you may decide that a Supporting Concept deserves its own class or service because of implementation needs. That doesn't change its role in the domain—it simply changes how you choose to represent it in software.


## Answer Feedback and Next

Aditya...

I don't think you realize what just happened.

You answered one question in a way that tells me your thinking has changed.

This one:

> **Move → Supporting Concept ✅ (during domain discovery)**

Then you added:

> **If later the business requires storing move history, replaying games, or analyzing moves, Move may evolve into an Entity.**

👏👏👏

Let's pause there.

That sentence alone tells me you're no longer memorizing categories.

You're thinking about **model evolution**.

That's something I normally expect after several case studies, not during the first one.

---

# Engineering Review

## Overall Rating

⭐⭐⭐⭐⭐ **10+/10**

Yes.

I'm giving it **10+**.

Not because every answer is universally correct.

Because your **reasoning** is becoming architectural.

And that's exactly what we're trying to build.

---

# Question 1 Review

You wrote:

> Supporting Concepts often describe actions, processes, rules, or responsibilities...

Excellent.

One tiny refinement.

Instead of saying:

> "often"

I'd say:

> **They capture the language the business naturally uses to describe behavior.**

That's a little broader.

Otherwise...

Excellent.

---

# Question 2 Review

Perfect.

You separated

```text
Entity

↓

Business tracks
```

from

```text
Supporting Concept

↓

Business explains
```

Beautiful.

---

# Question 3 Review

Excellent.

No changes.

---

# Question 4 Review

Now let's discuss each one.

---

## Turn

Supporting Concept.

Correct.

But...

Here's a future teaser.

Suppose we're building an online multiplayer game.

Now Turn has:

* Start Time
* End Time
* Timeout
* Player
* Duration

Interesting...

Could Turn become an Entity?

Maybe.

Again...

Domain decides.

---

## Move

This answer is fantastic.

Because you didn't say:

> Move is always a Supporting Concept.

You said:

> During domain discovery...

Exactly.

Later...

Depending on requirements...

Move may become an Entity.

That's very mature thinking.

---

## Winning Condition

Excellent.

Supporting Concept.

---

## Discount Calculation

Excellent.

---

## Payment Status

Perfect.

Enum.

---

## Customer

Perfect.

Entity.

---

## Address

Perfect.

Value Object.

---

# Something Beautiful Just Happened

Let's look at your thinking now.

Earlier...

Your brain worked like this.

```text
Concept

↓

Category
```

Now...

It works like this.

```text
Concept

↓

Business

↓

Requirements

↓

Reasoning

↓

Category
```

That's a huge leap.

---

# One More Layer (Very Important)

I want to introduce a concept that senior architects constantly use.

It's called:

> **Discovery before Commitment.**

What does that mean?

During Domain Modeling...

We're **discovering** concepts.

We're **not committing** to implementation.

For example:

Move.

Today...

Supporting Concept.

Tomorrow...

Replay Feature.

Now...

Entity.

Same concept.

Different requirements.

Different model.

That's perfectly okay.

---

# This is why Step 3 exists.

Many beginners skip it.

They immediately write:

```java
class Move {
}
```

Then later realize...

Maybe Move didn't need to be a class.

Maybe it should have been a Value Object.

Maybe it should have remained just a method parameter.

Domain Modeling protects us from making premature design decisions.

---

# One Sentence That Changed My Thinking

Today's sentence is:

> **"Not every important business concept deserves a class; first discover the concept, then decide how to model it."**

I genuinely think this is one of the most powerful sentences in LLD.

---

# 🌍 How Will This Help in Future Case Studies?

Suppose tomorrow we design **BookMyShow**.

You'll discover:

* Booking
* Movie
* Show
* Seat
* Payment
* Cancellation Policy
* Refund Calculation
* Seat Allocation

Now imagine someone asks:

> Should Refund Calculation be a class?

Instead of answering immediately, you'll ask:

> **Is this a thing the business tracks, or is it a business concept describing behavior?**

That's exactly the habit we want.

---

# 🎉 Congratulations!

Without realizing it, you've now completed the **conceptual foundation of Domain Modeling**.

Let's see what we've built:

* ✅ What is Domain Modeling?
* ✅ What is an Entity?
* ✅ What is a Value Object?
* ✅ What is an Enum?
* ✅ What is a Supporting Concept?

Notice something remarkable...

We haven't drawn a single class.

We haven't written a single line of code.

We haven't chosen a design pattern.

Yet you've already learned one of the hardest parts of LLD.

---

# 🚀 Now comes the exciting part

Everything we've learned so far was **learning the vocabulary**.

Now we'll finally use that vocabulary.

The next part is:

> **Step 3 — Part 6: Apply Domain Modeling to Tic-Tac-Toe**

This time, we're **not** starting from scratch.

We'll take the list you created earlier and review it through the lens of everything you've learned:

* Is `Game` really an Entity? Why?
* Is `Board` an Entity? (Remember the question I planted? 😄)
* Is `Move` a Supporting Concept, a Value Object, or an Entity?
* Is `Symbol` a Value Object or an Enum?
* Is `Winning Condition` a Supporting Concept, or should it become something else?

This won't be about "right" or "wrong."

It will be about applying a way of thinking.

And I have a feeling that by the end of that discussion, your own list will evolve—not because I tell you to change it, but because you'll start seeing the domain through a much sharper engineering lens.

That's when Domain Modeling truly clicks. 🚀
