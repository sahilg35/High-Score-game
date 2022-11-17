student_scores = input("Input a list of student scores ").split()
score = 0
highest_score = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  score = student_scores[n]
  if score > highest_score:
      highest_score = score
  else:
      highest_score

print(student_scores)
print(f"The highest score in the class is: {highest_score}")