#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
import requests
import tkinter as tk

janela = tk.Tk()
janela.title("Consulta CEP")
janela.geometry("400x300")
entrada_texto = tk.Entry(janela)
entrada_texto.pack()
texto = tk.Frame(janela)
texto.pack()


def clear_text():
	for widget in texto.winfo_children():
		widget.destroy()
def resposta_botao():
	cep = entrada_texto.get()
	if len(cep) != 8:
		clear_text()
		tk.Label(texto, text="digite o cep no padrão 00000000").pack()
	else:
		resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json").json()
		if "erro" in resposta:
			clear_text()
			tk.Label(texto,text = "CEP não encontrado").pack()
		else:
			clear_text()
			cep = tk.Label(texto, text=f"cep: {resposta['cep']}").pack()
			logr = tk.Label(texto, text=f"logradouro: {resposta['logradouro']}").pack()
			bai = tk.Label(texto,text=f"bairro: {resposta['bairro']}").pack()
			loc = tk.Label(texto,text=f"localidade: {resposta['localidade']}").pack()
			est = tk.Label(texto,text=f"estado: {resposta['estado']}").pack()
tk.Button(janela,text="consultar",command=resposta_botao).pack()
janela.mainloop()
