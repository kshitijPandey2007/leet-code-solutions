#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *dummy = malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = NULL;

    struct ListNode *cur = dummy;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int x = l1 ? l1->val : 0;
        int y = l2 ? l2->val : 0;

        int sum = x + y + carry;
        carry = sum / 10;

        struct ListNode *n = malloc(sizeof(struct ListNode));
        n->val = sum % 10;
        n->next = NULL;

        cur->next = n;
        cur = n;

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }

    return dummy->next;
}
