class Cart:
  flat_discount = 0
  min_bill = 100
  def __init__(self):
      self.items = {}
  def add_item(self,item_name,quantity):
      self.items[item_name] = quantity
  def display_items(self):
      print(self.items)
a = Cart()
print(Cart.min_bill)
a.add_item("pen",4)
print(a.items)
a.display_items()