def splitList(nums):
    evenList = list()
    oddList = list()
    for num in nums:
        if num % 2 == 0:
            evenList.append(num)
        else:
            oddList.append(num)

    return [evenList, oddList]


def main():
    nums1 = [1, 3, 5, 7, 2, 75, 345, 96]
    nums2 = [12, 34, 86, 23, 567, 53, 2, 5]

    split1 = splitList(nums1)
    split2 = splitList(nums2)
    print(
        f"The original list\n{nums1}\nThe splited list\nEven:{split1[0]}\nOdd:{
            split1[1]
        }\n"
    )
    print(
        f"The original list\n{nums2}\nThe splited list\nEven:{split2[0]}\nOdd:{
            split2[1]
        }\n"
    )


if __name__ == "__main__":
    main()
