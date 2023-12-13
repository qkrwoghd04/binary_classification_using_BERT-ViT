[1st atp.txt](https://github.com/qkrwoghd04/multimodal_learning/files/13655224/1st.atp.txt)### **Project** : Mobile Agent For Smart Home Using Multimodal Learning <2023-11-13>
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

## Test result
**1st attempt**<br>
C:\Users\Jaeho\OneDrive\바탕 화면\Final Year Project(Multimodal Learning)>C:/Python311/python.exe "c:/Users/Jaeho/OneDrive/바탕 화면/Final Year Project(Multimodal Learning)/code/fusion.py"<br>
Found 338 images belonging to 2 classes.<br>
Found 85 images belonging to 2 classes.<br>
2023-12-12 21:01:27.710407: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.<br>
To enable the following instructions: SSE SSE2 SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.<br>
Epoch 50/50<br>
6/6 [==============================] - 83s 14s/step - loss: 0.2365 - accuracy: 0.9112 - val_loss: 0.2324 - val_accuracy: 0.9176<br>
2/2 [==============================] - 5s 4s/step - loss: 0.2212 - accuracy: 0.9294<br>
테스트 손실: 0.22119773924350739, 테스트 정확도: 0.929411768913269<br>
2/2 [==============================] - 7s 3s/step<br>
정확도: 0.5411764705882353, 정밀도: 0.5142857142857142, 재현율: 0.45, F1 점수: 0.48<br>

