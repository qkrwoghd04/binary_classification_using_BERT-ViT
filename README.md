## Deep Learning for Image Classification<23.11.14>
#### This part aims to classify images using deep learning techniques, specifically leveraging a Convolutional Neural Network (CNN) to learn features of images and perform binary classification.

### Model Structure
#### The model is built using the Sequential API and includes the following layers:

 1. **Conv2D**: Convolution layer with 32 filters and a 3x3 kernel. ReLU activation function applied.
 2. **MaxPooling2D**: Max pooling layer with a 2x2 pool size.
 3. **Conv2D**: Another convolution layer with 64 filters and a 3x3 kernel. ReLU activation function applied.
 4. **MaxPooling2D**: Second max pooling layer with a 2x2 pool size.
 5. **Flatten**: Flatten the 2D feature maps into a 1D vector.
 6. **Dense**: Dense layer with 64 neurons. ReLU activation function applied.
 7. **Dense**: Output layer with 1 neuron. Sigmoid activation function applied for binary classification.

#### Image:
<img width="439" alt="Model_sequential" src="https://github.com/qkrwoghd04/multimodal_learning/assets/122519801/1ca11a51-deb8-4783-8cc5-eebcdb7d4a8f">

### Training Process
#### The model was trained over 10 epochs on a training set consisting of 335 images and validated on a set of 80 images. Image data was resized and normalized using ImageDataGenerator.

### Results and Interpretation
#### During training, the model consistently showed high accuracy, achieving 100% training accuracy in the final epoch. The validation set accuracy was approximately 83.75%, indicating that while the model learned the training data very well, it showed somewhat lower accuracy on the validation data.

#### On the test set, the model achieved an accuracy of 83.33%. This indicates that the model has achieved some generalization to new data.
#### Image:
<img width="888" alt="epoch" src="https://github.com/qkrwoghd04/multimodal_learning/assets/122519801/6b2897a4-82c9-4e5f-8d88-e6e2742411f3">

