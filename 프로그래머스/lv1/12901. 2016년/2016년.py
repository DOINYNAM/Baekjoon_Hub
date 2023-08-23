def solution(a, b):
    day_list = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"] # 1/1 금요일 기준 요일별 인덱스 설정
    month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 월별 총 일 수

    return day_list[(sum(month_list[:a-1]) + b) % 7] # 일 수 계산 후 7로 나누어 day_list 인덱스에 맞추어 요일 출력
