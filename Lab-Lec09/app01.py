import os 
from apikey import API_KEY
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
# hacemos que pueda leerse en nuestro programa
os.environ['OPENAI_API_KEY']= API_KEY

# Construimos la interface
st.title('🦜🔗 Interface con Langchain')
prompt = st.text_input("Ingrese su pregunta aqui ...")

# Conectar la LLM
llm = OpenAI(temperature=0.0) # regula cuan imaginativa o realista puede ser la respuesta
# Mostramos los resultados y verificamos con streamlit
response= llm(prompt)
st.write(response)

#usamos una variable para nuestra plantilla
title_template = PromptTemplate(
    input_variables=['topic'],
    template="Escribe una pregunta de opcion multiple con 3 opciones incorrectas y una correcta sobre el topico {topic}. Señala cual es la respuesta correcta."
    )

#Creamos la cadena
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

#llamamos y mostramos 
if(prompt): 
    response= title_chain.invoke(input=prompt)
    st.write(response["topic"])
    st.write(response["text"])