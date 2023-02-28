## Example 1
```
Enter a regular expression (Ex: "(a+ba)*1*"): a*b+
Enter a string (L = {a,b}): a
a*b+ : false
Type q to quit or enter another string: ab
a*b+ : true
Type q to quit or enter another string: abb
a*b+ : true
Type q to quit or enter another string: abababaa
a*b+ : false
```

## Example 2
```
Enter a regular expression (Ex: "(a+ba)*1*"): a(ab)*b
Enter a string (L = {a,b}): abb
a(ab)*b : false
Type q to quit or enter another string: ab
a(ab)*b : true
Type q to quit or enter another string: aabb
a(ab)*b : true
Type q to quit or enter another string: aaabbbaba
a(ab)*b : false
```

## Example 3
```
Enter a regular expression (Ex: "(a+ba)*1*"): (a+ba)*1*
Enter a string (L = {a,b}): abab
(a+ba)*1* : false
Type q to quit or enter another string: abb
(a+ba)*1* : false
Type q to quit or enter another string: aaaaaba
(a+ba)*1* : true
```