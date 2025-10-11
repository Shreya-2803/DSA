from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0
        damage_map=Counter(power)
        for k in damage_map:
            damage_map[k]*=k
        values=sorted(damage_map.keys())
        n=len(values)
        dp=[0]*n
        dp[0]=damage_map[values[0]]
        for i in range(1,n):
            curr_damage=damage_map[values[i]]
            j=i-1
            while j>=0 and values[i]-values[j]<=2:
                j-=1
            if j>=0:
                dp[i]=max(dp[i-1],dp[j]+curr_damage)
            else:
                dp[i]=max(dp[i-1],curr_damage)
        return dp[-1]
        