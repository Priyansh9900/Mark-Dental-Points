import cv2
import matplotlib.pyplot as plt
from required_functions import get_mid_point
from variables import PIXEL_FOR_22MM


def plot(data_dict, picture_location):
    point_seven_points(data_dict)
    mid_6x, mid_6y, mid_5x, mid_5y, mid_4x, mid_4y = find_and_plot_mid_points(data_dict)


    # plotting points 22mm away from 6M along line6
    plt.scatter([mid_6x + PIXEL_FOR_22MM * cos_slope6, mid_6x - PIXEL_FOR_22MM * cos_slope6],
                [mid_6y + PIXEL_FOR_22MM * sin_slope6, mid_6y - PIXEL_FOR_22MM * sin_slope6],
                color='green', s=15, marker='v')
    # plotting C' and C"
    plt.scatter([c_x, c__x], [c_y, c__y], color='red', s=25, marker='+')
    # plotting intersection points of ellipse and line 4,5
    plt.scatter([coord_4[0], coord_4[1], coord_5[0], coord_5[1]], [coord_4[2], coord_4[3], coord_5[2], coord_5[3]],
                color='blue', s=50, marker='+')

    plt.plot(x_per, y_per, color='green', linewidth=1)
    plt.plot([data_dict['6L_x'], data_dict['6R_x']], [data_dict['6L_y'], data_dict['6R_y']], color='blue', linewidth=1)
    plt.plot(x_par, y_par, color='purple', linewidth=1)
    plt.plot(x_5, y_5, color='orange', linewidth=1)
    plt.plot(x_4, y_4, color='yellow', linewidth=1)
    plt.plot(x_5, y_5_par, color='purple', linewidth=1)
    plt.plot(x_4, y_4_par, color='purple', linewidth=1)

    ax = plt.gca()
    plot_ellipse(ax, center=(mid_6x, mid_6y), width=PIXEL_FOR_22MM, height=M6_C__, phi=ellipse_angle, color='red', lw=1)

    plot_pic(picture_location)
    plt.show()


def point_seven_points(data_dict):
    x_coordinates = []
    y_coordinates = []
    for key in data_dict.keys():
        if 'x' in key:
            x_coordinates.append(data_dict[key])

        elif 'y' in key:
            y_coordinates.append(data_dict[key])
    plt.scatter(x_coordinates, y_coordinates, color='black', s=7, marker='v')


def plot_pic(picture_location):
    img_test = cv2.imread(picture_location)
    plt.imshow(img_test)


def find_and_plot_mid_points(data_dict):
    mid_6x, mid_6y = get_mid_point(data_dict['6L_x'], data_dict['6L_y'], data_dict['6R_x'], data_dict['6R_y'])
    mid_5x, mid_5y = get_mid_point(data_dict['5L_x'], data_dict['5L_y'], data_dict['5R_x'], data_dict['5R_y'])
    mid_4x, mid_4y = get_mid_point(data_dict['4L_x'], data_dict['4L_y'], data_dict['4R_x'], data_dict['4R_y'])
    plt.scatter([mid_6x, mid_5x, mid_4x], [mid_6y, mid_5y, mid_4y], color='red', s=25, marker='v')
    return mid_6x, mid_6y, mid_5x, mid_5y, mid_4x, mid_4y
