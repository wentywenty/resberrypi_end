#include <iostream>    //读写io c++标准库
#include <fstream>     //读写文件 c++标准库
#include <string>      //字符串类 c++标准库
#include <sstream>     //字符串流 c++标准库
#include "json/json.h" //jsoncpp的头文件
#include "json/json-forwards.h"
#include "shixian.hpp"
#include <ctime>
using namespace std;
using namespace Json;

int main()
{
    ifstream txt_user(log);
    string canshu1, canshu2, canshu3;
    txt_user >> canshu1 >> canshu2 >> canshu3;
    txt_user.close();
    if (canshu1[0]!='1')
    {
        add_time(canshu2, canshu3);
    }
    else
    {
        add_user(canshu2, canshu3);
    }
    
    ofstream ofs(log,ios::ate);
    ofs.close();
    
    return 0;
}
