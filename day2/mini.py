product_price = "1500.50"
quantity = "8"
discount = "500"

corrected_product_price = float(product_price)
corrected_quantity = int(quantity)
corrected_discount = float(discount)

gross_revenue = corrected_product_price*corrected_quantity
final_revenue = gross_revenue-corrected_discount
print(gross_revenue)
print(final_revenue)