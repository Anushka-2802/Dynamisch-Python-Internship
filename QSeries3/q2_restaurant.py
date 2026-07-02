class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self):
        n = int(input("Number of time you want to add menu: "))
        for i in range(n):
            item = input("Enter Menu Item: ")
            price = int(input("Enter price of item: "))
            self.menu_items[item] = price
        print(item, "\nMenu added successfully")

    def print_menu(self):
        print("\n====== MENU ======")

        for item, price in self.menu_items.items():
            print(item, ":", price)

    def book_tables(self):
        table_no = input("\nEnter table number you have to book: ")

        self.book_table.append(table_no)
        print("Table", table_no, "Booked")

    # Print reserved tables
    def print_reservation(self):
        print("\n====== RESERVED TABLES ======")
        for table_no in self.book_table:
            print("Table", table_no)

    def take_customer_orders(self):
        table_no = input("Enter table number: ")
        order = input("Enter order you want: ")

        self.customer_orders.append({"Table No": table_no, "Order": order})

        print("Order placed successfully")

    def print_customer_order(self):
        print("\n====== CUSTOMER ORDERS ======")

        for order in self.customer_orders:
            print(order)


obj = Restaurant()
obj.add_item_to_menu()
obj.print_menu()
obj.book_tables()
obj.print_reservation()
obj.take_customer_orders()
obj.print_customer_order()
