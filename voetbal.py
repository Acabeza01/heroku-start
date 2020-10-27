from bs4 import BeautifulSoup
import requests
import xlrd

def haalRanglijst(url):
    page = requests.get("https://www.voetbalzone.nl/competitie.asp?uid="+str(url))
    soup = BeautifulSoup(page.content, 'html.parser')

    stand = soup.find_all(class_="c-team b")

    ranglijst = []
    for a in stand:
        club = a.get_text().strip()
        if (club != "Team"):
            ranglijst.append(club)
    print(ranglijst)
    return ranglijst

def haalLijst(land):

    if (land == 'NL'):
            url = 1
            blad = 'Ned'
            deelnemers = 5
    elif (land == 'UK'):
            url = 8
            blad = 'Eng'
            deelnemers = 2
    elif (land == 'SP'):
            url = 7
            blad = "Spa"
            deelnemers = 2
    else:
            url = ""
            blad = ""

    ranglijst = haalRanglijst(url)

    def haalOp2(land, col_idx):
        if land == 'NL':
            row_vals =[
                ['PSV', 'Ajax', 'Feyenoord', 'FC Utrecht', 'AZ', 'Vitesse', 'Willem II', 'FC Groningen', 
                'Heracles Almelo', 'sc Heerenveen', 'PEC Zwolle', 'FC Twente', 'Sparta Rotterdam', 'FC Emmen', 
                'Fortuna Sittard', 'ADO Den Haag', 'VVV-Venlo', 'RKC Waalwijk'],
                ['Ajax', 'Feyenoord', 'PSV', 'AZ', 'Vitesse', 'FC Utrecht', 'FC Groningen', 'Willem II',
                'PEC Zwolle', 'sc Heerenveen', 'Sparta Rotterdam', 'Heracles Almelo', 'FC Twente', 'FC Emmen',
                'ADO Den Haag', 'RKC Waalwijk', 'VVV-Venlo', 'Fortuna Sittard'],
                ['Ajax', 'AZ', 'Feyenoord', 'PSV', 'Willem II', 'FC Utrecht', 'Vitesse', 'FC Groningen', 
                'FC Twente', 'sc Heerenveen', 'Sparta Rotterdam', 'Heracles Almelo', 'PEC Zwolle', 'FC Emmen', 
                'ADO Den Haag', 'Fortuna Sittard', 'VVV-Venlo', 'RKC Waalwijk'],
                ['PSV', 'Feyenoord', 'Ajax', 'AZ', 'FC Utrecht', 'FC Groningen', 'Willem II', 'Vitesse',
                'sc Heerenveen', 'Sparta Rotterdam', 'PEC Zwolle', 'ADO Den Haag', 'VVV-Venlo', 'FC Twente',
                'Heracles Almelo', 'FC Emmen', 'Fortuna Sittard', 'RKC Waalwijk'],
                ['Ajax', 'Feyenoord', 'AZ', 'PSV', 'FC Utrecht', 'Vitesse', 'Willem II', 'Heracles Almelo',
                'FC Groningen', 'Sparta Rotterdam', 'sc Heerenveen', 'PEC Zwolle', 'FC Twente', 'FC Emmen',
                'ADO Den Haag', 'VVV-Venlo', 'Fortuna Sittard', 'RKC Waalwijk']
            ]
        elif land == 'SP':
            row_vals =[
                ['Barcelona', 'Real Madrid', 'Atlético Madrid', 'Villarreal', 'Sevilla', 'Real Sociedad', 
                'Getafe', 'Real Betis', 'Athletic Club', 'Valencia', 'Granada', 'Celta de Vigo', 'Osasuna', 
                'Levante', 'SD Eibar', 'Real Valladolid', 'Elche', 'FC Cadiz', 'Alavés', 'Huesca'],
                ['Real Madrid', 'Atlético Madrid', 'Barcelona', 'Sevilla', 'Athletic Club', 'Real Sociedad',
                 'Villareal', 'Getafe', 'Real Betis', 'Osasuna', 'Valencia', 'Granada', 'Celta de Vigo',
                  'Levante', 'Real Valladolid', 'SD Eibar', 'Alavés', 'Huesca', 'FC Cadiz', 'Elche']
            ]
        elif land == 'UK':
            row_vals = [
                ['Manchester City', 'Liverpool', 'Chelsea', 'Manchester United', 'Arsenal', 'Tottenham Hotspur',
                 'Wolverhampton W.', 'Everton', 'Leicester City', 'Leeds United', 'Newcastle United',
                  'Sheffield United', 'Southampton', 'Crystal Palace', 'Brighton & Hove Albion',
                   'West Ham United', 'Burnley', 'Aston Villa', 'West Bromwich Albion', 'Fulham'],
                ['Manchester City', 'Chelsea', 'Liverpool', 'Arsenal', 'Manchester United', 'Leicester City',
                 'Tottenham Hotspur', 'Wolverhampton W.', 'Everton', 'Newcastle United', 'Southampton',
                  'Sheffield United', 'Leeds United', 'Crystal Palace', 'Burnley', 'West Ham United',
                   'Brighton & Hove Albion', 'Aston Villa', 'West Bromwich Albion', 'Fulham']
             ]
            
        return row_vals[col_idx]

    def haalNamen(land):
        if land == 'NL':
            return ['Arjan', 'Linda', 'Bram', 'Thijs', 'Rick']
        elif land == 'SP':
            return ['Arjan', 'Rick']
        elif land == 'UK':
            return ['Arjan', 'Rick']

    class Score:
        def __init__ (self, col_idx, land):
            self.name = haalNamen(land)[col_idx]
            self.dist, self.vol = verschil(ranglijst, haalOp2(land, col_idx))

        def getScore(self):
            score = f"{self.name} {self.dist} {self.vol}"
            return score

        def getNaam(self):
            naam = f"{self.name}"
            return naam

        def getDist(self):
            return self.dist

        def getVol(self):
            return self.vol

    def verschil(arr, ar2):
        teller = 0
        voltreffer = 0
        for i in range (0, len(arr)):
            subteller = 0
            for j in range (0, len(ar2)):
                if arr[i] == ar2[j]:
                    subteller += abs(i - j)
                    if (i==j):
                        voltreffer += 1
            teller += subteller

        return (teller, voltreffer)

    lijst = []
    for i in range(0,deelnemers):
        lijst.append(Score(i, land))

    import operator
    sortedLijst = sorted(lijst, key=operator.attrgetter('vol'), reverse=True)
    sortedLijst = sorted(sortedLijst, key=operator.attrgetter('dist'))

    for i in sortedLijst:
        print(i.getScore())

    return sortedLijst

