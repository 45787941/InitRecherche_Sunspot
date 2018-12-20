# -*- coding: utf-8 -*-
"""
=========================================
Submaps and Cropping
=========================================

In this example we demonstrate how to get a submap of a map.
"""

##############################################################################
# Start by importing the necessary modules.

from __future__ import print_function, division

import astropy.units as u
from astropy.coordinates import SkyCoord
from sunpy.coordinates import frames

import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt
from sunpy.net.helioviewer import HelioviewerClient
from sunpy.map import Map

swap_map = Map(sunpy.data.sample.SWAP_LEVEL1_IMAGE)
print(swap_map.coordinate_frame)

hv = HelioviewerClient()
filepath = hv.download_jp2('2012/07/05 00:30:00', observatory='SDO', instrument='HMI', detector='HMI', measurement='continuum')
hmi = Map(filepath)
#print(list(hmi.coordinate_frame.observer))

#sc = SkyCoord(0*u.deg, 0*u.deg, 5*u.km, obstime="2012/07/05 00:30:00",frame="helioprojective", observer=SkyCoord(HeliographicStonyhurst(-10*u.deg, 2*u.deg)))
#print(sc)
#print(swap_map.data)

#print(swap_map.meta)

sc = SkyCoord(208.5*u.deg, -17.35*u.deg, 1*u.km,frame="heliographic_carrington", obstime="2012/07/05 00:30:00")
sc = sc.transform_to(frames.Helioprojective)

sc2 = SkyCoord(208.5*u.deg, -17.35*u.deg, 2*u.km,frame="heliographic_carrington", obstime="2012/07/05 00:30:00")
sc2 = sc.transform_to(frames.Helioprojective)

print(sc)

hmi = hmi.submap(sc, sc2)
hmi.peek(draw_limb=True, draw_grid=True)
plt.tight_layout(pad=1.00)
plt.show()
