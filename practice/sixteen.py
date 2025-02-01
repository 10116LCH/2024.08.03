d = {"key" : "value", 2.3 : "value", 5 : 1, 5 : "111", (1,2,3) : 3}
print(d)

a = dict()
print(a)

print(d.keys())
print(d.values())
print("-----------------------------")

# 각각의 dictionary

inventory = {"water":"5", "coke":"4", "cider":"3", "coffee":"2"}
price = {"water":"1000", "coke":"1200", "cider":"1100", "coffee":"500"}

#사용자 모드
#음료는 물, 콜라, 사이다, 커피
#가격은 1000, 1200, 1100, 500
#질문, 대답
#해당음료가 있으면 o
#해당음료가 없으면 x

mode = "manager"

def print_menu():
    print("menu를 출력합니다.")
    for i in inventory.keys():
        print(i, "가격:", price[i], " 잔여수량:", inventory[i])

def print_function():
    print("관리자가 사용가능한 기능을 출력합니다.")
    print("1. 음료를 등록하기")
    print("2. 음료를 추가하기")
    print("3. 음료를 빼기")
    print("4. 음료를 삭제하기")

def buy_drink():
    print("음료를 선택하고, 구매합니다.")

def switch_mode():
    print("mode를 전환합니다.")

def manager_login():
    print("관리자 모드에 진입합니다.")

def print_function():
    print("관리자가 사용가능한 기능을 출력합니다.")
    print("1. 음료를 등록하기")
    print("2. 음료를 추가하기")
    print("3. 음료를 빼기")
    print("4. 음료를 삭제하기")
    print("5. 사용자 모드로 전환")

def change_price():
    print("음료의 가격을 변경합니다.")

def add_drink():
    print("음료를 추가합니다.")

def register_drink():
    print("음료를 등록합니다.")

def delete_drink():
    print("음료를 삭제합니다.")

def extract_drink():
    print("음료를 제거합니다.")


while True:
    if mode == "manager":
        manager_login()
        user_input = int(input("메뉴를 선택하세요"))

        if user_input == 1:
            register_drink()
        elif user_input == 2:
            add_drink()
        elif user_input == 3:
            extract_drink()
        elif user_input == 4:
            delete_drink()
        elif user_input == 5:
            switch_mode()

    else:
        print_menu()
        user_input = input("메뉴를 선택하세요")

