# Recursive and iterative Computation

def analyze_recursive_iterative(n):

    # Factorial by iterative approach
    def fact(n):
        fact=1
        if n==0:
            return 1
        for i in range(1,n+1):
            fact*=i
        return fact

    # Factorial by recurrsion
    fib_count=0
    def rfact(n):
        nonlocal fib_count
        fib_count+=1
        if n==0:
            return 1
        return n*rfact(n-1)

    # Fibonnacci using recursion
    def rfib(n):
        if n<=1:
            return n
        return rfib(n-1)+rfib(n-2)

    # Fibonnacci using iteration
    def fib(n):
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return a

    rfact_ans = rfact(n)
    fact_ans = fact(n)

    fib_count = 0
    rfib_ans = rfib(n)
    fib_ans = fib(n)

    print("Computation Analysis Report")
    print("Recursive Factorial:", rfact_ans)
    print("Iterative Factorial:", fact_ans)
    print("Recursive Fibonacci:", rfib_ans)
    print("Iterative Fibonacci:", fib_ans)
    print("Operation Count Comparison")
    print("Recursive Factorial Count:", n + 1)
    print("Iterative Factorial Count:", n)
    print("Recursive Fibonacci Count:", fib_count)
    print("Iterative Fibonacci Count:", n)

    return []

n = int(input("Enter the number : "))
analyze_recursive_iterative(n)