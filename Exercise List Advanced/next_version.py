def next_version(versions):
    version_as_int = [int(number) for number in version]

    num1 = version_as_int[0]
    num2 = version_as_int[1]
    num3 = version_as_int[2] + 1

    if num3 > 9:
        num3 = 0
        num2 += 1

    if num2 > 9:
        num2 = 0
        num1 += 1

    print(f"{num1}.{num2}.{num3}")


version = input().split('.')

(next_version(version))
