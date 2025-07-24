"""
Limak = a *3 per year
Bob = b *2 per year

Limak < bob == true at start
"""

def get_inputs() -> list[int]:
    # TODO get inputs from console
    return [4,9]

def compute_years(weight_limak:int, weight_bob:int) -> int:
    if a>b: return -1

    counter = 0
    limak = weight_limak
    bob = weight_bob

    while limak<=bob:
        counter += 1
        limak = limak*3
        bob = bob*2

    return counter

if __name__ == '__main__':
    a,b = get_inputs()
    print(a)
    print(b)
    years = compute_years(a,b)
    print(years)