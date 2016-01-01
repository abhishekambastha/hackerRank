#include <iostream>
using namespace std;

typedef struct node{
  int val;
  struct node *left;
  struct node *right;
  int ht;
}node;

int main()
{
  return 0;
}

node * insert(node *root, int val){
    node *refNode = insertSimple(root,val);

}

int height(node *root){
    if(root == 0){
        return 0;
    }
    int ans = max(height(root->left),height(node->right))+1;
    return ans;
}

node * insertSimple(node *root, int val){
    node *refNode;
    if(root == 0){
        node *newNode = new node;
        newNode->val = val;
        root = newNode;
        refNode = root;
    }else if(val < node->val){
        if(node->left == 0){
            node *newNode = new node;
            newNode->val = val;
            node->left = newNode;
            refNode = node->left;
        }else{
            refNode = insertSimple(node->left, val);
        }
    }else{
        if(node->right == 0){
            node *newNode = new node;
            newNode->val = val;
            node->right = newNode;
            refNode = node->right;
        }else{
            refNode = insertSimple(node->right, val);
        }
    }

    return refNode;
}
