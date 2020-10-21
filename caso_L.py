# -*- coding: utf-8 -*-
from reticulado import Reticulado
from barra import Barra
from math import *

def caso_L():
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 

    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N

    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa

   #Parametros
    L = 6.0  *m
    B = 2.0 *m
    H = 100*m
    F1=7.84*KN
    F2=19.9*KN
    F3=23.52*KN

    #Inicializar modelo
    ret = Reticulado()

    #Nodos y Barras
    
    altura_punta = 105*m
    
############# NODOS PUENTE ################### 
       
    ret.agregar_nodo(10     , 0   ,  H         ) #0
    ret.agregar_nodo(10     , B   ,  H         ) #1
        
    ret.agregar_nodo(14     , 0   ,  H         ) #2 primeros nodos para las barras de 4 m
    ret.agregar_nodo(14     , B   ,  H         ) #3 primeros nodos para las barras de 4 m
    ret.agregar_nodo(12    , B/2 , altura_punta) #4  nodo punta

    contador_distancia_laterales = 14
    contador_distancia_punta = 14 + L/2
        
    for i in range(36):
            
        contador_distancia_laterales += L
        ret.agregar_nodo( contador_distancia_laterales ,0 , H) #5 
        ret.agregar_nodo( contador_distancia_laterales ,B , H) #6
            
        ret.agregar_nodo( contador_distancia_punta, B/2 , altura_punta) #7 nodo punta
        contador_distancia_punta += L
        
    ret.agregar_nodo(contador_distancia_laterales + 4    , 0   ,  H         ) #113 ultimos nodos para las barras de 4 m
    ret.agregar_nodo(contador_distancia_laterales + 4    , B   ,  H         ) #114 ultimos nodos para las barras de 4 m
    ret.agregar_nodo(contador_distancia_laterales + 2, B/2 , altura_punta)    #115 nodo punta
    
############# BARRAS PUENTE ###################         
    #Barras
    r = 8*cm
    r2= 10*cm
    r3= 10*cm
    r4= 20*cm
    A = 3.141592*(r)**2
    t = 8*mm
    t2 = 2*mm
    t3 = 8*mm
    t4 = 2*cm
    props =  [r,  t, 200*GPa, 7600*kg/m**3, 420*MPa]
    props2 = [r2, t2, 200*GPa, 7600*kg/m**3, 420*MPa]
    props3 = [r3, t3, 200*GPa, 7600*kg/m**3, 420*MPa]
    props4 = [r4, t4, 200*GPa, 7600*kg/m**3, 420*MPa]
    
    
    ret.agregar_barra(Barra(0, 1, *props))   
    ret.agregar_barra(Barra(0, 2, *props))   
    ret.agregar_barra(Barra(0, 3, *props))
    ret.agregar_barra(Barra(0, 4, *props2))
    
    ret.agregar_barra(Barra(1, 2, *props))  
    ret.agregar_barra(Barra(1, 3, *props))
    ret.agregar_barra(Barra(1, 4, *props2))
    
    ret.agregar_barra(Barra(2, 3, *props))  
    ret.agregar_barra(Barra(2, 4, *props2))
    
    ret.agregar_barra(Barra(3, 4, *props2)) 
    
    for n in range(37):
        num = 3*n+2
        ret.agregar_barra(Barra(num, num +3, *props))
        ret.agregar_barra(Barra(num, num +4, *props))
        ret.agregar_barra(Barra(num, num +5, *props2))
        
        ret.agregar_barra(Barra(num +1, num +3, *props))
        ret.agregar_barra(Barra(num +1, num +4, *props))
        ret.agregar_barra(Barra(num +1, num +5, *props2))
        
        ret.agregar_barra(Barra(num +3, num +4, *props))
        ret.agregar_barra(Barra(num +3, num +5, *props2))
        
        ret.agregar_barra(Barra(num +4, num +5, *props2))
        ret.agregar_barra(Barra(num +2, num +5, *props3))
        
    ret.agregar_barra(Barra(110, 113, *props))
    ret.agregar_barra(Barra(110, 114, *props))
    ret.agregar_barra(Barra(110, 115, *props2))
    
    ret.agregar_barra(Barra(111, 113, *props))
    ret.agregar_barra(Barra(111, 114, *props))
    ret.agregar_barra(Barra(111, 115, *props2))
    
    ret.agregar_barra(Barra(113, 114, *props))
    ret.agregar_barra(Barra(113, 115, *props2))
    
    ret.agregar_barra(Barra(114, 115, *props2))
 
