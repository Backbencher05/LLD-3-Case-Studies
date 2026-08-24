| Object           | Behaviour                 | Public / Internal | Why?                                        |
| ---------------- | ------------------------- | ----------------- | ------------------------------------------- |
| Game             | Accept player's move      | Public            | Primary business capability others rely on. |
| Game             | Change current player     | Internal          | Part of coordinating game flow.             |
| Game             | Determine next game state | Internal          | Internal decision-making step.              |
| Game             | End the game              | Internal          | Lifecycle management belongs to Game.       |
| Board            | Accept placement          | Public            | Core board capability.                      |
| Board            | Locate Cell               | Internal          | Storage detail.                             |
| Board            | Validate position         | Public            | Legitimate board service.                   |
| Board            | Maintain consistency      | Internal          | Continuous internal responsibility.         |
| Board            | Reveal board state        | Public            | Needed by trusted collaborators.            |
| WinningCondition | Evaluate winner           | Public            | Core business capability.                   |
| WinningCondition | Evaluate rows             | Internal          | Helper operation.                           |
| WinningCondition | Evaluate columns          | Internal          | Helper operation.                           |
| WinningCondition | Evaluate diagonals        | Internal          | Helper operation.                           |



| Object           | Interaction                    | Command / Question | Why?                                            |
| ---------------- | ------------------------------ | ------------------ | ----------------------------------------------- |
| Game             | Start game                     | Command            | Begins the game lifecycle.                      |
| Game             | Accept player's move           | Command            | Changes the game state.                         |
| Game             | Is the game over?              | Question           | Reports current status.                         |
| Game             | Who is the current player?     | Question           | Reveals existing information.                   |
| Game             | Change current player          | Command            | Advances the game.                              |
| Board            | Accept placement               | Command            | Updates the playing area.                       |
| Board            | Is this position valid?        | Question           | Reports validity.                               |
| Board            | Is this Cell empty?            | Question           | Reports board state.                            |
| Board            | Reveal board state             | Question           | Provides a view of the board.                   |
| Board            | Reset board                    | Command            | Restores initial state.                         |
| Cell             | Store symbol                   | Command            | Changes Cell state.                             |
| Cell             | Is Cell empty?                 | Question           | Reports state.                                  |
| Cell             | Which symbol do you contain?   | Question           | Reports stored value.                           |
| WinningCondition | Evaluate winner                | Question           | Determines and reports whether a winner exists. |
| WinningCondition | Has someone won?               | Question           | Reports the current outcome.                    |
| WinningCondition | Which winning pattern matched? | Question           | Explains the result.                            |


# Board

| Method                           | Public?       | Command / Question | Business Behaviour         | Should Exist?                            |
| -------------------------------- | ------------- | ------------------ | -------------------------- | ---------------------------------------- |
| `place_symbol(position, symbol)` | ✅ Yes         | Command            | Accept a valid placement   | Yes                                      |
| `reset()`                        | ✅ Yes         | Command            | Restore playing area       | Yes                                      |
| `get_state()`                    | ✅ Yes         | Question           | Reveal board state         | Yes                                      |
| `is_position_valid(position)`    | ✅ Yes         | Question           | Validate a position        | Yes                                      |
| `get_cell(position)`             | ❌ No          | Question           | Exposes implementation     | Internal only if needed                  |
| `is_cell_empty(position)`        | ❌ Probably No | Question           | Too implementation-focused | Internal or replaced by richer behaviour |
| `update_cell(position, symbol)`  | ❌ No          | Command            | Internal board operation   | Internal only                            |


# Board Attribute
| Information      | Board Attribute? | Why?                                             | If Not, Owner               |
| ---------------- | ---------------- | ------------------------------------------------ | --------------------------- |
| Board Size       | ✅ Yes            | Part of the Board's identity and responsibility. | —                           |
| Cells            | ✅ Yes            | Represent the playing area owned by the Board.   | —                           |
| Current Player   | ❌ No             | Turn management is a game concern.               | Game                        |
| Winner           | ❌ No             | Outcome of the game, not the board.              | Game                        |
| Game Status      | ❌ No             | Lifecycle information.                           | Game                        |
| Move History     | ❌ No             | Historical record, separate concern.             | MoveHistory (future) / Game |
| Theme Colour     | ❌ No             | Presentation concern.                            | UI / Presentation           |
| Winning Strategy | ❌ No             | Rule evaluation concern.                         | WinningCondition            |

# Attribute / Parameter

| Information     | Attribute / Parameter | Why?                                 |
| --------------- | --------------------- | ------------------------------------ |
| Position        | Parameter             | Specific to one interaction.         |
| Symbol          | Parameter             | Describes a particular action.       |
| Board Size      | Attribute             | Stable property of the Board.        |
| Player          | Parameter             | Owned by the Game, not the Board.    |
| Winning Pattern | Parameter             | Used during a particular evaluation. |
| Move            | Parameter             | Represents one business event.       |


# Relationships

| Relationship             | Permanent?   | Reason                                   |
| ------------------------ | ------------ | ---------------------------------------- |
| Game → Board             | ✅ Yes        | Board is part of the Game's lifetime.    |
| Board → Cell             | ✅ Yes        | Cells form the playing area.             |
| Cell → Board             | ❌ No         | Cell doesn't need to know its owner.     |
| Game → Player            | ✅ Yes        | Players participate throughout the Game. |
| Player → Game            | ❌ Usually No | Player shouldn't depend on one Game.     |
| Game → WinningCondition  | ✅ Yes        | Uses the same rule throughout the Game.  |
| WinningCondition → Board | ⚠️ Temporary | Needs Board only during evaluation.      |
| Board → WinningCondition | ❌ No         | Board shouldn't know winning rules.      |


| Object           | Attribute / Parameter / Neither | Why                            |
| ---------------- | ------------------------------- | ------------------------------ |
| Position         | Parameter                       | Specific to one interaction.   |
| Board            | Attribute (for Game)            | Long-term collaborator.        |
| Cell             | Attribute (for Board)           | Long-term part of the Board.   |
| WinningCondition | Attribute (for Game)            | Reused throughout the Game.    |
| Move             | Parameter                       | Represents one business event. |
| Player           | Attribute (for Game)            | Exists throughout the Game.    |




| Object           | Who creates it?    | Internal or External? | Reason                                                                    |
| ---------------- | ------------------ | --------------------- | ------------------------------------------------------------------------- |
| Board            | Outside the Game   | Received              | Game collaborates with a Board but shouldn't decide how one is built.     |
| Cells            | Board              | Internal              | Cells are part of the Board's internal representation.                    |
| WinningCondition | Outside the Game   | Received              | Different rule implementations may be supplied without changing the Game. |
| Players          | Outside the Game   | Received              | Players are independent participants.                                     |
| Symbol           | Outside (or value) | Received              | Cell stores it but doesn't create it.                                     |


| Relationship            | Created Internally / Received Externally | Why                                               |
| ----------------------- | ---------------------------------------- | ------------------------------------------------- |
| Game → Board            | Received                                 | Board is a collaborator.                          |
| Game → WinningCondition | Received                                 | Rule evaluator is a collaborator.                 |
| Board → Cells           | Created internally                       | Cells are part of the Board's internal structure. |
| Game → Players          | Received                                 | Players participate independently.                |
| Cell → Symbol           | Received                                 | Cell stores the symbol rather than creating it.   |
