"""
Given an array of positive integers, return the number of elements that are strictly 
greater than the average of all previous elements. Skip the first element.

def countResponseTimeRegressions(responseTimes):
    # here u can code


"""

# moje rozwiązanie -> ok 

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


# # ai -> ok 

# def countResponseTimeRegressions(responseTimes):
#     count = 0
#     prefix_sum = 0

#     for i in range(len(responseTimes)):
#         if i > 0:
#             average = prefix_sum / i
#             if responseTimes[i] > average:
#                 count += 1
#         prefix_sum += responseTimes[i]
#     return count


