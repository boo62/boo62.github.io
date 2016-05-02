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

True parameter values and starting points:

================ ============= ==============
Parameter        Truth         Start
================ ============= ==============
C(t=0)           0.01          0.005
N(t=0)           1.0           0.8
k\ :sub:`n`      0.0 - 1.0     0.05
r                ~N(1, 1)      1.0
================ ============= ==============

Deviations of estimated prarameters from truth for independent and
competition fits for each k\ :sub:`n`.

==================== ================== ===================
k\ :sub:`n` = 0.00   Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0055191992       0.0401555437
N(t=0)               0.0407384612       0.3378106649
k\ :sub:`n`          na                 2.6926506252
r (MAD)              0.190852862 *      0.4386880843
==================== ================== ===================

[*] We shoud achieve quite a good fit of the independent model when k\
:sub:`n` is zero. The fairly poor result here suggests that the
stopping criteria may have been too lax or that we did not have enough
timepoints in the 'data'. See also the r comparison table below.

==================== ================== ===================
k\ :sub:`n` = 0.02   Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.005419919        0.0131022281
N(t=0)               0.1807962527       0.2453326719
k\ :sub:`n`          na                 2.9841599939
r (MAD)              0.1826788404       0.3903167822
==================== ================== ===================

==================== ================== ===================
k\ :sub:`n` = 0.04   Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0099258493       0.0021941877
N(t=0)               0.194596125        0.0575789015
k\ :sub:`n`          na                 1.3219260354
r (MAD)              0.4708014932       0.5628802379
==================== ================== ===================

==================== ================== ===================
k\ :sub:`n` = 0.06   Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0083602458       0.004763655
N(t=0)               0.296572103        0.0820861874
k\ :sub:`n`          na                 0.0998595903
r (MAD)              0.1802694093       0.6775813612
==================== ================== ===================

==================== ================== ===================
k\ :sub:`n` = 0.08   Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0098788302       0.0068623485
N(t=0)               0.2818536121       1 *
k\ :sub:`n`          na                 4.2788862717
r (MAD)              0.633607027        0.3568786201
==================== ================== ===================

[*] Here N(t=0) = 0. This suggests that there is either an error in my
code or that I am very far off the correct minimum. We may need more
iterations and stricter stopping criteria or randomized starting
points.

==================== ================== ===================
K\ :sub:`n` = 0.10   Absolute Deviation
-------------------- --------------------------------------
Parameter            Independent        Competition
==================== ================== ===================
C(t=0)               0.0097751934       0.009844427
N(t=0)               0.4692137739       0.3906327995
k\ :sub:`n`          na                 0.2757623871
r (MAD)              0.4686886906       0.6644247129
==================== ================== ===================

The table below looks in more detail at estimated growth constants for
several cultures. Values are rounded to 3.d.p.

============= ===== ============ ===== ============ ===== ============ ===== ============ ===== ============ ===== =========== ======
\                   k\ :sub:`n` = 0.00 k\ :sub:`n` = 0.02 k\ :sub:`n` = 0.04 k\ :sub:`n` = 0.06 k\ :sub:`n` = 0.08 k\ :sub:`n` = 0.10
------------------- ------------------ ------------------ ------------------ ------------------ ------------------ ------------------
Parameter     True  Inde         Comp  Inde         Comp  Inde         Comp  Inde         Comp  Inde         Comp  Inde         Comp
============= ===== ============ ===== ============ ===== ============ ===== ============ ===== ============ ===== =========== ======
r\ :sub:`103` 1.149 1.398        1.296 1.279        1.371 1.100        1.150 1.218        1.017 1.390        1.255 1.168       1.027
r\ :sub:`104` 0.0   0            0.386 0.177        0.377 0.752        0.801 0.183        0.977 0.275        0     0.513       0.970
r\ :sub:`105` 0.0   0            0.376 0.177        0.315 0.753        0.750 0.183        0.969 0.275        0     0.513       0.957
r\ :sub:`106` 2.598 2.004        1.274 2.047        1.477 1.521        1.331 2.591        1.045 5.017        1.759 4.378       1.095
============= ===== ============ ===== ============ ===== ============ ===== ============ ===== ============ ===== =========== ======


Discussion
----------




In the last blog post, using the CNS model, fits of C and N were good
compared to fits of S. We therefore beleived that removing S from the
model and just studying C and N would produce good estimates of
parameters in a shorter time. However, due to the different shape of
CN and CNS growth curves, estimates may in fact be less accurate. We
will verify this using smaller 3x3 plates as we did in CNS fits.

Surprisingly, the independent model is not fitting well to data
generated with the competition model with kn = 0. Is there an error
somewhere? Is the stopping criteria too lax?

The independent model finds the same minimum r value for
all zero growth cultures.



Possible Solutions
------------------

* Would more observations imporve results?

  - Perhaps I do not have enough timepoints during the growth phase or
    at the tail.

* Add extra bounds and constriaints.

  - Find zero growers from independent fits (all have the same minimum
    r value) and constrain these to be zero in competition fits.

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
