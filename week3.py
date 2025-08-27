def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is 20% or higher, apply it; otherwise return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print result
    if discount_percentage >= 20:
        print(f"Discount applied! The final price is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
