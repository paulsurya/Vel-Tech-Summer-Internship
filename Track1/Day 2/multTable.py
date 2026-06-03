def times_table(num):

    print(f"The Multiplication Tables for {num} are:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 10)


def main():
    nums = list()
    for i in range(3):
        num = int(input("Enter a number: "))
        nums.append(num)
    print("-" * 10)
    for i in range(3):
        times_table(nums[i])


if __name__ == "__main__":
    main()
