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