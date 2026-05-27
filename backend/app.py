# ==========================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================

# Librería para crear dashboard interactivo
import streamlit as st

# Librería para manipulación de datos
import pandas as pd

# Librería para gráficas interactivas
import plotly.express as px

# Librería para cargar modelos entrenados
import joblib


# ==========================================
# CARGAR DATASET LIMPIO
# ==========================================

# Ruta dataset limpio
ruta = "data/processed/energy_dataset_clean.csv"

# Cargar dataset
df = pd.read_csv(
    
    ruta,
    
    # Convertir datetime automáticamente
    parse_dates=["Datetime"]
)

# Mostrar primeras filas
df.head()

# ==========================================
# CARGAR MODELOS ENTRENADOS
# ==========================================

# Cargar modelo Linear Regression
linear_model = joblib.load(
    
    "models/linear_regression.pkl"
)

# Cargar modelo Random Forest
rf_model = joblib.load(
    
    "models/random_forest.pkl"
)

# Cargar modelo Neural Network
nn_model = joblib.load(
    
    "models/neural_network.pkl"
)

# Mensaje consola
print(
    "Modelos cargados correctamente"
)

# ==========================================
# CREAR VARIABLES TEMPORALES
# ==========================================

# Crear columna año
df["Year"] = df["Datetime"].dt.year

# Crear columna mes
df["Month"] = df["Datetime"].dt.month

# Crear columna semana
df["Week"] = df["Datetime"].dt.isocalendar().week

# Crear columna día
df["Day"] = df["Datetime"].dt.day



# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================

# Configuración principal del dashboard
st.set_page_config(
    
    # Título de la pestaña
    page_title="EnergyIQ",
    
    # Icono del dashboard
    page_icon="⚡",
    
    # Diseño horizontal completo
    layout="wide"
)


# ==========================================
# ESTILOS PERSONALIZADOS
# ==========================================

# Aplicar estilos CSS personalizados
st.markdown(
    """
    <style>

    /* Fondo principal */
    .main {
        background-color: #0E1117;
    }

    /* Títulos */
    h1, h2, h3 {
        color: white;
    }

    /* Texto */
    p {
        color: #CFCFCF;
    }

    </style>
    """,
    
    # Permitir código HTML/CSS
    unsafe_allow_html=True
)


# ==========================================
# HEADER PRINCIPAL
# ==========================================

# Título principal del dashboard
st.title("⚡ EnergyIQ")

# Subtítulo principal
st.subheader(
    "Sistema Inteligente de Análisis Energético"
)

# Descripción del proyecto
st.write(
    """
    Plataforma interactiva de Machine Learning
    para análisis y predicción del consumo energético.
    """
)

# Línea divisora
st.divider()


# ==========================================
# SIDEBAR - PANEL DE CONTROL
# ==========================================

# Título de la barra lateral
st.sidebar.title("⚙️ Panel de Control")


# ==========================================
# NAVEGACIÓN PRINCIPAL
# ==========================================

# Menú de navegación del dashboard
section = st.sidebar.radio(
    
    # Título del menú
    "Navegación",
    
    # Opciones disponibles
    [
        "Dashboard",
        "Modelos IA",
        "Visualizaciones",
        "Insights",
        "Dataset"
    ]
)


# ==========================================
# SELECTOR MODELO IA
# ==========================================

# Título sección modelos
st.sidebar.subheader("🤖 Modelo Predictivo")

# Selector del modelo de Machine Learning
selected_model = st.sidebar.selectbox(
    
    # Nombre del selector
    "Seleccionar modelo",
    
    # Modelos disponibles
    [
        "Linear Regression",
        "Random Forest",
        "Neural Network"
    ]
)

# ==========================================
# SELECCIONAR MODELO ACTIVO
# ==========================================

# Modelo Linear Regression
if selected_model == "Linear Regression":
    
    # Modelo activo
    active_model = linear_model


# Modelo Random Forest
elif selected_model == "Random Forest":
    
    # Modelo activo
    active_model = rf_model


# Modelo Neural Network
elif selected_model == "Neural Network":
    
    # Modelo activo
    active_model = nn_model

# ==========================================
# SELECTOR TEMPORAL
# ==========================================

# Título sección temporal
st.sidebar.subheader("📅 Análisis Temporal")

