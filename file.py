#!/usr/bin/env python3
"""
Prime Number Finder Script
-------------------------
This script finds all prime numbers between 1 and 250,
displays them, and saves them to a results.txt file.

The script uses Sieve of Eratosthenes algorithm to achieve it's goals which:
    - Creates a boolean array of size (upper_bound + 1), initialized to true (representing potential primes)
    - Sets indices 0 and 1 to false (as they're not prime)
    - Starting from 2, for each prime number p:
        - Marks all its multiples (p²+p, p²+2p, etc.) as non-prime (false)
        - Finds the next unmarked number, which is the next prime
    - And continues until p² exceeds the upper bound
    - The remaining marked (true) positions are prime numbers

"""

import os

def create_sieve(upper_bound):
    """
    Creates a sieve of Eratosthenes up to the given upper bound.
   
    Args:
        upper_bound (int): The maximum number to check for primality
       
    Returns:
        list: A boolean list where True at index i indicates i is prime
       
    Raises:
        ValueError: If upper_bound is less than 2
    """
    if upper_bound < 2:
        return []
   
    # Initialize boolean array with all True values
    # We'll mark non-primes as False
    sieve = [True] * (upper_bound + 1)
   
    # 0 and 1 are not prime numbers
    sieve[0] = sieve[1] = False
   
    # Apply the sieve algorithm
    # We only need to check up to the square root of upper_bound
    for i in range(2, int(upper_bound**0.5) + 1):
        # If i is prime (still marked as True)
        if sieve[i]:
            # Mark all multiples of i as non-prime
            # Start from i*i as all smaller multiples have already been marked
            for j in range(i*i, upper_bound + 1, i):
                sieve[j] = False
   
    return sieve

def extract_primes_from_sieve(sieve, lower_bound, upper_bound):
    """
    Extracts prime numbers within a specified range from a sieve.

    Args:
        sieve (list): Boolean list from create_sieve where True at index i means i is prime
        lower_bound (int): Lower limit of the range (inclusive)
        upper_bound (int): Upper limit of the range (inclusive)

    Returns:
        list: List of prime numbers within the specified range
    """

    #Adjust lower bound if i's less than 2 (smallest prime)
    effective_lower = max(2, lower_bound)

    # Extract prime numbers in the range
    primes = [i for i in range(effective_lower, min(len(sieve), upper_bound+1))
             if sieve[i]]
    return primes

def find_primes_in_range(lower_bound, upper_bound):
    """
    Finds all prime numbers within the specified range.
   
    Args:
        lower_bound (int): Lower limit of the range (inclusive)
        upper_bound (int): Upper limit of the range (inclusive)
       
    Returns:
        list: List of prime numbers within the specified range
       
    Raises:
        ValueError: If input bounds are invalid
    """
    # Input validation
    if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
        raise TypeError("Bounds must be integers")
   
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must be less than or equal to upper bound")
   
    # No primes less than 2
    if upper_bound < 2:
        return []
   
    # Create the sieve up to upper_bound
    sieve = create_sieve(upper_bound)
   
    # Extract primes within our range
    return extract_primes_from_sieve(sieve, lower_bound, upper_bound)

def print_primes(primes, format_type="list"):
    """
    Print prime numbers in different formats.
   
    Args:
        primes (list): List of prime numbers
        format_type (str): Format to print ("list" or "columns")
    """
    if not primes:
        print("No prime numbers found in the given range.")
        return
   
    if format_type == "list":
        print(f"Found {len(primes)} prime numbers: {', '.join(map(str, primes))}")
    elif format_type == "columns":
        print(f"Found {len(primes)} prime numbers:")
        # Print in columns of 10
        for i in range(0, len(primes), 10):
            row = primes[i:i+10]
            print(" ".join(f"{p:6d}" for p in row))
    else:
        print(f"Found {len(primes)} prime numbers: {primes}")

def save_primes_to_file(primes, filename="results.txt"):
    """
    Save prime numbers to a file.

    Args:
        primes (list): List of prime numbers
        filename (str): Name of the file to save to
    """

    # Remove file if it already exists
    if os.path.exists(filename):
        os.remove(filename)

    # Create and open file for write operations
    with open(filename, 'w') as file:
        file.write(f"Found {len(primes)} prime numbers between 1 and 250: \n\n")

        # Write in columns of 10 for better readability
        for i in range(0, len(primes), 10):
            row = primes[i:i+10]
            file.write(" ".join(f"{p:6d}" for p in row) + "\n")

def main():
    """
    Main function to run the prime number finder.
    """
    # Define the range to find prime numbers
    lower_bound = 1
    upper_bound = 250

    # Find prime numbers in the specified range
    print(f"Finding prime numbers between {lower_bound} and {upper_bound}")
    primes = find_primes_in_range(lower_bound, upper_bound)

    # Display the results
    print_primes(primes, "columns")

    # Save the results to a file
    save_primes_to_file(primes)
    print(f"\nResults have been saved to results.txt")

if __name__ == "__main__":
    main()

