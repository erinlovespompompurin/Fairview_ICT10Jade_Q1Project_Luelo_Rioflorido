from pyscript import display, document


def create_order(e):
    document.getElementById("output1").innerHTML = ""

    prod1 = document.getElementById("item1")
    subtotal = float(prod1.value) * prod1.checked

    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)

    grandtotal = subtotal + price

    display(subtotal, target="output1")


def place_order(e):
    document.getElementById("output1").innerHTML = ""

    brew = document.getElementById("chewy")
    brew_price = float(brew.value)

    display(brew_price, target="output1")


def generate_sku(e):
    document.getElementById("output1").innerHTML = ""

    category = document.getElementById("category").value
    product = document.getElementById("product").value
    stock = document.getElementById("stock").value

    sku = category[:3].upper() + "-" + product[:4].upper() + "-" + str(stock)

    display("SKU: ", sku, target="output1")