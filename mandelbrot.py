import PIL.Image,colorsys,numpy
#a slow, but small mandelbrot rendering engine...

#notes: i would like to make this faster by using numpy, but it doesnt make any difference

#image resolution - be careful
size=25000
width,height=3*size,2*size #ensures image is scaled correctly

iters=90 #higher values give nicer color sweep, but is more expensive
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

img=PIL.Image.new("RGB",(width,height)) #create image in memory
pixels=img.load() #load drawing module for image

#compute color of each pixel
for w in numpy.arange(width):
    print("Row = {}/{}".format(w,width))
    re=x+(w*xr/width) #real component
    for h in numpy.arange(height):
        im=y+(h*yr/height) #imaginary component
        pixels[int(w),int(h)]=mandelbrot(complex(re,im)) #draw pixel

print("Saving image...")
img.save("Mandelbrot.png".format(x,y,xr,yr,iters))
print("Done!")
