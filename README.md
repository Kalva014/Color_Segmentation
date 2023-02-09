# Color_Segmentation
I trained a model to detect orange cones in images and find the relative world coordinates of the cone
from images. 

I implement algorithms that learn the color model, segment the target color, and finally localize the target object from images. I used a set of training images, which I hand-labeled and from these training examples, I built a color classifier and orange cone detector. I created algorithms that marked the center of the detected orange cone and display the distance to the cone on new test images.

# Instructions if you want to run on trained image:
1. Place a test image file in the Test_Images folder
2. In the ColorSegmentationTraining.ipynb file, if there are files in "Data/saved_parameters/" folder uncomment and run the first and second code cell
3. For  the third code cell and in the function "def get_original_image(unlabeled_folder):" change string to file you want to test.
4. Now preconfiguration is finished run all cells in the notebook
5. Identify out of the centroid list and bounding box which is the one related to the cone to fix the indexing and get the right index

# Things that need to be fixed:
1. Get less bounding boxes and centroids