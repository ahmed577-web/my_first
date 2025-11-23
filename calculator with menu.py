while True:
    print("\nMain Menu")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        a = int(input("Enter the first value: "))
        b = int(input("Enter the second value: "))
        print("Result:", a + b)

    elif choice == '2':
        a = int(input("Enter the first value: "))
        b = int(input("Enter the second value: "))
        print("Result:", a - b)

    else:
        print("Invalid choice. Please enter 1 or 2")
        continue


    again = input("\nDo you want to perform another operation? (y/n): ").lower()
    if again != 'y':
        print("Exiting the calculator. Goodbye!")
        break


