import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import quandl
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py

#data
GDP_arm = quandl.get("ODA/ARM_NGDPD", authtoken = "EvzHu2GEhMsgyzCTaFz6")
GDP_geo = quandl.get("ODA/GEO_NGDPD", authtoken = "EvzHu2GEhMsgyzCTaFz6")
GDP_aze = quandl.get("ODA/AZE_NGDPD", authtoken = "EvzHu2GEhMsgyzCTaFz6")
#pop
pop_aze = quandl.get("ODA/AZE_LP", authtoken = "EvzHu2GEhMsgyzCTaFz6") 
pop_arm = quandl.get("ODA/ARM_LP", authtoken = "EvzHu2GEhMsgyzCTaFz6")
pop_geo = quandl.get("ODA/GEO_LP", authtoken = "EvzHu2GEhMsgyzCTaFz6")





trace_pop_arm = go.Scatter(x=pop_arm.index, y=pop_arm.Value, mode="lines", name = 'Armenia')
trace_pop_geo = go.Scatter(x=pop_arm.index, y=pop_geo.Value, mode="lines", name = 'Georgia')
trace_pop_aze = go.Scatter(x=pop_arm.index, y=pop_aze.Value, mode="lines", name='Azerbaijan')

data_pop=[trace_pop_arm, trace_pop_geo, trace_pop_aze]

layout_pop=dict(title="<b>Population [mln]</b>")
figure_pop = dict(data=data_pop, layout=layout_pop)





inf_index_arm = quandl.get("ODA/ARM_PCPIE", authtoken = "EvzHu2GEhMsgyzCTaFz6")
inf_index_geo = quandl.get("ODA/GEO_PCPIE", authtoken = "EvzHu2GEhMsgyzCTaFz6")
inf_index_aze = quandl.get("ODA/AZE_PCPIE", authtoken = "EvzHu2GEhMsgyzCTaFz6")

ur_aze = quandl.get("ODA/AZE_LUR", authtoken = "EvzHu2GEhMsgyzCTaFz6") 
ur_geo = quandl.get("ODA/GEO_LUR", authtoken = "EvzHu2GEhMsgyzCTaFz6")
ur_arm = quandl.get("ODA/ARM_LUR", authtoken = "EvzHu2GEhMsgyzCTaFz6")


#map 
mapbox_access_token = "pk.eyJ1IjoiZGF2dHlhbiIsImEiOiJjamZiZmhvZjUxc3N4MzNtbW1qaWZ4YW1uIn0.2XsxzZRRCBPquMfU3OsYEQ"

data = go.Data([
    go.Scattermapbox(
        lat=['40.7294371'],
        lon=['44.8387879'],
        mode='markers',
    )
])

layout_map = go.Layout(
    height=600,
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        layers=[
            dict(
                sourcetype = 'geojson',
                source = 'https://raw.githubusercontent.com/greencoder/geobatch/master/georgia.geojson',
                type = 'fill',
                color = "#ff0000"
            ),
            dict(
                sourcetype = 'geojson',
                source = 'https://raw.githubusercontent.com/greencoder/geobatch/master/armenia.geojson',
                type = 'fill',
                color = '#ff9900'
            ),
            dict(
                sourcetype = 'geojson',
                source = 'https://raw.githubusercontent.com/glynnbird/countriesgeojson/master/azerbaijan.geojson',
                type = 'fill',
                color = '#3FBF8E'
            ),
            
        ],
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40,
            lon=43
        ),
        pitch=0,
        zoom=5,
        style='light'
    ),
)

map_graph = dict(data=data, layout=layout_map)


trace_GDP_arm = go.Scatter(x=GDP_arm.index, y=GDP_arm.Value, mode="lines", name = 'Armenia')
trace_GDP_geo = go.Scatter(x=GDP_arm.index, y=GDP_geo.Value, mode="lines", name = 'Georgia')
trace_GDP_aze = go.Scatter(x=GDP_arm.index, y=GDP_aze.Value, mode="lines", name='Azerbaijan')

data_GDP=[trace_GDP_arm, trace_GDP_geo, trace_GDP_aze]

layout_GDP=dict(title="<b>Gross Domestic Product[USD]</b>")
figure_GDP = dict(data=data_GDP, layout=layout_GDP)
