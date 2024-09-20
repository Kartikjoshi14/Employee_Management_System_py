
    img = drawALL(img, buttonList)

    if hands:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
    
            if x< hands[8][0] < x+w: