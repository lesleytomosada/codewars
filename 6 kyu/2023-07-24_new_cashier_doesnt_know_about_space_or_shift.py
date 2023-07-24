# Some new cashiers started to work at your restaurant.

# They are good at taking orders, but they don't know how to capitalize words,
# or use a space bar!

# All the orders they create look something like this:

# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

# The kitchen staff are threatening to quit, because of how difficult it is to
# read the orders.

# Their preference is to get the orders as a nice clean string with spaces and
# capitals like so:

# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

# The kitchen staff expect the items to be in the same order as they appear in
#  the menu.

# The menu items are fairly simple, there is no overlap in the names of the
# items:

# 1. Burger
# 2. Fries
# 3. Chicken
# 4. Pizza
# 5. Sandwich
# 6. Onionrings
# 7. Milkshake
# 8. Coke


from collections import Counter


def get_order(order):
    menu = [
        "burger",
        "fries",
        "chicken",
        "pizza",
        "sandwich",
        "onionrings",
        "milkshake",
        "coke",
    ]

    for item in menu:
        order = order.replace(item, f"{item} ")

    order = order.split()

    menu_dict = Counter(order)
    new_order = []

    for item in menu:
        for _ in range(menu_dict[item]):
            new_order.append(item.capitalize())

    return " ".join(new_order)


def get_order1(order):
    menu = [
        "burger",
        "fries",
        "chicken",
        "pizza",
        "sandwich",
        "onionrings",
        "milkshake",
        "coke",
    ]
    clean_order = ""
    for i in menu:
        clean_order += (i.capitalize() + " ") * order.count(i)
    return clean_order[:-1]
