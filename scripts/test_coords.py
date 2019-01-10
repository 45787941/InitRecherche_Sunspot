# -*- coding: utf-8 -*-
from __future__ import print_function, division

import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord
from sunpy.net.helioviewer import HelioviewerClient
import matplotlib.pyplot as plt
from astropy.units import Quantity
from sunpy.map import Map
import sunpy.data.sample
from sunpy.coordinates.frames import HeliographicStonyhurst

hv = HelioviewerClient()
filepath = hv.download_jp2('2012/07/05 00:30:00', observatory='SDO', instrument='HMI', detector='HMI', measurement='continuum')
hmi = Map(filepath)

print(hmi.world_to_pixel(SkyCoord(1 * u.rad, 1 * u.rad, 0*u.AU)))
#print(hmi.world_to_pixel(SkyCoord(1 * u.carrington, 0 * u.carrington, 0*u.AU)))
#print(hmi.world_to_pixel(SkyCoord(lon=208.5*u.deg, lat=-17.35*u.deg, radius=2*u.km,frame="heliographic_carrington", obstime='2012/07/05 00:30:00')))

#top_right = SkyCoord(0*u.arcsec, 100 * u.arcsec)
#bottom_left = SkyCoord(100 * u.arcsec, 100 * u.arcsec)
#hmi = hmi.submap(bottom_left, top_right)

# RESTE A FAIRE
# CALCUL SCORE DE CHAQUE METHODE
# METHODES : LEVEL SET + K-MEAN
# CROP DANS IMAGE
# RECUPERATION DONNEES DEPUIS LE SITE
