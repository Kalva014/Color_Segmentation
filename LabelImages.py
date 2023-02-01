import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from roipoly import RoiPoly

# Save labeled region of interest image to a file. Remove extension of file and convert from png to csv
def create_labeled_file(roi_data, image_file_name):
    
    image_file_name = image_file_name[0:-3] + 'csv'
    image_file_path = os.path.join('Data/Labeled', image_file_name)
    image_file = open(image_file_path, "x")
    np.savetxt(image_file_path, roi_data)
    image_file.close()

# Setup figure to label orange cone region of interest
def label_image(folder_path, image_to_label):
    unlabeled_image_path = os.path.join(folder_path, image_to_label)
    img = mpimg.imread(unlabeled_image_path)

    # Show the image
    fig = plt.figure()
    plt.imshow(img, interpolation='nearest', cmap="Greys")
    plt.colorbar()
    plt.title("left click: line segment         right click or double click: close region")
    plt.show(block=False)

    # Let user draw first ROI
    cone_region_of_interest = RoiPoly(color='r', fig=fig)

    # # Show the image with the first ROI
    # fig = plt.figure()
    # plt.imshow(img, interpolation='nearest', cmap="Greys")
    # plt.colorbar()
    # cone_region_of_interest.display_roi()
    # plt.title('draw second ROI')
    # plt.show(block=False)

    # # Let user draw second ROI
    # extra_region_of_interest = RoiPoly(color='b', fig=fig)

    # # Show the image with both ROIs and their mean values
    # plt.imshow(img, interpolation='nearest', cmap="Greys")
    # plt.colorbar()
    # for roi in [cone_region_of_interest]:
    #     roi.display_roi()
    #     #roi.display_mean(img)
    #     #print(roi.display_mean(img))
    # plt.title('The two ROIs')
    # plt.show()

    # Show ROI masks
    cone_mask = cone_region_of_interest.get_mask(img[:, :, 0])
    #extra_mask = extra_region_of_interest.get_mask(img[:, :, 0])
    plt.imshow(cone_mask,
            interpolation='nearest', cmap="Greys")
    plt.title('ROI masks of the two ROIs')
    plt.show()
    #print(np.shape(img))
    #print(np.shape(cone_mask))
    cone_roi_pixels = img[cone_mask] # This gets pixels of region of interest

    create_labeled_file(cone_roi_pixels, image_to_label)

# Main Code Loop
def main():
    folder = 'Data/ECE5242Proj1-train'    
    for filename in os.listdir(folder):
        image_file_name = filename[0:-3] + 'csv'
        if image_file_name not in os.listdir('Data/Labeled'): # Check if file is already labeled
            label_image(folder, filename)

if __name__ == '__main__':
    main()
