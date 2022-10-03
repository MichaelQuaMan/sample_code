import random
import time
import unittest

from my_nn.nn import MyNnIndex
from my_nn.point import Point
from tests.fixtures.expected import expected_01
from tests.fixtures.test_points import many_index_points, many_query_points


class TestMyNnIndex(unittest.TestCase):
    @staticmethod
    def rand_point(random_lower=-1000, random_upper=1000):
        return random.uniform(random_lower, random_upper), random.uniform(random_lower, random_upper)

    def get_n_points(self, n):
        return [Point(*self.rand_point()) for _ in range(n)]

    def get_bulk_points(self, n_index_points=10000, n_query_points=1000):
        return self.get_n_points(n_index_points), self.get_n_points(n_query_points)

    @staticmethod
    def get_nn_slow_time(obj, query_points):
        expected = []
        start = time.time()
        for query_point in query_points:
            expected.append(obj.find_nearest_slow(query_point))
        period = time.time() - start
        return period, expected

    def test_basic(self):
        """Tests a handful of nearest neighbor queries to make sure they return the right result."""
        test_points = [
            Point(1, 2),
            Point(1, 0),
            Point(10, 5),
            Point(-1000, 20),
            Point(3.14159, 42),
            Point(42, 3.14159),
        ]
        uut = MyNnIndex(test_points)

        expected = (1, 0)
        query_point = Point(0, 0)
        actual = uut.find_nearest(query_point)
        self.assertEqual(expected, actual.as_tup())

        expected = (42, 3.14159)
        query_point = Point(40, 3)
        actual = uut.find_nearest(query_point)
        self.assertEqual(expected, actual.as_tup())

    def test_out_of_bounds(self):
        test_points = [
            Point(1, 2),
            Point(1, 0),
            Point(10, 5),
            Point(-1000, 20),
            Point(3.14159, 42),
            Point(42, 3.14159),
        ]
        uut = MyNnIndex(test_points)

        query_point = Point(-2000, 0)  # point is out of bounds
        actual = None
        with self.assertRaises(ValueError) as e:
            actual = uut.find_nearest(query_point)
        self.assertEqual(None, actual)

    def test_sparse(self):
        """Tests a handful of nearest neighbor queries to make sure they return the right result."""
        test_points = [
            Point(-1000, 20)
        ]
        uut = MyNnIndex(test_points)

        expected = (-1000, 20)
        query_point = Point(0, 0)
        actual = uut.find_nearest(query_point)
        self.assertEqual(expected, actual.as_tup())

    def test_edge_case_query_points(self):
        """Test edge case query points.
        origin          => x = 0 and y = 0
        positive x-axis => x > 0 and y = 0
        negative x-axis => x < 0 and y = 0
        positive y-axis => x = 0 and y > 0
        negative y-axis => x = 0 and y < 0
        """
        index_points = [
            Point(1, 2),
            Point(1, 0),
            Point(10, 5),
            Point(-1000, 20),
            Point(3.14159, 42),
            Point(42, 3.14159),
        ]

        query_points = [
            Point(0, 0),  # origin => x = 0 and y = 0
            Point(1, 0),  # positive x-axis => x > 0 and y = 0
            Point(-1, 0),  # negative x-axis => x < 0 and y = 0
            Point(0, 1),  # positive y-axis => x = 0 and y > 0
            Point(0, -1),  # negative y-axis => x = 0 and y < 0
        ]

        actual = []
        expected = [Point(1, 0).as_tup(), Point(1, 0).as_tup(), Point(1, 0).as_tup(), Point(1, 2).as_tup(),
                    Point(1, 0).as_tup()]
        uut = MyNnIndex(index_points)

        for point in query_points:
            actual.append(uut.find_nearest(point).as_tup())

        self.assertEqual(expected, actual)

    def test_many_points(self):
        actual = []
        expected = [Point(*i).as_tup() for i in expected_01]
        index_points = [Point(*i) for i in many_index_points]
        query_points = [Point(*i) for i in many_query_points]
        uut = MyNnIndex(index_points)

        for point in query_points:
            actual.append(uut.find_nearest(point).as_tup())

        self.assertEqual(expected, actual)

    def test_benchmark(self):
        """Tests values using the slow and fast version of the index to determine the effective speedup."""
        actual = []
        index_points, query_points = self.get_bulk_points()
        uut = MyNnIndex(index_points)

        slow_time, expected = self.get_nn_slow_time(uut, query_points)  # Benchmark score

        # Time custom NN method
        start = time.time()
        for point in query_points:
            actual.append(uut.find_nearest(point).as_tup())
        new_time = time.time() - start

        print("-- Expanding Area Search --")
        if slow_time and new_time:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")
            print(f"speedup: {(slow_time / new_time):0.2f}x")
        else:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")

    def test_worst_case_benchmark(self):
        """Test with query points and index points on opposite edges of boundary."""

        # Max points
        def rand_max_point(random_lower=800, random_upper=1000):
            return random.uniform(random_lower, random_upper), random.uniform(random_lower, random_upper)

        def get_n_max_points(n):
            return [Point(*rand_max_point()) for _ in range(n)]

        def get_bulk_max_points(n_index_points=10000):
            return get_n_max_points(n_index_points)

        # Min points
        def rand_min_point(random_lower=-1000, random_upper=-800):
            return random.uniform(random_lower, random_upper), random.uniform(random_lower, random_upper)

        def get_n_min_points(n):
            return [Point(*rand_min_point()) for _ in range(n)]

        def get_bulk_min_points(n_query_points=1000):
            return get_n_min_points(n_query_points)

        actual = []
        index_points = get_bulk_max_points()
        query_points = get_bulk_min_points()
        uut = MyNnIndex(index_points)

        slow_time, expected = self.get_nn_slow_time(uut, query_points)  # Benchmark score

        # Time custom NN method
        start = time.time()
        for point in query_points:
            actual.append(uut.find_nearest(point).as_tup())
        new_time = time.time() - start

        print("-- Worst Case Expanding Area Search --")
        if slow_time and new_time:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")
            print(f"speedup: {(slow_time / new_time):0.2f}x")
        else:
            print(f"slow time: {slow_time:0.2f}sec")
            print(f"new time: {new_time:0.2f}sec")


if __name__ == "__main__":
    unittest.main()
