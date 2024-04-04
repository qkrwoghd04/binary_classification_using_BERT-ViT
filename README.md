## **Project** : Mobile Agent For Smart Home Using Multimodal Learning <2023-11-13>
### **Project Field** : Multimodal Learning, ViT, Transformer, Image captioning
#### **Project Description** :
The advent of language models such as Google's LaMDA and OpenAI's ChatGPT has made significant contributions to fields like text generation, machine translation, and question-answering systems. Furthermore, the emergence of models like CLIP and DALL-E, which understand and utilize the interaction between two modalities, has ushered in the era of Multimodality. The use of various modalities, not limited to vision and text, enables the performance of richer and more diverse tasks compared to models with only one modality. This project aims to develop a Multimodal Model that can be embedded in robots designed to detect emergency situations for elderly individuals living alone. By leveraging the Vision Transformer model and image captioning, we intend to address issues that were previously undetectable. "The proposed method is not applicable to a person lying on the floor. This problem can be addressed by calculating the speed of a person while lying on the floor and while undergoing a fall. Full occlusion of a person is not addressed in the present work[1]." Compared to using a single modality, Vision-Language Models allow for the conversion of images to text, further enabling the implementation of a feature that sends precise situational emails to users.


---
### **Methodologies**
**Sleep & Fall Binary Classification** using CNN and ViT Architectures: CNN and ViT are two main neural network architectures widely used for tasks related to image processing. While CNN operates based on local features, ViT treats the image as a whole in a global context. By comparing the performance of both models on the same dataset, we aim to understand the strengths and weaknesses of these architectures and determine how well classification can be achieved using just one modality.

**Image Captioning**: Through image captioning techniques, features extracted from the generated captions are used to add weight to the image classification task, enabling the model to make more accurate distinctions between the two scenarios.

**Sending Situation to User via Email using SMTP protocol**: Finally, the derived results are sent to the user via email.

> ## 1. CNN Architecture (23.11.13) [CNNPractice](https://github.com/qkrwoghd04/ViT_For_ImageCaptionnng_Implementation/blob/master/practice/CNN_Architecture_Practice.ipynb).
> ## 2. Transformer (24.03.10 - 24.03.13) 
<br> **Attention is all you need(2017)** 논문을 읽고, Transformer Architecture Implementation practice
> ## 3. Vision Transformer Architecture(ViT) (23.03.27 - 23.04.02) [ViTPractice](https://github.com/qkrwoghd04/ViT_For_ImageCaptionnng_Implementation/blob/master/practice/Vision_Transformer_Practice.ipynb) [ViT](https://github.com/qkrwoghd04/ViT_For_ImageCaptionnng_Implementation/blob/master/practice/Vision_Transformer_Architecture_Practice.ipynb)

**The model shows good accuracy on the train and validation datasets, but it demonstrates a low accuracy of 0.55 on unseen test data.**
>**ViT Hyper-Parameters:**
- image_size: int (224)
- patch_size: int (64)
- num_classes: int (2)
- epochs : 70
- lr : 3e-6
- weight_decay : 4e-5
- channels: int (image channels = 3)

<img width="500" height="350" alt="ViT" src="https://github.com/qkrwoghd04/multimodal_learning/assets/122519801/27777d21-e7b0-4606-8164-05f3c07799aa"><br>


> ## 4. Image Captioning [Code](https://github.com/qkrwoghd04/ImageCaptionnng_Using_ViT/blob/master/practice/Image_Captioning.ipynb)
> ## 5. SMTP Protocol
---
### **Reference List**
[1] P. S. Sase and S. H. Bhandari, "Human Fall Detection using Depth Videos," Department of Computer Science and Engineering, Walchand College of Engineering, Sangli, India
<br>[2] J. Zhang and C. Zong, "Neural machine translation: Challenges, progress and future," Science China Technological Sciences, vol. 63, no. 10, pp. 2028-2050, 2020/10/01 2020, doi: 10.1007/s11431-020-1632-x.
<br>[3] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, "Attention is all you need," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. TBD, no. TBD, pp. TBD, Jun. 2017, revised Aug. 2023. [Online]. Available: https://arxiv.org/abs/1706.03762
<br>[4] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, and N. Houlsby, "An image is worth 16x16 words: Transformers for image recognition at scale," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. TBD, no. TBD, pp. TBD, Oct. 2020, revised Jun. 2021. [Online]. Available: https://arxiv.org/abs/2010.11929
<br>[5] P. Xu, X. Zhu and D. A. Clifton, "Multimodal Learning With Transformers: A Survey," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 45, no. 10, pp. 12113-12132, Oct. 2023, doi: 10.1109/TPAMI.2023.3275156.
keywords: {Transformers;Task analysis;Surveys;Visualization;Taxonomy;Mathematical models;Data models;Multimodal learning;transformer;introductory;taxonomy;deep learning;machine learning},

## Code Reference
https://www.tensorflow.org/tutorials/images/cnn?hl=ko <br>
https://keras.io/examples/vision/image_classification_with_vision_transformer/ <br>
https://medium.com/@konstantinos.gyftodimos/vision-transformer-for-binary-classification-of-custom-dataset-hands-on-fdcd162e605e

# Dataset Reference
[Elderly Set]https://gram.web.uah.es/data/datasets/fpds/index.html




