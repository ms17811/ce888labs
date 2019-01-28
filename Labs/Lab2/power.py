from numpy import array
from matplotlib import pyplot
from statsmodels.stats.power import TTestIndPower




effect_sizes = array([0.2, 0.5, 0.8])
sample_sizes = array(range(5, 100))


analysis = TTestIndPower()
analysis.plot_power(dep_var='nobs', nobs=sample_sizes, effect_size=effect_sizes)
pyplot.show()
