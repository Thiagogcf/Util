import time
from datetime import datetime, timedelta
from tkinter import Tk, Label, Entry, Button, StringVar


def atualizar_tempo_restante():
    agora = datetime.now()
    inicio = agora.replace(hour=7, minute=41, second=30, microsecond=0)
    iniciotarde = agora.replace(hour=13, minute=0, second=0, microsecond=0)
    final = agora.replace(hour=17, minute=30, second=0, microsecond=0)
    final2 = datetime.strptime(final2_var.get(), "%H:%M:%S")

    if final2.date() != agora.date():
        final2 = final2.replace(year=agora.year, month=agora.month, day=agora.day)

    if final > agora:
        label_inicio["text"] = f"Início da Hora: {agora.time()}"

        if 100 >= (((agora - inicio) / (final2 - inicio)) * 100) >= 0:
            label_restante["text"] = f"Tempo restante até {final2.time()}: {final2 - agora}"
        else:
            label_restante["text"] = f"Tempo restante até {final.time()}: {final - agora}"

        progresso = (agora - inicio) / (final - inicio) * 100
        progresso_tarde = (agora - iniciotarde) / (final - iniciotarde) * 100
        progresso_expediente = (agora - inicio) / (final - inicio) * 100
        progresso_final2 = (agora - inicio) / (final2 - inicio) * 100
        progresso_expediente_final2 = (agora - inicio) / (final2 - inicio) * 100

        label_progresso["text"] = f"Progresso entre Início e Final: {progresso:.2f}%"
        label_progresso_tarde["text"] = f"Progresso entre Início da Tarde e Final: {progresso_tarde:.2f}%"
        label_progresso_expediente[
            "text"] = f"Progresso entre Início do Expediente e Final: {progresso_expediente:.2f}%"

        if 100 >= (((agora - inicio) / (final2 - inicio)) * 100) >= 0:
            label_progresso_final2["text"] = f"Progresso entre Início e Final2: {progresso_final2:.2f}%"
            label_progresso_expediente_final2[
                "text"] = f"Progresso entre Início do Expediente e Final2: {progresso_expediente_final2:.2f}%"

    janela.after(1000, atualizar_tempo_restante)


janela = Tk()
janela.title("Acompanhamento do Expediente")

label_inicio = Label(janela, text="")
label_inicio.grid(row=0, column=0, padx=5, pady=5)

label_restante = Label(janela, text="")
label_restante.grid(row=1, column=0, padx=5, pady=5)

label_progresso = Label(janela, text="")
label_progresso.grid(row=2, column=0, padx=5, pady=5)

label_progresso_tarde = Label(janela, text="")
label_progresso_tarde.grid(row=3, column=0, padx=5, pady=5)

label_progresso_expediente = Label(janela, text="")
label_progresso_expediente.grid(row=4, column=0, padx=5, pady=5)

label_progresso_final2 = Label(janela, text="")
label_progresso_final2.grid(row=5, column=0, padx=5, pady=5)

label_progresso_expediente_final2 = Label(janela, text="")
label_progresso_expediente_final2.grid(row=6, column=0, padx=5, pady=5)

label_final2 = Label(janela, text="Insira o horário Final2 (formato: HH:MM:SS):")
label_final2.grid(row=7, column=0, padx=5, pady=5)

final2_var = StringVar()
entry_final2 = Entry(janela, textvariable=final2_var)
entry_final2.grid(row=8, column=0, padx=5, pady=5)

button_atualizar = Button(janela, text="Atualizar Final2", command=atualizar_tempo_restante)
button_atualizar.grid(row=9, column=0, padx=5, pady=5)

janela.after(1000, atualizar_tempo_restante)
janela.mainloop()

