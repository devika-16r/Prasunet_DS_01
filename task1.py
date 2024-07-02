import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Age': [10, 20, 30, 40, 50, 60, 70, 80, 90],
    'Male': [5, 20, 30, 25, 15, 10, 5, 2, 1],
    'Female': [4, 18, 28, 22, 14, 9, 4, 3, 1]
}


df = pd.DataFrame(data)
sns.set_style("whitegrid")
figure, axis = plt.subplots(figsize=(10, 6))
width = 0.35
index = df['Age']

#creating_bars
bar1 = axis.bar(index - width/2, df['Male'], width, label='Male', color=sns.color_palette("pastel")[0])
bar2 = axis.bar(index + width/2, df['Female'], width, label='Female', color=sns.color_palette("pastel")[1])
for bar in bar1 + bar2:
    height = bar.get_height()
    axis.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

#customizing
axis.set_xlabel('Age', fontsize=14, fontweight='bold')
axis.set_ylabel('Population', fontsize=14, fontweight='bold')
axis.set_title('Gender Distribution Among Ages in Population', fontsize=16, fontweight='bold')


axis.tick_params(axis='both', which='major', labelsize=12)
axis.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
axis.xaxis.grid(False)
axis.legend()
plt.tight_layout()
plt.show()




