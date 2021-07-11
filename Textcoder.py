import os;
import sys;
from random import randint;
import pyperclip;
import colorama;
from colorama import Fore, Style;
import math;
from math import sin, cos, log;
import datetime;
from datetime import datetime;
import ctypes;
import time;
colorama.init();
ctypes.windll.kernel32.SetConsoleTitleW('Textcoder');

history = '';
os.system("cls");

def dt():
    global date;
    td = datetime.today();

    d = td.day;
    if d < 10: d = '0' + str(d);
    d = str(d);

    m = td.month;
    if m < 10: m = '0' + str(m);
    m = str(m);

    y = str(td.year);

    h = td.hour;
    if h < 10: h = '0' + str(h);
    h = str(h);

    mi = td.minute;
    if mi < 10: mi = '0' + str(mi);
    mi = str(mi);

    s = td.second;
    if s < 10: s = '0' + str(s);
    s = str(s);

    date = d + '.' + m + '.' + y + ', ' + h + ':' + mi + ':' + s + ":\n";

def en_l():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25;
    l1 = "Input '0' to encrypt your text";
    l2 = "Input '1' to decrypt your text";
    l3 = "Input '5' to exit and save history";
    l4 = 'Input a text to encrypt it:';
    l5 = 'Input a crypted text to decrypt it:';
    l6 = 'Crypted text:';
    l7 = 'Encrypted text:';
    l8 = "Input '2' to see history"
    l9 = 'Welcome to';
    l10 = 'Text was encrypted and copied. Click "Enter" to continue.';
    l11 = 'Text was decrypted and copied. Click "Enter" to continue.';
    l12 = 'Saving file...';
    l13 = "Click 'Enter' to continue";
    l14 = 'History:\n';
    l15 = 'Come up with and/or enter your cryptography key (seed),\nusing latin and cyrillic alphabet, special symbols and numbers (a little simple, a little complex):\n';
    l16 = 'Do you want to save your key to a new file? If you forgot it,\nyou can use the file and get the access to encrypted information by the key.\n(y/n)?';
    l17 = 'Enter a path to any text file for encrypt it:';
    l18 = 'Enter a path to any text file for decrypt it:';
    l19 = 'Incorrect path: try again.'
    l20 = 'Enter a new path to a new encrypted file:';
    l21 = 'Enter a new path to a new decrypted file:';
    l22 = 'Name the file:';
    l23 = "Enter '3' to encrypt a text file";
    l24 = "Enter '4' to decrypt a text file";
    l25 = "Sorry, an error was occurred: please, come up with another, shorter key";

def ru_l():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25;
    l1 = "Введите '0' для шифровки текста";
    l2 = "Введите '1' для расшифровки текста";
    l3 = "Введите '5' для выхода из программы и сохранения истории";
    l4 = 'Введите текст для шифровки:';
    l5 = 'Введите зашифрованный текст для расшифровки:';
    l6 = 'Зашифрованный текст:';
    l7 = 'Расшифрованный текст:';
    l8 = "Введите '2' для того, чтобы показать историю"
    l9 = 'Добро пожаловать в';
    l10 = 'Текст зашифрован и скопирован. Нажмите Enter, чтобы продолжить.';
    l11 = 'Текст расшифрован и скопирован. Нажмите Enter, чтобы продолжить.';
    l12 = 'Сохранение файла...'
    l13 = 'Нажмите Enter, чтобы продолжить';
    l14 = 'История:\n';
    l15 = 'Придумайте и/или введите свой криптографический ключ (сид),\nиспользуя кириллицу, латиницу, цифры и специальные знаки (немного простой, немного сложный):\n';
    l16 = 'Вы хотите сохранить свой ключ в отдельном файле?\nПри сохранении ключа у вас будет доступ к зашифрованной вами информации.\ny - Да\nn - Нет';
    l17 = 'Введите путь файла для шифровки:';
    l18 = 'Введите путь файла для расшифровки:';
    l19 = 'Неверный путь: попробуйте ещё раз.';
    l20 = 'Введите новый путь для зашифрованного файла:';
    l21 = 'Введите новый путь для расшифрованного файла:';
    l22 = 'Назовите файл:';
    l23 = "Введите '3' для шифрования файла";
    l24 = "Введите '4' для расшифрования файла";
    l25 = 'Простите, произошла ошибка: придумайте другой, более короткий ключ';

