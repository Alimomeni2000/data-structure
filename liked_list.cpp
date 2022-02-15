#include <stdlib.h>
#include <iostream>
using namespace std;

struct Node{
    int data;
    struct Node* next;
    struct Node* pervious;
    
};
struct Node* head = NULL;

void insert(int newdata){
    struct Node* newnode = (struct Node*) malloc(sizeof(struct Node));
    newnode->data =  newdata;
    newnode->pervious = NULL;
    newnode->next = head;
    if (head != NULL)
        head->pervious = newnode;
    head = newnode;
    
}
void insertAfter(Node* prev_node, int new_data) 
{
   
    // 1. Check if the given prev_node is NULL
    if (prev_node == NULL) 
    { 
        cout << "The given previous node cannot be NULL"; 
        return; 
    }
   
    // 2. Allocate new node
    Node* new_node = new Node();
   
    // 3. Put in the data
    new_node->data = new_data; 
   
    // 4. Make next of new node as
    // next of prev_node
    new_node->next = prev_node->next; 
   
    // 5. move the next of prev_node
    // as new_node
    prev_node->next = new_node; 
}
 


void deleteNode_by_key(struct Node** head_ref, int key){
  struct Node *temp = *head_ref, *prev;

  if (temp != NULL && temp->data == key) {
  *head_ref = temp->next;
  free(temp);
  return ;
  }
  // Find the key to be deleted
  while (temp != NULL && temp->data != key) {
  prev = temp;
  temp = temp->next;
  }

  // If the key is not present
  if (temp == NULL) return ;

  // Remove the node
  prev->next = temp->next;

  free(temp);
  return;
}

struct Node * deleteAtIndex(struct Node * head, int index){
    struct Node *p = head;
    struct Node *q = head->next;
    for (int i = 0; i < index-1; i++)
    {
        p = p->next;
        q = q->next;
    }
    
    p->next = q->next;
    free(q);
    return head;
}

struct Node * deleteAtLast(struct Node * head){
    struct Node *p = head;
    struct Node *q = head->next;
    while(q->next !=NULL)
    {
        p = p->next;
        q = q->next;
    }
    
    p->next = NULL;
    free(q);
    return head;
}

Node* deleteFirst(struct Node* head1){
   if (head == NULL)
        return NULL;
 
    // Move the head pointer to the next node
    Node* temp = head;
    head = head->next;
 
    delete temp;
 
    return head;
}
 
void display(){
    struct Node* ptr;
    ptr = head;
    while(ptr !=NULL){
        cout<<ptr->data;
        if(ptr->next != NULL)
        cout<<"->";
        ptr = ptr->next;
    }
}
int main (){
     
    insert(3);
   insert(1);
insertAfter(head->next, 8);
   cout<<"add 8: \n";
   display();

   insert(7);

   insert(2);
   insert(9);
    insert(5);
   insert(8);
   insert(12);
   cout<<"\nThe doubly linked list is: \n";
   display();
    deleteNode_by_key(&head,9);

   cout<<"\nThe doubly linked list is key 9: \n";

   display();
    cout<<"\nThe doubly linked list is first: \n";

    deleteFirst(head);  
   display();

    deleteAtIndex(head,3);
    cout<<"\nThe doubly linked list is index 3: \n";
   display();

    deleteAtLast(head);
    cout<<"\nThe doubly linked list is end: \n";

   display();

   return 0;
}
