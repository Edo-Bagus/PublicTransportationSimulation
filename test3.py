from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# SOUTH, EAST, NORTH, WEST


# sim.create_quadratic_bezier_curve((0, -95), (0, -80), (0, -70))

# jalan menuju lingkaran
# sim.create_segment((-1, -100), (-1, -50))
# sim.create_segment((1, -50), (1, -100))
# 
# Lingkaran tengah -> jalan satu arah
# sim.create_quadratic_bezier_curve((0, -50), (-50, -50), (-50, 0))
# sim.create_quadratic_bezier_curve((-50, 0), (-50, 50), (0, 50))
# sim.create_quadratic_bezier_curve((0, 50), (50, 50), (50, 0))
# sim.create_quadratic_bezier_curve((50, 0), (50, -50), (0, -50))
# 
# Jalur keluar lingkaran -> kanan
# sim.create_segment((50, -1), (100, -1))
# sim.create_segment((100, 1), (50, 1))
# 
# sim.create_segment((-99, -100), (-99, 0))
# sim.create_segment((-101, 0), (-101, -100))
# 
# Jalan keluar lingkaran -> kiri
# sim.create_segment((-100, -1), (-50, -1))
# sim.create_segment((-50, 1), (-100, 1))
# 
# sim.create_segment((-99, 0), (-99, 50))
# sim.create_segment((-101, 50), (-101, 0))
# 
# sim.create_segment((-50, 101), (0, 101))
# sim.create_segment((0, 99), (-50, 99))
# 
# Jalan keluar lingkaran -> bawah
# sim.create_segment((1, 100), (1, 50))
# sim.create_segment((-1, 50), (-1, 100))

# sim.create_segment((0, -100), (100, 0))
# sim.create_segment((0, -100), (100, 0))

# sim.create_segment((0, 101), (100, 101))
# sim.create_segment((100, 99), (0, 99))
# 
# sim.create_segment((99, 100), (99, 0))
# sim.create_segment((101, 0), (101, 100))

# belah ketupat
sim.create_segment((-95, 60), (-60, 95))
sim.create_quadratic_bezier_curve((-60, 95), (-55, 100), (-60, 105))
sim.create_segment((-60, 105), (-95, 140))
sim.create_quadratic_bezier_curve((-95, 140), (-100, 145), (-105, 140))
sim.create_segment((-105, 140), (-140, 105))
sim.create_quadratic_bezier_curve((-140, 105), (-145, 100), (-140, 95))
sim.create_segment((-140, 95), (-105, 60))
sim.create_quadratic_bezier_curve((-105, 60), (-100, 55), (-95, 60))

sim.create_segment((-90, 145), (-55, 110))
sim.create_quadratic_bezier_curve((-55, 110), (-45, 100), (-55, 90))
sim.create_segment((-55, 90), (-90, 55))
sim.create_quadratic_bezier_curve((-90, 55), (-100, 45), (-110, 55))
sim.create_segment ((-110, 55), (-145, 90) )
sim.create_quadratic_bezier_curve((-145, 90), (-155, 100), (-145, 110))
sim.create_segment((-145, 110), (-110, 145))
sim.create_quadratic_bezier_curve((-110, 145),(-100, 155), (-90, 145))







# percobaan
# sim.create_segment((0, -99), (-165, -99))
# sim.create_segment((-165, -101), (0, -101))
# sim.create_segment((-165, -99), (-185, -99))

sim.create_quadratic_bezier_curve((-185, -101),(-174, -101),(-174, -90))

sim.create_segment((-185, -99), (-240, -99))
sim.create_segment((-240, -101), (-185, -101))
# sim.create_segment((-185, -101), (-165, -101))

# sim.create_quadratic_bezier_curve((-165, -99), (-176, -99), (-174, -90))

sim.create_segment((-174, -90), (-174, -10))
sim.create_segment((-176, -10), (-176, -90))

# sim.create_quadratic_bezier_curve((-176, -90), (-176, -101), (-165, -101))
sim.create_quadratic_bezier_curve((-176, -90), (-176, -99), (-185, -99))

# ---------

#Jalan pojok kiri
sim.create_segment((-249, -90), (-249, -10))
sim.create_segment((-251, -10), (-251, -90))

#24
sim.create_quadratic_bezier_curve((-240, -99), (-249, -99), (-249, -90))
sim.create_quadratic_bezier_curve((-251, -90), (-251, -101), (-240, -101))

#-----------

sim.create_segment((-240, -1), (-185, -1))
sim.create_segment((-185, 1), (-240, 1))

sim.create_segment((-165, -1), (-110, -1))
sim.create_segment((-110, 1), (-165, 1))

sim.create_segment((-249, 10), (-249, 90))
sim.create_segment((-251, 90), (-251, 10))

sim.create_quadratic_bezier_curve((-249, 90), (-249, 99), (-240, 99))
sim.create_quadratic_bezier_curve((-240, 101), (-251, 101), (-251, 90))

