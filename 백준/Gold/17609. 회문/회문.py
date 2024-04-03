def check_palindrome(word):
    front = 0
    back = len(word) - 1
    
    while front < back:
      if word[front] != word[back]:
        remove_front = word[:front] + word[front + 1:]
        if remove_front == remove_front[::-1]:
          return 1

        remove_back = word[:back] + word[back + 1:]
        if remove_back == remove_back[::-1]:
          return 1

        else: # 회문 불가
            return 2

      front += 1
      back -= 1
  
    return 0  # 원래부터 회문임

N = int(input())
for _ in range(N):
    word = input()
    print(check_palindrome(word))
