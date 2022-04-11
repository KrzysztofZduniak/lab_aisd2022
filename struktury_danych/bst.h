#include <stdio.h>
#include <time.h>
#include <stdlib.h>

struct tree
{
    int info;
    struct tree *left;
    struct tree *right;
};


int search(struct tree *root, int elem)
{
    if(root != NULL) 
    {
		if (root->info == elem)
        {
            return 1;
        }
        if (root->info < elem)
        {
            return search(root->left, elem);
        }
        else
        {
            return search(root->right, elem);
        }
	}
	return 0;
}

void remove_tree(struct tree *root)
{
    if (root == NULL)
    {
        return;
    }
    remove_tree(root->left);
    remove_tree(root->right);
    free(root);
    return;
}

struct tree *insert(struct tree *root, int x) 
{
	if(!root) 
    {
		root=(struct tree*)malloc(sizeof(struct tree));
		root->info = x;
		root->left = NULL;
		root->right = NULL;
		return(root);
	}
	if(root->info > x)
	     root->left = insert(root->left,x); 
    else 
    {
		if(root->info < x)
			root->right = insert(root->right,x);
	}
	return(root);
}