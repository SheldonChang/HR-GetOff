import tkinter as tk
from datetime import datetime, timedelta
import time


def shake_window(root, intensity=10, duration=500):
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    x = root.winfo_x()
    y = root.winfo_y()
    center_x = x + window_width // 2
    center_y = y + window_height // 2
    end_time = time.time() + (duration / 1000)
    while time.time() < end_time:
        offset_x = intensity if time.time() % 2 == 0 else -intensity
        offset_y = intensity if time.time() % 2 == 0 else -intensity
        new_x = center_x + offset_x - window_width // 2
        new_y = center_y + offset_y - window_height // 2
        root.geometry(f"+{new_x}+{new_y}")
        root.update()
        time.sleep(0.02)
    root.geometry(f"+{x}+{y}")


def get_remaining_seconds(checkin):
    now = datetime.now()
    compare_time = datetime.strptime('08:30', '%H:%M').time()
    time_in = datetime.strptime(checkin, '%H:%M').time()
    if time_in < compare_time:
        target_time = datetime.combine(now.date(), compare_time)
    else:
        target_time = datetime.combine(now.date(), time_in)
    end_time = target_time + timedelta(hours=9)
    remaining_time = end_time - now
    remaining_seconds = remaining_time.total_seconds()
    return int(remaining_seconds)


def change_color(view, color):
    view.configure(background=color)
    all_labels = view.winfo_children()
    for widget in all_labels:
        if isinstance(widget, tk.Label):
            widget.config(bg=color)


def update_countdown(root, label, checkin):
    remain = get_remaining_seconds(checkin)
    if remain > 0:
        if remain <= 600:
            change_color(root, "#EDC224")
        label.config(text=f"剩下 {remain} 秒就下班囉")
        label.after(1000, update_countdown, root, label, checkin)
    else:
        change_color(root, "#ED3B24")
        label.config(text="恭喜加班")


def show_window(data):
    root = tk.Tk()
    root.title(f"{data[0]} 下班倒數")
    root.geometry("300x150")
    root.attributes('-topmost', True)
    label = tk.Label(root, text=f"Hello, {data[2]} 今天{data[6]}進公司喔!")
    label.pack(pady=20)
    countdown_label = tk.Label(
      root,
      font=("Helvetica", 20),
      text="抓時間中",
      anchor="center",
    )
    countdown_label.pack(expand=True,)
    update_countdown(root, countdown_label, data[6])
    change_color(root, "#38DE10")
    root.mainloop()


def show_message():
    root = tk.Tk()
    root.withdraw()
    top = tk.Toplevel(root)
    top.title("Notification")
    top.geometry("300x100")
    message = tk.Label(top, text="No record for today", padx=20, pady=20)
    message.pack()

    def close_window():
        top.destroy()
        root.quit()

    root.after(1500, close_window)
    root.mainloop()
