.. title: Fit a 16x24 Competition Simulation
.. slug: fit-a-16x24-competition-simulation
.. date: 2016-05-14 14:12:16 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Outline
=======

This time we fit the competition model to plates also simulated using
the competition model with kn > 0.

Plan
====

Simulation
----------

We want to fit a full plate simulation of the competition model using
the competition model. We use some information that we will not have
for real data. For instance, we use the same N(5, 3) distribution to
genereate rate constants for the simulation and initial guesses for
fitting. We aim to determine sensible stopping criteria for the
minimizer, how many initial parameter guesses we will need to make to
find the correct minimum and how long fitting will take.

Becuase there is a large number of cultures on the plate (384), one
set of random growth constants should do for simulated data. For 3x3
plates, we have :doc:`previously shown <use-inde-est-as-comp-guess>`
that, using enough random initial guesses of growth constants, we can
achieve good fits over a range of kn values. Therefore, we will just
use one value for kn and one simulated data set.


Real Data
---------

We will not know how realistic values of test parameters are, or
whether the model can even produce a good fit, until we try fitting
real data. If, in fits of real data, some parameters are much smaller
than others then we may have to scale them to be of roughly the same
order of magnitude in order for the minimizer to work. We may also
have to use many more initial parameter guesses from different
distributions to achieve a first fit. After this we will have ball
park values which we can use.

To reduce computation time we will first fit a central 5x5 or 4x4
section of a real plate. To reduce errors due to not fitting the
entire plate, we will discard edge cultures and assess the inner 3x3
or 2x2 fit. We can use the results of this fitting to calibrate for
full plate fitting.


Results
=======

I simulated a full 16x24 plate and generated 100 sets of random
~N(5, 3) guesses for rate constants r which were annotated and saved
to file.

2x1 Fits
--------

I took the parameters from a 2x1 zone of the full plate. Coordiates of
the top left culture of the zone are (7, 13) with the origin of the
plate being (0, 0). I used these parameters and the competition model
to simulate new amounts as if the zone was not part of the larger
plate. I fitted the competition model to the simulations using ten of
the sets of random r guesses as initial guesses. To be consistant I
used the r guesses corresponding to the zone.

Effect of initial guess of kn
+++++++++++++++++++++++++++++

At first I used an initial guess for kn of 0.0. This produced poor
fits.

.. Plots of kn = 0 guess fits

Contrary to :doc:`previous findings <use-inde-est-as-comp-guess>`,
where different parameters were used for simulating data, the initial
guess of kn is importatant. A value of kn = 0.1 as an initial guess
improves fits (the true value is 0.2).

.. Plots of kn = 0.1 guess fits

I also made fits using a uniform guess for rate constants of r =
5.0 (the true distribution mean).

.. Uinform kn = 0.0
.. Uniform plot for kn = 0.1

Discussion of parameters and rescaling.

Stopping Criteria
+++++++++++++++++

To fit I used the `L-BFGS-B method`_ from scipy.optimize.minimize.

For each initial guess, I stopped the minimization over a logorithmic
range of factr: 10e14, 10e13, ..., 10e0, where ftol = factr*eps. Note
that documentation for the L-BFGS-B method is currently inaccurate
(19/05/2016) and factr must be passed through ftol (`issue report
<https://github.com/scipy/scipy/issues/5231>`_). To reduce computation
time, I used estimates at each stopping point as the initial guess for
the next lowest factr (low factr being more accurate).

.. _L-BFGS-B method: http://docs.scipy.org/doc/scipy-0.17.0/reference/optimize.minimize-lbfgsb.html#optimize-minimize-lbfgsb

The transition for a succesful fit (init_guess_5) is shown below.

.. Transition plots

Once I have data for a full plate fit I should know how to set factr
in order to reduce fitting time.

5x5 Fits
--------

I did the same for a 5x5 zone with coordinates (6, 11) using only
kn = 0.1 as an initial guess.

.. A good example showing transition with factr from bad to good and
   best.

.. A bad example, ideally uniform if this is bad


16x24 Fits
----------

Currently running on the yzer machine.
