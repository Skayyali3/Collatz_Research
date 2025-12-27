import sys
sys.set_int_max_str_digits(1000000)
def parse_collatz(val):
    val = val.replace(" ", "").lower()
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




try:
    print("Welcome to the Deep Search for the qn+r Conjecture!\nEnter the parameters for the conjecture and a starting integer.")
    print("You can test large numbers using scientific notation or exponentiation (e.g., 2.7e64, 2^64, 2.7*10^64, 2.7*10**64).")
    print("Note: you can only input integers as values for q and r.\n")
    print("WARNING: Don't input large numbers for q and r as they should be small integers, typically q=3 and r=1 for the classic Collatz conjecture.")
    print("WARNING: Don't input numbers larger than your RAM can handle as this program uses arbitrary-precision integers which can consume a lot of memory.")
    print("WARNING: Be aware that even testing extremely high numbers in small conjectures may cause issues within your RAM.")
    print("\nNote: Large numbers may take significant time to process.\n")

    q=int(input("Enter the 'q' value for the qn+r conjecture : "))
    r=int(input("Enter the 'r' value for the qn+r conjecture : "))
    start_n = input(f"Enter an integer to test the {q}n+{r} conjecture:")
except ValueError:
    print("Error: Please enter valid integers only.")
    input("Press Enter to exit...")
    sys.exit(1)



n = parse_collatz(str(start_n))
if n is None:
    print("Invalid starting value.")
    input("Press Enter to exit...")
    sys.exit(1)


steps = 0
limit = input("Enter the maximum number of steps to search (e.g., 1000000): ")
cont_after_1 = input("Continue simulation after reaching 1? (y/n): ").strip().lower()
continue_after_one = cont_after_1 == "y"

mode = "Continued" if continue_after_one else "Stopped at 1"
print(f"Mode: {mode}")
try:
    limit = int(limit)
except ValueError:
    print("Error: Please enter a valid integer for the step limit.")
    sys.exit(1)

print(f"\nStarting Deep Search for {n} using {q}n+{r}...")
seen=set()
seen.add(n)
while (n != 1 or continue_after_one) and steps < limit:
    steps+=1
    if n % 2 == 0:
        n //= 2
    else:
        n = q * n + r
    
    if n.bit_length() > 3322: # If it exceeds 1000 digits, it's probably diverging
        print(f"DIVERGENCE LIKELY: Value exceeded 1000 digits at step {steps}.")
        break
    if n in seen:
        print(f"\nLOOP DETECTED at step {steps}!")
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
        print(f"Full loop cycle: {loop_members}")
        print(f"Cycle length: {len(loop_members)}")
        
        break
    seen.add(n)
    
    
    # Print progress every 10,000 steps to keep the console clean
    if steps % 10000 == 0:
        print(f"Step {steps}: Current value is {n} and has {len(str(n))} digits.")

if n == 1 and not continue_after_one:
    print(f"SUCCESS: {start_n} reached 1 in {steps} steps!")
elif steps >= limit:
    print(f"LIMIT REACHED: Stopped after {steps} steps..")
    print(f"Last value: {n} ({len(str(n))} digits)")
    
elif n.bit_length() > 3322:
    print(f"STOPPED: Divergence detected at {len(str(n))} digits.")
else:
    print(f"LIMIT REACHED: Stopped after {steps} steps.")
input("Press Enter to exit...")
sys.exit(0)