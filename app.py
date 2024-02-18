import streamlit as st
import pandas as pd
import pickle

# Loading the adult income prediction model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Adult Income Prediction')

# Create a form for user input
with st.form(key='my_form'):
    age = st.number_input('Enter age:',min_value=15, max_value=100, value=40, step=1, format="%d")
    workclass_options = ['Never-worked', 'Without-pay', 'Self-emp-not-inc', 'Self-emp-inc',
    'Private', 'Local-gov', 'State-gov', 'Federal-gov']
    workclass = workclass_options.index(st.selectbox("Select workclass:", workclass_options))
    fnlwgt = st.number_input('Enter final weight:',value=1.896641e+05)
    education_options = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th',
    '10th', '11th', '12th', 'HS-grad', 'Some-college',
    'Assoc-voc', 'Assoc-acdm', 'Prof-school', 'Bachelors',
    'Masters', 'Doctorate']
    education = education_options.index(st.selectbox("Select education:", education_options))
    educational_num = st.number_input('Enter educational number:',min_value=0, max_value=20, value=10, step=1, format="%d")
    marital_options = ['Never-married', 'Married-spouse-absent', 'Separated',
    'Divorced', 'Widowed', 'Married-civ-spouse', 'Married-AF-spouse']
    marital_status = marital_options.index(st.selectbox("Select marital status:", marital_options))
    occupation_options = ['Priv-house-serv', 'Other-service', 'Handlers-cleaners', 'Farming-fishing',
    'Machine-op-inspct', 'Transport-moving', 'Craft-repair', 'Adm-clerical',
    'Sales', 'Tech-support', 'Protective-serv', 'Prof-specialty',
    'Exec-managerial', 'Armed-Forces']
    occupation = occupation_options.index(st.selectbox("Select occupation:", occupation_options))
    relationship_options = ['Own-child', 'Other-relative', 'Not-in-family',
    'Unmarried', 'Wife', 'Husband']
    relationship = relationship_options.index(st.selectbox("Select relationship:", relationship_options))
    race_options = ['Black', 'White', 'Asian-Pac-Islander', 'Other', 'Amer-Indian-Eskimo']
    race = st.selectbox('Select race:', race_options)
    black = 1 if race=='Black' else 0
    white = 1 if race=='White' else 0
    asian = 1 if race=='Asian-Pac-Islander' else 0
    other = 1 if race=='Other' else 0
    indian = 1 if race=='Amer-Indian-Eskimo' else 0
    gender = st.radio("Select gender:", ('Male', 'Female'))
    male = 1 if gender == 'Male' else 0
    female = 1 if gender == 'Female' else 0
    capital_gain = st.number_input('Enter capital gain:',min_value=0, max_value=99999, value=7452, step=1, format="%d")
    capital_loss = st.number_input('Enter capital loss:',min_value=0, max_value=99999, value=87, step=1, format="%d")
    hpw = st.number_input('Enter hours per week:',min_value=0, max_value=100, value=40, step=1, format="%d")
    country_options = {
        'United-States': 1, 'Canada': 1, 'England': 1, 'Germany': 1, 'Ireland': 1, 
        'France': 1, 'Holand-Netherlands': 1, 'Italy': 1, 'Scotland': 1,
        'Philippines': 2, 'India': 2, 'China': 2, 'Taiwan': 2, 'Japan': 2, 
        'South': 2, 'Iran': 2, 'Hong': 2,
        'Mexico': 3, 'Puerto-Rico': 3, 'El-Salvador': 3, 'Cuba': 3, 'Jamaica': 3,
        'Dominican-Republic': 3, 'Guatemala': 3, 'Columbia': 3, 'Haiti': 3,
        'Nicaragua': 3, 'Peru': 3, 'Ecuador': 3, 'Trinadad&Tobago': 3,
        'Vietnam': 4, 'Thailand': 4, 'Cambodia': 4, 'Laos': 4, 'Yugoslavia': 4,
        'Poland': 4, 'Hungary': 4, 'Portugal': 4, 'Greece': 4,
        'Outlying-US(Guam-USVI-etc)': 4, 'Honduras': 4
    }
    selected_country = st.selectbox("Select Country:", list(country_options.keys()))
    country = country_options[selected_country]

    # Submit button.
    submitted = st.form_submit_button('Submit')

# Process the input and display the predicted result
if submitted:
    feature_names = ['age', 'workclass', 'fnlwgt', 'education', 'educational-num',
                 'marital-status', 'occupation', 'relationship', 'capital-gain',
                 'capital-loss', 'hours-per-week', 'native-country',
                 'race_Amer-Indian-Eskimo', 'race_Asian-Pac-Islander', 'race_Black',
                 'race_Other', 'race_White', 'gender_Female', 'gender_Male']

    person = [age, workclass, fnlwgt, education, educational_num, marital_status, occupation, relationship, 
              capital_gain, capital_loss, hpw, country, indian, asian, black, other, white,
              female, male]
    
    print(person)

    df_person = pd.DataFrame([person], columns=feature_names)
    prediction = model.predict(df_person)  # Pass the input to your model's prediction function
    if prediction:
        income = ">50K"
    else:
        income = "<=50K"
    st.write(f"Predicted income: {income}")