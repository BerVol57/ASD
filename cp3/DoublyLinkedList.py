import sys


# Клас "Слово", що реалізоване як елемент двозв'язного списку і має функції перевірки та дії вказані в завданні
class Word:
    def __init__(self, word: str, next=None, prev=None):
        self.word = word
        self.next = next
        self.prev = prev

    def get_word(self):
        return self.word

    def set_word(self, word):
        self.word = word

    # видалення першого та останнього символу, або повертає "" якщо довжина слова 1
    def delete_first_and_last_symbol(self):
        if len(self.word) == 1:
            self.word = ''
        else:
            self.word = self.word[1:-1:]

    # перевірка слова чи є його довжина непарним числом (якщо так, то повертає False)
    def check_word_by_task(self):
        if 0 == len(self.word) % 2:
            return True
        else:
            return False

    # Функція, що повертає кількість байтів, що виділяється на фізичному носії пам'яті для цього слова
    def __sizeof__(self):
        return 48 + sys.getsizeof(self.word)


# Клас списку для слів
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def last_add(self, word: str):
        if self.tail is None:
            self.tail = Word(word)
            self.head = self.tail
        else:
            w = Word(word, None, self.tail)
            self.tail.next = w
            w.prev = self.tail
            self.tail = w

        self.length += 1

    def first_add(self, word: str):
        w = Word(word)
        if self.head is None:
            self.head = w
            self.tail = self.head
        else:
            self.head.prev = w
            w.next = self.head
            self.head = w

        self.length += 1

    def index_add(self, index: int, word: str):
        if index > self.length:
            return "Index > list length"
        elif index == self.length:
            self.last_add(word)
        elif index == 0:
            self.first_add(word)
        else:
            w = Word(word)
            k = 0
            current_word = self.head

            while k < index - 1:
                current_word = current_word.next

            w.next = current_word.next
            w.prev = current_word
            current_word.next = w

    # функція що розділяє текст за вказаним символом(дфеолт " ") і заносить утворені слова до списку
    def split_text_into_list(self, text: str, split_symbol=" "):
        word = ""
        for i in text:
            if i == split_symbol:
                self.last_add(word)
                word = ""
            else:
                word += i
        if word != "":
            self.last_add(word)

    # перевірка кожного слова в разі хиби - видає помилку
    def check_text(self):
        current_word = self.head
        for i in range(self.length):
            if current_word.check_word_by_task():
                return False
            current_word = current_word.next
        return True
        # print("All good")

    # дія для кожного слова (видалення першого та останнього символу)
    def task_action(self):
        current_word = self.head
        for i in range(self.length):
            current_word.delete_first_and_last_symbol()
            current_word = current_word.next

    def __str__(self):
        res = " "
        current_word = self.head
        for i in range(self.length):
            if i == self.length - 1:
                res += current_word.get_word()
            else:
                res += current_word.get_word() + ", "
            current_word = current_word.next
        return res

    def __sizeof__(self):
        res = 0
        current_word = self.head
        for i in range(self.length):
            res += sys.getsizeof(current_word)
            current_word = current_word.next
        return res
