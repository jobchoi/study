#include <iostream>

void funMax(int&, int& );
void getData(int *,int *);

// main 함수 시작, main -> 프로그램 시작부
int main() {
	int a(0), b(0); // 변수를 2개 정의 및 선언

	// 문자열 출력
	std::cout << "Start " << std::endl;
	
	// 사용자 함수1 콜
	getData(&a,&b);
	
	return 0;
}

// 리턴은 void로 리턴하는 값은 없고, 매개변수(파라미터) 2개를 포인터로 받는다.
void getData(int *a,int *b) {

	std::cout << "input a" <<std::endl;	// 문자열 출력
	std::cin >> *a;	// 사용자로부터 값을 입력 받는다
	std::cout << "input b" << std::endl;
	std::cin >> *b;

	if (a <= 0 || b <= 0) // 입력된 값이 1보다 작은 값인지 체크
	{
		std::cout << "1이상에 양수를 입력해주세요. a : " << *a<< " b : " << *b << std::endl;
	}
	if(*a==*b){	// 같은 수인지 체크
		
		std::cout << "두수가 동일합니다. a : " << *a<< " b : " << *b << std::endl;
	}

	// 사용자 함수2 콜
	funMax(*a, *b);
	return ;
}

// 사용자 함수 1과 같이 리턴은 따로 하지 않음, 파라미터로 2개(포인터, 주소를 받음, 원본에 영향을 미친다)를 입력받음
void funMax(int &a, int &b) {
	if (a >= 1 && b >= 1) {
		if (a > b) {
			a = a - b;
			if (a > 0) {
				std::cout << "(1). a>b -> a : " << a << " b : " << b << std::endl;
				if (a == b) {	// 변수 a와 b가 서로 같은경우

					// 문자열을 출력하고 변수 a에 값을 출력(b랑 값이 같은 상태라 b는 따로 출력하지 x)
					// retrun을 만나서 호출한 함수가 종료되면 호출했던 사용자 함수가 연쇄적으로 종료된다. 
					std::cout << "GCD : " << a <<std::endl;

					// return 을 만나면 해당 함수는 종료가 됨
					return;
				}

				/*
	
				두 변수의 값이 양수이고, 서로 같지 아니한 상태라면,
				프로그램이 종료되지 않았지만, 현 상태에서 사용자 함수를 재 호출한다. (이 부분이 재귀가 되는 것)
				*/

				funMax(a, b);
			}
		}
		else {
			b = b - a;
			if (b > 0) {
				std::cout << "(2). b > a -> a : " << a << " b : " << b << std::endl;
				if (a == b) {
					std::cout << "GCD : " << a << std::endl;
					return;
				}
				funMax(a, b);
			}
		}
	}
	else
	{
		std::cout << "(4(. else 입력한 값을 확인(입력값을 양수에 한해서)  => a : " << a << " b : " << b << std::endl;
	}
	return;
}
