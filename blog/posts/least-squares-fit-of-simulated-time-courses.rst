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


Parameter Values:

================ =============
Parameter        Value
================ =============
C(t=0)           0.1
N(t=0)           1.0
S(t=0)           0.0
k\ :sub:`n`      0.1
k\ :sub:`s`      0.1
 :math:`\beta`   0.05
 :math:`\alpha`  0.05
================ =============

Sim 1 r-values:

=========== ==========
 Parameter   Value
=========== ==========
r\ :sub:`0` 2.12038296
r\ :sub:`1` 0.23529426
r\ :sub:`2` 0.71800327
r\ :sub:`3` 0.70340588
r\ :sub:`4` 1.89093006
r\ :sub:`5` 0.32824214
r\ :sub:`6` 1.02039575
r\ :sub:`7` 1.77496177
r\ :sub:`8` 0.57991352
=========== ==========


Sim 2 r-values:

=========== ==========
 Parameter   Value
=========== ==========
r\ :sub:`0` 0.0
r\ :sub:`1` 2.70508608
r\ :sub:`2` 0.0
r\ :sub:`3` 1.33112558
r\ :sub:`4` 0.66875854
r\ :sub:`5` 0.96721998
r\ :sub:`6` 1.22867934
r\ :sub:`7` 0.64268857
r\ :sub:`8` 2.09978633
=========== ==========


Non-zero r\ :sub:`i`
----------------------------

.. image:: ../../images/least-squares-fit-of-simulated-time-courses/sim1_true.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod1_sim1_est.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod2_sim1_est.png
   :width: 32%

Estimated parameter errors - Model 1:

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


Zero-value r\ :sub:`i`
---------------------------

.. image:: ../../images/least-squares-fit-of-simulated-time-courses/sim2_true.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod1_sim2_est.png
   :width: 32%
.. image:: ../../images/least-squares-fit-of-simulated-time-courses/mod2_sim2_est.png
   :width: 32%



==================== ================== =================
Parameter            Deviation Model 1  Deviation Model 2
==================== ================== =================
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
==================== ================== =================


Discussion
----------

Fits are better for plate level :math:`\alpha` and :math:`\beta`.

If one or more cultures on a plate has a zero growth constant (r),
then fits are worse.

This may not be the case for different parameters (particularly ks).

We should also compare how well the independent model recovers rate
constants.
