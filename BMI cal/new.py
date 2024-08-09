import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import json
from datetime import datetime

class BMI_Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("400x300")

        self.weight_label = tk.Label(self, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        self.height_label = tk.Label(self, text="Height (cm):")
        self.height_label.pack()
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        self.calculate_button = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.save_button = tk.Button(self, text="Save Data", command=self.save_data)
        self.save_button.pack()

        self.show_history_button = tk.Button(self, text="Show History", command=self.show_history)
        self.show_history_button.pack()

        self.data = []

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # Convert height to meters
            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)
            self.result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")

            # Save data for history
            self.data.append({"weight": weight, "height": height * 100, "bmi": bmi, "category": category, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def save_data(self):
        with open("bmi_data.json", "w") as file:
            json.dump(self.data, file)
        messagebox.showinfo("Data Saved", "BMI data has been saved successfully.")

    def show_history(self):
        if not self.data:
            messagebox.showinfo("No Data", "No BMI data available.")
            return

        weights = [entry["weight"] for entry in self.data]
        dates = [entry["date"] for entry in self.data]

        plt.plot(dates, weights, marker='o')
        plt.title("Weight History")
        plt.xlabel("Date")
        plt.ylabel("Weight (kg)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = BMI_Calculator()
    app.mainloop()