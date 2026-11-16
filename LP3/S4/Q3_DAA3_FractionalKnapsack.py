# ============================================================
# A(3) Write a program to solve the Fractional Knapsack
# problem using a Greedy Method.
# ============================================================

def fractional_knapsack(capacity, items):

    # Sort by value/weight ratio (highest first)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total = 0

    for value, weight in items:

        if weight <= capacity:
            total += value
            capacity -= weight

        else:
            total += value * capacity / weight
            break

    return total


# Main Program
n = int(input("Enter number of items: "))

values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))

capacity = int(input("Enter capacity: "))

if (n <= 0 or len(values) != n or len(weights) != n
        or any(w <= 0 for w in weights) or capacity < 0):
    print("Invalid input!")
else:
    items = list(zip(values, weights))
    result = fractional_knapsack(capacity, items)
    print("Maximum value:", result)


# ============================================================
# SAMPLE OUTPUT
# ============================================================
#
# Enter number of items: 3
# Enter values: 60 100 120
# Enter weights: 10 20 30
# Enter capacity: 50
# Maximum value: 240.0


# ============================================================
# ------------------------------------------------------------
# THEORY AND VIVA QUESTIONS & ANSWERS
# ------------------------------------------------------------
# ============================================================

# THEORY:
#
# Fractional Knapsack is an optimization problem solved
# using the Greedy Method.
#
# The goal is to maximize profit without exceeding
# the given knapsack capacity.
#
# Items can be divided into fractions.
#
# FORMULA:
# Ratio = Value / Weight
# Fractional Value = Value * Remaining Capacity / Weight
#
# ALGORITHM:
# 1. Accept values, weights and capacity.
# 2. Sort items by value/weight ratio (descending).
# 3. Select the item with the highest ratio.
# 4. If it fits, take the complete item.
# 5. Otherwise, take the fraction that fits.
# 6. Continue until the capacity is filled.
#
# COMPLEXITY:
# Time Complexity  : O(n log n)
# Space Complexity : O(n) for storing input items
#
# Sorting takes O(n log n) time.
# Traversing items takes O(n) time.


# Q1. What is Fractional Knapsack?
# Ans: An optimization problem where whole or fractional
# items are selected to maximize profit within capacity.


# Q2. What is a Greedy Algorithm?
# Ans: An algorithm that selects the locally best
# choice at each step to reach an optimal solution.


# Q3. Why is Fractional Knapsack greedy?
# Ans: It always selects the item having the highest
# value/weight ratio first.


# Q4. Why do we calculate value/weight ratio?
# Ans: It represents profit per unit of weight.
# Higher ratio means better profit for the same weight.


# Q5. What is the time complexity?
# Ans: O(n log n), because sorting n items
# takes O(n log n) time.


# Q6. What is the space complexity?
# Ans: O(n) for storing n items.
# Python sorting may also use O(n) temporary memory.


# Q7. Why do we sort items in descending order?
# Ans: To select items with the highest profit
# per unit weight first.


# Q8. Difference between 0/1 and Fractional Knapsack?
# Ans: 0/1 Knapsack allows only complete items.
# Fractional Knapsack allows dividing items.


# Q9. Does greedy work for 0/1 Knapsack?
# Ans: Not always, because items cannot be divided.
# Dynamic Programming can find the optimal solution.


# Q10. Why does greedy give an optimal solution here?
# Ans: Because items are divisible, selecting maximum
# profit per unit weight is always optimal.


# Q11. What is lambda used for?
# Ans: It creates a small anonymous function.
# Here, it calculates value/weight for sorting.


# Q12. What is the purpose of zip()?
# Ans: It combines corresponding values and weights
# into pairs like (60, 10), (100, 20).


# Q13. What happens when an item exceeds capacity?
# Ans: Only the fraction that fits is selected,
# and the algorithm stops.


# Q14. Why is break used?
# Ans: After selecting a fraction, the remaining
# capacity is filled, so no more items are needed.


# Q15. What is the maximum profit in our example?
# Ans: 240.
# Item 1: 60  (10 kg)
# Item 2: 100 (20 kg)
# Item 3: 80  (20 kg out of 30 kg)
# Total : 240 (50 kg)


# Q16. Where is Fractional Knapsack used?
# Ans: Resource allocation, cargo loading and
# budget optimization when items are divisible.


# ============================================================
# CONCLUSION
# ============================================================
#
# Fractional Knapsack uses the Greedy Method to maximize
# profit by selecting items with the highest value/weight
# ratio first.
#
# Time Complexity: O(n log n).
# ============================================================
