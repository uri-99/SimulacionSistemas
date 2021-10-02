from particle import Particle
dt = 10**-1
particle = Particle(dt)
verletParticle = Particle(dt)
beemanParticle = Particle(dt)
gearParticle = Particle(dt)

#positions:
analytic = [particle.x]
# particle.advance()

verlet = [verletParticle.x]
# verletParticle.advance()

beeman = [beemanParticle.x]
beemanAcc = [beemanParticle.r2()]
# beemanParticle.advance()

gear = [gearParticle.x]

while particle.t < particle.tf:
    #analytic:
    analytic.append(particle.solucion_analitica())
    particle.advance()

    #verlet:
    if len(verlet) == 1:
        verlet.append(verletParticle.Euler_r())
    else:
        verlet.append(verletParticle.Verlet_r(verlet))
    verletParticle.advance()

    #beeman
    x, acc = beemanParticle.Beeman()
    beeman.append(x)
    beemanAcc.append(acc)

    #gear
    gear.append(gearParticle.Gear()) ##no estoy seguro que debería retornar esto


print(analytic)
print(verlet)
print(beeman)
print(gear)



