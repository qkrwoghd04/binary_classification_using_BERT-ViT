## **Project** : Mobile Agent For Smart Home Using Multimodal Learning <2023-11-13>
### **Project Field** : Multimodal Learning, ViT, Transformer, Image captioning
### **Project Description** :
The emergence of language models such as Google's LaMDA and OpenAI's ChatGPT has made significant contributions to fields like text generation, machine translation, and question-answering systems. Additionally, the arrival of models like CLIP and DALL-E, which understand and utilize the interaction between two modalities, has signaled the beginning of the Multimodality era. The use of various modalities, not limited to vision and text, enables the performance of richer and more diverse tasks compared to models that depend solely on one modality. This project aims to develop a Multimodal Model that can be embedded in robots designed to detect emergency situations for elderly individuals living alone. By leveraging the Vision Transformer model and image captioning, we intend to address problems that were previously undetectable. According to previous studies, "It was impossible to determine whether a person lying on the floor in a still image had fallen or was simply lying down." This is evidenced by the fact that after training on datasets for single modality, the test accuracy for BERT and ViT models was only 0.65 and 0.6, respectively, showing the difficulty. Compared to using a single modality, Vision-Language Models that utilize a dataset combining two modalities show significantly better results with a test accuracy of 0.92.

---
## **Methodologies**

> ### 1. BERT [BERT_MODEL_CODE](https://github.com/qkrwoghd04/ImageCaptionnng_Using_ViT/blob/master/code/Image%26Text_fusion_using_BERT.ipynb)
![image](https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/29666a47-d641-4c58-b107-4596ed4c995c)

> ### 2. CNN Architecture (23.11.13) [REFERENCE_MODEL_CODE](https://github.com/qkrwoghd04/ViT_For_ImageCaptionnng_Implementation/blob/master/practice/CNN_Architecture_Practice.ipynb).
> ### 3. Transformer (24.03.10 - 24.03.13)
<img width="298" alt="image" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/2d8ce1cf-c305-4863-8f8a-6d1009ce05cf">

> ### 4. Vision Transformer Architecture(ViT) (23.03.27 - 23.04.02) [ViT_MODEL_CODE](https://github.com/qkrwoghd04/ImageCaptionnng_Using_ViT/blob/master/code/Image%26Text_fusion_using_ViT.ipynb)
**The model shows good accuracy on the train and validation datasets, but it demonstrates a low accuracy of 0.6 on unseen test data.**
<img width="500" height="350" alt="ViT" src="https://github.com/qkrwoghd04/multimodal_learning/assets/122519801/27777d21-e7b0-4606-8164-05f3c07799aa"><br>
> ### 5. Multimodal deep learning [LATE_FUTION_CODE](https://github.com/qkrwoghd04/ImageCaptionnng_Using_ViT/blob/master/code/Image%26Text_late_fusion.ipynb)
---
## **Dataset**
> ### Image Dataset
- #### Train data
<img width="160" alt="fall dataset" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/e30eb6b6-7e9e-4357-8621-bb8b3b5cfe59">
<img width="160" alt="sleep" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/2ad370b5-6e2f-45b7-85ed-d01e9f33738c">

- #### Test data
<img width="160" alt="fall_test" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/7a515e4d-c29d-4217-89dd-6a163f94b7a5">
<img width="160" alt="sleep_test" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/72c3026b-a85f-488d-be77-37ec43c4b976">

> ### Text Dataset
<img width="563" alt="text_data" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/d652cf31-cab1-430f-82ac-762990f275f3">

> ### fusion Dataset
<img width="730" alt="multimodal dataset" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/1d058bc4-ef9a-4713-8c02-b28026c5163a">

---
## **Results**
- ### **Table**
| Method | Accuracy(%) |
|----------|----------|
| Image (ViT)   | 60  |
| Text (BERT)   | 64.9   |
| **Late Fusion (BERT&ViT)**   | **92.5**   |

- ### **Visualization**
<img width="650" alt="fusion result" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/20907efb-f012-4fa5-a964-48b47e2ff3f3">

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

## Dataset Reference
[Elderly Set]https://gram.web.uah.es/data/datasets/fpds/index.html




