# CargoScan

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url]

<!-- ABOUT THE PROJECT -->
## 📝 About The Project
*CargoScan* is an automated railway wagon number identification and tracking system designed to optimize the process of managing and monitoring freight traffic. The system uses computer vision technology to scan and identify individual wagons as they move through the railway network.

[![Demonstration Screenshot][demonstration-screenshot]](#)

**🆕 NEW**: *CargoScan* Web App Edition: `app.py` ~ just clone and run:

[![Demon Screen][demonstration-screenshot-1]](#)

[![Demon Screen][demonstration-screenshot-2]](#)

[![Demon Screen][demonstration-screenshot-3]](#)

----

### 👩‍🏭 Steps
1. **Data Collection;**
2. **Data Preprocessing;**
3. **Splitting the Dataset;**
4. **Model Training;**
5. **Model Evaluation;**
6. **Testing and Performance Assessment;**
7. **Setting Pre-Trained Optical Character Recognition (OCR);**
8. **Extracting data to a database;**

### 💾 Dataset & Training
*📈 Some statistics about dataset and training process*

[![Stats-1][data-1]](#)

[![Stats-2][data-2]](#)

*🔗 Links to the dataset:*
 - [>>>Dataset01<<<](https://drive.google.com/drive/folders/13qqmCHw7FyNBMU8W6fCJUX2Jh5vYw0y0?usp=sharing)
 - [>>>Dataset02<<<](https://drive.google.com/drive/folders/1EGlsHoJ2HWnBuaLSojRGpQ3Fl9N0RBMp?usp=sharing)
 - [>>>Dataset03<<<](https://drive.google.com/drive/folders/1ppZ05ZqkRegm6slyucGaWam32e-UwrZQ?usp=sharing)

*🔗 Link to the trained model: [>>>Click here<<<](https://drive.google.com/file/d/13W6pxMAM7Ic-TgNmzpDYTtVKKrR4JBVe/view?usp=share_link)*

*🔗 Link to the Processed & Annotated Dataset: [>>>Click here<<<](https://universe.roboflow.com/customobjectdetectionyolov8/cargoscan/)*

### 🦾 Prerequisites
 - *Python 3.7 or above*
 - *OpenCV (cv2)*
 - *Ultralytics (YOLOv8)*
 - *PyTesseract*
 
 ⚙️ Download tesseract here: https://github.com/UB-Mannheim/tesseract/wiki & install pytesseract using:  `pip3 install pytesseract`


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
 - [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/@murtazasworkshop)
 - [OCR - Tesseract](https://tesseract-ocr.github.io/)
 - [Ultralytics - YOLOv8](https://docs.ultralytics.com/)
 - [Roboflow](https://universe.roboflow.com/customobjectdetectionyolov8/cargoscan/)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/silvermete0r/CargoScan.svg?style=flat-square
[contributors-url]: https://github.com/silvermete0r/CargoScan/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/silvermete0r/CargoScan.svg?style=flat-square
[forks-url]: https://github.com/silvermete0r/CargoScan/network/members
[stars-shield]: https://img.shields.io/github/stars/silvermete0r/CargoScan.svg?style=flat-square
[stars-url]: https://github.com/silvermete0r/CargoScan/stargazers
[issues-shield]: https://img.shields.io/github/issues/silvermete0r/CargoScan.svg?style=flat-square
[issues-url]: https://github.com/silvermete0r/CargoScan/issues
[demonstration-screenshot]: https://sun9-80.userapi.com/impg/b30lzz6uKJUw50O8EfH5EUT6-LdIxPD4zKHxNw/SgfP3u7DWi0.jpg?size=1443x811&quality=95&sign=977b2b2316a246a3cabbde3f0fe3378c&type=album
[demonstration-screenshot-1]: https://sun9-73.userapi.com/impg/i28f7cm4D2xlgYAvxPs2EYPbKhcTkoVd2VcseQ/dQZOWYNR3Jw.jpg?size=1335x1165&quality=95&sign=e8d44895da12f6ffd10afddd3c75f2a7&type=album
[demonstration-screenshot-2]: https://sun9-62.userapi.com/impg/nlbHlnb-40sWJLmc3AhzadwOh0_A4Xa7buFePA/Sh1nKKZxxbI.jpg?size=1335x522&quality=95&sign=f6cdcfd533e68857e41feb48f64f512f&type=album
[demonstration-screenshot-3]: https://sun9-80.userapi.com/impg/LnZ6nuHlX5Chhyilb6z4XPbZHmD3rcUDFRIa3Q/OGqHOYGc2Yo.jpg?size=1338x534&quality=95&sign=012b743f4bb110a6d19a0e8f1d0f7747&type=album
[data-1]: https://sun9-7.userapi.com/impg/BUsUKZQ_TcXPrG_gU3L9kVzHo3OiAEQQdNXdXA/nZy6fIu4NKk.jpg?size=1693x478&quality=95&sign=25add4bc81a147440512ff90dd54b895&type=album
[data-2]: https://sun9-64.userapi.com/impg/rmY_egki5ONYSSW6_MO_TCPUuSGCwqjotmFgtg/oxZV67HyxQM.jpg?size=1234x910&quality=95&sign=c241b73c00574ff1f0f1ebb9b13855d8&type=album
