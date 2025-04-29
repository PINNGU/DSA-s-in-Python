import matplotlib.pyplot as plt

def plot_array(arr,alg, idx1=None, idx2=None,time = 0.2):
    plt.clf()
    colors = ['skyblue'] * len(arr)

    if idx1 is not None:
        colors[idx1] = 'red'
    if idx2 is not None:
        colors[idx2] = 'orange'

    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(f"{alg}")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(time)
    
def plot_merge(numbers, color_positions=None):
    plt.clf()
    colors = ['lightblue'] * len(numbers)
    if color_positions:
        for idx in color_positions:
            colors[idx] = 'orange'  # highlight currently merging elements
    plt.bar(range(len(numbers)), numbers, color=colors)
    plt.title(f"Merge Sort")
    plt.pause(0.5)

def plot_binary_search(arr, low, mid, high):
    colors = []
    for i in range(len(arr)):
        if i == mid:
            colors.append('red')      # Mid = red
        elif i == low:
            colors.append('green')    # Low = green
        elif i == high:
            colors.append('blue')     # High = blue
        else:
            colors.append('gray')

    plt.clf()
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(f"Binary Search: low={low}, mid={mid}, high={high}")
    plt.pause(1)  # pause to show update
