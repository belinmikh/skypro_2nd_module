import datetime
import json
import os
import sys
import tkinter.messagebox as mb
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.simpledialog import askstring

from src.fileio import file_to_list
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.tools import extract
from src.widget import mask_account_card

STATUSES = ["EXECUTED", "CANCELED", "PENDING", ""]


def provide_ui() -> None:
    """Provides Tkinter user interface for main logic"""
    window_title = "sky.pro // indpd58.0 // Belin Mikhail"

    filetypes = (
        ("Все файлы", "*"),
        ("Excel-файлы", "*.xlsx"),
        ("Значения, разделённые ';'", "*.csv"),
        ("JSON-файлы", "*.json"),
    )
    path = askopenfilename(title="Открыть файл", initialdir=os.getcwd(), filetypes=filetypes)
    if not path:
        mb.showerror(window_title, "Файл не был выбран!")
        sys.exit("Missing file")

    if path.endswith(".xlsx"):
        mb.showinfo(window_title, "Успешно выбран файл .xlsx")
    elif path.endswith(".csv"):
        mb.showinfo(window_title, "Успешно выбран файл .csv")
    elif path.endswith(".json"):
        mb.showinfo(window_title, "Успешно выбран файл .json")

    transactions = file_to_list(path)

    if len(transactions) == 0:
        mb.showerror(window_title, "Нечего фильтровать, либо при чтении произошла ошибка")
        sys.exit("Bad / empty / missing file")

    while True:
        filter_match = askstring(
            window_title,
            f"Обнаружено {len(transactions)} транзакций.\n"
            "Введите статус, по которому необходимо выполнить фильтрацию,\n"
            "или оставьте поле пустым, если не хотите её запускать",
        )
        if filter_match is None or filter_match.upper().strip() in STATUSES:
            break
        else:
            mb.showerror(
                window_title,
                f"Доступна фильтрация только по\n"
                f"следующим статусам: {', '.join(STATUSES)}.\n"
                f"Повторите попытку",
            )

    if filter_match and not filter_match.isspace():
        filter_match = filter_match.upper().strip()
        transactions = filter_by_state(transactions, filter_match)
        if len(transactions) == 0:
            mb.showinfo(window_title, "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            sys.exit("Out of records")
        mb.showinfo(window_title, f"Отфильтровано по статусу {filter_match}")

    do_date_sort = mb.askyesnocancel(
        window_title, f"Количество транзакций: {len(transactions)}\n" "Выполнить сортировку по дате?"
    )
    if do_date_sort is None:
        mb.showerror(window_title, "Операция прервана пользователем")
        sys.exit("User interrupt")
    if do_date_sort:
        reverse = mb.askyesnocancel(window_title, "Сначала последние?")
        if reverse is None:
            mb.showerror("Операция прервана пользователем")
            sys.exit("User interrupt")
        transactions = sort_by_date(transactions, reverse)
        if reverse:
            mb.showinfo(window_title, "Выполнена фильтрация в порядке,\n" "обратном историческому (по убыванию даты)")
        else:
            mb.showinfo(window_title, "Выполнена фильтрация в\n" "историческом порядке (по возрастанию даты)")

    do_rub_only = mb.askyesnocancel(
        window_title, f"Количество транзакций: {len(transactions)}\n" "Оставить только рублёвые транзакции?"
    )
    if do_rub_only is None:
        mb.showerror(window_title, "Операция прервана пользователем")
        sys.exit("User interrupt")
    if do_rub_only:
        transactions = [
            t
            for t in transactions
            if "RUB" in [extract(t, ("operationAmount", "currency", "code")), extract(t, ("currency_code",))]
        ]
        if len(transactions) == 0:
            mb.showinfo(window_title, "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            sys.exit("Out of records")
        mb.showinfo(window_title, "Выполнена фильтрация рублёвых транзакций")

    filter_match = askstring(
        window_title,
        f"Количество транзакций: {len(transactions)}\n"
        "Введите часть описания, по которому необходимо выполнить фильтрацию,\n"
        "или оставьте поле пустым, если не хотите её запускать",
    )
    if filter_match and not filter_match.isspace():
        transactions = filter_by_description(transactions, filter_match)
        if len(transactions) == 0:
            mb.showinfo(window_title, "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            sys.exit("Out of records")
        mb.showinfo(window_title, f"Выполнена фильтрация по вхождению\n" f"'{filter_match}' в описание")

    for t in transactions:
        try:
            date = datetime.datetime.strptime(extract(t, ("date",)), "%Y-%m-%dT%H:%M:%SZ").strftime("%d.%m.%Y")
        except ValueError:  # operations.json format
            date = datetime.datetime.strptime(extract(t, ("date",)), "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        except TypeError:
            date = "(дата отсутствует или повреждена)"

        print(date, extract(t, ("description",)))

        fr = mask_account_card(extract(t, ("from",)))
        to = mask_account_card((extract(t, ("to",))))
        if fr and to:
            print(fr + " -> " + to)
        elif fr:
            print(fr)
        elif to:
            print("(->) " + to)

        currency_code = extract(t, ("currency_code",))
        if not currency_code:
            currency_code = extract(
                t,
                (
                    "operationAmount",
                    "currency",
                    "code",
                ),
            )
        amount = extract(t, ("amount",))
        if not amount:
            amount = extract(
                t,
                (
                    "operationAmount",
                    "amount",
                ),
            )

        if currency_code and amount:
            print("Сумма:", currency_code, amount, "\n")
        else:
            print("Сумма: данные отсутствуют или повреждены")

    now = datetime.datetime.now().strftime("%Y-%m-%d")

    do_save_file = mb.askyesno(
        window_title,
        f"Результат выведен в консоль.\n"
        f"Записать {len(transactions)} операций в {now}.json?\n\n"
        "Внимание! Запись в исходном виде (без маскировки данных)",
    )
    if do_save_file:
        path = askdirectory(title=window_title, initialdir=os.getcwd())
        if sys.platform.startswith("win"):
            symbol = "\\"
        else:
            symbol = "/"
        with open(path + symbol + f"{now}.json", "w", encoding="UTF-8") as f:
            json.dump(transactions, f)
