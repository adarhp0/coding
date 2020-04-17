import heapq as hq


def largestSumAfterKNegations(a, k):
    hq.heapify(a)
    for i in range(k):
        z = hq.heappop(a)
        if z == 0:
            return sum(list(a))
        z = z*-1
        hq.heappush(a, z)
    return sum(list(a))


largestSumAfterKNegations([3, - 1, 0, 2], 3)
