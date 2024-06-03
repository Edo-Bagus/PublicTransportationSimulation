from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# SOUTH, EAST, NORTH, WEST

# Intersection in
sim.create_segment((lane_space/2, length+intersection_size/2), (lane_space/2, intersection_size/2))
sim.create_segment((length+intersection_size/2, -lane_space/2), (intersection_size/2, -lane_space/2))
sim.create_segment((-lane_space/2, -length-intersection_size/2), (-lane_space/2, -intersection_size/2))
sim.create_segment((-length-intersection_size/2, lane_space/2), (-intersection_size/2, lane_space/2))
# Intersection out
sim.create_segment((-lane_space/2, intersection_size/2), (-lane_space/2, length+intersection_size/2))
sim.create_segment((intersection_size/2, lane_space/2), (length+intersection_size/2, lane_space/2))
sim.create_segment((lane_space/2, -intersection_size/2), (lane_space/2, -length-intersection_size/2))
sim.create_segment((-intersection_size/2, -lane_space/2), (-length-intersection_size/2, -lane_space/2))
# Straight
sim.create_segment((lane_space/2, intersection_size/2), (lane_space/2, -intersection_size/2))
sim.create_segment((intersection_size/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_segment((-lane_space/2, -intersection_size/2), (-lane_space/2, intersection_size/2))
sim.create_segment((-intersection_size/2, lane_space/2), (intersection_size/2, lane_space/2))
# Right turn
sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (lane_space/2, -lane_space/2), (lane_space/2, -intersection_size/2))
sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (-lane_space/2, lane_space/2), (-lane_space/2, intersection_size/2))
# Left turn
sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (-lane_space/2, -lane_space/2), (-lane_space/2, intersection_size/2))
sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (lane_space/2, lane_space/2), (lane_space/2, -intersection_size/2))

# sim.create_quadratic_bezier_curve((lane_space/2, -length-intersection_size/2), (lane_space/2 , -length-intersection_size/2 - 20), (lane_space/2 + 20, -length-intersection_size/2 - 20))
# sim.create_segment((lane_space/2 + 20, -length-intersection_size/2 - 20), (lane_space/2 + 100, -length-intersection_size/2 - 20))
# sim.create_quadratic_bezier_curve((lane_space/2 + 100, -length-intersection_size/2 - 20), (lane_space/2 + 120, -length-intersection_size/2 - 20), (lane_space/2 + 120, -length-intersection_size/2))
# sim.create_segment((lane_space/2 + 120, -length-intersection_size/2), (lane_space/2 + 120, -length-intersection_size/2 + 100))
# sim.create_quadratic_bezier_curve((lane_space/2 + 120, -length-intersection_size/2 + 100), (lane_space/2 + 120, -length-intersection_size/2 + 105), (length+intersection_size/2, -lane_space/2))
# vg = VehicleGenerator({
#     'vehicles': [
#         (1, {'path': [0, 8, 6], 'v': 16.6}),
#         (1, {'path': [0, 12, 5], 'v': 16.6})
#         ]
#     })
# sim.add_vehicle_generator(vg)

sim.create_signal([[0], [1], [2], [3]])

sim.connect_segment(0, [8, 12, 16])
sim.connect_segment(1, [9, 13, 17])
sim.connect_segment(2, [10, 14, 18])
sim.connect_segment(3, [11, 15, 19])
sim.connect_segment(4, [0, 1, 2, 3])
sim.connect_segment(5, [0, 1, 2, 3])
sim.connect_segment(6, [0, 1, 2, 3])
sim.connect_segment(7, [0, 1, 2, 3])
sim.connect_segment(8, [6])
sim.connect_segment(9, [7])
sim.connect_segment(10, [4])
sim.connect_segment(11, [5])
sim.connect_segment(12, [5])
sim.connect_segment(13, [6])
sim.connect_segment(14, [7])
sim.connect_segment(15, [4])
sim.connect_segment(16, [7])
sim.connect_segment(17, [4])
sim.connect_segment(18, [5])
sim.connect_segment(19, [6])\

sim.set_spawnable_segments([0, 1, 2, 3])



      
# v = Vehicle({'path': [3]})
# sim.add_vehicle(v)

# v = Vehicle({'path': [2]})
# sim.add_vehicle(v)

# v = Vehicle({'path': [1]})
# sim.add_vehicle(v)

# v = Vehicle({'path': [0]})
# sim.add_vehicle(v)

sim.gen_npc(40, 0.3, 0.7)

win = Window(sim)
win.run()
win.show()