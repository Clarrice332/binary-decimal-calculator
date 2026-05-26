def binary_to_decimal(n: str) -> int:
    decimal = 0
    for i, bit in enumerate(n):
        if bit == "1":
            decimal += 2 ** (len(n) - 1 - i)
    return decimal

def decimal_to_binary(d: int) -> str:
    binary = []
    if d == 0:
        return "0"
    while d > 0:
        binary.append(str(d % 2))
        d //= 2
    return "".join(reversed(binary))


def get_binary() -> str:
    while True:
        binary = input("Enter binary: ").strip()
        valid = True
        for n in binary:
            if n not in ["0", "1"]:
                valid = False
                break
        if not binary or not valid:
            print("Enter 1s and 0s.")
            continue
        return binary 


def get_decimal() -> int:
    while True:
        decimal = input("Enter decimal: ")
        try:
            decimal = int(decimal)
            if decimal < 0:
                print("Negative values not allowed.")
                continue
            break
        except ValueError:
            print("Invalid input.")
            continue
    return decimal

def display_menu():
    print("************************************")
    print("  Decimal and Binary calculator")
    print("************************************")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Quit")

def get_choice() -> int:
    while True:
        choice = input("Enter choice(1-3): ")
        try:
            choice = int(choice)
            if choice not in range(1, 4):
                print("Enter choice from 1-3.")
                continue
            break
        except ValueError:
            print("Invalid input")
            continue
    return choice

def main():
    while True:
        display_menu()
        choice = get_choice()
        if choice == 1:
            print(binary_to_decimal(get_binary()))
        elif choice == 2:
            print(decimal_to_binary(get_decimal()))
        else:
            print("Quitting...")
            break
        

if __name__ == "__main__":
    main()