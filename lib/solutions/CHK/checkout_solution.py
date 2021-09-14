

# noinspection PyUnusedLocal
# skus = unicode string
import importlib.resources
import json
from math import floor


def apply_discount(sku, occurrence_data, number_required, discount_applied_per_offer, total_cost):
    if occurrence_data[sku] / number_required >= 1:
        total_discount = discount_applied_per_offer * floor(occurrence_data[sku] / number_required)
        occurrence_data[sku] = occurrence_data[sku] - number_required * floor(occurrence_data[sku] / number_required)
        return total_cost - total_discount, occurrence_data
    else:
        return total_cost, occurrence_data


def checkout(skus) -> int:
    if not isinstance(skus, str):
        return -1
    with importlib.resources.open_text("lib.solutions.CHK.sku_data", "sku_items_and_prices.json") as sku_data:
        sku_values = json.load(sku_data)
    occurrences = {sku: 0 for sku in sku_values}

    total_cost = 0
    for char in skus:
        if char not in sku_values.keys():
            return -1
        if sku_values.get(char):
            occurrences[char] = occurrences[char] + 1
            total_cost += sku_values.get(char)

    # Discounts applied in priority order (i.e. 'larger' discounts come first)
    total_cost, occurrences = apply_discount("A", occurrences, 5, 50, total_cost)
    total_cost, occurrences = apply_discount("A", occurrences, 3, 20, total_cost)
    for item in range(occurrences["B"]):
        if occurrences["E"] >= 2:
            occurrences["E"] -= 2
            occurrences["B"] -= 1
            total_cost -= 30
    total_cost, occurrences = apply_discount("B", occurrences, 2, 15, total_cost)
    total_cost, occurrences = apply_discount("F", occurrences, 3, 10, total_cost)

    return total_cost


