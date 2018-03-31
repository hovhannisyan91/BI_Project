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

#ease
business_geo = quandl.get("WWDI/GEO_IC_BUS_EASE_XQ", authtoken = "EvzHu2GEhMsgyzCTaFz6")
business_arm = quandl.get("WWDI/ARM_IC_BUS_EASE_XQ", authtoken = "EvzHu2GEhMsgyzCTaFz6")
business_aze = quandl.get("WWDI/AZE_IC_BUS_EASE_XQ", authtoken = "EvzHu2GEhMsgyzCTaFz6")
#ur
ur_aze = quandl.get("ODA/AZE_LUR", authtoken = "EvzHu2GEhMsgyzCTaFz6") 
ur_geo = quandl.get("ODA/GEO_LUR", authtoken = "EvzHu2GEhMsgyzCTaFz6")
ur_arm = quandl.get("ODA/ARM_LUR", authtoken = "EvzHu2GEhMsgyzCTaFz6")


#pop graph
trace_pop_arm = go.Scatter(x=pop_arm.index, y=pop_arm.Value, mode="lines", name = 'Armenia')
trace_pop_geo = go.Scatter(x=pop_arm.index, y=pop_geo.Value, mode="lines", name = 'Georgia')
trace_pop_aze = go.Scatter(x=pop_arm.index, y=pop_aze.Value, mode="lines", name='Azerbaijan')
data_pop=[trace_pop_arm, trace_pop_geo, trace_pop_aze]

layout_pop=dict(title="<b>Population [mln]</b>")
figure_pop = dict(data=data_pop, layout=layout_pop)



trace_ur_arm = go.Scatter(x=ur_arm.index, y=ur_arm.Value, mode="lines", name = 'Armenia')
trace_ur_geo = go.Scatter(x=ur_arm.index, y=ur_geo.Value, mode="lines", name = 'Georgia')
trace_ur_aze = go.Scatter(x=ur_arm.index, y=ur_aze.Value, mode="lines", name='Azerbaijan')
data_ur=[trace_ur_arm, trace_ur_geo, trace_ur_aze]

layout_ur=dict(title="<b>Unemployment Rate</b>")
figure_ur = dict(data=data_ur, layout=layout_ur)


trace_business_arm = go.Scatter(x=business_arm.index, y=business_arm.Value, mode="lines", name = 'Armenia')
trace_business_geo = go.Scatter(x=business_arm.index, y=business_geo.Value, mode="lines", name = 'Georgia')
trace_business_aze = go.Scatter(x=business_arm.index, y=business_aze.Value, mode="lines", name='Azerbaijan')
data_business=[trace_business_arm, trace_business_geo, trace_business_aze]

layout_business=dict(title="<b>Business doing index</b>")
figure_business = dict(data=data_business, layout=layout_business)




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
