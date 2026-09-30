class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = []
        l, r = 0, len(people)-1
        while l <= r:
            if people[l] == limit:
                ans.append([people[l]])
                l+=1
                continue

            if people[r] == limit:
                ans.append([people[r]])
                r-=1
                continue
            
            if people[l]+people[r] == limit:
                ans.append([people[l], people[r]])
            else:
                if people[l] + people[r] > limit:
                    ans.append([people[r]])
                    r-=1
                    continue
                elif people[l] + people[r] < limit:
                    ans.append([people[r]])
                # else:
                #     ans.append([people[l]])
                #     l+=1    
                #     continue
            l, r = l+1, r-1
        print(ans)
        return len(ans)