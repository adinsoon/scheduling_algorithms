import operator
import os
import math
from process import Process

dest = os.path.dirname(__file__)


def check_config(config):
    for key, value in config.items():
        if type(value) is dict:
            check_config(value)
        else:
            if value < 0:
                raise ValueError(f"An error occurred while validating config.\n"
                                 f"The variable that raised the error: "
                                 f"{key}.\nPlease make sure that all "
                                 f"variables are not lesser than zero.")


def prepare_processes_list(list_of_processes):
    """
    :param list_of_processes:
    :return: sorted by arrival time (in the order in which they would come
    to the processor) without proceeding the algorithm yet
    """
    prepared_list = sorted(list_of_processes, key=operator.attrgetter(
        'arrival_time'))
    return prepared_list


def save_processes(reason, source_list, timestamp):
    # every file will be saved to given dir
    target = dest + "/" + timestamp
    os.makedirs(target, exist_ok=True)

    # every file has its own prefix
    prefix = f'{reason}_'
    title = prefix + timestamp + ".txt"

    file = open(os.path.join(target, title), "w")
    # column names
    desc = "PID \t ARRIVAL \t DURATION \t WAITING \t START \t \t " \
           "TERMINATION \n"
    file.write(desc)

    for process in source_list:
        file.write(process.get_set_times().rstrip())
        file.write(process.get_completed_times())
    file.write('\n')
    file.write('\n')
    if reason == 'RR_DONE':
        file.write(f'Average waiting time: {Process.get_avg_rr()} \t')
        file.write(f'Std: {Process.get_std_rr()} \n')
        file.write(f'Switches: {Process.get_switches_rr()}')

    file.close()


def save_calls():
    pass


def save_pages():
    pass


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10 + 10
