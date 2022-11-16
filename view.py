from main import OperationType


def show_greetings():
    print("Добро пожаловать в телефонный справочник")


def get_operation_type():
    ordinal = int(
        input("Введите тип операции:\n1 для добавления; 2 для поиска; 3 для импорта; 4 для экспорта; 5 для выхода "))
    return OperationType(ordinal)


def get_new_name():
    return input("Введите имя новой записи: ")


def get_new_number():
    return input("Введите телефон новой записи: ")


def show_added_succeed():
    print("Успешно добавлено")


def get_name_for_search():
    return input("Введите имя для поиска: ")


def show_entry_found(name, phone):
    print(f"Для имени {name} найден телефон {phone}")


def show_not_found():
    print("Не найдено")


def get_file_name_for_import():
    return input("Введите имя файла для импорта: ")


def show_import_succeed():
    print("Успешно импортировано")


def show_export(file_name):
    print(f"Экпортировано в файл: {file_name}")


def show_error(error):
    print(f"Произошла ошибка: {error}")


def show_goodbye():
    print("Приходите ещё!")