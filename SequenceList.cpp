/**
 * 注意：该程序中顺序表的位置序号等同于数组下标
 * name: yhw-miracle
 * email: yhw_software@qq.com
 * date: 2018/08/26
 */
#include"iostream"

using namespace std;

#define MaxSize 100

typedef int ElementType;

//顺序表类型定义
typedef struct {
    ElementType data[MaxSize];
    int length;
}SequenceList;

/**
 * 初始化顺序表
 */
SequenceList InitSequenceList(SequenceList &sequenceList) {
    sequenceList.length = 0;   //数据清空
    for(int i=0;i<MaxSize;i++) {
        sequenceList.data[i] = 0;
    }
    return sequenceList;
}

/**
 * 求表长
 */
 int LengthSequenceList(SequenceList sequenceList) {
     return sequenceList.length;
 }

 /**
  * 按值查找
  * 有，返回位置；没有，返回没有
  */
int LocateElement(SequenceList sequenceList, ElementType e) {
    for(int i=0;i<MaxSize;i++) {
        if(sequenceList.data[i] == e) {
            return i;
        }
    }
    return -1;
}

/**
 * 按位查找
 */
ElementType GetElement(SequenceList sequenceList, int i) {
    if(i<0 || i>=sequenceList.length) {
        return -1;   //代表位置序号无效，无此值
    }
    return sequenceList.data[i];
}

/**
 * 插入操作
 */
bool SequenceListInsert(SequenceList &sequenceList, ElementType e, int j) {
    if(j<0 || j>sequenceList.length+1) {
        return false;
    }
    if(sequenceList.length>=MaxSize) {
        return false;
    }
    for(int i=sequenceList.length-1;i>=j;i--) {
        sequenceList.data[i+1] = sequenceList.data[i];
    }
    sequenceList.data[j] = e;
    sequenceList.length ++;
    return true;
}

/**
 * 删除操作
 */
bool SequenceListDelete(SequenceList &sequenceList, int j, ElementType &e) {
    if(j<0 || j>sequenceList.length) {
        return false;
    }
    e = sequenceList.data[j];
    for(int i=j+1;i<sequenceList.length;i++) {
        sequenceList.data[i-1] = sequenceList.data[i];
    }
    sequenceList.length --;
    return true;
}

/**
 * 打印顺序吧
 */
void PrintSequenceList(SequenceList sequenceList) {
    for(int i=0;i<sequenceList.length-1;i++) {
        cout<<sequenceList.data[i]<<",";
    }
    cout<<sequenceList.data[sequenceList.length-1]<<"."<<endl;
}

/**
 * 判断顺序表是否为空
 */
bool EmptySequenceList(SequenceList sequenceList) {
    if(sequenceList.length == 0) {
        return true;
    }
    return false;
}

/**
 * 销毁顺序表，释放空间
 */
void DestorySequenceList(SequenceList &sequenceList) {
    sequenceList.length = 0;
    //free(sequenceList);
}

/*
 * test
 */
int main() {
    SequenceList sequenceList;
    InitSequenceList(sequenceList);
    for(int i=0;i<10;i++) {
        SequenceListInsert(sequenceList, i, i);
    }
    PrintSequenceList(sequenceList);
    cout<<sequenceList.length<<endl;
    int k;
    cout<<SequenceListDelete(sequenceList, 2, k)<<endl;
    cout<<k<<endl;
    PrintSequenceList(sequenceList);
}