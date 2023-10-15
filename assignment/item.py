class Item:
    def __init__(self):
        self.phone = ""
        self.tv = ""
        self.quantity = 0
        self.total_amount = 0
    def enter_item_details(self):
        print("Please enter item details:")
        self.phone = input("Enter phone price: ")
        self.tv = input("Enter TV price: ")
        self.quantity = int(input("Enter quantity: "))
        self.calculate_total()
    def calculate_total(self):
        self.total_amount = (int(self.phone) + int(self.tv)) * self.quantity
class Bill:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, item):
        self.items[item_name] = item
    def calculate_total_bill(self):
        return sum(item.total_amount for item in self.items.values())
def main():
    bill = Bill()
    
    while True:
        print("Please enter your bill calculator details:")
        print("1. Add an item")
        print("2. Calculate total bill")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            item_name = input("Enter item name: ")
            item = Item()
            item.enter_item_details()
            bill.add_item(item_name, item)
        elif choice == '2':
            total_bill = bill.calculate_total_bill()
            print(f"Total Bill Amount: {total_bill}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()