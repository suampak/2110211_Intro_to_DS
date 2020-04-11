from stack import Expression

class ExpressionTree(Expression):
    class Node(object):
        def __init__(self, op):
            self.val = op
            self.left = None
            self.right = None

    def __init__(self, infix):
        super(infix)
        infix = []
        for op in super.infix:
            infix.append(ExpressionTree.Node(op))

        stack = []
        for op in infix:
            if Expression.out_priority.get(op.val) is not None:
                op2 = stack.pop()
                op1 = stack.pop()
                op.left = op1
                op.right = op2
            stack.append(op)
        
        self.__tree = stack.pop()
