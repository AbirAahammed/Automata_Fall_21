<h1><center>Intro to State machine and Exmaples of DFA</center></h1>

Contents
- [States](#states)
  - [Transitions](#transitions)
- [Example of DFA](#example-of-dfa)
  - [Details: [Login example]](#details-login-example)
    - [State (Q)](#state-q)
    - [Alphabets ($\sum$)](#alphabets-sum)
    - [Transition Function ($\delta$)](#transition-function-delta)
    - [Start State ($q_0$)](#start-state-q_0)
    - [Accepting States (F)](#accepting-states-f)
- [Deterministic Finite Automata (DFAs): Definition and Diagram](#deterministic-finite-automata-dfas-definition-and-diagram)
  - [languages of DFA](#languages-of-dfa)
    - [Formal definition: IS W accepted?](#formal-definition-is-w-accepted)
- [Regular Language](#regular-language)
  - [To Prove a language is regular:](#to-prove-a-language-is-regular)
  - [State Invariants](#state-invariants)

## States
- All the information at a instant is the system's state in that instance.
- From it's state, we can figure out what the system can do next.

### Transitions
- change of state
- Usually in response to external inputs/events
## Example of DFA

- Step 1: States | Q
- Step 2: External inputs | $\sum$
- Step 3: Transitions | $\delta$
- Step 4: Start State | $q_0$
  - How does the system start?
- Step 5: Decision | $F$
  - How does a system decide or reject?

### Details: [Login example]
#### State (Q)
Q = {Blank, UserFilled, PassFilled, User&PassFilled, Submitted, BlankWithError, LoggedIn}
#### Alphabets ($\sum$)
$\sum = $ {InputUserText, InputPassText, PushSubmit, DBMatch, DBNoMatch}
#### Transition Function ($\delta$)
Formally $\delta : Q \times \sum \rightarrow Q$
#### Start State ($q_0$)
$q_0 = Blank$
#### Accepting States (F)
F = {LoggedIn}

## Deterministic Finite Automata (DFAs): Definition and Diagram
- Automaton means machine. Automata is plural form of Automaton
- Deterministic measn that there is exactly one state in each cell of the transition of table
- Finite means that Q has finite size
  - the number of states is not infinite

### languages of DFA
> $\mathscr{L}(M) = \{W \in \sum^* | M accepts W\}$
 - Which language a machine decide?

#### Formal definition: IS W accepted?
Let W = $w_1 \cdot w_2 \cdot w_3 \cdot w_4.........$ where Each $w_j \in \sum$
IS there a sequence $(S_0, S_1, S_2, ......,S_n)$ such that 
1. Each $S_i$ in Q, i.e. machine state
2. $S_0 = q_0$ and $S_n \in F$
3. $\delta(S_i, w_{i+1}) = S_{i+1}$ for each i = 0 ,...n-1

## Regular Language
If L is a regular language then there exists  DFA $M$ such that $L = \mathscr{L}(M)$
- $M$ accepts all strings in L 
- and rejects all strings not in L.
### To Prove a language is regular:
1. Describe or Draw a DFA M
2. Prove that, $W \in L \implies M$ accepts $W$ And
3. Prove that,  $W \notin L \implies M$ rejects $W$
> Sometime easier to prove contrapositive

### State Invariants
- A state invariant for state S is something that is true about the string read so far when the machine is in state S.
