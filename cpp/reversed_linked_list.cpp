#include <iostream>


struct ListNode{
    int data;
    ListNode *next;
    ListNode(int val){
        data = val;
        next = nullptr;
    }
};

class Solution{
private:
    ListNode *head;
public:
    Solution(): head(nullptr) {}
    void insert(int x){
        ListNode *new_node = new ListNode(x);
        if (head == nullptr){
            head = new_node;
        }
        else{
            ListNode *temp = head;
            while (temp->next != nullptr){
                temp = temp->next;
            }
            temp->next = new_node;
        }

    }
    void display(){
        ListNode *temp = head;
        while (temp != nullptr){
           std::cout << temp->data  << "";
           temp = temp->next; 
        }
        std::cout << std::endl;

    }

    
    ListNode *reverseList(ListNode* head){
        ListNode *prev = nullptr;
        ListNode *current = head;

        while (current != nullptr){
            ListNode *new_Node = current->next;
            current->next = prev;

            prev = current;
            current = new_Node;
        }
        return prev;
    }

    void reverse(){
        head = reverseList(head);
    }
};


int main() {
    Solution s;
    s.insert(10);
    s.insert(20);
    s.insert(30);
    s.display();
    s.reverse();
    s.display();


}