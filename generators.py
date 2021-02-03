from process import Process
from frame import Frame
from random import randrange


def generate_processes(process_range, arrival_range, duration_range):
    """
    :param process_range: how many processes to generate
    :param arrival_range: specify the range of arrivals
    :param duration_range:  specify the range of durations (>0)
    :return: list of processes
    """
    target_list = []

    for i in range(process_range):
        process = Process(i, randrange(arrival_range),
                          randrange(1, duration_range))
        target_list.append(process)

    return target_list


def generate_calls(calls_range, value_range):
    """
    :param calls_range: how many calls to generate
    :param value_range: specify the range of calls value
    """
    calls_list: list = []

    for i in range(calls_range):
        calls_list.append(randrange(1, value_range + 1))

    return calls_list


def generate_frames(frames_range):
    """
    :param frames_range: how many frames to generate
    :return: list of frames
    """
    target_list: list = []

    for i in range(frames_range):
        target_list.append(Frame(i))

    return target_list
