def collapseRanges(susceptible_list):
    # susceptible is a list
    # each item is a tuple of signal and range, e.g., ('c_in', [0, 4])

    # intervals_per_sig a dictionary
    # each value item is a list of ranges, e.g., ('c_in', [0, 4], [6, 10], [15, 17])
    intervals_per_sig = {}

    for s in susceptible_list:
        sig = s[0]
        range = s[1]
        # print(f'current signal = {sig} and current range = {range}')
        if sig in intervals_per_sig:
            last_added_range = intervals_per_sig[sig][-1]
            # print(f'last added range = {last_added_range} and last_to in range = {last_added_range[1]}')
            if last_added_range[1] == range[0]:
                intervals_per_sig[sig][-1] = [last_added_range[0], range[1]]
                # print(f'new range = {intervals1_per_sig[sig][-1]}')
            else:
                intervals_per_sig[sig].append(range)
        else:
            intervals_per_sig[sig] = [range]

    return intervals_per_sig


def appendSAF(intervals_per_sig, SAF):
    """
    append SAF type for each susceptible interval
    to differentiate in plotting between SA1 & SA0
    """
    susceptible_SAF = []
    for sig in intervals_per_sig:
        susceptible_SAF.append(
            {(sig, tuple(item), SAF) for item in intervals_per_sig[sig]}
        )
    return susceptible_SAF
