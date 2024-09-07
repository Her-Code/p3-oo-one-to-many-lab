class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Valid types are: {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if isinstance(owner, Owner):
            owner.add_pet(self)

    # def pets(self):
    #     return [pet for pet in Pet.all if pet.owner == self]
    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class")
        
        if self.owner is not None:
            self.owner.remove_pet(self)
        
        self.owner = owner
        owner.add_pet(self)

class Owner:
    def __init__(self,name):
        self.name = name
        self.pets_list = []
    
    # def add_pet(self, pet):
    #     """Add a pet to the owner, validating that it is an instance of Pet."""
    #     if not isinstance(pet, Pet):
    #         raise Exception("Only Pet instances can be added.")
    #     pet.owner = self

    # def get_sorted_pets(self):
    #     """Return a list of pets owned by the owner, sorted by name."""
    #     return sorted(self.pets(), key=lambda pet: pet.name)
    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class")
        
        if pet not in self.pets_list:
            self.pets_list.append(pet)
            pet.owner = self

    def remove_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class")
        
        if pet in self.pets_list:
            self.pets_list.remove(pet)
            pet.owner = None

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
