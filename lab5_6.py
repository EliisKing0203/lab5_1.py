
import sys
import os
from math_operations import factorial, average, max_number, min_number, count_numbers, babylonian_sqrt

def print_menu():
    print("\nMenu:")
    print("1. Factorial")
    print("2. Average")
    print("3. Maximum Number")
    print("4. Minimum Number")
    print("5. Count Numbers")
    print("6. Square Root (Babylonian Method)")
    print("7. Exit")

def get_input(prompt):
    return input(prompt).strip()

def main():
    while True:
        print_menu()
        choice = get_input("\nEnter your choice (1-7): ")
        
        match choice:
            case '1':
                num = int(get_input("Enter a number to compute its factorial: "))
                print("Factorial:", factorial(num))
            case '2':
                numbers = list(map(float, get_input("Enter numbers separated by spaces: ").split()))
                print("Average:", average(numbers))
            case '3':
                numbers = list(map(float, get_input("Enter numbers separated by spaces: ").split()))
                print("Maximum Number:", max_number(numbers))
            case '4':
                numbers = list(map(float, get_input("Enter numbers separated by spaces: ").split()))
                print("Minimum Number:", min_number(numbers))
            case '5':
                print("Number of Numbers:", count_numbers())
            case '6':
                num = float(get_input("Enter a number to compute its square root: "))
                print("Square Root:", babylonian_sqrt(num))
            case '7':
                print("Exiting program...")
                sys.exit()
            case _:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
