list = [1,2,3,4,5,6,7,8,9]

try: 
    media = sum(list) / len(list)

    print(media)
except ZeroDivisionError:
    print('Não foi possível realizar a divisão por 0')