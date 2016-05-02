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

Prarameter Estimation
---------------------







Possible Solutions
------------------

- Add extra bounds and constriaints

  - For the slowest growers, use r\ :sub:`i`\'s from independent fits
    as maximum bounds in competition fits.

    + Requires extra computation.

  - Consider bounding k\ :sub:`n`.

    + Not clear how to do so without measurement.

- Randomize starting conditions.

  - Requries much extra computation.
