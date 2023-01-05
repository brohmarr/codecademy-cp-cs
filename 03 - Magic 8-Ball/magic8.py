# Project: Magic 8-Ball
# by: @Brohmarr

# The "Magic 8-Ball" is a popular toy developed in the 1950s for fortune-telling or advice seeking.
# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

import random


# Name of the person asking the question.
name = "Thiago"

# Asker's question.
question = "Is this the real life?"

# Magic 8-Ball's answer.
answer = ""

# Generating a random fortune.
random_number = random.randint(1, 12)

# Saving the generated fortune to its variable.
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."

# Adding a few more possible fortunes.
elif random_number == 10:
  answer = "Hm... Maybe..."
elif random_number == 11:
  answer = "Well yes, but actually no."
elif random_number == 12:
  answer = "Who knows?"

# Making sure the program always outputs something.
else:
  answer = "Error"

# Printing the question.
if question == "":
  print("What would you like to ask me?")
else:
  if name != "":
    print(name, "asks:", question)
  else:
    print("Question:", question)

  # Printing the answer.
  print("Magic 8-Ball's answer:", answer)
