.. title: Fitting of full plate (16x24) competition model simulations
.. slug: fitting-of-full-plate-16x24-competition-model-simulations
.. date: 2016-05-02 13:03:19 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Outline
-------

Here I fit full plate simulations of the competition only model,
varying nutrient diffusion constant k\ :sub:`n`, and asses how well
parameters are recovered.

The Competition Model
---------------------


The competition model is goverened by the following ODEs:

.. math::

   \begin{align}
   \frac{dC_{i}}{dt}& = r_{i}N_{i}C_{i}\\
   \frac{dN_{i}}{dt}& = - r_{i}N_{i}C_{i} - k_{n}\sum_{j \epsilon \delta_i}(N_{i} - N_{j}).
   \end{align}

For a full 16x24 plate we have 384 r\ :sub:`i`\'s and three additional
parameters:

C(t=0),
N(t=0),
and
k\ :sub:`n`\.

In the independent model we lose k\ :sub:`n` and the second term in
:math:`\dot{N}`\ vanishes.

Parameter Estimation
---------------------

Parameter Values and Initial Guesses:

================ ============= ==============
Parameter        True Value    Initial guess
================ ============= ==============
C(t=0)           0.01          0.005
N(t=0)           1.0           0.8
k\ :sub:`n`      0.0 - 1.0     0.05
r                ~N(1, 1)      1.0
================ ============= ==============

Deviations of estimated prarameters from truth for independent and
competition fits for each k\ :sub:`n`.

==================== ================== ===================
k\ :sub:`n` = 0.0    Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0055191992       0.0401555437
N(t=0)               0.0407384612       0.3378106649
k\ :sub:`n`          na                 2.6926506252
r (MAD)              0.190852862        0.4386880843
==================== ================== ===================

==================== ================== ===================
k\ :sub:`n` = 0.2    Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.005419919        0.0131022281
N(t=0)               0.1807962527       0.2453326719
k\ :sub:`n`          na                 2.9841599939
r (MAD)              0.1826788404       0.3903167822
==================== ================== ===================

============= ============ ============ ============ ============ ============
\                          kn = 0.2                  kn = 0.4
-------------------------- ------------------------- -------------------------
Parameter     True         Inde         Comp         Inde         Comp
============= ============ ============ ============ ============ ============
r\ :sub:`103` 1.1486959982 1.2793945487 1.3709772711 1.0996377636 1.1496507404
r\ :sub:`104` 0.0          0.1771394709 0.3769809764 0.7524952086 0.8008519751
r\ :sub:`105` 0.0          0.1771394709 0.3146762171 0.7524952086 0.7500936007
r\ :sub:`106` 2.5982502954 2.0474094037 1.4770082394 1.5207112715 1.3310899556
============= ============ ============ ============ ============ ============

==================== ================== ===================
k\ :sub:`n` = 0.4    Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0099258493       0.0021941877
N(t=0)               0.194596125        0.0575789015
k\ :sub:`n`          na                 1.3219260354
r (MAD)              0.4708014932       0.5628802379
==================== ================== ===================

==================== ================== ===================
k\ :sub:`n` = 0.6    Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0083602458       0.004763655
N(t=0)               0.296572103        0.0820861874
k\ :sub:`n`          na                 0.0998595903
r (MAD)              0.1802694093       0.6775813612
==================== ================== ===================

==================== ================== ===================
k\ :sub:`n` = 0.8    Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0098788302       0.0068623485
N(t=0)               0.2818536121       1 *
k\ :sub:`n`          na                 4.2788862717
r (MAD)              0.633607027        0.3568786201
==================== ================== ===================

[*] Suggests either that there is an error in my code or that I am not
finding the correct minimum.

==================== ================== ===================
K\ :sub:`n` = 1.0    Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)
N(t=0)
k\ :sub:`n`          na
r (MAD)
==================== ================== ===================

Discussion
----------

Surprisingly, the independent model is not fitting well to data
generated with the competition model with kn = 0. Is there an error
somewhere? Is the stopping criteria to loose?


The independent model find the same r value for all zero growth cultures.



Possible Solutions
------------------

* Would longer observation times imporve results?

* Add extra bounds and constriaints.

  - For the slowest growers, use r\ :sub:`i`\'s from independent fits
    as maximum bounds in competition fits.

    + Requires extra computation.

  - Consider bounding k\ :sub:`n`.

    + Not clear how to do so without measurement.

* Randomize starting conditions.

  - Requries much extra computation.

* Would Bayesian fitting be more accurate?

* Use a different model.


I will try some of these solutions for 2x2 and 3x3 plates containing
a proportion of cultures with zero growth constant.


As the code is more stable now it might be a good idea to start
writing some tests.
