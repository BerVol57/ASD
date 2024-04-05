from DoublyLinkedList import *
import generate_right_text
import tkinter as tk
import time
import sys

L = List()
test_text = generate_right_text.get_random_text(10_000)

def submit():
    print(sys.getsizeof(L))
    start_time = time.time()
    L.split_text_into_list( test_text )#entry.get())
    print(sys.getsizeof(L))

    if L.check_text():
        L.task_action()
        print(f"{time.time() - start_time}c")
        label_result.config(text=str(L))
    else:
        label_result.config(text="Текст має не коректно введене слово")


root = tk.Tk()
root.title("DoublyLinkedListCP")

label = tk.Label(root, text="Введіть текст, всі слова якого мають неапрну довжину\n(передбачається, що слова будуть розділені ' '[пробілом]):\n Результат:")
label.pack()

label_result = tk.Label(root, text="")
label_result.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Надрукувати слова без першого та останнього\nсимволу і додати до кожного слова знак ','", command=submit)
button.pack()

root.mainloop()
