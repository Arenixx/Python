#Shop stock and target hit?

quantity = int(input("What is the current stock level? "))
target = int(input("What is the sales target? "))
product_sold = int(input("How much of the product has been sold? "))

current_stock = quantity - product_sold
print("There is currently", current_stock, "of the product left in stock")

target_hit = product_sold >= target

if target_hit:
  print("Target was met, you are", product_sold - target, "over the target!")
else: 
  print("Target not met, you are", target - product_sold, "product sales behind!")