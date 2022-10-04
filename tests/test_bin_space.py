import unittest

from my_nn.nn import BinSpace
from my_nn.point import Point
from tests.fixtures.expected import expected_03
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
        # self.index = BinSpace(length=(-1000, 1000), width=(-1000, 1000), points=self.points)

    def test_make_bins(self):
        self.assertEqual(True, False)

    def test_place_points(self):
        self.index = BinSpace(length=(-1000, 1000), width=(-1000, 1000), points=self.index_points)
        self.index.make_bins()
        self.assertEqual(100, len(self.index.bin_map))
        self.index.place_points()
        self.assertEqual(len(self.index_points), len(self.index.points))

        bins_with_points = []
        for k, v in self.index.bin_map.items():
            if v.has_points:
                bins_with_points.append(k)
        self.assertEqual(len(expected_03), len(bins_with_points))
        self.assertEqual(expected_03, bins_with_points)

    def test_find_bin(self):
        self.assertEqual(True, False)

    def test_get_bins_with_points(self):
        self.assertEqual(True, False)

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
