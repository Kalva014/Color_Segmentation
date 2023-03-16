# Color_Segmentation
I trained a model to detect orange cones in images and find the relative world coordinates of the cone
from images. 

I implement algorithms that learn the color model, segment the target color, and finally localize the target object from images. I used a set of training images, which I hand-labeled and from these training examples, I built a color classifier and orange cone detector. I created algorithms that marked the center of the detected orange cone and display the distance to the cone on new test images.

# Instructions if you want to run on trained image:
1. Place a test image file in the Test_Images folder
2. In the third code cell there is a function called "unlabeled_img = get_test_image(real_test_folder, 'test_5.png'):". Change the string to file you want to test.
3. Now preconfiguration is finished so run all cells in the notebook.
4. You can see the outputs from the last few cells.

SIDE NOTE:
By running all the cells it trains the model since we don't use the EM step in the multivariate gaussian.