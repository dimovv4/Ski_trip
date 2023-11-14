days = int(input())
type_of_room = input()
        price_per_night *= 0.65
    elif nights > 15:  #else
        price_per_night *= 0.5
elif type_of_room == "president apartment":
    price_per_night = 35
    if nights < 10:
        price_per_night *= 0.9
    elif nights <= 15:
        price_per_night *= 0.85
    elif nights > 15:  #else
        price_per_night *= 0.8
total_sum = price_per_night * nights
if value == "positive":
    total_sum *= 1.25
elif value == "negative":
    total_sum *= 0.9
print(f"{total_sum:.2f}")
