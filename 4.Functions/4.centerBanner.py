# *******************************************************************
#       .center function / centering text items                     #
# *******************************************************************

def banner_text(text: str = " ", width: int = 80) -> None:
    """
    takes in a string and centered it with asteriks in the end
    :param text: input string
    :param width: space that should be on the left and right
    :return: None, but prints out the centered string
    """
    text = text[:]
    screen_width = width
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


# output of banner_tex("string")
# print("banner_text docstring: ")
# print(banner_text.__doc__)
help(banner_text)
banner_text("*", 66)
banner_text("Always look on the bright side of life...", 66)
banner_text("If life seems jolly rotten,", 66)
banner_text("There's something you've forgotten", 66)
banner_text("And that's to laugh and smile and dance and sing,", 66)
banner_text(width=66, text=" ")  # swap positions but same keywords
banner_text("When you're feeling in the dumps,", 66)
banner_text("Don't be silly chumps,", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of lif...", 66)
banner_text("*", 66)
