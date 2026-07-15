# Our Scope Clarification Questions

I want you to answer these one by one, and **don't worry about being "correct."** We can refine them together.

## Q1. What exactly are we designing?

Choose one (or propose another):

* The Tic-Tac-Toe game engine (core business logic only)
* A complete Tic-Tac-Toe application
* A Tic-Tac-Toe management system
* A multiplayer game server
* Something else

Explain **why** you chose it.

---

## Q2. Where will the data live?

Think about persistence.

Examples:

* Everything in memory
* Database
* File storage
* Doesn't matter for now

Also explain why.

---

## Q3. How will users interact with the system?

Examples:

* CLI (console)
* REST API
* GUI/Desktop
* Mobile
* Hardcoded `main()` for now

Again, explain your choice.

---

## Q4. Who are the users (actors)?

Think beyond "players."

Examples:

* Human Player
* AI Player
* Administrator
* Spectator

For our first version, who exists?

---

## Q5. What is explicitly **out of scope**?

This is one of the most important engineering habits.

What are we **not** building today?

Examples:

* Online multiplayer
* Database
* Authentication
* AI
* Leaderboards
* Tournament mode
* Chat
* Save/Load

Being explicit about what's excluded prevents accidental over-engineering.

---

## Q6. What assumptions are we making?

For example:

* Board is always 3×3.
* Exactly two players.
* Players alternate turns.
* The game ends after a win or draw.
* No concurrency.
* One game at a time.

Write down every assumption you're making.


# Out of Scope (Version 1)
Database
Networking
Authentication
Leaderboards
Tournament mode
Save/Load
Replay
Spectator mode
Chat
Multiple concurrent games

Part D — Out of Scope (Version 1)

To keep Version 1 focused, the following features are intentionally excluded:

Multiplayer
Online multiplayer
Networking
Multiple concurrent games
Persistence
Database
Save game
Load game
Replay previous games
User Management
Authentication
User profiles
Player statistics
Competitive Features
Leaderboards
Tournament mode
Match history
Rankings
Social Features
Chat
Spectator mode
Invitations
Friends list
Advanced Gameplay
Timers
Move history visualization
Redo functionality
Custom game rules editor
AI learning from previous games