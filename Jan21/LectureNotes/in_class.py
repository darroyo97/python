class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.count = 0

    def greeting(self):
        print(f'Hello {self.name} !')
        self.count += 1

    def printCount(self):
        print(self.count)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def friend_list(self, friend_name):
        self.friend_name = friend_name
        self.friends.append(friend_name)
        print(self.friends)
        print(len(self.friends))

    def contact_info(self):
        print(
            f'Hello my name is {self.name} and my email is {self.email} also  \t my number is {self.phone}')
        # print(self.email)
        # print(self.phone)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3455")
# sonny.friend_list("jordan")
# sonny.friend_list("joe")

sonny.greeting()
sonny.greeting()
sonny.greeting()
sonny.printCount()
# sonny.greet(jordan)
# jordan.greet(sonny)
# sonny.contact_info()
# jordan.contact_info()
