#include <iostream>

void funMax(int*, int* );
void getData(int *,int *);

int main(int , char*) {
	int a(0), b(0);
	std::cout << "Start " << std::endl;
	getData(&a,&b);
	return 0;
}

void getData(int *a,int *b) {
//	int getA(0), getB(0);
	std::cout << "a 입력" <<std::endl;
	std::cin >> *a;
	std::cout << "b  입력" << std::endl;

	std::cin >> *b;

	std::cout << "a : " << *a<< " b : " << *b << std::endl;

	funMax(a, b);
	return ;
}

void funMax(int *a, int *b) {
	if (*a >= 1 && *b >= 1) {
		if (*a > *b) {
			*a = *a - *b;
			if (*a > 0) {
				std::cout << "(1). a>b -> a : " << *a << " b : " << *b << std::endl;
				if (*a == *b) {
					std::cout << "최대공약수 : " << *a <<std::endl;

					exit(1);
				}
				funMax(a, b);
			}
		}
		else {
			*b = *b - *a;
			if (*b > 0) {
				std::cout << "(2). b > a -> a : " << *a << " b : " << *b << std::endl;
				if (*a == *b) {
					std::cout << "최대공약수 : " << *a << std::endl;

					exit(1);

				}
				funMax(a, b);

			}

			std::cout << "(3). a : " << *a << " b : " << *b << std::endl;

			funMax(a, b);
		}
	}
	else
	{
		std::cout << "(4(. else  => a : " << *a << " b : " << *b << std::endl;
	}
	exit(1);

}
