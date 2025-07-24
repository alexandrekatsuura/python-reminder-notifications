import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from reminder_service import ReminderService

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reminder Application")
        self.geometry("400x300")

        self.reminder_service = ReminderService()

        self.create_widgets()

    def create_widgets(self):
        # Reminder Text
        tk.Label(self, text="Reminder:").pack(pady=5)
        self.reminder_text = tk.Entry(self, width=50)
        self.reminder_text.pack(pady=5)

        # Date and Time
        tk.Label(self, text="Date (YYYY-MM-DD):").pack(pady=5)
        self.date_entry = tk.Entry(self, width=50)
        self.date_entry.pack(pady=5)

        tk.Label(self, text="Time (HH:MM):").pack(pady=5)
        self.time_entry = tk.Entry(self, width=50)
        self.time_entry.pack(pady=5)

        # Add Reminder Button
        tk.Button(self, text="Add Reminder", command=self.add_reminder).pack(pady=10)

        # Reminders List
        tk.Label(self, text="Upcoming Reminders:").pack(pady=5)
        self.reminders_listbox = tk.Listbox(self, width=60, height=8)
        self.reminders_listbox.pack(pady=5)
        self.update_reminders_list()

    def add_reminder(self):
        text = self.reminder_text.get()
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()

        if not text or not date_str or not time_str:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            reminder_datetime_str = f"{date_str} {time_str}"
            reminder_datetime = datetime.strptime(reminder_datetime_str, "%Y-%m-%d %H:%M")
            self.reminder_service.add_reminder(text, reminder_datetime)
            messagebox.showinfo("Success", "Reminder added successfully!")
            self.reminder_text.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.update_reminders_list()
        except ValueError:
            messagebox.showerror("Date/Time Error", "Invalid date or time format. Use YYYY-MM-DD and HH:MM.")

    def update_reminders_list(self):
        self.reminders_listbox.delete(0, tk.END)
        reminders = self.reminder_service.get_all_reminders()
        for reminder in reminders:
            self.reminders_listbox.insert(tk.END, f"{reminder['text']} - {reminder['time'].strftime('%Y-%m-%d %H:%M')}")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()


