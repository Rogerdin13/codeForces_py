"""
https://codeforces.com/problemset/problem/791/A

Limak = a *3 per year
Bob = b *2 per year

Limak < bob == true at start
"""
import re


def get_inputs() -> list[int]:
    weights = input()
    pattern = r"\d+"

    return list(map(int, re.findall(pattern, weights)[:2]))

def compute_years(weight_limak:int, weight_bob:int) -> int:
    if weight_limak>weight_bob: return -1

    counter = 0
    limak = weight_limak
    bob = weight_bob

    while limak <= bob:
        counter += 1
        limak = limak*3
        bob = bob*2

    return counter

if __name__ == '__main__':
    a,b = get_inputs()
    years = compute_years(a,b)
    print(years)