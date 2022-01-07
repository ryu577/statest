# This is for comparing new bias removal and variance minimizing strategy.
from statest.quantile.estimate import *
from statest.quantile.expon_based_estimators \
    import prcntl, prcntl2, prcntl3, prcntl4, prcntl5, prcntl6, prcntl7
from statest.quantile.some_distributions import *
from statest.quantile.perf_measurer import PrcntlEstPerfMeasurer
import numpy as np
import matplotlib.pyplot as plt


def make_lines(ax1, ax2, ax3, ax4):
    ax1.axhline(0, color="black")
    ax1.axvline(0.5, color="black")
    ax2.axhline(0, color="black")
    ax2.axvline(0.5, color="black")
    ax3.axhline(0, color="black")
    ax3.axvline(0.5, color="black")
    ax4.axhline(0, color="black")
    ax4.axvline(0.5, color="black")
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()


rvs_fn = rvs_fn6
ppf_fn = ppf_fn6
distr_name = "Fisk"
qs = np.arange(0.05, 0.8, 0.05)

prcntl_estimators = [prcntl, prcntl6,
                     prcntl7, est_4, est_9]

names = ["no_bias_1", "no_bias_2",
         "no_bias_2_two_trms",
         "r_strat4", "r_strat9"]

prf_results = []

fig1, ax1 = plt.subplots(1, 1)
fig2, ax2 = plt.subplots(1, 1)
fig3, ax3 = plt.subplots(1, 1)
fig4, ax4 = plt.subplots(1, 1)

for ix in range(len(prcntl_estimators)):
    prcntl_est = prcntl_estimators[ix]
    name = names[ix]
    prf1 = PrcntlEstPerfMeasurer(n=15,
                                 rvs_fn=rvs_fn,
                                 ppf_fn=ppf_fn,
                                 qs=qs,
                                 prcntl_estimator=prcntl_est,
                                 prll_wrlds=30000)
    prf1.simulate()
    prf_results.append(prf1)
    ax1.plot(qs, prf1.u_errs, label="Bias for " + name)
    ax2.plot(qs, prf1.u_stds, label="Standard deviation for " + name)
    ax3.plot(qs, prf1.u_medians, label="DelMedian for " + name)
    ax4.plot(qs, prf1.u_mses, label="MSE for " + name)
    print("###############")
    print("Finished processing " + name)
    print("###############")

make_lines(ax1, ax2, ax3, ax4)
plt.xlabel("Percentile (q)")
plt.show()
