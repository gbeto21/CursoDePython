def run():
    with open('numeros.txt','w') as fileNumeros:
        for num in range(10):
            fileNumeros.write(str(num))


if __name__ == '__main__':
    run()

