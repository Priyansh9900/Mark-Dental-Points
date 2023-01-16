import numpy as np
import math
# from required_functions import get_slope
from Read_data import D

def get_slope(x1,y1,x2,y2):
    slope = (y2-y1)/(x2-x1)
    return slope

# Get Mid points 
M6_x = (D['6L_x']+D['6R_x'])/2
M6_y = (D['6L_y']+D['6R_y'])/2
M5_x = (D['5L_x']+D['5R_x'])/2
M5_y = (D['5L_y']+D['5R_y'])/2
M4_x = (D['4L_x']+D['4R_x'])/2
M4_y = (D['4L_y']+D['4R_y'])/2
# 
pixel_per_mm = 14.697041795364752
d = 22 * pixel_per_mm
d2 = 1*pixel_per_mm

# Getting Slopes of lines
slope6 = get_slope(D['6L_x'],D['6L_y'],D['6R_x'],D['6R_y'])
slope6_per = -1/slope6
cos_slope6 = 1/math.sqrt(1+(slope6)**2)
sin_slope6 = slope6/math.sqrt(1+(slope6)**2)
cos_slope6_per = 1/math.sqrt(1+(slope6_per)**2)
sin_slope6_per = slope6_per/math.sqrt(1+(slope6_per)**2)
slope5 = get_slope(D['5L_x'],D['5L_y'],D['5R_x'],D['5R_y'])
slope4 = get_slope(D['4L_x'],D['4L_y'],D['4R_x'],D['4R_y'])

# getting the lines equaitions
x_par = np.linspace(500,1500)
y_par = slope6*x_par + D['C_y'] - slope6*D['C_x']
x_per = np.linspace(950,1020)
y_per = slope6_per*x_per + M6_y - slope6_per*M6_x
x_5 = np.linspace(500,1500)
y_5 = slope5*x_5 + D['5R_y'] - slope5*D['5R_x']
y_5_par = slope6*x_5+M5_y-slope6*M5_x
x_4 = np.linspace(500,1500)
y_4 = slope4*x_4 + D['4R_y'] - slope4*D['4R_x']
y_4_par = slope6*x_4+M4_y-slope6*M4_x

# Finding intersection point (C')
m1, c1 = slope6, D['C_y'] - slope6*D['C_x']
m2, c2 = slope6_per, M6_y - slope6_per*M6_x
c_x = (c1 - c2) / (m2 - m1)
c_y = m1 * c_x + c1
c__x = c_x+d2*cos_slope6_per
c__y = c_y+d2*sin_slope6_per

# tilt angle of ellipse
ellipse_angle = np.arctan(slope6)
ellipse_angle_degree = np.rad2deg(ellipse_angle)
# major axis,minor axis
M6_C__ = math.sqrt(((c__x-M6_x)**2)+((c__y-M6_y)**2))
b = M6_C__
a = d
