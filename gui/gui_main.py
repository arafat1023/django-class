import tkinter as tk
from tkinter import messagebox
import requests

# Tkinter window setup
root = tk.Tk()
root.title("Blog Manager")
root.geometry("500x500")

# Function to fetch posts from Django backend
def fetch_posts():
    try:
        response = requests.get("http://127.0.0.1:8000/api/posts/")
        posts = response.json()
        post_list.delete(0, tk.END)  # Clear the listbox
        for post in posts:
            post_list.insert(tk.END, f"{post['title']}: {post['content']}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch posts: {e}")

# Function to create a new post
def create_post():
    title = title_entry.get()
    content = content_entry.get()
    if not title or not content:
        messagebox.showwarning("Validation Error", "Both title and content are required.")
        return

    try:
        response = requests.post("http://127.0.0.1:8000/api/create-post/", data={"title": title, "content": content})
        if response.status_code == 201:
            messagebox.showinfo("Success", "Post created successfully!")
            fetch_posts()  # Refresh the list
            title_entry.delete(0, tk.END)
            content_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Failed to create post: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")

# UI Components for fetching posts
fetch_button = tk.Button(root, text="Fetch Posts", command=fetch_posts)
fetch_button.pack(pady=10)

post_list = tk.Listbox(root, width=60, height=10)
post_list.pack(pady=10)

# UI Components for creating a post
tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

tk.Label(root, text="Content:").pack()
content_entry = tk.Entry(root, width=40)
content_entry.pack(pady=5)

create_button = tk.Button(root, text="Create Post", command=create_post)
create_button.pack(pady=10)

# Run Tkinter loop
root.mainloop()
