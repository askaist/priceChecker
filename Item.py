class Item:
    def __init__(self, name, price, url, weight, category=None):
        self.name = name
        self.price = price
        self.category = category
        self.url = url
        self.weight = weight

    def __str__(self):
        item_info = f"Name: {self.name}\nPrice: ${self.price:.2f}\nWeight: {self.weight} units"
        if self.category:
            item_info += f"\nCategory: {self.category}"
        item_info += f"\nURL: {self.url}"
        return item_info
