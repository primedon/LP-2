def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)
    max_deadline = max(job[2] for job in jobs)
    slots = [None] * max_deadline

    for job in jobs:
        for i in range(min(max_deadline, job[2]) - 1, -1, -1):
            if slots[i] is None:
                slots[i] = job[0]
                break

    return [job for job in slots if job is not None]

jobs = [('J1', 100, 2), ('J2', 19, 1), ('J3', 27, 2), ('J4', 25, 1), ('J5', 15, 3)]
print("Jobs scheduled:", job_scheduling(jobs))