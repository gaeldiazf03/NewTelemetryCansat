import ttkbootstrap.themes.standard as st

# Variables
themename = "darkly"
font = "Cascadia Code 12"
config = {
    "geometry": "1700x723",  # Tamaño de la ventana (ratio 2.35:1)
    "title": "Probando Frames",  # Título de la ventana
    "icon": "img\\sinFondo.ico",  # Icono de la ventana
    "style": themename,  # Tema de la ventana
}
colores = {
    "background": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "foreground": str(st.STANDARD_THEMES[themename]["colors"]["light"]),
    "activebackground": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "activeforeground": str(st.STANDARD_THEMES[themename]["colors"]["light"]),
    "bordercolor": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "lightcolor": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "darkcolor": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "selectcolor": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "selectbackground": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "selectforeground": str(st.STANDARD_THEMES[themename]["colors"]["light"])
}