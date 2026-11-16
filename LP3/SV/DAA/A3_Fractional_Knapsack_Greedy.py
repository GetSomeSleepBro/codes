def fractional_knapsack(weights, values, capacity):
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i], i + 1))

    items.sort(key=lambda item: item[0], reverse=True)
    total_value = 0
    remaining_capacity = capacity
    fractions_taken = [0.0] * len(weights)

    for ratio, weight, value, item_number in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            selected_weight = weight
            selected_value = value
        else:
            selected_weight = remaining_capacity
            selected_value = ratio * selected_weight

        fraction_taken = selected_weight / weight
        total_value += selected_value
        remaining_capacity -= selected_weight
        fractions_taken[item_number - 1] = fraction_taken

    return total_value, fractions_taken


def main():
    n = int(input("Enter number of items: "))
    capacity = float(input("Enter knapsack capacity: "))

    if n <= 0 or capacity < 0:
        print("Enter a positive number of items and a non-negative capacity.")
        return

    weights = []
    values = []

    for i in range(n):
        weight = float(input("Enter weight of item " + str(i + 1) + ": "))
        value = float(input("Enter value of item " + str(i + 1) + ": "))

        if weight <= 0 or value < 0:
            print("Weight must be positive and value cannot be negative.")
            return

        weights.append(weight)
        values.append(value)

    maximum_value, fractions_taken = fractional_knapsack(weights, values, capacity)

    print("\nItems Taken:")
    for i in range(n):
        fraction = fractions_taken[i]
        weight_taken = weights[i] * fraction
        value_taken = values[i] * fraction
        print("Item", i + 1, "- Weight Taken:", round(weight_taken, 2),
              "Value:", round(value_taken, 2), "Fraction Taken:", round(fraction, 2))

    print("\nMaximum value:", round(maximum_value, 2))


if __name__ == "__main__":
    main()


# SAMPLE OUTPUT:
# Enter number of items: 3
# Enter knapsack capacity: 50
# Enter weight of item 1: 10
# Enter value of item 1: 60
# Enter weight of item 2: 20
# Enter value of item 2: 100
# Enter weight of item 3: 30
# Enter value of item 3: 120
#
# Items Taken:
# Item 1 - Weight Taken: 10.0 Value: 60.0 Fraction Taken: 1.0
# Item 2 - Weight Taken: 20.0 Value: 100.0 Fraction Taken: 1.0
# Item 3 - Weight Taken: 20.0 Value: 80.0 Fraction Taken: 0.67
#
# Maximum value: 240.0
