

# noinspection PyUnusedLocal
# skus = unicode string
import importlib.resources
import json
from math import floor


def buy_any_of_group_discount(occurrence_data, sku_values, number_required, total_cost):
    """Applies 'buy any of the following SKUs' group offer"""
    # ordered highest cost first
    group_discount_skus = ["Z", "T", "S", "Y", "X"]
    current_count = 0
    current_discount = 0
    total_discount = 0
    difference = 0
    number_of_discounts_applied = 0
    for index, sku in enumerate(group_discount_skus):
        current_count += occurrence_data.get(sku)
        if difference != 0:
            print(group_discount_skus[index-1])
            current_discount += sku_values.get(group_discount_skus[index-1]) * difference
            difference = 0
        current_discount += sku_values.get(sku) * occurrence_data.get(sku)
        if current_count >= number_required:
            difference = current_count - number_required
            current_discount -= sku_values.get(sku) * difference
            occurrence_data[sku] = occurrence_data[sku] - difference
            for previous_sku in group_discount_skus[:index]:
                occurrence_data[previous_sku] = 0
            current_count = 0
            total_discount += current_discount
            current_discount = 0
            number_of_discounts_applied += 1

    total_discount_for_group_offer_price = total_discount - (45 * number_of_discounts_applied)

    return total_cost - total_discount_for_group_offer_price, occurrence_data


def buy_some_get_one_free(sku_of_free_item, sku_of_dependent_item, occurrence_data, number_required, discount,
                          total_cost):
    """Applies buy a number of a given SKU and get one free offer"""
    for item in range(occurrence_data[sku_of_free_item]):
        if occurrence_data[sku_of_dependent_item] >= number_required:
            occurrence_data[sku_of_dependent_item] -= number_required
            occurrence_data[sku_of_free_item] -= 1
            total_cost -= discount
    return total_cost, occurrence_data


def apply_discount(sku, occurrence_data, number_required, discount_applied_per_offer, total_cost):
    """Applies generic discount offer"""
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
    total_cost, occurrences = buy_any_of_group_discount(occurrences, sku_values, 3, total_cost)
    total_cost, occurrences = apply_discount("A", occurrences, 5, 50, total_cost)
    total_cost, occurrences = apply_discount("A", occurrences, 3, 20, total_cost)
    total_cost, occurrences = buy_some_get_one_free("B", "E", occurrences, 2, 30, total_cost)
    total_cost, occurrences = apply_discount("B", occurrences, 2, 15, total_cost)
    total_cost, occurrences = apply_discount("F", occurrences, 3, 10, total_cost)
    total_cost, occurrences = apply_discount("H", occurrences, 10, 20, total_cost)
    total_cost, occurrences = apply_discount("H", occurrences, 5, 5, total_cost)
    total_cost, occurrences = apply_discount("K", occurrences, 2, 20, total_cost)
    total_cost, occurrences = buy_some_get_one_free("M", "N", occurrences, 3, 15, total_cost)
    total_cost, occurrences = apply_discount("P", occurrences, 5, 50, total_cost)
    total_cost, occurrences = buy_some_get_one_free("Q", "R", occurrences, 3, 30, total_cost)
    total_cost, occurrences = apply_discount("Q", occurrences, 3, 10, total_cost)
    total_cost, occurrences = apply_discount("U", occurrences, 4, 40, total_cost)
    total_cost, occurrences = apply_discount("V", occurrences, 3, 20, total_cost)
    total_cost, occurrences = apply_discount("V", occurrences, 2, 10, total_cost)

    return total_cost
