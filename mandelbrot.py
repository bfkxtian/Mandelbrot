import PIL.Image,colorsys,tkinter
#a slow, but small mandelbrot rendering engine...

#   TODO
#   i) Implement tkinter (see imports) for simple GUI to edit viewfield
#   ii) Make algorithm either j) faster or jj) chunked
#   iii) Implement faster algorithms using numpy

#image resolution - be careful
size=200
width,height=3*size,2*size #ensures image is scaled correctly

iters=90 #this provides best color sweep, but is expensive
x,y=-2,-1 #starting values for x/y
xr,yr=3,2 #ranges of x/y values
base_color=0.6 #rotates base color - changes palette

#computes mandelbrot color
def mandelbrot(c):
    z=0
    for i in range(iters):
        if abs(z)>2:
            return tuple(round(i*255) for i in colorsys.hsv_to_rgb(i*4/360+base_color,1,1))
        z=z*z+c #next iteration
    return (0,0,0)

#pillow library code
img=PIL.Image.new("RGB",(width,height)) #create image in memory
pixels=img.load() #load drawing module for image

#compute color of each pixel
for w in range(width):
    p=(w/width)*100
    if p%1==0:
        print("Percentage = {}%".format(p))
    re=x+(w*xr/width) #real component
    for h in range(height):
        im=y+(h*yr/height) #imaginary component
        pixels[int(w),int(h)]=mandelbrot(complex(re,im)) #draw pixel

print("Saving image...")
img.save("Mandelbrot.png".format(x,y,xr,yr,iters))
print("Done!")
