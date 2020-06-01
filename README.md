# TrashNet [![Build Status](https://travis-ci.org/vasantvohra/TrashNet.svg?branch=master)](https://travis-ci.org/vasantvohra/TrashNet/)  [![Udacity - Intro To Tensorflow](https://raw.githubusercontent.com/vasantvohra/TrashNet/master/ud.svg)](https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187) 
[![Linkedin Article](https://www.vectorlogo.zone/logos/linkedin/linkedin-ar21.svg)](https://www.linkedin.com/pulse/waste-segregation-convolution-neural-network-vasant-vohra)

**Waste Segregation** Project to classify waste into different classes. <br>

[![Already deployed version](https://raw.githubusercontent.com/vasantvohra/TrashNet/master/hr.svg)](https://trashnet.herokuapp.com)

[DIRECT LINK](https://trashnet.herokuapp.com)

[Kaggle Kernel](https://www.kaggle.com/vasantvohra1/using-cnn-test-accuracy-77)
Dataset: [Trashnet](https://github.com/garythung/trashnet)

| Categories|        
|---------| 
|Cardboard|
|Glass|
|Paper|
|Metal|
|Trash|

### Just a Beginner!
          
#### First attempt: Building Tensorflow keras CNN Model
[Notebook](https://github.com/vasantvohra/TrashNet/blob/master/Notebooks/Trashnet%20CNN%2040%25.ipynb)

- Training on GrayScale images
- Validation Accuracy 42%
- Loss function : Sparse Categorical Loss function
- Overfitting High

### Second attempt: 
[Notebook](https://github.com/vasantvohra/TrashNet/blob/master/Notebooks/Trashnet%20CNN%2080%25.ipynb)

- Image Augmentation
- Training on Colored images
- Validation Accuracy 80%
- Loss function : Categorical Loss function
- Added 1 more 32 filters Convolution block with default stride
- 2 Dense layers with dropouts

Understood
> - Image, Fit, Predict  Generators, Flow from directory.
>  - Difference between SpatialDropout2D and Dropout Regularization.
>   - Number of filters and dense perceptrons to build a model.
>  - Callbacks : Early Stopping and Model Checkpoints to save perfect model on Hierarchical Data Format HDF5 (.h5)  
>  - Visualizations by Matplotlib

# Completion of Course on : 
Udacity [Intro To Tensorflow](https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187)
<br>
![Completion](https://raw.githubusercontent.com/vasantvohra/TrashNet/master/udacity.png)

# Next Steps
1. Further Regularization -
	- Batch Normalization
	-  L1 & L2 error
	- intialization of weights
2. Transfer learning -
	- MobileNet
		- Saving & Deploying of TFLite
	- VGGNet
	- ResNet
3. Collect Preprocess my own Training Dataset.
4. Object Detection Localization
	- YOLO v2/v3
5. Trash, Instance Segmentation

## Understood Git Large File Storage
 [Large H5 Files](https://github.com/vasantvohra/TrashNet_H5/blob/master/Trashnet98.h5)
