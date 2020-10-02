def main():
    def power_of_2():
        a = num
        b = 0
        for i in range(num):
            a = a / 2
            b += 1
            if a == 1:
                break
        print(f"{num} = 2^{b}\n")

    num = int(input("Enter Even number: "))

    if (num % 2) == 0:
        power_of_2()
		else:
        print("!! Only Even number is accepted !!\n")
        exit


while True or False:
    main()
