/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    private int ans = Integer.MIN_VALUE;

    private int dfs(TreeNode root) {
        if (root == null) return 0;
        int ls = Math.max(0, dfs(root.left));
        int rs = Math.max(0, dfs(root.right));

        int cs = root.val + ls + rs;
        if (cs > this.ans) ans = cs;

        return root.val + Math.max(ls, rs);
    }

    public int maxPathSum(TreeNode root) {
        this.dfs(root);
        return ans;
    }
}
