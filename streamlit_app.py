import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    v0 = random.randint(1, 20)  # Velocidad inicial en m/s
    t = random.randint(1, 10)    # Tiempo en segundos
    a = random.randint(1, 5)      # Aceleración en m/s²
    # Fórmula: x = v0*t + 0.5*a*t^2
    x_correcto = v0 * t + 0.5 * a * t ** 2
    return v0, t, a, x_correcto

# Interfaz de usuario
st.title("Ejercicios de Cinemática")

# Generar un nuevo ejercicio
if st.button("Generar Ejercicio"):
    v0, t, a, x_correcto = generar_ejercicio()
    st.write(f"Un objeto parte con una velocidad inicial de {v0} m/s.")
    st.write(f"La aceleración es de {a} m/s² y el tiempo es de {t} segundos.")
    st.write("¿Cuál es la distancia recorrida (x) en metros?")
    
    # Input para la respuesta del usuario
    respuesta_usuario = st.number_input("Tu respuesta:", min_value=0.0)

    # Botón para verificar la respuesta
    if st.button("Verificar Respuesta"):
        if respuesta_usuario == x_correcto:
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. La respuesta correcta es {x_correcto:.2f} metros.")
