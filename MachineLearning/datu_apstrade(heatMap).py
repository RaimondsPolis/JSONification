import pandas as pd #failu apstrādei
import matplotlib.pyplot as plt # grafiki
import seaborn as sb #vizualizācija

sb.set_style('whitegrid')
plt.rcParams['figure.figsize']=(15,10)

def heat_map(datne): #korelācijas sūdi
    datu_fails = pd.read_csv(datne).select_dtypes('number')
    sb.heatmap(datu_fails.corr(), annot=True, cmap='magma')
    plt.show()
    return

def distribution(datne, kolonna):
        datu_fails = pd.read_csv(datne)
        sb.histplot(datu_fails[kolonna], color='r')

        plt.show()


auto_imports = "MachineLearning/auto_imports.csv"
auto_simple = "MachineLearning/auto_simple.csv"


heat_map("MachineLearning/auto_imports.csv")#korelācijas grafiks
#distribution(auto_simple, "Car")