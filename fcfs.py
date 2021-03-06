from process import Process


def fcfs_algorithm(list_of_processes):
    elapsed_time = 0

    for process in list_of_processes:

        # if the earliest process starts at process.arrival_time and its >0
        if elapsed_time == 0:
            if process.arrival_time > elapsed_time:
                elapsed_time = process.arrival_time

        # start the process
        process.started = True
        process.execution_time = elapsed_time
        elapsed_time += process.duration_time
        process.finished = True
        process.termination_time = elapsed_time
        time = [process.execution_time, process.termination_time]
        process.working_list = time

        # for the rest of processes that are waiting
        for rest in list_of_processes:
            if not rest.finished:
                # if the process arrived and is waiting
                if rest.arrival_time < elapsed_time:
                    delay = elapsed_time - rest.arrival_time
                    rest.waiting_time = delay
                    time = [rest.arrival_time, elapsed_time]
                    rest.waiting_list = time

    for process in list_of_processes:
        # count processes and their average waiting time
        Process.count_FCFS += 1
        Process.average_wait_FCFS.append(process.waiting_time)

    return list_of_processes
