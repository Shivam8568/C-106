import plotly.express as px 
import csv
import numpy as np 
def plotfigure ():
    with open ("Data1.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee", y = "Sleep")
        fig.show()
def getdatasource(datapath):
    Coffee= []
    Sleep = []
    with open (datapath) as csv_file:
        csvreader = csv.DictReader(csv_file)
        for row in csvreader:
            Coffee.append(float(row["Coffee"]))
            Sleep.append(float(row["Sleep"]))
    return {"x":Coffee,"y": Sleep}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print ("correlation", correlation[0,1])
def setup():
    datapath = "Data1.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)
    plotfigure()
setup()