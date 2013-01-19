'''
Created on Jan 19, 2013

@author: carl
'''

class HealthSystem:
    '''
    This class is the health point calculation system. It includes
    maximum health for each character, the solid and dynamic HP(Solid
    HP does not change if it is higher than critical point 2 and lower than 
    critical point 1, but 
    dynamic health drops regardless the total point is). Operation to
    hurt and recover, the function to get health. Critical points(CP) marks
    different behaviour of health: above CP1 solid health recovers automatically
    , between CP1 and 2 health remains same; between 2 and 3 health drops
    at rate 1; below 3 health drops at rate 2.
    '''


    def __init__(self, MaxHP):
        '''
        Constructor: Creates a new health system
        @param MaxHP: The maximum HP
        '''
        # TODO: Add critical points
        # Initialize maximum HP
        self.Maximum = int(MaxHP)
        # Initialize current HP
        self.currentHP = MaxHP
        # Initialize dynamic HP
        self.currentDynHP = 0
        
    def get(self):
        '''
        Returns current solid HP
        '''
        return self.currentHP
    
    def getDyn(self):
        '''
        Returns current dynamic HP
        '''
    
    def hurt(self, damage):
        '''
        Decreases total HP by damage which is pre-calculated.
        @return: Return true if character is still alive.
        '''
        self.currentDynHP -= damage
        if self.currentDynHP < 0:
            # Subtract the excess damage on dynamic HP from solid HP
            self.currentHP += self.currentDynHP
            self.currentDynHP = 0
        # Return true if still alive
        return self.currentHP > 0
    
    def recover(self, recovery):
        '''
        Increase dynamic HP by recovery which is pre-calculated.
        Can only recover 80% of total damage on solid HP.
        ''' 
        # Maximum HP after recovery, which is
        # current solid HP + 80% of total solid HP damage
        MaxAfterRecovery = (self.currentHP + 
                            (self.Maximum - self.currentHP) * 0.8)
        self.currentDynHP += recovery
        # If recovery is more than allowed, dynamic HP is set to
        # the difference between MaxAfterRecovery - current solid HP
        if self.currentDynHP > MaxAfterRecovery:
            self.currentDynHP = MaxAfterRecovery - self.currentHP
        
        