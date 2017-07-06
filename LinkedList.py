
#include <string>
#include <sstream>
#include <iostream>
#include <stdexcept>

#ifndef LINKED_LIST
#define LINKED_LIST

using std::string;
using std::stringstream;
using std::cout;
using std::endl;

template <typename T>
class LinkedList
public:
  LinkedList(): head(NULL) {
  };
  ~LinkedList() {
    clear();
  };
  void insertHead(T value) {

    if(head == NULL) {
      head = new Node;
      head->value = value;
      head->next = NULL;
    } else if(!find(value)) {
      Node* newHead = new Node;
      newHead->value = value;
      newHead->next = head;
      head = newHead;
    }
  };
  void insertTail(T value) {
    if(head == NULL) {
      insertHead(value);
    } else if(!find(value)) {
      Node* newTail = new Node;
      newTail->value = value;
      newTail->next = NULL;
      Node* buff = head;
      while(buff->next != NULL) {
        buff = buff->next;
      }
      buff->next = newTail;
    }
  };
  void insertAfter(T value, T insertionNode) {
    if (find(insertionNode) && !find(value)) {
      Node* buff = head;
      while (buff->value != insertionNode) {
        buff = buff->next;
      }
      Node* newNode = new Node;
      newNode->value = value;
      newNode->next = buff->next;
      buff->next =newNode;
    }
  };
  void remove(T value) {
    if(find(value)) {
      Node* removed;
      if(value == head->value){
        removed = head;
        head = head->next;
      } else {
        Node* buff = head;
        while(buff->next->value != value) {
          buff = buff->next;
        }
        removed = buff->next;
        buff->next = buff->next->next;
      }
      delete removed;
    }
  };
  void clear() {
    while(head != NULL) {
      remove(head->value);
    }
  };
  T at(int index) {
    if(head == NULL || index < 0 || index > size() - 1) {
      throw std::out_of_range("");
    }
    Node* buff = head;
    for(int i = 0; i < index && (buff->next != NULL); i++) {
      buff = buff->next;
    }
    return buff->value;
  };
  int size() {
    if(head == NULL) {
      return 0;
    }
    int size = 1;
    Node* buff = head;
    while(buff->next != NULL) {
      buff = buff->next;
      size ++;
    }
    return size;
  };
  string toString() {

    if(head == NULL) {
      return "";
    }
    stringstream ss;
    Node* buff = head;
    while(buff->next != NULL) {
      ss << buff->value << " ";
      buff = buff->next;
    }
    ss << buff->value;
    return ss.str();
  };
private:
  bool find(T value) {
    Node* buff = head;
    if(head == NULL) {
      return false;
    }
    if(head->value == value) {
      return true;
    }
    while(buff->next != NULL) {
      if(buff->next->value == value) {
        return true;
      }
      buff = buff->next;
    }
    return false;
  };
  Node* head;
};

#endif
