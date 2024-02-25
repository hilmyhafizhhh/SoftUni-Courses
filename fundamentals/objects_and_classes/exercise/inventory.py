class Inventory:
    def __init__(self, capacity: int ):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.__capacity - len(self.items)
        returning_items = ', '.join(self.items)
        return f"Items: {returning_items}.\nCapacity left: {left_capacity}"