# Selector tipo de análisis temporal
selected_time = st.sidebar.selectbox(
    
    # Nombre del selector
    "Seleccionar período",
    
    # Opciones disponibles
    [
        "Año",
        "Mes",
        "Semana",
        "Día"
    ]
)

# ==========================================
# FILTRO TEMPORAL
# ==========================================

# Filtrar por año
if selected_time == "Año":
    
    # Obtener años disponibles
    years = sorted(df["Year"].unique())
    
    # Selector de años
    selected_year = st.sidebar.selectbox(
        
        # Nombre selector
        "Seleccionar año",
        
        # Lista años
        years
    )
    
    # Filtrar dataset
    filtered_df = df[
        df["Year"] == selected_year
    ]


# ==========================================
# FILTRO POR MES
# ==========================================

elif selected_time == "Mes":
    
    # Obtener meses disponibles
    months = sorted(df["Month"].unique())
    
    # Selector meses
    selected_month = st.sidebar.selectbox(
        
        # Nombre selector
        "Seleccionar mes",
        
        # Lista meses
        months
    )
    
    # Filtrar dataset
    filtered_df = df[
        df["Month"] == selected_month
    ]


# ==========================================
# FILTRO POR SEMANA
# ==========================================

elif selected_time == "Semana":
    
    # Obtener semanas disponibles
    weeks = sorted(df["Week"].unique())
    
    # Selector semanas
    selected_week = st.sidebar.selectbox(
        
        # Nombre selector
        "Seleccionar semana",
        
        # Lista semanas
        weeks
    )
    
    # Filtrar dataset
    filtered_df = df[
        df["Week"] == selected_week
    ]


# ==========================================
# FILTRO POR DÍA
# ==========================================

elif selected_time == "Día":
    
    # Obtener días disponibles
    days = sorted(df["Day"].unique())
    
    # Selector días
    selected_day = st.sidebar.selectbox(
        
        # Nombre selector
        "Seleccionar día",
        
        # Lista días
        days
    )
    
    # Filtrar dataset
    filtered_df = df[
        df["Day"] == selected_day
    ]
# ==========================================
# DASHBOARD PRINCIPAL
# ==========================================

if section == "Dashboard":

    # ==========================================
    # KPIs DINÁMICOS
    # ==========================================

    # Título sección métricas
    st.header("📊 KPIs Principales")

    # Calcular consumo promedio
    avg_consumption = round(
        
        filtered_df["Global_active_power"].mean(),
        
        2
    )

    # Calcular voltaje promedio
    avg_voltage = round(
        
        filtered_df["Voltage"].mean(),
        
        2
    )

    # Calcular intensidad promedio
    avg_intensity = round(
        
        filtered_df["Global_intensity"].mean(),
        
        2
    )

    # Calcular cantidad registros
    total_records = filtered_df.shape[0]


    # ==========================================
    # CREAR COLUMNAS KPIs
    # ==========================================

    # Crear columnas horizontales
    col1, col2, col3, col4 = st.columns(4)


    # KPI CONSUMO
    with col1:

        st.metric(
            
            label="⚡ Consumo Promedio",
            
            value=f"{avg_consumption} kW"
        )


    # KPI VOLTAJE
    with col2:

        st.metric(
            
            label="⚡ Voltaje Promedio",
            
            value=f"{avg_voltage} V"
        )


    # KPI INTENSIDAD
    with col3:

        st.metric(
            
            label="📈 Intensidad Promedio",
            
            value=f"{avg_intensity} A"
        )


    # KPI REGISTROS
    with col4:

        st.metric(
            
            label="📂 Registros",
            
            value=total_records
        )


    # Línea divisora
    st.divider()


    # ==========================================
    # GRÁFICA CONSUMO ENERGÉTICO
    # ==========================================

    # Título sección gráfica
    st.header("📈 Consumo Energético")

    # Crear gráfica temporal
    fig = px.line(
        
        filtered_df,
        
        x="Datetime",
        
        y="Global_active_power",
        
        title="Consumo Energético a través del Tiempo"
    )

    # Mostrar gráfica
    st.plotly_chart(
        
        fig,
        
        use_container_width=True
    )

    




# ==========================================
# SECCIÓN DATASET
# ==========================================

