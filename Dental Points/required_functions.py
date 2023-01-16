from variables import *
from matplotlib.patches import Ellipse


def get_mid_point(point_ax, point_ay, point_bx, point_by):
    return (point_ax + point_bx) / 2, (point_ay + point_by) / 2


def get_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope


def plot_ellipse(ax, center, width, height, phi, color, lw):
    ellipse = Ellipse(
        xy=center, width=2 * width, height=2 * height, angle=np.rad2deg(phi),
        edgecolor=color, fc='None', lw=lw, label='Fit', zorder=2
    )
    ax.add_patch(ellipse)


def get_intersects2(Mx, My):
    m = slope6
    c = My - (m * Mx)
    sin0 = np.sin(np.arctan(slope6))
    cos0 = np.cos(np.arctan(slope6))
    e = ((a * sin0) ** 2) + ((b * cos0) ** 2)
    f = 2 * ((b ** 2) - (a ** 2)) * sin0 * cos0
    g = ((a * cos0) ** 2) + ((b * sin0) ** 2)
    h = (a * b) ** 2
    j = (m * M6_x) + c - M6_y
    t = e + (f * m) + (g * (m ** 2))
    u = (f * j) + (2 * g * m * j)
    z = (g * (j ** 2)) - h
    n1 = (-u - math.sqrt((u ** 2) - (4 * t * z))) / (2 * t)
    n2 = (-u + math.sqrt((u ** 2) - (4 * t * z))) / (2 * t)
    x1_intersect = n1 + M6_x
    x2_intersect = n2 + M6_x
    y1_intersect = (m * x1_intersect) + c
    y2_intersect = (m * x2_intersect) + c
    #     print(t,u,z)
    return x1_intersect, x2_intersect, y1_intersect, y2_intersect


def get_lineSegments(x1, y1, x2, y2):
    lengthOfSegment = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return lengthOfSegment


coord_4 = get_intersects2(M4_x, M4_y)
length_4 = get_lineSegments(coord_4[1], coord_4[0], coord_4[3], coord_4[2])
print('4L__X:', coord_4[0],
      '4R__X:', coord_4[1],
      '4L__Y:', coord_4[2],
      '4R__Y:', coord_4[3])
print('length of line4_: ', length_4)

coord_5 = get_intersects2(M5_x, M5_y)
length_5 = get_lineSegments(coord_5[1], coord_5[0], coord_5[3], coord_5[2])
print('5L__X:', coord_5[0],
      '5R__X:', coord_5[1],
      '5L__Y:', coord_5[2],
      '5R__Y:', coord_5[3])
print('length of line5_: ', length_5)
