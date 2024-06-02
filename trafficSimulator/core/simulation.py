from .vehicle_generator import VehicleGenerator
from .geometry.quadratic_curve import QuadraticCurve
from .geometry.cubic_curve import CubicCurve
from .geometry.segment import Segment
from .vehicle import Vehicle
from .trafficSignal import TrafficSignal
import random
import math


class Simulation:
    def __init__(self):
        self.segments = []
        self.vehicles = {}
        self.vehicle_generator = []
        self.traffic_signals = []

        self.t = 0.0
        self.frame_count = 0
        self.dt = 1/60  


    def add_vehicle(self, veh):
        self.vehicles[veh.id] = veh
        if len(veh.path) > 0:
            self.segments[veh.path[0]].add_vehicle(veh)

    def add_segment(self, seg):
        self.segments.append(seg)

    def add_vehicle_generator(self, gen):
        self.vehicle_generator.append(gen)

    
    def create_vehicle(self, **kwargs):
        veh = Vehicle(kwargs)
        self.add_vehicle(veh)

    def create_segment(self, *args):
        seg = Segment(args)
        self.add_segment(seg)

    def create_signal(self, segments, config={}):
        segments = [[self.segments[i] for i in segment_group] for segment_group in segments]
        sig = TrafficSignal(segments, config)
        self.traffic_signals.append(sig)
        return sig
    
    def connect_segment(self, segment_index, connected_segments_index):
        for seg_index in connected_segments_index:
            self.segments[segment_index].connected_segments.append(seg_index)

    def gen_npc(self, total_people):
        car_count = math.ceil(total_people / 4)
        segment_index = 0
        spawn_margin = 0
        for i in range(car_count):
            car_config = {}
            # random_segment_index = random.randint(0, len(self.segments) - 1)
            # random_spawn_x = random.uniform(0, self.segments[random_segment_index].get_length())
            # if len(self.segments[random_segment_index]) == 0:
            #     car_config['x'] = random_spawn_x
            # else:
            #     for spawn_choice in self.segments[random_segment_index].chosen_spawn_x:
            #         if random_spawn_x >= spawn_choice and random_spawn_x <= spawn_choice + 20:

            car_config['path'] = [segment_index]
            car_config['v'] = 0
            # spawn_choice = [0, self.segments[random_segment_index].
            car_config['x'] = self.segments[segment_index].get_length() - spawn_margin
            veh = Vehicle(car_config)
            self.add_vehicle(veh)
            if segment_index < len(self.segments) - 1:
                segment_index += 1
            else:
                segment_index = 0
                spawn_margin += 10


    def create_quadratic_bezier_curve(self, start, control, end):
        cur = QuadraticCurve(start, control, end)
        self.add_segment(cur)

    def create_cubic_bezier_curve(self, start, control_1, control_2, end):
        cur = CubicCurve(start, control_1, control_2, end)
        self.add_segment(cur)

    def create_vehicle_generator(self, **kwargs):
        gen = VehicleGenerator(kwargs)
        self.add_vehicle_generator(gen)


    def run(self, steps):
        for _ in range(steps):
            self.update()

    def update(self):


        for signal in self.traffic_signals:
            signal.update(self)
            # print(signal.segment[0][0])
            # signal.segment[0].isTraffic = signal.cycle[0][signal.current_cycle_index]

        # Update vehicles
        for segment in self.segments:
            if len(segment.vehicles) != 0:
                self.vehicles[segment.vehicles[0]].update(None, self.dt)
            for i in range(1, len(segment.vehicles)):
                self.vehicles[segment.vehicles[i]].update(self.vehicles[segment.vehicles[i-1]], self.dt)
                # Check for traffic signal
                

        # Check roads for out of bounds vehicle
        for segment in self.segments:
            # If road has no vehicles, continue
            if len(segment.vehicles) == 0: continue
            # If not
            vehicle_id = segment.vehicles[0]
            vehicle = self.vehicles[vehicle_id]

            if segment.traffic_signal_state:
                # If traffic signal is green or doesn't exist
                # Then let vehicles pass
                vehicle.unstop()
                for vehicle_id in segment.vehicles:
                    vehicle = self.vehicles[vehicle_id]
                    vehicle.unslow()
            else:
                if vehicle.x >= segment.get_length() - segment.slowDistance:
                    # Slow vehicles in slowing zone
                    vehicle.slow(0.4*vehicle._v_max)
                if vehicle.x >= segment.get_length() - segment.stopDistance and\
                    vehicle.x <= segment.get_length() - segment.stopDistance / 2:
                    # Stop vehicles in the stop zone
                    vehicle.stop()
                    
        for segment in self.segments:
            # If road has no vehicles, continue
            if len(segment.vehicles) == 0: continue
            # If not
            vehicle_id = segment.vehicles[0]
            vehicle = self.vehicles[vehicle_id]
            # If first vehicle is out of road bounds
            # print('x:', vehicle.x)
            if vehicle.x >= segment.get_length():
                
                # If vehicle has a next road
                # if vehicle.current_road_index + 1 < len(vehicle.path):
                #     # Update current road to next road
                #     vehicle.current_road_index += 1
                # else:
                #     vehicle.current_road_index = 0
                    # Add it to the next road
                next_road_index = random.choice(segment.connected_segments)
                self.segments[next_road_index].vehicles.append(vehicle_id)
                # Reset vehicle properties
                vehicle.x = 0
                # In all cases, remove it from its road
                segment.vehicles.popleft() 

        # Update vehicle generators
        for gen in self.vehicle_generator:
            gen.update(self)
        # Increment time
        self.t += self.dt
        self.frame_count += 1
