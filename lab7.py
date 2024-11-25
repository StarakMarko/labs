"""№23 => №8"""


class BoxesStack:
    """A class for implementing a stack of boxes"""

    def __init__(self, boxes=None):
        if boxes is None:
            boxes = []
        self.boxes = boxes

    def add_box(self, box):
        """Add box to stack"""
        self.boxes.append(box)

    def get_box(self):
        """Get the top box from the stack"""
        return self.boxes.pop()


class RestaurantQueue:
    """Class for implementing an order queue"""

    def __init__(self, orders=None):
        if orders is None:
            orders = []
        self.orders = orders

    def add_order(self, box):
        """Add order to queue"""
        self.orders.append(box)

    def get_order(self):
        """Get the first order in the queue"""
        return self.orders.pop(0)


stack = BoxesStack()
stack.add_box("box 1")
stack.add_box("box 2")
stack.add_box("box 3")
print(stack.get_box())

queue = RestaurantQueue()
queue.add_order("order 1")
queue.add_order("order 2")
queue.add_order("order 3")
print(queue.get_order())
