from tkinter import*


# tela_inicial = Tk()


# tela_inicial.title('Minha primeira janela')
# tela_inicial.geometry('600x400')
# tela_inicial.resizable(False, False)
# tela_inicial.maxsize(1000, 600)
# tela_inicial.state('zoomed')

# tela_inicial.iconbitmap('C:/Users/User/Desktop/gilcelio/2019_html/site/python.ico')

menu = Tk()
menu.title('Exercicio 01')
menu.geometry('600x400')
menu.config(bg = '#0000FF')

texto1 = Label(
               menu, 
               text='Informe a velocidade em km/h',
               font = 'Georgia 20',
               bg = '#0000FF',
               fg = 'white'                              
               )

texto2 = Label(
               menu, 
               text= 'Resultado',
               font = 'Georgia 20',
               bg = '#0000FF',
               fg = 'white'                              
               )

caixa_texto = Entry(menu)
botao = Button(
               menu, 
               text = 'Converter',
               command = 'converter'
               )


texto1.grid(row=0, column=0)
caixa_texto.grid(row=1, column=0)
botao.grid(row= 1, column=1)
texto2.grid(row=2, column=0)




# tela_inicial.mainloop()

menu.mainloop()
