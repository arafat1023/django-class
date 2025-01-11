import tkinter as tk
from tkinter import messagebox
import requests
import json

class ContactFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Us")

        self.name_label = tk.Label(root, text="Your Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.email_label = tk.Label(root, text="Your Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.subject_label = tk.Label(root, text="Subject:")
        self.subject_label.pack()
        self.subject_entry = tk.Entry(root)
        self.subject_entry.pack()

        self.message_label = tk.Label(root, text="Message:")
        self.message_label.pack()
        self.message_text = tk.Text(root, height=5)
        self.message_text.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.pack()

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        api_url = "http://127.0.0.1:8000/polls/api/contact/submit/"  # Replace with your Django server URL

        try:
            response = requests.post(api_url, data=data)
            response.raise_for_status()  # Raise an exception for bad status codes
            response_data = response.json()

            if response_data.get('status') == 'success':
                messagebox.showinfo("Success", response_data.get('message'))
                # Clear the form after successful submission
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.subject_entry.delete(0, tk.END)
                self.message_text.delete("1.0", tk.END)
            else:
                errors = response_data.get('errors', 'Unknown error')
                messagebox.showerror("Error", f"Error submitting form: {errors}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Network error: {e}")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding server response.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactFormApp(root)
    root.mainloop()