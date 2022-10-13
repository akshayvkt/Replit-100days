# print("2 plus 2 is 4 minus that's three quick mafs, everyday man's on the block. Now it's time to test your math skills \n")

# x = int(input("Which number's multiples do you want to guess?: "))
# counter = 0

# for i in range(1,11):
#   guess = int(input(f'What do you think {x} multiplied by {i} is?: '))
#   if guess == x*i:
#     print(f'Awesome, you guessed it right. The answer indeed is {x*i} \n')
#     counter += 1
#   else:
#     print(f"You guessed it wrong, the answer actually is {x*i}, but you thought it was {guess}. Guess being quick at maths isn't the same as being right at math afterall, lol \n\n")

# if counter == 10:
#   print(f"Amazing, your final score is {counter} out of {i} attempts.")
# else:
#   print(f"Your final score is {counter} out of {i} attempts. Can do better")

print("Welcome to Math Facts Game")
print()
print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
print()

fact_family = int(input("Name your multiples: "))
print()

counter = 0
for i in range(1, 11):
  correct_answer = i*fact_family
  print(i, "x", fact_family)
  answer = int(input("> "))
  if answer == correct_answer:
    print("You got it right!")
    counter += 1
  else:
    print("That's not correct. It should have been", correct_answer)

if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "out of 10 correct.")