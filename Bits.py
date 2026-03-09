import sys
sys.set_int_max_str_digits(10000000)
try:
    number = int(input("Input a number to find its bit length: "))
except ValueError:
    print("Invalid input")
    input("Press Enter to exit")
    sys.exit(1)

bit_length = number.bit_length()

print(f"The number of decimal digits is: {len(str(number))}")
print(f"The bit length is: {bit_length}")
input("Press Enter to exit")
sys.exit(1)