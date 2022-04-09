#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Node Node;
struct Node {
  int value;
  Node *next;
};

void print_list(Node *head) {
  Node *current = head;
  while (current != NULL) {
    printf("%d\n", current->value);
    current = current->next;
  }
}

void insert(Node **head_ref, Node *new_node) {
  struct Node *current;
  /* Special case for the head end */
  if (*head_ref == NULL || (*head_ref)->value >= new_node->value) {
    new_node->next = *head_ref;
    *head_ref = new_node;
  } else {
    /* Locate the node before the point of insertion */
    current = *head_ref;
    while (current->next != NULL && current->next->value < new_node->value) {
      current = current->next;
    }
    new_node->next = current->next;
    current->next = new_node;
  }
}

Node *new_node(int value) {
  Node *new_node = (Node *)malloc(sizeof(struct Node));
  new_node->value = value;
  new_node->next = NULL;
  return new_node;
}

int search(Node *head, int value) {
  Node *ptr = head;
  int i = 0;
  if (ptr == NULL) {
    printf("Empty list\n");
    return -1;
  }
  while (ptr != NULL) {
    if (ptr->value == value) {
      printf("FOUND\n");
    }
    i++;
    ptr = ptr->next;
  }
  return i;
}

void delete (Node **head) {
  while ((*head != NULL) && ((*head)->next != NULL)) {
    Node *temp = (*head)->next;
    free(*head);
    *head = temp;
  }
}

int main(int argc, char *argv[]) {
  int x[argc - 1];
  for (int i = 1; i < argc; i++) {
    sscanf(argv[i], "%d", &x[i - 1]);
  }
  FILE *outFile = fopen("linked_list.time", "a");
  time_t start, end;
  double create_time, search_time, delete_time;
  // int x[] = {10, 2, 9, 18, 7, 5, 6, 5};
  time(&start);
  Node *head = NULL;
  Node *new = NULL;
  for (int i = 0; i < 8; i++) {
    new = new_node(x[i]);
    insert(&head, new);
  }
  time(&end);
  create_time = difftime(end, start);

  time(&start);
  for (int i = 0; i < 8; i++) {
    search(head, x[i]);
  }
  time(&end);
  search_time = difftime(end, start);
  // print_list(head);
  time(&start);

  delete (&head);
  time(&end);
  delete_time = difftime(end, start);

  fprintf(outFile, "%lf %lf %lf", create_time, search_time, delete_time);
  fclose(outFile);

  return 0;
}
