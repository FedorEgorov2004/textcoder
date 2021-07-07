import os;
import sys;
import pyperclip;
import colorama;
from colorama import Fore, Style;
import datetime;
from datetime import datetime;
colorama.init();

history = '';
os.system("cls");

def dt():
    global td, d, m, y, h, mi, s, date;
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

        t = t.replace('a','a01');
        t = t.replace('b','a02');
        t = t.replace('c','a03');
        t = t.replace('d','a04');
        t = t.replace('e','a05');
        t = t.replace('f','a06');
        t = t.replace('g','a07');
        t = t.replace('h','a08');
        t = t.replace('i','a09');
        t = t.replace('j','a10');
        t = t.replace('k','a11');
        t = t.replace('l','a12');
        t = t.replace('m','a13');
        t = t.replace('n','a14');
        t = t.replace('o','a15');
        t = t.replace('p','a16');
        t = t.replace('q','a17');
        t = t.replace('r','a18');
        t = t.replace('s','a19');
        t = t.replace('t','a20');
        t = t.replace('u','a21');
        t = t.replace('v','a22');
        t = t.replace('w','a23');
        t = t.replace('x','a24');
        t = t.replace('y','a25');
        t = t.replace('z','a26');
        t = t.replace(' ','a27');

        t = t.replace('а','a28');
        t = t.replace('б','a29');
        t = t.replace('в','a30');
        t = t.replace('г','a31');
        t = t.replace('д','a32');
        t = t.replace('е','a33');
        t = t.replace('ё','a34');
        t = t.replace('ж','a35');
        t = t.replace('з','a36');
        t = t.replace('и','a37');
        t = t.replace('й','a38');
        t = t.replace('к','a39');
        t = t.replace('л','a40');
        t = t.replace('м','a41');
        t = t.replace('н','a42');
        t = t.replace('о','a43');
        t = t.replace('п','a44');
        t = t.replace('р','a45');
        t = t.replace('с','a46');
        t = t.replace('т','a47');
        t = t.replace('у','a48');
        t = t.replace('ф','a49');
        t = t.replace('х','a50');
        t = t.replace('ц','a51');
        t = t.replace('ч','a52');
        t = t.replace('ш','a53');
        t = t.replace('щ','a54');
        t = t.replace('ъ','a55');
        t = t.replace('ы','a56');
        t = t.replace('ь','a57');
        t = t.replace('э','a58');
        t = t.replace('ю','a59');
        t = t.replace('я','a60');

        t = t.replace(',','a61');
        t = t.replace('.','a62');
        t = t.replace('!','a63');
        t = t.replace(':','a64');
        t = t.replace('#','a65');
        t = t.replace('@','a66');
        t = t.replace('$','a67');
        t = t.replace('"','a68');
        t = t.replace("'",'a69');
        t = t.replace("=",'a70');
        t = t.replace("-",'a71');
        t = t.replace("+",'a72');
        t = t.replace("*",'a73');
        t = t.replace("/",'a74'); 
        t = t.replace("%",'a75');
        t = t.replace(";",'a76');
        t = t.replace("^",'a77');
        t = t.replace("(",'a78');
        t = t.replace(")",'a79');
        t = t.replace('&','a80');
        t = t.replace('?','a81');

        t = t.replace('A','b01');
        t = t.replace('B','b02');
        t = t.replace('C','b03');
        t = t.replace('D','b04');
        t = t.replace('E','b05');
        t = t.replace('F','b06');
        t = t.replace('G','b07');
        t = t.replace('H','b08');
        t = t.replace('I','b09');
        t = t.replace('J','b10');
        t = t.replace('K','с11');
        t = t.replace('L','b12');
        t = t.replace('M','b13');
        t = t.replace('N','b14');
        t = t.replace('O','b15');
        t = t.replace('P','b16');
        t = t.replace('Q','b17');
        t = t.replace('R','b18');
        t = t.replace('S','b19');
        t = t.replace('T','b20');
        t = t.replace('U','b21');
        t = t.replace('V','b22');
        t = t.replace('W','b23');
        t = t.replace('X','b24');
        t = t.replace('Y','b25');
        t = t.replace('Z','b26');

        t = t.replace('А','b28');
        t = t.replace('Б','b29');
        t = t.replace('В','b30');
        t = t.replace('Г','b31');
        t = t.replace('Д','b32');
        t = t.replace('Е','b33');
        t = t.replace('Ё','b34');
        t = t.replace('Ж','b35');
        t = t.replace('З','b36');
        t = t.replace('И','b37');
        t = t.replace('Й','b38');
        t = t.replace('К','b39');
        t = t.replace('Л','b40');
        t = t.replace('М','b41');
        t = t.replace('Н','b42');
        t = t.replace('О','b43');
        t = t.replace('П','b44');
        t = t.replace('Р','b45');
        t = t.replace('С','b46');
        t = t.replace('Т','b47');
        t = t.replace('У','b48');
        t = t.replace('Ф','b49');
        t = t.replace('Х','b50');
        t = t.replace('Ц','b51');
        t = t.replace('Ч','b52');
        t = t.replace('Ш','b53');
        t = t.replace('Щ','b54');
        t = t.replace('Ъ','b55');
        t = t.replace('Ы','b56');
        t = t.replace('Ь','b57');
        t = t.replace('Э','b58');
        t = t.replace('Ю','b59');
        t = t.replace('Я','b60');
        
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

        t = t.replace('a01','a');
        t = t.replace('a02','b');
        t = t.replace('a03','c');
        t = t.replace('a04','d');
        t = t.replace('a05','e');
        t = t.replace('a06','f');
        t = t.replace('a07','g');
        t = t.replace('a08','h');
        t = t.replace('a09','i');
        t = t.replace('a10','j');
        t = t.replace('a11','k');
        t = t.replace('a12','l');
        t = t.replace('a13','m');
        t = t.replace('a14','n');
        t = t.replace('a15','o');
        t = t.replace('a16','p');
        t = t.replace('a17','q');
        t = t.replace('a18','r');
        t = t.replace('a19','s');
        t = t.replace('a20','t');
        t = t.replace('a21','u');
        t = t.replace('a22','v');
        t = t.replace('a23','w');
        t = t.replace('a24','x');
        t = t.replace('a25','y');
        t = t.replace('a26','z');
        t = t.replace('a27',' ');

        t = t.replace('a28','а');
        t = t.replace('a29','б');
        t = t.replace('a30','в');
        t = t.replace('a31','г');
        t = t.replace('a32','д');
        t = t.replace('a33','е');
        t = t.replace('a34','ё');
        t = t.replace('a35','ж');
        t = t.replace('a36','з');
        t = t.replace('a37','и');
        t = t.replace('a38','й');
        t = t.replace('a39','к');
        t = t.replace('a40','л');
        t = t.replace('a41','м');
        t = t.replace('a42','н');
        t = t.replace('a43','о');
        t = t.replace('a44','п');
        t = t.replace('a45','р');
        t = t.replace('a46','с');
        t = t.replace('a47','т');
        t = t.replace('a48','у');
        t = t.replace('a49','ф');
        t = t.replace('a50','х');
        t = t.replace('a51','ц');
        t = t.replace('a52','ч');
        t = t.replace('a53','ш');
        t = t.replace('a54','щ');
        t = t.replace('a55','ъ');
        t = t.replace('a56','ы');
        t = t.replace('a57','ь');
        t = t.replace('a58','э');
        t = t.replace('a59','ю');
        t = t.replace('a60','я');

        t = t.replace('a61',',');
        t = t.replace('a62','.');
        t = t.replace('a63','!');
        t = t.replace('a64',':');
        t = t.replace('a65','#');
        t = t.replace('a66','@');
        t = t.replace('a67','$');
        t = t.replace('a68','"');
        t = t.replace("a69","'");
        t = t.replace("a70",'=');
        t = t.replace("a71",'-');
        t = t.replace("a72",'+');
        t = t.replace("a73",'*');
        t = t.replace("a74",'/'); 
        t = t.replace("a75",'%');
        t = t.replace("a76",';');
        t = t.replace("a77",'^');
        t = t.replace("a78",'(');
        t = t.replace("a79",')');
        t = t.replace('a80','&');
        t = t.replace('a81','?');

        t = t.replace('b01','A');
        t = t.replace('b02','B');
        t = t.replace('b03','C');
        t = t.replace('b04','D');
        t = t.replace('b05','E');
        t = t.replace('b06','F');
        t = t.replace('b07','G');
        t = t.replace('b08','H');
        t = t.replace('b09','I');
        t = t.replace('b10','J');
        t = t.replace('с11','K');
        t = t.replace('b12','L');
        t = t.replace('b13','M');
        t = t.replace('b14','N');
        t = t.replace('b15','O');
        t = t.replace('b16','P');
        t = t.replace('b17','Q');
        t = t.replace('b18','R');
        t = t.replace('b19','S');
        t = t.replace('b20','T');
        t = t.replace('b21','U');
        t = t.replace('b22','V');
        t = t.replace('b23','W');
        t = t.replace('b24','X');
        t = t.replace('b25','Y');
        t = t.replace('b26','Z');

        t = t.replace('b28','А');
        t = t.replace('b29','Б');
        t = t.replace('b30','В');
        t = t.replace('b31','Г');
        t = t.replace('b32','Д');
        t = t.replace('b33','Е');
        t = t.replace('b34','Ё');
        t = t.replace('b35','Ж');
        t = t.replace('b36','З');
        t = t.replace('b37','И');
        t = t.replace('b38','Й');
        t = t.replace('b39','К');
        t = t.replace('b40','Л');
        t = t.replace('b41','М');
        t = t.replace('b42','Н');
        t = t.replace('b43','О');
        t = t.replace('b44','П');
        t = t.replace('b45','Р');
        t = t.replace('b46','С');
        t = t.replace('b47','Т');
        t = t.replace('b48','У');
        t = t.replace('b49','Ф');
        t = t.replace('b50','Х');
        t = t.replace('b51','Ц');
        t = t.replace('b52','Ч');
        t = t.replace('b53','Ш');
        t = t.replace('b54','Щ');
        t = t.replace('b55','Ъ');
        t = t.replace('b56','Ы');
        t = t.replace('b57','Ь');
        t = t.replace('b58','Э');
        t = t.replace('b59','Ю');
        t = t.replace('b60','Я');
        
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
