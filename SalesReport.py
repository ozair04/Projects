print('Sales report')
year = int(input('Input the year the sales report is for: '))
total = 0
months = []
for i in range(12):
    month = int(input('Please enter the sales for month ' + str(i+1) + ': '))
    months.append(month)
    if i == 0:
        min = months[i]
        max = months[i]
    elif months[i] > max:
        max = months[i]
        month_max = i + 1
    elif months[i] < min:
        min = months[i]
        month_min = i + 1
    total += month
print('The total sales for', year, 'was £' + str(total))
print('The average monthly sales for', year, 'was £' + str(total / 12))
print('The month number with the maximum sales was', month_max, 'with £' + str(max))
print('The month number with the minimum sales was', month_min, 'with £' + str(min))



