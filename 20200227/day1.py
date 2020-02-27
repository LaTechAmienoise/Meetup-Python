def required_fuel(mass):
	return mass // 3 - 2

import pytest

@pytest.mark.parametrize("mass, fuel", [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
])
def test_required_fuel(mass, fuel):
    assert required_fuel(mass) == fuel


filename = "input.txt"

with open(filename) as f:
	lines = f.read().splitlines()

# Version "boucle for"
total = 0
for line in lines:
	total += required_fuel(int(line))
assert total == 3456641

# Version map/reduce
from functools import reduce
from operator import add

masses = list(map(int, lines))
fuels = list(map(required_fuel, masses))
total = reduce(add, fuels)
assert total == 3456641


# Version sum
masses = list(map(int, lines))
fuels = list(map(required_fuel, masses))
total = sum(fuels)
assert total == 3456641


# Version sum "lazy"
masses = map(int, lines)
fuels = map(required_fuel, masses)
total = sum(fuels)
assert total == 3456641


# Version sum+map one liner
total = sum(map(required_fuel, map(int, lines)))
assert total == 3456641


# Version list comprehensions
masses = [int(line) for line in lines]
fuels = [required_fuel(mass) for mass in masses]
total = sum(fuels)
assert total == 3456641


# Version generator expression 2-lines
masses = (int(line) for line in lines)
from itertools import tee
masses, copie = tee(masses)
print(list(copie))
total = sum(required_fuel(mass) for mass in masses)
assert total == 3456641


# Version generator expression 1-line
total = sum(
	required_fuel(int(line)) for line in lines
)
assert total == 3456641

# TODO: pandas

print("All tests passed")