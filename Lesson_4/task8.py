# CMYK to RGB
while True:

    params = input('Enter parameters in CMYK format: ')

    if params == 'exit' or params == 'e':
        break

    params = params.split(' ')
    print(params)

    if len(params) != 4:
        print('The input is INCORRECT. Try again.')
        continue

    if float(max(params)) > 1 or float(min(params)) < 0:
        print('All the values need to be from 0 to 1. Try again.')
        continue

    cyan = float(params[0])
    magenta = float(params[1])
    yellow = float(params[2])
    black = float(params[3])

    white = 1 - black
    red = 255 * white * (1 - cyan)
    green = 255 * white * (1 - magenta)
    blue = 255 * white * (1 - yellow)

    print(f'red = {round(red)}', f'green = {round(green)}', f'blue = {round(blue)}', sep='\n')
