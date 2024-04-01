## **Project** : Mobile Agent For Smart Home Using Multimodal Learning <2023-11-13>
### **Project Field** : Multimodal Learning, ViT, Transformer, Image captioning
#### **Project Description** :
Google의 LaMDA나 유명한 OpenAI의 Chatgpt와 같은 언어 모델의 등장으로 텍스트 생성, 기계번역, 질문 응답 시스템과 같은 분야에서 각각의 모델들은 큰 기여를 해왔습니다. 그리고 Vision-Language Models과 같이 두 모달리티 사이의 상호 작용을 이해하고 활용하는 CLIP, DALL-E와 같은 모델들의 등장으로 Multimodality의 시대가 도래했다. Vision과 text뿐만 아니라 다양한 Modalities의 활용은 기존의 하나의 Modality를 가진 모델보다 풍부하고 다양한 작업을 수행할 수 있다. 이 프로젝트에서는 독거노인을 위한 위급상황 탐지가 가능한 로봇에 탑제되는 Multimodal Model을 개발하는 것을 목표로 한다. Vision Transformer 모델을 활용해서 기존에 파악할 수 없었던 문제에 대해서 “Proposed method is not applicable to person lying on floor. This problem can be addressed by calculating speed of person while lying on the floor and while undergoing a fall. Full occlusion of a person is not addressed in the present work.” CNN 보다 자세하게 상황을 인지하고, Vision – Language Models을 통해서 그 이미지를 텍스트로 변환해 사용자에게 이메일을 보내는 기능까지 구현하려 합니다.

---
### **Methodologies**
**CNN과 ViT 아키텍처 비교**: CNN과 ViT는 이미지 처리와 관련된 작업에서 널리 사용되는 두 가지 주요 신경망 아키텍처입니다. CNN은 지역적 특성을 기반으로 작동하는 반면, ViT는 이미지 전체를 글로벌 컨텍스트로 처리합니다. 같은 데이터셋에 대해 두 모델의 성능을 비교하는 함으로 이러한 아키텍처의 강점과 약점을 이해를 통해 특정 유형의 이미지 처리 작업에 어떤 모델이 더 적합한지 결정하는 데 중요한 기준을 파악합니다.

**ViT를 사용한 이미지 캡셔닝**: 이렇게 비교한 Vision Transformer 모델로 이미지 캡셔닝을 진행 이미지를 분석하여 자연어 설명을 생성합니다.

**사용자 이메일로 상황 송신**: 마지막으로 생성된 이미지 캡셔닝을 텍스트를 사용자에게 이메일로 전송함으로 좀 더 정확한 상황을 표현합니다.

> ## 1. CNN Architecture (23.11.13) [Practice](https://github.com/qkrwoghd04/ViT_For_ImageCaptionnng_Implementation/blob/master/practice/CNN_Architecture_Practice.ipynb).
> ## 2. Transformer (24.03.10 - 24.03.13) 
<br> **Attention is all you need(2017)** 논문을 읽고, Transformer Architecture Implementation practice
> ## 3. Vision Transformer Architecture(ViT) (23.03.27 - ) [Practice](https://github.com/qkrwoghd04/ViT_For_ImageCaptionnng_Implementation/blob/master/practice/Vision_Transformer_Practice.ipynb),[ICUViT](https://github.com/qkrwoghd04/ViT_For_ImageCaptionnng_Implementation/blob/master/practice/Vision_Transformer_Architecture_Practice.ipynb).
<img width="500" height="350" alt="ViT" src="https://github.com/qkrwoghd04/multimodal_learning/assets/122519801/27777d21-e7b0-4606-8164-05f3c07799aa"><br>


> ## 4. Image Captioning
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

# Dataset Reference
[Elderly Set]https://gram.web.uah.es/data/datasets/fpds/index.html




