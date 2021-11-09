# Lecture 46
## Then Diagonal Method
the proof worksm by contradiction:
1. Assume that the reals are countable. then you could write all real numbers in a single infinite list.
2. Go DIgonally through the list and consttruct a read number that doesn't a[ear amywhere in the list.
3. this is a contradiction, because the list was assumed to contain all real numbers

##  Bijection
It means one-to-one and onto
Example: Let, $A = \{a,...,z\}$ and $B = \{1,...,26\}$
Define $f:A $&rarr;$ B$ bt, $f(a) = 1, f(b) = 2$,...$f(z) = 26$
- One-to-one
  - $\forall x,y \in A,$ if $x \not ={y}$ then, $f(x)\not ={f(y)}$
- Onto
  - $\forall \beta \in B$, there exists $\alpha \in A$ such that $f(\alpha) = \beta$

### Languages computed by TMs
- A Turing machine M decides a language L,
  - [ ] $\forall W\in L$, the machine $M$ accepts $W$
  - [ ] $\forall W\notin L$, the machine $M$ rejects $W$
- A Turing machine M recognizes a language L means
  - [ ] $\forall W\in L$, the machine $M$ accepts $W$
  - [ ] $\forall W\notin L$, the machine $M$ does not accpet $W$
  - [ ] $\forall W\notin L$, the machine $M$ rejects $W$ or doesn't halt.


## <center><span style="color:Green">Lecture 49 SLide 3 Example $Accept_{TM}$</span></center>


# Lecture 52
## A useful theroem slide 4
> A language L is decidable
> if and only if
> L is recognizeable and the complement of L is recognizable.
1. If L is decidable, then $L$ and $\bar{L}$ are both recognizeable
2. If $L$ and $\bar{L}$ are both recognizeable, then L is decidable
3. If L is undecidable, then at least one of $L$ or $\bar{L}$ are both unrecognizeable
4. If at least one of $L$ or $\bar{L}$ are both unrecognizeable, then L is undecidable 