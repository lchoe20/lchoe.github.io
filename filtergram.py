import filters

def main():
    # ask what image the user wants to edit
    filename = input("Enter the name of the file you want to edit")

    # import the image
    img = filters.load_img(filename)
    # filters.show_img(img)
    # save the final image
    filters.save_img(img, "recolored.jpg")
    filters.obamicon(img)

if __name__ == "__main__":
    main()
