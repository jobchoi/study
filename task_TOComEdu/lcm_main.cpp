#include <iostream>
#include <unistd.h>

using namespace std;

bool checkAB(int a,int b);
int myLcm(int a,int b);

int main(){
    // 2개의 변수를 선언 및 정의
    int a(0), b(0);

    cout<<"in put a"<<endl;
    cin>>a;
    cout<<"in put b"<<endl;
    cin>>b;


    if (!checkAB(a,b))
    {
        cout<<"check a : "<<a<<" | check b : "<<b<<endl;
    }
    

    cout <<"Start : "<< myLcm(a,b)<<endl;
    return 0;
}


bool checkAB(int a,int b){
    if (a <= 0 || b <= 0)
    {
        cout<<"두수는 1보다 큰 양수를 입력해야 합니다"<<endl;
        return false;
    } else {
        if(a == b){
            cout<<"서로 다른 두수를 입력해주세요."<<endl;
            return false;
        }
        else
            return true;
    }
}

int myLcm(int a,int b){
    int bufA = a;
    int bufB = b;
    cout << "===== myLcm ===== "<<endl;
    cout << "a : "<<a<<"\tb: "<<b <<endl;

    sleep(1);

    if(bufA > bufB){
        bufB += b;
        if(bufA == bufB){
            cout << "LCM : " << bufA <<endl;
            return bufA;
        } else{
            myLcm(bufA,bufB);
        }
    } else {
        bufA += a;
        if(bufA == bufB){
            cout << "LCM : " << bufA <<endl;
            return bufA;
        } else{
            myLcm(bufA,bufB);
        }
    }
    // if(a > b){
    //     b +=b;
    //     if(a == b){
    //         cout << "LCM : " << a <<endl;
    //         return a;
    //     }else {
    //         myLcm(a,b);
    //     }
    // } else {
    //     a += a;
    //     if(a == b){
    //         cout << "LCM : " << a <<endl;
    //         return a;
    //     } else {
    //         myLcm(a,b);
    //     }
    // }
    return 1;
}