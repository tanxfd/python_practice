set_ceshi = {'小明', '小张', '小黄', '小杨'}
set_yanfa = {'小黄', '小李', '小王', '小杨', '小周'}
set_shichang = {'小杨', '小张', '小吴', '小冯', '小周'}

set = set_ceshi.difference(set_yanfa, set_shichang).union(set_yanfa.difference(set_ceshi, set_shichang)).union(
    set_shichang.difference(set_ceshi, set_yanfa))

# 只在一个部门工作的人
print(set)

# 在两个或者两个以上部门的人
set_company = set_ceshi.union(set_yanfa).union(set_shichang)
print(set_company.difference(set))
