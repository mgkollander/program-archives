## Example 1
```
Enter the language set separated by spaces (Ex. "a b"): 0 1
Enter the number of states (Ex. "2"): 3
Enter the initial state (Ex. "0"): 0
Enter the final state(s) (Ex. "1"): 0
Enter the next state for state 0 and element 0: 0
Enter the next state for state 0 and element 1: 1
Enter the next state for state 1 and element 0: 2
Enter the next state for state 1 and element 1: 0
Enter the next state for state 2 and element 0: 1
Enter the next state for state 2 and element 1: 2
Enter a string to check: 010101
ACCEPTED
Press enter to quit...
```

## Example 2
```
Enter the language set separated by spaces (Ex. "a b"): a b
Enter the number of states (Ex. "2"): 3
Enter the initial state (Ex. "0"): 0
Enter the final state(s) (Ex. "1"): 2
Enter the next state for state 0 and element a: 1
Enter the next state for state 0 and element b: 2
Enter the next state for state 1 and element a: 1
Enter the next state for state 1 and element b: 2
Enter the next state for state 2 and element a: 2
Enter the next state for state 2 and element b: 2
Enter a string to check: aaa
NOT ACCEPTED
Press enter to quit...
```

## Example 3
```
Enter the language set separated by spaces (Ex. "a b"): a b c
Enter the number of states (Ex. "2"): 5
Enter the initial state (Ex. "0"): 1
Enter the final state(s) (Ex. "1"): 4
Enter the next state for state 0 and element a: 0
Enter the next state for state 0 and element b: 0
Enter the next state for state 0 and element c: 0
Enter the next state for state 1 and element a: 2
Enter the next state for state 1 and element b: 0
Enter the next state for state 1 and element c: 0
Enter the next state for state 2 and element a: 0
Enter the next state for state 2 and element b: 3
Enter the next state for state 2 and element c: 0
Enter the next state for state 3 and element a: 0
Enter the next state for state 3 and element b: 0
Enter the next state for state 3 and element c: 4
Enter the next state for state 4 and element a: 2
Enter the next state for state 4 and element b: 0
Enter the next state for state 4 and element c: 4
Enter a string to check: abcabcc
ACCEPTED
Press enter to quit...
```