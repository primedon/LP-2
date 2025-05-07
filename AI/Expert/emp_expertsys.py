def evaluate_performance(punctuality, task_completion, teamwork, communication):
    score = 0

    if punctuality >= 8:
        score += 1
    if task_completion >= 8:
        score += 1
    if teamwork >= 8:
        score += 1
    if communication >= 8:
        score += 1

    if score == 4:
        return "Excellent"
    elif score == 3:
        return "Good"
    elif score == 2:
        return "Average"
    else:
        return "Poor"

print("Rate the employee from 1 to 10 on the following:")

punctuality = int(input("Punctuality: "))
task_completion = int(input("Task Completion: "))
teamwork = int(input("Teamwork: "))
communication = int(input("Communication: "))

result = evaluate_performance(punctuality, task_completion, teamwork, communication)
print("\nPerformance Evaluation: ", result)
