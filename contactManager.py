contacts = []



def addContact():
    print(' Add a new Contact')
    name = input('Name of Contact: ')       
    countryCode = input('Telephon County Code: ')
    areaCode = input('Area Code from Contact:  ')
    localCode = input(' Local Number from Contact:  ')

    contactPhonNumber = (countryCode, areaCode, localCode)
    
    contactStreetName = input("Enter your Street Name:  ")
    contactCityName = input("Enter your City Name:  ")
    
    contactAdress = (contactCityName, contactStreetName)
    contactInfomation = {
        'name1' : name,
        'contactPhonNumber1' : contactPhonNumber,
        'contactAdress1' : contactAdress
    }
    # return contactInfomation
    contacts.append(contactInfomation)
    print(name,'has been added')


def showAllContacts():
    print(contacts)
    if not contacts:
        print('No Contact in List !!')
        return 
    for i, contact in enumerate(contacts):
        print('Contact', i+1)
        # print('Name', contact)
        print(f"Phone { contact['contactPhonNumber1'][0]} {contact['contactPhonNumber1'][1]} - {contact['contactPhonNumber1'][2]}")
        print(f"Adress { contact['contactAdress1'][0]} {contact['contactAdress1'][1]}")

def contactManager():
    while True:
        print('Menu')
        print('Add a Contact press 1')
        print('Show all Contacts press 2')
        print('Exit press 3')
        choice = input('Enter your Choice: ')
        if choice == '1' :
            addContact()
            
        elif choice == '2':
            showAllContacts()
        
        elif choice == '3': 
            break
        else:
            print('Enter a Valid Option')

if __name__ == "__main__":
    contactManager()

