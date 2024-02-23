import flet as ft
from models import Produto
from  sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker


connection="sqlite:///app_flet.db"
engine=create_engine(connection,echo=True)
Session=sessionmaker(bind=engine)
Session=Session()



def main(page:ft.Page):
    page.title="App de Cadastro"

    lista_produto=ft.ListView()

    def cadastrar(e):
        try:
            preco=input_text_produto_preco.value
            titulo_produto=input_text_produto.value
            novo_produto=Produto(titulo=titulo_produto,preco=preco)
            Session.add(novo_produto)
            Session.commit()
            lista_produto.controls.append(
                ft.Container(
                    ft.Text(titulo_produto),
                    bgcolor=ft.colors.BLUE_100,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=8
                )
            )
            text_erro.visible=False
            text_sucess.visible=True
        except:
            text_erro.visible=True
            text_sucess.visible=False
        
        page.update()
        ft.AlertDialog(modal=True,title="Produto salvo com sucesso!")
        print("Produto salvo com sucesso!")
    
    text_erro=ft.Container(ft.Text("Erro ao salvar o produto"),visible=False,bgcolor=ft.colors.RED_100,padding=10,alignment=ft.alignment.center)
    text_sucess=ft.Container(ft.Text("Produto  salvo com sucesso"),visible=False,bgcolor=ft.colors.GREEN_100,padding=10,alignment=ft.alignment.center)

    text_titulo=ft.Text("Titulo do produto:")
    input_text_produto=ft.TextField(label="Digite o titulo do produto...",text_align=ft.TextAlign.LEFT)
    text_preco = ft.Text("Preço do produto")
    input_text_produto_preco = ft.TextField(value=0,label="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    button_cadastrar=ft.ElevatedButton("Cadastrar Produto",on_click=cadastrar)



    page.add(
        text_erro,
        text_sucess,
text_titulo,
        input_text_produto,
        text_preco,
        input_text_produto_preco,
        button_cadastrar
    )

    for p in Session.query(Produto).all():
        lista_produto.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLUE_100,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=8
            )
        )
    page.add(
       lista_produto,
    )

ft.app(target=main)