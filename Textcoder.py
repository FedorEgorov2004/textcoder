import os;
import sys;
import pyperclip;
import colorama;
from colorama import Fore, Style;
import datetime;
from datetime import datetime;
import ctypes;
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

def eng():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14;
    l1 = "Input '0' to encrypt your text";
    l2 = "Input '1' to decrypt your text";
    l3 = "Input '2' to exit and save history";
    l4 = 'Input a text to encrypt it:';
    l5 = 'Input a crypted text to decrypt it:';
    l6 = 'Crypted text:';
    l7 = 'Encrypted text:';
    l8 = "Input '3' to see history"
    l9 = 'Welcome to';
    l10 = 'Text was encrypted and copied. Click "Enter" to continue';
    l11 = 'Text was decrypted and copied. Click "Enter" to continue';
    l12 = 'Saving file...';
    l13 = "Click 'Enter' to continue";
    l14 = 'History:\n';

print('Choose your language. Выберите свой язык.\n0 - English\n1 - Русский');
a = input();
if a == '0':
    eng();

if a == '1':
    l1 = "Введите '0' для шифровки текста";
    l2 = "Введите '1' для расшифровки текста";
    l3 = "Введите '2' для выхода из программы и сохранения истории";
    l4 = 'Введите текст для шифровки:';
    l5 = 'Введите зашифрованный текст для расшифровки:';
    l6 = 'Зашифрованный текст:';
    l7 = 'Расшифрованный текст:';
    l8 = "Введите '3' для того, чтобы показать историю"
    l9 = 'Добро пожаловать в';
    l10 = 'Текст зашифрован и скопирован. Нажмите Enter, чтобы продолжить';
    l11 = 'Текст расшифрован и скопирован. Нажмите Enter, чтобы продолжить';
    l12 = 'Сохранение файла...'
    l13 = 'Нажмите Enter, чтобы продолжить';
    l14 = 'История:\n';

else:
    eng();

arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '];
arr_EN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
arr_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я'];
arr_RU = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я', '~'];
arr_symb = [',', '.', '!', ':', '#', '@', '$', '"', "'", '=', '-', '+', '*', '/', '%', ';', '^', '(', ')', '&', '?'];

arr = arr_en + arr_ru + arr_symb + arr_EN + arr_RU;

arrl = [];
b = 1;

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

b = 1;

for a in arr_EN:
    if b < 10:
        arrl.append('b0' + str(b));
    else:
        arrl.append('b' + str(b));
    b = b + 1;

for a in arr_RU:
    arrl.append('b' + str(b));
    b = b + 1;

os.system("cls");

while True:
    print(Fore.YELLOW + l9, 'Textcoder!', Style.RESET_ALL);
    print(l1);
    print(l2);
    print(l3);
    print(l8);

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

    if a == '2':
        os.system('cls');
        print(l12);
        f = open('textcoder_history.txt', 'a+');
        f.write(history);
        sys.close();

    if a == '3':
        os.system('cls');
        print(Fore.YELLOW + l14 + Style.RESET_ALL);
        print(history);
        input(Fore.YELLOW + l13 + Style.RESET_ALL);
        os.system('cls');

    else: os.system("cls");