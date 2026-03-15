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
            loop_members = []
            curr = tortoise
            while True:
                loop_members.append(curr)
                curr = calc(curr, q, r)
                if curr == tortoise: break

            pos_m = [m for m in loop_members if m > 0]
            if pos_m:
                min_bits = min(m.bit_length() for m in pos_m)
                loop_val = min([m for m in pos_m if m.bit_length() == min_bits])
                return (n, f"Loop {loop_val}", steps)
            else:
                return (n, f"Loop {max(loop_members)}", steps)
        
    return (n, "Exceeded", steps)

def run_range_dynamic(start, end, step, q, r, limit):
    results = []
    for i in range(start, end, step):
        results.append(get_fate(i, q, r, limit))
    return results

def calc(num, q, r):
    num = num >> 1 if (num & 1) == 0 else num * q + r
    return num

if __name__ == "__main__":
    try:
        print("Welcome to the qn+r Conjecture Million Tester")
        q_val = int(input("Enter 'q' (Standard would be 3): "))
        r_val = int(input("Enter 'r' (Standard would be 1): "))
        step_limit = int(input("Enter Step Limit (e.g., 1000): "))
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
    start_time = time.time()

    print(f"\n[*] Initializing {label} Mega-Run...")
    print(f"[*] Conjecture: {q_val}n + {r_val} | Limit: {step_limit} steps")
    
    tasks = []
    if STEP == 1:
        for i in range(START, END + 1, CHUNK_SIZE):
            chunk_end = min(i + CHUNK_SIZE, END + 1)
            tasks.append((i, chunk_end, STEP, q_val, r_val, step_limit))
    else:
        for i in range(START, END - 1, -CHUNK_SIZE):
            chunk_end = max(i - CHUNK_SIZE, END - 1)
            tasks.append((i, chunk_end, STEP, q_val, r_val, step_limit))

   
    with multiprocessing.Pool() as pool:
        all_results = pool.starmap(run_range_dynamic, tasks)

    
    flat_results = [item for sublist in all_results for item in sublist]
    elapsed_time = time.time() - start_time
    
    filename = f"{label}_Results_{q_val}n+{r_val}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Number", "Fate", "Steps"])
        writer.writerows(flat_results)

    fates = [r[1] for r in flat_results]
    print(f"\n{'='*40}")
    print(f"RESEARCH LOG: {label.upper()} MILLION COMPLETE")
    print(f"{'='*40}")
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print(f"Average Speed: {1000000/elapsed_time:.0f} numbers/sec")
    print("-" * 40)

    for fate in sorted(set(fates)):
        count = fates.count(fate)
        percentage = (count / 1000000) * 100
        print(f"{fate}: {count} numbers ({percentage:.2f}%)")
    
    print("-" * 40)
    print(f"Data saved to: {filename}\n")
    input("Press Enter to exit..")
    sys.exit(1)