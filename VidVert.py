import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

def convert_mov_to_mp4(input_file, output_folder):
    try:
        video_clip = VideoFileClip(input_file)
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.mp4')
        video_clip.write_videofile(output_file, codec='libx264')
        messagebox.showinfo("Success", f"Conversion complete! Saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_input_file():
    input_file = filedialog.askopenfilename(filetypes=[("MOV files", "*.mov")])
    if input_file:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_file)

def browse_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_folder)

def start_conversion():
    input_file = input_entry.get()
    output_folder = output_entry.get()
    if not input_file or not output_folder:
        messagebox.showwarning("Input required", "Please select both input file and output folder.")
    else:
        convert_mov_to_mp4(input_file, output_folder)

# Create the main window
root = tk.Tk()
root.title("MOV to MP4 Converter")

# Input file selection
tk.Label(root, text="Select MOV file:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_input_file).grid(row=0, column=2, padx=10, pady=10)

# Output folder selection
tk.Label(root, text="Select output folder:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_output_folder).grid(row=1, column=2, padx=10, pady=10)

# Convert button
tk.Button(root, text="Convert", command=start_conversion).grid(row=2, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()