<h1><center>Definition and Notation</center></h1>

Contents
- [String](#string)
- [Kleene Star](#kleene-star)
- [String Contcatenation](#string-contcatenation)
- [Prefix](#prefix)
  - [Some facts](#some-facts)
- [Reverse](#reverse)
- [Sets](#sets)
  - [Union, Intersection, Substraction, Complement, Product, Conctenation of language](#union-intersection-substraction-complement-product-conctenation-of-language)
- [Powers of Language](#powers-of-language)
  - [Kleen stat * as power](#kleen-stat--as-power)
- [DeMorgan's laws](#demorgans-laws)
- [Strings vs. Sets](#strings-vs-sets)
- [Function Notation](#function-notation)
## String
- A **String** is a finite sequence of symbols, and these symbols come from a finite alphabet.
- An **Alphabet** is a finite set, often denoted by $\sum$
    - Each element of an **alphabet** is a **symbol**.
    - A **string** over $\sum$ is any finite-length sequence of **symbols** from $\sum$
    - String sometimes referred to as words
    - The length of a string is $W$ is the number of symbols in W, denoted by $|W|$.
> **GIST:** set of Symbols makes alphabet. A combination of those symbols of Alphabet gives string or word. Count of symbols in a string is the length.
- For any alphabet $\sum$ there is a special string called the empty string denoted by $\epsilon$, its length is 0.
- Exponent Notation: Shortcut for repeated symbols
  - $z^k$ to denote strings of Z's of length k, Example $2^3 = 222$
    - $2^0 = \epsilon$ Empty string.
## Kleene Star
- For any **Alphabet** $\sum$ the set of all string over $\sum$ is denoted by  $\sum^*$ 
  - One way to think about it, for each k>=0, list all string of lenmgth k you can make using symbols from $\sum$

## String Contcatenation
- string are concatenated by putting them side to side.
- it uses dot notation.
- THe length of the concatenation string $W_1 \cdot W_2$ : $|W_1\cdot W_2|$ = $|W_1| + |W_2|$
- Concatenation the empty string does nothing,
- For a string $W$ and integer $k \geq 0$, <br/> the value of $W^K$ is W concatenated to itself k times.

## Prefix
- String $P$ is a **prefix** of string $Y$ if $Y = P\cdot Z$ where $Z$ is a string
### Some facts
1. Empty string is a Prefix of every string
2. Every string is a prefix of itself

- A Prefix $P$ of $Y$ is called propper prefix if $P\neq \epsilon$ and $P \neq Y$

## Reverse
- For any string $W$, the reverse $W^R$ is reverse of $W$.
- If $W = W^R$ then it is a palindrome. 

## Sets
- A set is an **unordered** collection of __distinct__ elements.
- A set of **string** is a __language__
  - A **language** can be **finite** or **infinite**<br/> But **alphabets** and **string** are **finite**.
- For any two sets A and B, write $A \subseteq B$ to say A is a subset of B.
  - Formal definition: $x \in A \implies x\in B$
  - Two sets A and B are equal, $A \subseteq B$ and $B \subseteq A$
- The size of a finite ser $S$ is the number of elements in S, written as $|S|$


### Union, Intersection, Substraction, Complement, Product, Conctenation of language
| Name                      | Def                                                                       |
| ------------------------- | ------------------------------------------------------------------------- |
| Union                     | $A \cup B = \{x \| (x \in A) \bigvee (x \in B)\}$                         |
| Intersection              | $A \cap B = \{x \| (x \in A) \bigwedge (x \in B)\}$                       |
| Substraction              | $A - B = \{x \| (x \in A) \bigwedge (x \notin B)\}$                       |
| Complement                | If U is the set of Universal element $\bar{A} = U - A$                    |
| Product                   | $A \times B = \{(a, b) \| ( a \in A) \bigwedge ( b \in B)\}$              |
| Concatenation of Language | $AB = A \cdot B = \{W_1 \cdot W_2 \| (W_1 \in A) \bigwedge (W_2 \in A)\}$ |

## Powers of Language
- $A^K$ denotes the set of string obtained by concatenating A with itself K times.
### Kleen stat * as power
- $A* = A^0 \cup A^1 \cup A^2 \cup A^3 \cup A^4 \cup A^5 \cup A^6 \cdot \cdot \cdot \cdot$
  - $A*$ contains an infinite number of strings, but each string in $A*$ is finite

## DeMorgan's laws
For any sets A and B
- $\overline{A \cup B} = \bar{A} \cap \bar{B}$
- $\overline{A \cap B} = \bar{A} \cup \bar{B}$

## Strings vs. Sets

| Strings                                            | Sets                                           |
| -------------------------------------------------- | ---------------------------------------------- |
| Order matters <br/> $the \neq teh$                 | no ordering <br/> $\{t, h, e\} = \{t, e ,h\}$  |
| Repetations allowed <br/> `0100` is a valid string | no repetitions <br/> {0, 1, 0, 0} is not a set |


## Function Notation
- function takes one input and produces one output. It must be well defined.