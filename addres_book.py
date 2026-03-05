from collections import UserDict
from exceptions import InvalidPhoneFormat, MissingValueException


class Field():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if (not value):
            raise MissingValueException("Name is not provided")

        super().__init__(value)


class Phone(Field):
    def validate(self, value):
        if (len(value) != 10 or not value.isdigit()):
            raise InvalidPhoneFormat("Phone must contain 10 digits")

    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def set_value(self, value):
        self.validate(value)
        self.value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        record_phone = self.find_phone(phone)

        if (record_phone):
            self.phones.remove(record_phone)

    def edit_phone(self, phone, new_phone):
        record_phone = self.find_phone(phone)
        if (record_phone):
            record_phone.value = new_phone

    def find_phone(self, phone):
        return next(
            filter(lambda x: x.value == phone, self.phones), None)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def find(self, name):
        if (name in self.data.keys()):
            return self.data[name]

    def delete(self, name):
        del self.data[name]
