from frame import Frame


def fifo_algorithm(list_of_calls, list_of_frames):
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
                    Frame.logs_FIFO[f'{moment}'] = 'FAULT'
                    frame.log.append(moment)
                    # reload of value
                    frame.reload = moment
                    done = True
            # if call meet value equals itself
            elif frame.value == call:
                frame.values[f'{moment}'] = call
                Frame.logs_FIFO[f'{moment}'] = 'HIT'
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
                                Frame.logs_FIFO[f'{moment}'] = 'FAULT'
                                found.log.append(moment)
                                found.reload = moment
                                done = True
            if done:
                # fill rest with previous value
                for rest in list_of_frames:
                    rest.values[f'{moment}'] = rest.value
                break

    return list_of_frames
