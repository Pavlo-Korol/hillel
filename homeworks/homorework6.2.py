def format_time(seconds):
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    
    if days == 1:
        day_str = 'день'
    elif 1 < days <= 4:
        day_str = 'дні'
    else:
        day_str = 'днів'
    
    formatted_time = f"{days} {day_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    return formatted_time


seconds_input = int(input("Введіть кількість секунд: "))

if seconds_input < 0 or seconds_input > 8640000:
    print("Неправильне значення. Введіть число більше або дорівнює 0 і менше ніж 8640000.")
else:
    formatted_result = format_time(seconds_input)
    print("Час у читабельному форматі:", formatted_result)
