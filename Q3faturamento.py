from datetime import datetime, timedelta
import random

def gerar_dados_faturamento_ano(ano):
    data_inicio = datetime(ano, 1, 1)
    dias_no_ano = 365 if (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)) else 366
    
    faturamentos_com_data = []
    for i in range(dias_no_ano):
        data_atual = data_inicio + timedelta(days=i)
        if data_atual.weekday() in [5, 6]:
            faturamento = 0
        else:
            faturamento = random.randint(0, 5000)
        faturamentos_com_data.append((data_atual, faturamento))
    
    return faturamentos_com_data

def calcular_estatisticas_faturamento(faturamentos_com_data):
    faturamento_total = 0
    dias_com_faturamento = 0
    menor_faturamento = float('inf')
    maior_faturamento = float('-inf')
    dia_menor_faturamento = None
    dia_maior_faturamento = None
    
    for data, faturamento in faturamentos_com_data:
        if faturamento > 0:
            faturamento_total += faturamento
            dias_com_faturamento += 1
            if faturamento < menor_faturamento:
                menor_faturamento = faturamento
                dia_menor_faturamento = data
            if faturamento > maior_faturamento:
                maior_faturamento = faturamento
                dia_maior_faturamento = data
    
    media_anual = (faturamento_total / dias_com_faturamento) if dias_com_faturamento > 0 else 0
    
    dias_acima_da_media = 0
    for data, faturamento in faturamentos_com_data:
        if faturamento > media_anual:
            dias_acima_da_media += 1
    
    return menor_faturamento, dia_menor_faturamento, maior_faturamento, dia_maior_faturamento, dias_acima_da_media, media_anual

faturamentos_com_data = gerar_dados_faturamento_ano(2024)

menor_faturamento, dia_menor_faturamento, maior_faturamento, dia_maior_faturamento, dias_acima_da_media, media_anual = calcular_estatisticas_faturamento(faturamentos_com_data)

print(f"Menor faturamento: {menor_faturamento} ocorreu no dia {dia_menor_faturamento.strftime('%d/%m/%Y')}")
print(f"Maior faturamento: {maior_faturamento} ocorreu no dia {dia_maior_faturamento.strftime('%d/%m/%Y')}")
print(f"Dias com faturamento acima da média anual: {dias_acima_da_media}")
print(f"Média anual de faturamento: {media_anual:.2f}")
