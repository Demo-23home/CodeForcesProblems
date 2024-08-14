"""
8 6 4 5

8 6 4 6

10 3 11 4

4 2 1 4
"""

import math


def is_second_oven_reasonable(n, t, k, d):
    # Time required with one oven
    batches_needed = math.ceil(n / k)
    time_one_oven = batches_needed * t

    # Time with two ovens
    time_before_second_oven_ready = (d // t) * k
    remaining_cakes = n - time_before_second_oven_ready

    if remaining_cakes <= 0:
        return "NO"

    remaining_batches_needed = math.ceil(remaining_cakes / (2 * k))
    time_two_ovens = d + (remaining_batches_needed * t)

    return "YES" if time_two_ovens < time_one_oven else "NO"


# Input
n, t, k, d = map(int, input().split())

# Output
print(is_second_oven_reasonable(n, t, k, d))
