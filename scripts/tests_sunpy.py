from sunpy.net.helioviewer import HelioviewerClient
import matplotlib.pyplot as plt
from astropy.units import Quantity
from sunpy.map import Map

hv = HelioviewerClient()
filepath = hv.download_jp2('2012/07/05 00:30:00', observatory='SDO', instrument='HMI', detector='HMI', measurement='continuum')
hmi = Map(filepath)
xrange = Quantity([200, 550], 'arcsec')
yrange = Quantity([-400, 200], 'arcsec')
hmi.submap(xrange, yrange).peek()
