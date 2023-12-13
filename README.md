### **Project** : Mobile Agent For Smart Home Using Multimodal Learning <2023-11-13>
#### **Project field** : Multimodal Learning, Image Classification, Sound Classification

#### **Project Description** : The project involves developing a multimodal learning model that combines image and sound datasets to analyze specific events, such as detecting a fall in elderly people. The process of developing such a model includes the following steps:

### **Data Preparation and Preprocessing**
* **Image Dataset** : Prepare the 'fall down', 'stand' , 'sit' images that I have already downloaded.
<img width="450" alt="image dataset" src="https://github.com/qkrwoghd04/multimodal_deep_learning/assets/122519801/bf52a11a-f05b-469c-ae49-12e391f82d51">

* **Sound Dataset** : Prepare a dataset containing sounds of falls, such as a 'screaming'. These can be collected from field recordings or open sources.
<img width="489" alt="scream" src="https://github.com/qkrwoghd04/multimodal_deep_learning/assets/122519801/a33df38b-4bc0-40fa-8037-e3c400a3b6b6">

#### **Citation**
du Toit, Jaco (2023). Human pose dataset (sit & stand pose classes). North-West University. Dataset. https://doi.org/10.25388/nwu.23290937.v1

https://www.kaggle.com/datasets/aananehsansiam/audio-dataset-of-scream-and-non-scream

https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset

### **Data Preprocessing**
* **Image Data** : Requires resizing, normalization, and possibly data argmentation.
<br> https://medium.com/ddiddu-log/%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9D%B8%EC%8B%9D%EC%9D%98-%EC%A0%95%EC%9D%98%EC%99%80-%EC%A3%BC%EC%9A%94-%EB%AA%A8%EB%8D%B8-%EB%B9%84%EA%B5%90-1-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%B6%84%EB%A5%98-image-classification-ae7a59bfaf65
* **Sound Data** : Commonly transformed from time domain to frequency domain using Fourier Transform(FFT) or converted into a Mel spectogram.
<br> https://wikidocs.net/193397

### **The following hardware components will be required :**
* Arduino Mega
* Raspberry Pi4B/4GB
* Camera Module(Pi Camera V2)
* Microphone(TBD)

### Gantt Chart
<img width="700" alt="gantt chart" src="https://github.com/qkrwoghd04/multimodal_learning/assets/122519801/5d1087e9-ae40-4651-9181-c267ed750f2c">

