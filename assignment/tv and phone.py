class Item:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        self.items.append(item)

    def calculate_total_bill(self):
        return sum(item.calculate_total() for item in self.items)
        
def main():
    bill = Bill()
    items=[("Tv",12000,1),("phone",30000,1)]
    for name,price,quantity in items:
        bill.add_item(name,price,quantity)
    
    while True:
        print("Please enter your bill calculator details:")
        print("1. Add an item")
        print("2. Calculate total bill")
        print("3. Exit")      
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            bill.add_item(name, price, quantity)
        elif choice == '2':
            total_bill = bill.calculate_total_bill()
            print("Bill Details:")
            for item in bill.items:
                print(f"Item: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Total: {item.calculate_total()}")
            print(f"Total Bill Amount: {total_bill}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()
        