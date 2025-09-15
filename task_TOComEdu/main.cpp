#include <iostream>

void funMax(int&, int& );
void getData(int *,int *);

int main() {
	int a(0), b(0);
	std::cout << "Start " << std::endl;
	getData(&a,&b);
	return 0;
}

void getData(int *a,int *b) {

	std::cout << "input a" <<std::endl;
	std::cin >> *a;
	std::cout << "input b" << std::endl;
	std::cin >> *b;

	if (a <= 0 || b <= 0)
	{
		std::cout << "1이상에 양수를 입력해주세요. a : " << *a<< " b : " << *b << std::endl;
	}
	if(*a==*b){
		
		std::cout << "두수가 동일합니다. a : " << *a<< " b : " << *b << std::endl;
	}

	funMax(*a, *b);
	return ;
}

void funMax(int &a, int &b) {
	if (a >= 1 && b >= 1) {
		if (a > b) {
			a = a - b;
			if (a > 0) {
				std::cout << "(1). a>b -> a : " << a << " b : " << b << std::endl;
				if (a == b) {
					std::cout << "GCD : " << a <<std::endl;
					return;
				}
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
