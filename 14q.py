import matplotlib.pyplot as plt
def plot_profit():
    months = list(range(1, 13))
    profits = []
    print("enter the profit of the each 12 months :")
    for i in range(1, 13):
        profit = int(input(f"profit for month {i}"))
        profits.append(profit)
    plt.figure(figsize = (10, 5))
    plt.plot(months, profits, marker='o', linestyle='-', color= "blue")
    plt.xlabel("month number")
    plt.ylabel("total profit")
    plt.title("monthly profit of company ABC")
    plt.grid(True)
    plt.xticks(months)
    plt.show()
plot_profit()