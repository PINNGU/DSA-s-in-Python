from sorts.bubble import bubble
from sorts.insertion import insertion
from sorts.selection import selection
from sorts.counting import counting
from sorts.merge import merge
from sorts.radix import radix
from searches.linear import linear
from searches.binary import binary
import matplotlib.pyplot as plt

numbers = [2, 7, 54, 17, 29, 64, 43, 33, 47, 4, 82, 90, 40, 78, 92, 68, 76, 37, 19, 25]

def option(nums,opt):

    plt.ion()
    if opt == "bubble":
        bubble(nums)
    elif opt == "insertion":
        insertion(nums)
    elif opt == "selection":
        selection(nums)
    elif opt == "counting":
        counting(nums)
    elif opt == "merge":
        merge(nums)
    elif opt == "linear_search":
        linear(nums,40)
    elif opt == "binary_search":
        binary(nums,76)

    plt.ioff()
    plt.show()

option(numbers,"binary_search")