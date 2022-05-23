class Special:
    """
    Class implements special math functions.

    Attributes
    ----------
    No attributes.
    """

    def __init__(self):
        """
        Initializes class attributes.

        Parameters
        ----------
        No parameters.

        Raises
        ------
        No raises.
        """

        pass

    def factorial(self, n: int) -> int:
        """
        Calculates factorial

        Parameters
        ----------
        n: int
            Number to compute factorial.

        Raises
        ------
        No raises.

        Returns
        -------
        No returns.
        """

        fact = 1
        for i in range(1, n + 1):
            fact = fact * i

        return fact

    def fibonacci(self, n: int) -> int:
        """
        Predicts maximum and minimum candle values by Machine Learning.

        Parameters
        ----------
        n: int
            Number to compute fibonacci

        Raises
        ------
        No raises.

        Returns
        -------
        Tuple[int, int] value.
        """

        if n <= 1:
            return n
        else:
            return (self.fibonacci(n - 1) + self.fibonacci(n - 2))
