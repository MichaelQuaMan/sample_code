import unittest

from my_nn.nn import BinSpace
from my_nn.point import Point
from tests.fixtures.expected import expected_03, expected_04, expected_05
from tests.fixtures.test_points import many_index_points


class TestBinSpace(unittest.TestCase):
    def setUp(self) -> None:
        self.points = [
            Point(1, 2),
            Point(1, 0),
            Point(10, 5),
            Point(-1000, 20),
            Point(3.14159, 42),
            Point(42, 3.14159),
        ]
        self.index_points = [Point(*i) for i in many_index_points]
        self.index = BinSpace(length=(-1000, 1000), width=(-1000, 1000), points=self.index_points)
        self.space = BinSpace(length=(-1000, 1000), width=(-1000, 1000), points=self.points)

        self.all_bin_coords = [(x, y) for x in range(0, 10) for y in range(0, 10)]
        self.point_in_all_regions = [Point(i, j) for i in range(-900, 1100, 200) for j in range(-900, 1100, 200)]

    def test_make_bins(self):
        self.index.make_bins()
        self.assertEqual(100, len(self.index.bin_map))
        for i in self.all_bin_coords:
            b = self.index.bin_map.get(i)
            if not b:
                raise ValueError("missing bin")
            if b.has_points:
                raise ValueError("should not have points")
            self.assertEqual(i, b.coord)

    def test_place_points(self):
        self.index.make_bins()
        self.assertEqual(100, len(self.index.bin_map))
        self.index.place_points()
        self.assertEqual(len(self.index_points), len(self.index.points))

        bins_with_points = []
        for k, v in self.index.bin_map.items():
            if v.has_points:
                bins_with_points.append(k)
        expected = expected_03
        self.assertEqual(len(expected), len(bins_with_points))
        self.assertEqual(expected, bins_with_points)

    def test_find_bin(self):
        self.space.make_bins()
        self.assertEqual(100, len(self.space.bin_map))
        self.space.place_points()
        self.assertEqual(len(self.points), len(self.space.points))
        query_points = [
            Point(0, 0),  # origin => x = 0 and y = 0
            Point(1, 0),  # positive x-axis => x > 0 and y = 0
            Point(-1, 0),  # negative x-axis => x < 0 and y = 0
            Point(0, 1),  # positive y-axis => x = 0 and y > 0
            Point(0, -1),  # negative y-axis => x = 0 and y < 0
        ]
        actual = []
        for pt in query_points:
            actual.append(self.space.find_bin(pt).coord)
        expected = [(5, 5), (5, 4), (4, 4), (4, 5), (4, 4)]
        self.assertEqual(expected, actual)

        actual = []
        for pt in self.point_in_all_regions:
            actual.append(self.space.find_bin(pt).coord)
        expected = expected_04
        self.assertEqual(expected, actual)

    def test_get_bins_with_points(self):
        self.space = BinSpace(length=(-1000, 1000), width=(-1000, 1000), points=self.point_in_all_regions)
        self.space.make_bins()
        self.assertEqual(100, len(self.space.bin_map))
        actual = self.space.get_bins_with_points()
        expected = []
        self.assertEqual(expected, actual)
        self.space.place_points()
        actual = self.space.get_bins_with_points()
        self.assertEqual(100, len(actual))
        actual = [i.coord for i in actual]
        expected = expected_05
        self.assertEqual(expected, actual)

    def test_find_nearest(self):
        self.assertEqual(True, False)

    def test_get_total_points(self):
        self.assertEqual(True, False)

    def test_search_bins(self):
        self.assertEqual(True, False)

    def test_search_nn(self):
        self.assertEqual(True, False)

    def test_get_rand_coordinates(self):
        self.assertEqual(True, False)

    def test_get_points(self):
        self.assertEqual(True, False)

    def test_get_point_objects(self):
        self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()
