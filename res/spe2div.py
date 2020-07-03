file = open("specialite_medecine.txt",'r', encoding="utf-8")
out = open("speHtml.txt",'w', encoding="utf-8")
import re



option="""								<div class = "options">
									
									<input type="radio" class="option" id="bla">
									<label for="bla">bla</label>
								</div>"""



for spe in file:
    
    spe=re.sub("\n","",spe)
    div=re.sub("bla",spe,option)

    out.write(div+"\n")

        
        
file.close()
out.close()