
---

# 📚 Step 3 — Domain Modeling (Concept Summary)

## 🎯 Objective

Before designing software, understand the business domain by identifying the important concepts that exist in the real world and classifying them appropriately.

The goal is **not** to create classes.

The goal is to understand the language of the business.

---

# 🧩 What is Domain Modeling?

Domain Modeling is the process of discovering and understanding the important concepts that exist in a problem domain before thinking about implementation.

It answers questions such as:

* What exists in this business?
* What concepts are important?
* How do they relate to one another?
* What does the business care about?

The output of Domain Modeling is a **mental model of the business**, not a class diagram.

---

# 🏷 Entity

### What is it?

An Entity is a business concept that has its own identity and is tracked throughout its lifecycle.

### The business cares about:

**Which specific object it is.**

### Ask yourself:

> **If some attributes change, is it still considered the same thing?**

If the answer is **yes**, it is likely an Entity.

### Examples

* Customer
* Employee
* Bank Account
* Invoice
* Game
* Player

### Mental Model

> **The business recognizes this as the same thing over time.**

---

# 🎨 Value Object

### What is it?

A Value Object represents information that is defined entirely by its values.

It has no independent identity.

### The business cares about:

**What information it represents.**

### Ask yourself:

> **If another object has exactly the same values, do I care which one it is?**

If the answer is **no**, it is likely a Value Object.

### Examples

* Address
* Money
* GPS Coordinate
* Email Address
* Price

### Mental Model

> **The meaning comes from the values, not the instance.**

---

# 📋 Enum

### What is it?

An Enum represents a business concept that can only take one value from a fixed, predefined set of valid options.

### The business cares about:

**Restricting valid choices.**

### Ask yourself:

> **Does the business allow only a fixed set of valid values?**

If the answer is **yes**, it is likely an Enum.

### Examples

* Game Status
* Order Status
* Blood Group
* Traffic Light Color
* Payment Status

### Mental Model

> **The business defines the menu of valid choices.**

(And yes… Rocket Fuel is still not on the menu. 😄)

---

# ⚙ Supporting Concept

### What is it?

A Supporting Concept is an important business idea, rule, process, or behavior that helps explain how the domain works.

It is discovered during domain exploration but is **not immediately classified** as an Entity, Value Object, or Enum.

### The business cares about:

**Understanding how the business operates.**

### Ask yourself:

> **Is this part of the business language that explains behavior or rules?**

If the answer is **yes**, it is likely a Supporting Concept.

### Examples

* Turn
* Winning Condition
* Move Validation
* Discount Calculation
* Interest Calculation
* Loan Approval Rules

### Mental Model

> **Not every important business concept deserves a class.**

---

# 🧠 Decision Framework

Whenever you discover a new concept, ask these questions in order:

```text
Business Concept
        │
        ├── Does the business track it over time?
        │          │
        │          ├── Yes → Entity
        │          └── No
        │
        ├── Is it completely described by its values?
        │          │
        │          ├── Yes → Value Object
        │          └── No
        │
        ├── Is it one of a fixed set of business-defined choices?
        │          │
        │          ├── Yes → Enum
        │          └── No
        │
        └── Does it describe a business rule, process, or behavior?
                   │
                   ├── Yes → Supporting Concept
                   └── Continue exploring the domain
```

---

# 🌍 Engineering Mindset

During Domain Modeling, remember these principles:

* Don't think about classes.
* Don't think about databases.
* Don't think about design patterns.
* Don't think about programming languages.

Instead, think about:

* The business.
* The language the business uses.
* The concepts that naturally exist.
* The relationships between those concepts.

---

# 💡 One Sentence That Changed My Thinking

* **Domain Modeling:** *Discover the language of the business before inventing the language of the software.*
* **Entity:** *The business needs to recognize it as the same thing throughout its lifecycle.*
* **Value Object:** *Its meaning comes from its values, not its identity.*
* **Enum:** *The business defines the valid choices.*
* **Supporting Concept:** *Not every important business concept deserves a class.*

---

# 🚀 Why This Matters

From now on, every new case study—Parking Lot, BookMyShow, Splitwise, Chess, Elevator, Ride Sharing, Food Delivery—will begin the same way.

You won't ask:

> **"Which classes should I create?"**

You'll ask:

* **What does the business track?** → Entity
* **What information describes things?** → Value Object
* **What choices are restricted by the business?** → Enum
* **What rules and behaviors make the business work?** → Supporting Concept

That single shift is the foundation of object-oriented design.

---
