# Experiment 23: Module containing the Fibonacci function
def fibonacci(n):
    """
    Generate a Fibonacci series up to n terms.
    Returns a list containing the series.
    """
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
