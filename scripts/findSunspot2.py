import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord
from sunpy.net.helioviewer import HelioviewerClient
import matplotlib.pyplot as plt
from astropy.units import Quantity
from sunpy.map import Map
from sunpy.coordinates import frames
import astropy.wcs as wcs

import sunpy.map
import sunpy.data.sample


hv = HelioviewerClient()
filepath = hv.download_jp2('2012/07/05 01:59:10', observatory='SDO', instrument='HMI', detector='HMI', measurement='continuum')
hmi = Map(filepath)

sc1 = SkyCoord((208.5+(7.64/2))*u.deg, (-17.37+(7.64/2))*u.deg, frame="heliographic_carrington", obstime="2012/07/05 01:59:10")
sc = SkyCoord((208.5-(7.64/2))*u.deg, (-17.37-(7.64/2))*u.deg, frame="heliographic_carrington", obstime="2012/07/05 01:59:10")
print(sc)

print((208.5-(7.64/2))*u.deg, (-17.37-(7.64/2))*u.deg)

sc = sc.transform_to(frames.Helioprojective)
sc1 = sc1.transform_to(frames.Helioprojective)

print(hmi.world_to_pixel(sc, 1))

#hmi = hmi.submap(sc, sc1)

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
