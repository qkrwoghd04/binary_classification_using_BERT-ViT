import os
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image


class CustomImageDataset():
  def __init__(self, csv_file, img_dir, transform=None, target_transform=None):
        self.img_file = pd.read_csv(os.path.join(img_dir, csv_file))
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform
    
  def __len__(self):
    return len(self.img_file)
    
  def __getitem__(self, index):
    # 레이블을 기반으로 서브폴더 경로 결정
    label = self.img_file.iloc[index, 2]
    subfolder = 'Sleep' if label == 'Sleep' else 'Fall'
    img_path = os.path.join(self.img_dir, 'train', subfolder, self.img_file.iloc[index, 0])
    if(label == "Sleep"):
       label = 0
    else: label = 1
    image = read_image(img_path)
    if self.transform:
        image = self.transform(image)
    if self.target_transform:
        label = self.target_transform(label)

    return image, label