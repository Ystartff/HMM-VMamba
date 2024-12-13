

**1. Datasets.**

*A.ISIC2017* </br>
1- Download the ISIC 2017 train dataset from [this](https://challenge.isic-archive.com/data) link and extract both training dataset and ground truth folders inside the `/data/dataset_isic17/`. </br>
2- Run `Prepare_ISIC2017.py` for data preparation and dividing data to train,validation and test sets. </br>

*B.Spleen* </br>
1- Download the Spleen dataset from [this](http://medicaldecathlon.com/) link. </br>

*C.CVC-ClinicDB* </br>
1- Download the CVC-ClinicDB dataset from [this](https://polyp.grand-challenge.org/CVCClinicDB/) link. </br>

*D. Prepare your own dataset* </br>
1. The file format reference is as follows. (The image is a 24-bit png image. The mask is an 8-bit png image. (0 pixel dots for background, 255 pixel dots for target))
- './your_dataset/'
  - images
    - 0000.png
    - 0001.png
  - masks
    - 0000.png
    - 0001.png
  - Prepare_your_dataset.py
2. In the 'Prepare_your_dataset.py' file, change the number of training sets, validation sets and test sets you want.</br>
3. Run 'Prepare_your_dataset.py'. </br>

