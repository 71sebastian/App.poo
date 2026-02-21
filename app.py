import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Proyecto Módulo 1 - Python Fundamentals",
    page_icon="🐍",
    layout="wide"
)

# Inicializar el estado de la sesión para almacenar actividades
if 'actividades' not in st.session_state:
    st.session_state.actividades = []

# Menú lateral
menu = st.sidebar.selectbox(
    "📊 Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# Título principal en el sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 Proyecto Aplicado")
st.sidebar.markdown("Módulo 1 - Python Fundamentals")

# Módulo Home
if menu == "Home":
    # Título principal
    st.title("🏠 Proyecto Integrador - Python Fundamentals")
    
    # Información personal del estudiante
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 👤 Información del Estudiante")
        st.markdown("**Nombre completo:** Sebastian Alvarez Luyo")
        st.markdown("**Curso:** Especialización en Python for Analytics")
        st.markdown("**Módulo:** Módulo 1 – Python Fundamentals")
        st.markdown(f"**Año:** {datetime.now().year}")
        
    with col2:
        # Puedes agregar una imagen si lo deseas
        st.image("https://www.python.org/static/community_logos/python-logo-generic.svg", width=200)
    
    # Descripción del proyecto
    st.markdown("---")
    st.markdown("## 📝 Descripción del Proyecto")
    st.write("""
    Esta aplicación interactiva desarrollada en Streamlit integra los conceptos fundamentales 
    aprendidos durante el Módulo 1 del curso, incluyendo:
    
    - ✅ Variables y estructuras de datos
    - ✅ Control de flujo (condicionales y bucles)
    - ✅ Funciones y programación funcional
    - ✅ Programación Orientada a Objetos (POO)
    
    Cada ejercicio representa un módulo independiente que demuestra la aplicación práctica 
    de estos conceptos en un contexto de análisis financiero.
    """)
    
    # Tecnologías utilizadas
    st.markdown("## 🛠️ Tecnologías Utilizadas")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        - 🐍 Python 3.9+
        - 📊 Streamlit
        - 🧮 NumPy
        """)
    
    with col2:
        st.markdown("""
        - 📈 Pandas
        - 💾 Session State
        - 🔄 Programación Funcional
        """)
    
    with col3:
        st.markdown("""
        - 🏗️ POO
        - 📱 Responsive Design
        - 🎨 Custom CSS
        """)
    
    # Estructura del proyecto
    st.markdown("## 📁 Estructura del Proyecto")
    st.code("""
    proyecto-modulo1/
    ├── app.py          # Archivo principal
    ├── requirements.txt # Dependencias
    └── README.md       # Documentación
    """)

elif menu == "Ejercicio 1":
    st.title("💰 Ejercicio 1: Controla tu dinero por meses")
    
    st.write("""
    ### 🎯 Ahora puedes evaluar gastos en múltiples meses
    - **Presupuesto mensual:** Cuánto tienes para gastar cada mes
    - **Gasto mensual:** Cuánto gastas por mes
    - **Meses:** Por cuántos meses quieres evaluar
    """)
    
    st.write("---")
    
    # SESSION STATE PARA GUARDAR LOS VALORES
    if 'presupuesto_mensual' not in st.session_state:
        st.session_state.presupuesto_mensual = 1000.0
    if 'gasto_mensual' not in st.session_state:
        st.session_state.gasto_mensual = 500.0
    if 'meses_evaluar' not in st.session_state:
        st.session_state.meses_evaluar = 1  # Valor por defecto: 1 mes
    
    # Crear columnas para organizar
    col1, col2 = st.columns(2)
    
    with col1:
        # INPUT DE PRESUPUESTO MENSUAL
        presupuesto_mensual = st.number_input(
            "📊 Presupuesto MENSUAL:",
            min_value=0.0,
            value=st.session_state.presupuesto_mensual,
            step=100.0,
            format="%.2f",
            key="input_presupuesto_mensual",
            help="Cuánto dinero tienes disponible CADA MES"
        )
        
        # INPUT DE GASTO MENSUAL
        gasto_mensual = st.number_input(
            "💸 Gasto MENSUAL:",
            min_value=0.0,
            value=st.session_state.gasto_mensual,
            step=50.0,
            format="%.2f",
            key="input_gasto_mensual",
            help="Cuánto dinero gastas CADA MES"
        )
    
    with col2:
        # 📅 DESPLEGABLE DE MESES (selectbox)
        meses = st.selectbox(
            "📅 Período a evaluar:",
            options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            index=st.session_state.meses_evaluar - 1,  # -1 porque las listas empiezan en 0
            format_func=lambda x: f"{x} {'mes' if x == 1 else 'meses'}",
            key="select_meses",
            help="Elige por cuántos meses quieres evaluar"
        )
        
        # Mostrar información visual del período
        if meses == 1:
            st.info("📆 Evaluando 1 mes")
        else:
            st.info(f"📆 Evaluando {meses} meses")
        
        # Calcular totales
        presupuesto_total = presupuesto_mensual * meses
        gasto_total = gasto_mensual * meses
        
        st.metric(
            label="💰 Presupuesto TOTAL",
            value=f"${presupuesto_total:,.2f}",
            delta=f"({meses} meses × ${presupuesto_mensual:,.2f})"
        )
        
        st.metric(
            label="💸 Gasto TOTAL",
            value=f"${gasto_total:,.2f}",
            delta=f"({meses} meses × ${gasto_mensual:,.2f})"
        )
    
    # Guardar en session_state
    st.session_state.presupuesto_mensual = presupuesto_mensual
    st.session_state.gasto_mensual = gasto_mensual
    st.session_state.meses_evaluar = meses
    
    st.write("---")
    
    # BOTONES
    col1, col2, col3 = st.columns(3)
    
    with col1:
        evaluar = st.button("🔍 Evaluar gastos", type="primary", use_container_width=True)
    
    with col3:
        limpiar = st.button("🧹 Limpiar todo", type="secondary", use_container_width=True)
    
    if limpiar:
        # Resetear valores
        st.session_state.presupuesto_mensual = 1000.0
        st.session_state.gasto_mensual = 500.0
        st.session_state.meses_evaluar = 1
        st.rerun()
    
    if evaluar:
        st.write("---")
        st.write("### 📊 RESULTADO DETALLADO")
        
        # Calcular totales
        presupuesto_total = presupuesto_mensual * meses
        gasto_total = gasto_mensual * meses
        
        # Evaluación general
        if gasto_total <= presupuesto_total:
            diferencia = presupuesto_total - gasto_total
            st.success(f"✅ **¡TODO BIEN!** En total, estás DENTRO del presupuesto")
            
            # Crear columnas para mostrar información
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Presupuesto TOTAL", f"${presupuesto_total:,.2f}")
            
            with col2:
                st.metric("Gasto TOTAL", f"${gasto_total:,.2f}")
            
            with col3:
                st.metric("Te sobran", f"${diferencia:,.2f}", delta="👍")
            
            # Mostrar tabla mes por mes
            st.write("---")
            st.write("### 📅 Desglose por mes:")
            
            datos_meses = []
            for mes in range(1, meses + 1):
                datos_meses.append({
                    "Mes": f"Mes {mes}",
                    "Presupuesto": f"${presupuesto_mensual:,.2f}",
                    "Gasto": f"${gasto_mensual:,.2f}",
                    "Diferencia": f"${presupuesto_mensual - gasto_mensual:,.2f}",
                    "Estado": "✅ Bien"
                })
            
            df_meses = pd.DataFrame(datos_meses)
            st.dataframe(df_meses, use_container_width=True)
            
        else:
            diferencia = gasto_total - presupuesto_total
            st.error(f"❌ **¡CUIDADO!** En total, EXCEDISTE el presupuesto")
            
            # Crear columnas para mostrar información
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Presupuesto TOTAL", f"${presupuesto_total:,.2f}")
            
            with col2:
                st.metric("Gasto TOTAL", f"${gasto_total:,.2f}")
            
            with col3:
                st.metric("Te faltan", f"${diferencia:,.2f}", delta="⚠️", delta_color="inverse")
            
            # Mostrar tabla mes por mes con advertencia
            st.write("---")
            st.write("### 📅 Desglose por mes:")
            
            datos_meses = []
            for mes in range(1, meses + 1):
                if gasto_mensual <= presupuesto_mensual:
                    estado = "✅ Bien"
                else:
                    estado = "⚠️ Excedido"
                    
                datos_meses.append({
                    "Mes": f"Mes {mes}",
                    "Presupuesto": f"${presupuesto_mensual:,.2f}",
                    "Gasto": f"${gasto_mensual:,.2f}",
                    "Diferencia": f"${gasto_mensual - presupuesto_mensual:,.2f}",
                    "Estado": estado
                })
            
            df_meses = pd.DataFrame(datos_meses)
            st.dataframe(df_meses, use_container_width=True)
        
        # Gráfico de comparación (opcional, si quieres algo visual)
        st.write("---")
        st.write("### 📊 Visualización:")
        
        # Datos para el gráfico
        chart_data = pd.DataFrame({
            'Mes': [f'M{mes}' for mes in range(1, meses + 1)],
            'Presupuesto': [presupuesto_mensual] * meses,
            'Gasto': [gasto_mensual] * meses
        })
        
        # Mostrar gráfico de barras
        st.bar_chart(chart_data.set_index('Mes'))
        
        # Resumen final
        st.write("---")
        st.write("### 📝 Resumen ejecutivo:")
        
        if gasto_total <= presupuesto_total:
            st.success(f"""
            ✅ **Análisis positivo:**
            - Presupuesto mensual: ${presupuesto_mensual:,.2f}
            - Gasto mensual: ${gasto_mensual:,.2f}
            - Período: {meses} { 'mes' if meses == 1 else 'meses' }
            - Ahorro total: ${presupuesto_total - gasto_total:,.2f}
            - Ahorro mensual: ${(presupuesto_mensual - gasto_mensual):,.2f}
            """)
        else:
            st.warning(f"""
            ⚠️ **Análisis de riesgo:**
            - Presupuesto mensual: ${presupuesto_mensual:,.2f}
            - Gasto mensual: ${gasto_mensual:,.2f}
            - Período: {meses} { 'mes' if meses == 1 else 'meses' }
            - Déficit total: ${gasto_total - presupuesto_total:,.2f}
            - Déficit mensual: ${(gasto_mensual - presupuesto_mensual):,.2f}
            
            💡 **Sugerencia:** Necesitas reducir tu gasto mensual en 
            ${(gasto_mensual - presupuesto_mensual):,.2f} para estar dentro del presupuesto.
            """)

elif menu == "Ejercicio 2":
    st.title("📋 Ejercicio 2: Registro de actividades financieras")
    
    st.write("### Registra tus finanzas personales")
    st.write("---")
    
    # INICIALIZAR SESSION STATE PARA LOS CAMPOS
    if 'campo_nombre' not in st.session_state:
        st.session_state.campo_nombre = ""
    if 'campo_tipo' not in st.session_state:
        st.session_state.campo_tipo = "Ingreso"
    if 'campo_presupuesto' not in st.session_state:
        st.session_state.campo_presupuesto = 1000.0
    if 'campo_gasto' not in st.session_state:
        st.session_state.campo_gasto = 500.0
    
    # LISTA DE CATEGORÍAS (LAS QUE PEDISTE)
    categorias = ["Ingreso", "Egreso", "Ahorro", "Inversión"]
    
    # INPUTS con valores desde session_state
    col1, col2 = st.columns(2)
    
    with col1:
        nombre = st.text_input(
            "📌 Nombre de la actividad:",
            value=st.session_state.campo_nombre,
            placeholder="Ej: Sueldo, Alquiler, Ahorro mensual..."
        )
        
        tipo = st.selectbox(
            "🏷️ Tipo:",
            options=categorias,
            index=categorias.index(st.session_state.campo_tipo)
        )
    
    with col2:
        presupuesto = st.number_input(
            "💰 Presupuesto / Meta:",
            min_value=0.0,
            value=st.session_state.campo_presupuesto,
            step=100.0,
            format="%.2f"
        )
        
        gasto_real = st.number_input(
            "💸 Monto real:",
            min_value=0.0,
            value=st.session_state.campo_gasto,
            step=50.0,
            format="%.2f"
        )
    
    # Mensaje de ayuda según el tipo seleccionado
    if tipo == "Ingreso":
        st.info("💡 **Ingreso:** El monto real debería ser MAYOR o IGUAL al presupuesto")
    elif tipo == "Egreso":
        st.info("💡 **Egreso:** El monto real debería ser MENOR o IGUAL al presupuesto")
    elif tipo == "Ahorro":
        st.info("💡 **Ahorro:** El monto real es lo que guardaste. ¡Entre más, mejor!")
    elif tipo == "Inversión":
        st.info("💡 **Inversión:** Dinero que pones a trabajar. El retorno se calcula después")
    
    # BOTONES
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Guardar actividad", type="primary", use_container_width=True):
            if nombre:
                nueva = {
                    "nombre": nombre,
                    "tipo": tipo,
                    "presupuesto": presupuesto,
                    "gasto_real": gasto_real
                }
                st.session_state.actividades.append(nueva)
                
                # Limpiar campos después de guardar
                st.session_state.campo_nombre = ""
                st.session_state.campo_tipo = "Ingreso"
                st.session_state.campo_presupuesto = 1000.0
                st.session_state.campo_gasto = 500.0
                
                st.success(f"✅ Actividad '{nombre}' guardada")
                st.balloons()
                st.rerun()
            else:
                st.error("❌ Por favor, ingresa un nombre para la actividad")
    
    with col2:
        if st.button("🧹 Limpiar campos", type="secondary", use_container_width=True):
            st.session_state.campo_nombre = ""
            st.session_state.campo_tipo = "Ingreso"
            st.session_state.campo_presupuesto = 1000.0
            st.session_state.campo_gasto = 500.0
            st.rerun()
    
    # MOSTRAR ACTIVIDADES GUARDADAS
    st.write("---")
    st.write("### 📊 Actividades guardadas")
    
    if len(st.session_state.actividades) == 0:
        st.info("No hay actividades registradas. ¡Agrega tu primera actividad!")
        
        # Mostrar ejemplos
        with st.expander("📝 Ver ejemplos:"):
            st.write("""
            **Ingreso:** "Sueldo enero" - Presupuesto: $1000, Real: $1000
            **Egreso:** "Alquiler" - Presupuesto: $500, Real: $500
            **Ahorro:** "Ahorro mensual" - Presupuesto: $200, Real: $250
            **Inversión:** "Plazo fijo" - Presupuesto: $1000, Real: $1000
            """)
    else:
        # Botón para limpiar todo
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🗑️ Eliminar todas", type="secondary"):
                st.session_state.actividades = []
                st.rerun()
        
        with col1:
            st.write(f"**Total:** {len(st.session_state.actividades)} actividades")
        
        # Mostrar tabla
        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df, use_container_width=True)
        
        # Evaluar cada actividad según su tipo
        st.write("### 📈 Evaluación:")
        
        for act in st.session_state.actividades:
            if act["tipo"] == "Ingreso":
                if act["gasto_real"] >= act["presupuesto"]:
                    diferencia = act["gasto_real"] - act["presupuesto"]
                    st.success(f"✅ {act['nombre']} (Ingreso): Cumplido +${diferencia:,.2f} extra")
                else:
                    diferencia = act["presupuesto"] - act["gasto_real"]
                    st.warning(f"⚠️ {act['nombre']} (Ingreso): Faltaron ${diferencia:,.2f}")
            
            elif act["tipo"] == "Egreso":
                if act["gasto_real"] <= act["presupuesto"]:
                    ahorro = act["presupuesto"] - act["gasto_real"]
                    st.success(f"✅ {act['nombre']} (Egreso): Dentro del presupuesto, ahorraste ${ahorro:,.2f}")
                else:
                    exceso = act["gasto_real"] - act["presupuesto"]
                    st.warning(f"⚠️ {act['nombre']} (Egreso): Excedido en ${exceso:,.2f}")
            
            elif act["tipo"] == "Ahorro":
                if act["gasto_real"] >= act["presupuesto"]:
                    extra = act["gasto_real"] - act["presupuesto"]
                    st.success(f"✅ {act['nombre']} (Ahorro): Meta superada, ahorraste ${extra:,.2f} extra")
                else:
                    falta = act["presupuesto"] - act["gasto_real"]
                    st.warning(f"⚠️ {act['nombre']} (Ahorro): Te faltaron ${falta:,.2f} para la meta")
            
            elif act["tipo"] == "Inversión":
                if act["gasto_real"] == act["presupuesto"]:
                    st.success(f"✅ {act['nombre']} (Inversión): Inversión realizada correctamente")
                elif act["gasto_real"] > act["presupuesto"]:
                    extra = act["gasto_real"] - act["presupuesto"]
                    st.info(f"ℹ️ {act['nombre']} (Inversión): Invertiste ${extra:,.2f} más de lo planeado")
                else:
                    falta = act["presupuesto"] - act["gasto_real"]
                    st.info(f"ℹ️ {act['nombre']} (Inversión): Invertiste ${falta:,.2f} menos de lo planeado")
        
        # Totales por categoría
        st.write("---")
        st.write("### 💰 Resumen por categoría:")
        
        # Calcular totales
        total_ingresos = sum(a["gasto_real"] for a in st.session_state.actividades if a["tipo"] == "Ingreso")
        total_egresos = sum(a["gasto_real"] for a in st.session_state.actividades if a["tipo"] == "Egreso")
        total_ahorros = sum(a["gasto_real"] for a in st.session_state.actividades if a["tipo"] == "Ahorro")
        total_inversiones = sum(a["gasto_real"] for a in st.session_state.actividades if a["tipo"] == "Inversión")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("💰 Ingresos", f"${total_ingresos:,.2f}")
        with col2:
            st.metric("💸 Egresos", f"${total_egresos:,.2f}")
        with col3:
            st.metric("🏦 Ahorros", f"${total_ahorros:,.2f}")
        with col4:
            st.metric("📈 Inversiones", f"${total_inversiones:,.2f}")
        
        # Balance final
        st.write("---")
        st.write("### 📊 Balance final:")
        
        balance = total_ingresos - total_egresos - total_ahorros - total_inversiones
        
        if balance >= 0:
            st.success(f"✅ Balance positivo: ${balance:,.2f} disponible")
        else:
            st.warning(f"⚠️ Balance negativo: ${balance:,.2f} de déficit")

elif menu == "Ejercicio 3":
    st.title("📈 Ejercicio 3: Calculando ganancias")
    
    # SESSION STATE PARA LOS VALORES
    if 'tasa' not in st.session_state:
        st.session_state.tasa = 10.0
    if 'meses' not in st.session_state:
        st.session_state.meses = 12
    
    # Verificar si hay actividades
    if len(st.session_state.actividades) == 0:
        st.warning("⚠️ Primero ve al Ejercicio 2 y agrega algunas actividades")
    else:
        st.write("### Calcularemos cuánto puedes ganar")
        
        # Pedir datos
        col1, col2 = st.columns(2)
        
        with col1:
            tasa = st.slider(
                "📊 Tasa de retorno (%):",
                0.0, 100.0,
                value=st.session_state.tasa,
                key="slider_tasa"
            ) / 100
            st.session_state.tasa = tasa * 100
        
        with col2:
            meses = st.number_input(
                "📅 Meses:",
                min_value=1,
                max_value=60,
                value=st.session_state.meses,
                key="input_meses"
            )
            st.session_state.meses = meses
        
        # BOTONES
        col1, col2, col3 = st.columns(3)
        
        with col1:
            calcular = st.button("🧮 Calcular retornos", type="primary")
        
        with col3:
            if st.button("🧹 Limpiar valores", type="secondary"):
                st.session_state.tasa = 10.0
                st.session_state.meses = 12
                st.rerun()
        
        if calcular:
            st.write("---")
            st.write("### Resultados:")
            
            # Definir la función
            def calcular(actividad):
                retorno = actividad["presupuesto"] * tasa * meses
                return {
                    "nombre": actividad["nombre"],
                    "presupuesto": actividad["presupuesto"],
                    "retorno": retorno
                }
            
            # Usar map
            resultados = list(map(calcular, st.session_state.actividades))
            
            # Mostrar resultados
            for r in resultados:
                with st.container():
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**{r['nombre']}**")
                    with col2:
                        st.write(f"💰 ${r['presupuesto']:,.2f}")
                    with col3:
                        st.success(f"📈 ${r['retorno']:,.2f}")
                    st.write("---")

elif menu == "Ejercicio 4":
    st.title("🏗️ Ejercicio 4: Programación Orientada a Objetivos")
    
    # Definir la clase
    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real
        
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto
        
        def mostrar_info(self):
            estado = "✅" if self.esta_en_presupuesto() else "⚠️"
            diferencia = abs(self.presupuesto - self.gasto_real)
            if self.esta_en_presupuesto():
                return f"{estado} {self.nombre} - Ahorraste ${diferencia:,.2f}"
            else:
                return f"{estado} {self.nombre} - Te faltaron ${diferencia:,.2f}"
    
    # Verificar si hay actividades
    if len(st.session_state.actividades) == 0:
        st.warning("⚠️ Primero ve al Ejercicio 2 y agrega algunas actividades")
    else:
        st.write("### Convirtiendo actividades a objetos")
        
        # BOTÓN DE LIMPIAR (ENCIMA DE LOS RESULTADOS)
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🔄 Refrescar objetos", type="secondary"):
                st.rerun()
        
        st.write("---")
        
        # Convertir cada diccionario en un objeto
        objetos_actividad = []
        for act_dict in st.session_state.actividades:
            obj = Actividad(
                act_dict["nombre"],
                act_dict["tipo"],
                act_dict["presupuesto"],
                act_dict["gasto_real"]
            )
            objetos_actividad.append(obj)
        
        # Mostrar la información
        for i, obj in enumerate(objetos_actividad):
            with st.expander(f"📌 {obj.nombre}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Tipo:** {obj.tipo}")
                    st.write(f"**Presupuesto:** ${obj.presupuesto:,.2f}")
                    st.write(f"**Gasto real:** ${obj.gasto_real:,.2f}")
                
                with col2:
                    st.write(f"**¿Cumple?** {obj.esta_en_presupuesto()}")
                    if obj.esta_en_presupuesto():
                        st.success(obj.mostrar_info())
                    else:
                        st.warning(obj.mostrar_info())
                
                # Botón individual para cada actividad (opcional)
                if st.button(f"🧹 Limpiar {obj.nombre}", key=f"btn_{i}"):
                    # Esto solo muestra un mensaje, no borra (para no complicar)
                    st.info(f"Para limpiar {obj.nombre}, ve al Ejercicio 2")