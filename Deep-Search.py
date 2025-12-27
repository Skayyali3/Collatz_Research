import sys
sys.set_int_max_str_digits(1000000)
try:
    q=int(input("Enter the 'q' value for the qn+r conjecture : "))
    r=int(input("Enter the 'r' value for the qn+r conjecture : "))
    start_n = int(input(f"Enter an integer to test the {q}n+{r} conjecture:"))
except ValueError:
    print("Error: Please enter valid integers only.")
    sys.exit(1)


n = start_n
steps = 0
limit = input("Enter the maximum number of steps to search (e.g., 1000000): ")
try:
    limit = int(limit)
except ValueError:
    print("Error: Please enter a valid integer for the step limit.")
    sys.exit(1)

print(f"\nStarting Deep Search for {n} using {q}n+{r}...")
seen={n}
while n != 1 and steps < limit:
    if n % 2 == 0:
        n //= 2
    else:
        n = q * n + r
    
    if len(str(n)) > 1000: # If it exceeds 1000 digits, it's probably diverging
        print(f"DIVERGENCE LIKELY: Value exceeded 1000 digits at step {steps}.")
        break
    if n in seen:
        print(f"\nLOOP DETECTED at step {steps + 1}!")
        print(f"The number {n} has appeared again.")
        break

    seen.add(n)
    steps += 1
    
    # Print progress every 10,000 steps to keep the console clean
    if steps % 10000 == 0:
        print(f"Step {steps}: Current value is {n} and has {len(str(n))} digits.")

if n == 1:
    print(f"SUCCESS: {start_n} reached 1 in {steps} steps!")
elif steps >= limit:
    print(f"LIMIT REACHED: Stopped after {steps} steps without reaching 1.")
    print(f"Last value: {n} ({len(str(n))} digits)")
    
elif n in seen:
    print(f"\n LOOP DETECTED!")
    loop_members = []
    curr = n
    while True:
        loop_members.append(curr)
        # Apply the rule one more time to find the next member
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = q * curr + r
        if curr == n: # We've come full circle
            break
            
    print(f"Cycle detected: {loop_members}")
    print(f"Cycle length: {len(loop_members)} steps.")
elif len(str(n)) > 1000:
    print(f"STOPPED: Divergence detected at {len(str(n))} digits.")
else:
    print(f"LIMIT REACHED: Stopped after {steps} steps without reaching 1.")
input("Press Enter to exit...")