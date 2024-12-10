"""
Nombre: Ciclotrón
Fecha Inicio: 20/11/2021
Fecha Final: 25/11/2021
Autor: Oscar Joel Castro Contreras
Descripcion:
Con este programa se puede calcular la energía 
final que se le puede aplicar a una partícula 
que se inyecta a un ciclotrón.

"""
import math
print("""
                                   	CICLOTRÓN
      INSTRUCCIONES:
	 El ciclotrón es un tipo de acelerador de partículas, este programa ayuda a calcular la energía a 
  	 la que se obtiene al acelerar una partícula.
	 El programa te mostrara la fórmula para calcular la energía y te pedirá las variables con las que 
  	 se puede calcular y te pedirá su valor.
      Para colocar un numero con notación científica se coloca de la forma:
							1.56 X 10^-12 = 1.56e-12
      En ves de colocar un [ X 10^-12 ]  se coloca un [ e-12 ] después del numero, igual si el exponente
      es positivo. El progrma tambien te dira que unidades tienes que colocar el valor de cada variable.
      """)

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
     
     print("""
      ╔══════════════════════════════════════╗
      ╠══════════════___MENU___══════════════╣
      ╠══ ► Energia                  » 1 « ══╣
      ╠══ ► Frecuencia ciclotrónica  » 2 « ══╣
      ╠══ ► Velocidad maxima         » 3 « ══╣
      ╠══ ► Radio maxima             » 4 « ══╣
      ╠══ ► Velocidad en N vueltas   » 5 « ══╣
      ╠══ ► Radio en N vueltas       » 6 « ══╣
      ╠══ ► Frecuencia por R y v     » 7 « ══╣
      ╠══ ► Campo magnetico          » 8 « ══╣
      ╚══════════════════════════════════════╝
     """)
     
     o = int(input("\n\t¿Que deseas calcular? »» "))
     
     if o == 1:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Energia                  » 1 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔══════════════════════════╗		╔══════════════════════════╗")
          print("  \t║         Formula1:        ║		║         Formula2:        ║")
          print("  \t╠══════════════════════════╣		╠══════════════════════════╣")
          print("  \t║        R^2 · q^2 · B^2   ║		║                          ║")
          print("  \t║  k =  ────────────────── ║		║      k = 2N · q · ∆V     ║")
          print("  \t║               2m         ║		║                          ║")
          print("  \t╚══════════════════════════╝		╚══════════════════════════╝")
          print("  \t              a)                                 b)           ")
          
          w = str(input("\n\t¿Cual formula deseas utilizar? »» "))
          if w == "a":
               R = float(input("\n\t R ► Radio maximo del ciclotrón (m): "))
               
               q = float(input("\n\t q ► Carga de la particula (C)     : "))
               
               m = float(input("\n\t m ► Masa de la particula (kg)     : "))
               
               B = float(input("\n\t B ► Campo magnetico (T)           : "))
               
               k = ((R**2)*(q**2)*(B**2))/2*m
               
               keV = k/1.602176634e-19
               
               print("\nEnergia (J): ",k)
               print("  Energia (eV): ",keV)
               
          elif w == "b":
               N = float(input("\n\t N  ► Numero de vueltas en el ciclotrón (N): "))
               
               q = float(input("\n\t q  ► Carga de la particula (C)            : "))
               
               V = float(input("\n\t ∆V ► Diferencia de potencial (V)          : "))
               
               k = 2*N*q*V
               
               keV = k/1.602176634e-19
               
               print("\nEnergia (J): ",k)
               print("Energia (eV): ",keV)
               
     elif o == 2:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Frecuencia ciclotrónica  » 2 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔══════════════════════════╗		╔══════════════════════════╗")
          print("  \t║         Formula:         ║		║         Formula:         ║")
          print("  \t╠══════════════════════════╣		╠══════════════════════════╣")
          print("  \t║            q · B         ║		║            2π · m        ║")
          print("  \t║      f =  ────────       ║		║       T = ────────       ║")
          print("  \t║            2π · m        ║		║             q · B        ║")
          print("  \t╚══════════════════════════╝		╚══════════════════════════╝")
          
          q = float(input("\n\t q ► Carga de la particula (C): "))
          
          m = float(input("\n\t m ► Masa de la particula (kg): "))
          
          B = float(input("\n\t B ► Campo magnetico (T)      : "))
          
          f = (q*B)/((2*math.pi)*m)
          
          T = ((2*math.pi)*m)/(q*B)
          
          print("\nf (rev/s): ",f)
          print("T (s): ",T)
     
     elif o == 3:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Velocidad maxima         » 3 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔══════════════════════════╗")
          print("  \t║         Formula:         ║")
          print("  \t╠══════════════════════════╣")
          print("  \t║            R · q · B     ║")
          print("  \t║   v_max = ───────────    ║")
          print("  \t║                m         ║")
          print("  \t╚══════════════════════════╝")
          
          R = float(input("\n\t R ► Radio maximo del ciclotrón (m): "))
          
          q = float(input("\n\t q ► Carga de la particula (c)     : "))

          B = float(input("\n\t B ► Campo magnetico (T)           : "))
          
          m = float(input("\n\t m ► Masa de la particula (kg)     : "))
          
          v =(R*q*B)/m
          
          print("\nv (m/s): ",v)
          
     elif o == 4:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Radio maxima             » 4 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔══════════════════════════╗")
          print("  \t║         Formula:         ║")
          print("  \t╠══════════════════════════╣")
          print("  \t║            m · v_max     ║")
          print("  \t║   R_max = ───────────    ║")
          print("  \t║              q · B       ║")
          print("  \t╚══════════════════════════╝")
          
          m = float(input("\n\t m     ► Masa de la particula (kg)   : "))
          
          v = float(input("\n\t v_max ► velocidad en N vueltas (m/s): "))
          
          q = float(input("\n\t q     ► Carga de la particula (c)   : "))
          
          B = float(input("\n\t B     ► Campo magnetico (T)         : "))
          
          R = (m*v)/(q*B)
          
          print("\nR_max (m): ",R)
            
     elif o == 5:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Velocidad en N vueltas   » 5 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔════════════════════════════════╗")
          print("  \t║            Formula:            ║")
          print("  \t╠════════════════════════════════╣")
          print("  \t║              [ 4N · q · ∆V ]   ║")
          print("  \t║   v_n = sqrt [─────────────]   ║")
          print("  \t║              [      m      ]   ║")
          print("  \t╚════════════════════════════════╝")
          
          N = float(input("\n\t N  ► Numero de vueltas en el ciclotrón (N): "))
          
          q = float(input("\n\t q  ► Carga de la particula (C)            : "))
          
          V = float(input("\n\t ∆V ► Diferencia de potencial (V)          : "))
          
          m = float(input("\n\t m  ► Masa de la particula (kg)            : "))

          v = math.sqrt((4*N*q*V)/m)
          
          print("\nv_n (m/s): ",v)
     
     elif o == 6:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Radio en N vueltas       » 6 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔══════════════════════════╗")
          print("  \t║         Formula:         ║")
          print("  \t╠══════════════════════════╣")
          print("  \t║            m · v_n       ║")
          print("  \t║     R_n = ─────────      ║")
          print("  \t║             q · B        ║")
          print("  \t╚══════════════════════════╝")
          
          m = float(input("\n\t m   ► Masa de la particula (m)    : "))
          
          v = float(input("\n\t v_n ► velocidad en N vueltas (m/s): "))
          
          q = float(input("\n\t q   ► Carga de la particula (c)   : "))

          B = float(input("\n\t B   ► Campo magnetico (T)         : "))
          
          R = (m*v)/(q*B)
          
          print("\nR_n (m): ",R)
     
     elif o == 7:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Frecuencia por R y v     » 7 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔══════════════════════════╗		╔══════════════════════════╗")
          print("  \t║         Formula:         ║		║         Formula:         ║")
          print("  \t╠══════════════════════════╣		╠══════════════════════════╣")
          print("  \t║              v           ║		║            2π · r        ║")
          print("  \t║      f =  ────────       ║		║       T = ────────       ║")
          print("  \t║            2π · r        ║		║               v          ║")
          print("  \t╚══════════════════════════╝		╚══════════════════════════╝")
          
          v = float(input("\n\t v ► velocidad (m/s): "))
          
          R = float(input("\n\t R ► Radio (m)      : "))
          
          f = v/((2*math.pi)*R)
          
          T = ((2*math.pi)*R)/v
          
          print("\nf (rev/s): ",f)
          print("  T (s): ",T)
          
     elif o == 8:
          print("\n\t╔══════════════════════════════════════╗")
          print("  \t╠══ ► Campo magnetico          » 8 « ══╣")
          print("  \t╚══════════════════════════════════════╝")
          
          print("\n\t╔══════════════════════════╗")
          print("  \t║         Formula:         ║")
          print("  \t╠══════════════════════════╣")
          print("  \t║             m · v        ║")
          print("  \t║        B = ───────       ║")
          print("  \t║             q · R        ║")
          print("  \t╚══════════════════════════╝")
          
          m = float(input("\n\t m ► Masa de la particula (kg): "))
          
          v = float(input("\n\t v ► velocidad (m/s)          : "))
          
          q = float(input("\n\t q ► Carga de la particula (c): "))  
          
          R = float(input("\n\t R ► Radio (m)                : "))
          
          B = (m*v)/(q*R)
          
          print("\nB (T): ",B)
          
     p = str(input("\n\t¿Deseas calcular otra cosa respecto al ciclotrón? [si/no] »» "))