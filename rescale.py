import numpy as np
import pandas as pd

from hopfion import output


def open_file(csv_file):
    d = pd.read_csv(csv_file)

    old_x = d["0"]
    old_y = d["1"]
    old_z = d["2"]

    return old_x, old_y, old_z

def rescale(x1, y1, z1):

    new_x = []
    new_y = []
    new_z = []
    new_data = []

    for i in range(len(z1)):
        if z1[i]**2 < 4**2:
            new_z.append(z1[i])
        elif 4**2 <= z1[i]**2:
            if z1[i] > 0:
                new_z.append(z1[i]*np.sin((2 + z1[i])*np.pi/12))
            else:
                new_z.append(z1[i]*np.sin((2 + z1[i]*-1)*np.pi/12))

    for i in range(len(z1)):
        new_x.append(x1[i])
        new_y.append(y1[i])
        new_data.append([new_x[i], new_y[i], new_z[i]])

    return new_x, new_y, new_z, new_data

def select_file():
    return input('file name :')

if __name__ == '__main__':

    file_name = select_file()
    ax, ay, az = open_file(file_name)

    rescale_data = rescale(ax, ay, az)
    output(rescale_data[3], 'new_'+file_name)
