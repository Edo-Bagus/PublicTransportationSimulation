import random
import math

class TrafficSignal:
    def __init__(self, segment, config={}):
        # Initialize segment
        self.segment = segment
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()

    def generate_tuples(self, n):
        return [tuple(i == j for j in range(n)) for i in range(n)]

    def set_default_config(self):
        self.cycle = self.generate_tuples(len(self.segment))
        self.slow_distance = 20
        self.slow_factor = 0.4
        self.stop_distance = 12
        self.cycle_length = 8

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        
        for i in range(len(self.segment)):
            for segment in self.segment[i]:
                segment.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]
    
    def update(self, sim):
        cycle_length = math.ceil(len(self.segment) * 5 / 2)
        # randomize the cycle length after every cycle
        # if(sim.t % cycle_length == 0):
        #     cycle_length = random.randint(1, 40)
        k = (sim.t // cycle_length) % len(self.segment)
        self.current_cycle_index = int(k)
        if(len(self.segment) < len(self.segment)):
            self.current_cycle_index = len(self.segment) - 1