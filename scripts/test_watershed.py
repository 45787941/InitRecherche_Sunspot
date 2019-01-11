from Watershed import *
import os

#image_name = "2012-07-05_00-30-00.png"
for image_name in os.listdir('.'):
    if image_name[0] == "2":
        shed = Watershed(
                       data_image = str(image_name),
                       binary_or_gray_or_color = "color",
                       size_for_calculations = 128,
                       sigma = 1,
                       gradient_threshold_as_fraction = 0.08,
                       level_decimation_factor = 8,
                       padding = 0,
               )
        shed.extract_data_pixels()
        print("Displaying the original image:")
        shed.display_data_image()
        print("Calculating the gradient image")
        shed.compute_gradient_image()
        print("Computing Z level sets for the gradient image")
        shed.compute_Z_level_sets_for_gradient_image()
        print("Propagating influences:")
        shed.propagate_influence_zones_from_bottom_to_top_of_Z_levels()
        shed.display_watershed()
        shed.display_watershed_in_color()
        #   Extract up to 30 blob contours and, at the same time, only accept
        #   contours whose length is GREATER THAN 20 pixels:
        #contours = shed.extract_watershed_contours_with_random_sampling(50, 50)

        #   You can also call the following method for extracting the watershed
        #   contours
        contours = shed.extract_watershed_contours_separated()

        #   Uncomment the following lines if you want to print out the contours:
        #for contour in contours:
        #   print("\n\ncontour: ", contour)
        #   print("contour length: ", len(contour))

        shed.display_watershed_contours_in_color()
