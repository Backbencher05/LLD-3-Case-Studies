Awesome.

Now we're entering one of the most important concepts in software design.

I don't want you to think of this as:

> "Today we'll learn Entities."

Instead think of it as:

> **"Today we'll learn how software recognizes identity."**

That is the real topic.

---

# Step 3 — Domain Modeling

## Part 2 — What is an Entity?

Let's start with a story.

---

# Imagine a Classroom

There are 40 students.

One student is named **Rahul**.

Now suppose Rahul changes his hairstyle.

Is he still Rahul?

**Yes.**

Now suppose Rahul changes his T-shirt.

Still Rahul?

**Yes.**

Now suppose Rahul scores higher in exams.

Still Rahul?

**Yes.**

Many things changed.

But one thing didn't.

His **identity**.

---

Now imagine another student also named Rahul joins the class.

Do we now have one Rahul?

No.

We have two different people with the same name.

Why?

Because identity is not the name.

---

# Another Example

Think about your own bank account.

Your balance changes.

Today:

₹10,000

Tomorrow:

₹25,000

Next month:

₹5,000

Did your bank account become a different account?

No.

The **state** changed.

The **identity** remained the same.

---

# One More Example

Imagine your car.

You repaint it.

Still your car.

Replace the tires.

Still your car.

Install a new music system.

Still your car.

The properties changed.

Its identity didn't.

---

# So what is an Entity?

Here's the first-principles definition.

> **An Entity is a domain concept that has its own identity and continues to be the same entity even when some of its attributes change over time.**

Notice what the definition does **not** say.

It does **not** say:

* class
* object
* database table
* primary key

Those are implementation details.

An Entity exists **before** software.

---

# Identity vs State

This is the heart of today's lesson.

Every Entity has two things:

## 1. Identity

Who is this?

Example:

* Employee ID
* Account Number
* Vehicle Registration Number
* Game ID

Identity answers:

> **Which one is this?**

---

## 2. State

What does it currently look like?

Example:

Employee

State changes:

* Salary
* Department
* Address
* Phone Number

Identity remains:

Employee #101

---

Let's compare.

| Entity       | Identity            | State                          |
| ------------ | ------------------- | ------------------------------ |
| Student      | Student ID          | Name, Marks, Address           |
| Bank Account | Account Number      | Balance, Status                |
| Car          | Registration Number | Color, Mileage                 |
| Game         | Game ID             | Current State, Players, Winner |

State changes.

Identity remains.

---

# Real-World Analogy

Imagine a passport.

The passport number uniquely identifies it.

Inside,

your address changes.

Your appearance changes.

Your marital status changes.

Yet it's still the same passport.

That's identity.

---

# Why Do We Need Entities?

Imagine we didn't think about identity.

Suppose two players have the same name.

```
Player
Name = Aditya
```

Another player

```
Player
Name = Aditya
```

Which one is playing?

We don't know.

Identity solves this problem.

---

# How to Identify an Entity

This is the question I ask myself.

> **"If some properties change, is it still the same thing?"**

Let's test.

## Example 1

A Player changes name.

Still the same player?

Yes.

Entity.

---

## Example 2

A Board gets larger.

Still the same board?

Depends on the domain.

Interesting.

We'll discuss this later.

---

## Example 3

A Game progresses.

Moves increase.

Winner changes.

Game status changes.

Still the same game?

Yes.

Entity.

---

# Common Mistake

Many beginners think:

> Everything becomes an Entity.

No.

Imagine:

```
Position
(1,2)
```

Tomorrow:

```
(2,1)
```

Is that the same position?

No.

There isn't an ongoing identity we're tracking.

We'll later see that this is probably a **Value Object**, not an Entity.

This distinction is one of the foundations of good domain modeling.

---

# Another Common Mistake

People often say:

> If it has an ID, it's an Entity.

Not necessarily.

Adding an ID to everything doesn't magically make it an Entity.

Identity comes from the **business/domain**, not from the database.

For example:

```
Color
```

Giving Color an ID doesn't mean Color suddenly becomes an Entity.

The business still treats it as just a value.

---

# Engineering Perspective

When you're modeling software, ask yourself:

> **"Does the business care about tracking this specific thing over time?"**

If the answer is yes,

it's a strong candidate for an Entity.

If not,

it might be something else.

---

# One Engineering Habit

From today onward, every time we discover a concept in a problem, ask yourself two questions:

### Question 1

Does this thing have its own identity?

---

### Question 2

If some attributes change, is it still considered the same thing?

If both answers are **yes**,

you're probably looking at an Entity.

---

# Engineering Examples

Let's practice without Tic-Tac-Toe.

### Hospital

Possible Entities?

