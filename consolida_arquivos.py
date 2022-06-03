import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as dlg
import pandas as pd
import os
import chardet
from datetime import datetime
from tkinter import messagebox

window = tk.Tk()
bg = ''
window.title('Combina Arquivos v1.0')
window.iconbitmap('icone.ico')
window.geometry('700x183')
window.resizable(False, False)
img_fundo = PhotoImage(file="fundo.png")
lab_fundo = Label(window, image=img_fundo)
lab_fundo.pack()

def selecionar_origem():
    origem = dlg.askdirectory(title="Selecione o local dos arquivos a serem consolidados")
    var_origem.set(origem)
    if origem:
        localfile['text'] = origem

def selecionar_destino():
    destino = dlg.askdirectory(title="Selecione o local onde o consolidado será salvo")
    var_destino.set(destino)
    if destino:
        localdir['text'] = destino

bt_seleciona_file = Button(window, text = 'Selecionar Pasta de Origem', command = selecionar_origem)
bt_seleciona_file.place(width=160, height=30, x=12, y=13)
bt_seleciona_dir= Button(window, text = 'Selecionar Pasta de Destino', command = selecionar_destino)
bt_seleciona_dir.place(width=160, height=30, x=12, y=68)
var_origem = tk.StringVar()
var_destino = tk.StringVar()
localfile = Label(window,text = 'Não selecionado', font=("Calibri Light", 10), background = bg)
localfile.place(width=300, height=30, x=190, y=13)
localdir = Label(window,text = 'Não selecionado', font=("Calibri Light", 10), background = bg)
localdir.place(width=300, height=30, x=190, y=68)
colunasEntry = Entry(window,font=("Calibri", 15), justify=CENTER)
colunasEntry.place(width=470, height=33, x=12, y=140)

def inicio():
    window.update()
    caminho_destino = localdir['text']
    arquivo = '/Compilado_'
    stamp = (datetime.today().strftime('%d%m%Y%H%M%S'))
    final_file_name = (caminho_destino+arquivo+stamp)
    cols_to_delete = colunasEntry.get()
    cols_to_delete = cols_to_delete.split(',')
    rows_to_delete = []
    folder_name = localfile['text']+'/'
    dir = os.listdir(folder_name)
    try:
        def ShapeDataframe(file, cols_to_delete, rows_to_delete):
            df = pd.read_csv(file,compression='zip', sep=';', encoding='utf-8',low_memory=False)
            df_after_deleting_cols = df.drop(cols_to_delete,axis=1)
            final_df = df_after_deleting_cols.drop(labels=rows_to_delete, axis=0)
            return final_df

        def find_encoding(fname):
            r_file = open(fname, 'rb').read()
            result = chardet.detect(r_file)
            charenc = result['encoding']
            return charenc

        file_list = []
        for file in dir:
            file_list.append(file)

        frames = []
        for file in file_list:
            window.update()
            try:
                x = ShapeDataframe(folder_name+file, cols_to_delete, rows_to_delete)
                frames.append(x)
            except:
                my_encoding = find_encoding(folder_name+file)
                df = pd.read_csv(folder_name+file,compression='zip', encoding=my_encoding)
                df_after_deleting_cols = df.drop(cols_to_delete,axis=1)
                final_df = df_after_deleting_cols.drop(labels=rows_to_delete, axis=0)
                frames.append(final_df)
        result = pd.concat(frames, ignore_index=True)
        result.to_csv(final_file_name+'.csv', encoding='utf-8',sep=';', index=False)
        messagebox.showinfo("Tarefa concluída!", f'Os arquivos foram compilados e salvos com as colunas selecionadas! {final_file_name}.csv')
    except KeyError:
        window.update()
        messagebox.showerror('Erro', 'Ocorreu um erro, verifique os arquivos selecionados:\n\nUma ou mais colunas não existem neste arquivo\n\nou\n\nOs formatos dos arquivos desta pasta não correspondem')

bt_compilar= Button(window,text = 'Combinar!', command= inicio)
bt_compilar.place(width=84, height=33, x=490, y=140)

window.mainloop()