sim.create_quadratic_bezier_curve((-185, -1), (-176, -1), (-176, -10))
#35
sim.create_quadratic_bezier_curve((-174, -10), (-174, 1), (-185, 1))
sim.create_quadratic_bezier_curve((-174, -10), (-174, -1), (-165, -1))
sim.create_quadratic_bezier_curve((-165, 1), (-176, 1), (-176, -10))
sim.create_segment((-185, -1), (-165, -1))
sim. create_segment((-165, 1), (-185, 1))

#Pertigaan kiri
#40
sim.create_quadratic_bezier_curve((-249, -10), (-249, -1), (-240, -1))
sim.create_quadratic_bezier_curve((-240, 1), (-249, 1), (-249, 10))
sim.create_quadratic_bezier_curve((-240, 1), (-251, 1), (-251, -10))
sim.create_quadratic_bezier_curve((-251, 10), (-251, -1), (-240, -1))
sim.create_segment((-251, 10), (-251, -10))
sim.create_segment((-249, -10), (-249, 10))

sim.create_quadratic_bezier_curve((-110, -1), (-99, -1), (-99, 10))
sim. create_quadratic_bezier_curve((-101, 10), (-101, 1), (-110, 1))

sim.create_segment((-99, 10), (-99, 40))
sim.create_segment((-101, 40), (-101, 10))

sim.create_segment((-240, 99), (-160, 99))
sim.create_segment((-160, 101), (-240, 101))

#52
sim.create_quadratic_bezier_curve((-160, 99), (-150, 99), (-140, 95))
sim.create_quadratic_bezier_curve((-160, 99), (-150, 99), (-145, 110))
sim.create_quadratic_bezier_curve((-145, 90), (-150, 101), (-160, 101))
#55
sim.create_quadratic_bezier_curve((-140, 105), (-150, 101), (-160, 101))

sim.create_quadratic_bezier_curve((-99, 40), (-99, 50), (-95, 60))
sim.create_quadratic_bezier_curve((-99, 40), (-99, 50), (-110, 55))

sim.create_quadratic_bezier_curve((-105, 60), (-101, 50), (-101, 40))
sim.create_quadratic_bezier_curve((-90, 55), (-101, 50), (-101, 40))

#60
sim.create_segment((-260, 101), (-300, 101))
sim.create_segment((-300, 99), (-260, 99))
sim.create_quadratic_bezier_curve((-260, 99), (-251, 99), (-251, 90))
sim.create_segment((-240, 101), (-260, 101))
sim.create_segment((-260, 99), (-240, 99))

#65
sim.create_quadratic_bezier_curve((-249, 90), (-249, 101), (-260, 101))
sim.create_segment((-270, -101), (-240, -101))

# sim.create_segment((-250, 100), (-250, 200))
# sim.create_segment((-250, 100), (-250, 200))
# 
# sim.create_segment((-250, 200), (100, 200))
# sim.create_segment((-250, 200), (100, 200))
# 
# sim.create_segment((100, 200), (100, 100))
# sim.create_segment((100, 200), (100, 100))

# sim.create_segment((-100, 150), (-100, 200))
# sim.create_segment((-100, 150), (-100, 200))

sim.create_segment((-165, -101), (-110, -101))
sim.create_segment((-110, -99), (-165, -99))

sim.create_quadratic_bezier_curve((-176, -90), (-176, -101), (-165, -101))
sim.create_quadratic_bezier_curve((-165, -99), (-174, -99), (-174, -90))

#71
sim.create_segment((-165, -99), (-185, -99))
sim.create_segment((-185, -101), (-165, -101))

sim.create_quadratic_bezier_curve((-110, -101), (-99, -101), (-99, -90))
sim.create_quadratic_bezier_curve((-101, -90), (-101, -99), (-110, -99))

sim.create_segment((-99,-90), (-99, -10))
sim.create_segment((-101, -10), (-101, -90))

sim.create_segment((-90, -1), (-10, -1))
sim.create_segment((-10, 1), (-90, 1))

sim.create_segment((-99, -10), (-99, 10))
sim.create_segment((-101, 10), (-101, -10))

#81
sim.create_quadratic_bezier_curve((-99, -10), (-99, -1), (-90, -1))
sim.create_quadratic_bezier_curve((-99, -10), (-99, 1), (-110, 1))

sim.create_quadratic_bezier_curve((-90, 1), (-99, 1), (-99, 10))
sim.create_quadratic_bezier_curve((-90, 1), (-101, 1), (-101, -10))

sim.create_segment((-110, -1), (-90, -1))
sim.create_segment((-90, 1), (-110, 1))

sim.create_quadratic_bezier_curve((-110, -1), (-101, -1), (-101, -10))
sim.create_quadratic_bezier_curve((-101, 10), (-101, -1), (-90, -1))

sim.create_quadratic_bezier_curve((-10, -1), (1, -1), (1, 10))
sim.create_quadratic_bezier_curve((-1, 10), (-1, 1), (-10, 1))

