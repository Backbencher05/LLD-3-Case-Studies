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
