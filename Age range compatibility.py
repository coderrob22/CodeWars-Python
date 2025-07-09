import math
def dating_range(age):
    if age <= 14:
        min = math.floor(age - .10 * age)
        max = math.floor(age + .10 * age)
        return f"{min}-{max}"
    else:
        min = age/2 +7
        max = 2 * (age-7)
        return f"{math.floor(min)}-{math.floor(max)}"