#91
sim.create_segment((1, 10), (1, 90))
sim.create_segment((-1, 90), (-1, 10))

sim.create_quadratic_bezier_curve((1, 90), (1, 101), (-10, 101))
sim.create_quadratic_bezier_curve((-10, 99), (-1, 99), (-1, 90))

sim.create_segment((-10, 101), (-40, 101))
sim.create_segment((-40, 99), (-10, 99))

sim.create_quadratic_bezier_curve((-40, 101), (-50, 101), (-55, 90))
sim.create_quadratic_bezier_curve((-40, 101), (-50, 101), (-60, 105))

sim.create_quadratic_bezier_curve((-55, 110), (-50, 99), (-40, 99))
sim.create_quadratic_bezier_curve((-60, 95), (-50, 99), (-40, 99))

sim.connect_segment(0, [1, 100])
sim.connect_segment(1, [2])
sim.connect_segment(2, [3])
sim.connect_segment(3, [4])
sim.connect_segment(4, [5, 55])
sim.connect_segment(5, [6])
sim.connect_segment(6, [7, 58])
sim.connect_segment(7, [0])

sim.connect_segment(8, [9, 99])
sim.connect_segment(9, [10])
sim.connect_segment(10, [11, 59])
sim.connect_segment(11, [12])
sim.connect_segment(12, [13, 54])
sim.connect_segment(13, [14])
sim.connect_segment(14, [15])
sim.connect_segment(15, [8])
sim.connect_segment(16, [19])
sim.connect_segment(17, [24])
sim.connect_segment(18, [16, 72])
sim.connect_segment(19, [35, 36])
sim.connect_segment(20, [21, 69])
sim.connect_segment(21, [17])
sim.connect_segment(22, [40, 45])
sim.connect_segment(23, [25])
sim.connect_segment(24, [22])
sim.connect_segment(25, [18])
sim.connect_segment(26, [34, 38])
sim.connect_segment(27, [41, 42])
sim.connect_segment(28, [46, 85, 87])
sim.connect_segment(29, [37, 39])
sim.connect_segment(30, [32, 65])
sim.connect_segment(31, [43, 44])
sim.connect_segment(32, [50])
sim.connect_segment(33, [31])
sim.connect_segment(34, [20])
sim.connect_segment(35, [27])
sim.connect_segment(36, [28])
sim.connect_segment(37, [20])
sim.connect_segment(38, [28])
sim.connect_segment(39, [27])
sim.connect_segment(40, [26])
sim.connect_segment(41, [30])
sim.connect_segment(42, [23])
sim.connect_segment(43, [26])
sim.connect_segment(44, [23])
sim.connect_segment(45, [30])
sim.connect_segment(46, [48])
sim.connect_segment(47, [29])
sim.connect_segment(48, [56, 57])
sim.connect_segment(49, [47, 80, 88])
sim.connect_segment(50, [52, 53])
sim.connect_segment(51, [33, 63])
sim.connect_segment(52, [6])
sim.connect_segment(53, [14])
sim.connect_segment(54, [51])
sim.connect_segment(55, [51])
sim.connect_segment(56, [0])
sim.connect_segment(57, [12])
sim.connect_segment(58, [49])
sim.connect_segment(59, [49])
sim.connect_segment(61, [62, 64])
sim.connect_segment(62, [31])
sim.connect_segment(63, [60])
sim.connect_segment(64, [50])
sim.connect_segment(65, [60])
sim.connect_segment(66, [18])
sim.connect_segment(67, [73])
sim.connect_segment(68, [70, 71])
sim.connect_segment(69, [67])
sim.connect_segment(70, [19])
sim.connect_segment(71, [17])
sim.connect_segment(72, [67])
sim.connect_segment(73, [75])
sim.connect_segment(74, [68])
sim.connect_segment(75, [79, 81, 82])
sim.connect_segment(76, [74])
sim.connect_segment(77, [89])
sim.connect_segment(78, [83, 84, 86])
sim.connect_segment(79, [48])
sim.connect_segment(80, [76])
sim.connect_segment(81, [77])
sim.connect_segment(82, [29])
sim.connect_segment(83, [48])
sim.connect_segment(84, [76])
sim.connect_segment(85, [77])
sim.connect_segment(86, [29])
sim.connect_segment(87, [76])
sim.connect_segment(88, [77])
sim.connect_segment(89, [91])
sim.connect_segment(90, [78])
sim.connect_segment(91, [93])
sim.connect_segment(92, [90])
sim.connect_segment(93, [95])
sim.connect_segment(94, [92])
sim.connect_segment(95, [97, 98])
sim.connect_segment(96, [94])
sim.connect_segment(97, [10])
sim.connect_segment(98, [2])
sim.connect_segment(99, [96])
sim.connect_segment(100, [96])

vehicle = Vehicle({'path': [0]}) 
sim.add_vehicle(vehicle)
win = Window(sim)
win.run()
win.show()