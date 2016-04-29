.. title: Least squares fit of simulated time-courses
.. slug: least-squares-fit-of-simulated-time-courses
.. date: 2016-04-28 18:33:17 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text


Outline
-------

Here I look at least squares fits of the CANS model to simulated CANS
data. I do this for two simulations of a 3x3 plate. In the first all
cultures have non-zero growth constants (r\ :sub:`i`); in the second
some of the cultures have zero growth constant. Of the three curves
plotted, only the amount of cells (blue) is used to recover
parameters. Simulations contain 21 time-points. This is an attempt to
keep fitting relevent to the data we will be using.


In the simulations rate constants are drawn from a N(1, 1)
distribution. I set other parameters manually.

I compare the perfomance of two fitting approaches. The first allows
constants for the secretion of signal by cells :math:`(\beta)` and the
effect of signal on cells :math:`(\alpha)` to vary beteen cultures; the
second does not.

The fixing of other parameters is sumarised below.

Plate level:

- C(t=0) - Initial cell amount
- N(t=0) - Initial nutrient amount
- S(t=0) - Initial signal amount
- k\ :sub:`n` - Nutrient diffusion constant
- k\ :sub:`s` - Signal diffusion constant

Culture level:

- r\ :sub:`i` - Growth constants


Parameter Values and Initial Guesses:

================ ============= ==============
Parameter        Value         Initial guess
================ ============= ==============
C(t=0)           0.1           0.2
N(t=0)           1.0           0.2
S(t=0)           0.0           0.0
k\ :sub:`n`      0.1           0.05
k\ :sub:`s`      0.1           0.15
:math:`\beta`    0.05          0.05
:math:`\alpha`   0.05          0.05
r                (see below)   1.0
================ ============= ==============

=========== ============= =============
 Parameter   Value Sim 1   Value Sim 2
=========== ============= =============
r\ :sub:`0` 2.12038296    0.0
r\ :sub:`1` 0.23529426    2.70508608
r\ :sub:`2` 0.71800327    0.0
r\ :sub:`3` 0.70340588    1.33112558
r\ :sub:`4` 1.89093006    0.66875854
r\ :sub:`5` 0.32824214    0.96721998
r\ :sub:`6` 1.02039575    1.22867934
r\ :sub:`7` 1.77496177    0.64268857
r\ :sub:`8` 0.57991352    2.09978633
=========== ============= =============


Non-zero r\ :sub:`i`
----------------------------

Plots of simulation 1 and fitting:

.. image:: ../../images/least-squares-fit-of-simulated-time-courses/sim1_true.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod1_sim1_est.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod2_sim1_est.png
   :width: 32%

Deviations of fitted parameters:

==================== ================== ==================
Parameter            Deviation Model 1  Deviation Model 2
==================== ================== ==================
C(t=0)               0.0020385744       4.21348985868E-007
N(t=0)               0.0173966107       1.35868377105E-006
S(t=0)               0.0256967688       7.27393393862E-006
k\ :sub:`n`          0.0034546308       1.53308832754E-007
k\ :sub:`s`          0.0065764685       2.6762262845E-006
:math:`\beta`                           0.0094500157
:math:`\alpha`                          0.0116516464
:math:`\beta` (MAD)  0.098591232
:math:`\alpha` (MAD) 0.0322358689
r (MAD)              0.0338617287       4.29413653051E-006
==================== ================== ==================

Here we find that parameter fitting is more accurate for model 2 where
:math:`\alpha` and :math:`\beta` are plate level.

Zero-value r\ :sub:`i`
---------------------------

Plots of simulation 2 and fitting:

.. image:: ../../images/least-squares-fit-of-simulated-time-courses/sim2_true.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod1_sim2_est.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod2_sim2_est.png
   :width: 32%

Deviations of fitted parameters:

==================== ================== ==================
Parameter            Deviation Model 1  Deviation Model 2
==================== ================== ==================
C(t=0)               0.0028789924       0.0282316976
N(t=0)               0.0282431081       0.1812336171
S(t=0)               0.1646590344       0
k\ :sub:`n`          0.0051864629       0.2120190497
k\ :sub:`s`          0.1                0.05187543
:math:`\beta`                           0.05
:math:`\alpha`                          0.05
:math:`\beta` (MAD)  0.2544472169
:math:`\alpha` (MAD) 0.2208869765
r (MAD)              0.1572653337       0.6894003751
==================== ================== ==================

Both models have more trouble fitting plates where some cultures have
zero growth constant. Model 1 finds a local minimum where diffusion
constant k\ :sub:`s` is zero and :math:`\beta` and :math:`\alpha`
vary a lot between cultures; model 2 finds a local minimum where
:math:`\beta` and :math:`\alpha` are both zero and no signal is ever
produced. Estimates of
growth constant (r) are actually worse in model 2 where there are
fewer free parameters. It may be possible to get a better fit with
model 2 using different parameter guesses.

Fits would likely be better for different true parameter values. In
particular signal diffusion (controlled by k\ :sub:`s`) occurs quickly
in the simulations such that levels of signal are very similar in all
cultures.

Summary
----------

In the first example, with non-zero growth constants, fits are better
for plate level :math:`\beta` and :math:`\alpha`.

Where there are zero value growth constants, both models have trouble
producing accurate fits. In the example studied, fits with plate level
:math:`\beta` and :math:`\alpha` were actually worse, although this may not
be true in general. We could determine this with simulations.

Better fits may be obtained using different starting parameters or in
cases where true parameters (besides r) are different.

Parameter estimates may be better of worse for larger plates and we
should check this. If we
let :math:`\beta` and :math:`\alpha` vary from culture to culture we have many
more free parameters. If we fix :math:`\beta` and :math:`\alpha` at the plate
level then we have more information to determine parameters.

We should also compare how well the independent model recovers growth
constants.
