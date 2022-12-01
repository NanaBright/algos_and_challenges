def coinster(dx):
    dy = 0
    for i in dx.coin():
        if i == "p":
            dy += 0.01
        if i == "n":
            dy += 0.05
        if i == "d":
            dy += 0.10
        if i == "q":
            dy += 0.25
    
    return dy
    


#coinstar('nNpPqQdD')
