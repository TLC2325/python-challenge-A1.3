# In this task, you'll be required to to use Python to calculate information from data. It consists of a number of requirements, some easy and some a little more complex.

# A code snippet is provided below which assembles students’ marks from an exam. This code may be pasted directly into a Python code page and will create a list of marks called 'data’.

data = [
    90, 30, 13, 67, 85, 87, 50, 45, 51, 72, 64, 69, 59, 17, 22, 23, 44, 25, 16,
    67, 85, 87, 50, 45, 51, 72, 59, 14, 50, 55, 32, 23, 24, 25, 37, 28, 39, 30,
    33, 35, 40, 34, 41, 43, 94, 95, 98, 99, 44, 45, 47, 48, 49, 53, 61, 63, 69,
    75, 77, 60, 83
]

# Part 1 - Using a list, you will be required to calculate and print to the console the following information:
# The number of students' marks in the data sample.
# The lowest and highest marks.
# The average mark, formatted to two decimal places.

total_num_students = len(data)
maximum_mark = max(data)
minimum_mark = min(data)
total_marks = sum(data)
average_mark = round(total_marks / total_num_students, 2)
result = [total_num_students, minimum_mark, maximum_mark, average_mark]

# print(total_num_students)
# print(maximum_mark)
# print(minimum_mark)
# print(total_marks)
# print(average_mark)
print("A List containing number of students, lowest and highest marks, and average formatted to 2 decimal places:",result)

# Part 2 - you will be required to write code to process the data and calculate how many instances of marks in the categories shown below. Alongside each category you should print out one asterisk for each occurrence. As an example, the category 10-20 has four occurrences (13, 17, 16, & 14) and therefore has four asterisks, e.g.:
# Mark Count   0 - 10 0   10 - 20 4 **** 20 - 30 7 ******* 30 - 40 8 ******** 40-50 11 *********** 50 - 60 9 ********* 60 -70 8 ********

zeroToTen = 0
tenToTwenty = 0
twentyToThirty = 0
thirtyToFort = 0
fortyToFifty = 0
fiftyToSixty = 0
sixtyToSeventy = 0

for i in data:
  if (i <= 10):
    zeroToTen += 1
  elif (i >= 10 and i < 20):
    tenToTwenty += 1
  elif (i >= 20 and i < 30):
    twentyToThirty += 1
  elif (i >= 30 and i < 40):
    thirtyToFort += 1
  elif (i >= 40 and i < 50):
    fortyToFifty += 1
  elif (i >= 50 and i < 60):
    fiftyToSixty += 1
  elif (i >= 60 and i < 70):
    sixtyToSeventy += 1
  else:
    "Error try again"

# print(zeroToTen)
# print(tenToTwenty)
# print(twentyToThirty)
# print(thirtyToFort)
# print(fortyToFifty)
# print(fiftyToSixty)
# print(sixtyToSeventy)
print("\n")
print(
  f'Mark Count\n0 - 10 {zeroToTen} {zeroToTen * "*"}\n10 - 20 {tenToTwenty} {tenToTwenty * "*"}\n20 - 30 {twentyToThirty} {twentyToThirty * "*"}\n30 - 40 {thirtyToFort} {thirtyToFort * "*"}\n40 - 50 {fortyToFifty} {fortyToFifty * "*"}\n50 - 60 {fiftyToSixty} {fiftyToSixty * "*"}\n60 - 70 {sixtyToSeventy} {sixtyToSeventy * "*"}'
)
print("\n")

# Part 3 - Finally, you will be requested to calculate and print out what the pass mark should be to ensure that at least 60% of students will pass the exam. This should be to the nearest ten.

sixty_percentage_of_students = total_num_students * 0.6
print("Calculate 60% of students:",sixty_percentage_of_students)
round_num_nearest_ten = round(sixty_percentage_of_students / 10) * 10
print("Number of students who should pass rounded to nearest ten:",round_num_nearest_ten)


sorted_list_az = sorted(data)
print("\nGrades from lowest to highest:",sorted_list_az,"\n")

print("Number of students who should fail is:", total_num_students-round_num_nearest_ten)

print("\nThe grades of 40% of students who didn't passed:",sorted_list_az[:21])
print("\nThe grades of 60% of students passed:",sorted_list_az[22:])

pass_mark = sorted_list_az[22]
print("\nPass mark is:",pass_mark)