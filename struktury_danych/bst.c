#include "algo/bst.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
  FILE *out_f = fopen("wyniki/bst.time", "w");
  FILE *in_f = fopen("data", "r");
  int n;
  while (fscanf(in_f, "%d ", &n) != EOF) {
    int *x = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
      int temp;
      fscanf(in_f, "%d", &temp);
      *(x + i) = temp;
    }
    clock_t create_c, search_c, delete_c;

    create_c = clock();
    struct tree *head = NULL;
    for (int i = 0; i < n; i++) {
      head = insert(head, x[i]);
    }
    create_c = clock() - create_c;

    search_c = clock();
    for (int i = 0; i < n; i++) {
      search(head, x[i]);
    }
    search_c = clock() - search_c;

    delete_c = clock();
    remove_tree(head);
    delete_c = clock() - delete_c;

    fprintf(out_f, "%d %.10lf %.10lf %.10lf\n", n,
            ((double)create_c) / CLOCKS_PER_SEC,
            ((double)search_c) / CLOCKS_PER_SEC,
            ((double)delete_c) / CLOCKS_PER_SEC);
    free(x);
  }
  fclose(in_f);
  fclose(out_f);
  return 0;
}
