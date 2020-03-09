'''
Dieses Package enthält alle erweiterten Beispiele zum Kurs py4e, in denen sowohl die Beispiele aus dem Kurs, als auch
weitere Beispiele enthalten sind. Jedes Kapitel soll einen möglichst umfassenden Einblick in die Sprache Python, sowie
'best practices' aufzeigen.

@author: morrigan
@see: https://www.py4e.com/lessons 
'''

'''
Gibt vorhandene Informationen zu einer Aufgabe auf der Konsole aus
@param question: Frage oder Beschreibung einer Aufgabe
@param code:   
'''
def print_exercise(question, code=None, possible_answers=None, correct_answer=None):
    print(question)
    if(code is not None and len(code) > 0):
        print(code)
    if(possible_answers is not None):    
        for pa in possible_answers:
            print(pa)
    if(correct_answer is not None):        
        print("Answer:")    
        if(type(correct_answer) is int):
            print(possible_answers[correct_answer])
        else:
            print(correct_answer)
    print()

def print_header(header):
    print()
    print(header)
    print("=" * len(header))
    print()   