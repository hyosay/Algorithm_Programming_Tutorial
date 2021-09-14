# Algorithm_Programming_Tutorial

# 알고리즘 c++ 정리

### 알고리즘이 무엇인가.

## 2주차

### 자료구조

자료를 잘 구조화 시킨 것

#### 2.1 배열
> 하나의 이름, 동일한 자료형, 연속된 공간

index로 배열의 위치를 파악함
> start_index = 0   
> end_index = n - 1

```c++
#define CRT_SECURE_NO_WANINGS
#define N 5
#include <stdio.h>

int main(){
    int i;
    int a[N];
    for (i = 0; i < N; i++){
        printf("a[%d] : ", i);
        scanf("%d", &a[i]);
    }
    puts("각 요소의 값");

    for(i = 0; i < N; i++){
        printf("a[%d] = %d \n", i, a[i]);
    }
    return 0;
}
```
<img width="167" alt="스크린샷 2021-09-14 오전 9 25 59" src="https://user-images.githubusercontent.com/46950334/133174054-7358202e-f628-4c8a-a92f-2dc3cd96d1c1.png">


sizeof() 메모리의 크기
```c++
# include <stdio.h>

int main(void){
    int i;
    int a[5] = {1, 2, 3, 4, 5};
    int na  = sizeof(a) / sizeof(a[0]);
    printf("%d", na);
}
```

array를 사용할떄 상수화를 해야한다  번수를 사용하면 안된다. 
```c++

// 오류가 난다. 
int a = 5;
int b[a] = {1, 2, 3, 4, 5};

// 해답
int b[5] = {1, 2, 3, 4, 5};
```
#### 2.2 할당
##### 2.2.1 동적할당
실행중에 메모리 할당하는 것 
자원을 최적화 할때는 편하다.

##### 2.2.2 정적할당
실행전 메모리를 할당하는 것
