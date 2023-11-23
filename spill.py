import pygame, random

# Klasser

class Matbit:
    def __init__(self):
        self.bilde = pygame.image.load("bilder/rsz_burger.png").convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = random.randint(0, BREDDE)
        self.ramme.centery = random.randint(0, HOYDE)

    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)

class Celle:
    def __init__(self, navn: str, radius: int, bildesti: str, x: int, y: int, farge: str):
        self.navn = navn
        self.radius = radius
        self.bilde_original = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde_original, (self.radius * 2, self.radius * 2))
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centery = y
        self.farge = farge 
    
    def beveg(self, mus_x: int, mus_y: int ):
        #self.ramme.centerx = mus_x
        #self.ramme.centery = mus_y

        if mus_x > self.ramme.centerx:
            self.ramme.centerx += 1
        elif mus_x < self.ramme.centerx:
            self.ramme.centerx -= 1

        if mus_y > self.ramme.centery:
            self.ramme.centery += 1
        elif mus_y < self.ramme.centery:
            self.ramme.centery -= 1

    
    def spis(self, motspiller=None):
        print("spis")
        if motspiller:
            self.radius += motspiller.radius
        else: 
            self.radius += 1

        self.oppdater_bilde()

    def bli_spist(self):
        self.radius = 10
        self.oppdater_bilde()

    def oppdater_bilde(self):
        self.bilde = pygame.transform.scale(self.bilde_original,(self.radius * 2, self.radius * 2))
        gammel_x = self.ramme.centerx
        gammel_y = self.ramme.centery
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = gammel_x
        self.ramme.centery = gammel_y

    def tegn(self, vindu):
        pygame.draw.circle(vindu, self.farge, (self.ramme.centerx, self.ramme.centery), self.radius + 4)
        vindu.blit(self.bilde, self.ramme)
    

# 1. Oppsett 
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE,HOYDE))
klokke = pygame.time.Clock()

poeng_font = pygame.font.SysFont("Arial", 32)
poeng = 0
poeng_surface = poeng_font.render(str(poeng), True, "black")


spiller = Celle("Eple", 30, "bilder/kimmern.png", 100, 200, "red")
matbit = Matbit()

motspillere = [
    Celle("Cherry", 22, "bilder/trump.png", 500, 400, "pink"),
    Celle("Blomst", 50, "bilder/russia.png", 50, 400, "yellow"),
    Celle("Banan", 30, "bilder/german.png", 400, 300, "darkblue")
]

matbiter = []

for _ in range(10):
    matbiter.append(Matbit())






while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    mus_x, mus_y = pygame.mouse.get_pos()

    # 3. Oppdatere spill

    spiller.beveg(mus_x, mus_y)

    for i in range(len(motspillere) -1, -1, -1):
        if spiller.ramme.colliderect(motspillere[i].ramme):
            if spiller.radius > motspillere[i].radius:
                print("spis motstander")
                poeng += 5
                poeng_surface = poeng_font.render(str(poeng), True, "black")
                spiller.spis(motspillere[i])
                motspillere.pop(i)
                

            elif spiller.radius < motspillere[i].radius:
                print("bli spist")
                poeng = 0
                poeng_surface = poeng_font.render(str(poeng), True, "black")
                spiller.bli_spist()
        
    for i in range(len(matbiter) - 1, -1, -1):
        if spiller.ramme.colliderect(matbiter[i].ramme):
            poeng += 1
            poeng_surface = poeng_font.render(str(poeng), True, "black")
            spiller.spis()
            matbiter.pop(i)

    # 4. Tegn 
    vindu.fill("white")
    spiller.tegn(vindu)
    vindu.blit(poeng_surface, (550, 10))
    
    for motspiller in motspillere:
        motspiller.tegn(vindu)
    
    for matbit in matbiter:
        matbit.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)