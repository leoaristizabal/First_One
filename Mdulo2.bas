Attribute VB_Name = "M�dulo2"
Option Explicit
'Semana 1 - Tarea 2. Parte 1

'Declaraci�n de variables de entrada (ambas partes)

Dim perimetro As Single
Dim ancho As Single
Dim ano_nac As Integer
Dim edad As Integer

'Declaracion variables de calculo

Dim largo As Single

'Declaraci�n variables de salida

Dim area_patio As Single


perimetro = InputBox("Introduce el valor del perimetro del patio: ", "Perimetro patio")
ancho = InputBox("Introduce el valor del ancho del patio: ", " Ancho del patio")

'El area de un rect�ngulo viene dada por la multiplicacion de sus lados, al tener el ancho y perimetro debemos despejar quedando:

largo = ancho - perimetro / 2

area_patio = ancho * largo

MsgBox ("El �rea del patio cuyo largo es " & largo & ", es: " & area_patio)


ano_nac = Sheets("Hoja1").Cells(5, 2)

Sheets("Hoja1").Cells(5, 4) = 2020 - ano_nac



