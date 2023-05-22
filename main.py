import streamlit as st

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height from centimeters to meters
    bmi = weight / (height_m ** 2)
    return bmi

def get_weight_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Health App ⚕️")
    st.write("Welcome to the BMI Health App!")
    
    weight = st.number_input("Enter your weight in kilograms")
    height = st.number_input("Enter your height in centimeters")
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        weight_category = get_weight_category(bmi)
        
        st.write("Your BMI: {:.1f}".format(bmi))
        st.write("Weight Category: {}".format(weight_category))
        
if __name__ == '__main__':
    main()
