import math

def main():
    try:
        # Get input from user
        num = float(input("Enter a positive number (for sqrt and log): "))

        # Square root
        if num < 0:
            print("❌ Square root and logarithm are not defined for negative numbers.")
        else:
            sqrt_result = math.sqrt(num)
            log_result = math.log(num)
            print(f"√{num} = {sqrt_result}")
            print(f"ln({num}) = {log_result}")

        # Sine (in radians)
        sine_result = math.sin(num)
        print(f"sin({num}) = {sine_result}")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
