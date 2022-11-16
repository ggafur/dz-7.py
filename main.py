from enum import Enum
import view
import data


class OperationType(Enum):
    ADD = 1
    FIND = 2
    IMPORT = 3
    EXPORT = 4
    EXIT = 5


def main():
    view.show_greetings()
    while True:
        operation_type = view.get_operation_type()
        # Python настолько крив что не может сравнивать Enum:
        # operation_type is OperationType.ADD
        # поэтому приходится сравнивать их порядковые значения(((
        if operation_type.value == OperationType.ADD.value:
            add_entry()
        elif operation_type.value == OperationType.FIND.value:
            find_entry(view.get_name_for_search())
        elif operation_type.value == OperationType.IMPORT.value:
            import_data()
        elif operation_type.value == OperationType.EXPORT.value:
            export_data()
        elif operation_type.value == OperationType.EXIT.value:
            view.show_goodbye()
            break


def add_entry():
    name = view.get_new_name()
    phone = filter_digits(view.get_new_number())
    if data.add_entry(name, phone):
        view.show_added_succeed()


def find_entry(name):
    phone = data.find(name)
    if phone:
        view.show_entry_found(name, phone)
    else:
        view.show_not_found()


def import_data():
    file_name = view.get_file_name_for_import()
    try:
        data.import_data(file_name)
        view.show_import_succeed()
    except Exception as ex:
        view.show_error(ex)


def export_data():
    try:
        export_file_name = "export.json"
        data.export_data(export_file_name)
        view.show_export(export_file_name)
    except Exception as ex:
        view.show_error(ex)


def filter_digits(raw):
    return ''.join((filter(lambda c: c.isdigit(), raw)))


if __name__ == '__main__':
    main()