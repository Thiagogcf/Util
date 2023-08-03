import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import time

# Definindo os intervalos de tempo
inicio = datetime.now().timestamp()
inicioexpediente = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 7, 33, 0).timestamp()
iniciotarde = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12, 50, 0).timestamp()
iniciohora = datetime.now().time()

# Tempos finais iniciais
final_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17, 12, 0)
final2_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 11, 52, 0)

final = final_time.timestamp()
final2 = final2_time.timestamp()

# Criar uma nova janela tkinter
window = tk.Tk()
window.title("Rastreador de Tempo")
window.geometry('400x300')  # Definir o tamanho da janela

# Estilo da janela
style = ttk.Style()
style.configure("TButton",
                font=('Helvetica', 12),
                borderwidth='4')
style.configure("TLabel",
                font=('Helvetica', 12),
                borderwidth='4')
style.configure("TEntry",
                font=('Helvetica', 12),
                borderwidth='4')

# Adicionar campos de entrada para editar os valores de final e final2
final_label = ttk.Label(window, text="Final (HH:MM:SS):")
final_label.pack()
final_entry = ttk.Entry(window)
final_entry.pack()
final_entry.insert(0, final_time.strftime("%H:%M:%S"))

final2_label = ttk.Label(window, text="Final2 (HH:MM:SS):")
final2_label.pack()
final2_entry = ttk.Entry(window)
final2_entry.pack()
final2_entry.insert(0, final2_time.strftime("%H:%M:%S"))

# Adicionar um rótulo para exibir o tempo restante
time_label = ttk.Label(window, text="")
time_label.pack()

# Adicionar um rótulo para exibir o tempo restante até 23/08/2023
time2_label = ttk.Label(window, text="")
time2_label.pack()

# Adicionar um rótulo para exibir o tempo de início
start_time_label = ttk.Label(window, text="")
start_time_label.pack()

# Adicionar uma tela para exibir a barra de progresso gradiente
canvas = tk.Canvas(window, width=300, height=20)
canvas.pack()

# Adicionar uma tela para exibir a barra de progresso gradiente (para o período de 03/08/2023 até 23/08/2023)
canvas2 = tk.Canvas(window, width=300, height=20)
canvas2.pack()

# Adicionar um rótulo para exibir a porcentagem de progresso
percentage_label = ttk.Label(window, text="")
percentage_label.pack()

def interpolate_color(min_color, max_color, progress):
    return [int(min_c + (max_c - min_c) * progress) for min_c, max_c in zip(min_color, max_color)]


def update_progress_bar(canvas, progress):
    # Limpar a tela
    canvas.delete("all")

    # Desenhar a silhueta da barra de progresso
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), outline='#000')

    # Definir as cores de início (vermelho) e fim (azul)
    min_color = (255, 0, 0)  # RGB para vermelho
    max_color = (0, 0, 255)  # RGB para azul

    # Calcular o número de retângulos a serem desenhados (diminuído por desempenho)
    num_rectangles = 50

    for i in range(num_rectangles):
        # Calcular a cor deste retângulo
        rgb_color = interpolate_color(min_color, max_color, i / num_rectangles)
        hex_color = '#%02x%02x%02x' % tuple(rgb_color)

        # Calcular a posição deste retângulo
        x1 = i * (canvas.winfo_width() / num_rectangles)
        x2 = x1 + (canvas.winfo_width() / num_rectangles)

        # Só desenhar o retângulo se estiver dentro do progresso
        if x2 <= progress * canvas.winfo_width():
            canvas.create_rectangle(x1, 0, x2, canvas.winfo_height(), fill=hex_color, width=0)


def reset_initial_time():
    global inicio
    inicio = datetime.now().timestamp()
    start_time_label['text'] = "Início: " + datetime.fromtimestamp(inicio).strftime("%H:%M:%S")


def update():
    # Atualizar os valores finais e finais2
    try:
        final_time_str = final_entry.get()
        final2_time_str = final2_entry.get()
        final_time = datetime.strptime(final_time_str, '%H:%M:%S')
        final2_time = datetime.strptime(final2_time_str, '%H:%M:%S')
        final = final_time.replace(year=datetime.now().year, month=datetime.now().month,
                                   day=datetime.now().day).timestamp()
        final2 = final2_time.replace(year=datetime.now().year, month=datetime.now().month,
                                     day=datetime.now().day).timestamp()
    except ValueError:
        messagebox.showerror("Erro", "Formato de tempo inválido. Por favor, insira o tempo no formato HH:MM:SS.")
        return

    # Atualizar a barra de progresso e os rótulos
    if datetime.now().timestamp() < final:
        if 100 >= (((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)) >= 0:
            progress_value = ((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)
            time_label['text'] = 'Tempo restante: ' + str((datetime.fromtimestamp(final2)) - datetime.now())[:-7]
            percentage_label['text'] = f'Progresso: {progress_value:.2f}%'
            update_progress_bar(canvas, progress_value / 100)
        else:
            progress_value = ((datetime.now().timestamp() - inicio) * 100) / (final - inicio)
            time_label['text'] = 'Tempo restante: ' + str((datetime.fromtimestamp(final)) - datetime.now())[:-7]
            percentage_label['text'] = f'Progresso: {progress_value:.2f}%'
            update_progress_bar(canvas, progress_value / 100)
    else:
        time_label['text'] = "Primeira contagem regressiva concluída!"

    # Cálculo do progresso até 23/08/2023
    start_date = datetime(2023, 8, 3, 7, 45)
    end_date = datetime(2023, 8, 23, 18)
    progress_value = ((datetime.now() - start_date).total_seconds() * 100) / ((end_date - start_date).total_seconds())
    time2_label['text'] = 'Tempo restante até 23/08/2023: ' + str(end_date - datetime.now())[:-7]
    update_progress_bar(canvas2, progress_value / 100)

    # Agendar a próxima atualização
    window.after(100, update)  # Delay em milissegundos


# Adicionar um botão de reset para resetar o tempo inicial
reset_button = ttk.Button(window, text="Resetar Tempo Inicial", command=reset_initial_time)
reset_button.pack()

update()
window.mainloop()
