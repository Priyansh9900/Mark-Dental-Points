from read_data import read_data
from draw_geometry import plot

CSV_LOCATION = "C:\\Users\\HP\\PycharmProjects\\Dental Points\\000425_Initial_Mandibular.csv"
IMAGE_LOCATION = "C:\\Users\\HP\\PycharmProjects\\Dental Points\\000425_Initial_Mandibular.stl.png"


def main():
    data_dict = read_data(CSV_LOCATION)
    plot(data_dict, IMAGE_LOCATION)


if __name__ == '__main__':
    main()
