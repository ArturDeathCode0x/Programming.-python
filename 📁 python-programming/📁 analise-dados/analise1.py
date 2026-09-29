import time  as ti
import pandas as pd
import openpyxl

dados ={
"nome" :["ana" , "bruno" ,"carlos"],
"idade" :[25,47,32],
"salario" :[5000,3000,3999]
}


df = pd.DataFrame(dados)
df = df.drop("salario" , axis=1)
df
#fitro_maio_de_30 = df['idade'] > 30
#df[fitro_maio_de_30]
#fitro_salario_maio_500 = df['salario' > 5000]
#f[fitro_salario_maio_500 > 5000]
#df.info()
