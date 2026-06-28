names = ("Juan", "Maria", "Joseph")
scores = (70, 90, 81)

for name, score in zip(names, scores):
    print(f"{name} scored {score} in the exam.")

highest_scorer = sorted(scores)
print()
print(f"Highest Scorer: {highest_scorer[-1]}")

# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""
