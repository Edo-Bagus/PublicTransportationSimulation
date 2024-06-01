from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# SOUTH, EAST, NORTH, WEST

sim.create_segment((-100, -100), (100, -100))
# sim.create_segment((lane_space/2, lane_space/2), (100, -100))
# sim.create_quadratic_bezier_curve((100, -100), (120, -100), (120, -80))
# sim.create_segment((120, -80), (120, 100))
# sim.create_quadratic_bezier_curve((120, 100), (120, 120), (100, 120))
# sim.create_segment((100, 120), (-100, 120))
# sim.create_quadratic_bezier_curve((-100, 120), (-120, 120), (-120, 100))
# sim.create_segment((-120, 100), (-120, -80))
# sim.create_quadratic_bezier_curve((-120, -80), (-120, -100), (-100, -100))

# sim.create_segment((100, -100), (150, -100))
# sim.create_quadratic_bezier_curve((150, -100), (170, -100), (170, -80))
# sim.create_segment((170, -80), (170, 100))
# sim.create_quadratic_bezier_curve((170, 100), (170, 120), (150, 120))
# sim.create_segment((150, 120), (100, 120))

# Intersection in
# sim.create_segment((lane_space/2, length+intersection_size/2), (lane_space/2, intersection_size/2))
# sim.create_segment((length+intersection_size/2, -lane_space/2), (intersection_size/2, -lane_space/2))
# sim.create_segment((-lane_space/2, -length-intersection_size/2), (-lane_space/2, -intersection_size/2))
# sim.create_segment((-length-intersection_size/2, lane_space/2), (-intersection_size/2, lane_space/2))
# # Intersection out
# sim.create_segment((-lane_space/2, intersection_size/2), (-lane_space/2, length+intersection_size/2))
# sim.create_segment((intersection_size/2, lane_space/2), (length+intersection_size/2, lane_space/2))
# sim.create_segment((lane_space/2, -intersection_size/2), (lane_space/2, -length-intersection_size/2))
# sim.create_segment((-intersection_size/2, -lane_space/2), (-length-intersection_size/2, -lane_space/2))
# # Straight
# sim.create_segment((lane_space/2, intersection_size/2), (lane_space/2, -intersection_size/2))
# sim.create_segment((intersection_size/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
# sim.create_segment((-lane_space/2, -intersection_size/2), (-lane_space/2, intersection_size/2))
# sim.create_segment((-intersection_size/2, lane_space/2), (intersection_size/2, lane_space/2))
# # Right turn
# sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
# sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (lane_space/2, -lane_space/2), (lane_space/2, -intersection_size/2))
# sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
# sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (-lane_space/2, lane_space/2), (-lane_space/2, intersection_size/2))
# # Left turn
# sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
# sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (-lane_space/2, -lane_space/2), (-lane_space/2, intersection_size/2))
# sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
# sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (lane_space/2, lane_space/2), (lane_space/2, -intersection_size/2))

# vg = VehicleGenerator({
#     'vehicles': [
#         (1, {'path': [0, 1, 2, 3, 4, 5, 6, 7], 'v': 16.6})
#         ]
#     })
# sim.add_vehicle_generator(vg) 

# vehicle = Vehicle({'path': [0, 1, 2, 3, 4, 5, 6, 7], 'v': 0, 'v_max': 5, 'x': 50})
# vehicle2 = Vehicle({'path': [2, 3, 4, 5, 6, 7, 0, 1], 'v': 16.6, 'l': 4})
# vehicle3 = Vehicle({'path': [1, 2, 3, 4, 5, 6, 7, 0], 'v': 16.6})
# sim.add_vehicle(vehicle)
# sim.add_vehicle(vehicle2)
# sim.add_vehicle(vehicle3)

win = Window(sim)
win.run()
win.show()