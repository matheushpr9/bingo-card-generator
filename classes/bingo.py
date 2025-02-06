import random
import datetime


class Bingo:
    def __init__(self):
        self.bingo_card = {
            "B":[],
            "I":[],
            "N":[],
            "G":[],
            "O":[]
        }
    def get_bingo_numbers(self):

        b = [i+1 for i in range(0,15)]
        i = [i+1 for i in range(15,30)]
        n = [i+1 for i in range(30,45)]
        g = [i+1 for i in range(45,60)]
        o = [i+1 for i in range(60,75)]


        return [b,i,n,g,o]
    
    def get_bingo_card(self):
        bingo_numbers = self.get_bingo_numbers()

        for  index, letter in enumerate(self.bingo_card):
            numbers=bingo_numbers[index]
            count =0
            while count<5:
                if count == 2 and letter == "N":
                    self.bingo_card[letter].append("special")
                    count =count+1
                    continue
                random.seed(datetime.datetime.now().timestamp())
                random_index = random.randint(0,len(numbers)-1)
                self.bingo_card[letter].append(numbers[random_index])
                numbers.pop(random_index)
                count =count+1

        
                
        return self.bingo_card
        

    
    