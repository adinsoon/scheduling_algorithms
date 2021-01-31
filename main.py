from process_plan import case_rr, case_fcfs
from page_swap import case_fifo, case_lru
import time

timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")


if __name__ == '__main__':
    case_rr(timestamp)
    # case_fcfs()
    # case_fifo()
    # case_lru()
