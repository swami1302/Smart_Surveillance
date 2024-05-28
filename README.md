# Smart Surveillance - People Detection with OpenCV

## Overview

This project implements a smart surveillance system using OpenCV for people detection. It utilizes both the Histogram of Oriented Gradients (HOG) algorithm and the Haar Cascade algorithm for accurate detection of people in images and video streams.

## File Structure

- `main.py`: Main script for people detection using the Haar Cascade algorithm.
- `detect_img.py`: Script for detecting people in images using the HOG algorithm.
- `detect_vdo.py`: Script for detecting people in video streams using the HOG algorithm.
- `haarcascade_fullbody.xml`: Haar Cascade classifier for detecting full-body images.
- `Haar_Casscade`: File or component related to the Haar Cascade algorithm.
- `Hog_Algo`: File or component related to the Histogram of Oriented Gradients (HOG) algorithm.

## Usage

1. Install Python 3.x and OpenCV library on your system.
2. Clone or download the project repository.
3. Choose the appropriate script (`main.py`, `detect_img.py`, `detect_vdo.py`) based on your use case.
4. Run the selected script to perform people detection using the specified algorithm.

### Example Usage

For HOG algorithm (image detection):
```bash
python detect_img.py --image image.jpg
python main.py --video video.mp4
```
## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or enhancements, feel free to open an issue or create a pull request.


