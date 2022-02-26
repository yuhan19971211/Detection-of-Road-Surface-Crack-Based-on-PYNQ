# Detection-of-Road-Surface-Crack-Based-on-PYNQ
This is the code of paper “Detection of Road Surface Crack Based on PYNQ”

This project aims at the problem of road surface image denoising and crack recognition by using embedded camera. Using Gaussian filter to blur the image, over the threshold zero processing and the morphology on and off operation are binarization and further denoising. And the crack contour is marked by FAST feature point recognition, which reach for different road crack damage can be identified. After the simulation, the algorithm is transplanted to the Python on Zynq (PYNQ) system to achieve the purpose of crack identification. There are two parts to the innovation: First, using a lower-cost embedded camera to capture photos, and second, using the characteristics of large difference in gray value between crack region and other regions, the crack profile is marked by the way of FAST feature point recognition and use PYNQ to process. It makes the identification system more integrated and portable, and can judge the crack more accurately and reduce the cost.

If this Rep is useful for you please star ！

If you use this Rep（Include image and code）please cite this paper：
Z. Yuhan, Q. Juan, G. Zhiling, J. Kuncheng and C. Shiyuan, "Detection of Road Surface Crack Based on PYNQ," 2020 IEEE International Conference on Mechatronics and Automation (ICMA), 2020, pp. 1150-1154, doi: 10.1109/ICMA49215.2020.9233608.

@INPROCEEDINGS{9233608,  author={Yuhan, Zhang and Juan, Qin and Zhiling, Guo and Kuncheng, Jiang and Shiyuan, Cai},  booktitle={2020 IEEE International Conference on Mechatronics and Automation (ICMA)},   title={Detection of Road Surface Crack Based on PYNQ},   year={2020},  volume={},  number={},  pages={1150-1154},  doi={10.1109/ICMA49215.2020.9233608}}
