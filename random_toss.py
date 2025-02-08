import random
import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread

def flip_coin(times, heads_choice, tails_choice):
    """Simulate flipping a coin 'times' times and return results with percentages and choice mapping."""
    results = {"Heads": 0, "Tails": 0}
    
    for _ in range(times):
        flip = random.choice(["Heads", "Tails"])
        results[flip] += 1
    
    # Calculate percentages
    heads_percentage = (results["Heads"] / times) * 100
    tails_percentage = (results["Tails"] / times) * 100
    
    # Determine the selected choice
    final_choice = heads_choice if results["Heads"] > results["Tails"] else tails_choice
    
    return final_choice.upper(), {
        "Heads": results["Heads"],
        "Tails": results["Tails"],
        "Heads Percentage": round(heads_percentage, 2),
        "Tails Percentage": round(tails_percentage, 2)
    }

def run_simulation():
    def show_loading_then_flip():
        loading_label.pack()
        root.update()
        time.sleep(2)
        loading_label.pack_forget()
        complete_simulation()
    
    Thread(target=show_loading_then_flip).start()

def complete_simulation():
    try:
        num_flips = int(trials_entry.get())
        heads_choice = heads_entry.get()
        tails_choice = tails_entry.get()
        guess_choice = guess_entry.get()
        
        if num_flips <= 0 or not heads_choice or not tails_choice or not guess_choice:
            raise ValueError("Invalid input values")
        
        final_choice, flip_results = flip_coin(num_flips, heads_choice, tails_choice)
        
        result_window = tk.Toplevel(root)
        result_window.title("Coin Flip Results")
        result_window.geometry("400x300")
        
        tk.Label(result_window, text=final_choice, font=("Arial", 24, "bold")).pack(pady=10)
        result_text = "\n".join([f"{key}: {value}" for key, value in flip_results.items()])
        tk.Label(result_window, text=result_text, font=("Arial", 12)).pack()
        
        guess_result = "Correct!" if final_choice == guess_choice.upper() else "Incorrect!"
        tk.Label(result_window, text=f"Your Guess: {guess_choice}\nResult: {guess_result}", font=("Arial", 12, "bold")).pack(pady=10)
        
        return_button = tk.Button(result_window, text="Return", command=result_window.destroy)
        return_button.pack(pady=10)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values for trials and choices.")

# Create GUI window
root = tk.Tk()
root.title("Coin Flip Simulator")
root.geometry("400x350")

tk.Label(root, text="Enter number of trials:").pack()
trials_entry = tk.Entry(root)
trials_entry.pack()

tk.Label(root, text="Enter choice for Heads:").pack()
heads_entry = tk.Entry(root)
heads_entry.pack()

tk.Label(root, text="Enter choice for Tails:").pack()
tails_entry = tk.Entry(root)
tails_entry.pack()

tk.Label(root, text="Guess the result:").pack()
guess_entry = tk.Entry(root)
guess_entry.pack()

loading_label = tk.Label(root, text="⚫ Rolling...", font=("Arial", 24, "bold"))

flip_button = tk.Button(root, text="Flip Coin", command=run_simulation)
flip_button.pack(pady=10)

root.mainloop()