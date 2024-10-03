import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Load the dataset
df = pd.read_csv('D:\projects\orison_tech\student_performance\data\student_performance.csv')

# Instantiate LabelEncoders
le_gender = LabelEncoder()
le_parental_support = LabelEncoder()

# Fit and transform the Gender and Parental Support columns
df['Gender'] = le_gender.fit_transform(df['Gender'])
df['ParentalSupport'] = le_parental_support.fit_transform(df['ParentalSupport'])

# Step 2: Prepare the feature set (X) and target variable (y)
X = df[['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade', 
        'ExtracurricularActivities', 'Gender', 'ParentalSupport']]
y = df['FinalGrade']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create the regression model
model = LinearRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# step 6 Save the model
model_filename = 'D:\projects\orison_tech\student_performance\model\student_performance_model.pkl'
with open(model_filename, 'wb') as f:
    pickle.dump(model, f)

print("Model has been trained and saved!")