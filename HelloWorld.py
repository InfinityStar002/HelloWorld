import sys
import time

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def typewriter(text, delay=0.1, color=RESET):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

if __name__ == "__main__":
    colors = [RED, YELLOW, GREEN, CYAN]
    message = "Hello World..!"
    repeat_count = 5  # Number of times to repeat the animation

    for _ in range(repeat_count):
        # Animation: "Hello World..!" with a typewriter effect and color cycling
        for i, char in enumerate(message):
            color = colors[i % len(colors)]
            sys.stdout.write(color + char + RESET)
            sys.stdout.flush()
            time.sleep(0.15)
        print()
        
        # Add an additional animated message
        typewriter("Welcome to the animated Hello World!", delay=0.06, color=CYAN)
        
        time.sleep(0.5)  # Optional: small pause between loops
