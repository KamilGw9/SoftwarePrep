def countResponseTimeRegressions(responseTimes):
    count = 0
    prefix_sum = 0 

    for i in range(len(responseTimes)):
        if i == 0:
            prefix_sum += responseTimes[i]
            continue

        average = prefix_sum / i
        if responseTimes[i] > average:
            count += 1

        prefix_sum += responseTimes[i]
    
    return count
