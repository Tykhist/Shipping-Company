# Ground Shipping
def ground_shipping(weight, premium=False):
  if weight <= 2:
    cost = weight * 1.50
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00
  else:
    cost = weight * 4.75

  # Premium cost is static, regardless of weight
  if premium:
    cost = 100
  cost += 20
  print(f"Price: ${cost:.2f}")

# Drone Shipping
def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  print(f"Price: ${cost:.2f}")

# Price display

lbs = 8.4 # int(input("What is the total weight of your shipment?\n"))
ground_shipping(lbs)
ground_shipping(lbs, True)
print()

lbs = 1.5
drone_shipping(lbs)
print()

# Which method is cheaper for a 4.8 lb package?
lbs = 4.8
ground_shipping(lbs)
ground_shipping(lbs, True)
drone_shipping(lbs)
print()

# Which method is cheaper for a 41.5 lb package?
lbs = 41.5
ground_shipping(lbs)
ground_shipping(lbs, True)
drone_shipping(lbs)
print()