* Patient
* Doctor
* Appointment
* Prescription

Why?

Because the hospital tracks each one individually over time.

---

### Banking

Possible Entities?

* Customer
* Account
* Loan
* Card

Again,

the bank cares about each specific one.

---

### E-commerce

Possible Entities?

* Customer
* Order
* Product
* Shopping Cart

Each has its own lifecycle.

---

# Engineering Checkpoint ✅

Don't think about Tic-Tac-Toe yet.

Let's first make sure the concept is clear.

Answer these four questions in your own words.

### Question 1

What is an Entity?

Don't repeat my definition.

Teach it to a junior engineer.

---

### Question 2

What is the difference between **Identity** and **State**?

Use your own example.

---

### Question 3

Complete this sentence:

> **An Entity is tracked because the business cares about its __________, not just its __________.**

---

### Question 4

For each of the following, tell me whether you think it's an Entity and **why**:

* Student
* Bank Account
* Color
* Passport
* Invoice
* Temperature

Don't worry about being right.

Explain your reasoning.

---

We'll stay here until the concept becomes intuitive.

Only then will we return to your Tic-Tac-Toe list and decide which of your identified concepts are actually Entities—and, more importantly, *why*. That's the skill that will transfer to every future case study.


## My Answers

Excellent. These questions test whether you've understood the **concept of an Entity**, not whether you've memorized a definition. Below are answers written in the style I'd expect from a strong software engineering student.

---

# Engineering Checkpoint ✅

## Question 1

### What is an Entity?

An Entity is a real-world object or concept that has its own unique identity and can be distinguished from other objects, even if its properties change over time.

The business cares about **which specific object it is**, not just the values it currently holds.

For example, a student may change their name, address, or phone number, but they are still the same student because their identity (such as Student ID) remains the same.

In simple words:

> **An Entity is something the business needs to identify and track throughout its lifecycle.**

---

## Question 2

### What is the difference between Identity and State?

**Identity** tells us *who or what the object is*.

**State** tells us *what the object currently looks like or what information it currently has*.

### Example

Consider a **Bank Account**.

**Identity:**

* Account Number: `123456789`

This never changes because it uniquely identifies the account.

**State:**

* Balance: ₹10,000
* Status: Active
* Account Holder Address: Bangalore

These values can change over time.

Even if the balance changes from ₹10,000 to ₹50,000, it is still the same bank account because its identity has not changed.

So,

* **Identity remains constant.**
* **State can change throughout the object's lifetime.**

---

## Question 3

### Complete this sentence:

> **An Entity is tracked because the business cares about its *identity*, not just its *state*.**

---

## Question 4

### Student

**Entity ✅**

Reason:

Every student has a unique identity (Student ID or Roll Number).

Even if the student's name, address, or grades change, the student remains the same person in the system.

---

### Bank Account

**Entity ✅**

Reason:

Every bank account has a unique account number.

Its balance, account type, or status may change, but the account itself remains the same.

---

### Color

**Not an Entity ❌**

Reason:

A color has no identity.

If two objects are both "Red," there is no need to distinguish one "Red" from another. The business only cares about the value "Red," not a unique instance of it.

This makes it a better fit as a **Value Object**.

---

### Passport

**Entity ✅**

Reason:

Each passport has a unique passport number.

Its owner's address or expiration date may change (through renewal or updates, depending on the system), but the passport is still identified by its unique identity while it exists.

---

### Invoice

**Entity ✅**

Reason:

Every invoice has a unique invoice number.

Its payment status may change from Pending to Paid, but it is still the same invoice that the business continues to track.

---

### Temperature

**Not an Entity ❌**

Reason:

Temperature is simply a measurement or value.

If two sensors both read **25°C**, there is no identity that distinguishes one "25°C" from another. The business only cares about the measured value.

This is also better represented as a **Value Object**.

---

# One Sentence That Changed My Thinking 💡

> **An Entity is not defined by what it contains today, but by who it continues to be tomorrow.**

---

# Mentor's Feedback

There's a simple question you can ask whenever you're unsure whether something is an Entity:

> **"If two objects have exactly the same data, does the business still need to distinguish between them?"**

* If **yes**, you're probably looking at an **Entity**.
* If **no**, you're probably looking at a **Value Object**.

For example:

* Two students named "Rahul" with the same age are still different students because they have different identities.
* Two coordinates `(2, 3)` are simply the same coordinate; there's no reason to distinguish one from the other.

This single question will help you identify Entities correctly in most domain-modeling problems.



## Answers feedback on Entity 
Aditya...

This is another milestone.

I'm going to say something that I don't say often during teaching:

> **I don't think you're "learning Entities" anymore. I think you've understood the concept.**

