# basic 4/4
d1 >> play("x-o-")

# basic 4/4 with hh lead
d1 >> play("x-o[--]")

# use curlies to introduce variety at random
d1 >> play("x-o{-o[--]*}")

# swoopy
d2 >> play("x-o-", rate=[1,2,0.5,-1])

# simple high hat
d1 >> play("tt(-[---]-)t")