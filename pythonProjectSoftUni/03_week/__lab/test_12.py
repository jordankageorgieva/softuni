city = str(input())
volume_sales = float(input())
commission = 0
ERROR_DATA = False

if city == 'Sofia':
    if 0 <= volume_sales <= 500:
        commission = volume_sales * 0.05
    elif 500 < volume_sales <= 1000:
        commission = volume_sales * 0.07
    elif 1000 < volume_sales <= 10000:
        commission = volume_sales * 0.08
    elif volume_sales > 10000:
        commission = volume_sales * 0.12
    else:
        ERROR_DATA = True

elif city == 'Varna':
    if 0 <= volume_sales <= 500:
        commission = volume_sales * 0.045
    elif 500 < volume_sales <= 1000:
        commission = volume_sales * 0.075
    elif 1000 < volume_sales <= 10000:
        commission = volume_sales * 0.10
    elif volume_sales > 10000:
        commission = volume_sales * 0.13
    else:
        ERROR_DATA = True

elif city == 'Plovdiv':
    if 0 <= volume_sales <= 500:
        commission = volume_sales * 0.055
    elif 500 < volume_sales <= 1000:
        commission = volume_sales * 0.08
    elif 1000 < volume_sales <= 10000:
        commission = volume_sales * 0.12
    elif volume_sales > 10000:
        commission = volume_sales * 0.145
    else:
        ERROR_DATA = True
else:
    ERROR_DATA = True


if ERROR_DATA:
    print('error')
else:
    print(f'{commission:.02f}')