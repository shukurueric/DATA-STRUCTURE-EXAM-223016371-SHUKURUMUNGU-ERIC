class FixedOrderArray:
    
    def __init__(self, size):
        self.size = size
        self.orders = [None] * size  
        self.count = 0  
    def add_order(self, order):
        if self.count < self.size:
            self.orders[self.count] = order
            self.count += 1
            return True
        else:
            return False 

    def remove_order(self, index):
        if 0 <= index < self.count:
            for i in range(index, self.count - 1):
                self.orders[i] = self.orders[i + 1]
            self.orders[self.count - 1] = None  
            self.count -= 1
            return True
        else:
            return False  
    def display_orders(self):
        return [order for order in self.orders if order is not None]
fixed_array = FixedOrderArray(5)  
fixed_array.add_order("Order 1: Fix elevator")
fixed_array.add_order("Order 2: Replace HVAC filter")
fixed_array.add_order("Order 3: Inspect fire alarm")
print("Current Orders:", fixed_array.display_orders())
fixed_array.remove_order(1)  
print("Updated Orders:", fixed_array.display_orders())
fixed_array.add_order("Order 4: Check lighting system")
fixed_array.add_order("Order 5: Test water pump")
fixed_array.add_order("Order 6: Update software") 
print("Final Orders:", fixed_array.display_orders())
