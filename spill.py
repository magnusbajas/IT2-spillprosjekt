import pygame, random

# Klasser

class Matbit:
    def __init__(self):
        self.bilde = pygame.image.load("bilder/eple.webp").convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = random.randint(0, BREDDE)
        self.ramme.centery = random.randint(0, HOYDE)

    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)

class Celle:
    def __init__(self, navn: str, radius: int, bildesti: str, x: int, y: int):
        self.navn = navn
        self.radius = radius
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (self.radius * 2, self.radius * 2))
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centery = y
    
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

    
    def spis():
        pass

    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)


        

# 1. Oppsett 
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE,HOYDE))
klokke = pygame.time.Clock()


eple = Celle("Eple", 30, "bilder/eple.webp", 100, 200)
cherry = Celle("Cherry", 22, "bilder/cherry.webp", 500, 400)
matbit1 = Matbit()
matbit2 = Matbit()



while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    mus_x, mus_y = pygame.mouse.get_pos()

    # 3. Oppdatere spill

    eple.beveg(mus_x, mus_y)

    # 4. Tegn 
    vindu.fill("white")
    eple.tegn(vindu)
    cherry.tegn(vindu)
    matbit1.tegn(vindu)
    matbit2.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)