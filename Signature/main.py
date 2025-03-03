import tkinter as tk
from tkinter import ttk, filedialog
from signature import match

THRESHOLD = 85

def browse(entry):
    if (file := filedialog.askopenfilename(filetypes=[("Image Files", "*.jpeg;*.png;*.jpg")])):
        entry.delete(0, tk.END)
        entry.insert(tk.END, file)

def check_similarity(e1, e2, label):
    try:
        result = match(e1.get(), e2.get()) if e1.get() and e2.get() else "⚠️ Please select both images."
        label.config(text=f"✅ Match: {result}%" if isinstance(result, (int, float)) and result >= THRESHOLD else f"❌ No Match: {result}%", foreground="green" if result >= THRESHOLD else "red")
    except Exception as e:
        label.config(text=f"⚠️ Error: {e}", foreground="red")

def main():
    root = tk.Tk()
    root.title("Signature Matching")
    root.geometry("500x300")
    root.configure(bg="#f7f7f7")
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)

    ttk.Label(frame, text="Compare Signatures", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
    e1, e2 = ttk.Entry(frame, width=40), ttk.Entry(frame, width=40)
    for i, (text, entry) in enumerate([("Signature 1:", e1), ("Signature 2:", e2)]):
        ttk.Label(frame, text=text, font=("Arial", 10)).grid(row=i+1, column=0, sticky="w", pady=5)
        entry.grid(row=i+1, column=1, padx=5)
        ttk.Button(frame, text="Browse", command=lambda e=entry: browse(e)).grid(row=i+1, column=2, padx=5)

    result_label = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
    result_label.grid(row=4, column=0, columnspan=3, pady=10)
    ttk.Button(frame, text="Compare", command=lambda: check_similarity(e1, e2, result_label)).grid(row=3, column=0, columnspan=3, pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
