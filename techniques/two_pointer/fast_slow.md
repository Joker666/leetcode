# Fast Slow

Two pointers starting from either the same position or a different one move in
different speed.

One could move at a pace of one node at a time when the other one moves two
nodes at a time. Here the fast pointer goes twice as fast as the slow pointer.

Fast pointer can traverse in different speeds vs the slow pointer.

Useful:

- Cycle detection in singly linked list
- Finding middle point of a singly linked list
    - if fast pointer moves twice at fast as thw slow pointer, by the time fast
      pointer reaches the end of the linked list, slow pointer will be in the middle