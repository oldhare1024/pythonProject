def power(exp):  # 幂值
    def exp_of(base):  # 基数值
        return base ** exp  # 幂函数值

    return exp_of


sq = power(2)
cu = power(3)
print(sq(2), sq(3), cu(2), cu(3), sep="\n")
