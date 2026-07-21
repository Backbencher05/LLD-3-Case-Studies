## Part 3 — What is a Value Object?

😊 That reaction is exactly what I was hoping for.

You didn't immediately answer.

You said:

> **"I have to think..."**

That means your brain is no longer looking for memorized rules.

It's reasoning.

That's the biggest shift we've made so far.

---

Before we move ahead, let me tell you something.

That **Board** question...

We're **not** going to answer it today.

I'm deliberately planting these questions in your mind.

Why?

Because when we later discuss **Aggregates**, **Composition**, and **Bounded Contexts**, you'll suddenly remember:

> "Oh... that's why you asked whether Board is always an Entity."

Good mentors don't just answer questions.

Sometimes they plant questions that become meaningful later.

---

# Step 3 — Domain Modeling

## Part 3 — What is a Value Object?

Today we're going to learn something that even experienced developers often misunderstand.

---

# Let's start with a story.

Imagine I give you two ₹500 notes.

Both are worth ₹500.

From your perspective,

do you care **which** ₹500 note I give you?

Probably not.

You only care that its **value** is ₹500.

Now imagine I give you your passport.

Would you say:

> "Any passport is fine."

Of course not.

You want **your** passport.

Why?

Because the passport has identity.

The ₹500 note, in this example, is interchangeable based on its value.

That's the first hint.

---

# Another Example

Suppose you order a pizza.

The restaurant asks:

> What size?

You say:

> Large.

Now imagine another customer also orders:

> Large.

Are those two "Large" sizes different?

No.

"Large" is just a value.

Nobody tracks the lifecycle of "Large."

---

# One More Example

Imagine you're entering an address.

```text
City: Bangalore
State: Karnataka
Country: India
```

Now another customer enters exactly the same address.

Should the software care which "Bangalore" this is?

No.

If all the values are equal,

they represent the same thing.

---

# So what exactly is a Value Object?

Here's the first-principles definition.

> **A Value Object is a domain concept that is defined entirely by its values and has no independent identity.**

Notice the contrast.

Entity

↓

Identity first.

Value second.

---

Value Object

↓

Value first.

Identity doesn't matter.

---

# Let's compare.

Suppose we have:

Two students.

```text
Student A

Student ID = 101
Name = Rahul
```

```text
Student B

Student ID = 102
Name = Rahul
```

Same name.

Different students.

Identity matters.

Entity.

---

Now imagine coordinates.

```text
(2,3)
```

Another coordinate.

```text
(2,3)
```

Are they different?

No.

They're equal because their values are equal.

That's a Value Object.

---

# Identity vs Equality

This is the biggest difference.

Entities compare by **identity**.

Value Objects compare by **value**.

Let's see an example.

---

### Entity

Employee

```text
Employee #101
```

Another Employee

```text
Employee #101
```

Even if the name changes,

it's still the same employee.

---

### Value Object

Position

```text
Row = 2
Column = 1
```

Another Position

```text
Row = 2
Column = 1
```

Exactly the same.

There is no reason to distinguish them.

---

# Real-World Analogy

Imagine a recipe.

It says:

> Add **5 grams of salt**.

Do you care which specific "5 grams of salt" you used?

No.

Any 5 grams is fine.

Salt, in that context, behaves like a value.

---

Now imagine a chef.

Can you replace Chef A with Chef B just because they have the same age?

No.

Identity matters.

---

# Why Do We Need Value Objects?

Imagine every coordinate became an Entity.

```text
Position #1001

Row = 2

Column = 3
```

Then another one.

```text
Position #1002

Row = 2

Column = 3
```

Now you have two different objects representing exactly the same position.

That creates unnecessary complexity.

Instead, we simply compare the values.

---

# Characteristics of a Value Object

Most Value Objects have these characteristics:

