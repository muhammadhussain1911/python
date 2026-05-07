age = int(input("Tell your age."));

# if age>= 18:
#   eligibility = "You are eligible for vote:"
# else:
#   eligibility = "You are not eligible for vote."

# print(eligibility);


ticket_price_for_adults = 1200;
ticket_price_for_children = 800;
day = (input("Tell the day of the week:")).lower();

if age>=18 and day!= "wednesday":
  print("You have to pay: ", ticket_price_for_adults);
elif age<18 and day!= "wednesday":
  print("You have to pay: ", ticket_price_for_children);
elif age>=18 and day== "wednesday":
  print("You have to pay: ", ticket_price_for_adults-200);
else:
  print("You have to pay: ", ticket_price_for_children-200);
