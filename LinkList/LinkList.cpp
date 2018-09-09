/**
 * name: yhw-miracle
 * email: yhw_software@qq.com
 * date: 2018/09/05
 */
#include "iostream"

using namespace std;

typedef int ElementType;

typedef struct LinkNode {
	ElementType data;
	struct LinkNode *next;
} LinkNode, *LinkList;


/**
 * 头插法建立单链表
 */
LinkList CreateLinkListFromHead(LinkList &L) {
	LinkList *s;
	int x;
	L = (LinkList)malloc(sizeof(LinkNode));
	L->next = NULL;
	cin>>x;
	while(x != -1) {
		s->data = x;
		s->next = L->next;
		L->next = s;
		cin>>x;
	}
	return L;
}

/**
 * 尾插法建立单链表
 */
LinkList CreateLinkListFromTail(LinkList &L) {
	LinkList *s, *r;
	int x;
	L = (LinkList)malloc(sizeof(LinkNode));
	r = L;
	cin>>x;
	while(x != -1) {
		s = (LinkList)malloc(sizeof(LinkNode));
		s->data = x;
		r->next = s;
		r = s;
		cin>>x;
	}
	r->next = NULL;
	return L;
}

/**
 * 按序号查找表结点
 */
LinkNode *GetElement(LinkList &L, int i) {
	if(i < 0) {
		return NULL;
	}
	if(i == 0) {
		return L;
	}
	LinkList *p = L->next;
	int j = 1;
	while(p && j <= i) {
		p = p->next;
		j++;
	}
	return p;
}

/**
 * 按值查找表结点
 */
LinkNode *LocateElement(LinkList &L, ElementType x) {
	LinkNode *p = L->next;
	while(p && p->data != x) {
		p = p->next;
	}
	return p;
}

/**
 * 插入结点
 */
bool InsertLinkNode(LinkList &L, ElementType x, int i) {
	LinkNode *p;
	LinkList *s;
	p = GetElement(L, i-1);
	if(p != NULL) {
		s = (LinkList)malloc(sizeof(LinkNode));
		s->data = x;
		s->next = p->next;
		p->next = s;
		return true;
	} else {
		return false;
	}
}

/**
 * 删除结点
 */
bool DeleteLinkLode(LinkList &L, int i) {
	LinkNode *p, *q;
	p = GetElement(L, i-1);
	if(p != NULL) {
		q = p->next;
		p->next = q->next;
		free(q);
		return true;
	} else {
		return false;
	}
}
