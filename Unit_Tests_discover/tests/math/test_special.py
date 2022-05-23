import warnings, unittest
from src.math.special import Special

class SpecialTest(unittest.TestCase):
    """
    Automated test for the Special class.

    Attributes
    ----------
    No attributes.
    """

    def __init__(self, *args, **kargs):
        """
        Initializes class attributes.

        Parameters
        ----------
        No parameters.

        Raises
        ------
        No raises.
        """
        super(SpecialTest, self).__init__(*args, **kargs)

    def setUp(self):
        """
        Warm up for test cases ignoring warnings.

        Parameters
        ----------
        No parameters.

        Raises
        ------
        No raises.
        """
        warnings.simplefilter('ignore')

    def test_factorial(self):
        """
        Test the factorial function

        Assumptions
        -----------
        No assumptions.

        Expects
        -------
        factorial = 120
        """

        s = Special()
        self.assertEqual(120, s.factorial(5))

    def test_fibonacci(self):
        """
        Test the fibonacci function

        Assumptions
        -----------
        No assumptions.

        Expects
        -------
        fibonacci = 8
        """

        s = Special()
        self.assertEqual(8, s.fibonacci(6))
