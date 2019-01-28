import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
	
        samples = np.random.choice(sample, replace = True, size = [iterations, len(sample)])
        data_mean = sample.mean()
        #print(data_mean)
        values = []
        for s in samples:
            smp = sample_size(s)
            values.append(smp)
        bstp = np.array(values)
        lower, upper = np.percentile(bstp, [2.5, 97.5])  
        
        return data_mean, lower, upper

if __name__ == "__main__":
	
        df = pd.read_csv('./vehicles.csv')
        print(df.columns)
        
        #data = df.values.T[0]
        data = df.values[0]
        boots = []
        for i in range(1, 50, 1):
               boot = boostrap(data, np.mean, i)
               boots.append([i, boot[0], "mean"])
               boots.append([i, boot[1], "lower"])
               boots.append([i, boot[2], "upper"])
        
        df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
        sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")
             
    
        sns_plot.axes[0, 0].set_ylim(0,)
        sns_plot.axes[0, 0].set_xlim(0,)

        sns_plot.savefig("bootstrap2_currfleet_confidence.png", bbox_inches='tight')
        sns_plot.savefig("bootstrap2_currfleet_confidence.pdf", bbox_inches='tight')

        #print("Mean: %f", (np.mean(data))
        #print ("Var: %f")%(np.var(data))


if __name__ == "__main__":
	
        df = pd.read_csv('./vehicles.csv')
        #print(df.columns)
        
        #data = df.values.T[0]
        data = df.values[1]
        boots = []
        for i in range(1, 50, 1):
               boot = boostrap(data, np.mean, i)
               boots.append([i, boot[0], "mean"])
               boots.append([i, boot[1], "lower"])
               boots.append([i, boot[2], "upper"])
        
        df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
        sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")
             
    
        sns_plot.axes[0, 0].set_ylim(0,)
        sns_plot.axes[0, 0].set_xlim(0,)

        sns_plot.savefig("bootstrap2_newfleet_confidence.png", bbox_inches='tight')
        sns_plot.savefig("bootstrap2_newfleet_confidence.pdf", bbox_inches='tight')

        #print("Mean: %f", (np.mean(data))
        #print ("Var: %f")%(np.var(data))


