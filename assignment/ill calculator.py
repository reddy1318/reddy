class BillCalculator:
    def _init_(self, items):
        self.items = items

    def calculate_total_bill(self):
        total_bill = sum(item['cost'] for item in self.items)
        return total_bill

    def display_quantity(self):
        for item in self.items:
            print(f"Quantity of {item['name']}: {item['quantity']}")


if __name__== '__main__':
    items = [
        {'name': 'TV', 'cost': 100, 'quantity': 2},
        {'name': 'Phone', 'cost': 50, 'quantity': 3} 
    ]
    calculator = BillCalculator(items)
    total_bill = calculator.calculate_total_bill()
    print(f'The total bill amount is: ${total_bill}')
    calculator.display_quantity()