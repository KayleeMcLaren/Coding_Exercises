student_scores = {
  "Harry": 78,
  "Ron": 81,
  "Hermione": 99,
  "Draco": 62,
  "Neville": 74,
}

student_grades = {}

student_grades = {}
for name in student_scores:
    score = student_scores[name]
    if score> 90:
        student_grades[name] = "Outstanding"
    elif score> 80:
        student_grades[name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[name] = "Acceptable"
    else:
         student_grades[name] = "Fail"

print(student_grades)
