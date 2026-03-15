# The $qn+r$ Research Lab

## Mathematical Analysis and High-Precision Deep Searching
This repository serves as the Engine Room for the **[Collatz Multiverse](https://github.com/Skayyali3/Collatz_Multiverse)** and **[Collatz Standard](https://github.com/Skayyali3/CollatzStandard)** projects. While the main applications focus on visualization, this lab is dedicated to stress-testing conjectures, identifying loops, and mapping the limits of numerical consistency.

Inspired by:
*[The Collatz Multiverse](https://www.youtube.com/watch?v=n63FBYqj98E&t=123)* by [carykh on YouTube](https://www.youtube.com/@carykh)

---

## Included Tools: 
### 1: *[Deep Search Python Engine](Deep-Search.py):*

A high-performance terminal tool designed for massive integers that:

* Utilizes Python's arbitrary-precision integers with a 1,000,000 digit string limit.
* Utilizes Cycle Detection by implementing floyd's algorithm for loop detection.
* Uses Safety Guards for automatic divergence detection to prevent exponential memory consumption.

### 2: *[MIllion Test Python Engine](Million-Test.py):*

A fast terminal tool that tests all digits from 1 to a million (both positive and negative work, based on user-input) on user-entered conjectures 

* Utilizes Python's `multiprocessing` library to perform internal math quickly when numbers are huge

* Utilizes Python's `csv` library to convert results into a csv file to be saved on your computer 

### 3: *[Titan Hunter Python Engine](Titan-Hunter.py):*

An efficient terminal tool designed to test random 1,000 digit numbers (positive and negative, based on user-input) on user-entered conjectures to discover if there is any divergence, loop, or even just to test the strength of known attractors

* Utilizes Python's `random` library to randomize 1,000 digit numbers to be used as the value n within the $qn+r$ conjecture 

* Converts loops to text files if any number in them is above one million as displaying them on the CLI could cause unwanted and laggy behaviour (Safety fallback).

### 4: *[The Number to Bit Converter](Bits.py):*

A side terminal tool that converts numbers to bits for user input in the main engines.

---

## Research Documentation:
### Core Findings are in the [Research File](RESEARCH.md)
### Key Discoveries:
* The Precision Cliff: Why standard floating-point math fails for numbers like ($10^{67}$)
* $3n-1$ Mirroring: Proof of the symmetry between $3n-1$ (positive) and $3n+1$ (negative)
* Shared Trajectories: The discovery of mathematical highways in the $4n+8$ system where all paths of negative numbers eventually merge at the commencement 1.
 
## How to Run:
Follow these steps to run the project locally:

### 1: Clone the repository and enter:
```bash
git clone https://github.com/Skayyali3/Collatz_Research.git
cd Collatz_Research
```

### 2 To:
#### -a: Run the Deep Search Python Engine:
```bash
python Deep-Search.py
```
#### -b Run  the Million Tester Python Engine:
```bash
python Million-Test.py
```

#### -c Run the Titan Hunter Python Engine:
```bash
python Titan-Hunter.py
```
#### -d Run the Number to Bits Converter:
```bash
python Bits.py
```

## License

This project is licensed under the MIT License – see the **[LICENSE](LICENSE)** file for details.

## Author
**Saif Kayyali**
