from generators import generate_processes
from config import RR_PROCESS_RANGE, RR_ARRIVAL_RANGE, RR_DURATION_RANGE, \
    RR_QUANTUM
from utils import prepare_processes_list, save_processes

list_of_processes: list = []


def case_rr(timestamp):
    # generate list of processes
    generate_processes(RR_PROCESS_RANGE, RR_ARRIVAL_RANGE,
                       RR_DURATION_RANGE, list_of_processes)
    # save to file
    reason_generated = 'RR_GENERATED'
    reason_sorted = 'RR_SORTED'

    # before sorting, raw generated
    save_processes(reason_generated, list_of_processes, timestamp)
    # after sorting by arrival_time
    list_of_processes_RR = prepare_processes_list(list_of_processes)
    save_processes(reason_sorted, list_of_processes_RR, timestamp)


def case_fcfs():
    pass
