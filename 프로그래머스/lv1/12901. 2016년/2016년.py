def solution(a, b):
    day_list = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return day_list[(sum(month_list[:a-1]) + b) % 7]