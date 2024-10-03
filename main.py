import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model_filename = 'model/student_performance_model.pkl'
with open(model_filename, 'rb') as f:
    model = pickle.load(f)

# Function to predict student performance
def predict_student_performance(input_data):
    df = pd.DataFrame(input_data, index=[0])  # Convert input to dataframe
    prediction = model.predict(df)
    return prediction[0]

# Streamlit Web App
def main():
    # Set the title and description
    st.title("🎓 Student Performance Prediction App")
    st.markdown("""
    This application predicts students' final grades based on various features such as attendance rate, study hours, 
    previous grades, and extracurricular activities.
    """)

    # Add sidebar for customization
    st.sidebar.header("Adjust Model Parameters")

    # User input features
    gender = st.sidebar.selectbox("Gender", options=["Male", "Female"])
    attendance_rate = st.sidebar.slider("Attendance Rate (%)", min_value=50, max_value=100, value=85)
    study_hours = st.sidebar.slider("Study Hours per Week", min_value=5, max_value=40, value=15)
    previous_grade = st.sidebar.slider("Previous Grade (%)", min_value=50, max_value=100, value=80)
    extracurricular = st.sidebar.selectbox("Extracurricular Activities", options=["None", "Some", "A Lot"])
    parental_support = st.sidebar.selectbox("Parental Support", options=["Low", "Medium", "High"])

    # Convert categorical values to numeric
    gender_num = 0 if gender == "Male" else 1
    extracurricular_num = {"None": 0, "Some": 1, "A Lot": 2}[extracurricular]
    parental_support_num = {"Low": 0, "Medium": 1, "High": 2}[parental_support]

    # Predict button
    if st.button("Predict Final Grade"):
        input_data = {
            
            'AttendanceRate': attendance_rate,
            'StudyHoursPerWeek': study_hours,
            'PreviousGrade': previous_grade,
            'ExtracurricularActivities': extracurricular_num,
            'Gender': gender_num,
            'ParentalSupport': parental_support_num
        }

        # Predict grade
        final_grade = predict_student_performance(input_data)
        st.success(f"The predicted final grade is: {round(final_grade, 2)}")

    # A section to show the user how the input affects the result
    st.markdown("""
    ---
    **How to improve performance**:
    - Increasing your study hours and class participation can lead to a better final grade.
    - Having strong parental support and engaging in extracurricular activities also positively impacts performance.
    """)

if __name__ == '__main__':
    main()
