class Button():
    def __init__(self, image, pos, text_input, font, base_colour, hovering_colour): #pos is a list -> pos[0] is x coordinate and pos[1] is y coordinate
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_colour, self.hovering_colour = base_colour, hovering_colour #because colour of text should change if mouse hovers over it
        self.text_input = text_input
        self.text = self.font.render (self.text_input, True, self.base_colour) #apply font to text

        if self.image is None:
                self.image = self.text #no underlying image, only text is button

        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect (center =(self.x_pos, self.y_pos)) #create rectangle for text surface


    def update (self, screen):
        if self.image is not None:
            screen.blit(self.image,self.rect) #surface for button if it has an underlying image
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom): 
            return True #if mouse hovers within the bounds of the button
        return False

    def changeColour(self,position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_colour) #changing font colour 

        else:
            self.text = self.font.render(self.text_input, True, self.base_colour) #jo colour tha waisa hi hai
