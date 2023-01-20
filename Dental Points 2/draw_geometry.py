import cv2
import matplotlib.pyplot as plt
from required_function import *
from define_variables import *

def plot(data_dict,picture_location):

    def plot_lines(data_dict):
        plt.plot([data_dict['6L_x'], data_dict['6R_x']], [data_dict['6L_y'], data_dict['6R_y']], color='blue', linewidth=1) #line6
        plt.plot(x_perpendicular, y_perpendicular, color='green', linewidth=1) #line through mid6 peripendicular to line6
        plt.plot(x_range, y_parallel, color='purple', linewidth=1) # line through C' parallel to line6
        plt.plot(x_range, lin5_par6, color='purple', linewidth=1) # line through mid5 parallel to 6
        plt.plot(x_range, line4_par6, color='purple', linewidth=1) # line through mid4 parallel to 6
    plot_lines(data_dict)

    def plot_calculated_points(data_dict):

        '''plotting mid points'''
        plt.scatter([mid_6x, mid_5x, mid_4x], [mid_6y, mid_5y, mid_4y], color='red', s=25, marker='v')

        '''plotting C' and C" '''
        plt.scatter([c_x, c__x], [c_y, c__y], color='red', s=25, marker='+')

        '''plotting points 22mm away from mid6 along line 6'''
        plt.scatter([mid_6x + PIXEL_FOR_22MM * cos_slope6, mid_6x - PIXEL_FOR_22MM * cos_slope6],
                    [mid_6y + PIXEL_FOR_22MM * sin_slope6, mid_6y - PIXEL_FOR_22MM * sin_slope6],
                    color='green', s=15, marker='v')

        '''plotting intersection points of ellipse and line 4,5'''
        plt.scatter([coord4_[0], coord4_[1], coord5_[0], coord5_[1]], [coord4_[2], coord4_[3], coord5_[2], coord5_[3]],
                    color='blue', s=50, marker='+')
    plot_calculated_points(data_dict)

    def ellipse(data_dict):
        ax = plt.gca()
        plot_ellipse(ax, center=(mid_6x, mid_6y), width=a, height=b, phi=ellipse_angle, color='red', lw=1)
    ellipse(data_dict)

    def plot_seven_points(data_dict):
        x_coordinates = []
        y_coordinates = []
        for key in data_dict.keys():
            if 'x' in key:
                x_coordinates.append(data_dict[key])

            elif 'y' in key:
                y_coordinates.append(data_dict[key])
        plt.scatter(x_coordinates, y_coordinates, color='black', s=7, marker='v')
    plot_seven_points(data_dict)

    def plot_pic(picture_location):
        img_test = cv2.imread(picture_location)
        plt.imshow(img_test)
        plt.show()
    plot_pic(picture_location)

