def factorial(n: int) -> int:
    """
    Computes the factorial of the input number by recustion

    Arguments
    ---------
        n : int
            the input number

    Returns
    -------
        int
            the factorial of the input number
    """
    return 1 if n <= 1 else n * factorial(n - 1)
