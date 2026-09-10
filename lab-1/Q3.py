def generate_execution_observation_table(sizes):

    def count_rec_fib(n):
        calls = [0] * (n + 1)

        if n >= 0:
            calls[0] = 1

        if n >= 1:
            calls[1] = 1

        for i in range(2, n + 1):
            calls[i] = calls[i - 1] + calls[i - 2] + 1

        return calls[n]

    result = []

    result.append("Algorithm Execution Observation Table")

    result.append(
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci "
        "IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    )

    for n in sizes:
        row = [
            n,
            n + 1,
            n,
            count_rec_fib(n),
            n,
            n,
            n.bit_length(),
            (n * (n - 1)) // 2,
            (n * (n - 1)) // 2
        ]

        result.append(" ".join(map(str, row)))

    return result