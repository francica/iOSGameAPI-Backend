__author__ = 'Robert'


from Words.models import Word

class WordManager():

    def __init__(self):
        self.word={}

    def add_word(self,word):
        try:
            temp=Word(text=word)
            temp.save()
            return temp.word_id
        except:
            return -1

    def get_word(self,room_id):
        word_obj=Word.objects.order_by('?').first()
        self.word[room_id]=word_obj.text
        return word_obj

    def verify_word(self,room_id,guess):

        if self.word[room_id]==guess:
            word_obj=Word.objects.get(text=guess)
            word_obj.score+=1
            word_obj.save()


            return True
        else:
            print(self.word[room_id])
            print(guess)
            return False