def choose_l():
    while True:
        print('Choose your language. Выберите свой язык.\n0 - English\n1 - Русский');
        a = input();
        if a == '0':
            en_l();
            en = open('C:\\Users\\Public\\textcoder_locale', "w+", encoding='utf-8');
            en.write('en');
            en.close();
            break;

        if a == '1':
            ru_l();
            ru = open('C:\\Users\\Public\\textcoder_locale', "w+", encoding='utf-8');
            ru.write('ru');
            ru.close();
            break;
        else:
            os.system('cls');

path = 'C:\\Users\\Public\\textcoder_locale';

if os.path.isfile(path):
    locale = open('C:\\Users\\Public\\textcoder_locale', 'r');
    check_l = locale.read();
    locale.close();
    if check_l == 'en':
        en_l();
    if check_l == 'ru':
        ru_l();
    if check_l == '':
        choose_l();

else:
    choose_l();

os.system('cls');

arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '];
arr_EN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
arr_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я'];
arr_RU = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я', '~'];
arr_symb = [',', '.', '!', ':', '#', '@', '$', '"', "'", '=', '-', '+', '*', '/', '%', ';', '^', '(', ')', '&', '?'];

arr = arr_en + arr_ru + arr_symb + arr_EN + arr_RU;

start_symbols = ["à", "æ", "ó", "œ", "ë", "á", "«", "»", "±", "<", '⁰', '¹', "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "¿", "‽", "¡", "Æ", "Á", "É", "Ë", "ñ", ">", "Ê", "è", "ê", "û", "È", "Û", "û", "Ù", "ù" "Ú", "ú", "Ū", "ū", "ā", "Ā", "Ò", "Õ", "ò", "Ó", "õ", "Ô", "ô", "°"];
start_symbols = start_symbols * 10;

while True:
    try:
        print(l15);
        key = input();
        if key == '':
            os.system('cls');
        else:
            break;
    except:
        print(Fore.RED + l25 + Style.RESET_ALL);
        time.sleep(1.5);

count_key_symbols = len(key);
arr_key_len = [];
arrl = [];

for i in arr:
    if i in key:
        for ii in range(key.count(i)):
            arr_key_len.append(arr.index(i) + 1);

for i in range(1,10):
    if str(i) in key:
        for ii in range(key.count(str(i))):
            arr_key_len.append(i);

if '0' in key:
    for i in range(key.count('0')):
        arr_key_len.append(1);

b = 1;

for i in arr_key_len:
    b = b * i;

b = b * sin(count_key_symbols);

q = 0.1;

for i in range(count_key_symbols):
    b = b * q;
    q = q + 1.1;

if b < 0:
    b = b * (-2);

if b < 10:
    b = b * 100;

if b < 100:
    b = b * 10;

b = math.ceil(b);

if b > 1000000000:
    b = str(b);
    b = b[0:10];
    b = int(b);

b = b * count_key_symbols;

if b > 1000000000:
    b = str(b);
    b = b[0:10];
    b = int(b);

b_string = str(b);

if b_string[-1] == '0':
    b = b + 1;
    b_string = str(b);

if len(b_string) == 0:
    for i in range(len(arr)):
        pos1 = len(b_string) / 2;
        pos1 = int(pos1);
        pos = (i + 1) * cos(int(b_string[pos1] + 1)) + log(i + 1)/2;
        if pos == 0:
            pos = i * sin(int(b_string[pos1]));
        if pos < 0:
            pos = pos * -1;
        if 0 > pos >= 1:
            pos = pos * 100;
        pos = math.ceil(pos);
        if pos > 200:
            pos = pos - 200;
        start_letter = start_symbols[pos];
        arrl.append(start_letter + str(b * (i + 1)));
else:
    for i in range(len(arr)):
        pos1 = len(b_string) / 2 + 0.5;
        pos1 = int(pos1);
        pos = (i + 1) * cos(int(b_string[pos1])) + log(i + 1)/2;
        if pos == 0:
            pos = i * sin(int(b_string[pos1]));
        if pos < 0:
            pos = pos * -1;
        if 0 > pos >= 1:
            pos = pos * 100;
        pos = math.ceil(pos);
        if pos > 200:
            pos = pos - 200;
        start_letter = start_symbols[pos];
        arrl.append(start_letter + str(b * (i + 1)));

os.system('cls');

while True:
    print(l16);
    s = input();
    if s == 'y':
        keyfile = open('textcoder_key.txt', 'a+', encoding="utf-8");
        keytext = 'Key: ' + key + '\n';
        keyfile.write(keytext);
        keyfile.close();
        break;
    if s == 'n':
        break;
    else:
        os.system('cls');

os.system('cls');

while True:
    print(Fore.YELLOW + l9, 'Textcoder!', Style.RESET_ALL);
    print(l1);
    print(l2);
    print(l8);
    print(l23);
    print(l24);
    print(l3);
    print("Print '10' to reset Textcoder (сбросить настройки)");

    a = input();

    if a == '0':
        os.system('cls');

        print(l4);
        t = input();

        for i in range(len(arr)):
            if arr[i] in t:
                t = t.replace(arr[i], arrl[i], t.count(arr[i]));

        
        pyperclip.copy(t);

        dt();
        history = history + date + t + '\n\n';

        print('\n' + l6, t, '\n');
        input(Fore.YELLOW + l10 + Style.RESET_ALL + '\n');

        os.system('cls');
    
    if a == '1':
        os.system('cls');

        print(l5);
        t = input();
        
        for i in range(len(arr)):
            if arrl[i] in t:
                t = t.replace(arrl[i],arr[i]);
        
        pyperclip.copy(t);
        
        dt();
        history = history + date + t + '\n\n';

        print('\n' + l7, t, '\n');
        input(Fore.YELLOW + l11 + Style.RESET_ALL + '\n');

        os.system('cls');

    if a == '5':
        os.system('cls');
        print(l12);
        f = open('textcoder_history.txt', 'a+', encoding='utf-8');
        f.write(history);
        time.sleep(1);
        f.close();
        sys.close();

    if a == '2':
        os.system('cls');
        print(Fore.YELLOW + l14 + Style.RESET_ALL);
        print(history);
        input(Fore.YELLOW + l13 + Style.RESET_ALL);
        os.system('cls');
    
    if a == '3':
        try:
            os.system('cls');
            print(l17);
            path = input();
            file = open(path,'r', encoding="utf-8");
            t = file.read();
            for i in range(len(arr)):
                if arr[i] in t:
                    t = t.replace(arr[i],arrl[i],t.count(arr[i]));

            os.system('cls');
            print(l20);
            path = input();
            os.system("cls");
            print(l22);
            namefile = input();
            if path[-1] == '\\':
                path = path + namefile + '.txt';
            else:
                path = path + '\\' + namefile + '.txt';
        
            new_file = open(path,'a+',encoding="utf-8");
            new_file.write(t);
            new_file.close();
            file.close();
            os.system("cls");
        except:
            print(Fore.RED + l19 + Style.RESET_ALL);
            time.sleep(1.5);

    if a == '4':
        try:
            os.system('cls');
            print(l18);
            path = input();
            file = open(path, 'r', encoding="utf-8");
            t = file.read();
            for i in range(len(arr)):
                if arrl[i] in t:
                    t = t.replace(arrl[i],arr[i]);

            os.system('cls');
            print(l21);
            path = input();
            os.system("cls");
            print(l22);
            namefile = input();
            if path[-1] == '\\':
                path = path + namefile + '.txt';
            else:
                path = path + '\\' + namefile + '.txt';
        
            new_file = open(path,'a+', encoding="utf-8");
            new_file.write(t);
            new_file.close();
            file.close();
            os.system("cls");
        except:
            print(Fore.RED + l19 + Style.RESET_ALL);
            time.sleep(1.5);
            os.system("cls");
    if a == '10':
        if os.path.isfile(path):
            reset = open(path, 'w+', encoding='utf-8');
            reset.write('');
            reset.close();
            os.system('cls');
            print('Settings have been reset. Run Textcoder again.\nНастройки сброшены. Запустите Textcoder заново.');
            time.sleep(5);
            sys.close();
    else:
        os.system("cls");