class stego():
    def __init__(self, original):
        # image and iterating values
        self.image = original
        self.height, self.width, self.channels = original.shape
        self.w = 0
        self.h = 0
        self.chan = 0 
        self.or_mask = 1
        self.and_mask = 254
        
    # Update the masking values
    def updateMasks(self):
        self.and_mask -= self.orval
        self.orval = self.orval * 2
    
    # Get the binary version of 'val' with proper length
    def real_binary(self, val, ln):
        realbin = bin(val)[2:]
        while ln > len(realbin):
            realbin = '0' + realbin
        return realbin    
    
    # Hide text in class's image
    def text_hide(self, text):
        length_in_binary = self.real_binary(len(text), 16)
        self.hide_val(length_in_binary)
        for c in text:
            self.hide_val(self.real_binary(ord(c), 8))
        return self.image
    
    # Use mask to update passed in pixel value
    def mask_update(self,pxl, c):
        if int(c) == 0:
            return self.zero_out(pxl)
        else:
            return self.one_in(pxl)
    
    def zero_out(self, pxl):
        return int(pxl) & self.and_mask
    
    def one_in(self, pxl):
        return int(pxl) | self.orval

    # Hide pased in bits to current register in image
    def hide_val(self, bits):
        for c in bits:
            self.image[self.h,self.w][self.chan] = mask_update(self.image[self.h,self.w][self.chan], c)
            self.iterate()
    
    # Determine whether or not to update current value type (channel, width, height)
    def pu(self, val, maxVal): # possibly update (although really, we update no matter what)
        if (val != maxVal):
            return (val+1,True)
        return (0,False)
    
    # Move to next register
    def iterate(self):
        (self.chan, end) = self.pu(self.chan, self.channels-1)
        if (end):
            return
        
        (self.w, end) = self.pu(self.w, self.width-1)
        if (end):
            return

        (self.h, end) = self.pu(self.h, self.height-1)
        if (end):
            return
        
        # End of registers
        if self.orval == 128:
            raise Length("Input too large")
            
        self.updateMasks()
        
        
    # Reveal hidden text
    def text_seek(self):
        revealed = ""
        for i in range(int(self.next_bits(16),2)):
            revealed += chr(int(self.next_char() ,2))
        return revealed

    # Return only the next bit of current register
    def next_bit(self):
        val = self.orval & self.image[self.h,self.w][self.chan]
        self.iterate()
        if val == 0:
            return val
        else:
            return "1"
    
    # Get next bits and current current character 
    def next_char(self):
        return self.next_bits(8)
    
    # Return next number of bits, in string format
    def next_bits(self, ln):
        bits = ""
        for i in range(ln):
            bits += self.next_bit()
        return bits
    
    class Length(Exception):
        pass