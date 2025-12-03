import tkinter as tk
from tkinter import messagebox
import re
import validators

suspicious_keyword = ['login','secure','update','free','verify','bank','account','webscr','paypal','signin','confirm','security']

def has_ip(url):
    return bool(re.search(r'https?://(\d{1,3}\.){3}\d{1,3}',url))

def count_dots(url):
    return url.count('.')

def has_suspicious_keyword(url):
    return any(word in url.lower() for word in suspicious_keyword)

def check_url(url):
    if not validators.url(url):
        return "Invalid URL","gray"
    
    score = 0

    if len(url) > 75:
        score += 1
    if '@' in url:
        scope +=1
    if has_ip(url):
        score +=2
    if has_suspicious_keyword(url):
        score +=2
    if count_dots(url) > 5:
        score +=1

    if score >= 4:
        return "Phising","red"
    elif 2 <= score < 4:
        return "Suspicious", "Orange"
    else:
        return "safe","green"
    
#----------------GUI---------------#
def run_gui():
    def on_check():
        url = url_entry.get()
        label, color = check_url(url)
        result_var.set(f"Result: {label}")
        result_label.config(fg=color)

    app = tk.Tk()
    app.title("Phising URL Detector")
    app.geometry("400x220")
    app.resizable(False,False)

    heading = tk.Label(app, text="🔍 Phishing URL Detector", font=("Helvetica", 16, "bold"))
    heading.pack(pady=10)

    url_entry = tk.Entry(app, width=45, font=("Arial", 12))
    url_entry.pack(pady=10)
    url_entry.insert(0,"https://example.com")

    check_button = tk.Button(app, text="Check URl", command=on_check, font=("Arial",12), bg='#007acc', fg="white")
    check_button.pack(pady=5)

    result_var = tk.StringVar()
    result_label = tk.Label(app, textvariable=result_var, font=("Arial", 14,"bold"))
    result_label.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    run_gui()