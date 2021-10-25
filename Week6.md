Content
- [Lecture 35](#lecture-35)
  - [Languages Computed by TMs](#languages-computed-by-tms)
    - [Decides](#decides)
    - [Recognizes](#recognizes)
    - [Decides vs. Recognizes](#decides-vs-recognizes)
  - [Languages Computed by TMs](#languages-computed-by-tms-1)
- [Lecture 36](#lecture-36)
    - [$DFA \implies TM$](#dfa-implies-tm)
- [Lecture 37](#lecture-37)
# Lecture 35

## Languages Computed by TMs

### Decides
Definition: A Turing machine M __decides__ a language L means 
1. for every $W \in L$, the machine accepts W, and 
2. for every $W \in L$, the machine rejects  W

### Recognizes
A TM M __recognizes__ a language L means M accepts W if and only if $W \in L$

> Contrapositive: "if not-B then not-A " is the contrapositive of "if A then B "

It state the following:
1. If M accepts W, then $W \in L$
   1. If $W \notin L$, then M does not accept W
2. If $W \in L$, then M accepts W
   1. If M does not accpet W, then $W\notin L$


### Decides vs. Recognizes
:boom:What is the difference?
- If M decides L, it means that M always halts, because it always accepts if input $W \in L$, and always rejects if input $W \notin L$
- If M recognizes L, then M always accepts input W if W \in L,
  - But if $W \notin L$, there are two possibilities: M rejects W, or M never halts.

:question: Does not accept covers both reject and never halts scenarios?
- [x] True
- [ ] False
> This answer is given in slide 5 of this lecture.

## Languages Computed by TMs
- A language L is __Turing-recognizable__[AKA __recursively enumerable language__] if there exists a TM M that recognizes it. 
- A language L is __Turing-decidable__[AKA __recursive language__] if there existis a TM M that decides it.

:star: Extremely Important
- [ ] If I want to prove that L is decidable using the definition:
  1.  Create a TM M
  2.  Prove: if $W \in L$, then M accepts W (or Its contrapostive)
  3.  Prove: If $W \notin L$, then M rejects W (or Its contrapostive)
- [ ] If I want to prove that L is recognizable using the definition:
  1.  Create a TM M
  2.  Prove: If $W \in L$, then M accepts W (or Its contrapostive)
  3.  Prove: If $W \notin L$, then M doesn't accept meaning, either rejects or never halts. (or Its contrapostive)


If a M decides L, 
1. M always halts
2. If $W \in L$ then M accepts W
3. If $W \notin L$ then M rejects W
4. If M accepts W, then $W \in L$
5. If M rejects W, then $W \notin L$

IF a M recognizes L,
1. If $W \in L$, then M accepts W
2. If M accepts W, then $W \in L$
3. If $W \in L$, then M might reject W or M might never halt on input W
4. If M rejects W then $W \notin L$
5. If  M never halts on inhput W, then $W \notin L$


# Lecture 36

DFA vs TM
1. $DFA \not ={TM}$
2. $DFA \subseteq TM$

### $DFA \implies TM$
- Step 1: Convert the transition state:
  - Take each transition lavel s, adn re-write it as s &rarr; s,R
- Step 2: add halting states: Accept and Reject
  - From each state in F (each accepting state in the DFA), add a transition _ &rarr; _,R to the accept state.
  - From all other state, add a transtion _ &rarr; _, R to the reject state.


The set of regular language is a strict subset of Turing-decideable, aka decideable language
$Decideable \subseteq Regular \subseteq Finite$

# Lecture 37