There's a big difference.

If I change the domain tomorrow to:

* Flight Booking
* Uber
* Chess
* WhatsApp
* Hospital

I think you'll still be able to identify Entities.

That tells me you've learned the principle, not the example.

---

# Engineering Review

## Overall Rating

⭐⭐⭐⭐⭐ **10/10**

This is exactly the kind of understanding we're aiming for.

Now let's review it like a Staff Engineer.

---

# Question 1 Review

You wrote:

> **An Entity is something the business needs to identify and track throughout its lifecycle.**

👏

This is actually my favorite sentence in your answer.

Why?

Because you've unconsciously introduced another important concept:

> **Lifecycle**

We never explicitly discussed lifecycle.

Yet you naturally included it.

That's a very good sign.

Entities usually live through a lifecycle.

Example:

Invoice

```text
Created

↓

Sent

↓

Pending

↓

Paid

↓

Archived
```

Still the same Invoice.

Excellent.

---

# Question 2 Review

Excellent.

I especially liked this sentence.

> Identity remains constant.
>
> State can change.

That's exactly the mental model.

---

# Small refinement

Technically...

Identity doesn't always have to be **constant** in implementation.

For example,

Some businesses allow changing employee IDs.

Some systems regenerate IDs.

But...

From the **business perspective**,

the business still knows

> "This is the same employee."

So I'd slightly refine it.

Instead of

> Identity remains constant.

I'd say

> **The business continues to recognize it as the same thing.**

That's a subtle distinction.

Don't worry too much about it now.

---

# Question 3 Review

Perfect.

No changes.

---

# Question 4 Review

Excellent.

Let's go through them.

---

### Student

Correct.

Entity.

---

### Bank Account

Correct.

Entity.

---

### Color

Excellent reasoning.

You didn't say

> It doesn't have an ID.

You said

> The business doesn't care about distinguishing one Red from another.

That's exactly how domain modeling works.

---

### Passport

Correct.

One interesting observation.

You said

> Expiry date changes.

Actually...

Many countries issue a **new passport** instead of modifying the old one.

This is a fantastic example of why **domain matters**.

The business rules define identity.

Not us.

---

### Invoice

Excellent.

Payment Status changes.

Invoice remains.

Classic Entity.

---

### Temperature

Excellent.

This answer tells me you've started separating

```text
Identity

vs

Value
```

Without me teaching Value Objects yet.

That's really encouraging.

---

# One More Layer

Now I want to introduce something that senior engineers constantly think about.

Remember this question:

> **"What does the business track?"**

Let's test it.

Suppose you're building software for Amazon.

Customer

Tracked?

Yes.

Entity.

---

Order

Tracked?

Yes.

Entity.

---

Shopping Cart

Tracked?

Maybe.

Depends on the business.

Interesting.

---

Discount Percentage

Tracked?

No.

Just a value.

---

See what's happening?

We're asking:

> **What matters to the business?**

That's how domain modeling works.

---

# The Biggest Mistake Beginners Make

I want to warn you about something now.

Many beginners think:

```text
Database Table

↓

Entity
```

Wrong.

Suppose I have:

```sql
Colors
------
ID
Name
```

Because the database has an ID...

Does Color become an Entity?

No.

The business still treats it as a value.

The database doesn't define the domain.

The domain defines the software.

This is an incredibly important principle.

---

# Something I Want You to Remember Forever

I think today's mental model is even stronger than yesterday's.

## 💡 One Sentence That Changed My Thinking

> **"An Entity is not important because it has an ID; it is important because the business needs to recognize it as the same thing throughout its lifecycle."**

Notice how different this is from:

> "Entity has ID."

One is engineering.

The other is memorization.

---

# Engineering Habit

From now onward, every time you discover something in a case study, ask yourself:

```text
Does the business track this?

↓

YES

↓

Probably an Entity.
```

Don't ask:

```text
Can I make this a class?
```

That's a completely different question.

---

# One Small Challenge

Before we move to **Value Objects**, I want to stretch your thinking just a little.

Don't answer now—just think about it.

Suppose we have:

* Chess
* Tic-Tac-Toe
* Snake & Ladder

All of them have a **Board**.

Is **Board** always an Entity?

Or...

Can the answer change depending on the business?

That's not a trick question.

It's a preview of something we'll explore later: **the same concept can be modeled differently depending on the domain and requirements**.

---

## Where we are now

We have completed:

* ✅ What is Domain Modeling?
* ✅ What is an Entity?

And we haven't written a single class.

That's intentional.

Because when we finally return to your Tic-Tac-Toe domain model, you won't be guessing—you'll be reasoning.

And that's the mindset we're building.
