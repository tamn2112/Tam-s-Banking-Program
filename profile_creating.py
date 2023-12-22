# Creating A Profile For User 
class UserProfile:
    def __init__(self):
        self._profile_data = {}

    def get_user_info(self):
        self._profile_data['Name'] = input("What is your full name? ")
        self._profile_data['Age'] = input("Please enter your age: ")
        self._profile_data["Gender"] = input("Please enter your gender (F / M / NB): ")

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            profile_str = f"Name: {self._profile_data['Name']}, Age: {self._profile_data['Age']}, Gender: {self._profile_data['Gender']}\n"
            file.write(profile_str)
            file.write('\n')






    
    

    
    


    

