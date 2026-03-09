import random
import time
import sys

sys.set_int_max_str_digits(0) 

def Titan_Hunter():
    print("Welcome to the Titan Hunter!")
    try:
        q = int(input("Enter value 'q' for qn+r conjecture: "))
        r = int(input(f"Enter value 'r' for {q}n+r conjecture: "))
        limit = int(input("Step Limit (be careful and try to not make it more than your RAM can handle): "))
        
        choice = input("Do you want to start with a positive or a negative 1000-digit number (p/n): ").lower()

        n = random.randint(10**999, 10**1000)
        if choice == 'n':
            n = -n
        
        print(f"Beginning {q}n+{r} testing on a {'positive' if n > 0 else 'negative'} 1000-digit number")
    except ValueError:
        print("Invalid input.")
        input("Press Enter to exit")
        sys.exit(1)

    seen = {} 
    start_time = time.time()
    curr_n = n
    max_bits=n.bit_length()

    print(f"\n Launching Titan ({curr_n.bit_length()} bits)...")

    for i in range(1, limit + 1):
        if curr_n.bit_length()>max_bits:
            max_bits=curr_n.bit_length()

        if curr_n.bit_length() > 500000:
            print(f"\nEMERGENCY STOP at step {i}: Magnitude reached 500,000 bits.")
            print("Stopping to protect your RAM")
            print(f"Peak amount of bits was: {max_bits}")
            break
        
        if -20000 < curr_n < 20000:
            if curr_n in seen:
                meeting_point = curr_n
                print(f"\nLOOP FOUND at step {i}!")
                loop_members=[]
                while True:
                    loop_members.append(curr_n)
                    if curr_n % 2 == 0:
                        curr_n //= 2
                    else:
                        curr_n = q * curr_n + r
                    if curr_n == meeting_point:
                     break
                if any(abs(m) > 1000000 for m in loop_members):
                    filename = f"loop_q{q}_r{r}_step{i}.txt"
                    with open(filename, "w") as f:
                        f.write(f"Conjecture: {q}n+{r}\n")
                        f.write(f"Peak amount of bits was: {max_bits}")
                        f.write(f"Loop Length: {len(loop_members)}\n")
                        f.write(f"Members: {loop_members}\n")
                    print(f"[*] Large numbers detected. Loop saved to {filename} to keep console clean.")
                else:
                    print(f"Loop Members: {loop_members} which is a {len(loop_members)} step loop.\n Largest amount of bits was {max_bits}")
                break
                
            seen[curr_n] = i
        
        if curr_n % 2 == 0:
            curr_n //= 2
        else:
            curr_n = q * curr_n + r
            
        if i % 50000 == 0:
            print(f"Step {i//1000}k: {curr_n.bit_length()} bits | {time.time()-start_time:.2f}s")

    else:
        print(f"\nFinished at {limit} steps.")
        print(f"Final Magnitude: {curr_n.bit_length()} bits")

    print(f"Total Time: {time.time() - start_time:.4f} seconds")
    input("Press Enter to exit..")
    
if __name__ == "__main__":
    Titan_Hunter()