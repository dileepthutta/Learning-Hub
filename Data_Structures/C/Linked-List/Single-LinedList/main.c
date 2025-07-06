#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *link;
};
struct node *root=NULL;
void insert(){
    struct node *temp;
    temp = (struct node*)malloc(sizeof(struct node));
    printf("Enter node Data : ");
    scanf("%d", &temp->data);
    temp->link = NULL;

    if (root == NULL) {
        root = temp;
    }
    else {
        struct node *ptr = root;
        while (ptr->link != NULL) {
            ptr = ptr->link;
        }
        ptr->link = temp;
    }
}

void display(){
    struct node *temp = root;
    if (root == NULL) {
        printf("List is Empty!\n");
    }
    else {
        while (temp != NULL) {
            printf("%d -> ", temp->data);
            temp = temp->link;
        }
        printf("NULL\n");
    }
}
int length(){
    int len = 0;
    struct node *temp = root;
    if(root ==NULL){
        return len;
    }
    else{
        while(temp!=NULL){
            len+=1;
            temp = temp -> link;
        }
    }
    return len;
}
void delete(){
    struct node *temp=root;
    if(root ==  NULL){
        printf("List is Empty.");
    }
    else{
        printf("%d Deleted Successfully !",temp->data);
        temp = temp->link;
        root = temp;
    }
}
void insert_at_begin(){
    struct node *temp, *ptr = root;
    temp = (struct node*)malloc(sizeof(struct node));
    printf("Enter Node data :");
    scanf("%d",&temp->data);
    temp->link = NULL;
    if(root == NULL){
        root = temp;
    }
    else{
        temp->link = ptr;
        root = temp;
    }
}
void insert_at_spec() {
    struct node *temp, *temp1, *ptr;
    int loc, len, i = 1;

    printf("Enter the location: ");
    scanf("%d", &loc);

    len = length(); // Assume this returns number of nodes

    if (loc < 1 || loc > len + 1) {
        printf("Invalid Location!\n");
        printf("Current list has %d nodes.\n", len);
        return;
    }

    temp = (struct node*) malloc(sizeof(struct node));
    printf("Enter Node data: ");
    scanf("%d", &temp->data);
    temp->link = NULL;

    // Insert at the beginning
    if (loc == 1) {
        temp->link = root;
        root = temp;
    }
    else {
        temp1 = root;
        while (i < loc - 1) {
            temp1 = temp1->link;
            i++;
        }
        temp->link = temp1->link;
        temp1->link = temp;
    }
}
void delete_at_spec() {
    struct node *temp, *ptr;
    int loc, len, i = 1;

    printf("Enter the location to delete: ");
    scanf("%d", &loc);

    len = length(); // Assumes a function that returns number of nodes

    if (loc < 1 || loc > len) {
        printf("Invalid location! Current list has %d nodes.\n", len);
        return;
    }

    // Delete the first node
    if (loc == 1) {
        temp = root;
        root = root->link;
        free(temp);
    } else {
        temp = root;
        while (i < loc - 1) {
            temp = temp->link;
            i++;
        }
        ptr = temp->link;            // Node to be deleted
        temp->link = ptr->link;      // Bypass the deleted node
        free(ptr);
    }

    printf("Node at location %d deleted successfully.\n", loc);
}

void delete_end() {
    struct node *temp = root, *ptr;

    if (root == NULL) {
        printf("List is Empty!\n");
    } else if (root->link == NULL) {
        free(root);
        root = NULL;
    } else {
        while (temp->link != NULL) {
            ptr = temp;
            temp = temp->link;
        }
        ptr->link = NULL;
        free(temp);
    }
}


int main(){
    int n,len;
    while(1){
        printf("\nEnter option\n1)Insert\n2)Insert at Begin\n3)Length\n4)Delete\n5)display\n6)Delete at end\n7)Insert at specific\n8)Delete at sepcific\n9)Exit");
        scanf("%d",&n);
        switch(n){
        case 1:
            insert();
            break;
        case 2:
            insert_at_begin();
            break;
        case 3:
            len = length();
            printf("Length of List : %d\n",len);
            break;
        case 4:
            delete();
            break;
        case 5:
            display();
            break;
        case 6:
            delete_end();
            break;
        case 7:
            insert_at_spec();
            break;
        case 8:
            delete_at_spec();
            break;
        case 9:
            exit(0);
        default:
            printf("IN-valid Input\n");
        }
    }
    return 0;
}
