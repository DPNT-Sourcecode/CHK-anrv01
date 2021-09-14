

# noinspection PyUnusedLocal
# skus = unicode string
import importlib.resources
import json
from math import floor


def buy_some_get_one_free(sku_of_free_item, sku_of_dependent_item, occurrence_data, number_required, discount,
                          total_cost):

    for item in range(occurrence_data[sku_of_free_item]):
        if occurrence_data[sku_of_dependent_item] >= number_required:
            occurrence_data[sku_of_dependent_item] -= number_required
            occurrence_data[sku_of_free_item] -= 1
            total_cost -= discount
    return total_cost, occurrence_data


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
    total_cost, occurrences = buy_some_get_one_free("B", "E", occurrences, 2, 30, total_cost)
    #for item in range(occurrences["B"]):
    #    if occurrences["E"] >= 2:
    #        occurrences["E"] -= 2
    #        occurrences["B"] -= 1
    #        total_cost -= 30
    total_cost, occurrences = apply_discount("B", occurrences, 2, 15, total_cost)
    total_cost, occurrences = apply_discount("F", occurrences, 3, 10, total_cost)
    total_cost, occurrences = apply_discount("H", occurrences, 10, 20, total_cost)
    total_cost, occurrences = apply_discount("H", occurrences, 5, 5, total_cost)
    total_cost, occurrences = apply_discount("K", occurrences, 2, 10, total_cost)
    total_cost, occurrences = buy_some_get_one_free("M", "N", occurrences, 3, 15, total_cost)
    #for item in range(occurrences["M"]):
    #    if occurrences["N"] >= 3:
    #        occurrences["N"] -= 3
    #        occurrences["M"] -= 1
    #        total_cost -= 15
    total_cost, occurrences = apply_discount("P", occurrences, 5, 50, total_cost)
    total_cost, occurrences = buy_some_get_one_free("Q", "R", occurrences, 3, 30, total_cost)
    total_cost, occurrences = apply_discount("Q", occurrences, 3, 10, total_cost)
    total_cost, occurrences = apply_discount("U", occurrences, 4, 40, total_cost)
    total_cost, occurrences = apply_discount("V", occurrences, 3, 20, total_cost)
    total_cost, occurrences = apply_discount("V", occurrences, 2, 10, total_cost)

    return total_cost

