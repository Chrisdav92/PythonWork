if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

student = student_marks.pop(query_name)
selected_scores = 0.00

for x in student:
    selected_scores+=x

selected_scores = selected_scores/float(len(scores))

print("{:.2f}".format(selected_scores))