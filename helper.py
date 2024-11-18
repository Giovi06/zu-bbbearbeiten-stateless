from dataclasses import dataclass
from datetime import datetime, date

items = []

@dataclass
class Item:
    text: str
    due_date: date
    isCompleted: bool = False


def add(text, due_date):
    # Konvertiere das Datum in ein datetime.date-Objekt
    parsed_date = datetime.strptime(due_date, '%Y-%m-%d').date()
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text, parsed_date))

def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
