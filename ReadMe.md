## Automate The Boring Stuff With Python

#### Basics

##### Math Operators
`**`    Exponent
`%`     Modulus/Remainder
`//`    Integer division
`/`     Division
`*`     Multiplication
`-`     Subtraction
`+`     Addition

### Tuples
`(` and `)`
`Immutable` cannot have their values modified, appended or removed.
You can use tuples to convery to anyone that you don't intend for that sequence to change
`tuple(args)` converts arguments to tuple

### Lists
`[` and `]`
`list(args)` converts arguments to list
assigning a list `reference` to the variable. A reference is a value that points to some bit of data.
List variables store reference to list and not the actual list
#### Methods
`copy()` used to make a duplicate copy of a mutable value(list or dictionary), not just a copy of reference.
`deepcopy()` copy inner lists(list in list).

### Dictionary
`{` and `}`
collection of many values. Indexes for dictionaries are called `keys` and associated value called `key-value`.
#### Methods
`keys()`
`values()`
`items`
these methods return list-like values, they cannot be modified and do not have an append() method
`get()` takes two arguments, the key of the value to retrieve and a fallback value to return if that key does not exist
`setdefault` receives two arguments, the first argument is the key to check for, and the second argument is the value to set at that key if the key does not exist. If the key does exist, the setdefault() method returns the key's value.
`pprint.pprint()` **pretty print** a dictionary's values.
`pprint.pformat()` obtain the prettified text as a string value instead of displaying it on the screen

### Strings
`print(r'--')`
place an **r** before the beginning quotation mark of a string to make it a raw string. A raw string completely ignores all escape characters and prints any backslash that appears in the string.
#### Methods
`upper()` turn to uppercase
`lower()` turn to lowercase
`join()` useful for joing lists
`split()` separates strings at the position specified as argument
`rjust(), ljust() and center()`
justify text to the right, left and center, the first argument is the length of characters and the second arguments is the character used to replace spaces
`strip(), rstrip() and lstrip()`
strip off whitespace characters (space, tab, and newline) or string passed as argument
##### Checking Methods
`isalpha()` returns True if the string consists only of lettes and is not blank
`isalnum()` returns True if the string consists only of letters and numbers and is not blank
`isdecimal()` returns True if the string consists only of numeric characters and is not blank
`isspace()` returns True if the string consists only of spaces, tabs, and newlines and is not blank
`istitle()` returns True if the string consists only of words that begin with an uppercase letter
`startswith()`
`endswith()`

### Regular Expressions
`import re` *all the regex functions are in this module

`\d, \w, and \s` match a digit, word, or space character, respectively.
`\D, \W, and \S` match anything except a digit, word, or space character, respectively.
` . (or dot)` character in regular expression is called a `wildcard` and will match any character except for a newline.
`re.compile()` create regular expression
`.search()` search for regular expression in string to find a single match
`.findall()` to find all matching instances
`.sub()` replace regex string. Censor the regex by passing `(\1, \2, \3)` as first argument

- **?** matches zero or one of the preceding group.
- * matches zero or more of the preceding group.
- **+** matches one or more of the preceding group.
- **{n}** matches exactly n of the preceding group.
- **{n,}** matches n or more of the preceding group.
- **{,m}** matches 0 to m of the preceding group.
- **{n,m}** matches at least n and at most m of the preceding group.
- **{n,m}?** or ***?** or **+?** performs a nongreedy match of the preceding group.
- **^spam** means the string must begin with spam.
- **spam$** means the string must end with spam.
- **.** matches any character, except newline characters.
- **[abc]** matches any character between the brackets (such as a, b, or c).
- **[^abc]** matches any character that isn’t between the brackets.

`re.IGNORECASE` or `re.I` passed as second argument to make regular expression case insensitive
`re.VERBOSE` passed as second argument to make function ignore whitespace and comments inside the regular expression string
`re.DOTALL` makes the dot character match all characters including the newline character
> re.compile('--', re.IGNORECASE | re.DOTALL | re.VERBOSE)

### Files
"# Automate-the-Boring-Stuff" 
