from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.plotly as py
import quandl
import cufflinks as cf
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from plotly.grid_objs import Grid, Column
import time
from Project_Figure import figure_pop




#GDP
GDP_arm = quandl.get("ODA/ARM_NGDPD", authtoken = "EvzHu2GEhMsgyzCTaFz6")
GDP_geo = quandl.get("ODA/GEO_NGDPD", authtoken = "EvzHu2GEhMsgyzCTaFz6")
GDP_aze = quandl.get("ODA/AZE_NGDPD", authtoken = "EvzHu2GEhMsgyzCTaFz6")

#GDP_PC
GDP_aze_pc = quandl.get("ODA/AZE_NGDPDPC", authtoken = "EvzHu2GEhMsgyzCTaFz6")
GDP_geo_pc = quandl.get("ODA/GEO_NGDPDPC", authtoken = "EvzHu2GEhMsgyzCTaFz6")
GDP_arm_pc = quandl.get("ODA/ARM_NGDPDPC", authtoken = "EvzHu2GEhMsgyzCTaFz6")


#import/export
import_arm=pd.read_csv("https://raw.githubusercontent.com/hovhannisyan91/BI_Project/master/Import_Geo.csv")
export_arm=pd.read_csv("https://raw.githubusercontent.com/hovhannisyan91/BI_Project/master/Export_Arm.csv")

import_geo=pd.read_csv("https://raw.githubusercontent.com/hovhannisyan91/BI_Project/master/Import_Geo.csv")
export_geo=pd.read_csv("https://raw.githubusercontent.com/hovhannisyan91/BI_Project/master/Export_Geo.csv")

import_aze=pd.read_csv("https://raw.githubusercontent.com/hovhannisyan91/BI_Project/master/Import_Azr.csv")
export_aze=pd.read_csv("https://raw.githubusercontent.com/hovhannisyan91/BI_Project/master/Export_Azr.csv")

#other GDP components
inv_arm = quandl.get("ODA/ARM_NID_NGDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")
inv_geo = quandl.get("ODA/GEO_NID_NGDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")
inv_aze = quandl.get("ODA/AZE_NID_NGDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")


gov_exp_geo = quandl.get("ODA/GEO_GGX_NGDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")
gov_exp_arm = quandl.get("ODA/ARM_GGX_NGDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")
gov_exp_aze = quandl.get("ODA/AZE_GGX_NGDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")
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



app=dash.Dash()


app.css.append_css({"external_url":'https://codepen.io/chriddyp/pen/bWLwgP.css'})
#app.css.append_css({"external_url":'https://codepen.io/khovhannisyan/pen/MVVwKN.css'})

app.title="BI Project"

app.layout=html.Div([
	
	html.Div([
		html.H1("Introduction of Macroeconomic indicators of Transcaucasian countries", style={"color":"darkred", "text-align":"center", "font-family":"cursive",})
	], className="twelve columns", id="menu"),

	html.Div([
		html.Div([
			dcc.Graph(id="pop",  figure=figure_pop),
			], className="four columns"),
		html.Div([
			dcc.Graph(id="ease", figure="")
			], className="four columns"),
		html.Div([
			dcc.Graph(id="ur",)
			], className="four columns"),
	], className="twelve columns"),
	
	
	
	#part 1 moving average
	html.Div([
		html.Div([dcc.Input(id="years",
    		placeholder='Enter a value...',
    		type='number',
		     min=2, max=8,
		),
		], className="twp columns"),

		html.Div([
			dcc.Graph(id="GDP_Graph")
		], className="five columns"),	
		
		html.Div([
			dcc.Graph(id="GDP_Graph_pc")
		], className="five columns")	
		


	], className="twelve columns"),
	
	html.Div([
		
		html.Div([
			dcc.Graph(id="GDP_comp1")
		], className="six columns"),	
		
		html.Div([
			dcc.Graph(id="GDP_comp2")
		], className="six columns")	
		


	], className="twelve columns"),
	
	
#part 3 import/export by country
	html.Div([
		
		html.Div([
			dcc.Dropdown(id = 'option_in', options=[
	            {'label': 'Armenia', 'value': 'arm'},
	            {'label': 'Azerbaijan', 'value': 'aze'},
	            {'label': 'Georgia', 'value': 'geo'}
            ], placeholder='Select the country...'),
		
			], className="two columns"),

		html.Div([
				dcc.Graph(id="import_graph")

		], className="five columns"),	
		
		html.Div([
			
			dcc.Graph(id="export_graph")

								

		], className="five columns")	
	
	], className="twelve columns"),


	
		
])	
###CALLBAKCS
#moving average
@app.callback(
	Output(component_id="GDP_Graph", component_property="figure"),
	[Input(component_id="years", component_property="value")]
)

