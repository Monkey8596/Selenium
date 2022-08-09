from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchstests import Searchstests

assertipons_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(Searchstests)

smoke_test = TestSuite([assertipons_test, search_test])

kwargs={
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)