## Linked List

### Sentinel/dummy nodes
Adding a sentinel/dummy node at the head and/or tail might help to handle many edge cases where operations have to be
performed at the head or the tail. The presence of dummy nodes essentially ensures that operations will never be done
on the head or the tail, thereby removing a lot of headache in writing conditional checks to dealing with null pointers.
Be sure to remember to remove them at the end of the operation.

```python
dummy = curr = ListNode()
curr.next = head
```

or

```python
dummy = ListNode(0, head)
prev, curr = dummy, head
```