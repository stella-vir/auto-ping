import random
import time

def shuffle_string(input_str):
    char_list = list(input_str)
    random.shuffle(char_list)
    return ''.join(char_list)

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    return ''.join(random.choice(characters) for _ in range(length))

def guess_password(target_password):
    start_time = time.time()
    attempts = 0

    while True:
        attempts += 1
        guess = generate_password(len(target_password))
        if guess == target_password:
            end_time = time.time()
            time_taken = end_time - start_time
            return attempts, time_taken


if __name__ == "__main__":
    # input one or two digit to start
    user_password = input("Enter your password: ")

    # Password successfully guessed in 6724 attempts.
    # Time taken: 0.01 seconds

    shuffled_password = shuffle_string(user_password)
    print(f"Shuffled password: {shuffled_password}")

    print("Guessing the password...")
    attempts, time_taken = guess_password(user_password)

    print(f"Password successfully guessed in {attempts} attempts.")
    print(f"Time taken: {time_taken:.2f} seconds")
