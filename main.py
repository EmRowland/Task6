#collecting user input

IsVegiterian = input("Is anyone in your party a vegetarian? ")

IsVegiterian = IsVegiterian.capitalize()

IsVegan = input("Is anyone in your party a vegan?")

IsVegan = IsVegan.capitalize()

IsGluttonFree = input("Is anyone in your party gluten-free? ")

IsGluttonFree = IsGluttonFree.capitalize()

print(f"Your Selections are\n Vegetarian:{IsVegiterian} \n Vegan:{IsVegan} \n Gluten-Free:{IsGluttonFree}")

try:

  if IsVegiterian == "Yes" and IsVegan == "Yes" and IsGluttonFree == "Yes":

    print("Here are your restaurant choices:\n Corner Cafe \n The Chef's Kitchen \n")

    

  elif IsVegiterian == "No" and IsVegan == "No" and IsGluttonFree == "No":

    print("Here are your restaurant choices:\n Main Street Pizza Company \n")

    

  

  elif IsVegiterian == "Yes" and IsVegan == "No" and IsGluttonFree == "Yes":

    print("Here are your restaurant choices:\n Main Street Pizza Company \n Corner Cafe\n The Chef's Kitchen")

    

  

  elif IsVegiterian == "Yes" and IsVegan == "No" and IsGluttonFree == "No":

    print("Here are your restaurant choices:\n Mama’s Fine Italian \n")  

    

  else:

    print("Incorrect Combination or no place resolved for you please Re-enter :")

    

except Exception:

  print ("an Error occurred")
