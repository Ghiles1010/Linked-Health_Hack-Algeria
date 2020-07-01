import json, re

file = open("maladies.txt",'r',encoding="utf-8")
out = open("maladiesHtml.txt",'w',encoding="utf-8")

dup=[]

option="""								<div class = "options">
									
									<input type="radio" class="option" id="bla">
									<label for="bla">bla</label>
								</div>"""

for i in file:


    field=json.loads(i,encoding="utf-8")

    for ill in list(field.values())[0]:

        ill=re.sub("^ +","",ill)
        ill=re.sub("( +);?$","",ill)

        if ill not in dup:
            
            dup.append(ill)
            div=re.sub("bla",ill,option)

            #print(div)
            out.write(div+"\n")
        
        else:
            print("ok")

file.close()
out.close()

