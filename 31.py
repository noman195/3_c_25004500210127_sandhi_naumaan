inventory={"Pen":20,"Book":12,"Pencil":30}
for name,qty in sorted(inventory.items()): print(name,qty)
item=input("Item to update: "); inventory[item]=int(input("New quantity: ")); print(inventory)
