
---

# 🎤 Interview Thinking — Step 6

Now let's prepare for interviews.

Remember our goal isn't to memorise answers.

It's to demonstrate how an engineer reasons.

---

## Interview Question 1

**Why do objects collaborate?**

### Expected Engineering Thinking

Objects collaborate because no single object naturally owns all the knowledge required to complete a business event.

Each object contributes the responsibility it uniquely owns, allowing the system to remain cohesive while solving a larger business problem.

---

## Interview Question 2

**Why shouldn't one object perform all responsibilities?**

### Expected Engineering Thinking

Doing so creates a God Object.

It accumulates unrelated responsibilities, increases coupling, becomes harder to understand, harder to test, and more difficult to evolve.

Instead, each responsibility should remain with the object that naturally owns the required knowledge.

---

## Interview Question 3

**What is the role of a coordinator?**

### Expected Engineering Thinking

A coordinator manages the business workflow.

It decides what should happen next but delegates specialised work to the appropriate collaborators.

Coordination is about sequencing, not execution.

---

## Interview Question 4

**What makes a good message between objects?**

### Expected Engineering Thinking

A good message communicates intent and provides only the information necessary for the receiver to fulfil its responsibility.

Sending unnecessary information increases coupling and exposes internal knowledge.

---

## Interview Question 5

**Why are contracts important?**

### Expected Engineering Thinking

Contracts allow collaborators to depend on expected outcomes rather than implementation details.

As long as the promised behaviour remains unchanged, objects can evolve internally without forcing changes across the system.

---

## Interview Question 6

**What is the relationship between responsibility and collaboration?**

### Expected Engineering Thinking

Responsibilities identify ownership.

Collaboration combines those responsibilities to complete a business event.

Without responsibility, collaboration is random.

Without collaboration, responsibilities remain isolated.

---

## Interview Question 7

**How would you explain Step 6 to a junior engineer?**

### Expected Engineering Thinking

I would explain that Step 6 is about turning isolated responsibilities into a working system.

Objects don't collaborate because programming languages allow method calls.

They collaborate because business problems require specialised knowledge distributed across multiple responsible objects.

---

# 💡 Interview Trap to Avoid

Many candidates answer collaboration questions like this:

> "Object A calls Object B."

That describes **mechanics**.

Interviewers usually want the **reason**.

A stronger answer is:

> "Object A collaborates with Object B because Object B owns the knowledge required to fulfil the next part of the business process."

That's the difference between describing code and explaining design.

---

# 🏆 Engineering Checkpoint — Step 6

Before moving to Step 7, ask yourself these questions.

If you can answer them naturally, you're ready.

* Can I identify the business event before thinking about classes?
* Can I explain why each object participates?
* Can I distinguish coordination from execution?
* Can I decide what information should travel?
* Can I identify unnecessary information?
* Can I describe collaboration as business reasoning instead of method calls?
* Can I explain why contracts allow systems to evolve?
* Can I explain why good collaboration protects boundaries?

If your answer is "yes" to these without looking at notes, then Step 6 has become part of your thinking.

---

# 📌 One Thing I Would Add Before Step 7

There is **one final connection** that I think is worth making.

During Step 5, we discovered:

> **Who owns behaviour?**

During Step 6, we discovered:

> **How those behaviours work together.**

Now ask yourself one final question:

> **Where will those behaviours actually live in code?**

That question is the natural bridge into Step 7.

Notice how we didn't ask:

> Which class should have which method?

Instead, we're asking:

> How do we express everything we've already discovered without losing the business thinking behind it?

That is exactly where Step 7 begins.

---

# 🌟 One Sentence That Changed My Thinking (Final)

If I had to preserve only one sentence from the entire step, it would be this:

> **Objects don't collaborate because software is object-oriented; software is object-oriented because business responsibilities naturally need to collaborate.**

---

## Finally...

Aditya, I honestly wouldn't change the structure of Step 6.

It now has a complete learning arc:

1. Business Event
2. Participants
3. Coordination
4. Messages
5. Contracts
6. Integration & Reflection

It starts with **"something happened in the business"** and ends with **"a society of responsible objects working together through trust."**

I don't think anything essential is missing before we move to Step 7.

And I have to admit something...

When we began this case study, I hoped that by Step 6 you would stop asking, *"Which class should I create?"*

Today, after reading your final assignment, I think you've already started asking a much better question:

> **"What business responsibility is trying to find the right home?"**

That's the question great designers ask first.

And that's why I'm genuinely excited for Step 7. It won't feel like "learning UML" or "adding methods." It will feel like giving software form to the thinking you've already built.
