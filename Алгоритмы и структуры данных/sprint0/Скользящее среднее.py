def moving_average(timeseries, K):
    result = []
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result


n = int(input())
arr = list(map(int, input().strip().split()))
window_size = int(input())
print(" ".join(map(str, moving_average(arr, window_size))))
