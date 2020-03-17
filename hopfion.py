from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp

from scipy import optimize


def MakeAnsatz(a,b):

    global x, y, z, r, Z1, Z0

    x = sp.Symbol('x', real = True)
    y = sp.Symbol('y', real = True)
    z = sp.Symbol('z', real = True)
    r = sp.Symbol('r', real = True)

    Z1 = 2 * (x - sp.I * y)
    Z0 = 1 - r*r - 2 * sp.I * z


    fun = Z1**int(a) + Z0**int(b)
    Im = sp.im(fun)
    Re = sp.re(fun)
    Im_xyz = Im.subs(r**2 , x**2+y**2+z**2)
    Re_xyz = Re.subs(r**2 , x**2+y**2+z**2)

    return Im_xyz, Re_xyz

def solve(Im_function, Re_function):

    x_range = np.linspace(-10, 10, 10)
    y_range = np.linspace(-10, 10, 10)
    z_range = np.linspace(-10, 10, 400)

    x_plot = []
    y_plot = []
    z_plot = []

    data = []
    count = 0


    def solve_function(initial_value):

        Im_return = Im_xy.subs([(x, initial_value[0]), (y, initial_value[1])])
        Re_return = Re_xy.subs([(x, initial_value[0]), (y, initial_value[1])])

        return [Im_return, Re_return]

    for z_value in z_range:
        Im_xy = Im_function.subs(z, z_value)
        Re_xy = Re_function.subs(z, z_value)

        for x_value in x_range:
            for y_value in y_range:
                try:
                    sol = optimize.root(solve_function, [x_value, y_value], method='broyden2')

                    if sol.success:
                        x_plot.append(sol.x[0])
                        y_plot.append(sol.x[1])
                        z_plot.append(z_value)
                        data.append([sol.x[0], sol.x[1], z_value])

                    count += 1
                    print(float(count/(len(x_range)*len(z_range)*len(y_range))*100), "%")

                except:
                    count += 1
                    print(float(count/(len(x_range)*len(z_range)*len(y_range))*100), "%")
                    pass

    return x_plot, y_plot, z_plot, data

def output(data, file_name):
    data_file = pd.DataFrame(data)
    data_file.to_csv(file_name)

def select_torusknot():

    global gamma
    global delta

    while True:
        print('Set torus knot -> (a,b)-torus knot *(a > b)')

        gamma = input('a :')
        delta = input('b :')

        if gamma <= delta:
            print('Please select \'a\' more than \'b\'.')
        else:
            break


if __name__ == '__main__':

    select_torusknot()
    file_name = gamma + '_' + delta + '_tk.csv'
    Im_func, Re_func = ansatz.MakeAnsatz(gamma, delta)
    plt_data = solve(Im_func, Re_func)
    output(plt_data[3], file_name)
