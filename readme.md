# Campus Placement Prediction

A machine learning project to predict student placement outcomes using academic and skill-based features.

## Project Overview

This project uses machine learning to predict whether a student will be placed during campus recruitment based on various academic and professional parameters. The model takes into account factors like CGPA, internships, projects, certifications, and test scores.

## Features Used

- CGPA
- Number of Internships  
- Number of Projects
- Number of Workshops/Certifications
- Aptitude Test Score
- Soft Skills Rating
- Extracurricular Activities
- Placement Training
- 10th Marks (SSC)
- 12th Marks (HSC)

## Tech Stack

- Python
- scikit-learn
- pandas
- numpy
- streamlit (for web interface)

## Model Details

The project uses a Gradient Boosting Classifier with the following parameters:
- Learning rate: 0.1
- Max depth: 3
- Max features: sqrt
- Min samples leaf: 2
- Min samples split: 10
- Number of estimators: 200
- Subsample: 0.8

## Project Structure

```
.
├── Data/
│   ├── Original.csv
│   ├── X.csv
│   └── y.csv
├── models/
│   ├── ct.pkl
│   └── model.pkl
├── app.py
├── EDA.ipynb
├── model.ipynb
├── modeling.ipynb
└── readme.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CampusPlacement.git
cd CampusPlacement
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Enter student details in the web interface to get placement prediction

## Web Interface

The application provides a simple web interface where users can input:
- CGPA (0-10 scale)
- Number of internships completed
- Number of projects completed
- Number of workshops/certificates obtained
- Aptitude test score (0-100)
- Soft skills rating (1-10)
- Extracurricular activities (Yes/No)
- Placement training completion (Yes/No)
- 10th marks percentage
- 12th marks percentage

## Model Training

The model was trained using:
- Train-test split: 80-20
- Cross-validation: 5 folds
- Hyperparameter tuning using GridSearchCV
- Performance metrics: Accuracy

## Files Description

- `app.py`: Streamlit web application for user interface
- `EDA.ipynb`: Exploratory Data Analysis notebook with visualizations
- `model.ipynb`: Initial model development and experimentation
- `modeling.ipynb`: Final model implementation with evaluation
- `Data/`: Directory containing training and testing datasets
- `models/`: Directory containing saved model files and transformers

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
