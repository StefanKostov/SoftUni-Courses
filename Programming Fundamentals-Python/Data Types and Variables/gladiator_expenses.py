
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
spend_counter = 0
shield_counter = 0
for game in range(1, lost_fights_count + 1):
    if game % 2 == 0:
        spend_counter += helmet_price
    if game % 3 == 0:
        spend_counter += sword_price
    if (game % 2 == 0) and (game % 3 == 0):
        spend_counter += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            spend_counter += armor_price
print(f"Gladiator expenses: {spend_counter:.2f} aureus")
