import heapq

def min_cost_connect(lengths):
    """
    Return the minimal total cost to connect all hoses into one.
    Joining two hoses costs the sum of their lengths.
    """
    # Edge case: 0 or 1 hose
    if not lengths or len(lengths) <= 1:
        return 0

    # Make a copy to avoid modifying the input list
    h = list(lengths)
    heapq.heapify(h)

    total_cost = 0

    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        join_cost = a + b
        total_cost += join_cost
        heapq.heappush(h, join_cost)

    return total_cost
