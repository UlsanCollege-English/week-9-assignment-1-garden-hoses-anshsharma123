from garden_hoses import min_cost_connect
import heapq

def ref_cost(arr):
    h = list(arr)
    heapq.heapify(h)
    total = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        total += a + b
        heapq.heappush(h, a + b)
    return total

# --- normal tests ---
def test_small_known_1():
    assert min_cost_connect([1,2,3,4]) == 19

def test_small_known_2():
    assert min_cost_connect([5,2,4]) == 17  # corrected

def test_small_known_3():
    assert min_cost_connect([8,4,6,12]) == 58

def test_small_known_4():
    assert min_cost_connect([20,4,8,2]) == 54

# --- edge cases ---
def test_empty():
    assert min_cost_connect([]) == 0

def test_single():
    assert min_cost_connect([7]) == 0

def test_all_ones():
    assert min_cost_connect([1,1,1,1]) == 8

# --- more complex ---
def test_descending_many():
    arr = [10,9,8,7,6]
    assert min_cost_connect(arr) == ref_cost(arr)

def test_mixed_values():
    arr = [31,12,7,18,3,25]
    assert min_cost_connect(arr) == ref_cost(arr)

def test_larger_specific():
    arr = [6,5,4,3,2,7,8,9,1]
    assert min_cost_connect(arr) == ref_cost(arr)
