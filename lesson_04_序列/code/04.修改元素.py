# 创建一个列表
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

# print("修改前：",stus)
# 修改列表中的元素
# 直接通过索引来修改元素
stus[0] = 'sunwukong'
stus[2] = '哈哈'
# 通过del来删除元素
del stus[2] # 删除索引为2的元素

# print('修改后：',stus)

stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

# print("修改前：",stus)

# 通过切片来修改列表
# 在给切片进行赋值时，只能使用序列
# stus[0:2] = ['牛魔王','红孩儿'] #使用新的元素替换旧元素
# stus[0:2] = ['牛魔王','红孩儿','二郎神']
# stus[0:0] = ['牛魔王'] # 向索引为0的位置插入元素
# 当设置了步长时，序列中元素的个数必须和切片中元素的个数一致
# stus[::2] = ['牛魔王','红孩儿','二郎神']

# 通过切片来删除元素
# del stus[0:2]
# del stus[::2]
# stus[1:3] = []

# 注意！注意！注意！Python的切片是左闭右开区间
# stus[0:1]	选取索引 0 的元素 可替换索引 0 的元素
# stus[0:0]	选取索引 0 之前的空隙（空范围）可在索引 0 之前插入新元素
print('修改后：',stus)

# 以上操作，只适用于可变序列
s = 'hello'
# s[1] = 'a' 不可变序列，无法通过索引来修改
# 可以通过 list() 函数将其他的序列转换为list
s = list(s)
print(s)