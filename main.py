
from pyscript import display, document

def create_order(e):
  document.getElementById("output1").innerHTML = "" 

    prod1 = document.getElementbyId("item1") 
    subtotal = float(prod1.value) * prod1.checked
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    grandtotal = subtotal + price
    display(subtotal, target="output1")

def place_order(e):
        document.getElementById("output1").innerHTML = "" 

        brew = document.getElementbyId("chewy")
        brew_price = float(chewy.value)
        display(chewy_price, target ="output1")
        document.getElementById("").checked:
        upsize_price = float(document.getElementById("chewy").value)
