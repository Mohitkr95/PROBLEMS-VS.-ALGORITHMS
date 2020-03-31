## Rearrange Array Elements

### Reasoning

- #### new solution

  since we know elements in input can only be [0-9] then we can create an array of size 10 with each index representing an element and loop through the input to count the frequency of each number, then we loop through the frequency array from last index to the first, and at each index we loop adding digits to the numbers until the frequency is 0.
  then we return a tuple made up of the two numbers.

* #### old solution
  we start both numbers as 0,
  then first use mergesort to sort the values in a descending order, then we loop through the sorted array and for even indecies we multiply one number by 10 and add the value at the index to it, and for odd indecies we do the same for the other, that way we get the two lagrest values possible that don't differ by more than 1 digit.

### Efficiency (for new solution)

- Time Complexity: we create the size 10 frequencey array O(1), then iterate through the input list once to count the frequencies of each digit O(n), then we loop through the frequency array O(1), performing at most O(n) operations through each iteration.
  therefore our time complexity is `O(n)`.

- Space Complexity: we make a size 10 array and 3 other values and a size 2 tuple only, regardless of the input
  therefore our space complexity is `O(1)`.

### Efficiency (for old solution)

- Time Complexity: merge sort takes `O(nlog(n))` then we iterate through the list once to build the numbers taking O(1) for each iteration so `O(n)`,
  therefore our time complexity is `O(nlog(n))`.

- Space Complexity: merge sort makes a copy of the array at each iteration O(n) and it takes log(n) iteration. then building the numbers has a space complexity O(1).
  therefore our space complexity is `O(nlog(n))`.
