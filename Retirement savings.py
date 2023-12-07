
import matplotlib.pyplot as plt
import numpy as np
    

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mrate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mrate) + monthly] # computing compound interest
    return base, savings


def displayRetire(monthlies, rate, terms):
    plt.figure('Retiremonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.suptitle('Plot of how much savings it would take to retire at different monthly savings ')
        plt.plot(xvals, yvals, label = 'Retire:' + str(monthly))
        plt.legend(loc = 'upper left')
    plt.show()

displayRetire([500, 700, 800,1000, 1200], .05, 40*12)