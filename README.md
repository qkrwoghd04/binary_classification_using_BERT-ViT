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
