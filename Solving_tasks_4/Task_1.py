# Вычислить число Pi c заданной точностью d

import math

d = input ("С какой точностью определить число Пи? -- ")

num = int (len (d.split(".")[1]))
print (round (math.pi, num))