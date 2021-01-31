from process import Process


def round_robin_algorithm(list_of_processes, quantum):
    iteration = 0
    elapsed_time = 0
    interval = 0

    while True:

        process_start = 0
        process_end = 0

        for process in list_of_processes:

            # if the earliest process starts at process.arrival_time and its >0
            if elapsed_time == 0:
                if process.arrival_time > elapsed_time:
                    elapsed_time = process.arrival_time

            if not process.finished:

                # start the process
                if not process.started:
                    process.execution_time = elapsed_time
                    process.started = True

                else:
                    # if the process does not complete after handling
                    if process.duration_time_copy > quantum:
                        process_start = elapsed_time
                        interval = quantum
                        elapsed_time += interval
                        process.duration_time_copy -= interval
                        process_end = elapsed_time
                        time = [process_start, process_end]
                        process.working_list.append(time)
                    # if it is the last handle for given process
                    else:
                        process_start = elapsed_time
                        interval = process.duration_time_copy
                        elapsed_time += interval
                        process.termination_time = elapsed_time
                        process.end = elapsed_time
                        process.duration_time_copy = 0
                        process.finished = True
                        time = [process_start, process_end]
                        process.working_list.append(time)
            else:
                # calculate total waiting time for this process
                process.waiting_time = process.termination_time - \
                                       process.duration_time - \
                                       process.arrival_time

            # for the rest of processes that are waiting
            for rest in list_of_processes:
                # if the process arrived and is waiting
                if elapsed_time >= rest.arrival_time:
                    # and is not finished yet
                    if not rest.finished:
                        if process_start < rest.arrival_time:
                            time = [rest.arrival_time, process_end]
                        else:
                            time = [process_start, process_end]
                        if time in rest.waiting_list:
                            break
                        if process_start + interval < elapsed_time or \
                                process_end < elapsed_time:
                            break
                        else:
                            rest.waiting_list.append(time)

            iteration += 1

        # if all processes are finished, algorithm ends
        if all(process.finished for process in list_of_processes):
            break

    for process in list_of_processes:
        Process.average_wait_RR.append(process.waiting_time)
    Process.switches_RR = iteration

    return list_of_processes
