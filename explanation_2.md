## Search in a Rotated Sorted Array

### Reasoning

when searching for a number in an array that is sorted then rotated we can use a modified version of binary search, we only need to change the conditions on which we search one half or the other after testing the middle.
instead of testing if the target is greater than or smaller than the middle, we test the halfs of the array:

- we test the middle, if it's the target then we return the middle index.
- otherwise we check one side, if it's ordered (ex: value at last index greater than the one at the middle for the right side) we test if the target value is between the two values at the edges, otherwise if it's not odered (then it's the rotated half) we test that the target value is greater than the start or smaller than the end.
- otherwise it must be in the other half or doesn't exist.

### Efficiency

- Time Complexity: Since we are using binary search with a few extra conditional statements of complexity O(1), then our time comlexity remains the same as binary search's `O(log(n))`.

- Space Complexity: O(1) per recursive iteration, since we do about log(n) iterations then it's of the order `O(log(n))`.
  \*ps: an iterative implementation would have a space complexity of `O(1)`
