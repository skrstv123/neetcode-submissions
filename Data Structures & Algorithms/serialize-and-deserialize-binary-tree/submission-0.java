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

public class Codec {

    private int deserIndex = 0;

    private String serhelp(TreeNode root) {
        if (root == null) {
            return "null";
        }
        return String.format("%d,%s,%s", root.val, this.serhelp(root.left), this.serhelp(root.right));
    }

    private TreeNode deserhelp(String[] arr) {
        
        if (deserIndex == arr.length) {
            return null;
        }
        String vals = arr[deserIndex];
        deserIndex++;

        if ("null".equals(vals)) {
            return null;
        }
        int val = Integer.parseInt(vals);
        TreeNode node = new TreeNode(val);
        node.left = this.deserhelp(arr);
        node.right = this.deserhelp(arr);
        return node;
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        final String ser = this.serhelp(root);
        System.out.println(ser);
        return ser;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String arr[] = data.split(",");

        return this.deserhelp(arr);
    }
}
