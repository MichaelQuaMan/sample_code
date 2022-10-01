# (x, y) convention
# Where x is horizontal, y is vertical
# Starting point is bottom left, which is (0,0)
# bottom right quadrant is index (0,0)
# move from min to max in each quad (low to high)
sizes = [{
    "x": (-1000, -800),
    "y": (-1000, -800),
    "coord": (0, 0),
    "x_min": -1000,
    "x_max": -800,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (-800, -600),
    "y": (-1000, -800),
    "coord": (1, 0),
    "x_min": -800,
    "x_max": -600,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (-600, -400),
    "y": (-1000, -800),
    "coord": (2, 0),
    "x_min": -600,
    "x_max": -400,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (-400, -200),
    "y": (-1000, -800),
    "coord": (3, 0),
    "x_min": -400,
    "x_max": -200,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (-200, 0),
    "y": (-1000, -800),
    "coord": (4, 0),
    "x_min": -200,
    "x_max": 0,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (-1000, -800),
    "y": (-800, -600),
    "coord": (0, 1),
    "x_min": -1000,
    "x_max": -800,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (-800, -600),
    "y": (-800, -600),
    "coord": (1, 1),
    "x_min": -800,
    "x_max": -600,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (-600, -400),
    "y": (-800, -600),
    "coord": (2, 1),
    "x_min": -600,
    "x_max": -400,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (-400, -200),
    "y": (-800, -600),
    "coord": (3, 1),
    "x_min": -400,
    "x_max": -200,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (-200, 0),
    "y": (-800, -600),
    "coord": (4, 1),
    "x_min": -200,
    "x_max": 0,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (-1000, -800),
    "y": (-600, -400),
    "coord": (0, 2),
    "x_min": -1000,
    "x_max": -800,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (-800, -600),
    "y": (-600, -400),
    "coord": (1, 2),
    "x_min": -800,
    "x_max": -600,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (-600, -400),
    "y": (-600, -400),
    "coord": (2, 2),
    "x_min": -600,
    "x_max": -400,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (-400, -200),
    "y": (-600, -400),
    "coord": (3, 2),
    "x_min": -400,
    "x_max": -200,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (-200, 0),
    "y": (-600, -400),
    "coord": (4, 2),
    "x_min": -200,
    "x_max": 0,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (-1000, -800),
    "y": (-400, -200),
    "coord": (0, 3),
    "x_min": -1000,
    "x_max": -800,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (-800, -600),
    "y": (-400, -200),
    "coord": (1, 3),
    "x_min": -800,
    "x_max": -600,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (-600, -400),
    "y": (-400, -200),
    "coord": (2, 3),
    "x_min": -600,
    "x_max": -400,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (-400, -200),
    "y": (-400, -200),
    "coord": (3, 3),
    "x_min": -400,
    "x_max": -200,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (-200, 0),
    "y": (-400, -200),
    "coord": (4, 3),
    "x_min": -200,
    "x_max": 0,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (-1000, -800),
    "y": (-200, 0),
    "coord": (0, 4),
    "x_min": -1000,
    "x_max": -800,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (-800, -600),
    "y": (-200, 0),
    "coord": (1, 4),
    "x_min": -800,
    "x_max": -600,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (-600, -400),
    "y": (-200, 0),
    "coord": (2, 4),
    "x_min": -600,
    "x_max": -400,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (-400, -200),
    "y": (-200, 0),
    "coord": (3, 4),
    "x_min": -400,
    "x_max": -200,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (-200, 0),
    "y": (-200, 0),
    "coord": (4, 4),
    "x_min": -200,
    "x_max": 0,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (-1000, -800),
    "y": (800, 1000),
    "coord": (0, 9),
    "x_min": -1000,
    "x_max": -800,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (-800, -600),
    "y": (800, 1000),
    "coord": (1, 9),
    "x_min": -800,
    "x_max": -600,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (-600, -400),
    "y": (800, 1000),
    "coord": (2, 9),
    "x_min": -600,
    "x_max": -400,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (-400, -200),
    "y": (800, 1000),
    "coord": (3, 9),
    "x_min": -400,
    "x_max": -200,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (-200, 0),
    "y": (800, 1000),
    "coord": (4, 9),
    "x_min": -200,
    "x_max": 0,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (-1000, -800),
    "y": (600, 800),
    "coord": (0, 8),
    "x_min": -1000,
    "x_max": -800,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (-800, -600),
    "y": (600, 800),
    "coord": (1, 8),
    "x_min": -800,
    "x_max": -600,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (-600, -400),
    "y": (600, 800),
    "coord": (2, 8),
    "x_min": -600,
    "x_max": -400,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (-400, -200),
    "y": (600, 800),
    "coord": (3, 8),
    "x_min": -400,
    "x_max": -200,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (-200, 0),
    "y": (600, 800),
    "coord": (4, 8),
    "x_min": -200,
    "x_max": 0,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (-1000, -800),
    "y": (400, 600),
    "coord": (0, 7),
    "x_min": -1000,
    "x_max": -800,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (-800, -600),
    "y": (400, 600),
    "coord": (1, 7),
    "x_min": -800,
    "x_max": -600,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (-600, -400),
    "y": (400, 600),
    "coord": (2, 7),
    "x_min": -600,
    "x_max": -400,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (-400, -200),
    "y": (400, 600),
    "coord": (3, 7),
    "x_min": -400,
    "x_max": -200,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (-200, 0),
    "y": (400, 600),
    "coord": (4, 7),
    "x_min": -200,
    "x_max": 0,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (-1000, -800),
    "y": (200, 400),
    "coord": (0, 6),
    "x_min": -1000,
    "x_max": -800,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (-800, -600),
    "y": (200, 400),
    "coord": (1, 6),
    "x_min": -800,
    "x_max": -600,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (-600, -400),
    "y": (200, 400),
    "coord": (2, 6),
    "x_min": -600,
    "x_max": -400,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (-400, -200),
    "y": (200, 400),
    "coord": (3, 6),
    "x_min": -400,
    "x_max": -200,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (-200, 0),
    "y": (200, 400),
    "coord": (4, 6),
    "x_min": -200,
    "x_max": 0,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (-1000, -800),
    "y": (0, 200),
    "coord": (0, 5),
    "x_min": -1000,
    "x_max": -800,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (-800, -600),
    "y": (0, 200),
    "coord": (1, 5),
    "x_min": -800,
    "x_max": -600,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (-600, -400),
    "y": (0, 200),
    "coord": (2, 5),
    "x_min": -600,
    "x_max": -400,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (-400, -200),
    "y": (0, 200),
    "coord": (3, 5),
    "x_min": -400,
    "x_max": -200,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (-200, 0),
    "y": (0, 200),
    "coord": (4, 5),
    "x_min": -200,
    "x_max": 0,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (800, 1000),
    "y": (-1000, -800),
    "coord": (9, 0),
    "x_min": 800,
    "x_max": 1000,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (600, 800),
    "y": (-1000, -800),
    "coord": (8, 0),
    "x_min": 600,
    "x_max": 800,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (400, 600),
    "y": (-1000, -800),
    "coord": (7, 0),
    "x_min": 400,
    "x_max": 600,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (200, 400),
    "y": (-1000, -800),
    "coord": (6, 0),
    "x_min": 200,
    "x_max": 400,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (0, 200),
    "y": (-1000, -800),
    "coord": (5, 0),
    "x_min": 0,
    "x_max": 200,
    "y_min": -1000,
    "y_max": -800
}, {
    "x": (800, 1000),
    "y": (-800, -600),
    "coord": (9, 1),
    "x_min": 800,
    "x_max": 1000,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (600, 800),
    "y": (-800, -600),
    "coord": (8, 1),
    "x_min": 600,
    "x_max": 800,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (400, 600),
    "y": (-800, -600),
    "coord": (7, 1),
    "x_min": 400,
    "x_max": 600,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (200, 400),
    "y": (-800, -600),
    "coord": (6, 1),
    "x_min": 200,
    "x_max": 400,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (0, 200),
    "y": (-800, -600),
    "coord": (5, 1),
    "x_min": 0,
    "x_max": 200,
    "y_min": -800,
    "y_max": -600
}, {
    "x": (800, 1000),
    "y": (-600, -400),
    "coord": (9, 2),
    "x_min": 800,
    "x_max": 1000,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (600, 800),
    "y": (-600, -400),
    "coord": (8, 2),
    "x_min": 600,
    "x_max": 800,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (400, 600),
    "y": (-600, -400),
    "coord": (7, 2),
    "x_min": 400,
    "x_max": 600,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (200, 400),
    "y": (-600, -400),
    "coord": (6, 2),
    "x_min": 200,
    "x_max": 400,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (0, 200),
    "y": (-600, -400),
    "coord": (5, 2),
    "x_min": 0,
    "x_max": 200,
    "y_min": -600,
    "y_max": -400
}, {
    "x": (800, 1000),
    "y": (-400, -200),
    "coord": (9, 3),
    "x_min": 800,
    "x_max": 1000,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (600, 800),
    "y": (-400, -200),
    "coord": (8, 3),
    "x_min": 600,
    "x_max": 800,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (400, 600),
    "y": (-400, -200),
    "coord": (7, 3),
    "x_min": 400,
    "x_max": 600,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (200, 400),
    "y": (-400, -200),
    "coord": (6, 3),
    "x_min": 200,
    "x_max": 400,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (0, 200),
    "y": (-400, -200),
    "coord": (5, 3),
    "x_min": 0,
    "x_max": 200,
    "y_min": -400,
    "y_max": -200
}, {
    "x": (800, 1000),
    "y": (-200, 0),
    "coord": (9, 4),
    "x_min": 800,
    "x_max": 1000,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (600, 800),
    "y": (-200, 0),
    "coord": (8, 4),
    "x_min": 600,
    "x_max": 800,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (400, 600),
    "y": (-200, 0),
    "coord": (7, 4),
    "x_min": 400,
    "x_max": 600,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (200, 400),
    "y": (-200, 0),
    "coord": (6, 4),
    "x_min": 200,
    "x_max": 400,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (0, 200),
    "y": (-200, 0),
    "coord": (5, 4),
    "x_min": 0,
    "x_max": 200,
    "y_min": -200,
    "y_max": 0
}, {
    "x": (800, 1000),
    "y": (800, 1000),
    "coord": (9, 9),
    "x_min": 800,
    "x_max": 1000,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (600, 800),
    "y": (800, 1000),
    "coord": (8, 9),
    "x_min": 600,
    "x_max": 800,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (400, 600),
    "y": (800, 1000),
    "coord": (7, 9),
    "x_min": 400,
    "x_max": 600,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (200, 400),
    "y": (800, 1000),
    "coord": (6, 9),
    "x_min": 200,
    "x_max": 400,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (0, 200),
    "y": (800, 1000),
    "coord": (5, 9),
    "x_min": 0,
    "x_max": 200,
    "y_min": 800,
    "y_max": 1000
}, {
    "x": (800, 1000),
    "y": (600, 800),
    "coord": (9, 8),
    "x_min": 800,
    "x_max": 1000,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (600, 800),
    "y": (600, 800),
    "coord": (8, 8),
    "x_min": 600,
    "x_max": 800,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (400, 600),
    "y": (600, 800),
    "coord": (7, 8),
    "x_min": 400,
    "x_max": 600,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (200, 400),
    "y": (600, 800),
    "coord": (6, 8),
    "x_min": 200,
    "x_max": 400,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (0, 200),
    "y": (600, 800),
    "coord": (5, 8),
    "x_min": 0,
    "x_max": 200,
    "y_min": 600,
    "y_max": 800
}, {
    "x": (800, 1000),
    "y": (400, 600),
    "coord": (9, 7),
    "x_min": 800,
    "x_max": 1000,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (600, 800),
    "y": (400, 600),
    "coord": (8, 7),
    "x_min": 600,
    "x_max": 800,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (400, 600),
    "y": (400, 600),
    "coord": (7, 7),
    "x_min": 400,
    "x_max": 600,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (200, 400),
    "y": (400, 600),
    "coord": (6, 7),
    "x_min": 200,
    "x_max": 400,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (0, 200),
    "y": (400, 600),
    "coord": (5, 7),
    "x_min": 0,
    "x_max": 200,
    "y_min": 400,
    "y_max": 600
}, {
    "x": (800, 1000),
    "y": (200, 400),
    "coord": (9, 6),
    "x_min": 800,
    "x_max": 1000,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (600, 800),
    "y": (200, 400),
    "coord": (8, 6),
    "x_min": 600,
    "x_max": 800,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (400, 600),
    "y": (200, 400),
    "coord": (7, 6),
    "x_min": 400,
    "x_max": 600,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (200, 400),
    "y": (200, 400),
    "coord": (6, 6),
    "x_min": 200,
    "x_max": 400,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (0, 200),
    "y": (200, 400),
    "coord": (5, 6),
    "x_min": 0,
    "x_max": 200,
    "y_min": 200,
    "y_max": 400
}, {
    "x": (800, 1000),
    "y": (0, 200),
    "coord": (9, 5),
    "x_min": 800,
    "x_max": 1000,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (600, 800),
    "y": (0, 200),
    "coord": (8, 5),
    "x_min": 600,
    "x_max": 800,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (400, 600),
    "y": (0, 200),
    "coord": (7, 5),
    "x_min": 400,
    "x_max": 600,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (200, 400),
    "y": (0, 200),
    "coord": (6, 5),
    "x_min": 200,
    "x_max": 400,
    "y_min": 0,
    "y_max": 200
}, {
    "x": (0, 200),
    "y": (0, 200),
    "coord": (5, 5),
    "x_min": 0,
    "x_max": 200,
    "y_min": 0,
    "y_max": 200
}]