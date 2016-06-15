.. title: Fits of overlapping 5x5 zones
.. slug: fits-of-overlapping-5x5-zones
.. date: 2016-06-15 13:14:58 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Procedure
---------

I took cell measurement data of overlapping 5x5 zones with top-left
coordinates (7, 13) and (9, 15) from plate 15 with coordinates
starting (0, 0). I guessed the initial amount of nutrients from final
cell amounts. I used a 10x11x11 grid of guesses for C_0, kn,
and r. C_0 guesses were on a logarithmic scale whereas kn and r
guesses were ona linear scale (see code below). I used the same r
guess for all cultures in a single fit.

Code for grid of guesses:

.. code-block:: python
  :linenos:

  import numpy as np

  C_0s = np.logspace(-10, -1, 10)
  kns = np.linspace(0.0, 10.0, 11)
  rs = np.linspace(25.0, 75.0, 11)

I made bounds large in the hope that solutions would not have any
estimates located at a boundary. I fit the competition model to both
zones using each of the 1000 initial guesses. The table bw

.. image:: ../../images/fits-of-overlapping-5x5-zones/est_table.png

Unfortunately, agreement of parameter estimates between the two zones
is fairly poor

Estimates 440 and 803 produced N_0 guesses at the lower? bounds for
the (7, 13) zone.
