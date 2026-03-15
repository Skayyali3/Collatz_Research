import csv
import multiprocessing
import sys
import time

def get_fate(n, q, r, limit):
    steps = 0
    tortoise = n
    hare = n

    isstandardcollatz = (q == 3 and r == 1)
    while steps < limit:
        tortoise = calc(tortoise, q, r)
        steps += 1
        hare = calc(calc(hare, q, r), q, r)
        if tortoise == 0: return (n, "Zero Loop", steps)
        if isstandardcollatz and tortoise == 1: return(n, "Standard Collatz one attraction", steps)
        if tortoise == hare:
            loopmems = []
            curr = tortoise
            while True:
                loopmems.append(curr)
                curr = calc(curr, q, r)
                if curr == tortoise: break

            pos_m = [m for m in loopmems if m > 0]
            if pos_m:
                min_bits = min(m.bit_length() for m in pos_m)
                loop_val = min([m for m in pos_m if m.bit_length() == min_bits])
                return (n, f"Loop {loop_val}", steps)
            else:
                return (n, f"Loop {max(loopmems)}", steps)
        
    return (n, "Exceeded", steps)

def run_range_dynamic(dynstarttime, end, step, q, r, limit):
    results = []
    for i in range(dynstarttime, end, step):
        results.append(get_fate(i, q, r, limit))
    return results

def calc(num, q, r):
    num = num >> 1 if (num & 1) == 0 else num * q + r
    return num

def parse_collatz(val):
    val = val.replace(" ", "").replace(",", "").lower()
    try:
        if "*10^" in val:
            base, exp = val.split("*10^")
            if "." in base:
                digits, dec_places = base.replace(".", ""), len(base.split(".")[1])
                return int(digits) * (10 ** (int(exp) - dec_places))
            else:
                return int(base) * (10 ** int(exp))
        elif "*10**" in val:
            base, exp = val.split("*10**")
            if "." in base:
                digits, dec_places = base.replace(".", ""), len(base.split(".")[1])
                return int(digits) * (10 ** (int(exp) - dec_places))
            else:
                return int(base) * (10 ** int(exp))
        elif "^" in val:
            base, exp = val.split("^")
            return int(base) ** int(exp)
        elif "**" in val:
            base, exp = val.split("**")
            return int(base) ** int(exp)
        elif "e" in val:
            base, exp = val.split("e")
            if "." in base:
                digits, dec_places = base.replace(".", ""), len(base.split(".")[1])
                return int(digits) * (10 ** (int(exp) - dec_places))
            else:
                return int(base) * (10 ** int(exp))
        else:
            return int(val)
    except:
        return None

if __name__ == "__main__":
    try:
        print("Welcome to the qn+r Conjecture Million Tester")
        q = parse_collatz(input("Enter 'q' (Standard would be 3): "))
        r = parse_collatz(input("Enter 'r' (Standard would be 1): "))
        limit = parse_collatz(input("Enter Step Limit (e.g., 1000): "))
        direction = input("Run Positive (p) or Negative (n) million? ").lower()
    except ValueError:
        print("\nError: Please enter valid integers for q, r, and limit.")
        input("Press Enter to exit..")
        sys.exit(1)

    if direction == 'n':
        START, END, STEP = -1, -1000000, -1
        label = "Negative"
    else:
        START, END, STEP = 1, 1000000, 1
        label = "Positive"

    CHUNK_SIZE = 10000
    starttime = time.time()

    print(f"\n[*] Initializing {label} Mega-Run...")
    print(f"[*] Conjecture: {q}n + {r} | Limit: {limit} steps")
    
    tasks = []
    if STEP == 1:
        for i in range(START, END + 1, CHUNK_SIZE):
            endchunk = min(i + CHUNK_SIZE, END + 1)
            tasks.append((i, endchunk, STEP, q, r, limit))
    else:
        for i in range(START, END - 1, -CHUNK_SIZE):
            endchunk = max(i - CHUNK_SIZE, END - 1)
            tasks.append((i, endchunk, STEP, q, r, limit))

   
    with multiprocessing.Pool() as pool:
        allresults = pool.starmap(run_range_dynamic, tasks)

    
    flatresults = [item for sublist in allresults for item in sublist]
    elapsedtime = time.time() - starttime
    
    filename = f"{label}_Results_{q}n+{r}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Number", "Fate", "Steps"])
        writer.writerows(flatresults)

    fates = [r[1] for r in flatresults]
    print(f"\n{'='*40}")
    print(f"Research Log: {label.upper()} MILLION COMPLETE")
    print(f"{'='*40}")
    print(f"Total Time: {elapsedtime:.2f} seconds")
    print(f"Average Speed: {1000000/elapsedtime:.0f} numbers/sec")
    print("-" * 40)

    for fate in sorted(set(fates)):
        count = fates.count(fate)
        percentage = (count / 1000000) * 100
        print(f"{fate}: {count} numbers ({percentage:.2f}%)")
    
    print("-" * 40)
    print(f"Data saved to: {filename}\n")
    input("Press Enter to exit..")
    sys.exit(1)