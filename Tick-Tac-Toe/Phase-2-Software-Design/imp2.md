| Business Event | Participants            |
| -------------- | ----------------------- |
| Player decides | Player                  |
| Validate move  | Game + Board            |
| Update board   | Game + Board + Cell     |
| Check winner   | Game + WinningCondition |
| Check draw     | Game + Board            |
| Change turn    | Game                    |

| Business Event         | Main Participants      | Why They Participate                                                      |
| ---------------------- | ---------------------- | ------------------------------------------------------------------------- |
| Player decides to move | Player                 | Originates the move and provides intent, position, and symbol.            |
| Move is validated      | Game, Board            | Game enforces game-level rules; Board validates board-specific rules.     |
| Board is updated       | Game, Board, Cell      | Game orchestrates, Board locates, Cell updates its own state.             |
| Winner is checked      | Game, WinningCondition | Game triggers the evaluation; WinningCondition applies the business rule. |
| Draw is checked        | Game, Board            | Board provides board state; Game determines the overall outcome.          |
| Turn changes           | Game                   | Game owns the lifecycle and controls progression.                         |
