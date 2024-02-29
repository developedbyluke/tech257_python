x = 0

while x < 10:
    print(f"x -> {x}")
    # if you don't increment x at the end, the exit condition 'x < 10' will always be true, leading to an infinite loop.
    x += 1

x = 0
print()

while x <= 4:
    print(f"x -> {x}")
    x += 1
