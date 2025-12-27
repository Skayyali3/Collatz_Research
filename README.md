# The $qn+r$ Research Lab
## Mathematical Analysis and High-Precision Deep Searching
This repository serves as the "Engine Room" for the [Collatz Multiverse](https://github.com/saifkayyali3/Collatz_Multiverse) project. While the main application focuses on visualization, this lab is dedicated to stress-testing conjectures, identifying loops, and mapping the limits of numerical stability.

---

## Included Tool:
* **[Deep Search Python Engine](Deep-Search.py):**

    A high-performance terminal tool designed for massive integers.

* Utilizes Python's arbitrary-precision integers with a 1,000,000 digit string limit.
* Cycle Detection: Implements a hashed `seen` set for loop detection.
* Safety Guards: Automatic divergence detection to prevent exponential memory consumption.

## Research Documentation:
#### Core Findings are in [Research](RESEARCH.md)
### Key Discoveries:
* The Precision Cliff: Why standard floating-point math fails for numbers ($10^{67}$)
* $3n-1$ Mirroring: Proof of the symmetry between $3n-1$ (positive) and $3n+1$ (negative)
* Shared Trajectories: The discovery of "Mathematical Highways" in the $4n+8$ system where all paths od negative numbers eventually merge at the commencement 1.
 
# How to Run:
Follow these steps to run the project locally:

# 1. Clone the repository and enter:
```bash
git clone https://github.com/saifkayyali3/Collatz-Research.git
cd Collatz_Research
```
# 2. Make a virtual environment
```bash
python -m venv venv

source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

# 3. Run
```bash
python Deep-Search.py

```
## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Author
**Saif Kayyali**