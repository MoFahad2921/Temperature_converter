choice = [1, 2, 3]

while True:
    print('Temperature Conversion Programme.')
    print('[1] Convert Celsius to Fahrenheit.\n[2] Convert Fahrenheit to Celsius.\n[3] Exit.\n')
    try:
        choice = int(input('Enter your choice[1, 2, 3]:\n'))
    except ValueError:
        print('Invalid input! Kindly enter the correct choice')

    if choice == 1:
        print('Celsius (C) to Fahrenheit (F) Conversion:\n')
        min_temp = int(input('Enter minimum temperature in celsius:\n'))
        max_temp = int(input('Enter maximum temperature in celsius:\n'))

        for celsius in range(int(min_temp), int(max_temp) + 1):
            fahrenheit = (celsius * 9 / 5) + 32
            print(celsius, 'C', '={:.2f}'.format(fahrenheit), 'F')

    elif choice == 2:
        print('Fahrenheit (F) to Celsius (C) Conversion:\n')
        min_temp = int(input('Enter minimum temperature in fahrenheit:\n'))
        max_temp = int(input('Enter maximum temperature in fahrenheit:\n'))

        for Fahrenheit in range(int(min_temp), int(max_temp) + 1):
            celsius = (fahrenheit - 32) * 5 / 9
            print(fahrenheit, 'F', '={:.2f}'.format(celsius), 'C')

    elif choice == 3:
        print('Bye bye!')
        break

    else:
        print('Invalid input! Kindly enter the correct choice')