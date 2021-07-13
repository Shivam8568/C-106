import plotly.express as px 
import csv
import numpy as np 
def plotfigure ():
    with open ("Data2.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks", y = "Days")
        fig.show()
def getdatasource(datapath):
    Marks= []
    Days = []
    with open (datapath) as csv_file:
        csvreader = csv.DictReader(csv_file)
        for row in csvreader:
            Marks.append(float(row["Marks"]))
            Days.append(float(row["Days"]))
    return {"x":Marks,"y": Days}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print ("correlation", correlation[0,1])
def setup():
    datapath = "Data2.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)
    plotfigure()
setup()