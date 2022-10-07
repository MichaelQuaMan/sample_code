import math
import random

from my_nn.bin_settings import sizes
from my_nn.point import Point


class Bin:
    """Represents an individual region of the search space or area of the grid. I.e., it's a bin or container to
    hold points found to be located in a given region of space.
    """

    def __init__(self, uid=None, coord=None, width=None, length=None, x_min=None, x_max=None, y_min=None, y_max=None):
        self.uid = uid
        self.coord = coord
        self.width = width
        self.length = length
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.abs_length = abs(length[0] - length[1])
        self.abs_width = abs(width[0] - width[1])
        self.area = self.abs_length * self.abs_width
        self.has_points = False
        self.points = []


class BinSpace:
    """Represents the region of space containing all the index points, and serves as a container for all the regions
    in the search grid, i.e., it holds all the data bins.
    """

    def __init__(self, width: tuple, length: tuple, points: list):
        self.length = length
        self.width = width
        self.abs_length = abs(length[0] - length[1])
        self.abs_width = abs(width[0] - width[1])
        self.area = self.abs_length * self.abs_width
        self.bin_map = {}
        self.bin_sizes = sizes
        self.points = points
        self.directions = {
            "N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1), "NE": (1, 1), "SE": (-1, 1),
            "SW": (-1, -1), "NW": (1, -1)
        }

    def make_bins(self):
        """Given the boundaries of all the points, creates non-overlapping bins for the search area."""
        for i, size in enumerate(self.bin_sizes):
            self.bin_map[size["coord"]] = Bin(uid=i, width=size["x"], length=size["y"], coord=size["coord"],
                                              x_min=size["x_min"], x_max=size["x_max"], y_min=size["y_min"],
                                              y_max=size["y_max"])

    def place_points(self):
        """Places all the index points into one or more bins based on which region or bin area they fall into."""
        for point in self.points:
            for k, v in self.bin_map.items():
                if (v.x_min <= round(point.x) <= v.x_max) and (v.y_min <= round(point.y) <= v.y_max):
                    v.points.append(point)
                    v.has_points = True
                    break

    def find_bin(self, point):
        """Locates the bin a given point falls into."""
        if (round(point.x), round(point.y)) == (0, 0):  # Origin edge case
            b = self.bin_map.get((5, 5))  # return bin next to origin
            if b:
                return b
            else:  # bin (5, 5) doesn't have point, return an empty bin
                return Bin(width=(0, 200), length=(0, 200), coord=(5, 5), x_min=0, x_max=200, y_min=0, y_max=200)

        for k, v in self.bin_map.items():
            if (v.x_min <= round(point.x) <= v.x_max) and (v.y_min <= round(point.y) <= v.y_max):
                return v

    def get_bins_with_points(self):
        """Returns a list of bins that contain points."""
        return [v for k, v in self.bin_map.items() if v.has_points]

    @staticmethod
    def find_nearest(query_point: Point, points: list) -> Point:
        """Finds the point closest to query_point, or returns None if no point is found.

        Uses standard Cartesian distance formula:
            d = sqrt((x2-x1)^2 + (y2-y1)^2)
        """
        if not type(query_point) == Point:
            raise TypeError(f"The query point must be of type Point not: {type(query_point)}")

        min_dist = None
        min_point = None

        for point in points:
            delta_x = point.x - query_point.x
            delta_y = point.y - query_point.y
            dist = math.sqrt(delta_x * delta_x + delta_y * delta_y)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point
        return min_point

    @staticmethod
    def get_total_points(to_search):
        """Returns a flat list of all the points contained in a list of data bins containing the query point and its
        adjacent squares."""
        total_points = []
        if to_search:
            for i in to_search:
                total_points.extend(i.points)
        return total_points

    def search_bins(self, home_bin, expand_factor):
        """Core of the search algorithm: Given the "home bin" of the query point, finds the adjacent squares
        surrounding the home bin. If the surrounding bins contain points, it appends them to a list to be searched.
        Finally, it returns a flat list of all the total points found in the interesting bins.
        """
        to_search = []
        if home_bin and home_bin.has_points:
            to_search.append(home_bin)
        home_coord = home_bin.coord

        for k, v in self.directions.items():
            coord = home_coord[0] + v[0] * expand_factor, home_coord[1] + v[1] * expand_factor
            next_bin = self.bin_map.get(coord)
            if next_bin and next_bin.has_points:
                to_search.append(next_bin)

        total_points = []
        if to_search:
            total_points = self.get_total_points(to_search)
        return total_points

    def search_nn(self, query_point):
        """Manages the search of the search space. The search stops when it finds points to measure, or it reaches
        the outer bounds of the search space.

        When there are points found in some square/bin surrounding the query point, it finds are returns the
        nearest point using the basic Cartesian distance formula.
        """
        home_bin = self.find_bin(query_point)
        total_points = []

        expand_factor = 1
        while not total_points and expand_factor < 10:
            total_points.extend(self.search_bins(home_bin, expand_factor))

            if total_points:
                return self.find_nearest(query_point, total_points)
            else:
                expand_factor += 1

    @staticmethod
    def get_rand_coordinates(pt_min: int = -1000, pt_max: int = 1000) -> tuple:
        """Returns a tuple of 2 random numbers for uses as a coordinate."""
        return random.uniform(pt_min, pt_max), random.uniform(pt_min, pt_max)

    @staticmethod
    def get_points(n_pts: int = 10) -> list:
        """Returns list of random coordinate tuples."""
        return [BinSpace.get_rand_coordinates() for _ in range(n_pts)]

    @staticmethod
    def get_point_objects(n_pts: int = 10) -> list:
        """Returns list of Point objects with random coordinates."""
        return [Point(*BinSpace.get_rand_coordinates()) for _ in range(n_pts)]


