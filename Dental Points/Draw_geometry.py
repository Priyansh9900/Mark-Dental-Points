from variables import *
from required_functions import *
from Read_data import *
import matplotlib.pyplot as plt
#plot seven points
x_coordinates = []
y_coordinates = []
for key in D.keys():
    if 'x' in key:
        x_coordinates.append(D[key])

    elif 'y' in key:
        y_coordinates.append(D[key])
plt.scatter(x_coordinates,y_coordinates,color='black',s=7,marker='v')

#plotting mid points
plt.scatter([M6_x,M4_x,M5_x],[M6_y,M4_y,M5_y],color='red',s=25,marker='v')
#plotting points 22mm away from 6M along line6
plt.scatter([M6_x+d*cos_slope6,M6_x-d*cos_slope6],[M6_y+d*sin_slope6,M6_y-d*sin_slope6],
            color='green',s=15,marker='v')
#plotting C' and C"
plt.scatter([c_x,c__x], [c_y,c__y], color='red',s=25,marker='+')
#plotting intersection points of ellipse and line 4,5
plt.scatter([coord_4[0],coord_4[1],coord_5[0],coord_5[1]],[coord_4[2],coord_4[3],coord_5[2],coord_5[3]],
            color='blue',s=50,marker='+')


plt.plot(x_per,y_per,color='green',linewidth=1)
plt.plot([D['6L_x'],D['6R_x']],[D['6L_y'],D['6R_y']],color='blue',linewidth=1)
plt.plot(x_par,y_par,color='purple',linewidth=1)
plt.plot(x_5,y_5,color='orange',linewidth=1)
plt.plot(x_4,y_4,color='yellow',linewidth=1)
plt.plot(x_5,y_5_par,color='purple',linewidth=1)
plt.plot(x_4,y_4_par,color='purple',linewidth=1)



ax = plt.gca()
plot_ellipse(ax, center=(M6_x,M6_y), width=d, height=M6_C__, phi=ellipse_angle, color='red',lw=1)

plt.imshow(img_test)
plt.show()