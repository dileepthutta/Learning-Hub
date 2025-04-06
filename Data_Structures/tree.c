#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left, *right;
};

struct node *root = NULL;

void insert() {
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    printf("Enter node data: ");
    scanf("%d", &temp->data);
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
    if (root == NULL) {
        return;
    }
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

void preorder(struct node *root) {
    if (root == NULL) {
        return;
    }
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

void postorder(struct node *root) {
    if (root == NULL) {
        return;
    }
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

struct node *findMin(struct node *root) {
    while (root && root->left != NULL) {
        root = root->left;
    }
    return root;
}

struct node *delete_node(struct node *root, int data) {
    if (root == NULL) {
        return root; // Node not found
    }

    if (data < root->data) {
        root->left = delete_node(root->left, data);
    } else if (data > root->data) {
        root->right = delete_node(root->right, data);
    } else {
        // Case 1: No Child
        if (root->left == NULL && root->right == NULL) {
            free(root);
            root = NULL;
        }
        // Case 2: One Child
        else if (root->left == NULL) {
            struct node *temp = root;
            root = root->right;
            free(temp);
        } else if (root->right == NULL) {
            struct node *temp = root;
            root = root->left;
            free(temp);
        }
        // Case 3: Two Children
        else {
            struct node *temp = findMin(root->right);
            root->data = temp->data; // Replace data with the minimum value from the right subtree
            root->right = delete_node(root->right, temp->data); // Delete the node containing the minimum value
        }
    }
    return root;
}

struct node *search(struct node *root, int sea) {
    if (root == NULL) {
        return NULL;
    } else if (sea == root->data) {
        return root;
    } else if (sea < root->data) {
        return search(root->left, sea);
    } else {
        return search(root->right, sea);
    }
}

int main() {
    int option, nd, key;
    while (1) {
        printf("1) Insert\n");
        printf("2) Inorder\n");
        printf("3) Preorder\n");
        printf("4) Postorder\n");
        printf("5) Min-value\n");
        printf("6) Delete\n");
        printf("7) Search\n");
        printf("Enter your option: ");
        scanf("%d", &option);

        switch (option) {
            case 1:
                insert();
                break;

            case 2:
                printf("Inorder traversal: ");
                inorder(root);
                printf("\n");
                break;

            case 3:
                printf("Preorder traversal: ");
                preorder(root);
                printf("\n");
                break;

            case 4:
                printf("Postorder traversal: ");
                postorder(root);
                printf("\n");
                break;

            case 5:
                {
                    struct node *minNode = findMin(root);
                    if (minNode != NULL) {
                        printf("Minimum value in the tree: %d\n", minNode->data);
                    } else {
                        printf("The tree is empty.\n");
                    }
                    break;
                }

            case 6:
                if (root == NULL) {
                    printf("Tree is Empty!\n");
                } else {
                    printf("Enter the node data to delete: ");
                    scanf("%d", &nd);
                    struct node *s = search(root, nd);
                    if (s == NULL) {
                        printf("%d not found!\n", nd); // If the node is not found, notify the user
                    } else {
                        root = delete_node(root, nd);
                        printf("%d is deleted!\n", nd); // Confirm the deletion
                    }
                }
                break;

            case 7:
                if (root == NULL) {
                    printf("Tree is empty!\n");
                } else {
                    printf("Enter data to search: ");
                    scanf("%d", &key);
                    struct node *s = search(root, key);
                    if (s != NULL) {
                        printf("%d is found!\n", key);
                    } else {
                        printf("%d not found!\n", key);
                    }
                }
                break;
            case 8:
                exit(0);
                printf("Program terminated successfully.!\n");
            default:
                printf("\nInvalid option!\n");
                break;
        }
    }
    return 0;
}
