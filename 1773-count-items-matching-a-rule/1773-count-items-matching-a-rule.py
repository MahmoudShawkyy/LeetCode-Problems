class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        typee,colorr,name=False,False,False
        answer=0
        if ruleKey=="type":
            typee=True
        elif ruleKey=="color":
            colorr=True
        else:
            namee=True
        
        for i in range(len(items)):
            if typee:
                if items[i][0]==ruleValue:
                    answer+=1
            elif colorr:
                if items[i][1]==ruleValue:
                    answer+=1
            else:
                if items[i][2]==ruleValue:
                    answer+=1
                    
        return  answer
            
                