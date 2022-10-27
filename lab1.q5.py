#A program that inputs 5 numbers from the user in a loop and finds the sum of the numbers

#Ask the user to input the numbers listed

#Loop through the numbers and calculate sum output


def main():
    print()
    print("Enter five numbers.")


    n = 5
    sum = 0


    for i in range (n):
        number = int(input(f"Enter number{i + 1} > "))
        sum = sum + number


    print(f"The sum of the {n} numbers is {sum}")


main()
