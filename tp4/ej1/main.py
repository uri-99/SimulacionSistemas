from particle import Particle
dt = 10**-3
analyticParticle = Particle(dt)
verletParticle = Particle(dt)
beemanParticle = Particle(dt)
gearParticle = Particle(dt)

#positions:
analytic = [analyticParticle.x]
# particle.advance()

verlet = [verletParticle.x]
# verletParticle.advance()

beeman = [beemanParticle.x]
# beemanParticle.advance()

gear = [gearParticle.x]

while analyticParticle.t < analyticParticle.tf:
    #analytic:
    # analytic.append(analyticParticle.solucion_analitica())
    print("A ", analyticParticle.solucion_analitica())
    analyticParticle.advance()

    #verlet:
    if len(verlet) == 1:
        verlet.append(verletParticle.Euler_r())
    else:
        # verlet.append(verletParticle.Verlet_r())
        print("V ", verletParticle.Verlet_r())
    verletParticle.advance()

    #beeman
    # beeman.append(beemanParticle.Beeman())
    print("B ", beemanParticle.Beeman())
    beemanParticle.advance()

    #gear
    # gear.append(gearParticle.Gear())
    print("G ", gearParticle.Gear())
    gearParticle.advance()
    print()


print(analytic)
print(verlet)
print(beeman)
print(gear)



