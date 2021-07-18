import os;
import random;
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
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28;
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
    l15 = 'Enter a range of numbers for creating strings for a list.\nMinimum:\n';
    l16 = '\nMaximum:\n';
    l17 = 'Enter a path to any text file for encrypt it:';
    l18 = 'Enter a path to any text file for decrypt it:';
    l19 = 'Incorrect path: try again.'
    l20 = 'Enter a new path to a new encrypted file:';
    l21 = 'Enter a new path to a new decrypted file:';
    l22 = 'Name the file:';
    l23 = "Enter '3' to encrypt a text file";
    l24 = "Enter '4' to decrypt a text file";
    l25 = "Enter a path to save a crypt settings file (do not afraid __init__.py):\n";
    l26 = '0 - Creating a new crypt settings file\n1 - Import';
    l27 = 'Enter a path to a folder (!) where the file is located:';
    l28 = 'Enter the name of the file (without path):'

def ru_l():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28;
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
    l15 = 'Введите диапазон чисел для создания строк в массиве:\nМинимальное число:';
    l16 = 'Максимальное число:';
    l17 = 'Введите путь файла для шифровки:';
    l18 = 'Введите путь файла для расшифровки:';
    l19 = 'Неверный путь: попробуйте ещё раз.';
    l20 = 'Введите новый путь для зашифрованного файла:';
    l21 = 'Введите новый путь для расшифрованного файла:';
    l22 = 'Назовите файл:';
    l23 = "Введите '3' для шифрования файла";
    l24 = "Введите '4' для расшифрования файла";
    l25 = 'Укажите путь для сохранения файла настроек шифрования (не бойтесь __init__.py):\n';
    l26 = 'Выберите создание или импорт файла настроек шифрования.\n0 - Создание\n1 - Импорт';
    l27 = 'Укажите путь к папке (!), где находится импортируемый файл:';
    l28 = 'Введите название файла (без пути):';

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
    if 'en' in check_l:
        en_l();
    if 'ru' in check_l:
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
arr_symb = [',', '.', '!', ':', '#', '@', '$', '"', "'", '=', '-', '+', '*', '/', '%', ';', '^', '(', ')', '&', '?', '[', ']','<','>'];
arr_n = ['0','1','2','3','4','5','6','7','8','9'];

arr = arr_en + arr_ru + arr_symb + arr_EN + arr_RU;
random.shuffle(arr);

def get_random_unicode(length): # Author of function: Jacob Wan, Stack Overflow.

    try:
        get_char = unichr;
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length));

b = '';
arrl = [];

os.system('cls');

while True:
    print(l26);
    a = input();

    if a == '0':
        while True:
            os.system('cls');
            print(l15);
            first = input();
            print(l16);
            second = input();
            try:
                first = int(first);
                second = int(second);
                break;
            except:
                os.system('cls');

        arr_exc = [];

        def stringg():
            global b;
            rand = random.randint(first, second);
            if rand == 1:
                for i in range(rand):
                    a = get_random_unicode(1);
                    if a in arr or a in arr_exc or a in arr_n:
                        stringg();
                    else:
                        arr_exc.append(a);
                        b = b + a;
            else:
                for i in range(rand):
                    a = get_random_unicode(1);
                    if a in arr or a in arr_exc or a in arr_n:
                        stringg();
                    else:
                        b = b + a;

        for lc in range(145):
            stringg();
            arrl.append(b);
            b = '';

        try:
            os.system('cls');
            print(l25);
            path = input();
            pathd = path + '\\' + '__init__.py';
            init = open(pathd,'w+');
            init.close();
            os.system("cls");
            print(l22);
            namefile = input();
            path = path + '\\' + namefile + '.py';

            new_file = open(path,'a+',encoding="utf-8");
            new_file.write('arr1 = ' + str(arr) + '\n' + 'arr2 = ' + str(arrl));
            new_file.close();
            os.system("cls");
            break;

        except:
            print(Fore.RED + l19 + Style.RESET_ALL);
            time.sleep(1.5);
            os.system('cls');

    if a == '1':
        try:
            os.system('cls');

            print(l28);

            path = input();

            pathd = path + '\\..\\' + '__init__.py';

            init = open(pathd,'w+');
            init.close();

            namefile = os.path.basename(path);
            namefile = namefile[0:-3];
            namefile = __import__(namefile);
            arr = namefile.arr1;
            arrl = namefile.arr2;
            os.system("cls");
            break;

        except:
            print(Fore.RED + l19 + Style.RESET_ALL);
            time.sleep(1.5);
            os.system('cls');

    else:
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
        break;

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
        break;
    else:
        os.system("cls");