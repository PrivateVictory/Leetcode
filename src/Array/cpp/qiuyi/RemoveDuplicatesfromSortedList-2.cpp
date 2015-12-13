/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
    
        struct ListNode *cur, *tmp, *pre, *p;
        cur = head; pre = NULL;
    
        while (cur->next != NULL) {
            tmp = cur->next;
            while (tmp != NULL && cur->val == tmp->val) {
                p = tmp;
                tmp = tmp->next;
                free(p);
            }
        if (tmp != cur->next) {
            free(cur);
            cur = NULL;
            if (tmp == NULL && pre == NULL)
                return NULL;
            if (tmp == NULL && pre != NULL) {
                pre->next = NULL;
                return head;
            }
            if (tmp != NULL && pre != NULL)
                pre->next = tmp;
            if (tmp != NULL && pre == NULL)
                head = tmp;
            cur = tmp;
        } else {
            pre = cur;
            cur = tmp;
        }
    }
    
    return head;
    }
};