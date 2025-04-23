import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

color = '#EDE8D9'


class HolidayChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Каждый день праздник")
        self.root.geometry("400x711")
        self.root.configure(bg=color)

        self.current_date = date.today()
        self.visible_count = 5  # сколько праздников показывать сразу
        self.celebrations = self.fetch_celebrations(self.get_url())

        # Настройка стилей
        self.style = ttk.Style()
        self.style.configure('TFrame', background=color)
        self.style.configure('TLabel', background=color)
        self.style.configure('Nav.TButton', font=("Arial", 12, "bold"), foreground="white", background="#5A8F7B")
        self.style.map('Nav.TButton', background=[('active', '#457D68')])

        # Навигационные кнопки
        self.nav_frame = ttk.Frame(self.root)
        self.nav_frame.pack(fill='x', pady=5)

        self.prev_btn = ttk.Button(self.nav_frame, text="← Вчера",
                                   style='Nav.TButton', command=self.show_previous_day)
        self.prev_btn.pack(side='left', padx=10)

        self.today_btn = ttk.Button(self.nav_frame, text="Сегодня",
                                    style='Nav.TButton', command=self.show_today)
        self.today_btn.pack(side='left', padx=10)

        self.next_btn = ttk.Button(self.nav_frame, text="Завтра →",
                                   style='Nav.TButton', command=self.show_next_day)
        self.next_btn.pack(side='right', padx=10)

        # Основной интерфейс
        self.canvas = tk.Canvas(root, bg=color, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.display_celebrations()

    def fetch_celebrations(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            return [h4.text.strip() for h4 in soup.find_all('h4') if h4.text.strip()]
        except Exception as e:
            return [f"Ошибка загрузки: {str(e)}"]

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def display_celebrations(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        formatted_date = self.current_date.strftime('%d.%m.%Y')

        ttk.Label(self.scrollable_frame,
                  text='Какой сегодня праздник?',
                  font=("Bookman Old Style", 12)).pack(pady=5, anchor='w')

        ttk.Label(self.scrollable_frame,
                  text=formatted_date,
                  font=("Bookman Old Style", 14, "bold")).pack(pady=10, anchor='w')

        for celebration in self.celebrations[:self.visible_count]:
            emoji = "🎉"
            ttk.Label(self.scrollable_frame,
                      text=f"{emoji} {celebration}",
                      font=("Bookman Old Style", 12),
                      wraplength=350).pack(pady=5, anchor="w")

        if self.visible_count < len(self.celebrations):
            ttk.Button(self.scrollable_frame, text="Показать ещё", command=self.show_more).pack(pady=10)

    def show_more(self):
        self.visible_count += 5
        self.display_celebrations()

    def update_display(self, new_date):
        self.current_date = new_date
        self.visible_count = 5  # сброс при смене даты
        self.celebrations = self.fetch_celebrations(self.get_url())
        self.display_celebrations()
        self.canvas.yview_moveto(0)

    def get_url(self):
        if self.current_date == date.today():
            return "https://kakoyprazdnik.com/"
        elif self.current_date == date.today() - timedelta(days=1):
            return "https://kakoyprazdnik.com/vchera/"
        elif self.current_date == date.today() + timedelta(days=1):
            return "https://kakoyprazdnik.com/zavtra/"
        else:
            return "https://kakoyprazdnik.com/"

    def show_previous_day(self):
        self.update_display(date.today() - timedelta(days=1))

    def show_today(self):
        self.update_display(date.today())

    def show_next_day(self):
        self.update_display(date.today() + timedelta(days=1))


# Запуск приложения
root = tk.Tk()
app = HolidayChecker(root)
root.mainloop()
