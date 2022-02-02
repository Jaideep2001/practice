def check_binary_search_tree_(root):
    return check_bin_sub(root,-1,10001)

def check_bin_sub(root,min_val,max_val):
    if root==None: return True
    
    data=root.data
    if (min_val<data) and (data<max_val):
        return check_bin_sub(root.left,min_val,data) and check_bin_sub(root.right,data,max_val)
    
    else: return False
