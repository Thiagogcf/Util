import matplotlib.pyplot as plt

complete = 360
percent = 0.088
def view_pizza_chart(complete, percent):
    # Data to plot
    labels = 'Complete', 'Percent'
    sizes = [complete, percent]
    colors = ['purple', 'gold']
    explode = (0.1, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


def view_how_many_to_100(complete, percent):
    print('You have to complete', 100 - percent, 'to reach 100%')
    print('You have to complete', complete - percent, 'to reach', complete, 'hours')

view_pizza_chart(complete, percent)
view_how_many_to_100(complete, percent)