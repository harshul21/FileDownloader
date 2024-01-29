import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from urllib.parse import urlparse
import os

class FileDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Downloader")

        # Main Frame
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(padx=20, pady=20)

        # URL Entry
        self.url_label = tk.Label(self.main_frame, text="Enter Image URL:", bg="#f0f0f0", font=("Helvetica", 12))
        self.url_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        self.url_entry = tk.Entry(self.main_frame, width=50, bd=2, relief="groove", font=("Helvetica", 12))
        self.url_entry.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

        # Download Button
        self.download_button = tk.Button(self.main_frame, text="Download File", command=self.download_file, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.download_button.grid(row=1, column=1, padx=(10, 0), pady=(0, 10), sticky="w")

    def download_file(self):
        url = self.url_entry.get().strip()
        try:
            if not url:
                messagebox.showwarning("Warning", "Please enter a valid URL.")
                return

            response = requests.get(url)
            if response.status_code != 200:
                messagebox.showerror("Error", f"Failed to download file. Status Code: {response.status_code}")
                return

            # Extract filename and extension from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            extension = os.path.splitext(filename)[1]

            # Prompt user to choose a location to save the file
            file_path = filedialog.asksaveasfilename(defaultextension=extension, filetypes=[("All files", "*.*")])
            if file_path:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                messagebox.showinfo("Success", "File downloaded successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDownloaderApp(root)
    root.mainloop()
