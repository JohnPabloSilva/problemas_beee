meses = {'1': 'January', '2': 'February', '3': 'March', '4': 'April',
         '5': 'May', '6': 'June', '7': 'July', '8': 'August',
         '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
n = str(input())
if n in meses:
    print(f'{meses[n]}')
else:
    print("It's not in calendar")