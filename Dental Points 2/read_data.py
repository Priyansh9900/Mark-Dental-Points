import pandas as pd

CSV_LOCATION = "C:\\Users\\HP\\PycharmProjects\\Dental Points\\000425_Initial_Mandibular.csv"
IMAGE_LOCATION = "C:\\Users\\HP\\PycharmProjects\\Dental Points\\000425_Initial_Mandibular.stl.png"

def read_data(csv_location):
    csv_data = pd.read_csv(csv_location)
    data_columns_list = csv_data.columns.to_list()
    start_index = data_columns_list.index('6L_x')
    data_columns_new_list = data_columns_list[start_index:]
    csv_new_data = csv_data[data_columns_new_list]
    row_dict = csv_new_data.loc[0]
    data_dict = dict(zip(data_columns_new_list, row_dict))
    return data_dict
D = read_data(CSV_LOCATION)