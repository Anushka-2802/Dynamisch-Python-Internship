import tracemalloc
# Decorator to measure memory usage
def memory_usage(func):
    def wrapper():
        '''Wrapper function used inside the decorator to measure
           the memory usage of the given function.
           It starts memory tracking, executes the original function,
           displays current and peak memory usage, and then stops tracking'''
        
        tracemalloc.start() # Start tracking memory
        
        func() # Call the original function

        current, peak = tracemalloc.get_traced_memory()

        print(f"Current Memory Usage: {current / 1024:.2f} KB")
        print(f"Peak Memory Usage: {peak / 1024:.2f} KB")

        tracemalloc.stop() # Stop tracking memory

    return wrapper

@memory_usage
def create_list():
    numbers = [i for i in range(10000)]
    print("List Created")

create_list()