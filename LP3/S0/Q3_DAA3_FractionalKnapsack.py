n = 3
weight = [10, 20, 30]
profit = [60, 100, 120]
capacity = 50

ratio = []

for i in range(n):
    ratio.append(profit[i] / weight[i])

items = sorted(range(n), key=lambda i: ratio[i], reverse=True)

total_profit = 0

for i in items:
    if capacity >= weight[i]:
        total_profit += profit[i]
        capacity -= weight[i]
    else:
        total_profit += ratio[i] * capacity
        break

print("Maximum Profit:", total_profit)
