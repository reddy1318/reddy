class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total(self):
        return self.price * self.quantity
class Bill:
    def __init__(self):
        self.items = {}
    def add_item(self, item):
        self.items[item.name] = item
    def calculate_total_bill(self):
        return sum(item.calculate_total() for item in self.items.values())
def main():
    bill = Bill()
    items = [("TV",40000,1 ), ("Mobile",12000 ,3 )]
    bill.items = {name: Item(name, price, quantity) for name, price, quantity in items}
    print("Bill Details:")
    total_bill = bill.calculate_total_bill()
    for item in bill.items.values():
        print(f"{item.name}: Price - {item.price}, Quantity - {item.quantity}, Total - {item.calculate_total()}")   
    print(f"Total Bill Amount: {total_bill}")
if __name__ == "__main__":
    main()