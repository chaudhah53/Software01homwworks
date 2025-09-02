SIZE_LIMIT = 42

length = int(input("Enter the length of the zander in centimeters: "))

if length < SIZE_LIMIT:
    diff = SIZE_LIMIT - length
    print("The zander is too small. Please release it back into the lake.")
    print(f"It is {diff} cm below the size limit of {SIZE_LIMIT} cm.")
else:
    print("The zander meets the size limit. You may keep it.")
