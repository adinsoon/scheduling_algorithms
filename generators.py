from process import Process
from random import randrange


def generate_processes(process_range, arrival_range, duration_range):
    target_list = []
    """
    :param process_range: how much process to generate
    :param arrival_range: specify the range of arrivals
    :param duration_range:  specify the range of durations (>0)
    :param target_list: appends to the given list
    :return: list of processes
    """
    for i in range(process_range):
        process = Process(i, randrange(arrival_range),
                          randrange(1, duration_range))
        target_list.append(process)
    return target_list


def generate_pages():
    pass
