transactions = [1200, 1500, 1300, 1250, 1400, 5000, 1350, 1280, 6000, 1320]
total = 0
for amount in transactions:
    total += amount
average = total / len(transactions)
variance_sum = 0
for amount in transactions:
    variance_sum += (amount - average) ** 2
variance = variance_sum / len(transactions)
std_dev = variance ** 0.5
threshold = average + (2 * std_dev)
print("Average Spending:", average)
print("Standard Deviation:", std_dev)
print("Anomaly Threshold:", threshold)
print("Anomalous Transactions:")
for amount in transactions:
    if amount > threshold:
        print(amount)