def update_GDP_graph(input_value1):
	GDP_aze["MA"] = GDP_aze.Value.rolling(input_value1).mean()
	GDP_arm["MA"] = GDP_arm.Value.rolling(input_value1).mean()
	GDP_geo["MA"] = GDP_geo.Value.rolling(input_value1).mean()

	trace_GDP_arm = go.Scatter(x=GDP_arm.index, y=GDP_arm.Value, mode="lines",  marker = dict(color="ff9900"), name = 'Armenia')
	trace_GDP_geo = go.Scatter(x=GDP_arm.index, y=GDP_geo.Value, mode="lines", marker = dict(color="#ff0000"), name = 'Georgia')
	trace_GDP_aze = go.Scatter(x=GDP_arm.index, y=GDP_aze.Value, mode="lines", marker = dict(color="#3FBF8E"), name='Azerbaijan')
	trace_GDP_arm_ma = go.Scatter(x=GDP_arm.index, y=GDP_arm.MA, mode="markers",  marker = dict(color="ff9900"), name = 'Armenia_MA')
	trace_GDP_geo_ma = go.Scatter(x=GDP_arm.index, y=GDP_geo.MA, mode="markers", marker = dict(color="#ff0000"), name = 'Georgia_MA')
	trace_GDP_aze_ma = go.Scatter(x=GDP_arm.index, y=GDP_aze.MA, mode="markers", marker = dict(color="#3FBF8E"), name='Azerbaijan_MA')


	data_GDP=[trace_GDP_arm, trace_GDP_geo, trace_GDP_aze, trace_GDP_arm_ma, trace_GDP_geo_ma, trace_GDP_aze_ma]

	layout_GDP=dict(title="<b>Gross Domestic Product[USD]</b>")

	figure_GDP = dict(data=data_GDP, layout=layout_GDP)

	return figure_GDP



@app.callback(
	Output(component_id="GDP_Graph_pc", component_property="figure"),
	[Input(component_id="years", component_property="value")]
)

def update_GDP_graph(input_value1):
	GDP_aze_pc["MA"] = GDP_aze_pc.Value.rolling(input_value1).mean()
	GDP_arm_pc["MA"] = GDP_arm_pc.Value.rolling(input_value1).mean()
	GDP_geo_pc["MA"] = GDP_geo_pc.Value.rolling(input_value1).mean()

	trace_GDP_arm_pc = go.Scatter(x=GDP_arm_pc.index, y=GDP_arm_pc.Value, marker = dict(color="ff9900"), mode="lines", name = 'Armenia')
	trace_GDP_geo_pc = go.Scatter(x=GDP_arm_pc.index, y=GDP_geo_pc.Value, marker = dict(color="#ff0000"), mode="lines", name = 'Georgia')
	trace_GDP_aze_pc = go.Scatter(x=GDP_arm_pc.index, y=GDP_aze_pc.Value, marker = dict(color="#3FBF8E"), mode="lines", name='Azerbaijan')
	trace_GDP_arm_pc_ma = go.Scatter(x=GDP_arm_pc.index, y=GDP_arm_pc.MA, marker = dict(color="ff9900"), mode="markers", name = 'Armenia_MA')
	trace_GDP_geo_pc_ma = go.Scatter(x=GDP_arm_pc.index, y=GDP_geo_pc.MA, marker = dict(color="#ff0000"), mode="markers", name = 'Georgia_MA')
	trace_GDP_aze_pc_ma = go.Scatter(x=GDP_arm_pc.index, y=GDP_aze_pc.MA,marker = dict(color="#3FBF8E"),  mode="markers", name='Azerbaijan_MA')


	data_GDP_pc=[trace_GDP_arm_pc, trace_GDP_geo_pc, trace_GDP_aze_pc, trace_GDP_arm_pc_ma, trace_GDP_geo_pc_ma, trace_GDP_aze_pc_ma]

	layout_GDP_pc=dict(title="<b>Gross Domestic Product per capita [USD]</b>")
	figure_GDP_pc = dict(data=data_GDP_pc, layout=layout_GDP_pc)

	return figure_GDP_pc

#import
@app.callback(
    Output(component_id='import_graph', component_property='figure'),
    [Input(component_id='option_in', component_property='value')]
)

def update_pie_imp(input_value_2):
	labels_imp = eval("import_"+input_value_2)["Products"]
	values_imp = eval("import_"+input_value_2)["Value(in Millions)"]
	trace_imp=go.Pie(labels=labels_imp, values=values_imp)
	return dict(data=[trace_imp])

