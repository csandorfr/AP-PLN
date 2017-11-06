def weighted_sum_marcott(list_score,m):
        sum_link=0
        for i in range(0,len(list_score)):
                if i==0:
                        sum_link+=list_score[i]
                else:
                        sum_link+=list_score[i]/(float(m*i))
        return sum_link
