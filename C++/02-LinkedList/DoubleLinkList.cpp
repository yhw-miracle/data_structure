/**
 * name: yhw-miracle
 * email: yhw_software@qq.com
 * date: 2018/09/09
 */
#include "iostream"

typedef int ElementType;

typedef struct DoubleLinkNode
{
	ElementType data;
	struct DoubleLinkNode *prior, *next;
} DoubleLinkNode, *DoubleLinkList;

/**
 * 按序号查找结点
 */
DoubleLinkNode *GetElement(DoubleLinkList DL, int i)
{
	if (i < 0)
	{
		return NULL;
	}
	if (i == 0)
	{
		return DL;
	}
	DoubleLinkNode *p = DL->next;
	int j = 1;
	while (p && j < i)
	{
		p = p->next;
		j++;
	}
	return p;
}

/**
 * 插入结点操作
 */
bool InsertLinkNode(DoubleLinkList &DL, int i)
{
	DoubleLinkNode *p, *s;
	p = GetElement(DL, i - 1);
	if (p != NULL)
	{
		s = (DoubleLinkList)malloc(sizeof(DoubleLinkNode));
		s->next = p->next;
		p->next->prior = s;
		s->prior = p;
		p->next = s;
		return true;
	}
	else
	{
		return false;
	}
}

/**
 * 删除结点操作
 */
bool DeleteLinkNode(DoubleLinkList &DL, int i)
{
	DoubleLinkNode *p, *q;
	p = GetElement(DL, i - 1);
	if (p != NULL)
	{
		q = p->next;
		p->next = q->next;
		q->next->prior = p;
		free(q);
		return true;
	}
	else
	{
		return false;
	}
}