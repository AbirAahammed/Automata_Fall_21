- [a](#a)
- [b](#b)
- [c](#c)
# a
To show that $C$ is one-to-one, the proof is: [We will prove the contrapositive of definition of one-to-one, i.e. $[x \not ={y}] \implies [f(x) \not ={f(y)}]$
1. Let, x, y be 2 arbitrary binary string, suppose that C(x) = C(y)
2. Evaluate C(x) and C(y), we get $1 \cdot x$  and $1 \cdot y$
   Since C(x) = C(y), we get $1 \cdot x$ = $1 \cdot y \implies x = y$
therefore, $C$ is one to one.
<!-- 
$x \not ={y}$
$C(x) = C(y)$
$\implies 1 \cdot x = 1 \cdot y$
since, $x \not ={y}$
therefore,  $1 \cdot x \not ={1 \cdot y}$
or, $C(x) \not ={C(y)}$
Hence, $C$ is one to one. -->

# b
$C$ is not onto, the proof is as follows:
let, $\beta = 0$
Now, let $\alpha = x$ where $x \in \{0, 1\}^*$
then, $C(\alpha) = 1 \cdot x$, therefore, $C(\alpha)$ always starts with 1 no matter what is $x$. Hence, $\forall x \in \{0,1\}^* C(\alpha) = C(x) \not ={0} $
Hence, $\exist \beta \in \{0, 1\}^*, \forall \alpha \in \{0, 1\}^*$ such that, $C(\alpha) \not ={\beta}$

Hence $C$ is not onto.

# c
Let, 
-   $A = \{0, 1\}^*$
-   $B$ = { all binary string starting with 1 } 
-   $C : A $&rarr;$ B$ be defined as $C(W) = 1 \cdot W$

**To show that, C : A &rarr; B is one to one,**
1. Take any 2 $x$ and $y$ such that, $x, y \in A$, supoose that $C(x) = C(y)$
2. Evaluate $C(x)$ and $C(y)$, we get $1\cdot x$ and $1\cdot y$
Since $C(x) = C(y)$, we get $1\cdot x = 1\cdot y$, which implies $x=y$

**To show that,  C : A &rarr; B is onto,**
1. Let, $\beta = 1 \cdot x$ be an arbitrary element. As all string in $B$ starts with 1. And $x \in \{0, 1\}^*$
2. Define $\alpha = x$
3. Evaluate $C(\alpha)$: we get $C(\alpha) = C(x)= 1 \cdot x = \beta$

Therefore, $C$ is a bijection from $A \rightarrow B$. 

And in lecture 47, slide 4, the set of all binary strings that start with 1 is countable. Therefore, B or set of all binary string starting with 1 is countable.

Now, there exists a bijection $C$ from $A$ to $B$, and $B$ is countable therefore, $A$ or set of all binary string is also countable. Therefore, $L = \{0, 1\}^*$, is countable.
<!-- 
A set of all binary strin to B set of all binary  starting with 1. 
Now, Since there is a biject from $\mathbb{Z}^+ \rightarrow \{$Set of all binary starting with 1$\}$ [we have proved this in lecture]
Hence, $\{$Set of all binary string starting with 1$\}$ is countable.
Now since there is a bijecttion from set of all binary string to $\{$Set of all binary string starting with 1$\}$, set of all binaryb string is also countable.
If we can proof a bijection from a countable set to another set thant that set is also countable.

If A is a countably infinite and if $\exist$ bijection, 

C(W) maps all binary string to another binary string that starts with 1. let's set of all binary string that starts with 1 is $S_1$.

BinToDeci: $S_1$ &rarr; $\mathbb{Z}^+$.
Hence, $S_1$ is a countable set. And we have showed that, C(W) for $W \in \{0, 1\}^*$ is a bijection from all binary string to a new set $S_1$,
therefore, set of all binary string is also countable. or L is also countable.


Notes: 
-   for all $x, y\in A$, if $x\not ={y},$ then, $f(x)\not ={f(y)}$
-   for all $\beta \in B$, there exists $\alpha \in A$ such that, $f(\alpha) = \beta$ -->