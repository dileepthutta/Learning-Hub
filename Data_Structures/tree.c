#include <stdio.h>
#include <stdlib.h>
struct node {
    int data;
    struct node *left, *right;
};

struct node *root = NULL;

void insert(int d) {
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = d;
    temp->left = NULL;
    temp->right = NULL;

    if (root == NULL) {
        root = temp;
    } else {
        struct node *parent = NULL;
        struct node *curr = root;

        while (curr) {
            parent = curr;
            if (temp->data > curr->data) {
                curr = curr->right;
            } else {
                curr = curr->left;
            }
        }

        // Now we know where to insert the new node
        if (temp->data > parent->data) {
            parent->right = temp;
        } else {
            parent->left = temp;
        }
    }
}

void inorder(struct node *root) {
    if (root==NULL) {
            return;
    }   inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);

}
void preorder(struct node *root){
    if (root==NULL){
        return;
     }
        printf("%d ",root->data);
        preorder(root->left);
        preorder(root->right);
}
void postorder(struct node *root){
    if(root==NULL){
        return;
    }
        preorder(root->left);
        preorder(root->right);
        printf("%d ",root->data);
}
int main() {
    insert(50);
    insert(2);
    insert(59);
    insert(49);
    insert(60);
    insert(10);
    insert(70);
    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");
    printf("Preorder treversal: ");
    preorder(root);
    printf("\n");
    printf("Postorder traversal: ");
    postorder(root);
    printf("\n");
    return 0;
}
