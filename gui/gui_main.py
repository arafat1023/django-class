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
            # Include post ID in the display for internal reference
            post_list.insert(tk.END, f"ID {post['id']}: {post['title']} - {post['content']}")
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
            fetch_posts()
            title_entry.delete(0, tk.END)
            content_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Failed to create post: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")

# Function to update a post
def update_post():
    selected = post_list.curselection()
    if not selected:
        messagebox.showwarning("Validation Error", "Please select a post to update.")
        return

    post_index = selected[0]
    post_data = post_list.get(post_index).split(":")[0]  # Extract ID part
    post_id = post_data.split(" ")[1]  # Fetch only the ID

    title = title_entry.get()
    content = content_entry.get()

    if not title or not content:
        messagebox.showwarning("Validation Error", "Both title and content are required.")
        return

    try:
        response = requests.post(f"http://127.0.0.1:8000/api/update-post/{post_id}/", data={"title": title, "content": content})
        if response.status_code == 200:
            messagebox.showinfo("Success", "Post updated successfully!")
            fetch_posts()
        else:
            messagebox.showerror("Error", f"Failed to update post: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")


def delete_post():
    selected = post_list.curselection()
    if not selected:
        messagebox.showwarning("Validation Error", "Please select a post to delete.")
        return

    post_index = selected[0]
    post_data = post_list.get(post_index).split(":")[0]  # Extract ID part
    post_id = post_data.split(" ")[1]  # Fetch only the ID

    try:
        response = requests.post(f"http://127.0.0.1:8000/api/delete-post/{post_id}/")
        if response.status_code == 200:
            messagebox.showinfo("Success", "Post deleted successfully!")
            fetch_posts()
        else:
            messagebox.showerror("Error", f"Failed to delete post: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")


# Main Frame Setup
main_frame = tk.Frame(root)
main_frame.pack(pady=10)

# Fetch Posts Section
tk.Button(main_frame, text="Fetch Posts", command=fetch_posts).pack(side=tk.LEFT, padx=5)
post_list = tk.Listbox(main_frame, width=50, height=15)
post_list.pack(side=tk.RIGHT)

# Form for Post Operations
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Title:").grid(row=0, column=0)
title_entry = tk.Entry(form_frame, width=40)
title_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Content:").grid(row=1, column=0)
content_entry = tk.Entry(form_frame, width=40)
content_entry.grid(row=1, column=1)

# Buttons
tk.Button(form_frame, text="Create Post", command=create_post).grid(row=2, column=0, pady=5)
tk.Button(form_frame, text="Update Post", command=update_post).grid(row=2, column=1, pady=5)
tk.Button(form_frame, text="Delete Post", command=delete_post).grid(row=2, column=2, pady=5)

# Run Tkinter loop
root.mainloop()
