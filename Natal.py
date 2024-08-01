import time

def get_total_seconds_in_year(year):
    if year % 4 == 0:  # Se for um ano bissexto
        return 31622400  # 366 dias * 24 horas * 60 minutos * 60 segundos
    else:
        return 31536000  # 365 dias * 24 horas * 60 minutos * 60 segundos
import time

def get_time_until(target_time):
    '''Calculate the time until a target time, given in seconds since the epoch, and return a tuple of (days, hours, minutes, seconds).'''
    current_time = time.time()
    time_until = target_time - current_time
    # Calculating days, hours, minutes, seconds
    min, sec = divmod(time_until, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    month, day = divmod(day, 30)  # note this gives an approximate month number, as not all months have 30 days
    return (int(month), int(day), int(hour), int(min))

def print_results():
    '''Calculate the time until New Year and Christmas Eve, and print the results.'''
    # Defining the target times (New Year and Christmas Eve)
    next_year = time.gmtime().tm_year + 1
    new_year = time.mktime((next_year, 1, 1, 0, 0, 0, 0, 0, 0))
    christmas_eve = time.mktime((next_year, 12, 24, 0, 0, 0, 0, 0, 0))
    # Calculating the time until each event
    time_until_new_year = get_time_until(new_year)
    time_until_christmas_eve = get_time_until(christmas_eve)
    # Printing the results
    print(f"Faltam {time_until_new_year[0]} mês(es), {time_until_new_year[1]} dia(s), {time_until_new_year[2]} hora(s) e {time_until_new_year[3]} minuto(s) para o Ano Novo.")
    print(f"Faltam {time_until_christmas_eve[0]} mês(es), {time_until_christmas_eve[1]} dia(s), {time_until_christmas_eve[2]} hora(s) e {time_until_christmas_eve[3]} minuto(s) para a véspera de Natal.")

print_results()
def calculate_seconds_until_new_year(current_time):
    '''Calcule o número de segundos até o próximo Ano Novo.'''
    new_year = time.mktime((2024, 1, 1, 0, 0, 0, 0, 0, 0))
    return new_year - current_time

def calculate_percentage_of_year_passed(current_time):
    '''Calcule a porcentagem do ano atual que já passou.'''
    # Recuperando o início do ano
    current_year = time.gmtime().tm_year
    start_of_year = time.mktime((current_year, 1, 1, 0, 0, 0, 0, 0, 0))
    # Total de segundos que se passaram desde o início do ano
    seconds_passed = current_time - start_of_year
    # Obtendo o total de segundos no ano corrente
    total_seconds = get_total_seconds_in_year(current_year)
    # Calculando a porcentagem do ano que já passou
    return (seconds_passed / total_seconds) * 100

def print_results():
    '''Get current time, calculate seconds until New Year and percentage of the year that has passed, and print the results.'''
    current_time = time.time()
    seconds_until_new_year = calculate_seconds_until_new_year(current_time)
    percentage = calculate_percentage_of_year_passed(current_time)
    print(f"Faltam {seconds_until_new_year:.0f} segundos para o Ano Novo, {percentage:.2f}% do ano já passou.")

print_results()