import math

from PIL import Image
from PIL import ImageFilter

# Define float-step compatible range function
def frange(a, b, step):
    while a < b:
        yield a
        a += step

def main():
    # Define width, height & threshold for f
    __width__ = 1000
    __height__ = 1000

    __h_step__ = 4.0 / (__height__)
    __w_step__ = 4.0 / (__width__)

    __threshold__ = 2
    __max_iteration__ = 1000

    # Define complex function
    f = lambda z: z*z + 0.285

    sc_lst = []
    mi = 0
    
    # Iterate
    for w in frange(-2, 2, __w_step__):
        for h in frange(-2, 2, __h_step__):
            z  = complex(h, w)
            sc = math.exp(-abs(z))
            it = 0

            while abs(z) < __threshold__ and it < __max_iteration__:
                z = f(z)
                it += 1
                sc += math.exp(-abs(z))

            # Save the highest iteration done
            if it > mi:
                mi  = it
            
            sc_lst.append(sc)

    pixels = []

    # Give it some color
    for sc in sc_lst:
        b = 0.5 + 0.5 * (math.sin(sc * 0.1))
        r = b**3
        g = b**2
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        pixels.append((r, g, b))

    # Save image
    image = Image.new('RGB', (__width__, __height__))
    image.putdata(pixels)

    image.save("image.png")

if __name__ == '__main__': 
    main()

