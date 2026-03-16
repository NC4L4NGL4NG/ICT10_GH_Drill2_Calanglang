from pyscript import document, display

def area_triangle(base, height):
    return {'base': base, 'height': height}

def computing_area(e):
    output_div = document.getElementById('display1')
    output_div.innerHTML = ""

    base1 = int(document.getElementById('input1').value)
    height1 = int(document.getElementById('input2').value)


    area67 = (base1 * height1) / 2

    triangle_info = area_triangle(base1, height1)

    display(f'Base: {base1}, Height: {height1}. The area is {area67}', target='display1')