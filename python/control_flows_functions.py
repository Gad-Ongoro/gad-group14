"""
1. Create a function named calculate_discount(price, discount_percent) 
    that calculates the final price after applying a discount. 
    The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.

2. Using the calculate_discount function, 
    prompt the user to enter the original price of an item and the discount percentage. 
    Print the final price after applying the discount, or if no discount was applied, print the original price.
"""


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# user input
price = float(input("Enter item price: "))
discount_percent = float(input("Enter discount percentage: "))

# final price
final_price = calculate_discount(price, discount_percent)

print(f"The final price is: ${final_price:.2f}")


# res
"""

>_$ Enter the original price of the item: 100
>_$ Enter the discount percentage: 25
>_$ The final price is: $75.00

"""
