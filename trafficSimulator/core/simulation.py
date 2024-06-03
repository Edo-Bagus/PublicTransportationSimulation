from .vehicle_generator import VehicleGenerator
from .geometry.quadratic_curve import QuadraticCurve
from .geometry.cubic_curve import CubicCurve
from .geometry.segment import Segment
from .vehicle import Vehicle
from .trafficSignal import TrafficSignal
import random
import math
import copy


class Simulation:
    def __init__(self):
        self.initial_vehicles = {}
        self.initial_traffic_signals = []
        self.segments = []
        self.vehicles = {}
        self.vehicle_generator = []
        self.traffic_signals = []
        self.spawnable_segment_indeces = []

        self.t = 0.0
        self.frame_count = 0
        self.dt = 1/60  


    def add_vehicle(self, veh):
        self.vehicles[veh.id] = veh
        if veh.is_main:
            self.main_vehicle = copy.deepcopy(veh)
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

    def set_spawnable_segments(self, segment_indeces):
        self.spawnable_segment_indeces = segment_indeces

    def create_signal(self, segments, config={}):
        segments = [[self.segments[i] for i in segment_group] for segment_group in segments]
        sig = TrafficSignal(segments, config)
        self.traffic_signals.append(sig)
        return sig
    
    def connect_segment(self, segment_index, connected_segments_index):
        for seg_index in connected_segments_index:
            self.segments[segment_index].connected_segments.append(seg_index)

    def gen_npc(self, total_people, car_proportion, bus_proportion):
        self.total_people = total_people
        self.car_proportion = car_proportion
        self.bus_proportion = bus_proportion
        car_count = math.ceil(round(total_people*car_proportion) / 4)
        bus_count = math.ceil(round(total_people*bus_proportion) / 10)
        random.shuffle(self.spawnable_segment_indeces)
        veh_l_list = []
        for i in range(car_count):
            veh_l_list.append(4)
        for i in range(bus_count):
            veh_l_list.append(8)
        random.shuffle(veh_l_list)
        segment_index = 0
        spawn_margin = 10
        for i in range(car_count + bus_count):
            veh_config = {}
            # random_segment_index = random.randint(0, len(self.segments) - 1)
            # random_spawn_x = random.uniform(0, self.segments[random_segment_index].get_length())
            # if len(self.segments[random_segment_index]) == 0:
            #     veh_config['x'] = random_spawn_x
            # else:
            #     for spawn_choice in self.segments[random_segment_index].chosen_spawn_x:
            #         if random_spawn_x >= spawn_choice and random_spawn_x <= spawn_choice + 20:

            spawn_index = self.spawnable_segment_indeces[segment_index]
            veh_config['path'] = [spawn_index]
            veh_config['v'] = 0
            veh_config['l'] = veh_l_list[i]
            # spawn_choice = [0, self.segments[random_segment_index].
            veh_config['x'] = self.segments[spawn_index].get_length() - spawn_margin
            veh = Vehicle(veh_config)
            self.add_vehicle(veh)
            if segment_index < len(self.spawnable_segment_indeces) - 1:
                segment_index += 1
            else:
                segment_index = 0
                spawn_margin +=  10 + veh_l_list[i]
        # self.initial_vehicles = copy.deepcopy(self.vehicles)
        # print(self.vehicles)
        # print(self.initial_vehicles)
        
    def restart(self):
        # self.vehicles = copy.deepcopy(self.initial_vehicles)
        # random.shuffle(self.spawnable_segment_indeces)
        # segment_index = 0
        # spawn_margin = 10
        # for key in self.vehicles:
        #     spawn_index = self.spawnable_segment_indeces[segment_index]
        #     self.vehicles[key].path = [spawn_index]
        #     self.vehicles[key].x = self.segments[spawn_index].get_length() - spawn_margin
        #     if segment_index < len(self.spawnable_segment_indeces) - 1:
        #         segment_index += 1
        #     else:
        #         segment_index = 0
        #         spawn_margin +=  10 + self.vehicles[key].l
        self.vehicles.clear()
        for segment in self.segments:
            segment.vehicles.clear()
        self.gen_npc(self.total_people, self.car_proportion, self.bus_proportion)
        self.add_vehicle(self.main_vehicle)




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
                
        # for segment in self.segments:
        #     if len(segment.vehicles) == 0: 
        #         segment.is_full = False
        #         continue
        #     vehicle_id = segment.vehicles[-1]
        #     vehicle = self.vehicles[vehicle_id]
        #     if vehicle.x <= 0:
        #         segment.is_full = True
        #     else:
        #         segment.is_full = False

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
            next_road_index = random.choice(segment.connected_segments)
            # If first vehicle is out of road bounds
            # print('x:', vehicle.x)

            # if self.segments[next_road_index].is_full == False:
            #     # If traffic signal is green or doesn't exist
            #     # Then let vehicles pass
            #     vehicle.unstop()
            #     for vehicle_id in segment.vehicles:
            #         vehicle = self.vehicles[vehicle_id]
            #         vehicle.unslow()
            # else:
            # if self.segments[next_road_index].is_full and vehicle.x >= segment.get_length() - segment.slowDistance:
            #     vehicle.slow(0.4*vehicle._v_max)
            # if self.segments[next_road_index].is_full and vehicle.x >= segment.get_length() - segment.stopDistance and\
            #         vehicle.x <= segment.get_length():
            #     vehicle.stop()
            if vehicle.x >= segment.get_length():
                
                # If vehicle has a next road
                if vehicle.is_main:
                    if vehicle.current_road_index + 1 < len(vehicle.path):
                        # Update current road to next road
                        vehicle.current_road_index += 1
                    else:
                        vehicle.current_road_index = 0
                        vehicle.is_finish = True
                    next_road_index = vehicle.path[vehicle.current_road_index]

                    # Add it to the next road
                
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
