number_of_snowballs = int(input())
max_snowball_value = 0
max_weight_of_snowball = 0
max_time_to_target = 0
max_quality_of_snowball = 0
for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_to_target = int(input())
    quality_of_snowball = int(input())
    snowball_value = int((weight_of_snowball / time_to_target) ** quality_of_snowball)
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_weight_of_snowball = weight_of_snowball
        max_time_to_target = time_to_target
        max_quality_of_snowball = quality_of_snowball
print(f"{max_weight_of_snowball} : {max_time_to_target} = {max_snowball_value} ({max_quality_of_snowball})")

