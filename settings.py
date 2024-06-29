import ttkbootstrap.themes.standard as st

# Variables
geometry = "1700x723"
title = "CansatGUI"
icon = "img\\sinFondo.ico"
themename = "darkly"
font = "Cascadia Code 12"
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