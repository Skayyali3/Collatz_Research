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
        if "+" in val:
            parts = val.split("+")
            return sum(parse_collatz(p) for p in parts)
        if "*10^" in val or "*10**" in val:
            base, exp = val.split("*10^") if "*10^" in val else val.split("*10**")
            exponent = int(exp)
            if exponent < 0: return None
            if "." in base:
                digits, dec_places = base.replace(".", ""), len(base.split(".")[1])
                return int(digits) * (10 ** (exponent - dec_places))
            else:
                return int(base) * (10 ** int(exp))
        elif "^" in val or "**" in val:
            base, exp = val.split("^") if "^" in val else val.split("**")
            exponent = int(exp)
            if exponent < 0: return None
            return int(base) ** exponent
        elif "e" in val:
            base, exp = val.split("e")
            exponent = int(exp)
            if exponent < 0: return None
            if "." in base:
                digits, dec_places = base.replace(".", ""), len(base.split(".")[1])
                return int(digits) * (10 ** (exponent - dec_places))
            else:
                return int(base) * (10 ** exponent)
        else:
            return int(val)
    except:
        return None

if __name__ == "__main__":
    try:
        print("Welcome to the qn+r Conjecture Custom Range Tester")
        q = parse_collatz(input("Enter 'q' (Standard would be 3): ") or "3")
        r = parse_collatz(input("Enter 'r' (Standard would be 1): ") or "1")
        limit = parse_collatz(input("Enter Step Limit: ") or "10^9")

        minrange = parse_collatz(input("Enter the minimum of your range (Default is one): ") or "1")
        maxrange = parse_collatz(input("Enter the maximum of your range (Default is one mil): ") or "10^6")

        if minrange is None or maxrange is None:
            raise ValueError("Invalid range values.")

        diff = abs(maxrange - minrange)
        if diff > 1000000:
            print(f"\nError: Range size is {diff:,}. Please keep it under 1,000,000.")
            input("Press Enter to exit...")
            sys.exit(1)

    except ValueError as e:
        print(f"\nError: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

    if maxrange < minrange:
        STEP = -1
        label = "Descending"
    else:
        STEP = 1
        label = "Ascending"

    CHUNK_SIZE = 10000
    starttime = time.time()

    print(f"\nInitializing {label} Run ({minrange} to {maxrange})...")
    print(f"Conjecture: {q}n + {r} | Limit: {limit} steps")
    
    tasks = []
    current = minrange
    if STEP == 1:
        while current <= maxrange:
            endchunk = min(current + CHUNK_SIZE, maxrange + 1)
            tasks.append((current, endchunk, STEP, q, r, limit))
            current = endchunk
    else:
        while current >= maxrange:
            endchunk = max(current - CHUNK_SIZE, maxrange - 1)
            tasks.append((current, endchunk, STEP, q, r, limit))
            current = endchunk

    with multiprocessing.Pool() as pool:
        allresults = pool.starmap(run_range_dynamic, tasks)

    flatresults = [item for sublist in allresults for item in sublist]
    processedtotal = len(flatresults)
    elapsedtime = time.time() - starttime
    
    filename = f"Range_{minrange}_to_{maxrange}_{q}n+{r}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Number", "Fate", "Steps"])
        writer.writerows(flatresults)

    fates = [r[1] for r in flatresults]
    print(f"\n{'='*40}")
    print(f"Research Log: Completion of Custom Range")
    print(f"{'='*40}")
    print(f"Total Time: {elapsedtime:.2f} seconds")
    print(f"Average Speed: {processedtotal/elapsedtime:.0f} numbers/sec")
    print("-" * 40)

    for fate in sorted(set(fates)):
        count = fates.count(fate)
        percentage = (count / processedtotal) * 100
        print(f"{fate}: {count} numbers ({percentage:.2f}%)")
    
    print("-" * 40)
    print(f"Data saved to: {filename}\n")
    input("Press Enter to exit...")
    sys.exit(0)