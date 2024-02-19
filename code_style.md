# 코드 스타일 가이드


## 명명 규칙
파일 내부, 클래스 내부 등 스코프가 한정된 곳에서만 사용되는 변수일 경우 이름 앞에 _ 붙이기
(필요 없다 판단되는 경우 생략)
### 변수, 필드
스네이크 케이스 사용 (ex: my_variable)

### 상수
스크리밍 스네이크 케이스 사용 (ex: MY_CONSTANT)

### 함수, 메서드
스네이크 케이스 사용 (ex: my_variable)

### 클래스
파스칼 케이스 사용 (ex: MyClass)


## import문
### 순서
1. 표준 라이브러리 (ex: os, json)
2. 외부 라이브러리 (ex: numpy, pandas)
3. discord.py 라이브러리 (단, `import foo; from foo import bar`와 같이 라이브러리를 임포트 할 경우 import foo 문이 위에 오도록 코드 작성)
4. 프로젝트 내부 모듈

### 소괄호
`from foo import bar, baz`와 같이 한 모듈에서 여러 객체를 가져올 경우 소괄호로 감싸기
```python
from typing import (Any, Iterable)
```

## 줄바꿈
### 1번
- 셔뱅과 import문
- import문 순서에서 번호가 바뀔 때
- 파일의 끝
- 그 외에 1번의 줄바꿈이 보기 좋다 판단되는 경우

### 2번
- import문 후
- 각 함수 선언 전후
- 각 클래스 선언 전후

## 공백
### 변수, 필드
- 모든 연산자 전후에 공백 1개
- 타입 힌팅시 콜론 뒤에 공백 1개
ex: `var: int = 1`
- 칸 맞추기용 공백 금지
```python
my_var1 = 0
my_var  = None  # 금지
```
### 파라미터
파라미터의 기본값이 지정되지 않았을 경우 콜론 뒤 공백 1개.
만약 지정되었을 경우 콜론 뒤 공백 1개, 대입 연산자 전후에 공백 1개
```python
def my_func1(param: bool):
    pass

def my_func2(param: bool = True):
    pass
```
### 주석 
- 코드 뒤에 주석 작성시 앞 2칸, 뒤 1칸
- 새 줄에 주석 작성시 뒤 1칸
```python
do_something()  # 코드 뒤에서 주석 작성
# 새 줄에서 주석 작성
```
- (데이터의 경우) 칸 맞추기용 공백을 주석 기호 앞에 사용 가능
```json
{
    "my_val": true,   // 칸 맞추기용 주석 사용됨
    "my_val2": false  // 주석
}
```

## 객체 선언
- 전역 변수는 import문과 전역 함수 선언 전에 모아서 선언
- 전역 함수는 전역 변수 후, 전역 클래스 선언 전에 모아서 선언
- 전역 클래스는 전역 함수 선언 후에 모아서 선언
- 단, 선언 순서를 바꿔야만 하는 경우 예외
```python
global_var1 = object()  # 전역 변수
global_var2 = True


def func_1():  # 전역 함수
    pass


def func_2():
    pass


class A:  # 전역 클래스
    pass


class B:
    pass
```

## 타입 힌팅
### 변수, 필드
기본적으로 타입 힌팅 금지
단, 필요하다 판단되는 경우 사용

### 함수, 메서드
각 파라미터에 타입 힌팅 사용.
파라미터의 타입이 Any 경우 typing.Any 사용해 파라미터의 타입 지정
반환값이 `None`일 경우 반환값 타입 힌팅 금지

```python
from typing import Any


def function1(x: int) -> int:
    return x + 1


def function2(x: Any):
    return None
```

## 독스트링
### 파라미터
함수, 메서드, 클래스의 생성자의 파라미터 독스트링 작성시
`:param <파라미터 이름>: <설명>` 형식으로 작성

### 반환값
함수의 반환값 독스트링 작성시
`:return: <설명>` 형식으로 작성
