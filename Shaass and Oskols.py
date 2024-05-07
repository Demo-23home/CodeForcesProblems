n_wires = int(input())
wire_vals = list(map(int, input().split()))
n_shots = int(input())

for i in range(n_shots):
    wire, bird = map(int, input().split())
    bird -= 1
    left_birds = bird
    right_birds = wire_vals[wire - 1] - bird - 1

    if wire > 1:
        wire_vals[wire - 2] += left_birds
    if wire < n_wires:
        wire_vals[wire] += right_birds

    wire_vals[wire - 1] = 0

print(*wire_vals)
