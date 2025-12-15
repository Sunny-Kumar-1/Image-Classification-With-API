# Image Classification Web Application

This project is a web-based image classification application built using Python, Streamlit, and TensorFlow. It allows users to upload an image via a simple web interface and uses a pre-trained deep learning model to predict the category of the image.

The model appears to be trained on the CIFAR-10 dataset, capable of recognizing classes such as airplanes, automobiles, birds, cats, deer, dogs, frogs, horses, ships, and trucks.

## ✨ Features

* **User-Friendly Interface:** Built with Streamlit for easy image uploading and interaction.
* **Deep Learning Backend:** Utilizes a pre-trained TensorFlow/Keras model (`Image_classify.keras`) for accurate predictions.
* **Instant Classification:** Provides immediate feedback on uploaded images.
* **Research Notebook Included:** Includes the Jupyter notebook (`research.ipynb`) used for training the model.

## 🛠️ Technologies Used

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) - For building the web application interface.
* [TensorFlow / Keras](https://www.tensorflow.org/) - For loading and running the deep learning model.
* [Pillow (PIL)](https://python-pillow.org/) - For image processing.
* [NumPy](https://numpy.org/) - For numerical operations on image data.

## 📂 Project Structure

```bash
├── Image_classify.keras  # The pre-trained Keras classification model
├── app.py                # The main Streamlit application script
├── requirements.txt      # List of Python dependencies listed required to run the app
└── research.ipynb        # Jupyter notebook used for model training and development

🚀 Getting Started & Installation
Follow these steps to set up and run the project locally on your machine.

Prerequisites
Python 3.7 or higher installed.

Installation Steps
Clone the repository:

Bash

git clone [https://github.com/Sunny-Kumar-1/Image-Classification-With-API.git](https://github.com/Sunny-Kumar-1/Image-Classification-With-API.git)
cd Image-Classification-With-API
Create a virtual environment (Recommended):

Bash

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies: Install the required Python packages using requirements.txt:

Bash

pip install -r requirements.txt
💡 Usage
Once dependencies are installed, run the Streamlit application:

Bash

streamlit run app.py
Streamlit will start a local web server and typically open your default web browser automatically to http://localhost:8501.

Use the "Browse files" button on the web page to upload an image (JPG, PNG, or JPEG).

The application will display the uploaded image and the model's predicted classification.

👤 Author
Sunny Kumar - GitHub Profile
