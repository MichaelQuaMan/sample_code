import logging
import math

import kdtree

log = logging.getLogger(__name__)


class NearestNeighborIndex:
    """Indexes a set of given points to provide fast nearest neighbor lookup."""

    def __init__(self, points):
        """Takes an array of 2d tuples as input points to be indexed."""
        self.points = points
        self.dist_index = []
        self.tree = None
        self.make_kdtree_index()
        self.dispatch = {
            "slow": self.find_nearest_slow,
            "fastest": self.find_nn_fastest,
        }

    def make_kdtree_index(self):
        """Uses 3rd party K-d tree lib data structure for fastest benchmark.
        Found: https://github.com/stefankoegl/kdtree
        """
        self.tree = kdtree.create(self.points)

    def find_nearest_slow(self, query_point):
        """Finds the point closest to query_point, or returns None if no point is found."""
        min_dist = None
        min_point = None

        for point in self.points:
            delta_x = point[0] - query_point[0]
            delta_y = point[1] - query_point[1]
            dist = math.sqrt(delta_x * delta_x + delta_y * delta_y)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point
        return min_point

    def find_nn_fastest(self, query_point):
        """Uses 3rd party kdtree lib for fast benchmark.
        Found: https://github.com/stefankoegl/kdtree
        """
        return self.tree.search_nn(query_point)

    def find_nearest(self, query_point, mode="slow"):
        """Finds the nearest neighbor to the given point."""
        func = self.dispatch.get(mode)
        return func(query_point)
