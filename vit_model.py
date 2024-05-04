# Pytorch
import sys
import torch

print(torch.__version__)
from torch import nn
import os
from torch.utils.data import DataLoader
from torchvision import datasets
from custom_image_dataset import CustomImageDataset
import argparse
from Image_preprocess import *

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available() else "cpu"
)
print(f"Using {device} device")


class NerualNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(224 * 224, 512),
            nn.RuLU(),
            nn.Linear(512, 512),
            nn.RuLU(),
            nn.Linear(512, 2),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


def main(argv):

    parser = argparse.ArgumentParser(
        description="Fall detection with Vision Transformer(ViT) Model",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-l",
        "--load",
        nargs="+",
        type=str,
        help="python vit_model.py --load train_captions.csv",
    )
    args = parser.parse_args()

    ## data load & argumentation
    if args.load is not None:
        file_path = "C:/Users/Jaeho/OneDrive/바탕 화면/fall detection/dataset/"
        data_csv = args.load[0]
        print("Loading file...")
        transform = image_transform()
        train_dataset = CustomImageDataset(
            csv_file=data_csv, img_dir=file_path, transform=transform
        )
        # test_dataset = CustomImageDataset(data_csv, file_path, transform)
        train_dataloader = torch.utils.data.DataLoader(
            train_dataset, batch_size=1024, shuffle=True, num_workers=4
        )
        # test_dataloader = torch.utils.data.DataLoader(test_dataset,
        #                                           batch_size=1024,
        #                                           shuffle=True,
        #                                           num_workers=4)

        visualize_data(train_dataloader)


if __name__ == "__main__":
    main(sys.argv[1:])
