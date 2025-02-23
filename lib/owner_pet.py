class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name, pet_type, owner=None):
        self.pet_type = pet_type
        self.owner = owner
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"invalid pet type: {self.pet_type} must be one of: {Pet.PET_TYPES}")
        
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner class")

    
        Pet.all.append(self)
   

class Owner:
    def __init__(self,name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet, Pet) and pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)




owner1 = Owner("John")
owner2 = Owner("Alice")

pet1 = Pet("Buddy", "dog", owner1)
pet2 = Pet("Whiskers", "cat", owner2)
pet3 = Pet("Crock", "reptile", owner1)
pet4 = Pet("Badie", "bird", owner2)


owner1.add_pet(pet1)  
owner1.add_pet(pet2) 
owner2.add_pet(pet3) 
owner2.add_pet(pet4)   


print(f"{owner1.name}'s sorted pets: {[pet.name for pet in owner1.get_sorted_pets()]}")  
print(f"{owner2.name}'s sorted pets: {[pet.name for pet in owner2.get_sorted_pets()]}") 
   
        