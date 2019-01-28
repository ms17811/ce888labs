import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as npr


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	print((df.columns))
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')

	data = df.values.T[1]
	
        	
	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('current Fleet') 
	axes.set_ylabel('new Fleet')

	sns_plot2.savefig("histogram.png",bbox_inches='tight')
	sns_plot2.savefig("histogram.pdf",bbox_inches='tight')

