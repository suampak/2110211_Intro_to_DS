import copy

from stack import Expression

class ExpressionTree(Expression):
    class Node(object):
        def __init__(self, op):
            self.val = op
            self.left = None
            self.right = None

    def __init__(self, infix, node = None):
        if node is not None:
            self.__tree = node
        else:
            super(ExpressionTree, self).__init__(infix)
            postfix = []
            for op in self.postfix:
                postfix.append(ExpressionTree.Node(op))

            stack = []
            for op in postfix:
                if Expression.out_priority.get(op.val) is not None:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    op.left = op1
                    op.right = op2
                stack.append(op)
            
            self.__tree = stack.pop()

    def __str__(self):
        return ''.join(ExpressionTree.__convert2infix(self.__tree))

    def eval(self, num=1):
        return ExpressionTree.__eval(self.__tree, num)

    def derivative(self):
        return ExpressionTree([],ExpressionTree.__derivative(self.__tree)) # dummy infix

    @staticmethod
    def __convert2infix(node):
        if node.left is None and node.right is None:
            return [node.val]

        op1 = ExpressionTree.__convert2infix(node.left)
        op2 = ExpressionTree.__convert2infix(node.right)
        return ['(']+op1+[node.val]+op2+[')']

    @staticmethod
    def __eval(node, num):
        if node.left is None and node.right is None:
            return int(node.val) if node.val.isdigit() else num
        
        op1 = ExpressionTree.__eval(node.left, num)
        op2 = ExpressionTree.__eval(node.right, num)
        return Expression._eval_binary_op(op1, node.val, op2)

    @staticmethod
    def __derivative(node):
        if node.left is None and node.right is None:
            if node.val.isdigit():
                return ExpressionTree.Node('0')
            return ExpressionTree.Node('1')

        if node.val == '^':
            ret = ExpressionTree.Node('*')
            ret.left = ExpressionTree.Node(node.right.val)
            ret.right = ExpressionTree.Node('^')
            ret.right.left = ExpressionTree.Node(node.left.val)
            ret.right.right = ExpressionTree.Node(str(int(node.right.val)-1))
            return ret

        # only support '*' and '+' derivative
        if node.val == '+':
            ret = ExpressionTree.Node(node.val)
            ret.left = ExpressionTree.__derivative(node.left)
            ret.right = ExpressionTree.__derivative(node.right)
            return ret

        if node.val == '*':
            ret = ExpressionTree.Node('+')
            ret.left = ExpressionTree.Node('*')
            ret.left.left = copy.deepcopy(node.left)
            ret.left.right = ExpressionTree.__derivative(node.right)
            ret.right = ExpressionTree.Node('*')
            ret.right.left = ExpressionTree.__derivative(node.left)
            ret.right.right = copy.deepcopy(node.right)
            return ret

if __name__ == '__main__':
    e1 = ExpressionTree('2*(3+4)')
    e2 = ExpressionTree('(x^2+2)*x')
    e2diff = e2.derivative() 
    assert e1.eval() == 14
    assert e2diff.eval(1) == 5