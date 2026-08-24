> **"What is a class diagram?"**

> **A class diagram is the visual representation of an already-discovered software design. It communicates the system's static structure—its responsibilities, knowledge, relationships, and ownership—so another engineer can understand how the software is organised before reading any code.**

> "A class diagram is a communication tool that captures the static architecture of a system. It shows the key objects, the responsibilities they own, the knowledge they maintain, and how they collaborate, allowing engineers to reason about the design before looking at the implementation."


# Interview Thinking

If an interviewer asks:

> **"What do you include in a class diagram?"**

A beginner often lists UML elements:

* Classes
* Attributes
* Methods
* Associations
* Multiplicity

An engineer explains the intent:

> "I start with the minimum structural information needed to communicate the architecture: the core classes, their responsibilities, and how they relate. As the design matures, I layer in attributes, operations, multiplicities, and other implementation-oriented details only when they improve understanding."

That answer shows you understand **why** the diagram exists, not just **what** UML allows.


## Final Discovery

> **Every engineering representation has a responsibility.**

A class diagram's responsibility is to communicate **structure**.

A sequence diagram's responsibility is to communicate **behaviour**.

A state diagram's responsibility is to communicate **lifecycle**.

Documentation's responsibility is to communicate **intent**.

This is the visual equivalent of the Single Responsibility Principle.