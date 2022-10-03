import random
import time
import unittest

from pynn import NearestNeighborIndex


class TestNearestNeighborIndex(unittest.TestCase):
    @staticmethod
    def rand_point():
        return random.uniform(-1000, 1000), random.uniform(-1000, 1000)

    def get_n_points(self, n):
        return [self.rand_point() for _ in range(n)]

    def get_bulk_points(self):
        return self.get_n_points(10000), self.get_n_points(1000)

    @staticmethod
    def get_nn_slow_time(obj, query_points):
        expected = []
        start = time.time()
        for query_point in query_points:
            expected.append(obj.find_nearest_slow(query_point))
        return time.time() - start

    def test_basic(self):
        """Tests a handful of nearest neighbor queries to make sure they return the right result."""
        test_points = [
            (1, 2),
            (1, 0),
            (10, 5),
            (-1000, 20),
            (3.14159, 42),
            (42, 3.14159),
        ]

        uut = NearestNeighborIndex(test_points)

        self.assertEqual((1, 0), uut.find_nearest((0, 0)))
        self.assertEqual((-1000, 20), uut.find_nearest((-2000, 0)))
        self.assertEqual((42, 3.14159), uut.find_nearest((40, 3)))

    def test_benchmark(self):
        """Tests values using the slow and fast version of the index to determine the effective speedup."""
        actual = []

        index_points, query_points = self.get_bulk_points()

        # Do not include the indexing time when benchmarking
        uut = NearestNeighborIndex(index_points)

        slow_time = self.get_nn_slow_time(uut, query_points)

        # Run the indexed tests
        start = time.time()
        for query_point in query_points:
            actual.append(uut.find_nearest(query_point))
        new_time = time.time() - start

        print(f"----")
        if slow_time and new_time:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")
            print(f"speedup: {(slow_time / new_time):0.2f}x")
        else:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")

    def multi_benchmark(self, mode="slow"):
        """Tests values using the slow and fast version of the index to determine the effective speedup."""
        actual = []

        index_points, query_points = self.get_bulk_points()

        # Do not include the indexing time when benchmarking
        uut = NearestNeighborIndex(index_points)

        slow_time = self.get_nn_slow_time(uut, query_points)

        # Run the indexed tests
        start = time.time()
        for query_point in query_points:
            actual.append(uut.find_nearest(query_point, mode=mode))
        new_time = time.time() - start

        print(f"-- Mode: {mode} --")
        if slow_time and new_time:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")
            print(f"speedup: {(slow_time / new_time):0.2f}x")
        else:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")

    def test_benchmark_fastest(self):
        """Use 3rd party kdtree lib for fast benchmark."""
        self.multi_benchmark("fastest")
