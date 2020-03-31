## Dutch National Flag Problem

### Reasoning

since we only have 3 values, all we need to do is put the 2's at the end and 0 at the start and the array will be sorted, we can do that by having an index for the zeros at the start of the array `z_index`, index for the twos at the end `t_index`, and an index to iterate through the array with `index`.
while `index` is less than `t_index` then we haven't walked the whole array once yet:

- so we keep checking if `t_index` is over a 2 we reduce it by 1
- otherwise if `index` is over a 0 we swap it with `z_index` and move them both 1 forward
- otherwise if `index` is over a 2 we swap it with `t_index` and reduce `t_index` by 1
- or if `index` is over a 1 we just move `index` forward.

by the end the 2's will be at the end, the zeros at the start, the 1's in the middle.

### Efficiency

- Time Complexity: we only loop through the array once, and do O(1) operations in each loop, so the time complexity is `O(n)`.

- Space Complexity: all the operations on the array are inplace, we only use 3 variables for the indecies, so the complexity is `O(1)`
