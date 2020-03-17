from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

from rescale import select_file, open_file

def data_plot(x_plot, y_plot, z_plot):

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.plot(x_plot, y_plot, z_plot, c='blue', linewidth=0, marker='o')


if __name__ == "__main__":
    file_name = select_file()
    data = open_file(file_name)

    data_plot(data[0], data[1], data[2])
    data_name = file_name.strip(".csv")
    plt.savefig(data_name + ".png")

