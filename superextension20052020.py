sales = {
     "John" : {
        "N" : 3056,
        "S" : 8463,
        "E" : 8441,
        "W" : 2694
        },
      "Tom" : {
        "N" : 4832,
        "S" : 6786,
        "E" : 4737,
        "W" : 3612
        },
     "Anne" : {
        "N" : 5239,
        "S" : 4802,
        "E" : 5820,
        "W" : 1859
        },
    "Fiona" : {
        "N" : 3904,
        "S" : 3645,
        "E" : 8821,
        "W" : 2451
        }
}



name = input("Select a name: John, Tom, Anne or Fiona: ")
region = input("Select a region: N, S, E or W: ")

if name == "John" or "Tom" or "Anne" or "Fiona" and region == "N" or "S" or "E" or "W":
    print("Sales for {} in {} is {}.".format(name, region, sales.get(name).get(region)))

alt_name = input("Select a name: John, Tom, Anne or Fiona: ")
alt_region = input("Select a region that you would like to change: ")
newfigure = int(input("Enter your new sales figure: "))

if alt_name == "John" or "Tom" or "Anne" or "Fiona" and alt_region == "N" or "S" or "E" or "W":
    sales[alt_name][alt_region] = newfigure
    print("Updated sales for {} are {}.".format(alt_name, sales.get(alt_name)))
    


 


