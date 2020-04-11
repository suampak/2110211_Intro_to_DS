import operator

class Expression(object):
    out_priority = {'+' : 3,
                    '-' : 3,
                    '*' : 5,
                    '/' : 5,
                    '^' : 8,
                    '(' : 9,
                    ')' : 1}
    in_priority = {'+' : 3,
                   '-' : 3,
                   '*' : 5,
                   '/' : 5,
                   '^' : 7,
                   '(' : 0}    

    def __init__(self, infix):
        self.postfix = Expression.__convert2postfix([ch for ch in infix])

    def eval(self, num=1):
        return Expression.__eval_postfix(self.postfix, num)

    @staticmethod
    def __convert2postfix(infix):
        postfix = []
        stack = []
        for op in infix:
            if Expression.out_priority.get(op) is None:
                postfix.append(op)
            else:
                while len(stack) > 0 and Expression.in_priority[stack[-1]] >= Expression.out_priority[op]:
                    postfix.append(stack.pop())
                if op == ')':
                    stack.pop()
                else:
                    stack.append(op)
        while len(stack) > 0:
            postfix.append(stack.pop())
        return postfix
            
    @staticmethod
    def __eval_postfix(postfix, num):
        stack = []
        for op in postfix:
            if Expression.out_priority.get(op) is None:
                stack.append(int(op) if op.isdigit() else num)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(Expression.__eval_binary_op(op1, op, op2))
        return stack.pop()

    @staticmethod
    def __get_operator(op):
        return {'+' : operator.add,
                '-' : operator.sub,
                '*' : operator.mul,
                '/' : operator.div,
                '^' : operator.pow}[op]

    @staticmethod
    def __eval_binary_op(op1, op, op2):
        return Expression.__get_operator(op)(op1, op2)

if __name__ == '__main__':
    e = Expression('2*(3+4)')
    assert e.eval() == 14