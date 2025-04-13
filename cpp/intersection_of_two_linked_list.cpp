#include <iostream>
#include <string>

struct Node{

    int data;
    Node *next;
    Node(int val)
    {
        data = val;
        next = nullptr;
    }
};


class LinkedList{
private:
    Node *head;
public:
    LinkedList(): head(nullptr) {}
    
    void insert(int x){
        Node *newnode = new Node(x);
        newnode-> next = head;
        head = newnode;
    }
    int _get_length(Node *head){
        int length = 0;
        while (head!= nullptr){
            length += 1;
            head = head->next;
        }
        return length;

    }

    Node *getintersection(Node *headA, Node *headB) {
        Node *A = headA;
        Node *B = headB;
        int lena = _get_length(A);
        int lenb = _get_length(B);
        
        if (lena > lenb){
            int diff = lena -lenb;
            while (diff --){
                A = A->next;
            }    
        }
        if (lenb >lena){
            int diff = lenb - lena;
            while (diff --){
                B = B->next;
            }
        }
        while (A != nullptr && B != nullptr){
            if (A ==B){
                return A;
            }
            A = A->next;
            B = B->next;
        return 0;
             
        }
    }

    ~LinkedList(){
        Node *temp;
        while (head != nullptr){
            temp = head;
            head = temp->next;
            delete temp;
        }
    }
};