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
    
    struct ListNode *cur, *tmp, *p;
    cur = head;
    
    while (cur != NULL) {
        tmp = cur->next;
        while (tmp != NULL && cur->val == tmp->val) {
            p = tmp;
            tmp = tmp->next;
            free(p);
        }
        cur->next = tmp;
        cur = cur->next;
    }
    
    return head;
    }
};