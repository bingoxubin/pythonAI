import matplotlib.pyplot as plt

# 1.创建画布
plt.figure(figsize=(20,8),dpi=100)

# 2.绘制图像
x = [1,2,3]
y = [4,5,6]
plt.plot(x,y)

# 3.显示图像
plt.show()