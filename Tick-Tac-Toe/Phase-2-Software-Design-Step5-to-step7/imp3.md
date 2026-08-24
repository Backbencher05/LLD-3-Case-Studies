| Conversation            | Information That Should Travel      | Information That Should Not Travel           |
| ----------------------- | ----------------------------------- | -------------------------------------------- |
| Player → Game           | Position (and intent to move)       | Board state, winner, validation result       |
| Game → Board            | Position, Symbol                    | Board layout, game status, turn information  |
| Board → Cell            | Symbol                              | Board, Player, other Cells, game status      |
| Game → WinningCondition | Current board state (or equivalent) | Turn, lifecycle, rule implementation details |


Business Event

↓

Responsibility

↓

Collaboration

↓

Coordination

↓

Message

↓

Contract


This feels like the right way to end Step 6.

Not by asking:

> **"Can you draw the sequence diagram?"**

But by asking:

> **"Have you changed the way you think?"**

When I look back at these six days, I realise we were never learning Tic-Tac-Toe.

We were learning how software conversations are discovered.

---

# Part A — Tell the Story of One Move

The game is already in progress, and it is Player X's turn.

The journey begins when the **Player** decides to place **X** at position **(1,2)**. The Player's responsibility is not to update the board or determine the winner. Its responsibility is simply to express its intention to make a move.

The Player communicates that intention to the **Game**. This message contains only the information the Game needs to continue the business process, such as the chosen position. The Player doesn't explain how the move should be processed because that responsibility belongs elsewhere.

The **Game** becomes the coordinator of this business event. Its responsibility is not to perform every piece of work itself, but to ensure that the move progresses through the correct business flow. It first determines whether the move is allowed to proceed from the perspective of the game's lifecycle—for example, whether the game is still active and whether it is actually Player X's turn.

Once the move is eligible to continue, the Game collaborates with the **Board**. The message between them contains only the information the Board needs to do its job, such as the position and the symbol to be placed. The Game does not send information the Board already owns, such as its dimensions or internal structure.

The **Board** now performs the responsibilities that naturally belong to it. It determines whether the requested position exists and whether the target location can accept a symbol. If the move is valid, the Board identifies the appropriate **Cell**.

The Board collaborates with that Cell by asking it to update its own state. The Cell's responsibility is limited to managing its own value. It neither knows nor cares whose turn it is or whether the move might win the game. It simply fulfils the responsibility it owns.

Once the board has been updated, the Game continues coordinating the overall business process. It now collaborates with the **WinningCondition**.

The contract between these two objects is very clear.

The Game expects one outcome:

> Determine whether the current board satisfies the winning rule.

It does not need to know how the WinningCondition reaches that answer.

The WinningCondition evaluates the current board and reports that no winning condition has been achieved.

The Game then determines whether the game has reached a draw. Finding that empty positions still remain, it concludes that the game should continue.

Finally, because neither a win nor a draw has occurred, the Game performs the responsibility of advancing the game by changing the turn to the next player.

The business event is now complete.

Every object fulfilled the responsibility it naturally owned.

Every collaboration happened because another object possessed knowledge it did not.

Every message contained only the information necessary to continue the business process.

Every contract was honoured because collaborators depended on promised outcomes rather than internal implementation.

The move is complete, and the next player is ready.

---

# Part B — Connect the Discoveries

| Discovery            | What question does it answer?                                                    | Why was it necessary?                                                                                                                                                                 |
| -------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Responsibilities** | **Who should own each piece of business behaviour?**                             | Without responsibility assignment, behaviour would be placed arbitrarily, leading to confused and unfocused objects.                                                                  |
| **Collaboration**    | **How do those responsible objects work together to complete a business event?** | No single object owns all the knowledge needed for a complete use case, so we needed to understand how specialised objects contribute together.                                       |
| **Coordination**     | **Who guides the business process from start to finish?**                        | Collaboration without coordination would become chaotic. Someone must be accountable for moving the business process forward while allowing others to perform their specialised work. |
| **Messages**         | **What information should collaborators exchange?**                              | Even with good responsibilities, poor communication can create unnecessary dependencies. Messages protect boundaries by sharing only what is required.                                |
| **Contracts**        | **What reliable promises do collaborators make to one another?**                 | Stable contracts allow objects to evolve internally without forcing every collaborator to change whenever an implementation changes.                                                  |

### How they build on each other

Responsibilities identify the right owners.

Once owners exist, they must collaborate.

Once collaboration exists, someone must coordinate it.

Once coordination exists, collaborators need to communicate.

Once communication exists, they need stable agreements so those conversations remain reliable even as the system evolves.

Each discovery depends on the one before it.

---

