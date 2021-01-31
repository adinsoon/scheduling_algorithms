import numpy


class Process:

    average_wait_RR: list = []
    switches_RR: int = 0
    count_RR = 0

    def __init__(self, name, arrival, duration):
        # PID
        self.name: int = name
        Process.count_RR += 1
        ###
        # each process has its own arrival and duration time
        self.arrival_time: int = arrival
        self.duration_time: int = duration
        # for algorithm
        self.duration_time_copy: int = duration
        ##
        # each process has its own execution and termination time during
        # algorithm, then waiting time is calculated
        self.execution_time: int = 0
        self.termination_time: int = 0
        self.waiting_time: int = 0
        ##
        # each list consist of given times
        self.working_list: list = []
        self.waiting_list: list = []
        ###
        self.started: bool = False
        self.finished: bool = False

    def __str__(self):
        name = "P" + str(self.name) + " (" + str(self.arrival_time) + ", " + \
            str(self.duration_time) + ")"
        return name

    def get_set_times(self):
        response = f'{self.name} \t' \
                   f'{self.arrival_time} ms\t \t' \
                   f'{self.duration_time} ms\n'
        return response

    def get_completed_times(self):
        response = f'\t\t {self.waiting_time} ms \t\t' \
                   f'{self.execution_time} ms \t\t' \
                   f'{self.termination_time} ms \n'
        return response

    def get_working(self):
        return self.working_list

    def get_waiting(self):
        return self.waiting_list

    @classmethod
    # for RR
    def get_avg_rr(cls):
        sums = 0
        for times in Process.average_wait_RR:
            sums += times
        return round(sums / Process.count_RR, 3)

    @classmethod
    # for RR
    def get_switches_rr(cls):
        return Process.switches_RR

    @classmethod
    # for RR
    def get_std_rr(cls):
        return numpy.around(numpy.std(Process.average_wait_RR, ddof=1), 3)
