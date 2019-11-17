
from flask import Flask, request, jsonify           # import flask
import re
import pandas as pd
from flask_cors import CORS 
import json


accidents_report = pd.read_csv('accidents_report.csv')

accidents_report['Date'] = pd.to_datetime(accidents_report['Actual_DateOf_Occurance'], format="%Y-%m-%d")
accidents_report = accidents_report.dropna(subset = ['Date'])
accidents_report['Year'] = accidents_report.Date.dt.year.astype('int')
accidents_report['Month'] = accidents_report.Date.dt.month.astype('int')
accidents_report['Weekday'] = accidents_report.Date.dt.weekday.astype('int')

accidents_greater_2011 = accidents_report[accidents_report['Year']>2013]
accidents_greater_2011 = accidents_greater_2011[accidents_greater_2011['Year']<2019]

months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug','Sept', 'Oct', 'Nov', 'Dec']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
years = [i for i in range(2014, 2019)]

app = Flask(__name__)             # create an app instance
CORS(app)

@app.route("/", methods=['GET', 'POST'])                   # at the end point /
def hello():                      # call method hello 
    content = request.json
    
    col = content['col']
    graph_type = content['graph_type']
    
    if graph_type == 'heatmap':
        row = content['row']
        if col == 'Weekday':
            accidents_greater_2011['Weekday'] = accidents_greater_2011.Date.dt.weekday.astype('int')
            accident_table = accidents_greater_2011.groupby(['Year', 'Weekday']).size().unstack('Weekday')
            accident_table_list = accident_table.values.tolist()
            returnJson = {'cols':days,
                         'rows': years,
                         'values': accident_table_list,
                         'graph_type': 'heatmap',
                         'title': 'Accidents by Years and Days'}
            return jsonify(returnJson)
        else:
            accidents_greater_2011['Month'] = accidents_greater_2011.Date.dt.month.astype('int')
            accident_table = accidents_greater_2011.groupby(['Year', 'Month']).size().unstack('Month')
            accident_table_list = accident_table.values.tolist()
            returnJson = {'cols':months,
                         'rows': years,
                         'values': accident_table_list,
                         'graph_type': 'heatmap',
                         'title': 'Accidents by Years and Months'}
            return jsonify(returnJson)
    elif graph_type == 'pie':
        bd = accidents_report[col].value_counts()
        bd = dict(bd)
        for k,v in bd.items():
            bd[k] = str(v)
        
        returnJson = {'graph_type': 'pie',
                      'data': bd,
                     'title':col}
        return jsonify(returnJson)
    
    elif graph_type == 'multibar':
        '''
        data = []
        acc_grpd = accidents_report.groupby([col[0], col[1]]).size()
        for c in col:
            bd = accidents_report[c].value_counts()
            bd = dict(bd)
            for k,v in bd.items():
                bd[k] = str(v)
            data.append({'data':bd, 'title':c})

        returnJson = {'graph_type': 'multibar',
                      'data': data,
                     'title':' and '.join(col)}
        '''
        data = []
        acc_grpd = accidents_report.groupby([col[0], col[1]]).size().unstack(col[1]).to_json()
        acc_grpd = json.loads(acc_grpd)
        for col0_field in acc_grpd:
           bd = acc_grpd[col0_field]
           for k,v in bd.items():
               if v == None:
                   bd[k] = str(0)
               else:
                   bd[k] = str(v)
           data.append({'data':bd, 'title':col0_field})

        returnJson = {'graph_type': 'multibar',
                'data': data,
                'title':' and '.join(col)}
        return jsonify(returnJson)
    
    elif graph_type == 'scatteredline':
        accident_report = accidents_greater_2011
        accident_report['year'] = accident_report['Date'].dt.year
        accident_report['month'] = accident_report['Date'].dt.month
        #accident_report['weekday'] = accident_report['Actual_DateOf_Occurance'].dt.weekday
        accident_report['day'] = accident_report['Date'].dt.day
        accident_report['hour'] = accident_report['Date'].dt.hour
        
        accident_report = accident_report[["year", "month", "Date"]]
        ymwdh = accident_report[accident_report["year"] > 2014]
        ymwdh = ymwdh[ymwdh["year"]<2019]
        
        ymwdh = ymwdh.groupby(["year", "month"]) 
#         dates = accident_report.groupby("Date")#["Date"].tolist()[:500]
        
        inout_df = ymwdh.size().reset_index(name="count")
        
        count_list = inout_df['count'].tolist()[:500]
        year_list = inout_df['year'].tolist()[:500]
        month_list = inout_df['month'].tolist()[:500]
        
        count_list = list(map(str, count_list))
        
        returnJson = {'graph_type': 'scatteredline',
                     'years': year_list,
                      'months': month_list,
                     'values': count_list }
        return jsonify(returnJson)

            
            
            
    return "Hello World!"         # which returns "hello world"

@app.route("/column_stats", methods=['GET', 'POST'])
def column_stats():
    content = request.json
    col = content['col']
    bd = accidents_report[col].value_counts()
    bd = dict(bd)
    returnJson = {'graph_type': 'pie',
                  'data': bd}
    return jsonify(returnJson)
    
if __name__ == "__main__":        # on running python app.py
    app.run(host='0.0.0.0',port='8000')