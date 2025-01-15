# Principles of Artificial Intelligence - Group Project
This repository contains the working files for the group assignment.

## Subject Details
Code: ISB46703  
Name: Priciples of Artificial Intelligence

## Topic Focused
Main Object Type: Flower - Orchid  
Sub-species:
- Brassavola (2633 images)
- Masdevallia (1725 images)
- Paphiopedilum Bellatulum (1795 images)
- Paphiopedilum Charlesworthii (1665 images)
- Phalaenopsis (2320 images)

Total images in used dataset: 10138 images

## Contents
- `dataset.py` was used to check the size of the base dataset and used to determine which species were to be used for training.
- `cleaner.py` was used to clean the folder and file names for ease of usage during training, and was used to aid `dataset.py` in categorizing which folder was for which species.
- `dataset` contains all images used in the training and validation stages of the model.
- `testing-data` contains human-curated images from the internet for validation purposes.
- `Group-10-Project.ipynb` contains the code and markdown for the entire assignment. When viewing this work, this file should be viewed in liew of the other two files mentioned above.

## Notes
- The original dataset contained 50k images, and will not be included in the repository.
- The used dataset, due to the sheer number of images (10k total), is compressed and is saved as `dataset.zip`.