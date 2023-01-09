# Project: Gradebook
# by: @Brohmarr

# You are a student and you are trying to organize your subjects and
#     grades using Python.


# Initial Data
last_semester_gradebook = [["Politics", 80], ["Latin", 96], ["Dance", 97],
                           ["Architecture", 65]]

# Initializing Lists
subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85],
             ["History", 88]]

# My grade for the Computer Science class just came in! Perfect score!
gradebook.append(["Computer Science", 100])

# Another grade came in: Visual Arts! Got a score of 93!
gradebook.append(["Visual Arts", 93])

# My instructor made a mistake grading the Visual Arts class. Got 5
#     extra points!
gradebook[-1][-1] += 5

# Er, I don't care that much about Poetry, just need to know if I
#     passed...
gradebook[2].remove(gradebook[2][-1])
gradebook[2].append("Pass")

# Let's combine the grades from both semesters to wrap this up!
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
