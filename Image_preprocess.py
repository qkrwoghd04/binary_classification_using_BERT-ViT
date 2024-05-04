# Image Classification
import torch
from torchvision.transforms import v2
# Visualization
import matplotlib.pyplot as plt

def image_transform():

  H, W = 224, 224
  img = torch.randint(0, 256, size=(3, H, W), dtype=torch.uint8)

  transforms = v2.Compose([
      v2.RandomResizedCrop(size=(224, 224), antialias=True),
      v2.RandomPhotometricDistort(p=1),
      v2.RandomChannelPermutation() ,# 채널 무작위 변경
      v2.RandomHorizontalFlip(p=0.2),
      v2.ToDtype(torch.float32, scale=True),
      v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
  ])
 

  return transforms


def visualize_data(train_dataloader):
    # 이미지와 정답(label)을 표시합니다.
    train_features, train_labels = next(iter(train_dataloader))
    print(f"Feature batch shape: {train_features.size()}")
    print(f"Labels batch shape: {train_labels.size()}")
    img = train_features[0].squeeze()
    label = train_labels[0]

    if img.dim() == 3 and img.size(0) == 3:
        img = img.permute(1, 2, 0)
        
    plt.imshow(img, cmap="gray")
    plt.show()
    print(f"Label: {label}")