import tkinter as tk
from tkinter import messagebox
import threading

def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

def generate_binary(prime_list):
    binary_outputs = []
    for prime in prime_list:
        ones = '1' * prime
        zeros = '0' * (prime - 1)
        binary_outputs.append(ones + zeros)
    return binary_outputs

def binary_to_decimal(binary):
    return int(binary, 2)

def find_perfect_numbers():
    try:
        limit = int(entry_limit.get())
        if limit < 2:
            messagebox.showerror("Error", "Please enter a limit greater than or equal to 2.")
        else:
            text_output.config(state="normal")
            text_output.delete("1.0", tk.END)  # Clear the text widget
            text_output.config(state="disabled")
            threading.Thread(target=calculate_perfect_numbers, args=(limit,)).start()
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid integer.")

def calculate_perfect_numbers(limit):
    prime_list = sieve_of_eratosthenes(limit)
    binary_outputs = generate_binary(prime_list)
    for binary in binary_outputs:
        decimal_value = binary_to_decimal(binary)
        if is_perfect_number(decimal_value):
            text_output.config(state="normal")
            text_output.insert(tk.END, f"Binary: {binary} - Decimal: {decimal_value}\n")
            text_output.config(state="disabled")
            text_output.see(tk.END)
            text_output.update_idletasks()
    messagebox.showinfo("Calculation Finished", "Perfect number search finished!")

def on_enter(event=None):
    find_perfect_numbers()

# Create GUI window
root = tk.Tk()
root.title("Perfect Number Finder")

# Create input label and entry
label_limit = tk.Label(root, text="Enter the upper limit for prime numbers:")
label_limit.pack()
entry_limit = tk.Entry(root)
entry_limit.pack()

# Bind Enter key to entry widget
entry_limit.bind("<Return>", on_enter)

# Create find button
button_find = tk.Button(root, text="Find Perfect Numbers", command=find_perfect_numbers)
button_find.pack()

# Create output text area
text_output = tk.Text(root, height=10, width=50)
text_output.pack(fill="both", expand=True)

# Run the GUI
root.mainloop()
