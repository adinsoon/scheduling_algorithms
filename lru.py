from frame import Frame


def lru_algorithm(list_of_calls, list_of_frames):
    # well, lru algorithm is almost identical to the fifo_algorithm
    # but this time, reload is made also if the call meet value equal to itself
    # technically, it is possible to merge both algorithms into one function and
    # through one additional parameter choose whether the additional part below
    # > frame.reload = moment
    # in elif frame.value == call should be executed or not
    # as it is the only difference between fifo and lru
    # also saving logs into different class' variable should not be a problem
    # so at least according to the D-R-Y, there will be only one function
    # for drawing tables as it is the same story as with algorithms

    # to start from zero in loop
    moment = -1

    for call in list_of_calls:

        moment += 1

        for frame in list_of_frames:
            done = False
            # if call meet zero (say empty spot in frame)
            if frame.value == 0:
                # check if free
                if not frame.taken:
                    frame.taken = True
                    frame.value = call
                    frame.values[f'{moment}'] = call
                    Frame.logs_LRU[f'{moment}'] = 'FAULT'
                    frame.log.append(moment)
                    # reload of value
                    frame.reload = moment
                    done = True
            # if call meet value equals itself
            elif frame.value == call:
                frame.values[f'{moment}'] = call
                Frame.logs_LRU[f'{moment}'] = 'HIT'
                # # # # # # mentioned part
                frame.reload = moment
                # # # # # #
                done = True
            # if call meet value different from itself
            else:
                # list of reload times of each frame
                span = []
                # if all frames are taken
                if all(frame.taken for frame in list_of_frames):
                    # if this value is nowhere found
                    if not any(frame.value == call for frame in list_of_frames):
                        # find oldest reload time
                        for item in list_of_frames:
                            span.append(item.reload)
                        switch = min(span)
                        # change value in the found frame
                        for found in list_of_frames:
                            if found.reload == switch:
                                found.value = call
                                found.values[f'{moment}'] = call
                                Frame.logs_LRU[f'{moment}'] = 'FAULT'
                                found.log.append(moment)
                                found.reload = moment
                                done = True
            if done:
                # fill rest with previous value
                for rest in list_of_frames:
                    rest.values[f'{moment}'] = rest.value
                break

    return list_of_frames
