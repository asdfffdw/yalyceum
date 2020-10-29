num_bullets = int(input())
full_damage1 = 0
full_damage2 = 1
for i in range(num_bullets):
    one_damage1 = int(input())
    one_damage2 = int(input())
    full_damage1 = (full_damage1 * one_damage2) + (one_damage1 * full_damage2)
    full_damage2 *= one_damage2
    continue
x, y = full_damage1, full_damage2
while y > 0:
    x, y = y, x % y
print(full_damage1 // x, '/', full_damage2 // x, sep='')