# Part C — Reflection

## Question 1

### What did collaboration mean to me at the beginning?

At the beginning, collaboration simply meant:

> "Objects calling each other's methods."

It felt like a technical concept.

Now I see collaboration very differently.

Collaboration is how independent business responsibilities come together to complete a business event.

Objects collaborate because each one owns only part of the business knowledge.

It's no longer about method calls.

It's about sharing responsibility while remaining independent.

---

## Question 2

### Which discovery changed my thinking the most?

The discovery of **contracts** changed my thinking the most.

Earlier, I thought collaboration was successful because objects could communicate.

Now I understand that communication alone isn't enough.

Two objects collaborate successfully because they agree on **outcomes**, not on **implementation**.

That one idea explains why good designs survive change.

If collaborators trust promises instead of implementation details, they can evolve independently.

---

## Question 3

### Why didn't we draw UML diagrams on Day 1?

Because diagrams describe a design.

They don't create one.

If we had started with sequence diagrams on Day 1, we would probably have drawn arrows between objects without understanding why those arrows existed.

Over the last six days we discovered, in order:

* the business story,
* the participating objects,
* the entry point of collaboration,
* the information exchanged,
* the agreements between collaborators.

Only after discovering those ideas does a sequence diagram become meaningful.

Now, if I draw a sequence diagram, every arrow has a reason.

Every participant has a responsibility.

Every message exists because of a business event.

The diagram becomes a summary of understanding instead of a guess.

---

# Engineering Challenge

Imagine tomorrow the business adds:

* Move History
* Replay
* AI Difficulty
* Game Timer
* Undo
* Online Multiplayer

I don't believe our current design would remain unchanged.

Some responsibilities would grow, some new collaborators would appear, and some contracts might expand.

But I also don't think we would need to redesign the entire system.

Here's why.

The design is organised around **business responsibilities**, not around one powerful object.

Suppose **Move History** is introduced.

Instead of teaching the Game how to remember every move internally, we can introduce a collaborator responsible for recording or managing move history. The Game remains accountable for the move, but it doesn't become responsible for storing history.

Suppose **Replay** is added.

Replay is a different business capability from running a live game. It can collaborate with move history without forcing the Board, Cell, or WinningCondition to change their core responsibilities.

Suppose **AI Difficulty** grows from Easy to Medium, Hard, or custom strategies.

The Game still asks the Bot to choose a move. The collaboration remains the same. Only the Bot's decision-making evolves.

Suppose **Game Timer** is introduced.

Timing is another business concern. It influences when moves are allowed, but it doesn't change how the Board manages cells or how WinningCondition evaluates a winner. A timer can collaborate with the Game instead of being absorbed into it.

Suppose **Undo** is added.

Undo changes how the game state progresses, but it doesn't change what a Cell means or what a Board represents. The design grows by extending collaboration rather than replacing existing responsibilities.

Finally, imagine **Online Multiplayer**.

Instead of changing how the Board works, we would likely introduce collaborators responsible for networking, communication, or synchronisation. The business conversation of "a player makes a move" remains recognisable.

If everything had been inside one giant `Game` object, every one of these features would require modifying the same class.

That class would gradually become responsible for:

* gameplay,
* board management,
* AI,
* networking,
* replay,
* timers,
* undo,
* logging,
* presentation.

Different business changes would constantly collide in the same place.

With the collaboration-based design, change tends to follow the responsibility it affects.

The Game still coordinates the business process.

The Board still represents the playing area.

The WinningCondition still evaluates rules.

New capabilities are introduced by extending the collaboration rather than replacing it.

That doesn't eliminate change.

It makes change **local**, **purposeful**, and **aligned with the business responsibilities we've already discovered**.

---

# 🌟 One Sentence That Changed My Thinking

> **Software design is not the art of creating classes—it is the art of discovering how independent business responsibilities collaborate through clear messages and trustworthy contracts to achieve a business goal.**

---

# Final Mentor's Reflection

This is the end of **Step 6**, and I think it's worth reflecting on what has actually happened.

At the start of this journey, you looked at Tic-Tac-Toe and saw a small game.

Now, you look at the same problem and naturally ask questions like:

* *What business event has just happened?*
* *Who is accountable for this outcome?*
* *Who has the knowledge to perform this work?*
* *What information should cross this boundary?*
* *What promise should collaborators rely on?*

Those questions are transferable.

Whether you design **Amazon**, **Uber**, **Netflix**, **ERPNext**, or a distributed payment system, the business vocabulary will change—but these questions remain the same.

That's the real achievement of Step 6.

You haven't just learned how Tic-Tac-Toe works.

You've built a repeatable way to discover collaboration in any software system.


