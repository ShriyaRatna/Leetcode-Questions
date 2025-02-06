
// struct TreeNode
// {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class Solution
{
public:
    int maxDepth(TreeNode *root)
    {
        vector<TreeNode *> stack;
        int d = 0;
        TreeNode *temp = root;
        if (temp == NULL)
        {
            return d;
        }
        while (1)
        {
            while (temp != NULL)
            {
                stack.push_back(temp);
                temp = temp->left;
            }
            if (d < stack.size())
            {
                d = stack.size();
            }

            if (stack.at(stack.size() - 1)->right == NULL)
            {
                temp = stack.at(stack.size() - 1);
                stack.pop_back();
            }

            while (stack.size() != 0 && stack.at(stack.size() - 1)->right == temp)
            {
                temp = stack.at(stack.size() - 1);
                stack.pop_back();
            }

            if (stack.size() == 0)
            {
                break;
            }
            temp = stack.at(stack.size() - 1)->right;
        }
        return d;
    }
};