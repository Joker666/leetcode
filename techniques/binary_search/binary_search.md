## Binary Search

Binary search is a form of divide and conquer.
We discard the search space that does not hold the desired value.
And we keep doing this continuously until the search space is fully exhausted.

To discard the search space, we usually find a middle point.
If the left side does not hold the desired value, we discard the left side.
Similarly, if the right side does not hold the desired value, we discard the right side.

And then we update the middle point again.

This technique can be applied both iteratively and recursively.
