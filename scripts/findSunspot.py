import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord
from sunpy.net.helioviewer import HelioviewerClient
import matplotlib.pyplot as plt
from astropy.units import Quantity
from sunpy.map import Map


import sunpy.map
import sunpy.data.sample
import sunpy.map.mapbase

hv = HelioviewerClient()
filepath = hv.download_jp2('2012/07/05 00:30:00', observatory='SDO', instrument='HMI', detector='HMI', measurement='continuum')
hmi = Map(filepath)

#            corners = u.Quantity([bottom_left, bottom_right, top_left, top_right])
#        coord = SkyCoord(corners, frame=self.coordinate_frame)
#    pixel_corners = self.world_to_pixel(coord)
#a =SkyCoord(200*u.arcsec,500*u.arcsec,frame=hmi.coordinate_frame)
#b =SkyCoord(-400*u.arcsec,200*u.arcsec,frame=hmi.coordinate_frame)
#hmi = hmi.submap([2400,1400]*u.pixel,[3000,1750]*u.pixel)
#print(a)
#bottom_left = u.Quantity(a).to(u.pixel) #hmi.world_to_pixel(a,1)
#top_right = u.Quantity(b).to(u.pixel)#hmi.world_to_pixel(b,1)
#print(bottom_left)
#hmi = hmi.submap(bottom_left,top_right)
#top_right = hmi.wcs_world2pix(-1000*u.arcsec, -1000 * u.arcsec, frame=hmi.coordinate_frame)
#bottom_left = SkyCoord(1000 * u.arcsec,  1000* u.arcsec, frame=hmi.coordinate_frame)
coordinate = SkyCoord(200*u.arcsec,500*u.arcsec, frame=hmi.coordinate_frame)
native_frame = coordinate.transform_to(hmi.coordinate_frame)
lon, lat = u.Quantity(self._get_lon_lat(native_frame)).to(u.deg)
x, y = hmi.wcs.wcs_world2pix(lon, lat, origin)

#hmi = hmi.submap(bottom_left,top_right)

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
