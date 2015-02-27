import math
import logging
from bisect import bisect

import numpy as np

from config import Config


class ParticleFilter:
    map_granularity = 0.1
    # per_state_particle = 1
    max_walking_speed = 2
    distance_observation_stdvariance = 3


    def __init__(self):
        self.max_row_state = 0
        self.max_column_state = 0
        self.particle_number = 500
        self.particles = []
        self.distances_buffer = {}
        self.distances_buffer_counter = 0

    def init_particles(self):
        max_row = 0
        max_column = 0
        for key in Config.anchors:
            item = Config.anchors[key]
            if item[0] > max_row:
                max_row = item[0]
            if item[1] > max_column:
                max_column = item[1]
        logging.info("Map statistic: max_row:%d max_column:%d" % (max_row, max_column))
        self.max_row_state = max_row / self.map_granularity
        self.max_column_state = max_column / self.map_granularity
        # self.particle_number = self.max_column_state * self.max_row_state * self.per_state_particle
        i = 00
        while ( i < self.particle_number):
            r = np.random.random_integers(1, self.max_row_state)
            c = np.random.random_integers(1, self.max_column_state)
            self.particles.append((r, c))
            i += 1
        logging.info("Total particles:%d" % (self.particle_number))


    def particles_time_elapse(self):
        max_step = self.max_walking_speed / self.map_granularity
        new_particles = []
        for (r, c) in self.particles:
            r1 = r - max_step
            r2 = r + max_step
            c1 = c - max_step
            c2 = c + max_step
            if r1 < 1:
                r1 = 1
            if r2 > self.max_row_state:
                r2 = self.max_row_state
            if c1 < 1:
                c1 = 1
            if c2 > self.max_column_state:
                c2 = self.max_column_state
            nr = np.random.random_integers(r1, r2)
            nc = np.random.random_integers(c1, c2)
            new_particles.append((nr, nc))
        self.particles = new_particles
        # logging.info("Update particles done")


    def likelihood_reweight(self, distances):
        particles_probability = []
        new_particles = []
        total_probability = 0
        max_probability = 0
        result_particle = None

        # logging.info("Reweight Start")
        for particle in self.particles:
            reweight_probability = 1
            for anchor_key in Config.anchors:
                anchor = Config.anchors[anchor_key]
                particle_distance = self.calc_distance_between_particle_and_anchor(particle, anchor)
                reweight_probability *= self.calc_probability_based_on_observation(distances[int(anchor_key)],
                                                                                   particle_distance)
            particles_probability.append(reweight_probability)
            if (reweight_probability > max_probability):
                max_probability = reweight_probability
                result_particle = particle
            total_probability += reweight_probability
        #logging.info("Reweight Done")



        i = 0
        #Weighted Sampling Using Bisects
        total = 0
        cum_weights = []
        for w in particles_probability:
            total += w
            cum_weights.append(total)
        while i < len(particles_probability):
            draw = total_probability * np.random.random_sample()
            result = bisect(cum_weights, draw)
            #print(self.particles)
            new_particles.append(self.particles[result])
            #print(self.particles[result])
            i += 1

        final_x = (result_particle[0] - 0.5) * self.map_granularity
        final_y = (result_particle[1] - 0.5) * self.map_granularity

        return (final_x, final_y)

    def calc_distance_between_particle_and_anchor(self, particle, anchor):
        rposition = anchor[0] - (particle[0] - 0.5) * self.map_granularity
        cposition = anchor[1] - (particle[1] - 0.5) * self.map_granularity
        return math.sqrt(rposition * rposition + cposition * cposition)


    def calc_probability_based_on_observation(self, observation_distance, particle_distance):
        return math.exp(-(observation_distance - particle_distance) * (observation_distance - particle_distance) / (
            2 * self.distance_observation_stdvariance * self.distance_observation_stdvariance))

    def update(self, anchorId, distance):
        # Init
        if len(self.distances_buffer) == 0:
            for anchor_key in Config.anchors:
                self.distances_buffer[int(anchor_key)] = 0

        #Assign
        self.distances_buffer[anchorId] = distance
        self.distances_buffer_counter += 1
        if (self.distances_buffer_counter > 10):
            self.distances_buffer_counter = 0
            self.particles_time_elapse()
            #print(self.distances_buffer)
            #logging.warning("H")
            result = self.likelihood_reweight(self.distances_buffer)
            return result
        #logging.warning("N")
        return None


# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(levelname)s: %(message)s')
# Config.load_config()
# filter = ParticleFilter()
# filter.init_particles()
#
# i = 0
# x = 0
# y = 0
# distance={}
# time = 100
# totalerror = 0
# sign = 1
# while i < time:
# x += 0.2*sign
# y += 0.2*sign
#     if(x>=10):
#         sign = -1;
#     if(x<=0):
#         sign = 1;
#     x = 5
#     y = 5
#
#     distance[1] = math.sqrt((x-0)**2+(y-0)**2)+np.random.normal(loc=0.0, scale=0.1, size=None)
#     distance[2] = math.sqrt((x-10)**2+(y-0)**2)+np.random.normal(loc=0.0, scale=0.1, size=None)
#     distance[3] = math.sqrt((x-10)**2+(y-10)**2)+np.random.normal(loc=0.0, scale=0.1, size=None)
#     distance[4] = math.sqrt((x-0)**2+(y-10)**2)+np.random.normal(loc=0.0, scale=0.1, size=None)
#
#     filter.particles_time_elapse()
#     result = filter.likelihood_reweight(distance)
#     x1 = (result[0]-0.5)*filter.map_granularity
#     y1 = (result[1]-0.5)*filter.map_granularity
#     error = (x-x1)**2 + (y-y1)**2
#     totalerror+=error
#     #print("realposition: %f %f calcposition %f %f error:%f" % (x,y,x1,y1,error))
#     i += 1
# print("Error:%f"%(totalerror/time))
