def dt(nap, kredit, tanulas, intervallum):
    '''
    Ez egy lináris időbeosztás.
    Megmondja mennyit kell intervallumonként hozzáadni a tanulási idődhöz, hogy elérd a követelményeket.

    nap: Megmondod hány napod van még, a vizsgáig
    kredit: Hány kreditet kell előadással vagy önnáló munkával tölteni
    tanulas: Hány órát tanulsz ma
    intervallum: Mekkora intervallumonként akarod változtatni a tanulásodat
    
    '''

    a = 2 * ((kredit * 14)/nap**2 - tanulas/nap)
    return a * intervallum*60


def update_pomodoro_fixed_interval(T, dt, S):
    'returns pomodoro time in hours'
    S /= 24
    x = round(T/dt)
    return 24 * 2 * S / x /(x+1)/dt


def update_pomodoro(T,S):
    pomo = 25/60/24
    S/=24
    x = 2 * S/T/pomo - 1
    dt = T/x
    return dt