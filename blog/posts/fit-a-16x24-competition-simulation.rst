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
