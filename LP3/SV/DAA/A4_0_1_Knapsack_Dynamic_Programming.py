def knapsack(weights, values, capacity):
    n = len(weights)
    table = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for current_capacity in range(capacity + 1):
            table[i][current_capacity] = table[i - 1][current_capacity]

            if weights[i - 1] <= current_capacity:
                include_value = values[i - 1] + table[i - 1][current_capacity - weights[i - 1]]
                table[i][current_capacity] = max(table[i][current_capacity], include_value)

    selected_items = []
    current_capacity = capacity

    for i in range(n, 0, -1):
        if table[i][current_capacity] != table[i - 1][current_capacity]:
            selected_items.append(i)
            current_capacity -= weights[i - 1]

    selected_items.reverse()
    return table[n][capacity], selected_items


def main():
    n = int(input("Enter number of items: "))
    capacity = int(input("Enter knapsack capacity: "))

    if n <= 0 or capacity < 0:
        print("Enter a positive number of items and a non-negative capacity.")
        return

    weights = []
    values = []

    for i in range(n):
        weight = int(input("Enter weight of item " + str(i + 1) + ": "))
        value = int(input("Enter value of item " + str(i + 1) + ": "))

        if weight <= 0 or value < 0:
            print("Weight must be positive and value cannot be negative.")
            return

        weights.append(weight)
        values.append(value)

    maximum_value, selected_items = knapsack(weights, values, capacity)
    total_weight = sum(weights[i - 1] for i in selected_items)

    print("\nMaximum value:", maximum_value)
    print("Selected items:", selected_items)
    print("Total weight:", total_weight)
    print("Time Complexity: O(n x W)")
    print("Space Complexity: O(n x W)")


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
# Maximum value: 220
# Selected items: [2, 3]
# Total weight: 50
# Time Complexity: O(n x W)
# Space Complexity: O(n x W)
