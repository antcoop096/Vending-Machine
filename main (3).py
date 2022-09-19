

drink_list = [['Coke',1.50],['Sprite',1.75],['Water', 1.00],['Boxed Water',10.00]]
 
print('Choose a drink:')
for drink in drink_list:
  print(drink)
 
#Write the rest of the code below:

drink_selection = input()
if drink_selection == 'Coke' or 'Sprite' or 'Water' or 'Boxed Water':
  print('Your selection:',drink_selection)
 #Coke
  if drink_selection == 'Coke':
   print('That will be $1.50')
   amount = float(input())
   if amount < 1.50:
    print('Sorry,that is not enough money for this drink...')
   elif amount == 1.50:
    print("Perfect! Thank you and enjoy your drink!")
   elif amount > 1.50:
    print('You will receive', amount - 1.50,'in change. Thank you and enjoy your drink!')
   else:
    ('Thats not a payment.')
   #Sprite
  elif drink_selection == 'Sprite':
   print('That will be $1.75')
   amount = float(input())
   if amount < 1.75:
    print('Sorry,that is not enough money for this drink...')
   elif amount == 1.75:
    print("Perfect! Thank you and enjoy your drink!")
   elif amount > 1.75:
    print('You will receive', amount - 1.75,'in change. Thank you and enjoy your drink!')
   else: ('Thats not a payment.')
   #Water
  elif drink_selection == 'Water':
   print('That will be $1.00')
   amount = float(input())
   if amount < 1.00:
    print('Sorry,that is not enough money for this drink...')
   elif amount == 1.00:
    print("Perfect! Thank you and enjoy your drink!")
   elif amount > 1.00:
    print('You will receive', amount - 1.00,'in change. Thank you and enjoy your drink!')
   else: ('Thats not a payment.')
   #Boxed Water
  elif drink_selection == 'Boxed Water':
   print('That will be $10.00')
   amount = float(input())
   if amount < 10.00:
    print('Sorry,that is not enough money for this drink...')
   elif amount == 10.00:
    print("Perfect! Thank you and enjoy your drink!")
   elif amount > 10.00:
    print('You will receive', amount - 10.00,'in change. Thank you and enjoy your drink!')
   else:
    ('Thats not a payment.')
  elif drink_selection != 'Coke' or 'Sprite' or 'Water' or 'Boxed Water':
   print('That is not a drink that we offer. Please choose a drink that we offer.')
else:
  print('Please choose a drink that we offer.')


 

