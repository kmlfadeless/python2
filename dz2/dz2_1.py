import csv
import re


def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for file_name in file_list:
        with open(file_name, encoding='cp1251') as f_n:
            for row in f_n:
                # делим строку на ключ-значение
                param = re.split(":\s+", row.strip())
                if isinstance(param, list) and len(param) == 2:
                    # записываем значения в массивы в соответствии с ключем
                    if param[0] == 'Изготовитель системы':
                        os_prod_list.append(param[1])
                    elif param[0] == 'Название ОС':
                        os_name_list.append(param[1])
                    elif param[0] == 'Код продукта':
                        os_code_list.append(param[1])
                    elif param[0] == 'Тип системы':
                        os_type_list.append(param[1])
    # согласно требованиям задачи, возвращать данные необходимо в виде пяти массивов:
    # заголовки, изготовитель системы, название ос, код продукта, тип системы
    header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    return header, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv():
    data = get_data()  # получаем данные из файла в формате, как указано в задаче
    number_of_lines = len(data[1])  # считаем сколько строк данных нужно записать
    processed_data = [data[0]]  # сначала заголовок
    for i in range(number_of_lines):
        processed_data.append([row[i] for row in data[1:]])  # данные построчно
    with open('info_result.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        for row in processed_data:
            f_n_writer.writerow(row)


if __name__ == '__main__':
    write_to_csv()
