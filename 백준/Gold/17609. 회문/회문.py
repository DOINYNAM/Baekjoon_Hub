def is_palindrome(s):
    return s == s[::-1]

def check_substring(front, back, word):
    # 앞쪽 문자 또는 뒤쪽 문자를 제거한 후 회문인지 검사
    return is_palindrome(word[front:back]) or is_palindrome(word[front+1:back+1])

def check_palindrome(word):
    front = 0
    back = len(word) - 1

    while front < back:
        if word[front] != word[back]:
            # 불일치가 발견되면, 한 번에 하나의 문자를 제거하고 나머지 부분이 회문인지 확인
            if check_substring(front, back, word):
                return 1  # 한 문자를 제거하여 회문을 만들 수 있음
            else:
                return 2  # 회문을 만들 수 없음
        front += 1
        back -= 1

    return 0  # 원래부터 회문임

N = int(input())
for _ in range(N):
    word = input()
    print(check_palindrome(word))