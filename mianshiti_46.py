class Solution:

    def numToLis(self, num):
        lis = []
        while num:
            t = num % 10
            lis.append(t)
            num = int(num / 10)
        lis.reverse()
        return lis

    def numMetCom(self, l):
        if l == 1:
            return 2
        elif l == 2:
            return 3
        else:
            return self.numMetCom(l - 1) + self.numMetCom(l - 2)

    def translateNum(self, num: int) -> int:       
        list_num = self.numToLis(num)
        len_com = []
        tmp_len = 0
        for i in range(len(list_num)):
            if list_num[i] == 1 or list_num[i] == 2:
                tmp_len += 1
            else:
                if ((list_num[i - 1] == 1) or (list_num[i - 1] == 2 and list_num[i] <= 5)) and (tmp_len > 0):
                    len_com.append(tmp_len)
                    tmp_len = 0
                elif tmp_len > 1:
                    tmp_len -= 1
                    len_com.append(tmp_len)
                    tmp_len = 0
                else:
                    tmp_len = 0
    
        if tmp_len > 1:
            tmp_len -= 1
            len_com.append(tmp_len)
        
        num_met = 1
        if len(len_com) != 0:
            for num in len_com:
                num_met *= self.numMetCom(num)
        
        return num_met
