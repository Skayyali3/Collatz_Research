import random
import time
import sys

sys.set_int_max_str_digits(0) 
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

def Titan_Hunter():
    print("Welcome to the Titan Hunter!")
    try:
        q = int(input("Enter value 'q' for qn+r conjecture: "))
        r = int(input(f"Enter value 'r' for qn+r conjecture: "))
        limit = input("Step Limit (be careful and try to not make it more than your RAM can handle): ")
        
        choice = input("Do you want to start with a positive or a negative 1000-digit number (p/n): ").lower()

        n = random.randint(10**999, 10**1000)
        if choice == 'n':
            n = -n
        
        print(f"Beginning {q}n+{r} testing on a {'positive' if n > 0 else 'negative'} 1000-digit number")
    except ValueError:
        print("Invalid input.")
        input("Press Enter to exit")
        sys.exit(1)

    start_time = time.time()
    tortoise = n
    hare = n
    max_bits = n.bit_length()
    limit = parse_collatz(str(limit))

    print(f"\n Launching Titan ({tortoise.bit_length()} bits)...")

    for i in range(1, limit + 1):
        tortoise = calc(tortoise, q, r)
        hare = calc(calc(hare, q, r), q, r)

        if tortoise.bit_length() > max_bits:
            max_bits = tortoise.bit_length()

        if tortoise.bit_length() > 500000 or hare.bit_length() > 500000:
            print(f"\nEMERGENCY STOP at step {i}: Magnitude reached 500,000 bits.")
            print("Stopping to protect your RAM")
            print(f"Peak amount of bits was: {max_bits}")
            break 
        
        if tortoise == hare:
            meeting_point = tortoise
            print(f"\nLOOP FOUND at step {i}!")
            loop_members=[]
            while True:
                loop_members.append(tortoise)
                tortoise = calc(tortoise, q, r)
                if tortoise == meeting_point:
                    break
            if any(abs(m) > 100000 for m in loop_members):
                filename = f"loop_{q}n+{r}_step{i}.txt"
                with open(filename, "w") as f:
                    f.write(f"Conjecture: {q}n+{r}\n")
                    f.write(f"Peak amount of bits was: {max_bits}")
                    f.write(f"Loop Length: {len(loop_members)}\n")
                    f.write(f"Members: {loop_members}\n")
                print(f"[*] Large numbers detected. Loop saved to {filename} to keep console clean.")
            else:
                print(f"Loop Members: {loop_members} which is a {len(loop_members)} step loop.\n Largest amount of bits was {max_bits}")
            break
            
        if i % 50000 == 0:
            print(f"Step {i//1000}k: {tortoise.bit_length()} bits | {time.time()-start_time:.2f}s")

    else:
        print(f"\nFinished at {limit} steps.")
        print(f"Final Magnitude: {tortoise.bit_length()} bits")

    print(f"Total Time: {time.time() - start_time:.4f} seconds")
    input("Press Enter to exit..")

def calc(num, q, r):
    num = num >> 1 if (num & 1) == 0 else num * q + r
    return num
    
if __name__ == "__main__":
    Titan_Hunter()