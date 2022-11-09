import imghdr

# path = 'C:/Users/falak/Documents/GitHub/SENG696/ImageProcessing/cat.jpeg'
# print (imghdr.what(path))

def FileVerification(abc):
    verification = 1
    fileTypes = ['jpeg', 'jpg', 'png']
    for t in fileTypes:
        if abc == t:
            verification = 0
            break
    return verification