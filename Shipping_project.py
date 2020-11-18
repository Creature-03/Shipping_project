#Ground shipping rate:
#Flat charge plus price per pound:

#Drone Shipping rate:
#No flat charge, increased price per pound

#Premium ground shipping rate:
#Flat charge, no price per pound


#Cost of the flat charge added to ground shipping
ground_shipping_flat_charge = 20.00

#Cost of premium ground shipping
premium_ground_shipping = 125

#Ground shipping weight rates
ground_two_lbs_and_under = 1.50
ground_two_to_six = 3.00
ground_six_to_ten = 4.00
ground_over_ten = 4.75

#Drone shipping rates
drone_two_lbs_and_under = 4.50
drone_two_to_six = 9.00
drone_six_to_ten = 12.00
drone_over_ten = 14.25

wt = input("How much does your package weigh? ")

def ground_shipping(weight):
  if weight <= 2:
    pp_cost = weight * ground_two_lbs_and_under
  elif weight > 2 and weight <= 6:
    pp_cost = weight * ground_two_to_six
  elif weight > 6 and weight <= 10:
    pp_cost = weight * ground_six_to_ten
  elif weight > 10:
    pp_cost = weight * ground_over_ten
  cost = pp_cost + ground_shipping_flat_charge
  return cost


def drone_shipping(weight):
  if weight <= 2:
    cost = weight * drone_two_lbs_and_under
  elif weight > 2 and weight <= 6:
    cost = weight * drone_two_to_six
  elif weight > 6 and weight <= 10:
    cost = weight * drone_six_to_ten
  elif weight > 10:
    cost = weight * drone_over_ten
  return cost

def most_efficient(weight):
  if ground_shipping(weight) <= drone_shipping(weight) and ground_shipping(weight) <= premium_ground_shipping:
    return "The most cost efficient shipping is Ground Shipping, it will cost: ", ground_shipping(weight)
  elif drone_shipping(weight) <= ground_shipping(weight) and drone_shipping(weight) <= premium_ground_shipping:
    return "The most cost efficient shipping is Drone Shipping, it will cost: ", drone_shipping(weight)
  elif premium_ground_shipping <= ground_shipping(weight) and premium_ground_shipping <= drone_shipping(weight):
    return "The most cost efficient shipping is Premium Ground Shipping, it will cost: ", premium_ground_shipping

best_deal = most_efficient(int(wt))
print(best_deal)