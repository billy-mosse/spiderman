import matplotlib.pyplot as plt
import seaborn as sns



def frequency_by_age(df):
	plt.figure(figsize=(20,10))
	plt.subplot(2,2,1)
	viajes15 = df.bici_edad
	viajes15.plot.hist(grid=True, bins=20, rwidth=0.9,
	                   color='#2F9599')
	plt.title('Recorridos')
	plt.suptitle('Distribución de los viajes en bicicleta por edad. CABA', fontsize=15);


def frequency_by_gender(df):
	edad = df.bici_edad
	sexo = df.bici_sexo

	plt.figure(figsize=(15,5))
	plt.hist([[e for e, s in zip(edad, sexo) if s=='MASCULINO'], 
	          [e for e, s in zip(edad, sexo) if s=='FEMENINO']], 
	          color=['#FF847C','#ADD8E6'], bins=20, stacked=True)
	plt.grid(alpha=0.3)
	plt.title('Recorridos según sexo del usuario')
	plt.show();



def users_by_gender(df):

	genderdf = df18.groupby(['bici_sexo'])['bici_edad'].count()
	# Usuarios por sexo
	# Plot 1
	sizes = []
	labels = ['MASCULINO', 'FEMENINO']
	colors = ['#ADD8E6', '#FF847C']
	try:
		sizes = [genderdf["MASCULINO"], genderdf["FEMENINO"]]
	except TypeError:
		sizes = [genderdf["M"], genderdf["F"]]

	explode = (0.09, 0)  

	# Plot 2
	sizes2 = [537252, 178962]

	# Plot 3
	sizes3 = [1402028, 484136]
	explode3 = (0.09, 0)  

	# Plot 4
	sizes4 = [2162906, 807495]
	 
	# Grilla de plots
	plt.figure(figsize=(15,6))

	plt.subplot(1,4,1)
	plt.pie(sizes, explode=explode, labels=None, colors=colors,
	        autopct='%1.1f%%', shadow=True, startangle=140, pctdistance = 0.5)
	 
	plt.legend(labels, loc=(0.22,0.1))
	plt.axis('equal')
	plt.title('Usuarios por sexo \n Recorridos CABA-2015', y=0.8)

	plt.subplot(1,4,2)
	plt.pie(sizes2, explode=explode, labels=None, colors=colors,
	        autopct='%1.1f%%', shadow=True, startangle=140, pctdistance = 0.5)
	plt.legend(labels, loc=(0.22,0.1))
	plt.title('Usuarios por sexo \n Recorridos CABA-2016', y=0.8)
	plt.axis('equal')

	plt.subplot(1,4,3)
	plt.pie(sizes3, explode=explode, labels=None, colors=colors,
	        autopct='%1.1f%%', shadow=True, startangle=140, pctdistance = 0.5)
	plt.legend(labels, loc=(0.22,0.1))
	plt.title('Usuarios por sexo \n Recorridos CABA-2017', y=0.8)
	plt.axis('equal')

	plt.subplot(1,4,4)
	plt.pie(sizes4, explode=explode, labels=None, colors=colors,
	        autopct='%1.1f%%', shadow=True, startangle=140, pctdistance = 0.5)
	plt.legend(labels, loc=(0.22,0.1))
	plt.title('Usuarios por sexo \n Recorridos CABA-2018', y=0.8)
	plt.axis('equal')
	plt.show();