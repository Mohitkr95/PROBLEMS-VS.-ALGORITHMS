## Finding the Square Root of an Integer

### Reasoning

when we are findng the floor of the sqrt of a number `X`, then we are searching for a number `N` in the range `(0, X)` that meets a the condition `N^2 = X` or `(N^2 < X) and ((N+1)^2 > X)`, since the range `(0, X)` is sorted, we can use a version of binary search:

- if the number is negative sqrt is `None`
- we start with the number itself as `N`, if it meets the condition above then its the answer, otherwise if `(N^2 > X)` then the next `N = N/2`, if `(N^2 < X)` then `N` is between its current value and its previous value.

### Efficiency

- Time Complexity: Since our algorithem halves the search range every iteration and performs O(1) calculations on every iteration then our Time complexity is `O(log(n))`.

- Space Complexity: O(1) since we only use a the same ammount of memory (four variables only `(current_num, previous_num, current_square, next_square)`) regardles of the input
