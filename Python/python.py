from datetime import timedelta

# Lista de horários fornecidos para soma
horarios = [
    "04:41", "10:21", "17:10", "23:59", "17:28", "38:54", "12:30", "46:40", "13:30", "44:05", "11:30", "39:38", "15:09", "35:59"]

# Somando todos os horários válidos
total_time = timedelta()

for horario in horarios:
    h, m = map(int, horario.split(':'))
    total_time += timedelta(hours=h, minutes=m)

# Exibindo o total acumulado
print(total_time)


dias = 13
horas_adicionais = 19
minutos = 34

# Convertendo tudo para horas
total_horas = dias * 24 + horas_adicionais + (minutos / 60)
print(total_horas)