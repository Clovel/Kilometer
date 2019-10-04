import matplotlib.pyplot as plt


def plot_odometry(p_entries):
    # Set the x axis
    x = [p_entries[i].date for i in range(len(p_entries))]

    # Set the y axis : Odometry
    y_odometry = [p_entries[i].odometry for i in range(len(p_entries))]

    # Set the y axis : mean odometry
    y_mean_odometry1 = []
    sum = 0
    for i in range(len(p_entries)):
        delta_odometry = p_entries[i].odometry - p_entries[0].odometry
        delta_date = p_entries[i].date - p_entries[0].date

        if delta_date:
            y_mean_odometry1.append(delta_odometry/delta_date.days*365)
        else:
            y_mean_odometry1.append(None)

    # Set the y axis : Cost
    cost_sum = 0
    y_cost = [p_entries[i].cost for i in range(len(p_entries))]
    y_cost_sum = []
    for element in y_cost:
        if not element:
            element = None
            y_cost_sum.append(cost_sum)
        else:
            cost_sum += element
            y_cost_sum.append(cost_sum)

    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Date")

    ax1.plot(x, y_odometry, "b-o")
    ax1.set_ylabel("Odometry", color='b')
    ax1.tick_params('y', colors='b')
    ax1.set_ylim(bottom=110000.0)

    ax2 = ax1.twinx()
    ax2.plot(x, y_mean_odometry1, "r-o")
    ax2.set_ylabel("Mean odometry", color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()

    plt.gcf().autofmt_xdate()


def plot_cost(p_entries):
    # Set the x axis
    x = [p_entries[i].date for i in range(len(p_entries))]

    # Set the y axis : Cost
    cost_sum = 0
    y_cost = [p_entries[i].cost for i in range(len(p_entries))]
    y_cost_sum = []
    for element in y_cost:
        if not element or 0 == element:
            element = None
            y_cost_sum.append(cost_sum)
        else:
            cost_sum += element
            y_cost_sum.append(cost_sum)

    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Date")

    ax1.plot(x, y_cost, "b-o")
    ax1.set_ylabel("Cost", color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(x, y_cost_sum, "r-o")
    ax2.set_ylabel("Total cost", color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()

    plt.gcf().autofmt_xdate()

    fig.show()


def show():
    plt.show(block=True)

