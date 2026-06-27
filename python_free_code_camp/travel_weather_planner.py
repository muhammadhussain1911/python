distance_mi = 10
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if distance_mi == False:
  print('False')
elif distance_mi <= 1 and is_raining == False:
  print('True')
elif distance_mi <= 1 and is_raining == True:
  print('False')
elif distance_mi > 1 and distance_mi <= 6:
  if has_bike == True and is_raining == False:
    print('True')
  else:
    print('False')
elif distance_mi > 6:
  if has_car == True or has_ride_share_app == True:
    print('True')
  else:
    print('False')




# More optimized code:

distance_mi = 10
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
  print('False')
elif distance_mi <= 1 and not is_raining:
  print('True')
elif distance_mi <= 1 and is_raining:
  print('False')
elif distance_mi > 1 and distance_mi <= 6:
  if has_bike and not is_raining:
    print('True')
  else:
    print('False')
elif distance_mi > 6:
  if has_car or has_ride_share_app:
    print('True')
  else:
    print('False')