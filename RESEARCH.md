# The Collatz Multiverse: *qn+r* Conjecture Research Log

## Research Tool: The Universal Engine
My research is powered by a custom Python-based ["Deep Search"](Deep-Search.py) tool capable of:
1. **Infinite Precision:** Handling numbers with 1,000,000+ digits.
2. **Cycle Detection:** Tracking every state to find loops in any system.
3. **Divergence Guarding:** Automatically stopping if a number grows exponentially.

## Key Experiments

## 1. The 3n-1 "Mirror" System
Contrary to the 3n+1 Collatz conjecture, 3n-1 contains multiple domains of attraction:
* **The 1-Loop:** The primary target [2, 1].
* **The 5-Loop:** A 5-step cycle [14, 7, 20, 10, 5].
* **The 17-Loop:** A complex 18-step loop. [17, 50, 25, 74, 37, 110, 55, 164, 82, 41, 122, 61, 182, 91, 272, 136, 68, 34].
* **The Negative Mirror:** Discovered the [-4, -2, -1] loop using $n = -773$.

**Conclusion:** $3n-1$ on positive integers is a perfect mirror of $3n+1$ on negative integers, exhibiting identical loop structures with inverted signs.

## 2. High-Magnitude Verification
Tested $2.756 \times 10^{67}$. 
* **Discovery:** Using floating-point notation in GUIs causes a "Precision Cliff," leading to false loops.
* **Verification:** Using full integers, the value successfully reached 1 in **1046 steps**.

## 3. Edge Cases
* **The Centurion Number:** 983,232 reached 1 in exactly **100 steps** in the $3n-1$ conjecture (on GUI it says 101 because it counts an extra step).
* **The Boundary Shift:** 983,233 (only 1 higher) was captured by the 5-loop in **96 steps** in the $3n-1$ conjecture.

## 4. The $4n+8$ "Plummet" Phenomenon
### 4.1 The Mechanism
Every tested negative number follows a predictable two-phase life cycle:

-The Ascent: The $+8$ constant is powerful enough to "lift" negative numbers toward $0$.

-The Breach: If a number reaches $1$, it triggers the $n/2$ rule.

-The Plummet: Once the value crosses into the positive commencement, the $4n+8$ multiplier overpowers the $n/2$ division, causing the number to diverge toward infinity, and all negative numbers interestingly enough plummet in the same trajectory as they all diverge at 1 and go up from there all the same.

### 4.2 Case Study: (-786,678)

*Starting Point: $-786,678$*

#### Behavior: Climbed steadily for over 500,000 steps. (For you nerds, it is 590,011 steps exactly)

#### The Climax: Reached the value $1$.

#### The Terminal Event: Immediately following the success at $1$, the sequence enters a divergent loop where the $4n$ multiplier causes an exponential explosion.

## 5. The $-3n+-1$ Anomalies:
### 5.1 The path of Most Numbers:
Most numbers in this sequence converge at some point to 1, but some loops exist too:
* The $1$ loop [1,-2,-1,2,1] which in total is a **5 step loop**.

* The $17$ loop [17, -52, -26, -13, 38, 19, -58, -29, 86, 43, -130, -65, 194, 97, -292, -146, -73, 218, 109, -328, -164, -82, -41, 122, 61, -184, -92, -46, -23, 68, 34, 17] which in total is a **32 step loop**.

### 5.2 The Anomalous Result
I was testing out the number $97$ as $n=97$ and discovered a loop! 
Loop:
[97, -292, -146, -73, 218, 109, -328, -164, -82, -41, 122, 61, -184, -92, -46, -23, 68, 34, 17, -52, -26, -13, 38, 19, -58, -29, 86, 43, -130, -65, 194, 97] which in total is a **32 step loop** just like the 17-loop.
