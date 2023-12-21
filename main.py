from tkinter import *
from tkinter.messagebox import showerror, showinfo
import random, os
import xlsxwriter

ws = Tk()
ws.title('YASH')
ws.geometry('355x200')
ws["bg"] = "gray80"

Label(ws, bg='gray81', text="Проверка").place(x=60, y=10)
Label(ws, bg='gray81', text="Фраза").place(x=30, y=30)
decimal_number_ = Entry(ws)
decimal_number_.place(x=30, y=50)

Label(ws, bg='gray81', text="Ключ").place(x=30, y=75)
decimal_number_key_ = Entry(ws)
decimal_number_key_.place(x=30, y=95)

Label(ws, bg='gray81', text="Генерация").place(x=225, y=10)
Label(ws, bg='gray81', text="Количество данных").place(x=200, y=30)
decimal_count_ = Entry(ws)
decimal_count_.place(x=200, y=50)

def Decimal_number(number):
    x=''
    decimal_number = number
    if decimal_number != '':
        decimal_number = int(decimal_number)
        binary_representation = bin(int(decimal_number))[2:]
        if len(binary_representation) < 16:
            x = '0' * (16 - len(binary_representation)) + binary_representation
        else:
            x = binary_representation
    return x

def Decimal_number_key(key):
    k=''
    decimal_number_key = key
    if decimal_number_key != '':
        decimal_number_key = int(decimal_number_key)
        binary_representation = bin(decimal_number_key)[2:]
        if len(binary_representation) < 24:
            k = '0' * (24 - len(binary_representation)) + binary_representation
        else:
            k = binary_representation
    return k

def input_number():
    decimal_number = decimal_number_.get()
    return decimal_number

def input_key():
    decimal_number_key = decimal_number_key_.get()
    return decimal_number_key

def input_count():
    decimal_count = decimal_count_.get()
    return decimal_count

def permutation_with_expansion(data_for_permutation, keyE1): #перестановка с расширением
    result = ''
    for i in range(0, 12):
        result = result + data_for_permutation[int(keyE1[i]) - 1]
    return result

def summ_with_key(data, key):
    result = ''
    for i in range(0, 12):
        if data[i] == key[i]:
            result += "0"
        else:
            result += "1"
    return result

def summ_with_left_side(left_side, data):
    result = ''
    for i in range(0, 8):
        if data[i] == left_side[i]:
            result += "0"
        else:
            result += "1"
    return result

def permutation(data, key):
    result = ''
    for i in range(0, 8):
        result = result + data[int(key[i]) - 1]
    return result

def Answer(data, key):
    x = data
    k = key
    dict1 = {
        '0000': '100', '0001': '110', '0010': '001', '0100': '101',
        '0011': '011', '0111': '101', '0101': '111', '0110': '010',
        '1000': '101', '1001': '111', '1010': '010', '1100': '110',
        '1011': '100', '1111': '110', '1101': '001', '1110': '011'
    }
    dict2 = {
        '0001': '101', '0010': '111', '0000': '011', '0011': '010',
        '0101': '110', '0110': '001', '0111': '111', '0100': '100',
        '1001': '110', '1010': '001', '1000': '100', '1011': '011',
        '1101': '111', '1110': '010', '1111': '001', '1100': '101'
    }
    dict3 = {
        '0001': '10', '0010': '11', '0000': '01', '0011': '01',
        '0101': '11', '0110': '01', '0111': '10', '0100': '10',
        '1001': '01', '1010': '10', '1000': '11', '1011': '11',
        '1101': '10', '1110': '11', '1111': '01', '1100': '01'
    }

    k1 = k[:12]
    k2 = k[6:18]
    k3 = k[12:24]

    left_side = str(x[:8])
    data_for_permutation = str(x[8:] * 2)

    keyE1 = "341268573824"
    keyE2 = "87325416"

    f3_1 = ""

    f1_1 = permutation_with_expansion(data_for_permutation, keyE1) #перестановка с расширением
    f2_1 = summ_with_key(f1_1, k1) #сумма с ключем
    f3_1 = f3_1 + dict1[f2_1[:4]] + dict2[f2_1[4:8]] + dict3[f2_1[8:]] #поиск по таблицам 3956874
    f4_1 = permutation(f3_1, keyE2) #перестановка
    f5_1 = summ_with_left_side(left_side, f4_1) #сложение с левой частью

    x1 = str(x[8:])
    x2 = f5_1
    f3_2 = ""

    f1_2 = permutation_with_expansion(x2, keyE1) #перестановка с расширением
    f2_2 = summ_with_key(f1_2, k2) #сумма с ключем
    f3_2 = f3_2 + dict1[f2_2[:4]] + dict2[f2_2[4:8]] + dict3[f2_2[8:]] #поиск по таблицам
    f4_2 = permutation(f3_2, keyE2) #перестановка
    f5_2 = summ_with_left_side(x1, f4_2) #сложение с левой частью

    x1 = x2
    x2 = f5_2

    f3_3 = ""

    f1_3 = permutation_with_expansion(x2, keyE1) #перестановка с расширением
    f2_3 = summ_with_key(f1_3, k3) #сумма с ключем
    f3_3 = f3_3 + dict1[f2_3[:4]] + dict2[f2_3[4:8]] + dict3[f2_3[8:]]
    f4_3 = permutation(f3_3, keyE2) #перестановк
    f5_3 = summ_with_left_side(x1, f4_3) #сложение с левой частью

    answer = f5_3 + x2
    answer_final = (int(answer, 2))
    return answer_final

def generate_number():
    return random.randint(0, 65535)

def generate_key():
    return random.randint(0, 16777215)

def Generate(count):
    try:
        workbook = xlsxwriter.Workbook('dataYASH.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'X')
        worksheet.write('B1', 'K')
        worksheet.write('C1', 'Answer')

        for i in range(1, int(count) + 1):
            x = str(Decimal_number(generate_number()))
            k = str(Decimal_number_key(generate_key()))


            answer = Answer(x, k)
            worksheet.write(f'A{i + 1}', int(x, 2))
            worksheet.write(f'B{i + 1}', int(k, 2))
            worksheet.write(f'C{i + 1}', answer)

        workbook.close()

        # Проверяем, существует ли файл после закрытия
        if os.path.exists('dataYASH.xlsx'):
            showinfo("Информация", "Данные успешно сгенерированы и сохранены в dataYASH.xlsx")
        else:
            showerror("Ошибка", "Не удалось создать файл")

    except Exception as e:
        showerror("Ошибка", f"Произошла ошибка при генерации данных: {str(e)}")

def check():
    data = input_number()
    key = input_key()

    if data == '' or key == '':
        showerror(title="Ошибка", message="Заполните все поля")
    else:
        data_to_answer = Decimal_number(data)
        key_to_answer = Decimal_number_key(key)
        answer = Answer(str(data_to_answer), str(key_to_answer))
        Label(ws, bg='gray81', text=f'Результат: {answer}').place(x=50, y=170)
def check_generate():
    count = input_count()

    if count == '':
        showerror(title="Ошибка", message="Заполните поле")
    else:
        Generate(count)

btn = Button(ws, text="Зашифровать", command=check)
btn.place(x=50, y=135)
btn_generate = Button(ws, text="Сгенерировать", command=check_generate)
btn_generate.place(x=215, y=135)
ws.mainloop()
