import pandas as pd
import cv2
csv_data = pd.read_csv("C:\\Users\\HP\\PycharmProjects\\Dental Points\\000425_Initial_Mandibular.csv")
img_test = cv2.imread("C:\\Users\\HP\\PycharmProjects\\Dental Points\\000425_Initial_Mandibular.stl.png")
data_columns_list = csv_data.columns.to_list()
data_columns_new_list = []
for i in range(data_columns_list.index('6L_x'),len(data_columns_list)):
    new_list = data_columns_list[i]
    data_columns_new_list.append(new_list)
csv_new_data = csv_data[data_columns_new_list]
row_dict = csv_new_data.loc[0]
data_row_new_list = []
for l in range(len(data_columns_new_list)):
    data_row_new_list.append(row_dict[l])
data_dict = dict(zip(data_columns_new_list,data_row_new_list))
D = data_dict
