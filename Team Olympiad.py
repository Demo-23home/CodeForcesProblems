n = int(input())
students = input().split(" ")

students = list(map(int, students))
teams = []
programming = []
math = []
PE = []

for index, student in enumerate(students):
    if student == 1:
        programming.append(index+1)
    elif student == 2:
        math.append(index+1)
    elif student == 3:
        PE.append(index+1)

n_teams = min(len(programming), len(math), len(PE))
for i in range(n_teams):
    team_i = [programming[i], math[i], PE[i]]
    if len(team_i) == 3:
        teams.append(team_i)
print(n_teams)
for team in teams:
    print(*team)