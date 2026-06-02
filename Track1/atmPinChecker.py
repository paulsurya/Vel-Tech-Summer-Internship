def check_pin(guess):
    correct_pin = 8415
    if guess == correct_pin:
        return True
    else:
        return False


def main():
    attempt = 0
    while attempt < 3:
        guessed_pin = int(input("Enter the pin:"))
        if 1000 <= guessed_pin <= 9999:
            if check_pin(guessed_pin):
                print("-" * 5, "Access granted", "-" * 5)
                return
            else:
                print("-" * 5, "Incorrect Pin", "-" * 5)
                attempt += 1
        else:
            print("The Pin number provided must be 4-digits long. Please try again.")
    if attempt == 3:
        print("-" * 5, "Access is Revoked due to incorrect guesses", "-" * 5)
        return


if __name__ == "__main__":
    main()
