def indexOf(items, item):
    return items.index(item)

# list of resistance colors
act_clr = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white", "gold", "silver"]
pct = [1, 10, 100, 1000, 1e4, 1e5, 1e6, 1e7, 1e8, 1, 0.1, 0.01]
# list of tolerance colors
tol = ["brown", "red", "green", "blue", "violet", "gray", "gold", "silver", "none"]
tol1 = ["±1%", "±2%", "±0.5%", "±0.25%", "±0.1%", "±0.05%", "±5%", "±10%", "±20%"]

c = input("Enter color code: ").lower().split()

x1 = indexOf(act_clr, c[0])
x2 = indexOf(act_clr, c[1])
x3 = indexOf(act_clr, c[2])
x13 = pct[x3]
x4 = indexOf(tol, c[3])
x41 = tol1[x4]

z1 = str(x1)+str(x2)
z2 = float(z1)*x13

print("\nR =", z2, x41, "Ω")

print("\n============== More Details ==============\n")

if z2 in range(0, 1000):
    print(f"Resistance = {z2} Ω\nTolerance = {x41}")
    print(f"\nR ={z2} {x41} Ω")

elif z2 in range(1000, 999000):
    z = z2*(pow(10, -3))

    print(f"Resistance = {z} KΩ\nTolerance = {x41}")
    print(f"\nR = {z} {x41} KΩ")

elif z2 in range(1000000, 999000000):
    z = z2*(pow(10, -6))

    print(f"Resistance = {z} MΩ\nTolerance = {x41}")
    print(f"\nR = {z} {x41} MΩ")

else:
    z = z2*(pow(10, -9))

    print(f"Resistance = {z} GΩ\nTolerance = {x41}")
    print(f"\nR = {z} {x41} GΩ")


print("\n==========================================")
