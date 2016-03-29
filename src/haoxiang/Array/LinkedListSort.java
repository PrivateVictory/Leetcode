package haoxiang.Array;

/**
 * Created by haoxiang on 16/2/29.
 */

//Definition for singly-linked list.


public class LinkedListSort {
    public  static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode midNode = head;
        ListNode temp = head.next;

        while (temp != null && temp.next != null) {
            temp = temp.next.next;
            midNode = midNode.next;
        }
        ListNode head2 = midNode.next;
        midNode.next = null;
        head = sortList(head);
        head2 = sortList(head2);
        return merge(head, head2);
    }

    public ListNode merge(ListNode head1, ListNode head2) {

        ListNode dummyNode = new ListNode(-1);
        ListNode currNode = dummyNode;
        while (head1 != null || head2 != null) {
            while (head1 != null && head2 != null) {
                if (head1.val <= head2.val) {
                    currNode.next = head1;
                    head1 = head1.next;
                } else {
                    currNode.next = head2;
                    head2 = head2.next;
                }
                currNode = currNode.next;
            }
            while (head1 != null) {
                currNode.next = head1;
                head1 = head1.next;
                currNode = currNode.next;
            }
            while (head2 != null) {
                currNode.next = head2;
                head2 = head2.next;
                currNode = currNode.next;
            }
        }
        return dummyNode.next;
    }
}
