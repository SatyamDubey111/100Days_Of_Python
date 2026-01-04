student_scores = [150, 200, 300, 400, 500, 600, 700]

total_exam_score = sum(student_scores)
# print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

# max
print(max(student_scores))
# using loop
max_score = 0
for maximum in student_scores:
    if maximum > max_score:
        max_score = maximum

print(max_score)
