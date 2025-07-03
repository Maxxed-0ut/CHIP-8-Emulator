import pygame

def instruction(self, opcode):
    self.pc += 2
    x = (opcode & 0x0F00 ) >> 8
    y = (opcode & 0x00F0) >> 4

def mapping(self, opcode):
    match (opcode & 0xF000):
        case 0x0000:
            match (opcode):

                case 0x00E0:
                    self.renderer.clear()
                    return
                
                case 0x00EE:
                    self.pc = self.stack.pop()
                    return

            
        case 0x1000:
            self.pc = (opcode & 0xFFF)
            return
        case 0x2000:
            self.stack.push(self.pc)
            self.pc = (opcode & 0xFFF)
    
            return 
        case 0x3000:
            if (self.v[x] ==(opcode & 0xFF)):

                self.pc += 2
            return
        case 0x4000:


        