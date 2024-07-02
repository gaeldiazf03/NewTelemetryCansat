import ttkbootstrap.themes.standard as st

# Variables
geometry = "1700x723"
title = "CansatGUI"
icon = "img\\sinFondo.ico"
themename = "darkly"
font = ("Cascadia Code", 12)
bauds_list = ['9600', '115200']
colores = {
    "primary": str(st.STANDARD_THEMES[themename]["colors"]["primary"]),
    "secondary": str(st.STANDARD_THEMES[themename]["colors"]["secondary"]),
    "success": str(st.STANDARD_THEMES[themename]["colors"]["success"]),
    "info": str(st.STANDARD_THEMES[themename]["colors"]["info"]),
    "warning": str(st.STANDARD_THEMES[themename]["colors"]["warning"]),
    "danger": str(st.STANDARD_THEMES[themename]["colors"]["danger"]),
    "light": str(st.STANDARD_THEMES[themename]["colors"]["light"]),
    "dark": str(st.STANDARD_THEMES[themename]["colors"]["dark"]),
    "background": str(st.STANDARD_THEMES[themename]["colors"]["bg"]),
    "foreground": str(st.STANDARD_THEMES[themename]["colors"]["fg"]),
    "selectedbackground": str(st.STANDARD_THEMES[themename]["colors"]["selectbg"]),
    "selectedforeground": str(st.STANDARD_THEMES[themename]["colors"]["selectfg"]),
    "border": str(st.STANDARD_THEMES[themename]["colors"]["border"]),
    "inputforeground": str(st.STANDARD_THEMES[themename]["colors"]["inputfg"]),
    "inputbackground": str(st.STANDARD_THEMES[themename]["colors"]["inputbg"]),
    "active": str(st.STANDARD_THEMES[themename]["colors"]["active"])
}