def ChampionsLeague() :
    page = requests.get("https://www.voetbalzone.nl/competitie.asp?uid=10")
    soup = BeautifulSoup(page.content, 'html.parser')

    stand = soup.find_all(class_="c-team b")
    pnt = soup.find_all(class_="c-punt j")

    ploegen = []
    for a in stand:
        ploegen.append(a.get_text().strip())
    print (ploegen)
    punten = []
    for b in pnt:
        punten.append(b.get_text())
    print (punten)

    puntenR = 0
    puntenA = 0
    result = {}
    for i in range (len(ploegen)):
        if ploegen[i] in ('Bayern München', 'Manchester City', 'Liverpool', 'Chelsea' ):
            result[ploegen[i]] = punten[i]
            puntenR += int(punten[i])
    result['Totaal Rick'] = puntenR   
    for i in range (len(ploegen)):             
        if ploegen[i] in ('Barcelona', 'Paris Saint-Germain', 'Real Madrid', 'Borussia Dortmund' ):
            result[ploegen[i]] = punten[i]
            puntenA += int(punten[i])
    result['Totaal Arjan'] = puntenA

    for key in result:
        print( f"{key} {result[key]}")
    return (result) 

    # ranglijst = []
    # for a in stand:
    #     club = a.get_text().strip()
    #     if (club != "Team"):
    #         ranglijst.append(club)
    # print(ranglijst)
    # return ranglijst


if __name__ == '__main__':
    haalLijst()   