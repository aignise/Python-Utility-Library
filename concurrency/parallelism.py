from multiprocessing import Pool

def parallel_function(x):
    """
    A simple function to demonstrate parallelism.
    """
    return x * x

def main():
    data = [i for i in range(10)]
    with Pool() as pool:
        results = pool.map(parallel_function, data)
    print(f"Results: {results}")

main()  # To execute the tasks
