# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eqwP1b-2e3AE3siXTAjCaR4S7R4ghXoE
"""





#BIENVENIDO A LA CALCULADORA DE INDICE DE MASA CORPORAL
#calculadora de IMC
#cantidad de personas aqui
personas = int(input( "personas: "))

#Aqui verificamos que la cantidad sea mayor a 0 si no, no es necesario solicitar mas informacion
while personas > 0:
    #solicitamos el nombre y se guarda el dato en un input
    a = input("el nombre en letras por favor: ")
     #solicitamos el apeLLIdo y lo guardamos en un input
    b = input("Su apellido paterno en letras por favor: ")
    #solicitamos el apellido materno y se garda el dato en input
    c = input ("Su apellido materno en letras por favor: ")

    #solicitamos la edad que siempre debe ser un numero entero por eso el int()
    d = int(input("Su edad en años por favor: "))
    #como la altura se solicita en metros y no centimetros hay que ponerle punto y por eso es un float()
    e = float(input ("Su altura en metros por favor: "))
    #Decimos que estura (de estatura) es igual a altura (No me diga)
    estatura = e
    #La masa en kilogramos si puede tener decimales
    m = float (input("Su masa en kilogramos por favor :"))
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
    IMC = m / estatura**2
    #Revelamos el IMC
    print("IMC: " + str(IMC) )

    #se realizan las distintas validaciones de datos
    if IMC >= 0 and IMC <= 15.99 :
        print ("Desnutrcion severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Desnutricion moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Desnutricion baja")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Rango Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad baja")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad moderada")
    elif IMC >= 40.00:
        print ("obesidad extrema")

    #Por cada persona a la que le pedimos los datos se resta una
    personas = personas - 1