def say():
    return "hi everybody"

def add(a,b):
    return a+b

# __name__ 은 파이썬 기본 내부 변수 중 하나
if __name__ =="__main__":
    print(say())
    print(add(5,6))