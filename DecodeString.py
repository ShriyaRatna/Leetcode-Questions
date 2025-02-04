numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
s = "3[a2[c]]"


stack = []
num = 0
temp = ""

for i in s:
    print("\n\n", i)
    if i.isdigit():
        num = (num * 10) + int(i)
        print(num)

    elif i == "[":
        stack.append((temp, num))
        num = 0
        temp = ""
        print(stack)

    elif i == "]":
        string, nums = stack.pop()
        print(temp)
        temp = string + (temp * nums)
        print(temp, "\n", string, "\n", nums, "\n")

    else:
        temp += i
print(temp)