#export
@app.callback(
    Output(component_id='export_graph', component_property='figure'),
    [Input(component_id='option_in', component_property='value')]
)

def update_pie_imp(input_value_3):
	labels_exp = eval("export_"+input_value_3)["Products"]
	values_exp = eval("import_"+input_value_3)["Value(in Millions)"]
	trace_exp=go.Pie(labels=labels_exp, values=values_exp)
	return dict(data=[trace_exp])

#gdp_comp1
@app.callback(
	Output(component_id="GDP_comp1", component_property="figure"),
	[Input(component_id="years", component_property="value")]
)

def update_GDP_comp_1(input_value5):
	inv_aze["MA"] = GDP_aze.Value.rolling(input_value5).mean()
	inv_arm["MA"] = GDP_arm.Value.rolling(input_value5).mean()
	inv_geo["MA"] = GDP_geo.Value.rolling(input_value5).mean()

	trace_inv_arm = go.Scatter(x=inv_arm.index, y=inv_arm.Value, mode="lines",  marker = dict(color="ff9900"), name = 'Armenia')
	trace_inv_geo = go.Scatter(x=inv_arm.index, y=inv_geo.Value, mode="lines", marker = dict(color="#ff0000"), name = 'Georgia')
	trace_inv_aze = go.Scatter(x=inv_arm.index, y=inv_aze.Value, mode="lines", marker = dict(color="#3FBF8E"), name='Azerbaijan')
	trace_inv_arm_ma = go.Scatter(x=inv_arm.index, y=inv_arm.MA, mode="markers",  marker = dict(color="ff9900"), name = 'Armenia_MA')
	trace_inv_geo_ma = go.Scatter(x=inv_arm.index, y=inv_geo.MA, mode="markers", marker = dict(color="#ff0000"), name = 'Georgia_MA')
	trace_inv_aze_ma = go.Scatter(x=inv_arm.index, y=inv_aze.MA, mode="markers", marker = dict(color="#3FBF8E"), name='Azerbaijan_MA')


	data_inv=[trace_inv_arm, trace_inv_geo, trace_inv_aze, trace_inv_arm_ma, trace_inv_geo_ma, trace_inv_aze_ma]

	layout_inv=dict(title="<b>Total Investment [GDP]</b>")

	figure_inv = dict(data=data_inv, layout=layout_inv)

	return figure_inv


#gdp_comp2
@app.callback(
	Output(component_id="GDP_comp2", component_property="figure"),
	[Input(component_id="years", component_property="value")]
)

def update_GDP_comp_1(input_value6):
	gov_exp_aze["MA"] = gov_exp_aze.Value.rolling(input_value6).mean()
	gov_exp_arm["MA"] = gov_exp_arm.Value.rolling(input_value6).mean()
	gov_exp_geo["MA"] = gov_exp_geo.Value.rolling(input_value6).mean()

	trace_gov_exp_arm = go.Scatter(x=gov_exp_arm.index, y=gov_exp_arm.Value, mode="lines",  marker = dict(color="ff9900"), name = 'Armenia')
	trace_gov_exp_geo = go.Scatter(x=gov_exp_arm.index, y=gov_exp_geo.Value, mode="lines", marker = dict(color="#ff0000"), name = 'Georgia')
	trace_gov_exp_aze = go.Scatter(x=gov_exp_arm.index, y=gov_exp_aze.Value, mode="lines", marker = dict(color="#3FBF8E"), name='Azerbaijan')
	trace_gov_exp_arm_ma = go.Scatter(x=gov_exp_arm.index, y=gov_exp_arm.MA, mode="markers",  marker = dict(color="ff9900"), name = 'Armenia_MA')
	trace_gov_exp_geo_ma = go.Scatter(x=gov_exp_arm.index, y=gov_exp_geo.MA, mode="markers", marker = dict(color="#ff0000"), name = 'Georgia_MA')
	trace_gov_exp_aze_ma = go.Scatter(x=gov_exp_arm.index, y=gov_exp_aze.MA, mode="markers", marker = dict(color="#3FBF8E"), name='Azerbaijan_MA')


	data_gov_exp=[trace_gov_exp_arm, trace_gov_exp_geo, trace_gov_exp_aze, trace_gov_exp_arm_ma, trace_gov_exp_geo_ma, trace_gov_exp_aze_ma]

	layout_gov_exp=dict(title="<b>Government expenditure [GDP]</b>")

	figure_gov_exp = dict(data=data_gov_exp, layout=layout_gov_exp)

	return figure_gov_exp

if __name__=='__main__':
	app.run_server(debug=True)


