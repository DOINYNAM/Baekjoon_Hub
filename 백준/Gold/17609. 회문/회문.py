def check_palindrome(word):
    front = 0
    back = len(word) - 1
    
    while front < back:
        if word[front] != word[back]:
            # 앞쪽 문자를 제거하는 경우
            remove_front = word[front+1:back+1]
            # 뒤쪽 문자를 제거하는 경우
            remove_back = word[front:back]
            if remove_front == remove_front[::-1] or remove_back == remove_back[::-1]:
                return 1  # 한 문자를 제거하여 회문을 만들 수 있음
            return 2  # 회문을 만들 수 없음
        front += 1
        back -= 1

    return 0  # 원래부터 회문임

N = int(input())
for _ in range(N):
    word = input()
    print(check_palindrome(word))