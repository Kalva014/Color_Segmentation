# Color_Segmentation
I trained a model to detect orange cones in images and find the relative world coordinates of the cone
from images. 

I implement algorithms that learn the color model, segment the target color, and finally localize the target object from images. I used a set of training images, which I hand-labeled and from these training examples, I built a color classifier and orange cone detector. I created algorithms that marked the center of the detected orange cone and display the distance to the cone on new test images.

# Instructions:
1. Place a test image file in the Test_Images folder
2. In the ColorSegmentationTraining.ipynb file, within the second cell and in the funciton "def get_original_image(unlabled_folder):" change string to file you want to test.
3. Run all cells in the notebook
4. Identify out of the centroid list and bounding box which is the one related to the cone to fix the indexing and get the right index

# Things that need to be fixed:
1. Get less bounding boxes and centroids