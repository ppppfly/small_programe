# coding=utf-8

names = [u'建业', u'受恩', u'辉鉴', u'唯民', u'恩召', u'青显', u'孝军']

group_set = set([])

for a in names:
    for b in names:
        for c in names:
            set_obj = set([a, b, c])
            if len(set_obj) == 3:
                group_set.add(tuple(set_obj))

# 有两个人一样，就要换
f_set = list(group_set)
to_rm = []
for g in group_set:

    if g not in to_rm:

        e1, e2 = list(g)[:2]
        for g2 in group_set:
            if not g == g2 and g2 not in to_rm:
                if e1 in g2 and e2 in g2:
                    to_rm.append(g2)

final_3_groups = [n for n in f_set if n not in to_rm]

for s in final_3_groups:
    l = list(s)
    n = [n for n in names if n not in l]
    print l[0], l[1], l[2], n[0], n[1], n[2], n[3]



