# Python 연습용 코드

import random

def number_game():
    print("===== 번호 맞히기 게임 =====")

    answer = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("1~100 사이 숫자를 입력하세요: "))
            attempts += 1

            if guess < answer:
                print("에게~! 더 큰 숫자입니다.")

            elif guess > answer:
                print("너무높아요!! 더 작은 숫자입니다.")

            else:
                print(f"성공! {answer}")
                print(f"총 {attempts}번 만에 맞혔습니다.")
                break

        except ValueError:
            print("숫자만 입력해주세요!")

if __name__ == "__main__":
    number_game()

    print("Hello GitHub!")
print("Fork한 hub에서 수정했습니다.")