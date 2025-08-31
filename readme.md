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

## Usage

1. Clone the repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

4. Enter student details in the web interface to get placement prediction

## Web Interface

The application provides a simple web interface where users can input:
- CGPA
- Number of internships
- Number of projects
- Number of workshops/certificates
- Aptitude test score
- Soft skills rating
- Extracurricular activities (Yes/No)
- Placement training (Yes/No)
- 10th marks
- 12th marks

## Model Training

The model was trained using:
- Train-test split: 80-20
- Cross-validation: 5 folds
- Hyperparameter tuning using GridSearchCV

## Files Description

- `app.py`: Streamlit web application
- `EDA.ipynb`: Exploratory Data Analysis  
- `model.ipynb`: Initial model development
- `modeling.ipynb`: Detailed modeling and evaluation
- `Data`: Contains training and testing datasets
- `models`: Contains saved