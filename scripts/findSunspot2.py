import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord
from sunpy.net.helioviewer import HelioviewerClient
import matplotlib.pyplot as plt
from astropy.units import Quantity
from sunpy.map import Map

import sunpy.map
import sunpy.data.sample

hv = HelioviewerClient()
filepath = hv.download_jp2('2012/07/05 00:30:00', observatory='SDO', instrument='HMI', detector='HMI', measurement='continuum')
hmi = Map(filepath)

sc = SkyCoord(208.5*u.deg, -17.37*u.deg, frame="heliographic_carrington", obstime="2012/07/05 00:30:00")
print(sc)
hmi = hmi.submap([2400,1400]*u.pixel,[3000,1750]*u.pixel)

fig = plt.figure()
# Provide the Map as a projection, which creates a WCSAxes object
ax = plt.subplot(projection=hmi)

im = hmi.plot()

# Prevent the image from being re-scaled while overplotting.
ax.set_autoscale_on(False)

#xc = [0,100,1000] * u.arcsec
#yc = [0,100,1000] * u.arcsec
#coords = SkyCoord(xc, yc, frame=smap.coordinate_frame)
#p = ax.plot_coord(coords, 'o')

# Set title.
ax.set_title('Custom plot with WCSAxes')

plt.show()
