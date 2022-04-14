

#for i in range(1,11):
    #print(i)



#for i in range(5,16):
    #print(i)



#for i in range(7):
 #   print("ahoj")


#for i in range(7):
   # print(i)


#x = [x for x in range(1,21,2)]
#print(x)


#for i in range(1,21,2):
    #print(i)
    
#for i in range(0,21,2):
 #   print(i)

#for i in range(10,-11,-1):
 #   print(i)



#for i in range(10,0,-1):
    #print(i)

#suda_cisla = []
#licha_cisla = []

#for i in range(0,21):
 #   if i % 2 == 0:
  #      suda_cisla.append(i)
   # else:
   #     licha_cisla.append(i)
#task 1
#print(suda_cisla)
#print(licha_cisla)

#number_1 = int(input("Enter number one: "))
#number_2 = int(input("Enter number two: "))

#if number_1 < number_2:
    #for i in range(number_1,number_2 + 1):
        #print(i)#
#elif number_1 > number_2:
    #for i in range(number_2,number_1 + 1):
        #print(i)
#else:
    #print("Entered numbers are equal each other!!!")

#task 2 and 3 

#number_1 = int(input("Enter number one: "))
#number_2 = int(input("Enter number two: "))

#even_numbers = []
#o#dd_numbers = []

#for number in range(number_1, number_2 + 1):
    #if number % 2 == 0:
        #even_numbers.append(number)
    #else:
        #odd_numbers.append(number)

#print("Even numbers are:", even_numbers)
#print("Odd numbers are:", odd_numbers)


#task 4
#number_1 = int(input("Enter number one: "))
#number_2 = int(input("Enter number two: "))

#for number in range(number_1,number_2 -1,-1):
    #print(number)

#task 5
#number_1 = int(input("Enter number one: "))
#number_2 = int(input("Enter number two: "))
#odd_numbers = []


#if number_1 < number_2:
    #for number in range(number_1, number_2 + 1):
        #if number % 2 == 1:
            #odd_numbers.append(number)
            #print(number)
#if number_1 > number_2:
    #for number in range(number_2, number_1 + 1):
        #if number % 2 == 1:
           # odd_numbers.append(number)
            #print(number)

#print("Odd numbers are:", odd_numbers)

import random
number = range(1,501)
tries = 0
program_number = random.choice(number)
print("You should not see this but program number is:", program_number,":-)")
user_guess_number = int(input("Enter number from 1 to 500. For end press zero = 0: "))


if user_guess_number == program_number:
  print(f"Your number: {user_guess_number} is the same with program number. Congratulations.You needed only {tries + 1} try.")
elif user_guess_number == 0:
  print(f"You did not guess program number. You had {tries} try.")
  pass
else:
  while user_guess_number != program_number:
    if user_guess_number == 0:
      print(f"You did not guess program number. You had {tries} tries.")
      break
    elif user_guess_number < program_number:
      tries += 1
      print(f"Your guess number: {user_guess_number} is less than program number. Try it again! You already have {tries} try/tries.")
      user_guess_number = int(input("Enter number from 1 to 500: "))
    elif user_guess_number > program_number:
      tries += 1
      print(f"Your guess number: {user_guess_number} is bigger than program number. Try it again! You already have {tries} try/tries.")
      user_guess_number = int(input("Enter number from 1 to 500: "))
  if user_guess_number == program_number:
    tries += 1
    print(f"You have just guessed right number!! You needed {tries} tries.")



print("Gameover")