## Test result(1st attempt)
C:\Users\Jaeho\OneDrive\바탕 화면\Final Year Project(Multimodal Learning)>C:/Python311/python.exe "c:/Users/Jaeho/OneDrive/바탕 화면/Final Year Project(Multimodal Learning)/code/fusion.py"
Found 338 images belonging to 2 classes.
Found 85 images belonging to 2 classes.
2023-12-12 21:01:27.710407: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE SSE2 SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Epoch 1/50
6/6 [==============================] - 52s 8s/step - loss: 0.7785 - accuracy: 0.5355 - val_loss: 0.6811 - val_accuracy: 0.5059
Epoch 2/50
6/6 [==============================] - 46s 8s/step - loss: 0.6864 - accuracy: 0.5030 - val_loss: 0.6691 - val_accuracy: 0.7765
Epoch 3/50
6/6 [==============================] - 54s 9s/step - loss: 0.6906 - accuracy: 0.5237 - val_loss: 0.7061 - val_accuracy: 0.5059
Epoch 4/50
6/6 [==============================] - 61s 10s/step - loss: 0.6952 - accuracy: 0.5237 - val_loss: 0.6744 - val_accuracy: 0.5059
Epoch 5/50
6/6 [==============================] - 47s 8s/step - loss: 0.6765 - accuracy: 0.5799 - val_loss: 0.6518 - val_accuracy: 0.6824
Epoch 6/50
6/6 [==============================] - 49s 8s/step - loss: 0.6838 - accuracy: 0.5473 - val_loss: 0.6590 - val_accuracy: 0.4941
Epoch 7/50
6/6 [==============================] - 48s 8s/step - loss: 0.6740 - accuracy: 0.5710 - val_loss: 0.6161 - val_accuracy: 0.8000
Epoch 8/50
6/6 [==============================] - 44s 7s/step - loss: 0.6290 - accuracy: 0.6953 - val_loss: 1.1506 - val_accuracy: 0.5059
Epoch 9/50
6/6 [==============================] - 44s 7s/step - loss: 0.7986 - accuracy: 0.5858 - val_loss: 0.6314 - val_accuracy: 0.6118
Epoch 10/50
6/6 [==============================] - 49s 8s/step - loss: 0.5754 - accuracy: 0.7515 - val_loss: 0.5444 - val_accuracy: 0.7765
Epoch 11/50
6/6 [==============================] - 53s 9s/step - loss: 0.6146 - accuracy: 0.6657 - val_loss: 0.6012 - val_accuracy: 0.6000
Epoch 12/50
6/6 [==============================] - 48s 8s/step - loss: 0.5678 - accuracy: 0.7219 - val_loss: 0.6406 - val_accuracy: 0.6000
Epoch 13/50
6/6 [==============================] - 51s 9s/step - loss: 0.5008 - accuracy: 0.7692 - val_loss: 0.4116 - val_accuracy: 0.8353
Epoch 14/50
6/6 [==============================] - 47s 8s/step - loss: 0.5112 - accuracy: 0.7781 - val_loss: 0.5941 - val_accuracy: 0.6353
Epoch 15/50
6/6 [==============================] - 50s 8s/step - loss: 0.4842 - accuracy: 0.7988 - val_loss: 0.5149 - val_accuracy: 0.7412
Epoch 16/50
6/6 [==============================] - 59s 10s/step - loss: 0.5279 - accuracy: 0.7515 - val_loss: 0.5870 - val_accuracy: 0.6588
Epoch 17/50
6/6 [==============================] - 53s 9s/step - loss: 0.4242 - accuracy: 0.8166 - val_loss: 0.3729 - val_accuracy: 0.8588
Epoch 18/50
6/6 [==============================] - 51s 9s/step - loss: 0.4165 - accuracy: 0.8284 - val_loss: 0.4762 - val_accuracy: 0.7647
Epoch 19/50
6/6 [==============================] - 53s 9s/step - loss: 0.4362 - accuracy: 0.8047 - val_loss: 0.6873 - val_accuracy: 0.6118
Epoch 20/50
6/6 [==============================] - 45s 7s/step - loss: 0.3833 - accuracy: 0.8402 - val_loss: 0.3807 - val_accuracy: 0.8471
Epoch 21/50
6/6 [==============================] - 45s 8s/step - loss: 0.4931 - accuracy: 0.7751 - val_loss: 0.5147 - val_accuracy: 0.6824
Epoch 22/50
6/6 [==============================] - 44s 7s/step - loss: 0.4599 - accuracy: 0.8047 - val_loss: 0.3998 - val_accuracy: 0.8471
Epoch 23/50
6/6 [==============================] - 45s 8s/step - loss: 0.3718 - accuracy: 0.8669 - val_loss: 0.6975 - val_accuracy: 0.6000
Epoch 24/50
6/6 [==============================] - 45s 7s/step - loss: 0.4036 - accuracy: 0.8284 - val_loss: 0.3324 - val_accuracy: 0.8824
Epoch 25/50
6/6 [==============================] - 45s 7s/step - loss: 0.3915 - accuracy: 0.8432 - val_loss: 0.3235 - val_accuracy: 0.9059
Epoch 26/50
6/6 [==============================] - 43s 7s/step - loss: 0.3806 - accuracy: 0.8698 - val_loss: 0.2623 - val_accuracy: 0.9176
Epoch 27/50
6/6 [==============================] - 44s 7s/step - loss: 0.3452 - accuracy: 0.8728 - val_loss: 0.5156 - val_accuracy: 0.7176
Epoch 28/50
6/6 [==============================] - 44s 7s/step - loss: 0.2967 - accuracy: 0.8935 - val_loss: 0.6275 - val_accuracy: 0.6471
Epoch 29/50
6/6 [==============================] - 46s 8s/step - loss: 0.3956 - accuracy: 0.8166 - val_loss: 0.2194 - val_accuracy: 0.9176
Epoch 30/50
6/6 [==============================] - 55s 9s/step - loss: 0.2910 - accuracy: 0.9053 - val_loss: 0.5284 - val_accuracy: 0.7294
Epoch 31/50
6/6 [==============================] - 48s 8s/step - loss: 0.4980 - accuracy: 0.7959 - val_loss: 0.2607 - val_accuracy: 0.8941
Epoch 32/50
6/6 [==============================] - 50s 8s/step - loss: 0.3150 - accuracy: 0.8609 - val_loss: 0.2826 - val_accuracy: 0.9176
Epoch 33/50
6/6 [==============================] - 49s 8s/step - loss: 0.3395 - accuracy: 0.8639 - val_loss: 0.2528 - val_accuracy: 0.9176
Epoch 34/50
6/6 [==============================] - 45242s 9016s/step - loss: 0.2434 - accuracy: 0.9172 - val_loss: 0.3941 - val_accuracy: 0.8471
Epoch 35/50
6/6 [==============================] - 43s 7s/step - loss: 0.3726 - accuracy: 0.8521 - val_loss: 0.2846 - val_accuracy: 0.8941
Epoch 36/50
6/6 [==============================] - 74s 14s/step - loss: 0.2981 - accuracy: 0.8728 - val_loss: 0.4255 - val_accuracy: 0.7882
Epoch 37/50
6/6 [==============================] - 76s 13s/step - loss: 0.2528 - accuracy: 0.9083 - val_loss: 0.2362 - val_accuracy: 0.9176
Epoch 38/50
6/6 [==============================] - 86s 15s/step - loss: 0.2345 - accuracy: 0.9201 - val_loss: 0.6166 - val_accuracy: 0.7059
Epoch 39/50
6/6 [==============================] - 83s 14s/step - loss: 0.4655 - accuracy: 0.8284 - val_loss: 0.2518 - val_accuracy: 0.8941
Epoch 40/50
6/6 [==============================] - 90s 15s/step - loss: 0.2425 - accuracy: 0.9053 - val_loss: 0.4606 - val_accuracy: 0.7765
Epoch 41/50
6/6 [==============================] - 88s 15s/step - loss: 0.2169 - accuracy: 0.9320 - val_loss: 1.7353 - val_accuracy: 0.5176
Epoch 42/50
6/6 [==============================] - 92s 15s/step - loss: 0.5644 - accuracy: 0.8047 - val_loss: 0.3035 - val_accuracy: 0.8706
Epoch 43/50
6/6 [==============================] - 89s 15s/step - loss: 0.2351 - accuracy: 0.9231 - val_loss: 0.2358 - val_accuracy: 0.8941
Epoch 44/50
6/6 [==============================] - 88s 15s/step - loss: 0.2314 - accuracy: 0.9260 - val_loss: 0.1977 - val_accuracy: 0.9059
Epoch 45/50
6/6 [==============================] - 88s 15s/step - loss: 0.2406 - accuracy: 0.8994 - val_loss: 0.1900 - val_accuracy: 0.9059
Epoch 46/50
6/6 [==============================] - 69s 11s/step - loss: 0.2085 - accuracy: 0.9290 - val_loss: 0.1118 - val_accuracy: 0.9529
Epoch 47/50
6/6 [==============================] - 88s 15s/step - loss: 0.4300 - accuracy: 0.8550 - val_loss: 0.1559 - val_accuracy: 0.9647
Epoch 48/50
6/6 [==============================] - 85s 14s/step - loss: 0.1798 - accuracy: 0.9556 - val_loss: 0.2842 - val_accuracy: 0.8471
Epoch 49/50
6/6 [==============================] - 84s 14s/step - loss: 0.2135 - accuracy: 0.9260 - val_loss: 0.1676 - val_accuracy: 0.9294
Epoch 50/50
6/6 [==============================] - 83s 14s/step - loss: 0.2365 - accuracy: 0.9112 - val_loss: 0.2324 - val_accuracy: 0.9176
2/2 [==============================] - 5s 4s/step - loss: 0.2212 - accuracy: 0.9294
테스트 손실: 0.22119773924350739, 테스트 정확도: 0.929411768913269
2/2 [==============================] - 7s 3s/step
정확도: 0.5411764705882353, 정밀도: 0.5142857142857142, 재현율: 0.45, F1 점수: 0.48
