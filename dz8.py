#Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phones.txt')
    reserve_book=read_txt('reserve.txt')
    while (choice<9):
        if choice==1:
            print_result(phone_book)
            input('Нажмите enter кнопку чтобы продолжить...')  
        elif choice==2:
            print_result(reserve_book)
            input('Нажмите enter кнопку чтобы продолжить...')  
        elif choice==3:
            src_txt=input('Введите текст для поиска\n')
            print(find_by_any(phone_book,str(src_txt)))
        elif choice==4:     
            print(add_new(phone_book))	    	
        elif choice==5:            
            print(change_by_last(phone_book))
        elif choice==6:            
            print(del_rec(phone_book))
        elif choice==7:           
            copy_from_file(reserve_book,phone_book,'phones.txt') 
        elif choice==8:           
            copy_from_file(phone_book,reserve_book,'reserve.txt')                   
        choice=show_menu()
    print("Выход")
def copy_from_file(from_book,to_book,file_name):
    print_result(from_book)
    idx = int(input("Какой номер скопировать? \n"))
    to_book.append(from_book[idx-1])
    write_txt(file_name,to_book)

def del_rec(phone_book):
    search = input('Введите фамилию контакта для удаления\n')
    del_idx = -1
    for i in range(len(phone_book)): 
        if phone_book[i]["Фамилия"]== search:
            del_idx=i
            break
    if del_idx == -1:
        print("Такая запись не найдена")
        return
    phone_book.pop(del_idx)    
    write_txt('phones.txt',phone_book)


def change_by_last(phone_book):
    search = input('Введите фамилию контакта для изменения\n')
    ch_idx = -1
    for i in range(len(phone_book)): 
        if phone_book[i]["Фамилия"]== search:
            ch_idx=i
            break
    if ch_idx == -1:
        print("Такая запись не найдена")
        return
    lastname=input('Введите новое значение фамилия было: '+phone_book[ch_idx]["Фамилия"]+' \n')    
    name=input('Введите новое значение имя было: '+phone_book[ch_idx]["Имя"]+' \n')
    number=input('Введите новое значение номер было: '+phone_book[ch_idx]["Номер"]+' \n')
    note=input('Введите новое значение описание было: '+phone_book[ch_idx]["Описание"]+' \n')  
    phone_book.pop(ch_idx)
    phone_book.append(fio_dict([lastname,name,number,note]))
    write_txt('phones.txt',phone_book)


def add_new(phone_book):
    lastname=input('Введите фамилию \n')
    name=input('Введите имя  \n')
    number=input('Введите номер  \n')
    note=input('Введите описание  \n')
    phone_book.append(fio_dict([lastname,name,number,note]))
    write_txt('phones.txt',phone_book)
    input('Запись добавлена. Нажмите enter чтобы продолжить...')  

def find_by_any(phone_book,src_txt):
    s=''
    for i in range(len(phone_book)):   
        for v in phone_book[i].values():            
            if v.find(src_txt)>-1:
                s=s+format_out(phone_book[i])+'\n'
                break
    if len(s)>0:
        print('Найдено:')
        print(s)
    else:
        print('Записи не найдены')
    input('Нажмите enter кнопку чтобы продолжить...')  


def print_result(phone_book):      
      for i in range(len(phone_book)):        
            print(str(i+1)+" - "+format_out(phone_book[i]))  
      


def format_out(rec):
    return "{0:<10}{1:<10}{2:<10}{3:<15}".format(rec["Фамилия"],rec["Имя"],rec["Номер"],rec["Описание"])


def show_menu():
   # os.system('cls')
    print("\nВыберите необходимое действие:\n"
            "1. Отобразить весь справочник\n"
            "2. Отобразить весь резервный\n"
            "3. Поиск по всем полям\n"
            "4. Добавить абонента в справочник\n"            
            "5. Изменить абонента в справочнике\n"
            "6. Удалить запись \n"
            "7. Скопировать из резерва \n"
            "8. Скопировать в резерв \n"
            "9+ Закончить работу\n")
    choice = int(input())
    return choice


def fio_dict(vals):
    fields=    ['Фамилия', 'Имя', 'Номер', 'Описание']
    return dict(zip(fields, vals))


def read_txt(filename): 
    phone_book=[]
    
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = fio_dict( line[:-1].split(','))
            phone_book.append(record)	
    return phone_book



def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

 
work_with_phonebook()

   