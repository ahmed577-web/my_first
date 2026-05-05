

fruits = {
    1: ("apple", 100),
    2: ("banana", 80),
    3: ("orange", 150),
}
##for displaying items
def item():
    for number, (name, _) in fruits.items():
        print(f'{number},{name}')
##for displaying items price
def item_price():
   price=[{name},{price} for name, price in fruits.items()]
##for displaying items total
def total_price():
    total = 0
    for number, (_, prices) in fruits.items():
     total += prices
    print(total)
##start of menu

print("welcome")
name = (input("PLease enter your name "))
print(f'Hello {name}')
print("What do you want us to do???")
while True:
    print("\nServices"
          "es list")
    print("1. show items")
    print("2. price")
    print('3.Show my total receipt')
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        item()
    elif choice == 2:
        item_price()
    elif choice==3:
       print (f'Name:{name} ')
       print('Item purchased')

       item_price()
       print('Your total is')

       total_price()
    else:
        print('Invalid choice')
        continue
    again = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if again != 'yes':
        print(f"Thankyou {name}. Goodbye!")
        break
