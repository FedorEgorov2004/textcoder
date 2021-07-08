import os;
import sys;
from random import randint;
import pyperclip;
import colorama;
from colorama import Fore, Style;
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

while True:
    print('Choose your language. Выберите свой язык.\n0 - English\n1 - Русский');
    a = input();
    if a == '0':
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
        l15 = 'Come up with and/or enter your cryptography key (seed),\nusing latin and cyrillic alphabet, special symbols and numbers:\n';
        l16 = 'Do you want to save your key to a new file? If you forgot it,\nyou can use the file and get the access to encrypted information by the key.\n(y/n)?';
        l17 = 'Enter a path to any text file for encrypt it:';
        l18 = 'Enter a path to any text file for decrypt it:';
        l19 = 'Incorrect path: try again.'
        l20 = 'Enter a new path to a new encrypted file:';
        l21 = 'Enter a new path to a new decrypted file:';
        l22 = 'Name the file:';
        l23 = "Enter '3' to encrypt a text file";
        l24 = "Enter '4' to decrypt a text file";
        break;

    if a == '1':
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
        l15 = 'Придумайте и/или введите свой криптографический ключ (зерно),\nиспользуя кириллицу, латиницу, цифры и специальные знаки:\n';
        l16 = 'Вы хотите сохранить свой ключ в отдельном файле?\nПри сохранении ключа у вас будет доступ к зашифрованной вами информации.\ny - Да\nn - Нет';
        l17 = 'Введите путь файла для шифровки:';
        l18 = 'Введите путь файла для расшифровки:';
        l19 = 'Неверный путь: попробуйте ещё раз.';
        l20 = 'Введите новый путь для зашифрованного файла:';
        l21 = 'Введите новый путь для расшифрованного файла:';
        l22 = 'Назовите файл:';
        l23 = "Введите '3' для шифрования файла";
        l24 = "Введите '4' для расшифрования файла";
        break;
    else:
        os.system('cls');

os.system('cls');

arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '];
arr_EN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
arr_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я'];
arr_RU = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я', '~'];
arr_symb = [',', '.', '!', ':', '#', '@', '$', '"', "'", '=', '-', '+', '*', '/', '%', ';', '^', '(', ')', '&', '?'];

arr = arr_en + arr_ru + arr_symb + arr_EN + arr_RU;

while True:
    print(l15);
    key = input();
    if key == '':
        os.system('cls');
    else:
        break;

b = 1;

len_arr = [];

for count in range(len(arr)):
    len_arr.append(count);
    
for i in len_arr:
    if arr[i] in key:
        b = b * len_arr[i];

for i in len_arr:
    if str(len_arr[i]) in key:
        b = b * len_arr[i];

arrl = [];

for a in arr_en:
    if b < 10:
        arrl.append('a0' + str(b));
    else:
        arrl.append('a' + str(b));
    b = b + 1;

for a in arr_ru:
    arrl.append('a' + str(b));
    b = b + 1;

for a in arr_symb:
    arrl.append('a' + str(b));
    b = b + 1;

for a in arr_EN:
    if b < 10:
        arrl.append('b0' + str(b));
    else:
        arrl.append('b' + str(b));
    b = b + 1;

for a in arr_RU:
    arrl.append('b' + str(b));
    b = b + 1;

os.system('cls');

while True:
    print(l16);
    s = input();
    if s == 'y':
        keyfile = open('textcoder_key.txt', 'a+');
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

    a = input();

    if a == '0':
        os.system('cls');

        print(l4);
        t = input();

        for i in range(len(arr)):
            if arr[i] in t:
                t = t.replace(arr[i],arrl[i]);
        
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
        f = open('textcoder_history.txt', 'a+');
        f.write(history);
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
                    t = t.replace(arr[i],arrl[i]);

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
        
            new_file = open(path,'a+');
            new_file.write(t);
            new_file.close();
            file.close();
            os.system("cls");
        except:
            print(Fore.RED + l19 + Style.RESET_ALL);
            time.sleep(3);

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
        
            new_file = open(path,'a+');
            new_file.write(t);
            new_file.close();
            file.close();
            os.system("cls");
        except:
            print(Fore.RED + l19 + Style.RESET_ALL);
            time.sleep(3);
            os.system("cls");
    else:
        os.system("cls");