############# RESTRICCIONES PUENTE ###################

    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    
    ret.agregar_restriccion(1, 0, 0)
    ret.agregar_restriccion(1, 1, 0)
    ret.agregar_restriccion(1, 2, 0)
    
    ret.agregar_restriccion(113, 0, 0)
    ret.agregar_restriccion(113, 1, 0)
    ret.agregar_restriccion(113, 2, 0)
    
    ret.agregar_restriccion(114, 0, 0)
    ret.agregar_restriccion(114, 1, 0)
    ret.agregar_restriccion(114, 2, 0)
    
    
    
    
###############  NODOS PILAR 1 ##############
    
    B = 2.0 *m
    
    ret.agregar_nodo(44.0    , 0   ,  53.0         ) #116
    ret.agregar_nodo(44.0    , B   ,  53.0         ) #117
    
 
###############  BARRAS PILAR 1 ##############    
 
    
    ret.agregar_barra(Barra(116 , 17, *props4)) 
    ret.agregar_barra(Barra(116 , 18, *props4))
    ret.agregar_barra(Barra(117,  17, *props4)) 
    ret.agregar_barra(Barra(117,  18, *props4))
    
###############  RESTRICCIONES PILAR 1 ##############
        
    ret.agregar_restriccion(116, 0, 0)
    ret.agregar_restriccion(116, 1, 0)
    ret.agregar_restriccion(116, 2, 0)
    
    ret.agregar_restriccion(117, 0, 0)
    ret.agregar_restriccion(117, 1, 0)
    ret.agregar_restriccion(117, 2, 0)
    
    
###############  NODOS PILAR 2 ##############
    
    B = 2.0 *m
    
    ret.agregar_nodo(80.0    , 0   ,  47.0         ) #118
    ret.agregar_nodo(80.0    , B   ,  47.0         ) #119
    
###############  BARRAS PILAR 2 ##############    
 
    
    ret.agregar_barra(Barra(118  , 35, *props4)) 
    ret.agregar_barra(Barra(118  , 36, *props4))
    ret.agregar_barra(Barra(119  , 35, *props4)) 
    ret.agregar_barra(Barra(119  , 36, *props4))
    
###############  RESTRICCIONES PILAR 2 ##############
        
    ret.agregar_restriccion(118, 0, 0)
    ret.agregar_restriccion(118, 1, 0)
    ret.agregar_restriccion(118, 2, 0)
    
    ret.agregar_restriccion(119, 0, 0)
    ret.agregar_restriccion(119, 1, 0)
    ret.agregar_restriccion(119, 2, 0)
    
###############  NODOS PILAR 3 ##############
    
    B = 2.0 *m  
    
    
    ret.agregar_nodo( 164  ,0 , 64) #120
    ret.agregar_nodo( 164  ,B , 64) #121

###############  BARRAS PILAR 3 ##############    
 
 
    
    ret.agregar_barra(Barra(120  , 77, *props4)) 
    ret.agregar_barra(Barra(120  , 78, *props4))
    ret.agregar_barra(Barra(121  , 77, *props4)) 
    ret.agregar_barra(Barra(121  , 78, *props4))
    
###############  RESTRICCIONES PILAR 3 ##############
        
    ret.agregar_restriccion(120, 0, 0)
    ret.agregar_restriccion(120, 1, 0)
    ret.agregar_restriccion(120, 2, 0)
    
    ret.agregar_restriccion(121, 0, 0)
    ret.agregar_restriccion(121, 1, 0)
    ret.agregar_restriccion(121, 2, 0)
    
    ret.agregar_fuerza(0, 2, -F1)
    ret.agregar_fuerza(1, 2, -F1)
    ret.agregar_fuerza(2, 2, -F2)
    ret.agregar_fuerza(3, 2, -F2)
    ret.agregar_fuerza(114, 2, -F1)
    ret.agregar_fuerza(113, 2, -F1)
    ret.agregar_fuerza(111, 2, -F2)
    ret.agregar_fuerza(110, 2, -F2)
    
    for n in range(35):
        nodo=3*n+5
        ret.agregar_fuerza(nodo, 2, -F3)
        ret.agregar_fuerza(nodo+1, 2, -F3)
    
    return ret