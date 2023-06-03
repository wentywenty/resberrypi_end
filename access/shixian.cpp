#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include "json/json.h"
#include "json/json-forwards.h"
#include "shixian.hpp"
#include <ctime>
using namespace std;
using namespace Json;

void add_user(string str_name,string str_face)
{
    ifstream ifs(access);
    Value root;
    Value new_user;
    ifs >> root;
    ifs.close();
    //time
    time_t now = time(0); // 把 now 转换为字符串形式
    char *dt = ctime(&now);
    new_user[dt]=str_face;
    //root
    root[str_name] = new_user;
    //write
    StyledWriter writer;
    string output = writer.write(root);
    ofstream ofs(access);
    // 写入格式化后带格式的字符串
    ofs << output;
    // 关闭文件
    ofs.close();
}

void add_time(string str_name,string str_face)
{ // 读取 json 文件
    ifstream ifs(access);
    Value root;
    ifs >> root;
    ifs.close();
    // time
    time_t now = time(0); // 把 now 转换为字符串形式
    char *dt = ctime(&now);
    root[str_name][dt]=str_face;
    //write
    StyledWriter writer;
    string output = writer.write(root);
    ofstream ofs(access);
    // 写入格式化后带格式的字符串
    ofs << output;
    // 关闭文件
    ofs.close();
}