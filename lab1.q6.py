#Ask the user to input the looped numbers and calculate the average
#Output the sum of the numbers and its average


def main():
    print()
    print("Enter five numbers.")


    n = 5
    sum = 0


    for i in range (n):
        number = int(input(f"Enter number{i + 1} > "))
        sum = sum + number


    average = sum / n

    print(f"The sum is {sum} and average is {average}")


main()
    


