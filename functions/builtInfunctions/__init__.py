
from functools import reduce

from itertools import accumulate
from operator import add


# from functools import reduce
#
# # --- The Map Function ---

numbers = [1, 2, 3, 4]


squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared List: {squared_numbers}")

# # --- The Reduce Function ---

max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum Value: {max_value}")

# # -- the Filter function ---

filtered_number=list(filter(lambda x:x%2==0,numbers))
print(f"Filtered List: {filtered_number}")

# # --- The Accumulator Function ---

accumulate_function=accumulate(numbers,add)
print(f"Accumulate Function: {list(accumulate_function)}")
