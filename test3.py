from trafficSimulator import *

sim = Simulation()

# belah ketupat
sim.create_segment((-95, 110), (-10, 145))
sim.create_quadratic_bezier_curve((-10, 145), (-5, 150), (-10, 155))
sim.create_segment((-10, 155), (-95, 240))
sim.create_quadratic_bezier_curve((-95, 240), (-100, 245), (-105, 240))
sim.create_segment((-105, 240), (-190, 155))
sim.create_quadratic_bezier_curve((-190, 155), (-195, 150), (-190, 145))
sim.create_segment((-190, 145), (-105, 110))
sim.create_quadratic_bezier_curve((-105, 110), (-100, 105), (-95, 110))

sim.create_segment((-90, 245), (-5, 160))
sim.create_quadratic_bezier_curve((-5, 160), (5, 150), (-5, 140))
sim.create_segment((-5, 140), (-90, 105))
sim.create_quadratic_bezier_curve((-90, 105), (-100, 100), (-110, 105))
sim.create_segment ((-110, 105), (-195, 140) )
sim.create_quadratic_bezier_curve((-195, 140), (-205, 150), (-195, 160))
sim.create_segment((-195, 160), (-110, 245))
sim.create_quadratic_bezier_curve((-110, 245),(-100, 255), (-90, 245))


sim.create_quadratic_bezier_curve((-285, -151),(-274, -151),(-274, -140))

sim.create_segment((-285, -149), (-440, -149))
sim.create_segment((-440, -151), (-285, -151))
# sim.create_segment((-285, -101), (-265, -101))

# sim.create_quadratic_bezier_curve((-265, -99), (-276, -99), (-274, -90))

sim.create_segment((-274, -140), (-274, -10))
sim.create_segment((-276, -10), (-276, -140))

# sim.create_quadratic_bezier_curve((-276, -90), (-276, -101), (-265, -101))
sim.create_quadratic_bezier_curve((-276, -140), (-276, -149), (-285, -149))

# ---------

#Jalan pojok kiri
sim.create_segment((-449, -140), (-449, -60))
sim.create_segment((-451, -60), (-451, -140))

#24
sim.create_quadratic_bezier_curve((-440, -149), (-449, -149), (-449, -140))
sim.create_quadratic_bezier_curve((-451, -140), (-451, -151), (-440, -151))

#-----------

sim.create_segment((-440, -51), (-285, -51))
sim.create_segment((-285, -49), (-440, -49))

sim.create_segment((-265, -1), (-110, -1))
sim.create_segment((-110, 1), (-265, 1))

sim.create_segment((-449, 10), (-449, 140))
sim.create_segment((-451, 140), (-451, 10))

sim.create_quadratic_bezier_curve((-449, 140), (-449, 149), (-440, 149))
sim.create_quadratic_bezier_curve((-440, 151), (-451, 151), (-451, 140))

sim.create_quadratic_bezier_curve((-285, -1), (-276, -1), (-276, -10))
#35
sim.create_quadratic_bezier_curve((-274, -10), (-274, 1), (-285, 1))
sim.create_quadratic_bezier_curve((-274, -10), (-274, -1), (-265, -1))
sim.create_quadratic_bezier_curve((-265, 1), (-276, 1), (-276, -10))
sim.create_segment((-285, -1), (-265, -1))
sim. create_segment((-265, 1), (-285, 1))

#Pertigaan kiri
#40
sim.create_quadratic_bezier_curve((-449, -50), (-449, -51), (-440, -51))
sim.create_quadratic_bezier_curve((-440, -49), (-449, -49), (-449, -40))
sim.create_quadratic_bezier_curve((-440, -49), (-451, -49), (-451, -60))
sim.create_quadratic_bezier_curve((-451, -40), (-451, -51), (-440, -51))
sim.create_segment((-451, -40), (-451, -60))
sim.create_segment((-449, -60), (-449, -40))

sim.create_quadratic_bezier_curve((-110, -1), (-99, -1), (-99, 10))
sim. create_quadratic_bezier_curve((-101, 10), (-101, 1), (-110, 1))

sim.create_segment((-99, 10), (-99, 90))
sim.create_segment((-101, 90), (-101, 10))

sim.create_segment((-440, 149), (-210, 149))
sim.create_segment((-210, 151), (-440, 151))

