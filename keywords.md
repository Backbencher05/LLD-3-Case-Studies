A class is:

- A software abstraction that owns state and/or behavior to fulfill a specific responsibility in the system.
- A class is not created because Python supports classes; a class is created because a business responsibility needs a stable home in the software.

__init__ establishes the minimum valid state required for this object to begin fulfilling its responsibility.

# State vs Parameters

Another subtle question.

- Should position be an attribute?

self.position

- Or a parameter?

place_symbol(position, symbol)

-Ask: Does the Board permanently own one position?

No.

Each placement brings a new position.

That information is temporary.

- Temporary information usually travels as parameters.

- Persistent business knowledge usually becomes state.

- Methods answer: What can I do?
- Attributes answer: What must I remember?