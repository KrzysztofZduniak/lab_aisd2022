#include "linked_list.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
  FILE *out_f = fopen("linked_list2.time", "w");
  FILE *in_f = fopen("data", "r");
  FILE *log_f = fopen("linked_list.log", "w");
  int n;
  while (fscanf(in_f, "%d ", &n) != EOF) {
    fprintf(log_f, "%d\n", n);
    int *x = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
      int temp;
      fscanf(in_f, "%d", &temp);
      *(x + i) = temp;
    }
    // for (int i = 0; i < n; i++) {
    //   printf("%d\n", x[i]);
    // }

    clock_t create_c, search_c, delete_c;
    // double create_t, search_t, delete_t;
    // int x[] = {10, 2, 9, 18, 7, 5, 6, 5};
    create_c = clock();
    Node *head = NULL;
    Node *new = NULL;
    for (int i = 0; i < n; i++) {
      new = new_node(x[i]);
      insert(&head, new);
    }
    create_c = clock() - create_c;

    search_c = clock();
    for (int i = 0; i < n; i++) {
      search(head, x[i]);
    }
    search_c = clock() - search_c;

    // print_list(head);

    delete_c = clock();
    delete (&head);
    delete_c = clock() - delete_c;

    fprintf(out_f, "%d %.10lf %.10lf %.10lf\n", n,
            ((float)create_c) / CLOCKS_PER_SEC,
            ((float)search_c) / CLOCKS_PER_SEC,
            ((float)delete_c) / CLOCKS_PER_SEC);
    free(x);
  }
  fclose(log_f);
  fclose(in_f);
  fclose(out_f);
  return 0;
}
