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

def calc(num, q, r):
    num = num >> 1 if (num & 1) == 0 else num * q + r
    return num
try:
    print("Welcome to the Deep Search for the qn+r Conjecture!\nEnter the parameters for the conjecture and a starting integer.")
    print("You can test large numbers using scientific notation or exponentiation (e.g., 2.7e64, 2^64, 2.7*10^64, 2.7*10**64).")
    print("Note: you can only input integers as values for q and r.\n")
    print("WARNING: Don't input large numbers for q and r as they should be small integers, typically q=3 and r=1 for the classic Collatz conjecture.")
    print("WARNING: Don't input numbers larger than your RAM can handle as this program uses arbitrary-precision integers which can consume a lot of memory.")
    print("WARNING: Be aware that even testing extremely high numbers in small conjectures may cause memory issues.")
    print("\nNote: Large numbers may take significant time to process.\n")

    q=int(input("Enter the 'q' value for the qn+r conjecture: "))
    r=int(input("Enter the 'r' value for the qn+r conjecture: "))
    n = input(f"Enter an integer to test the {q}n+{r} conjecture: ")
    bit=int(input("Enter the maximum number of bits allowed for each number: \n(If you don't know how many bits the max number of digits you want to allow is,\n use the Bits.py tool then come back and enter)\n"))
except ValueError:
    print("Error: Please enter valid integers only.")
    input("Press Enter to exit...")
    sys.exit(1)

n = parse_collatz(str(n))
if n is None:
    print("Invalid starting value.")
    input("Press Enter to exit...")
    sys.exit(1)

steps = 0
limit = input("Enter the maximum number of steps to search (e.g., 1000000): ")
cont_after_1 = input("Continue simulation after reaching 1? (y/n): ").strip().lower()
continue_after_one = cont_after_1 == "y"

limit = parse_collatz(str(limit))
tortoise = n
hare = n

mode = "Continued" if continue_after_one else "Stopped at 1"
print(f"Mode: {mode}")
try:
    limit = int(limit)
except ValueError:
    print("Error: Please enter a valid integer for the step limit.")
    sys.exit(1)

print(f"\nStarting Deep Search for {n} using {q}n+{r}...")

while (tortoise != 1 or continue_after_one) and steps < limit:
    steps += 1
    tortoise = calc(tortoise, q, r)

    harestep1 = calc(hare, q, r)
    harestep2 = calc(harestep1, q, r)

    hare = harestep2
    if hare.bit_length() > bit or harestep1.bit_length() > bit or harestep2.bit_length() > bit or tortoise.bit_length() > bit: 
        print(f"DIVERGENCE LIKELY: Value exceeded {bit} bits at step {steps}.")
        break
    if tortoise == hare:
        print(f"\nLOOP DETECTED at step {steps}!")
        loopmems = []
        curr = tortoise
        while True:
           loopmems.append(curr)
           curr = calc(curr, q, r)
           if curr == tortoise:
                break
        pos_number=[num for num in loopmems if num > 0]
        if pos_number:
            min_digits = min(num.bit_length() for num in pos_number)
            candidates = [num for num in pos_number if num.bit_length() == min_digits]
            loop_name=min(candidates)
        else:
            loop_name=min(loopmems)
        print(f"Full loop cycle: {loopmems}" if len(loopmems) < 100 else "Loop cycle too long to display.")
        print(f"Cycle length: {len(loopmems)}")
        print(f"This is the {loop_name} loop of the {q}n + {r} conjecture.")
        break
    
    if steps % 10000 == 0 or tortoise < 1000000:
        display_val = tortoise if tortoise < 10**15 else f"{tortoise.bit_length()} bits"
        print(f"Step {steps}: Current value is {display_val} and has {len(str(tortoise))} digits.")

if tortoise == 1 and not continue_after_one:
    print(f"SUCCESS: {n} reached 1 in {steps} steps!")
elif steps >= limit:
    print(f"LIMIT REACHED: Stopped after {steps} steps..")
    print(f"Last value: {tortoise} ({len(str(tortoise))} digits)")

elif tortoise.bit_length() > bit:
    print(f"STOPPED: Divergence detected at {len(str(tortoise))} digits.")
else:
    print(f"LIMIT REACHED: Stopped after {steps} steps.")
input("Press Enter to exit...")
sys.exit(0)