# Please create a simple example using pynn library.
#
# Assume that the end user knows their subject but has only a basic understanding of Python.
#
# Meaningful examples may include reading a file, finding a few nearby points and writing them
# out to the console.
from my_nn.nn import BinSpace, MyNnIndex


def main():
    points = BinSpace.get_point_objects(n_pts=10)
    nn_index = MyNnIndex(points)
    nn_index.make_index()


if __name__ == "__main__":
    main()
