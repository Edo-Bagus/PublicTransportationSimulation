from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# SOUTH, EAST, NORTH, WEST

# Intersection in
sim.create_segment((lane_space/2, length+intersection_size/2), (lane_space/2, intersection_size/2))
# Intersection out
# sim.create_segment((-lane_space/2, intersection_size/2), (-lane_space/2, length+intersection_size/2))
sim.create_segment((intersection_size/2, lane_space/2), (length+intersection_size/2, lane_space/2))
sim.create_segment((lane_space/2, -intersection_size/2), (lane_space/2, -length-intersection_size/2))
# sim.create_segment((-intersection_size/2, -lane_space/2), (-length-intersection_size/2, -lane_space/2))
# Straight
sim.create_segment((lane_space/2, intersection_size/2), (lane_space/2, -intersection_size/2))
# sim.create_segment((intersection_size/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
# sim.create_segment((-lane_space/2, -intersection_size/2), (-lane_space/2, intersection_size/2))
# sim.create_segment((-intersection_size/2, lane_space/2), (intersection_size/2, lane_space/2))
# Right turn
sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
# sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (lane_space/2, -lane_space/2), (lane_space/2, -intersection_size/2))
# sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
# sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (-lane_space/2, lane_space/2), (-lane_space/2, intersection_size/2))
# # Left turn
# sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
# sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (-lane_space/2, -lane_space/2), (-lane_space/2, intersection_size/2))
# sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
# sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (lane_space/2, lane_space/2), (lane_space/2, -intersection_size/2))

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


sim.connect_segment(0, [3, 4])
sim.connect_segment(1, [0])
sim.connect_segment(2, [0])
sim.connect_segment(3, [2])
sim.connect_segment(4, [1])


# v = Vehicle({'path': [0], 'x': 20, 'v':16.6})
# sim.add_vehicle(v)

# v = Vehicle({'path': [6, 20, 21, 22, 23, 24, 1, 13], 'x': 20, 'v':16.6})
# sim.add_vehicle(v)

# v = Vehicle({'path': [ 21, 22, 23, 24, 1, 13, 6, 20], 'x': 20, 'v':16.6})
# sim.add_vehicle(v)

# v = Vehicle({'path': [0, 12, 5]})
# sim.add_vehicle(v)

sim.gen_npc(17)

win = Window(sim)
win.run()
win.show()