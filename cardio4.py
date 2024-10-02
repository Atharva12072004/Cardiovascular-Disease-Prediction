from tkinter import *
from tkinter import messagebox
import numpy as np
import joblib

# Load the model and scaler
model = joblib.load('model3.pkl')
scaler = joblib.load('skaler.pkl')

# Step 2: Create a Tkinter UI for Predictions
root = Tk()
root.title("Cardiovascular Disease Prediction")
root.geometry("500x600")  # Set window size

# Set background color
root.configure(bg="#f0f8ff")

# Function to add hover effect to buttons
def on_enter(e):
    e.widget['background'] = '#90EE90'

def on_leave(e):
    e.widget['background'] = '#98FB98'

# Function to make a prediction
def predict():
    try:
        # Get user inputs from the UI
        age = int(entry_age.get())
        gender = int(entry_gender.get())
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        sbp = float(entry_sbp.get())  # Systolic Blood Pressure
        dbp = float(entry_dbp.get())  # Diastolic Blood Pressure
        cholesterol = int(entry_cholesterol.get())
        glucose = int(entry_glucose.get())
        smoking = int(entry_smoking.get())
        alcohol = int(entry_alcohol.get())
        physical_activity = int(entry_activity.get())

        # Create the input array with the user data
        features = np.array([[age, gender, height, weight, sbp, dbp, cholesterol, glucose, smoking, alcohol, physical_activity]])

        # Scale the input features using the same scaler used during training
        scaled_features = scaler.transform(features)

        # Perform the prediction
        prediction = model.predict(scaled_features)[0]

        if prediction == 1:
            result_text = "The model predicts that you are at risk of cardiovascular disease."
        else:
            result_text = "The model predicts that you are NOT at risk of cardiovascular disease."

        messagebox.showinfo("Prediction Result", result_text)

        # Display the result
        label_result.config(text=f"Prediction: {result_text}")
        
    except Exception as e:
        label_result.config(text=f"Error: {str(e)}")

# Create a heading
Label(root, text="Cardiovascular Disease Prediction", font=("Arial", 30, "bold"), bg="#f0f8ff", fg="#333333").grid(row=0, columnspan=2, pady=20)

# Create input labels and text entry fields with styling
def create_label_and_entry(text, row):
    label = Label(root, text=text, bg="#f0f8ff", font=("Arial", 12, "bold"), fg="#333333")
    label.grid(row=row, column=0, pady=10, padx=20, sticky=W)
    entry = Entry(root, font=("Arial", 12), width=25)
    entry.grid(row=row, column=1, pady=10)
    return entry

# Creating input fields starting from row 1 (to leave space for the heading)
entry_age = create_label_and_entry("Age:", 1)
entry_gender = create_label_and_entry("Gender (0=Female, 1=Male):", 2)
entry_height = create_label_and_entry("Height (in cm):", 3)
entry_weight = create_label_and_entry("Weight (in kg):", 4)
entry_sbp = create_label_and_entry("Systolic Blood Pressure:", 5)
entry_dbp = create_label_and_entry("Diastolic Blood Pressure:", 6)
entry_cholesterol = create_label_and_entry("Cholesterol (0=Normal, 1=Above Normal, 2=Well Above Normal):", 7)
entry_glucose = create_label_and_entry("Glucose (0=Normal, 1=Above Normal, 2=Well Above Normal):", 8)
entry_smoking = create_label_and_entry("Smoking (0=No, 1=Yes):", 9)
entry_alcohol = create_label_and_entry("Alcohol (0=No, 1=Yes):", 10)
entry_activity = create_label_and_entry("Physical Activity (0=No, 1=Yes):", 11)

# Button styling
predict_button = Button(root, text="Predict", command=predict, font=("Arial", 12, "bold"), bg="#98FB98", activebackground="#90EE90", bd=3)
predict_button.grid(row=12, column=1, pady=20)

# Adding hover effect to the button
predict_button.bind("<Enter>", on_enter)
predict_button.bind("<Leave>", on_leave)

# Label to display the result with initial animation color
label_result = Label(root, text="", bg="#f0f8ff", font=("Arial", 14, "bold"))
label_result.grid(row=13, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
