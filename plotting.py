import matplotlib.pyplot as plt

def plot_array(arr,alg, idx1=None, idx2=None):
    plt.clf()
    colors = ['skyblue'] * len(arr)

    if idx1 is not None:
        colors[idx1] = 'red'
    if idx2 is not None:
        colors[idx2] = 'orange'

    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(f"{alg} Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.2)
    
def plot_merge(numbers, color_positions=None):
    plt.clf()
    colors = ['lightblue'] * len(numbers)
    if color_positions:
        for idx in color_positions:
            colors[idx] = 'orange'  # highlight currently merging elements
    plt.bar(range(len(numbers)), numbers, color=colors)
    plt.title(f"Merge Sort")
    plt.pause(0.5)
