## **Project** : Mobile Agent For Smart Home Using Multimodal Learning <2023-11-13>
### **Project Field** : Multimodal Learning, ViT, Transformer, Image captioning
### **Project Description** :
This project aims to develop a Multimodal Model that can be embedded in robots designed to detect emergency situations for elderly individuals living alone. By leveraging the Vision Transformer model and image captioning, we intend to address problems that were previously undetectable. According to previous studies, "It was impossible to determine whether a person lying on the floor in a still image had fallen or was simply lying down." This is evidenced by the fact that after training on datasets for single modality, the test accuracy for BERT and ViT models was only 0.7 and 0.875, respectively, showing the difficulty. Compared to using a single modality, Vision-Language Models that utilize a dataset combining two modalities show significantly better results with a test accuracy of 0.92.

---
## **Methodologies**

> ### 1. BERT Implementation [BERT_MODEL_CODE](https://github.com/qkrwoghd04/ImageCaptionnng_Using_ViT/blob/master/code/Image%26Text_fusion_using_BERT.ipynb)
**This project utilized a general Pretrained BERT model, and employed the tensorflow keras library for model training and dataset management.<br>
Each sentence is tokenized using a tokenizer, and these tokenized sentences undergo input embedding followed by the addition of positional encoding before entering the multi-head attention mechanism.<br>**
<img width="500" height='700' alt="image" src="https://github.com/qkrwoghd04/binary_classification_using_BERT-ViT/assets/122519801/4a00f0d1-32e3-4390-a793-d47a033eacc6">

**The token “man” strongly attends to “hallway”, and “lying” similarly focuses on “ground”. <br>
This highlights how the model prioritizes certain tokens over others, revealing how information is centralized around specific words.<br>**
<img width="500" height='500' alt="image" src="https://github.com/qkrwoghd04/binary_classification_using_BERT-ViT/assets/122519801/4c528134-0320-4d24-b889-52fca8bb4329"><br>

---
> ### 2. Transformer Background Study (24.03.10 - 24.03.13)
<img width="500" height='350' alt="image" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/2d8ce1cf-c305-4863-8f8a-6d1009ce05cf"><br>

---
> ### 3. Vision Transformer Architecture(ViT) Implementation (23.03.27 - 23.04.02) [ViT_MODEL_CODE](https://github.com/qkrwoghd04/ImageCaptionnng_Using_ViT/blob/master/code/Image%26Text_fusion_using_ViT.ipynb)
> #### ViT Mechanism
**Similar to the BERT model, these patches are processed as individual image tokens. Each patch token progress linear projection and subsequently augmented with positional embeddings.<br>
This step enables the Transformer encoder to process each patch. The self-attention mechanism within each Transformer block allows the model to prioritize and weigh the patches independently of their spatial positions, capturing global dependencies within the image.<br>**
<img width="600" height='350' alt="image" src=https://github.com/qkrwoghd04/binary_classification_using_BERT-ViT/assets/122519801/e7549589-ef2c-4b8f-895f-61bdeda48d4d><br>

> #### Split img
**The fundamental mechanism begins with dividing the image into patches according to established patch size which is 16x16.<br>
Then, the image is resized from 224 x 224 to 16x16, resulting in a total of 196 patches of 16x16 each.<br>**
<img width="500" alt="split img" src="https://github.com/qkrwoghd04/binary_classification_using_BERT-ViT/assets/122519801/80d98b59-5b3c-46a1-8148-93f4be533c51"><br>

---
> ### 4. Multimodal deep learning Implementation (24.03.14 - 24.04.15) [LATE_FUTION_CODE](https://github.com/qkrwoghd04/ImageCaptionnng_Using_ViT/blob/master/code/Image%26Text_late_fusion.ipynb)

**The figure below illustrates the training process of a Late Fusion Model that combines textual and visual inputs along with labels. After integration as shown in Figure 2.10, the data passes through modality-specific layers: a BERT layer for textual data, and a Vision Transformer (ViT) layer. The BERT layer processes the textual data, producing a 768-dimensional pooled feature vector, and the ViT layer for visual data, establishing a 1000-dimensional pooled output.<br>**
<img width="700" alt="split img" src="https://github.com/qkrwoghd04/binary_classification_using_BERT-ViT/assets/122519801/7ee60d76-de79-4860-b567-4d033e947f7b"><br>

---
## **Dataset**
> ### Image Dataset
- #### Train data
<img width="730" alt="multimodal dataset" src="https://github.com/qkrwoghd04/binary_classification_using_BERT-ViT/assets/122519801/0c8064f8-e6ad-42c7-ac7c-01e5521d7240">

> ### fusion Dataset
<img width="730" alt="multimodal dataset" src="https://github.com/qkrwoghd04/Image-text_fusion_for_binary_classification_using_BERT-ViT/assets/122519801/1d058bc4-ef9a-4713-8c02-b28026c5163a">

---
## **Results**
Test evaluations can vary significantly from the table. **I believe that the quantity and quality of the dataset are the most crucial parts of any AI model**. However, since this project was trained and tested with only 400 training and 40 test data, the results may differ significantly.<br>
- ### **Table**
| Method | Accuracy(%) |
|----------|----------|
| Image (ViT)   | 70  |
| Text (BERT)   | 87.4   |
| **Late Fusion (BERT&ViT)**   | **92.5**   |

- ### **Visualization**
<img width="730" alt="multimodal dataset" src="https://github.com/qkrwoghd04/binary_classification_using_BERT-ViT/assets/122519801/620d1900-c159-4578-9175-48a70e55d75d">

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

---
## License
This project is released by Apeche License version 2.0




