import matplotlib.pyplot as plt

'''

This module creates photo and returns name 
'''

name = 'graphic.png'

def get_plot(days, values):
        x = range(len(values))
        labels = days
        fig = plt.plot(x, values)
        plt.xticks(x, labels, rotation='vertical')
        plt.margins(0.2)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(name)
        return name


