from DoublyLinkedList import *
import generate_right_text
import tkinter as tk
import time
import sys

L = List()
test_text = generate_right_text.get_random_text(10_000)


def submit_linkedlist():
    print("Doubly linked list\n------------------")
    print(sys.getsizeof(L))
    start_time = time.time()
    L.split_text_into_list(test_text)  # entry.get())
    print(sys.getsizeof(L))

    if L.check_text():
        L.task_action()
        print(f"{time.time() - start_time}c")
        label_result.config(text=str(L))
    else:
        label_result.config(text="Текст має не коректно введене слово")


def submit_pythonlist():
    print("Python list\n-----------")
    split_text = []
    print(sys.getsizeof(split_text))
    start_time = time.time()
    text = test_text#entry.get()
    split_text = text.split()
    print(sys.getsizeof(split_text))
    for word in split_text:
        if 0 == len(word) % 2:
            label_result.config(text="Текст має не коректно введене слово")
            return "error"
    for i in range(len(split_text)):
        if len(split_text[i]) == 1:
            split_text[i] = " "
        else:
            split_text[i] = split_text[i][1:-1:]
    print(f"{time.time() - start_time}c")
    label_result.config(text=str(split_text)[1:-1:].replace("'", ""))


root = tk.Tk()
root.title("DoublyLinkedListCP")

label = tk.Label(root,
                 text="Введіть текст, всі слова якого мають неапрну довжину\n(передбачається, що слова будуть "
                      "розділені ' '[пробілом]):\n Результат:")
label.pack()

label_result = tk.Label(root, text="")
label_result.pack()

entry = tk.Entry(root)
entry.pack()

button_linkedlist = tk.Button(root,
                              text="Надрукувати слова без першого та останнього\nсимволу і додати до кожного слова "
                                   "знак ','",
                              command=submit_linkedlist)
button_linkedlist.pack()

button_pythonlist = tk.Button(root,
                              text="Надрукувати те саме, що робить і кнопка вище,\nале використовуючи звичайний "
                                   "пайтоновський список",
                              command=submit_pythonlist)
button_pythonlist.pack()

root.mainloop()
