import operator

class Expression(object):

    @staticmethod
    def eval_infix(infix):
        stack = []
        for op in infix:
            if op.isdigit():
                stack.append(int(op))
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
                '%' : operator.mod,
                '^' : operator.xor}[op]

    @staticmethod
    def __eval_binary_op(op1, op, op2):
        return Expression.__get_operator(op)(op1, op2)

print Expression.eval_infix(['2','3','+','4','-'])