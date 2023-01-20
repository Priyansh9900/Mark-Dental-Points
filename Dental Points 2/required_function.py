from define_variables import *
from input_parameters import *
from matplotlib.patches import Ellipse

def get_lineSegments(x1,y1,x2,y2):
    lengthOfSegment = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return lengthOfSegment

length6 = get_lineSegments(D['6L_x'],D['6L_y'],D['6R_x'],D['6R_y']) # lineSegment - 6
length6_ = get_lineSegments(mid_6x + PIXEL_FOR_22MM * cos_slope6,mid_6y + PIXEL_FOR_22MM * sin_slope6,
                            mid_6x - PIXEL_FOR_22MM * cos_slope6,mid_6y - PIXEL_FOR_22MM * sin_slope6) # lineSegment- 6'
''' Major and minor axis of ellipse '''
b = M6_C__ # major axis
if (space_required > 0 and length6 < 2*PIXEL_FOR_22MM) or (space_required < 0 and length6 > 2*PIXEL_FOR_22MM):
    a = PIXEL_FOR_22MM
elif (space_required > 0 and length6 > 2*PIXEL_FOR_22MM) or (space_required < 0 and length6 < 2*PIXEL_FOR_22MM):
    a = length6/2
if length6>=2*PIXEL_FOR_22MM:
    a = length6/2
else :
    a = PIXEL_FOR_22MM # minor axis
def plot_ellipse(ax, center, width, height, phi, color,lw):
    ellipse = Ellipse(
        xy=center, width=2 * width, height=2 * height, angle=np.rad2deg(phi),
        edgecolor=color, fc='None', lw=lw, label='Fit', zorder=2
    )
    ax.add_patch(ellipse)

def line_ellipse_intersection(slope,mid_x, mid_y):
    m = slope
    c = mid_y - (m * mid_x)
    sin0 = np.sin(np.arctan(slope6))
    cos0 = np.cos(np.arctan(slope6))
    e = ((a * sin0) ** 2) + ((b * cos0) ** 2)
    f = 2 * ((b ** 2) - (a ** 2)) * sin0 * cos0
    g = ((a * cos0) ** 2) + ((b * sin0) ** 2)
    h = (a * b) ** 2
    j = (m * mid_6x) + c - mid_6y
    t = e + (f * m) + (g * (m ** 2))
    u = (f * j) + (2 * g * m * j)
    z = (g * (j ** 2)) - h
    n1 = (-u - math.sqrt((u ** 2) - (4 * t * z))) / (2 * t)
    n2 = (-u + math.sqrt((u ** 2) - (4 * t * z))) / (2 * t)
    x1_intersect = n1 + mid_6x
    x2_intersect = n2 + mid_6x
    y1_intersect = (m * x1_intersect) + c
    y2_intersect = (m * x2_intersect) + c
    return x1_intersect, x2_intersect, y1_intersect, y2_intersect

coord4_ = line_ellipse_intersection(slope6, mid_4x, mid_4y)
length4 = get_lineSegments(D['4L_x'],D['4L_y'],D['4R_x'],D['4R_y'])
length4_ = get_lineSegments(coord4_[1], coord4_[0], coord4_[3], coord4_[2])
# print('4L__X:', coord4_[0],
#       '4R__X:', coord4_[1],
#       '4L__Y:', coord4_[2],
#       '4R__Y:', coord4_[3])
# print('length of line4_: ', length4_)

coord5_ = line_ellipse_intersection(slope6, mid_5x, mid_5y)
length5 = get_lineSegments(D['5L_x'],D['5L_y'],D['5R_x'],D['5R_y'])
length5_ = get_lineSegments(coord5_[1], coord5_[0], coord5_[3], coord5_[2])
# print('5L__X:', coord5_[0],
#       '5R__X:', coord5_[1],
#       '5L__Y:', coord5_[2],
#       '5R__Y:', coord5_[3])
# print('length of line5_: ', length5_)