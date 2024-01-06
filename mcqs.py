class question:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



question_prompts = [
"what is the clolor of apples?\n(a)g/r\n(B)b\n(c)pink \n\n",

"what is the clolor of mangoo?\n(a)g\n(B)y\n(c)r \n\n",

"what is the clolor of malta?\n(a)g\n(B)b\n(c)r \n\n "

]



questions =[
     question(prompt = question_prompts[0], answer = 'a'),
     question(prompt = question_prompts[1], answer = 'b'),
     question(prompt = question_prompts[2],answer = 'c')
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got "+ str(score) + "/" + str(len(questions)) + " correct. ")        

run_test(questions)
