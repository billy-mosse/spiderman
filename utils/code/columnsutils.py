from datetime import datetime

# Función para devolver columna de fecha y hora
def fecha_hora(df):
    '''
    Separa la indormacion de fecha y hora que en todos los df estan juntas como string
    
    Argumentos
    ----------
    
    df: el dataframe de cada año de recorridos de bicis
    '''
    
    # Se splitea la columna en dos: fecha y hora que en todos los df estan juntas como str
    fecha_hora = df['bici_Fecha_hora_retiro'].str.split(' ', expand=True)
    
    # Se almacena en un nuevo df
    fecha_hora.columns = ['Fecha','Hora']
    
    return fecha_hora


# Función para devolver dia de la semana
def obtener_dia_semana(fecha):
    '''
    Devuelve el dia de la semana a partir de la fecha
    
    Argumentos
    ----------
    
    fecha: columna del df, para usarla hay que mapearla porque strptime no toma series 
    '''
    return datetime.strptime(fecha,'%Y-%m-%d').weekday()


# Reemplaza numero de dia por nombre. Se le pasa cualquier de los dataframes
def nombre_dia(df):
    dia = df.replace({0:'lunes', 1:'martes', 2:'miercoles', 3:'jueves', 4:'viernes', 5:'sabado', 6:'domingo'})
    return dia