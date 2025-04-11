#include <iostream>
#include <string>


struct Node
{
    int data;
    Node* next;
    Node(int value){
        data = value;
        next = nullptr;

    }
};

class Linkedlist{
private:
    Node* head;
public:
   Linkedlist(): head(nullptr) {}
    
   void insert(int x) {
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
  }

    void display(){
        Node* display = head;
        while (display != nullptr){
            std::cout << display->data << std::endl;
            display = display->next;
        }
        std::cout << "NULL" << std::endl;
    }

    bool hasCycle(Node *head){
        Node *slow = head;
        Node *fast = head;
        while (slow != nullptr && fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast){
                return true;
            }
            return false;

        }

    }

    ~Linkedlist(){
        std::cout << "Destructor is cleaning data" << std::endl;
        Node* temp;
        while (head != nullptr){
            temp = head;
            head = temp->next;
            delete temp;
        }


    }
};


int main(){
    Linkedlist list;
    list.insert(10);
    list.insert(20);
    list.insert(30);
    list.display();

    return 0;

}