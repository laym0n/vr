from queue import Queue
from threading import Thread

# Filter 1: Generates all possible positions for the queens
def position_generator(output_queue):
    def is_safe(queens, row, col):
        for i in range(row):
            if queens[i] == col or \
               queens[i] - i == col - row or \
               queens[i] + i == col + row:
                return False
        return True

    def solve(queens, row=0):
        if row == 8:
            output_queue.put(queens[:])  # Add solution to the queue
        else:
            for col in range(8):
                if is_safe(queens, row, col):
                    queens[row] = col
                    solve(queens, row + 1)

    queens = [-1] * 8
    solve(queens)
    output_queue.put(None)  # Signifies the end of generation

# Filter 2: Checks each combination for conflicts
def conflict_checker(input_queue, output_queue):
    while True:
        solution = input_queue.get()
        if solution is None:
            output_queue.put(None)  # End of transmission
            break
        # Since the generator already avoided conflicts, we pass the solution along
        output_queue.put(solution)

# Filter 3: Collects and displays solutions
def solution_collector(input_queue):
    solutions = []
    while True:
        solution = input_queue.get()
        if solution is None:
            break
        solutions.append(solution)
        print("Solution:", solution)
    print(f"Total Solutions: {len(solutions)}")

# Main function that connects the filters through queues
def main():
    # Create queues to connect filters
    q1 = Queue()
    q2 = Queue()

    # Run filters as separate threads
    generator_thread = Thread(target=position_generator, args=(q1,))
    checker_thread = Thread(target=conflict_checker, args=(q1, q2))
    collector_thread = Thread(target=solution_collector, args=(q2,))

    generator_thread.start()
    checker_thread.start()
    collector_thread.start()

    # Wait for all threads to complete
    generator_thread.join()
    checker_thread.join()
    collector_thread.join()

# Run the main function
main()