elif section == "Dataset":

    # Calcular registros
    total_records = filtered_df.shape[0]

    # Título sección dataset
    st.header("📂 Datos Filtrados")

    # Mostrar cantidad registros
    st.write(
        
        f"Registros encontrados: {total_records}"
    )

    # Mostrar dataframe interactivo
    st.dataframe(
        
        filtered_df,
        
        use_container_width=True
    )


# ==========================================
# SECCIÓN MODELOS IA
# ==========================================

elif section == "Modelos IA":

    # Título sección modelos
    st.header("🤖 Comparación Modelos IA")


    # ==========================================
    # CARGAR MÉTRICAS MODELOS
    # ==========================================

    # Cargar métricas Linear Regression
    linear_metrics = pd.read_csv(
        
        "results/linear_regression_metrics.csv"
    )

    # Cargar métricas Random Forest
    rf_metrics = pd.read_csv(
        
        "results/random_forest_metrics.csv"
    )

    # Cargar métricas Neural Network
    nn_metrics = pd.read_csv(
        
        "results/neural_network_metrics.csv"
    )


    # ==========================================
    # UNIR MÉTRICAS MODELOS
    # ==========================================

    # Combinar métricas
    models_df = pd.concat(
        
        [
            linear_metrics,
            rf_metrics,
            nn_metrics
        ],
        
        ignore_index=True
    )


    # ==========================================
    # MOSTRAR TABLA MODELOS
    # ==========================================

    # Mostrar dataframe modelos
    st.dataframe(
        
        models_df,
        
        use_container_width=True
    )

    # ==========================================
    # PREDICCIÓN IA
    # ==========================================

    # Línea divisora
    st.divider()

    # Título sección predicción
    st.header("🤖 Predicción IA")

    
    # ==========================================
    # VARIABLES PARA PREDICCIÓN
    # ==========================================

    # Seleccionar variables usadas en entrenamiento
    X_predict = filtered_df[
        [
            "Global_reactive_power",
            "Voltage",
            "Global_intensity",
            "Sub_metering_1",
            "Sub_metering_2",
            "Sub_metering_3"
        ]
    ]


    # ==========================================
    # REALIZAR PREDICCIÓN
    # ==========================================

    # Generar predicciones
    predictions = active_model.predict(
        
        X_predict
    )


    # ==========================================
    # CALCULAR PROMEDIOS
    # ==========================================

    # Promedio real
    real_avg = round(
        
        filtered_df["Global_active_power"].mean(),
        
        2
    )

    # Promedio predicho
    predicted_avg = round(
        
        predictions.mean(),
        
        2
    )


    # ==========================================
    # MOSTRAR RESULTADOS
    # ==========================================

    # Crear columnas
    pred1, pred2, pred3 = st.columns(3)


    # Consumo real
    with pred1:

        st.metric(
            
            label="⚡ Consumo Real",
            
            value=f"{real_avg} kW"
        )


    # Consumo predicho
    with pred2:

        st.metric(
            
            label="🤖 Predicción IA",
            
            value=f"{predicted_avg} kW"
        )


    # Modelo utilizado
    with pred3:

        st.metric(
            
            label="🧠 Modelo Utilizado",
            
            value=selected_model
        )

# ==========================================
    # GRÁFICA REAL VS PREDICCIÓN
    # ==========================================

    # Crear dataframe comparación
    comparison_df = pd.DataFrame(
        
        {
            "Datetime": filtered_df["Datetime"],
            
            "Real": filtered_df["Global_active_power"],
            
            "Predicción IA": predictions
        }
    )


    # ==========================================
    # CREAR GRÁFICA COMPARATIVA
    # ==========================================

    # Título gráfica
    st.header("📈 Comparación Real vs IA")

    # Crear gráfica líneas
    fig_compare = px.line(
        
        comparison_df,
        
        x="Datetime",
        
        y=[
            "Real",
            "Predicción IA"
        ],
        
        title="Consumo Real vs Predicción IA"
    )

    # Mostrar gráfica
    st.plotly_chart(
        
        fig_compare,
        
        use_container_width=True
    )


# ==========================================
# SECCIÓN VISUALIZACIONES
# ==========================================

