import time

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1

    print("\nTime Up")

if __name__ == "__main__":
    try:
        t = get_positive_integer("Enter the time in seconds: ")
        countdown(t)
    except KeyboardInterrupt:
        print("\nCountdown stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
