'''
참고 : https://peps.python.org/pep-0008/

problem_ex
1. 파이썬 개발자는 PEP 8을 준수해야 할까요? 만약 그렇다면 왜 준수해야 할까요?
2. 아래의 코드에는 'PEP 8'의 가이드라인에 어긋난 부분이 존재합니다. 어떤 부분이 어긋났고 어떻게 수정하면 될까요?
3. 아래 코드는 무엇을 하는 코드일까요? 이 코드를 실행하면 어떤 결과를 얻게 될까요?

answer_ex
1. 'PEP 8' 은 가독성과 일관성을 위하여 만들어진 하나의 '규칙'이다.
-> 가이드라인을 정한 이유는 가독성과 일관성을 위하여 만들어졌지만 이를 좀 더 구체적으로 얘기하면 다음과 같다.
    - 대부분의 경우 의미없는 경우가 없다. (각각이 의미하는 것들이 있기에 규칙에 맞게 사용하지 않으면 원하는 방향으로 흘러가지 않을 수 있다.)
    - 뜻하지 않는 영문 모를 충돌이 발생할 수 있다. 
    - 협업을 함에 있어서 기준 점이 없을 경우 소통이 원활하지 않을 수 있다.
    - 호환성 문제 혹은 오류가 발생할 수 있다.
- > 따라서 PEP 8을 준수해야 하는 이유는 다음과 같다.
    - 여러가지 발생될 수 있는 오류와 충돌을 최소한으로 줄이면서 깔끔하고 효율적인 작업을 하기 위함.
    - 협업,의사소통을 원활하게 하기 위함.
    - 수정하거나 오류 해결을 할 때 보다 쉽고 빠르게 하기 위함. 
- > 위와 같은 이유로 파이썬 개발자들은 "다른 규칙들보다 최소한의 오류와 충돌이 발생되는" PEP 8을 준수해야 한다.


2. 가이드라인은 다음과 같다.
    - 들여쓰기
    - 최대 라인 길이
    - 빈 줄
    - 소스 파일 인코딩 (항상 UTF-8 사용, ASCII 전용 식별자 사용)
    - 수입품 (가져오기는 일반적으로 별도의 줄에 있어야 함, 
    가져오기 시스템이 잘못 구성된 경우 절대 가져오기 권장이유는 오류 덜 발생)
    - 모듈 수준 던더 이름
    - 문자열 따옴표
    - 표현식 및 명령문의 공백 ((ex)후행 공백 피해라)
    - 후행 쉼표를 사용하는 경우
    - 코멘트 (의사소통 문제)
    - 댓글 차단
    - 인라인 댓글
    - 문서 문자열
    - 명명 규칙
    - 프로그래밍 권장 사항
- > 아래 코드에서 76줄에 들여쓰기가 잘못됐다.
    들여쓰기는 4개의 스페이스를 사용할 것 (혹은 탭이며 둘 중 하나만 사용하길 권장)
- > 따라서 아래 코드와 같이 수정하면 된다.


3. 아래 코드는 다음과 같은 역할을 하는 코드 인 것 같다.
- > 원하는 데이터를 입력한 순서대로 저장해두고, 필요시 데이터의 개수를 알려준다.
    데이터가 꽉 차서 지워야 할 땐 오래된 것부터 지운다. 이때 지울 데이터가 무엇인 지 알려준다.
- > 이 코드를 실행할 경우 2 3 1 5의 결과를 얻을 수 있다. 
        - 저장공간에 3,5를 추가한 후 데이터의 개수를 확인한다.(=2)
        - 저장공간에 오래된 데이터 하나를 삭제한 후 삭제한 데이터를 출력한다.(=3)
        - 저장공간에 있는 데이터의 개수를 확인한다.(=1)
        - 저장공간에 있는 가장 오래된 데이터가 무엇인지 확인한다. (=5)

'''


# code_start

# error_class
class Empty(Exception):
    pass

# list add/modify/del
class ArrayQueue:
    # 생성자
    def __init__(self):
        self._data = []

    # Duck Typing vs none
    '''
    def len(self):              
        return len(self._data)
    '''

    # Duck Typing(?)
    def __len__(self):
        return len(self._data)

    # 리스트 요소 유/무 확인
    def is_empty(self):
        if len(self._data):
            return False
        else:
            return True

    '''
  def first(self):
    '''

    # 첫 번째 요소 출력
    def first(self):
        if len(self._data) == False:        
            raise Empty("error")            # 에러 발생 시키기
        else:
            return self._data[0]

    # 첫 번째 요소 추출    
    def dequeue(self):
        if len(self._data) == False:
            raise Empty("error")
        val = self._data[0]
        del self._data[0]
        return val

    # 인덱스 추가
    def enqueue(self,e):
        self._data.append(e)

Q = ArrayQueue()
Q.enqueue(3)
Q.enqueue(5)
print(len(Q))
print(Q.dequeue())
print(len(Q))
print(Q.first())


# test
'''
print("test")
print(len(Q))
pring("hi")
'''
