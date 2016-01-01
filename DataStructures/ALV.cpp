#include <iostream>
using namespace std;

typedef struct node{
  int val;
  struct node *left;
  struct node *right;
  int ht;
}node;

node * insertSimple(node *root, int val);
int height(node *root);
node * insert(node *root, int val);

int main()
{
  return 0;
}

node * insert(node *root, int val){
    root = insertBST(root,val);
    balance(root);
}

int height(node *root){
    if(root == 0){
        return 0;
    }
    int ans = max(height(root->left),height(node->right))+1;
    return ans;
}

int balanceFactor(node *root){
    if(root==0){
        return 0;
    }
    int left = height(root->left);
    int right = height(root->right);

    return (left-right);
}

node * balance(node *root){
    int factor = balanceFactor(root);
    if (factor > 1) {
        if(balanceFactor(root->left) > 0){
            //single Left Rotate
        }else{
            //Double Left Rotate
        }
    }else if(factor < -1){
        if(balanceFactor(root->right) < 0){
            //single right rotate
        }else{
            //double right rotate
        }
    }
}



node * ll_rotate(node *root){
    node *temp = root->left;
    root->left = temp->right;
    temp->right = root;
    return temp;
}


node * lr_rotate(node *root){
    node *leftChild = root->left;
    root->left = rr_rotate(leftChild);
    return ll_rotate(root);
}


node * rr_rotate(node *root){
    node *rightChild = root->right;
    root->right = rightChild->left;
    rightChild->left = root;
    return rightChild;
}

node * rl_rotate(node *root){
    node *rightChild = root->right;
    root->right = ll_rotate(rightChild);
    return rr_rotate(root);
}



node * insertBST(node *root, int val){
    if(root == 0){
        node *newNode = new node;
        newNode->val = val;
        root = newNode;
    }else if(val < root->val){
        root = insertBST(root->left, val);
    }else{
        root = insertBST(root->right, val);
    }

    root->height = height(refNode);
    return root;
}
