class List:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_all(self):
        return self.items

    def __str__(self):
        return str(self.items)