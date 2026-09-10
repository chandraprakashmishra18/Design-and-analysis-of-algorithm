def generate_execution_observation_table(sizes):
    def fib_calls(n):
        if n <= 1:
            return 1
        return 1 + fib_calls(n - 1) + fib_calls(n - 2)

    table = []

    table.append("Algorithm Execution Observation Table")
    table.append("InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort")

    for n in sizes:
        table.append(
            f"{n} {n + 1} {n} {fib_calls(n)} {n} {n} {n.bit_length()} {n * (n - 1) // 2} {n * (n - 1) // 2}"
        )

    return table