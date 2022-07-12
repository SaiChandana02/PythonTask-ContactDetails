class ContactDetails:
    def __init__(self,contactID,contactType,contactEmail):
        self.ContactDetailsId = contactID
        self.contactType = contactType
        self.ContactEmail = contactEmail

    def readContactDetails(self):
        print("contact details id is "+ self.ContactDetailsId)
        print("contact details Type "+self.contactType)
        print("contact details email "+ self.ContactEmail)
        
    def updateContactDetails(self,contactDetailsID,contactType,ContactEmail):
        self.ContactDetailsId = contactDetailsID
        self.contactType = contactType
        self.ContactEmail = ContactEmail



class Contact:
    isActive = True
    def __init__(self,contactID,firstName,lastName):
        self.contactID = contactID
        self.firstName = firstName
        self.lastName = lastName
        self.contactDetailsList = []

    def createContactDetails(self,contactDetailsID,contactType,contactEmail):
        newContactDetails = ContactDetails(contactDetailsID,contactType,contactEmail)
        return newContactDetails

    def updateContact(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        return 

    def addContactDetails(self,contactID,contactType,contactEmail):
        newContactDetails = ContactDetails(contactID,contactType,contactEmail)
        self.contactDetailsList.append(newContactDetails)
        return 

    def readContactDetails(self,index):
        contactDetailsObj = self.contactDetailsList[index]
        contactDetailsObj.readContactDetails()
        return 

    def updateContactDetails(self,index,contactDetailsID,contactType,ContactEmail):
        contactDetailsObj = self.contactDetailsList[index]
        contactDetailsObj.updateContactDetails(contactDetailsID,contactType,ContactEmail)

    def deleteContactDetails(self,index):
        self.contactDetailsList.pop(index)
        return True
        
        



class User:
    isActive = True
    isAdmin = False
    def __init__(self,userID,firstName,lastName,isAdmin):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.isAdmin = isAdmin

    def __isUserActive(self):
        if self.isActive==False:
          print("you are not active cannot read contacts")
          return False 
        return True

    def createUser(self,userID,fName,LName):
        if self.isAdmin ==False:
            print("you are not a admin you cannot create a new user")
            return 
        newUser = User(userID,fName,LName,False)
        return newUser    

    def readUser(self,user):
        if self.isAdmin == False:
           print("you are not a admin you cannot read a user's data")
           return    
        if user.isActive == False:
            print("user is not active")
            return 
        print("user First Name "+user.firstName)
        print("user Last Name "+user.lastName)
        print("user userId "+user.userID)
        if user.isAdmin == False:
            print("user is staff")
        else:
            print("user is Admin")
        
    def updateUser(self,user,fName,LName,userId,isAdmin,isActive):
        if self.isAdmin == False:
           print("you are not admin you cannot update a user's data")
           return  
        if user.isActive == False:
           print("user is not active")
           return  
        user.firstName = fName
        user.lastName = LName
        user.userId = userId
        user.isAdmin = isAdmin
        user.isActive = isActive

    def deleteUser(self,user):
        if self.isAdmin == False:
           print("you are not admin you cannot delete a user")
           return  
        user.isActive = False
        return 

    def addContact(self,contactId,firstName,lastName):
        if self.isAdmin == True or self.isActive==False:
            print("you cannot add contacts")
            return 
        newContact =  Contact(contactId,firstName,lastName)
        self.Usercontacts.append(newContact)

    def readContact(self,index):
        if self.isActive==False:
            print("you are not active cannot read contacts")
            return 
        contact =  self.Usercontacts[index]
        print("contact ID is "+contact.contactID)
        print("contact First Name is "+contact.firstName)
        print("contact lastName is "+contact.lastName)
        return 

    def updateContacts(self,index,firstName,lastName):
        if self.isActive==False:
            print("you are not active cannot read contacts")
            return 
        contact =  self.Usercontacts[index]
        contact.updateContact(firstName,lastName)

    def deleteContact(self,index):
      if self.__isUserActive:
        self.Usercontacts.pop(index)
    
    def readContactDetails(self,contactIndex,contactDetailsIndex):
      if self.__isUserActive:
        contact = self.Usercontacts[contactIndex]
        contact.readContactDetails(contactDetailsIndex)
      return 

    def updateContactDetails(self,contacID,contactType,contactEmail,contactIndex,contactDetailsIndex):
      if self.__isUserActive:
         contact = self.Usercontacts[contactIndex]
         contact.updateContactDetails(contactDetailsIndex,contacID,contactType,contactEmail)
      return 

    def deleteContactDetails(self,contactIndex,contactDetailsIndex):
      if self.__isUserActive:
            contact = self.Usercontacts[contactIndex]
            contact.deleteContactDetails(contactDetailsIndex)
      return