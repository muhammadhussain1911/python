# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time
attempts = 0
max_attempts = 5
wait_time = 1  # initial wait time in seconds

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}: Waiting for {wait_time} seconds before retrying...")
    time.sleep(wait_time)  # simulate waiting
    attempts += 1
    wait_time *= 2  # double the wait time for the next attempt