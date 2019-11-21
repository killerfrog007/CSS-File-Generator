#Dimitry Maizik | Oct, 10, 2019
import random
fonts = ["\"Agency FB\"", "Albertina", "Antiqua", "Archetect", "Arial", "BankFuturistic", "BankGothic", "Blackletter", "Blagovest", "Calibri", "\"Comic Sans MS\"", "Consolas", "Courier", "Cursive", "Decorative", "Fantasy", "Fraktur", "Frosty", "Garamond", "Geogia", "Helvetica", "Impact", "Minion", "Monospace", "Perpetua", "Roman", "Sans-serif", "Serif", "Script", "Swiss", "Times", "\"Times New Roman\"", "Verdana"]
hexdict = ["1", "2", "3", "4", "5", "6", "7", "8", "9","A", "B", "C", "D", "E", "F"]
START_WIDTH = 710 #Smallest width in px to start the media queries
END_WIDTH = 720 #Largest width in px to end media querying
START_HEIGHT  = 710 #Smallest height in px to start the media queries
END_HEIGHT = 720 #Largest height in px to start the media queries

def generate_colorcode():
    hexdigit = "#"
    for x in range(6):
        hexdigit = hexdigit + hexdict[random.randint(0, 14)]
    return hexdigit

def generate_font():
    returnfont = ""
    returnfont = fonts[random.randint(0, 32)]
    return returnfont

f_append = ""
i = START_WIDTH
while i <= END_WIDTH:
    j = START_HEIGHT
    while j <= END_HEIGHT:
        print("Generating @Media for " + str(i) + " Px " + str(j) + " Px")
        css = "@media screen and (min-width: " + str(i) + "px), screen and (min-height: " + str(j) + "px) {h1 { font-family: " +str(generate_font()) + ";  background-color: " + str(generate_colorcode()) + ";  color: " + str(generate_colorcode()) + "; } h2 {  font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + ";  color: " + str(generate_colorcode()) + ";} h3 { font-family: " +str(generate_font()) + ";  background-color: " + str(generate_colorcode()) + ";  color: " + str(generate_colorcode()) + "; } h4{ font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}h5{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}h6{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}p{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}hr{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}a{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}ul{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}ol{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}li{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}img{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}div{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}span{font-family: " +str(generate_font()) + "; background-color: " + str(generate_colorcode()) + "; color: " + str(generate_colorcode()) + ";}}" 

        j = j+1
        f_append = f_append + css
    i = i+1


#print(f_append)
f = open("style.css", "w")
f.write(f_append)
