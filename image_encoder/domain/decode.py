from image_encoder.domain.image_functions import read_image

def decode(image_name):

    img = read_image(image_name)
    data = ''
    img_data = iter(img.getdata())
    while (True):
        pixels = [value for value in img_data.__next__()[:3] +
                                img_data.__next__()[:3] +
                                img_data.__next__()[:3]]
 
        # string of binary data
        binstr = ''
 
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        
        if (pixels[-1] % 2 != 0):
            return data