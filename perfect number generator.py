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

if __name__ == "__main__":
    try:
        limit = int(input("Enter the upper limit for prime numbers: "))
        if limit < 2:
            print("Please enter a limit greater than or equal to 2.")
        else:
            prime_list = sieve_of_eratosthenes(limit)
            binary_outputs = generate_binary(prime_list)
            for i, binary in enumerate(binary_outputs, 1):
                print(f"Binary output {i}: {binary}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


