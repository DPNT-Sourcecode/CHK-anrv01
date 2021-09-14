

# noinspection PyUnusedLocal
# skus = unicode string
from math import floor


def apply_discount(sku, occurrence_data, number_required, discount_applied_per_offer, total_cost):
    if occurrence_data[sku] / number_required >= 1:
        total_discount = discount_applied_per_offer * floor(occurrence_data[sku] / number_required)
        occurrence_data[sku] = occurrence_data[sku] - number_required * floor(occurrence_data[sku] % number_required)
        return total_cost - total_discount, occurrence_data
    else:
        return total_cost, occurrence_data


def checkout(skus):
    if not isinstance(skus, str):
        return -1
    sku_values = {"A": 50,
                  "B": 30,
                  "C": 20,
                  "D": 15,
                  "E": 40}
    occurrences = {"A": 0,
                   "B": 0,
                   "C": 0,
                   "D": 0,
                   "E": 0}
    total_cost = 0
    for char in skus:
        if char not in sku_values.keys():
            return -1
        if sku_values.get(char):
            occurrences[char] = occurrences[char] + 1
            total_cost += sku_values.get(char)

    total_cost, occurrences = apply_discount("A", occurrences, 5, 50, total_cost)
    total_cost, occurrences = apply_discount("A", occurrences, 3, 20, total_cost)
    total_cost, occurrences = apply_discount("B", occurrences, 2, 15, total_cost)
    print(total_cost)
    if occurrences["E"] >= 2 and occurrences["B"] >= 1:
        for item in range(occurrences["B"]):
            total_cost, occurrences = apply_discount("E", occurrences, 2, 30, total_cost)

    return total_cost



