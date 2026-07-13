/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    int maxDiam = 0;

    int diameterOfBinaryTree(TreeNode* root) {

        maxHeight(root);
        return maxDiam;
        
       

    }

    int maxHeight(TreeNode* node) {
        if(node == nullptr) {
            return 0;
        }

        int depth = 1;

        int left = maxHeight(node->left);
        int right = maxHeight(node->right);

        depth = depth + max(left, right);

        maxDiam = max(maxDiam, left + right);

        return depth;
    }
};
