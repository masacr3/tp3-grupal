def KML (archivo, grafo=None):

    MartoGato = "Marto gato"

    ciudades = ["Moscu,55.755833,37.617778",
              "San Petesburgo,59.950000,30.316667",
              "Kaliningrado,54.716667,20.500000",
              "Kazan,55.790833,49.114444",
              "Nizhni Novgorod,56.326944,44.007500",
              "Volgogrado,48.700000,44.483333",
              "Samara,53.183333,50.116667",
              "Sochi,43.585278,39.720278",
              "Saransk,54.183333,45.183333",
              "Rostov del Don,47.233333,39.716667",
              "Ekaterinburgo,56.833333,60.583333"]

    f = open(archivo, "w")

    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f.write("<kml xmlns=\"http://earth.google.com/kml/2.1\">\n")
    f.write("<Document>\n")
    f.write("\t<name>"+ MartoGato +"</name>\n")

    con = {}

    for ciudad in ciudades:

        #espliteo gracias python
        cede , posx , posy = ciudad.split(",")

        #No le des bola es para un experimento
        con[cede] = posx +","+posy

        f.write("\t<Placemark>\n")
        f.write("\t\t<name>" + cede + "</name>\n")
        f.write("\t\t<description>" + cede + "</description>\n")
        f.write("\t\t<Point>\n")
        f.write("\t\t\t<coordinates>" + posx + ", " + posy + "</coordinates>\n")
        f.write("\t\t</Point>\n")
        f.write("\t</Placemark>\n")

    f.write("</Document>\n")
    f.write("</kml>\n")

    f.close()

    #esto es mas para una controlar la salida de consola
    print("archivo")
    for ciudad in ciudades:
        print(ciudad)

    # para el tema de duplicado de conectores
    print("\n\nConecciones")
    for cede in con:
        print(cede," ",con[cede])

    print("OK")

KML("ej.kml")
