def count_food(days):
    result = 0
    for day in days:
        result += daily_food[day - 1]
    return result