# Kidney Disease Classifier

## Overview
The Kidney Disease Classifier is a web application designed to analyze CT scan images and predict whether the scan is normal or indicates the presence of a tumor. Leveraging the VGG16 architecture as a base model, the classifier has been fine-tuned with a dataset of CT scan images, achieving an accuracy of 89%. The model is modular, allowing for enhanced accuracy with an increased number of epochs during training.

## Features
- **Image Upload**: Users can upload CT scan images for analysis.
- **Prediction Result**: The application displays predictions, changing the result box color to green for normal scans and red for scans with tumors.
- **Modular Design**: The architecture is designed for easy scalability and adjustments.

## Tech Stack
- **Deep Learning Framework**: 
  - TensorFlow (for model training and inference)
- **Data Handling**:
  - Pandas (for data manipulation)
  - NumPy (for numerical operations)
- **Model Management**:
  - MLflow (for tracking experiments and managing models)
  - DVC (Data Version Control for dataset versioning)
- **Visualization**:
  - Matplotlib (for plotting)
  - Seaborn (for statistical data visualization)
- **Web Framework**:
  - Flask (for building the web application)
  - Flask-CORS (to handle Cross-Origin Resource Sharing)
- **Other Libraries**:
  - Python-box (for managing configurations)
  - PyYAML (for YAML parsing)
  - TQDM (for progress bars in loops)
  - Ensure (for ensuring type hints)
  - Joblib (for model serialization)
  - Types-PyYAML (for type checking)
  - SciPy (for scientific computations)
  - Gdown (for downloading files from Google Drive)

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mShubham18/kidney-disease-dl-project.git
   cd kidney-disease-dl-project
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. Open the web application in your browser.
2. Upload a CT scan image using the provided upload button.
3. Click on the 'Predict' button to receive the analysis result.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## Acknowledgments
- [VGG16 Model](https://arxiv.org/abs/1409.1556)
- [MLflow](https://mlflow.org/)
- [DVC](https://dvc.org/)

## Contact
For any inquiries, please contact:
- **Shubham Mishra**: [GitHub](https://github.com/mShubham18)

Happy Coding ;)
