import matplotlib.pyplot as plt
from utils import roundup
import random
import math
from config import RR_PROCESS_RANGE, RR_ARRIVAL_RANGE, RR_DURATION_RANGE, \
    RR_QUANTUM


def rr_plot(list_of_processes, timestamp):
    width_xaxis = []
    for process in list_of_processes:
        width_xaxis.append(process.termination_time)
    width_value = max(width_xaxis)
    height_value = RR_PROCESS_RANGE * 5 + 5

    WIDTH = math.ceil((width_value + 150) / 50)
    HEIGHT = math.ceil((height_value + 100) / 50)
    BAR_HEIGHT = 2

    fig, gnt = plt.subplots(figsize=(WIDTH, HEIGHT))

    plt.title(f'GANNT PLOT FOR {RR_PROCESS_RANGE} PROCESSES, RR, '
              f'QUANTUM {RR_QUANTUM} [MS]')

    gnt.set_ylim(0, height_value)
    gnt.set_xlim(0, roundup(width_value + 15))

    gnt.set_xlabel('Time[ms]')
    gnt.set_ylabel('Process')

    gnt.set_yticks([i for i in range(5, RR_PROCESS_RANGE * 5 + 5, 5)])
    gnt.invert_yaxis()

    gnt.grid(True)
    gnt.set_axisbelow(True)

    names = []
    # mark times
    for index, process in enumerate(list_of_processes):
        names.append("P" + str(process.name))
        for interval in process.waiting_list:
            gnt.broken_barh([(interval[0], interval[1] - interval[0])],
                            ((index * 5 + 5) - BAR_HEIGHT / 2,
                             BAR_HEIGHT),
                            facecolors='#8e8888', label='waiting time')
        for interval in process.working_list:
            gnt.broken_barh([(interval[0], interval[1] - interval[0])],
                            ((index * 5 + 5) - BAR_HEIGHT / 2,
                             BAR_HEIGHT),
                            facecolors='#00ff00', label='burst time')
        gnt.annotate(f'{process.termination_time}',
                     xy=(
                         process.termination_time,
                         index * 5 + 5 + BAR_HEIGHT / 2),
                     xytext=(BAR_HEIGHT * 10, 5),
                     xycoords='data',
                     textcoords='offset pixels', ha='center', va='center')

    gnt.set_yticklabels(names)

    # fix legend
    hand, labl = gnt.get_legend_handles_labels()
    handout = []
    lablout = []
    for h, l in zip(hand, labl):
        if l not in lablout:
            lablout.append(l)
            handout.append(h)
    gnt.legend(handout, lablout, prop={'size': 6})

    title = "CHART_RR_" + timestamp + ".png"
    sub = timestamp + "/"
    plt.savefig(sub + title)
