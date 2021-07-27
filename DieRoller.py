# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class DieRoll:
        def __init__(self, die_num, die_type):
            self.die_num = die_num
            self.die_type = die_type
            self.max_roll = die_num*die_type
            self.min_roll = die_num
            
        def __repr__(self):
            die_string = str(self.die_num) + 'd' + str(self.die_type)
            return die_string 
        def get_die_num(self):
            return self.die_num
        def get_die_type(self):
            return self.die_type
        def get_min_roll(self):
            return self.min_roll
        def get_max_roll(self):
            return self.max_roll
        def get_possible_rolls(self):
            possible_roll_list = []
            for x in range(self.get_min_roll(), self.get_max_roll()+1):
                possible_roll_list.append(x)
            return possible_roll_list
                
        def roll(self):
            roll_total = 0
            for x in range (0, self.die_num):
                random_num = random.randint(1, self.die_type)
                # print ('Your Random Number this time is: ',random_num)
                roll_total = roll_total + random_num
            return roll_total
        
class AdvDieRoll(DieRoll):
    def __init__(self,die_num,die_type,die_drop):
        self.die_num = die_num
        self.die_type = die_type
        self.die_drop = die_drop
        self.max_roll = (die_num - die_drop)*die_type
        self.min_roll = die_num - die_drop
    def get_die_drop(self):
        return self.die_drop
    
    def roll(self):
        roll_total = 0
        roll_list = list()
        for x in range (0, self.die_num):
            random_num = random.randint(1, self.die_type)
            roll_list.append(random_num)
        # print ('Your list of rolls:  ', roll_list)
        roll_list_sorted = sorted(roll_list)
        # print ('Your list of rolls sorted:  ', roll_list_sorted)
        roll_list_dropped = roll_list_sorted[self.die_drop::]
        # print ('Your roles with dropped dice:' ,roll_list_dropped)
        
        for x in roll_list_dropped:
            roll_total = roll_total + int(x)
        return roll_total

# num_dice =int( input('How many dice do you want to roll?\n'))
# type_dice =int( input('What type of dice do you want to roll?\n'))
# dice_to_drop = int(input('How many dice to drop?'))

def DieRollStats(DieRoll, num_rolls):
    max_roll = DieRoll.get_max_roll()
    min_roll = DieRoll.get_min_roll()
    # print ('Min roll:', min_roll, '   Max Roll: ', max_roll)
    # print (max_roll , '   ', min_roll)
    die_hist = []
    for x in range(0,max_roll-min_roll+1):
        die_hist.append(0)
    # print(die_hist)
    for x in range (0, num_rolls):
        current_roll = DieRoll.roll()
        # print (current_roll)
        die_hist[current_roll-min_roll] = die_hist[current_roll-min_roll] + 1
        # print(die_hist)
    for i in range(len(die_hist)):
        die_hist[i] = die_hist[i]/num_rolls * 100
    return die_hist


# test_adv_die_roll = AdvDieRoll(4,6,1)

# stats_4_plot = DieRollStats(test_adv_die_roll, 100000)
# y_pos = test_adv_die_roll.get_possible_rolls()

# print(stats_4_plot, y_pos)

# plt.bar(y_pos,stats_4_plot,align='center')