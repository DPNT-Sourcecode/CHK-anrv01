

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    sku_values = {"A": 50,
                  "B": 30,
                  "C": 20,
                  "D": 15}
    occurrences = {"A": 0,
                   "B": 0,
                   "C": 0,
                   "D": 0}
    total_cost = 0
    for char in skus:
        if sku_values.get(char):
            occurrences[char] = occurrences[char] + 1
            total_cost += sku_values.get(char)
    if occurrences["A"] % 3:
        total_cost -= 20 * occurrences["A"] % 3
    if occurrences["B"] % 2:
        total_cost -= 15 * occurrences["B"] % 2

    return total_cost


