import hopfion, plot, rescale

#decide kind of torus knot and file name
hopfion.select_torusknot()
file_name = hopfion.gamma + '_' + hopfion.delta + '_tk.csv'

#solve ansatz
Im_func, Re_func = hopfion.MakeAnsatz(hopfion.gamma, hopfion.delta)
plt_data = hopfion.solve(Im_func, Re_func)

#rescale data
rescale_data = rescale.rescale(plt_data[0], plt_data[1], plt_data[2])

#output
hopfion.output(rescale_data[3], file_name)

#plot
plot.data_plot(rescale_data[0], rescale_data[1], rescale_data[2])

#save
data_name = file_name.strip(".csv")
plt.savefig(data_name + ".png")

plt.show()