class MyNnIndex:
    """Implements a grid-like search space and an iteratively expanding search."""

    def __init__(self, points):
        self.points = points
        self.index = None
        self.upper_bound = 1001
        self.lower_bound = -1001
        self.dispatch = {
            "slow": self.find_nearest_slow,
            "fast": self.find_nn,
        }
        self.filled_bins = None
        self.make_index()

    def make_index(self):
        """Initializes the BinSpace data structure."""
        if not self.points:
            raise ValueError("Must have points to make the index.")
        self.index = BinSpace(length=(-1000, 1000), width=(-1000, 1000), points=self.points)
        self.index.make_bins()
        self.index.place_points()
        self.filled_bins = self.index.get_bins_with_points()

    def find_nearest_slow(self, query_point):
        """Finds the point closest to query_point, or returns None if no point is found.

        Uses standard Cartesian distance formula:
            d = sqrt((x2-x1)^2 + (y2-y1)^2)
        """
        if not type(query_point) == Point:
            raise TypeError(f"The query point must be of type Point not: {type(query_point)}")

        min_dist = None
        min_point = None

        for point in self.points:
            delta_x = point.x - query_point.x
            delta_y = point.y - query_point.y
            dist = math.sqrt(delta_x * delta_x + delta_y * delta_y)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point
        return min_point

    @staticmethod
    def distance(point: Point, query_point: Point):
        """Finds distance using standard Cartesian distance formula:
            d = sqrt((x2-x1)^2 + (y2-y1)^2)

        Args:
            point: (point): point (x, y)
            query_point (tuple): query point (x, y)
        Returns:
            dist (float):
        """
        if not type(query_point) == Point:
            raise TypeError(f"The query point must be of type Point not: {type(query_point)}")

        delta_x = point.x - query_point.x
        delta_y = point.y - query_point.y
        return math.sqrt(delta_x * delta_x + delta_y * delta_y)

    @staticmethod
    def nearest(query_point: Point, points):
        """Given a query point, and set of points, finds the nearest point to the query point in the set.
        Args:
            query_point (tuple): (x, y)
            points (list of tuples):

        Returns:
            min_point (tuple): (x, y)
        """
        if not type(query_point) == Point:
            raise TypeError(f"The query point must be of type Point not: {type(query_point)}")

        min_dist = None
        min_point = None
        for point in points:
            dist = MyNnIndex.distance(point, query_point)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point
        return min_point

    def find_nn(self, query_point: Point):
        """Insulates the code from change, creating a layer of abstraction between the find_nearest() and the actual
        implementation in self.index.search_nn(query_point).
        """
        if not type(query_point) == Point:
            raise TypeError(f"The query point must be of type Point not: {type(query_point)}")
        if not self.index:
            raise ValueError("Must have an index to find NN.")

        return self.index.search_nn(query_point)

    def find_nearest(self, query_point: Point):
        """Entry point for finding the nearest neighbor to the given point."""
        if not type(query_point) == Point:
            raise TypeError(f"The query point must be of type Point not: {type(query_point)}")
        if (query_point.x < self.lower_bound or query_point.x >= self.upper_bound) or (
                query_point.y < self.lower_bound or query_point.y >= self.upper_bound):
            raise ValueError(f"Query point out of bounds. max: {self.upper_bound} and min: {self.lower_bound}")

        return self.find_nn(query_point)
