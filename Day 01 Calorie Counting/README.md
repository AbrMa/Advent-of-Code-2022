# Solution

## First Part

The problem is asking for the elf who is carrying the most amount of calories.

To do that we have to calculate each elf sum of calories so that 

```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```

becomes 

```
6000

4000

11000

24000

10000
```

we can store those values into a data structure that can be sorted, in python we can use a list 

$$ elves = [6000, 4000, 11000, 24000, 10000] $$

then for finding the largest value we can sort the list 

$$ elves = [4000, 6000, 10000, 11000, 24000] $$

the largest value is going to be stored at the end.

## Second Part

The problem now is asking for the sum of the top 3, since we already have a list that is sorted we can just return the sum of the last three elements.
