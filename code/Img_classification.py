import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from keras.models import Sequential  # 수정: Model 대신 Sequential 사용
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense  # 수정: Dense 직접 임포트
from keras.preprocessing.image import ImageDataGenerator


train_data_dir = 'C:\\Users\\Jaeho\\OneDrive\\바탕 화면\\Final Year Project(Multimodal Learning)\\train'
validation_data_dir = 'C:\\Users\\Jaeho\\OneDrive\\바탕 화면\\Final Year Project(Multimodal Learning)\\validation'


# # 'processed_images' 리스트에 전처리된 모든 이미지가 저장됩니다.
# plt.imshow(processed_images[0])  # 첫 번째 이미지 확인
# plt.title('Processed Image')
# plt.show()

# 모델 생성
model = Sequential()

# 첫 번째 합성곱 레이어: 32개의 필터, 3x3 커널, ReLU 활성화 함수
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))

# 첫 번째 맥스 풀링 레이어: 2x2 풀링 사이즈
model.add(MaxPooling2D((2, 2)))

# 두 번째 합성곱 레이어: 64개의 필터, 3x3 커널, ReLU 활성화 함수
model.add(Conv2D(64, (3, 3), activation='relu'))

# 두 번째 맥스 풀링 레이어: 2x2 풀링 사이즈
model.add(MaxPooling2D((2, 2)))

# Flatten 레이어: 2D 특징 맵을 1D 벡터로 변환
model.add(Flatten())

# Dense 레이어: 64개의 뉴런, ReLU 활성화 함수
model.add(Dense(64, activation='relu'))

# 출력 레이어: 1개의 뉴런, 시그모이드 활성화 함수 (이진 분류를 가정)
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 모델 구조 요약
model.summary()

from keras.preprocessing.image import ImageDataGenerator


# 데이터 생성기 구성
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

# 훈련 데이터 생성기
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary')  # 'binary' 또는 'categorical'

# 검증 데이터 생성기
validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary')  # 'binary' 또는 'categorical'


history = model.fit(
    train_generator,
    steps_per_epoch=11,  # 전체 훈련 데이터셋 크기에 따라 조정
    epochs=10,  # 훈련을 원하는 에포크 수
    validation_data=validation_generator,
    validation_steps=50)  # 전체 검증 데이터셋 크기에 따라 조정

print(history.history)

# 훈련 및 검증 정확도 시각화
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# 훈련 및 검증 손실 시각화
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

test_data_dir='C:\\Users\\Jaeho\\OneDrive\\바탕 화면\\Final Year Project(Multimodal Learning)\\test'
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary')

test_loss, test_accuracy = model.evaluate(test_generator)
print('Test Accuracy:', test_accuracy)
print('Test Loss:', test_loss)
