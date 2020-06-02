import json
def set_charset(name):
    character = {
        "name": name,
        "level": 1,
        "hp": 100,
        "items": ["돌맹이","돌덩이"],
        "skill": ["돌던지기"]
    }
    with open("save.txt",'w',encoding='utf-8') as f:
        json.dump(character,f, ensure_ascii = False , indent=4)
    #print("{0}님 반갑습니다. (hp {1})으로 게임을 시작 합니다.".format(character"

@app.route('/hello/<name>')
def helloovar(name):
    character = game.set_charact(name)
    return "{0}님 반갑습니다. (hp{1})으로 게임을 시작합니다.".format(character["name"]),

# @app.route('/game')
# def game():
#   return "{0}님 반갑습니다. (hp{1})으로 게임을 시작합니다.".format(character["name"])

def charact(name):
    character = {
        "name":name,
        "level":1,
        "hp": 100,
        "items":["돌맹이","돌덩이"],
        "skill":["돌던지기"]
    }
    print("{0}님 반갑습니다. (hp{1})으로 게임을 시작합니다.".format(character["name"],))

print("내가 만든 게임")
name = input("이름을 입력하시오: ")

# 캐릭터 설정 함수
character = charact(name)


#캐릭터 정보 파일에 저장
save_game("save.txt",character)

print("길을 가다가 A를 만났습니다.")
while(True):
    try:
        print("1.싸운다 2.도망간다")
        num =int(input("선택:"))
        break
    except:
        print("숫자만 입력")

game(num, character)

with open("save.txt", "r", encoding='utf-8') as f: 
    data = f.read() 
    character = json.loads(data) 
    
print(type(character))
print(character)


