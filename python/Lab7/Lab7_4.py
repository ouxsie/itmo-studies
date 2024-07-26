import matplotlib.pyplot as plt

def read_file_fully(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', ' ').split()
        data = list(map(float, data))
    return data


def read_file_by_lines(filename):
    with open(filename, 'r') as file:
        data = [list(map(float, line.split())) for line in file]
    return data


def plot_data(data, read_fully=True):
    plt.figure(figsize=(10, 6))

    if read_fully:
        plt.plot(data, label='Все данные')
    else:
        for i in range(len(data)):
            x = data[i]
            y = i+1
            plt.scatter(x, y, s=100, c='red', alpha=0.5)

    plt.legend()
    plt.ylabel('Строка')
    plt.xlabel('Значение')
    plt.title('Данные из файла')
    plt.show()


filename = 'Lab7_4.txt'
choice = int(input("Введите 1 для чтения файла полностью, или 2 для чтения построчно: "))

if choice == 1:
    data = read_file_fully(filename)
    plot_data(data, read_fully=True)
elif choice == 2:
    data = read_file_by_lines(filename)
    plot_data(data, read_fully=False)
else:
    print("Неверный выбор. Введите '1' или '2'.")
