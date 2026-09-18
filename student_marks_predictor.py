import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression

DATA_FILE = "student_marks_dataset.csv"

def train_model():
    data = pd.read_csv(DATA_FILE)
    X = data[["Study_Hours"]]
    y = data["Marks"]
    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_model()

def predict_marks():
    try:
        hours = float(hours_entry.get())
        if hours < 0:
            raise ValueError
        prediction = model.predict([[hours]])[0]
        prediction = max(0, min(100, prediction))
        result_label.config(text=f"Predicted Marks: {prediction:.2f} / 100")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid non-negative number.")

root = tk.Tk()
root.title("AI/ML Student Marks Predictor")
root.geometry("500x320")
root.resizable(False, False)

title = tk.Label(root, text="Student Marks Prediction", font=("Arial", 20, "bold"))
title.pack(pady=20)

subtitle = tk.Label(root, text="Linear Regression • AI/ML Mini Project", font=("Arial", 11))
subtitle.pack()

tk.Label(root, text="Enter study hours:", font=("Arial", 13)).pack(pady=(25, 8))
hours_entry = tk.Entry(root, font=("Arial", 14), justify="center")
hours_entry.pack()

predict_btn = tk.Button(root, text="Predict Marks", font=("Arial", 13, "bold"),
                        command=predict_marks, padx=20, pady=8)
predict_btn.pack(pady=20)

result_label = tk.Label(root, text="Predicted Marks: --", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

root.mainloop()
