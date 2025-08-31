def exif2Medford():
    from exif import Image
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename()
    fstubb=filename.split("/")[-1]
    with open(filename, 'rb') as image_file:
        my_image = Image(image_file)
    fname2=filename+".mfd"
    out=open(fname2,"w")
    out.write("@MEDFORD description\n@MEDFORD-Version 2.0\n\n")
    out.write("@exif "+ fstubb+"\n")
    for h in my_image.list_all():
        temp=""
        temp=str(my_image.get(h))
        if(len(temp)<1):
            temp="NA"
        #print(h)
        out.write("@exif-"+h+" "+temp+"\n")
    out.close()

exif2Medford()