* No identity.
* Defined entirely by their values.
* Usually immutable (we'll discuss immutability later).
* Equality is based on values, not identity.
* Often reused.

Notice I said **usually** immutable.

We'll learn *why* in a later lesson.

---

# Entity vs Value Object

| Entity               | Value Object                           |
| -------------------- | -------------------------------------- |
| Has identity         | No identity                            |
| Identity matters     | Values matter                          |
| Has lifecycle        | Usually no independent lifecycle       |
| Compared by identity | Compared by value                      |
| Business tracks it   | Business uses it to describe something |

Don't memorize this table.

Understand the reasoning behind it.

---

# Common Mistake

Many beginners think:

> Small object = Value Object.

Wrong.

Size has nothing to do with it.

A huge object can still be a Value Object.

A tiny object can be an Entity.

The deciding factor is:

> **Does identity matter to the business?**

---

# Another Common Mistake

People often say:

> If it has multiple fields, it must be an Entity.

No.

Example:

Address

```text
Street

City

State

Country

ZIP
```

Many fields.

Still often modeled as a Value Object.

Because we care about the values, not the identity of the address object itself.

---

# Engineering Habit

Whenever you discover something, ask:

> **If another object has exactly the same values, do I care which one it is?**

If the answer is:

> No.

It's probably a Value Object.

---

# Engineering Examples

Hospital

Possible Value Objects:

* Blood Group
* Address
* Temperature
* Weight
* Height

---

Banking

Possible Value Objects:

* Money (depending on the domain)
* Currency
* Interest Rate
* Address

---

E-commerce

Possible Value Objects:

* Price
* Dimension
* Weight
* Color

Again...

These depend on the domain.

---

# Engineering Checkpoint ✅

Don't think about Tic-Tac-Toe yet.

Let's first understand Value Objects.

### Question 1

In your own words,

> **What is a Value Object?**

Teach it to a junior engineer.

---

### Question 2

What is the biggest difference between an Entity and a Value Object?

Don't say:

> One has ID.

Think deeper.

---

### Question 3

Complete this sentence:

> **A Value Object is compared by its __________, whereas an Entity is compared by its __________.**

---

### Question 4

For each of the following, tell me whether you think it's an **Entity** or a **Value Object**, and explain why.

* Address
* Money
* Email Address
* Employee
* GPS Coordinate
* Product Price

Take your time.

And one last thing...

Do you remember the sentence that changed your thinking about Entities?

> **"The business needs to recognize it as the same thing throughout its lifecycle."**

Here's today's sentence—but don't accept it yet. See if your own answers lead you to the same conclusion.

> **"A Value Object isn't important because of *which one it is*; it's important because of *what value it represents*."**

Let's see whether your own reasoning arrives there naturally. That's much more valuable than memorizing it.

----------------------------------------------------------------------
## My Answers 
------------------------------------------------------------------------
Excellent. This checkpoint is where many engineers start to truly understand **Domain-Driven Design (DDD)**. The goal is to move beyond thinking "Entity has an ID" and instead understand *why* Entities and Value Objects exist.

---

# Engineering Checkpoint ✅

## Question 1

### In your own words, what is a Value Object?

A Value Object is a concept that represents a characteristic, measurement, or description of something. It doesn't have its own identity because the business doesn't need to track it individually.

What matters is **the value it represents**, not which particular instance it is.

For example, two GPS coordinates with the values `(12.9716, 77.5946)` represent the exact same location. The business has no reason to distinguish one from the other because they mean the same thing.

In simple words:

> **A Value Object is something whose meaning comes entirely from its values, not from its identity.**

---

## Question 2

### What is the biggest difference between an Entity and a Value Object?

The biggest difference is **what the business cares about**.

For an **Entity**, the business wants to keep track of the same object throughout its lifetime, even if its properties change.

For a **Value Object**, the business only cares about the information it represents. If another object has the same values, it is considered the same from the business perspective.

In other words:

* **Entities represent "who or what" something is.**
* **Value Objects represent "what information" something carries.**

---

## Question 3

### Complete this sentence:

> **A Value Object is compared by its *values*, whereas an Entity is compared by its *identity*.**

---

## Question 4

### Address

**Value Object ✅**

Reason:

An address describes a location. If two addresses contain exactly the same street, city, state, and postal code, they represent the same place.

The business usually doesn't care about distinguishing one identical address object from another.

---

### Money

**Value Object ✅**

Reason:

Money is defined by its amount and currency.

For example:

* ₹500
* USD 100

Two Money objects with the same amount and currency are considered equal because they represent the same value.

---

### Email Address

**Value Object ✅**

Reason:

An email address is simply a way to identify a communication address.

If two email address objects contain `abc@example.com`, they represent the same email.

The business cares about the email value, not a unique email object.

---

### Employee

**Entity ✅**

Reason:

Every employee has an identity, such as an Employee ID.

An employee's name, department, salary, or address may change over time, but the employee remains the same person in the organization.

---

### GPS Coordinate

**Value Object ✅**

Reason:

A GPS coordinate is completely described by its latitude and longitude.

For example:

```
Latitude: 12.9716
Longitude: 77.5946
```

If another coordinate has the same values, they represent the same location.

There is no need to distinguish between them.

---

### Product Price

**Value Object ✅**

Reason:

A product price is simply a value, such as:

* ₹999
* USD 49.99

If two products have the same price, the price itself is considered equal because it represents the same monetary value.

The product is an Entity, but its price is a Value Object.

---

# One Sentence That Changed My Thinking 💡

> **An Entity answers "Who is it?", while a Value Object answers "What is it?"**

---

# Mentor's Feedback

A useful way to identify a Value Object is to ask:

> **"If I create another object with exactly the same values, would the business care that it's a different instance?"**

* If the answer is **No**, it's likely a **Value Object**.
* If the answer is **Yes**, it's likely an **Entity**.

For example:

* Two `Money(₹500)` objects are effectively the same because they represent the same amount.
* Two employees named "Aditya" are not the same employee, even if all their details match, because the business tracks each employee individually.

This mindset shift is more important than memorizing definitions. Once you start asking **what the business cares about**, identifying Entities and Value Objects becomes much more intuitive.


# Answers Feedbacks and Next 

Aditya...

I think we're reaching a point where I need to change **how** I mentor you.

Earlier, I had to explain a concept and then correct your understanding.

Now I'm noticing something different.

You're beginning to **derive the concepts yourself**.

That means my role is slowly shifting from **teacher** to **reviewer**.

That's a very good sign.

---

# Engineering Review

## Overall Rating

⭐⭐⭐⭐⭐ **10/10**

Again, not because everything is universally true in every domain.

But because your **reasoning process** is correct.

And engineering is mostly about reasoning.

---

# Question 1 Review

You wrote:

> **A Value Object is a concept that represents a characteristic, measurement, or description of something.**

Excellent.

Then you wrote

> **It doesn't have its own identity because the business doesn't need to track it individually.**

This is the key.

Notice...

You're no longer saying

> "It doesn't have an ID."

You're saying

> **"The business doesn't care."**

That's exactly how Domain-Driven Design thinks.

---

# Question 2 Review

I really liked this sentence.

> **The biggest difference is what the business cares about.**

👏

That is much deeper than

> Entity has ID.

Value Object doesn't.

---

Then you wrote

> Entities represent **who or what** something is.

> Value Objects represent **what information** something carries.

That's a beautiful mental model.

I'm stealing that sentence for future students. 😊

---

# Question 3 Review

Perfect.

No changes.

---

# Question 4 Review

Let's go through them.

---

## Address

You wrote

Value Object.

Correct.

But...

Here's our first interesting discussion.

Imagine you're building:

📍 Google Maps.

Now imagine an Address has:

* Reviews
* Owner
* Popularity
* Visit Count
* Photos

Suddenly...

The business starts tracking that Address.

Could Address become an Entity?

Yes.

Same word.

Different domain.

Different modeling.

This is why I keep saying:

> **The business decides.**

Not us.

---

## Money

Excellent.

This is actually one of the classic Value Object examples in Domain-Driven Design.

---

## Email Address

Excellent.

Again...

In most domains...

Value Object.

---

## Employee

Perfect.

---

## GPS Coordinate

Perfect.

---

## Product Price

Excellent.

I especially liked:

> The Product is an Entity.

The Price is a Value Object.

Exactly.

---

# One Layer Deeper

Now I want to introduce another idea.

Suppose we have

```text
Money

Amount = 100

Currency = INR
```

Tomorrow,

someone changes it.

```text
Amount = 200
```

Question.

Did the Money object change?

Or...

Did we create a new Money value?

Interesting...

This is why Value Objects are usually immutable.

We'll study immutability later.

I'm only planting the question today.

---

# One Important Engineering Principle

Today we've discovered something huge.

Look at this.

Student

↓

Entity

---

Address

↓

Value Object

---

Employee

↓

Entity

---

Price

↓

Value Object

---

Now imagine:

Employee

contains

Address

```text
Employee
    |
    +---- Address
```

Suddenly...

Software starts looking exactly like reality.

Why?

Because we're modeling the domain.

Not inventing classes.

---

# The Biggest Mistake Beginners Make

I want to show you something.

Imagine someone writes

```java
class Address {

    int id;

    String city;

}
```

Then says

> It's an Entity.

Why?

> Because it has an ID.

Wrong.

The ID came from the database.

The domain didn't ask for it.

Never let the database design your domain model.

The domain should design the database.

This principle will save you countless design mistakes.

---

# One Sentence That Changed My Thinking

Today's sentence is:

> **"A Value Object isn't important because of which instance it is; it's important because of the meaning carried by its values."**

Notice how this perfectly complements yesterday's Entity sentence.

Entity

↓

Who is it?

---

Value Object

↓

What does it represent?

---

# Now Something Beautiful Happens

Let's combine both concepts.

Imagine this.

```text
Employee
-------------------
Employee ID

Name

Salary

Address
```

Question.

What is Employee?

Entity.

---

What is Address?

Value Object.

---

Now software starts resembling reality.

This...

is Domain Modeling.

---

# Here's something I want to tell you

Do you remember the Machine Learning journey?

Every few days I'd say

> "This is one of the most important concepts."

You used to laugh. 😄

I think the same thing is happening here.

But this time...

It really is true.

Because once you deeply understand:

* Domain
* Entity
* Value Object

The rest of Object-Oriented Design starts making much more sense.

Responsibilities become clearer.

Relationships become clearer.

Class diagrams become simpler.

Design patterns become easier to justify.

---

# One Small Challenge (Don't answer now)

Imagine we have:

```text
Chess Piece
```

Is it

Entity

or

Value Object?

Most people immediately answer.

I don't want you to.

Just think about it.

Because, just like the Board question, the answer depends on the domain and what the business needs to track.

That's a glimpse of the kind of nuanced thinking we'll continue to develop.

---

# Before we move ahead...

I want to make one small improvement to our learning process.

Until now, we've had:

* What is it?
* Why do we need it?
* Problem it solves.
* Engineering Checkpoint.
* Mentor Review.
* One Sentence That Changed My Thinking.

I'd like to add one more permanent section after every concept:

## 🌍 "How will this help me in future case studies?"

For today's concept:

When you work on **Parking Lot**, **BookMyShow**, **Splitwise**, or **Elevator**, don't ask:

> "Which classes should I create?"

Instead ask:

* Which concepts does the business track over time? → **Entity**
* Which concepts simply describe information? → **Value Object**

That single shift in questioning will make domain modeling much more natural, no matter what problem you're solving.

I think this addition will help you see each concept not as something tied to Tic-Tac-Toe, but as a reusable way of thinking that carries forward into every future design problem.
