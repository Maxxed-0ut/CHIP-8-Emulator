import pygame

def mapping(self, opcode):

    self.pc += 2
    x = (opcode & 0x0F00 ) >> 8
    y = (opcode & 0x00F0) >> 4
    
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
            if (not self.v[x] == (opcode & 0xFFF)):

                self.pc +=2

            return
        
        case 0x5000:
            if(self.v[x] == self.v[y]):

                self.pc += 2

            return
        
        case 0x6000:
            self.v[x] = (opcode & 0x0FF)

            return
        
        case 0x7000:
            self.v[x] += (opcode & 0x0FF)

            return
        
        case 0x8000:
            match (opcode & 0xF):

                case 0x0:
                    self.v[x] = self.v[y]

                    return
                  
                case 0x1:
                    self.v[x] = self.v[x] | self.v[y]

                    return
                
                case 0x2:
                    self.v[x] = self.v[x] & self.v[y]

                    return
                
                case 0x3:
                    self.v[x] = self.v[x] ^ self.v[y]

                    return
                case 0x4:
                    
                    self.v[0xF] = 0

                    if((self.v[x]+ self.v[y]) > 0xFF):
                        self.v[0xF] = 1

                    self.v[x] = self.v[x]+ self.v[y]
                    return
                case 0x5:
                    return
                case 0x6:
                    return
                case 0x7:
                    return
                case 0xE:
                    return

           
        case 0x9000:
            return
        case 0xA000:
            return
        case 0xB000:
            return
        case 0xC000:
            return
        case 0xD000:
            return
        case 0xE000:
            return
        case 0xF000:
            return

        