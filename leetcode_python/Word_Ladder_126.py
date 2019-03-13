#-*-coding:utf-8-*-
# 作者：jgz 
# 创建日期：2019/1/21 15:02   
#  IDE：PyCharm 
import queue

class Solution:
    def __init__(self):
        self.beginWord = beginWord
        self.endWord = endWord
        self.wordList = wordList
    def noly_one_letter_change(self,str1, str2):
        if len(str1) != len(str2):
            return False
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False

    def df(self,curr_word,curr_list,is_visited,curr_len,last_len,ret):
        if curr_len==last_len:
            return
        if curr_len == last_len-1 and self.noly_one_letter_change(curr_word,self.endWord):
            curr_list.append(self.endWord)
            ret.append(list(curr_list))
            curr_list.remove(self.endWord)
            return
        for i_word in self.wordList:
            if is_visited[i_word] == False and self.noly_one_letter_change(curr_word, i_word):
                curr_list.append(i_word)
                is_visited[i_word] = True
                self.df(i_word,curr_list,is_visited,curr_len+1,last_len,ret)
                curr_list.remove(i_word)
                is_visited[i_word] = False

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        min_word_len = self.ladderLength(beginWord, endWord, wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        is_visited = {}
        is_visited[beginWord] = True
        for i_word in wordList:
            is_visited[i_word] = False
        if min_word_len == 0:
            return []
        if min_word_len == 1:
            return [[beginWord]]
        ret ,curr_list= [],[beginWord]
        self.df(beginWord,curr_list,is_visited,curr_len=1,last_len=min_word_len,ret=ret)
        return ret

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if beginWord == endWord:
            return 1

        cur = queue.Queue()
        cur.put(beginWord)
        is_visited = {}
        is_visited[beginWord] = True
        for i_word in wordList:
            is_visited[i_word] = False
        layer = 2
        last,nlast = beginWord,None
        while cur.empty() == False:
            cur_word = cur.get()
            for i_word in wordList:
                if is_visited[i_word]==False and self.noly_one_letter_change(cur_word,i_word):
                # if self.noly_one_letter_change(cur_word, i_word):
                    if i_word==endWord:
                        return layer
                    else:
                        nlast = i_word
                        cur.put(i_word)
                        is_visited[i_word] = True
                        # wordList.remove(i_word)
            if last == cur_word:
                layer +=1
                last = nlast
        return 0



if __name__ == '__main__':
    beginWord = "cet"
    endWord = "ism"
    wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]

    # beginWord =  "hit"
    # endWord  = "cog"
    # wordList = ["hot", "cog", "dot", "dog", "hit", "lot", "log"]
    # print(Solution().ladderLength(beginWord,endWord,wordList))
    ret = Solution().findLadders(beginWord,endWord,wordList)
    for iCombine in ret:
        print(iCombine)
