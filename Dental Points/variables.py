import numpy as np
import math
from read_data import *

def get_slope(x1,y1,x2,y2):
    slope = (y2-y1)/(x2-x1)
    return slope
'''Getting all the required slopes'''
slope6 = get_slope(D['6L_x'],D['6L_y'],D['6R_x'],D['6R_y'])
slope6_perpendicular = -1 / slope6
cos_slope6 = 1/math.sqrt(1+(slope6)**2)
sin_slope6 = slope6/math.sqrt(1+(slope6)**2)
cos_slope6_perpendicular = 1 / math.sqrt(1 + (slope6_perpendicular) ** 2)
sin_slope6_perpendicular = slope6_perpendicular / math.sqrt(1 + (slope6_perpendicular) ** 2)
slope5 = get_slope(D['5L_x'],D['5L_y'],D['5R_x'],D['5R_y'])
slope4 = get_slope(D['4L_x'],D['4L_y'],D['4R_x'],D['4R_y'])

def get_mid_point(a,b):
    mid_point = (a+b)/2
    return mid_point
'''Getting mid points'''
mid_6x, mid_6y = get_mid_point(D['6L_x'], D['6R_x']), get_mid_point(D['6L_y'], D['6R_y'])
mid_5x, mid_5y = get_mid_point(D['5L_x'], D['5R_x']), get_mid_point(D['5L_y'], D['5R_y'])
mid_4x, mid_4y = get_mid_point(D['4L_x'], D['4R_x']), get_mid_point(D['4L_y'], D['4R_y'])

PIXEL_PER_MM = 14.697041795364752
PIXEL_FOR_22MM = 22 * PIXEL_PER_MM
C_C__ = 1 * PIXEL_PER_MM # length (C'C")

def get_line_equation(slope, x, x1, y1):
    c = y1 - slope*x1
    y = slope*x + c
    return y
'''getting equations of different required lines'''
x_range = np.linspace(500, 1500)
y_parallel = get_line_equation(slope6, x_range, D['C_x'], D['C_y']) #line through C parallel to line6
x_perpendicular = np.linspace(950,1020)
y_perpendicular = get_line_equation(slope6_perpendicular, x_perpendicular, mid_6x, mid_6y) #line through mid6 perpendicular to line6
line_5 = get_line_equation(slope5, x_range, D['5R_x'], D['5R_y'])
lin5_par6 = get_line_equation(slope6, x_range, mid_5x, mid_5y) #line through mid5 parallel to line6
line_4 = get_line_equation(slope4, x_range, D['4R_x'], D['4R_y'])
line4_par6 = get_line_equation(slope6, x_range, mid_4x, mid_4y) #line through mid4 parallel to line6

'''Getting intersection of perpendicular lines C' '''
m1, c1 = slope6, D['C_y'] - slope6*D['C_x']
m2, c2 = slope6_perpendicular, mid_6y - slope6_perpendicular * mid_6x
c_x = (c1 - c2) / (m2 - m1) # C'x
c_y = m1 * c_x + c1 # C'y
'''Getting co-orfinates of C" '''
c__x = c_x + C_C__ * cos_slope6_perpendicular # C"x
c__y = c_y + C_C__ * sin_slope6_perpendicular # C"y
M6_C__ = math.sqrt(((c__x-mid_6x)**2)+((c__y-mid_6y)**2)) #lenth between mid6 and C"

'''tilt angle of ellipse'''
ellipse_angle = np.arctan(slope6)

''' Major and minor axis of ellipse '''
b = M6_C__
a = PIXEL_FOR_22MM
