#모듈 테스트용
def my_add(a,b):
    return a+b

def my_sub(a,b):
    return a-b

# 테스트 코드
# print(my_add(7,3))
# print(my_sub(7,3))

#모듈로써 실행 vs py파일 실행인지 구분해보기
print(f"mymoudle안에서의 __name__:{__name__}")

#모듈로 불렀을 때는 실행 X, 이 파일 자체가 실행됐을 때만 실행되도록
#모듈 테스트 용도로 사용
if __name__ == "__main__": 
    print(my_add(7,3))
    print(my_sub(7,3))