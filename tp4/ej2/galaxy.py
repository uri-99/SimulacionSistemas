from ej2.object import Object

class Galaxy:

    G = 6.67384 * 10**-11 #N m**2 kg**-2
    dt = 1
    t=0
    
    earth_initial_pos = (1.500619962348151e8, 2.288499248197072e6)
    earth_initial_speed = (-9.322979134387409e-1, 2.966365033636722e1)
    mars_initial_pos = (-2.426617401833969e8, -3.578836154354768e7)
    mars_initial_speed = (4.435907910045917e0, -2.190044178514185e1)
    sun_initial_position = (0, 0)
    sun_initial_speed = (0, 0)

    # angulos de diferencia para que esten alineados la tierra y la nave con respecto al sol
    alignment_condition = 2
    
 #  Planet = Object(radius, mass, coords, speed, initT, dt)   #km, kg, [posX, posY], [speedX, speedY], t, dt 
    Earth = Object(6371, 5.97*10**24, earth_initial_pos, earth_initial_speed, t, dt)
    Mars = Object(3390, 6.4171*10**23, mars_initial_pos, mars_initial_speed, t, dt)
    Sun = Object(696000, 1988500*10**24, [0, 0], 0, 0, t, dt)
    Ship = null
    system=[Sun, Earth, Mars]



    def __init__(self, shipCoords):
        self.Ship = Object(radius, 2*10**5, shipCoords, 7.12, self.t, self.dt, self.system) #1500km de la superficie y 7.12 km/s
        # V0 = 8 km/s (sumada a las velocidad orbital total que ya tiene la nave antes del despegue, dada por la velocidad de la tierra mas la velocidad de la estación espacial)

    def advance(self): 
        self.Earth.changePosition()
        self.Mars.changePosition()
        self.Ship.changePosition()
        if(self.shipTimeToTakeOff()):
            # cambiar speed de ship ya que despega

     # calcular si estan alineados
    def shipTimeToTakeOff(self):
        ship_angle = self.Ship.angle_to_object()
        earth_angle = self.Earth.angle_to_object()
        if(math.fabs(ship_angle - earth_angle) >= alignment_condition):
            return True
        return False