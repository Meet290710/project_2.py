print("welcome to the pattern gentator and number analyzer!")

while True:
    print("select an option")
    print("1.Generator Pattern")
    print("2. Number Analyzer")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        n = int(input("Enter number of rows the pattern: "))

        print("\nStar Pattern:")
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end=" ")
            print()

   
    elif choice == 2:
     start = int(input("Enter the start of the range: "))
     end = int(input("Enter the end of the range: "))

     total = 0

     for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number {num} is Even")
        else:
            print(f"nNumber {num} is Odd")

        total += num

     print("Sum of all numbers from", start,"to",end,"is",total)
     
      
    elif choice == 3:
        print("exiting the program. goodbyy!")
        break

    
    else:
        print("Invalid choice! Try again.")
        continue
