def non_recur_post(root):
    stack = []
    mark = None
    while (stack or root):
        if root:
            stack.append(root)
            root = root.left
        elif stack[-1].right != mark:
            root = stack[-1].right
            mark = None
        else:
            mark = stack.pop()
            print(mark.val)


def non_recur_pre(root):
    stack = []
    while(root or stack):
        if root:
            print(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right


def non_recur_pre(root):
    stack = []
    while(root or stack):
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val)
            root = root.right



