import argparse
import unittest


def run_tests(day=None):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    if day:
        test_name = f"tests.test_day{day}"
        suite.addTest(loader.loadTestsFromName(test_name))
    else:
        suite = loader.discover("./tests", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(
        f"Ran {result.testsRun} tests in {len(result.failures)} failed, {len(result.errors)} errors"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code solutions runner")
    parser.add_argument(
        "--day",
        metavar="N",
        type=int,
        nargs="+",
        help="Run specific day(s) (e.g., --day 1 2 3)",
    )
    args = parser.parse_args()

    if args.day:
        for day_num in args.day:
            run_tests(day_num)
    else:
        run_tests()
