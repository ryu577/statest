# statest
A library for statistical estimation of the properties of various distributions.

## Installation
> pip install statest

## First use-case: estimate quantiles
The <a href="https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/quantile">R quantile function</a> has 9 estimators. The Python estimator in numpy (percentile) has only one (the seventh version in R). This library implements the remaining 8 methods.

```python
from statest.quantile.estimate import est_1, est_2, est_3,\
                                      est_4, est_5, est_6,\
                                      est_7, est_8, est_9
a = np.arange(15); q=0.8
quartile = est_4(a, q)
```

To measure the performance of the quantile estimation methods on various distributions, the library has a simulator. The simulations take about 20 minutes to run. The bias, variance and MSE are plotted for all the estimators. The data from the simulations is stored to disk in a folder called "sim_data" and the plots are saved to a folder called "plots".

```python
from statest.quantile.simulator.estimator_racetrack1 import RaceTrack
rt = RaceTrack("Normal")
rt.race()
```
The avaiable distributions are: Normal, LogNormal, LogLogistic, Weibull, Lomax and Exponential.

## Resources
Based on the paper: https://arxiv.org/abs/2201.01421
And the blog: https://towardsdatascience.com/hear-me-out-i-found-a-better-way-to-estimate-the-median-5c4971be4278
