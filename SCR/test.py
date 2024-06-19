import tkinter as tk
import time

def on_screenshot_attempt():
    print("Screenshot attempt detected! Masking sensitive data...")
    mask_label.config(text="Sensitive data masked", fg="red")

# Exemple de fonction pour simuler la détection de tentatives de capture d'écran
def simulate_screenshot_detection():
    time.sleep(5)  # Simuler un délai avant la détection d'une tentative de capture d'écran
    on_screenshot_attempt()

# Fonction pour le premier bouton
def button1_action():
    data_label.config(text="Button 1 was clicked")
    print("Button 1 clicked")

# Fonction pour le deuxième bouton
def button2_action():
    data_label.config(text="Button 2 was clicked")
    print("Button 2 clicked")

root = tk.Tk()
root.title("Sensitive Data")

data_label = tk.Label(root, text="This is some sensitive data.")
data_label.pack()

mask_label = tk.Label(root, text="")
mask_label.pack()

# Ajouter les boutons
button1 = tk.Button(root, text="Button 1", command=button1_action)
button1.pack(pady=5)

button2 = tk.Button(root, text="Button 2", command=button2_action)
button2.pack(pady=5)

# Simuler la détection de tentatives de capture d'écran après un délai
root.after(1000, simulate_screenshot_detection)

root.mainloop()
