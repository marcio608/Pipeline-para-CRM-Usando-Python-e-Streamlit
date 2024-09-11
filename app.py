import streamlit as st
from datetime  import datetime, time
from contrato import Vendas 
from pydantic import ValidationError
from database import salvar_no_postgres


def main():
    # valores padrões (o que vai aparecer para o usuário antes de preencher)
    st.title("Sistema de CRM e Vendas da ZapFlow - FrontEnd Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor.")
    data = st.date_input("Campo para selecionar a data em que a venda foi realizada.", datetime.now())
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada.", value=time(9,0)) #valor padrão
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda realizada.", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos vendidos.", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção para escolher o produto vendido.", ["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    if st.button("Salvar"):
            
            try:
            
                data_hora = datetime.combine(data, hora)

                venda = Vendas(
                     email = email,
                     data = data_hora,
                     valor = valor,
                     quantidade = quantidade,
                     produto = produto
                )
                st.write(venda)
                salvar_no_postgres(venda)
            except ValidationError as e:
                 st.error(f"Ocorreu um erro: {e}")
                 

            


if __name__ =="__main__":
    main()