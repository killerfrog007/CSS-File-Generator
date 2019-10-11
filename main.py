#Dimitry Maizik | Oct, 10, 2019
import random
fonts = ["Arial", "Helvetica", "sans-serif", "Gadget", "cursive", "Impact", "Charcoal", "Tahoma", "Geneva", "Verdana", "\"Courier New\"", "\"Lucida Console\"", "\"Trebuchet MS\"", "\"Lucida Sans Unicode\"", "\"Lucida Grande\"", "\"Comic Sans\""]
hexdict = ["1", "2", "3", "4", "5", "6", "7", "8", "9","A", "B", "C", "D", "E", "F"]
START_WIDTH = 8 #Smallest width in px to start the media queries
END_WIDTH = 1920 #Largest width in px to end media querying


def generate_colorcode():
    hexdigit = "#"
    for x in range(6):
        hexdigit = hexdigit + hexdict[random.randint(0, 14)]
    return hexdigit

def generate_font():
    returnfont = ""
    returnfont = fonts[random.randint(0, 15)]
    return returnfont

f_append = ""
i = START_WIDTH
while i <= END_WIDTH:
    print("Generating @Media for " + str(i) +" Px")
    css = "@media screen and (min-width: "+str(i)+ "px) {h1 { font-family: " +str(generate_font()) + ";  background-color: " + str(generate_colorcode()) + ";  color: " + str(generate_colorcode()) + "; } h2 {  font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + ";  color: " + str(generate_colorcode()) + ";} h3 { font-family: " +str(generate_font()) + ";  background-color: " + str(generate_colorcode()) + ";  color: " + str(generate_colorcode()) + "; } h4{ font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}h5{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}h6{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}p{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}hr{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}a{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}ul{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}ol{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}li{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}img{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}div{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}span{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}}" 

    f_append = f_append + css
    i = i+1


#print(f_append)
f = open("style.css", "w")
f.write(f_append)