elif section == "Visualizaciones":

    # Título sección visualizaciones
    st.header("📈 Visualizaciones")

    # ==========================================
    # HISTOGRAMA CONSUMO ENERGÉTICO
    # ==========================================

    # Crear histograma consumo energético
    fig_hist = px.histogram(
        
        # Dataset filtrado
        filtered_df,
        
        # Variable eje X
        x="Global_active_power",
        
        # Número intervalos histograma
        nbins=50,
        
        # Título gráfica
        title="Distribución del Consumo Energético"
    )

    # Mostrar histograma interactivo
    st.plotly_chart(
        
        fig_hist,
        
        use_container_width=True
    )

    # ==========================================
    # BOXPLOT CONSUMO ENERGÉTICO
    # ==========================================

    # Crear boxplot consumo energético
    fig_box = px.box(
        
        # Dataset filtrado
        filtered_df,
        
        # Variable eje Y
        y="Global_active_power",
        
        # Título gráfica
        title="Distribución del Consumo Energético"
    )

    # Mostrar boxplot interactivo
    st.plotly_chart(
        
        fig_box,
        
        use_container_width=True
    )

    # ==========================================
    # HEATMAP DE CORRELACIONES
    # ==========================================

    # Seleccionar variables numéricas
    correlacion = filtered_df[
        [
            "Global_active_power",
            "Global_reactive_power",
            "Voltage",
            "Global_intensity",
            "Sub_metering_1",
            "Sub_metering_2",
            "Sub_metering_3"
        ]
    ].corr()


    # ==========================================
    # CREAR HEATMAP INTERACTIVO
    # ==========================================

    # Crear heatmap correlaciones
    fig_heatmap = px.imshow(
        
        # Matriz correlación
        correlacion,
        
        # Mostrar valores numéricos
        text_auto=True,
        
        # Título gráfica
        title="Mapa de Correlaciones"
    )


    # ==========================================
    # AJUSTAR TAMAÑO HEATMAP
    # ==========================================

    # Ajustar tamaño del heatmap
    fig_heatmap.update_layout(
        
        # Altura gráfica
        height=700
    )


    # ==========================================
    # MOSTRAR HEATMAP
    # ==========================================

    # Mostrar heatmap interactivo
    st.plotly_chart(
        
        fig_heatmap,
        
        use_container_width=True
    )

        # ==========================================
    # CONSUMO PROMEDIO POR HORA
    # ==========================================

    # Crear columna hora
    filtered_df["Hour"] = (
        
        filtered_df["Datetime"].dt.hour
    )


    # ==========================================
    # CALCULAR PROMEDIO POR HORA
    # ==========================================

    # Agrupar consumo promedio por hora
    consumo_hora = filtered_df.groupby(
        
        "Hour"
        
    )["Global_active_power"].mean().reset_index()


    # ==========================================
    # CREAR GRÁFICA DE BARRAS
    # ==========================================

    # Crear gráfica barras
    fig_bar = px.bar(
        
        # Dataset agrupado
        consumo_hora,
        
        # Eje X
        x="Hour",
        
        # Eje Y
        y="Global_active_power",
        
        # Título gráfica
        title="Consumo Promedio por Hora"
    )


    # ==========================================
    # MOSTRAR GRÁFICA
    # ==========================================

    # Mostrar gráfica interactiva
    st.plotly_chart(
        
        fig_bar,
        
        use_container_width=True
    )
        # ==========================================
    # DIAGRAMA DE DISPERSIÓN
    # ==========================================

    # Crear scatter plot interactivo
    fig_scatter = px.scatter(
        
        # Dataset filtrado
        filtered_df,
        
        # Variable eje X
        x="Global_intensity",
        
        # Variable eje Y
        y="Global_active_power",
        
        # Transparencia puntos
        opacity=0.3,
        
        # Título gráfica
        title="Relación entre Intensidad y Consumo"
    )


    # ==========================================
    # MOSTRAR SCATTER PLOT
    # ==========================================

    # Mostrar gráfica interactiva
    st.plotly_chart(
        
        fig_scatter,
        
        use_container_width=True
    )

# ==========================================
# SECCIÓN INSIGHTS
# ==========================================

elif section == "Insights":

    # Título sección insights
    st.header("🧠 Insights")

    # Mensaje temporal
    st.info(
        "Próximamente análisis e insights."
    )


# ==========================================
# FOOTER
# ==========================================

# Línea divisora
st.divider()

# Texto pie de página
st.caption(
    "EnergyIQ Dashboard © 2026"
)