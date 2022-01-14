def to_hrs_and_minutes(num):
   hours = num//60
   minutes = num % 60
   if hours > 1 and minutes > 1 or hours == 0 and minutes == 0:
      print (f"{hours} hours, {minutes} minutes")
   elif hours == 1 and minutes == 1:
      print (f"{hours} hour, {minutes} minute")
   elif hours > 1 and minutes == 1:
      print (f"{hours} hours, {minutes} minute")
   elif hours == 1 and minutes > 1:
      print (f"{hours} hour, {minutes} minutes")
   elif hours == 0 and minutes > 1:
      print (f"{hours} hours, {minutes} minutes")
   elif hours > 1 and minutes ==  0:
      print (f"{hours} hours, {minutes} minutes")
   else: 
      print (f"{hours} hours, {minutes} minute")


to_hrs_and_minutes(133)
