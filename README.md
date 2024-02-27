# Adult Income Prediction App

This Streamlit application predicts whether a person's income is <=50K or >50K based on various demographic factors.

## Overview

The app uses a RandomForestClassifier model trained on demographic data to predict income levels. Users can input their details through a user-friendly web interface, and the model will output a prediction for their income bracket.

## Features

- Predict income level based on personal information
- Easy-to-use web interface
- Input validation and user feedback

## How to Use

1. Enter your age.
2. Select your work class from the dropdown.
3. Enter your final weight (continuous).
4. Select your education level from the dropdown.
5. Enter your education number (continuous).
6. Select your marital status from the dropdown.
7. Select your occupation from the dropdown.
8. Select your relationship status from the dropdown.
9. Select your race from the dropdown.
10. Select your gender (Male/Female).
11. Enter your capital gain (continuous).
12. Enter your capital loss (continuous).
13. Enter your hours worked per week (continuous).
14. Select your country from the dropdown.

After filling out all the information, click the "Submit" button to see the prediction.

## Installation

To run this application on your local machine, you will need Python and Streamlit installed.

```
pip install streamlit
pip install pickle
pip install pandas
```

After installing the necessary packages, you can start the app by running:

```
python -m streamlit run app.py
```

## Interface

Explore the Adult Income Prediction App's interface. Below is a snapshot of App in action:
![image](https://github.com/asma-hachaichi/Adult-Income-Prediction/assets/72823346/280d62bd-48e3-48ef-9e02-16498ed52c42)

## Contributions

Contributions are welcome. Please fork the project and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
