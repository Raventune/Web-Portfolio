import tkinter as tk
from tkinter import messagebox
import threading

class PerfectNumberFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Perfect Number Finder")
        self.root.geometry("800x600")
        
        self.label_limit = tk.Label(root, text="Enter the upper limit for prime numbers:")
        self.label_limit.pack()
        
        self.entry_limit = tk.Entry(root)
        self.entry_limit.pack()
        
        self.button_find = tk.Button(root, text="Find Perfect Numbers", command=self.start_calculation)
        self.button_find.pack()
        
        self.button_cancel = tk.Button(root, text="Cancel", command=self.cancel_calculation, state="disabled")
        self.button_cancel.pack()
        
        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack(fill="both", expand=True)
        
        self.cancelled = threading.Event()

    def is_perfect_number(self, n):
        if n <= 1:
            return False
        divisors_sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors_sum += i
                if i != n // i:
                    divisors_sum += n // i
        return divisors_sum == n

    def sieve_of_eratosthenes(self, limit):
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

    def generate_binary(self, prime_list):
        binary_outputs = []
        for prime in prime_list:
            ones = '1' * prime
            zeros = '0' * (prime - 1)
            binary_outputs.append(ones + zeros)
        return binary_outputs

    def binary_to_decimal(self, binary):
        return int(binary, 2)

    def find_perfect_numbers(self, limit):
        prime_list = self.sieve_of_eratosthenes(limit)
        binary_outputs = self.generate_binary(prime_list)
        for binary in binary_outputs:
            decimal_value = self.binary_to_decimal(binary)
            if self.is_perfect_number(decimal_value):
                self.text_output.config(state="normal")
                self.text_output.insert(tk.END, f"Binary: {binary} - Decimal: {decimal_value}\n")
                self.text_output.config(state="disabled")
                self.text_output.see(tk.END)
                self.text_output.update_idletasks()
            if self.cancelled.is_set():
                self.text_output.config(state="normal")
                self.text_output.insert(tk.END, "Calculation cancelled!\n")
                self.text_output.config(state="disabled")
                return
        self.text_output.config(state="normal")
        self.text_output.insert(tk.END, "Calculations have finished!\n")
        self.text_output.config(state="disabled")
        self.button_cancel.config(state="disabled")
        self.button_find.config(state="normal")

    def start_calculation(self):
        try:
            self.text_output.config(state="normal")
            self.text_output.delete("1.0", tk.END)
            self.text_output.config(state="disabled")
            limit = int(self.entry_limit.get())
            if limit < 2:
                messagebox.showerror("Error", "Please enter a limit greater than or equal to 2.")
            else:
                self.cancelled.clear()
                self.button_cancel.config(state="normal")
                self.button_find.config(state="disabled")
                threading.Thread(target=self.find_perfect_numbers, args=(limit,), daemon=True).start()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid integer.")

    def cancel_calculation(self):
        self.cancelled.set()
        self.button_cancel.config(state="disabled")
        self.button_find.config(state="normal")

root = tk.Tk()
app = PerfectNumberFinderApp(root)
root.mainloop()
