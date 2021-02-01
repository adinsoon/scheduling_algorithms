from generators import generate_processes
from config import RR_PROCESS_RANGE, RR_ARRIVAL_RANGE, RR_DURATION_RANGE, \
    RR_QUANTUM
from config import FCFS_PROCESS_RANGE, FCFS_ARRIVAL_RANGE, \
    FCFS_DURATION_RANGE, USE_RR_TO_FCFS
from utils import prepare_processes_list, save_processes
from round_robin import round_robin_algorithm as rr
from fcfs import fcfs_algorithm as fcfs
from matplotlib_processes import rr_plot, fcfs_plot
from copy import deepcopy

list_of_processes: list = []


def case_rr(timestamp):
    # generate list of processes
    global list_of_processes
    list_of_processes = generate_processes(RR_PROCESS_RANGE,
                                           RR_ARRIVAL_RANGE,
                                           RR_DURATION_RANGE)
    # save to file
    reason_generated = 'RR_GENERATED'
    reason_sorted = 'RR_SORTED'
    if USE_RR_TO_FCFS:
        reason_generated = 'RR_&_FCFS_GENERATED'
        reason_sorted = 'RR_&_FCFS_SORTED'

    # before sorting, raw generated
    save_processes(reason_generated, list_of_processes, timestamp)
    # after sorting by arrival_time
    list_of_processes_RR = prepare_processes_list(list_of_processes)
    save_processes(reason_sorted, list_of_processes_RR, timestamp)

    # execute the algorithm
    round_robin_result = rr(list_of_processes_RR, RR_QUANTUM)

    # save results
    save_processes('RR_DONE', round_robin_result, timestamp)

    # make a plot
    rr_plot(round_robin_result, timestamp)


def case_fcfs(timestamp):
    if not USE_RR_TO_FCFS:
        fcfs_list_of_processes = generate_processes(FCFS_PROCESS_RANGE,
                                                    FCFS_ARRIVAL_RANGE,
                                                    FCFS_DURATION_RANGE)
        reason_generated = 'FCFS_GENERATED'
        reason_sorted = 'FCFS_SORTED'
        # before sorting, raw generated
        save_processes(reason_generated, fcfs_list_of_processes, timestamp)
        # after sorting by arrival_time
        list_of_processes_FCFS = prepare_processes_list(fcfs_list_of_processes)
        save_processes(reason_sorted, list_of_processes_FCFS, timestamp)
    else:
        list_of_processes_FCFS = deepcopy(list_of_processes)

    # execute the algorithm
    # fcfs_result = fcfs(list_of_processes_FCFS)

    # save results
    # save_processes('FCFS_DONE', fcfs_result, timestamp)

    # make a plot
    # fcfs_plot(fcfs_result, timestamp)
