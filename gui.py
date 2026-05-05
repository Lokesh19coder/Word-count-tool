import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from utils import analyze_text

def open_file():
    file_path = filedialog.askopenfilename(title="Select Text File")

    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    line_count, word_count, char_count, most_common = analyze_text(text)

    # Display results
    result_text.set(
        f"Lines: {line_count}\n"
        f"Words: {word_count}\n"
        f"Characters: {char_count}"
    )

    # Display top words
    top_words_box.delete("1.0", tk.END)
    for word, count in most_common:
        top_words_box.insert(tk.END, f"{word} : {count}\n")

    # Plot graph
    words = [w for w, _ in most_common]
    counts = [c for _, c in most_common]

    plt.figure()
    plt.bar(words, counts)
    plt.title("Top Word Frequency")
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.show()

# GUI window
root = tk.Tk()
root.title("Word Count Tool")
root.geometry("400x500")

# Title
tk.Label(root, text=" Word Count Tool", font=("Arial", 16, "bold")).pack(pady=10)

# Button
tk.Button(root, text=" Upload File", command=open_file, bg="#4CAF50", fg="white").pack(pady=10)

# Result label
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack(pady=10)

# Top words box
tk.Label(root, text=" Top Words", font=("Arial", 12, "bold")).pack()
top_words_box = tk.Text(root, height=10, width=40)
top_words_box.pack(pady=5)

# Run app
root.mainloop()