#52
sim.create_quadratic_bezier_curve((-210, 149), (-200, 149), (-190, 145))
sim.create_quadratic_bezier_curve((-210, 149), (-200, 149), (-195, 160))
sim.create_quadratic_bezier_curve((-195, 140), (-200, 151), (-210, 151))
#55
sim.create_quadratic_bezier_curve((-190, 155), (-200, 151), (-210, 151))

sim.create_quadratic_bezier_curve((-99, 90), (-99, 100), (-95, 110))
sim.create_quadratic_bezier_curve((-99, 90), (-99, 100), (-110, 105))

sim.create_quadratic_bezier_curve((-105, 110), (-101, 100), (-101, 90))
sim.create_quadratic_bezier_curve((-90, 105), (-101, 100), (-101, 90))

#60
sim.create_segment((-460, 151), (-500, 151))
sim.create_segment((-500, 149), (-460, 149))
sim.create_quadratic_bezier_curve((-460, 149), (-451, 149), (-451, 150))
sim.create_segment((-440, 151), (-460, 151))
sim.create_segment((-460, 149), (-440, 149))

#65
sim.create_quadratic_bezier_curve((-449, 140), (-449, 151), (-460, 151))
sim.create_segment((-470, -151), (-440, -151))

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

sim.create_segment((-265, -151), (-110, -151))
sim.create_segment((-110, -149), (-265, -149))

sim.create_quadratic_bezier_curve((-276, -140), (-276, -151), (-265, -151))
sim.create_quadratic_bezier_curve((-265, -149), (-274, -149), (-274, -140))

#71
sim.create_segment((-265, -149), (-285, -149))
sim.create_segment((-285, -151), (-265, -151))

sim.create_quadratic_bezier_curve((-110, -151), (-99, -151), (-99, -140))
sim.create_quadratic_bezier_curve((-101, -140), (-101, -149), (-110, -149))

sim.create_segment((-99, -140), (-99, -10))
sim.create_segment((-101, -10), (-101, -140))

sim.create_segment((-90, -1), (90, -1))
sim.create_segment((90, 1), (-90, 1))

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

sim.create_quadratic_bezier_curve((90, -1), (101, -1), (101, 10))
sim.create_quadratic_bezier_curve((99, 10), (99, 1), (90, 1))

#91
sim.create_segment((101, 10), (101, 140))
sim.create_segment((99, 140), (99, 10))

sim.create_quadratic_bezier_curve((101, 140), (101, 151), (90, 151))
sim.create_quadratic_bezier_curve((90, 149), (99, 149), (99, 140))

sim.create_segment((90, 151), (10, 151))
sim.create_segment((10, 149), (90, 149))

sim.create_quadratic_bezier_curve((10, 151), (0, 151), (-5, 140))
sim.create_quadratic_bezier_curve((10, 151), (0, 151), (-10, 155))

sim.create_quadratic_bezier_curve((-5, 160), (0, 149), (10, 149))
sim.create_quadratic_bezier_curve((-10, 145), (0, 149), (10, 149))

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
sim.connect_segment(30, [32])
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
sim.connect_segment(51, [33])
sim.connect_segment(52, [6])
sim.connect_segment(53, [14])
sim.connect_segment(54, [51])
sim.connect_segment(55, [51])
sim.connect_segment(56, [0])
sim.connect_segment(57, [12])
sim.connect_segment(58, [49])
sim.connect_segment(59, [49])
sim.connect_segment(60, [66])
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

sim.create_signal([[22], [27], [31]])
sim.create_signal([[18], [68], [20]])
sim.create_signal([[26], [19], [29]])
sim.create_signal([[50], [12], [4]])
sim.create_signal([[10], [6], [48]])
sim.create_signal([[0], [8], [95]])
sim.create_signal([[28], [75], [78], [49]])   

# vehicle = Vehicle({'path': [0]}) 
sim.set_spawnable_segments([17, 18, 67, 68, 75, 76, 20, 19, 23, 22, 31, 30, 50, 51, 26, 27, 28, 29, 49, 48, 77, 78, 92, 91, 96, 95, 0, 10, 12, 6, 14, 4, 8, 2])
sim.gen_npc(200, 0, 1)
vehicle = Vehicle({'path': [66, 18, 16, 19, 36, 28, 85, 77, 89, 91, 93, 95, 98, 2, 3, 4, 55, 51, 63, 60], 'is_main': True})
sim.add_vehicle(vehicle)
win = Window(sim)
win.run()
win.show()