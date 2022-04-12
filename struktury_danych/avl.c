#include "bst.h"

void inorder_avl(struct tree *root, int *index, int *arr);
void inorder_avl_index(struct tree *root, int *arr);
void fill_shuffle(int *arr, int len);
void print_inorder(struct tree *root);
struct tree *bin_avl(struct tree *root, int *arr, int start, int end);
int level(struct tree *root);
int level_r(struct tree *root, int l);

int main()
{
    int start_elements, steps, step_size, tries;
    struct tree *bst = NULL;

    printf("Start elements: ");
    scanf("%d", &start_elements);
    printf("Steps: ");
    scanf("%d", &steps);
    printf("Step size: ");
    scanf("%d", &step_size);
    printf("Tries: ");
    scanf("%d", &tries);

    int end_elements = start_elements + (steps * step_size);
    int arr[end_elements];
    // int bst_levels[steps];
    // int avl_levels[steps];
    FILE *out = fopen("struktury_danych/out.csv", "w");
    fprintf(out, "elements,bst,avl\n");

    for (int i = start_elements; i <= end_elements; i += step_size)
    {
        printf("%d\n", i);
        double bst_level = 0;
        for (int k = 0; k < tries; k++)
        {
            struct tree *bst = NULL;
            fill_shuffle(arr, i);
            for (int j = 0; j < i; j++)
            {
                bst = insert(bst, arr[j]);
            }
            bst_level += level(bst);
            remove_tree(bst);
        }
        bst_level = bst_level / tries;
        struct tree *bst = NULL;
        fill_shuffle(arr, i);
        for (int j = 0; j < i; j++)
        {
            bst = insert(bst, arr[j]);
        }
        // printf("bst: %d\n", level(bst));
        // bst_levels[(i - start_elements) / step_size] = level(bst);
        inorder_avl_index(bst, arr);
        remove_tree(bst);
        bst = NULL;
        bst = bin_avl(bst, arr, 0, i - 1);
        int avl_level = level(bst);
        // avl_levels[(i - start_elements) / step_size] = level(bst);
        // printf("avl: %d\n", level(bst));
        remove_tree(bst);
        fprintf(out, "%d,%lf,%d\n", i, bst_level, avl_level);
    }
    fclose(out);
    system("pause");
    return 0;
}

struct tree *bin_avl(struct tree *root, int *arr, int start, int end)
{
    if (!root)
    {
        if (end - start < 3)
        {
            if (end - start < 0)
            {
                return root;
            }
            else if (end - start == 0)
            {
                root = insert(root, arr[start]);
                return root;
            }
            else if (end - start == 1)
            {
                root = insert(root, arr[start]);
                root->right = insert(root->right, arr[end]);
                return root;
            }
            else
            {
                root = insert(root, arr[start + 1]);
                root->left = insert(root->left, arr[start]);
                root->right = insert(root->right, arr[end]);
                return root;
            }
        }
        int r = (start + end) / 2;
        root = insert(root, arr[r]);
        root->left = bin_avl(root->left, arr, start, r - 1);
        root->right = bin_avl(root->right, arr, r + 1, end);
        return root;
    }
    else
    {
        printf("ERROR");
        return root;
    }
}

int level_r(struct tree *root, int l)
{
    if (root)
    {
        /*for (int i = 0; i < l; i++)
        {
            printf("\t");
        }*/
        // printf("%d\n", root->info);
        int a = level_r(root->left, l + 1);
        int b = level_r(root->right, l + 1);
        return a > b ? a : b;
    }
    else
    {
        return l;
    }
}

int level(struct tree *root)
{
    return level_r(root, 0);
}

void inorder_avl(struct tree *root, int *index, int *arr)
{
    if (root != NULL)
    {
        inorder_avl(root->left, index, arr);
        arr[*index] = root->info;
        (*index)++;
        inorder_avl(root->right, index, arr);
    }
    return;
}

void inorder_avl_index(struct tree *root, int *arr)
{
    int index = 0;
    inorder_avl(root, &index, arr);
}

void fill_shuffle(int *arr, int len)
{
    for (int i = 0; i < len; i++)
    {
        arr[i] = i;
    }
    for (int i = len; i > 0; i--)
    {
        int pos = (rand() * RAND_MAX + rand()) % len;
        int temp = arr[pos];
        arr[pos] = arr[len - 1];
        arr[len - 1] = temp;
    }
}

/*void print_inorder(struct tree *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        printf(" %d", root->info);
        inorder(root->right);
    }
    printf("\n");
    return;
}*/