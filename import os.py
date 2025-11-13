import os
import time

# Dos "fotogramas" circulares en texto ASCII
frame1 = """
   ***   
 *     *
*       *
 *     *
   ***   
"""

frame2 = """
    *    
  *   *  
 *     * 
  *   *  
    *    
"""

# Animación infinita
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame1)
    time.sleep(0.3)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame2)
    time.sleep(0.3)
