class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # undirected graph with no weights
        adjList = {}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account) - 1):
                cur_email = account[i]
                next_email = account[i + 1]
                # create forward edge
                if cur_email not in adjList:
                    adjList[cur_email] = [next_email]
                else:
                    adjList[cur_email].append(next_email)
                # create backward edge
                if next_email not in adjList:
                    adjList[next_email] = [cur_email]
                else:
                    adjList[next_email].append(cur_email)
            # edge case: when there is only one email under the name
            if len(account) == 2:
                adjList[account[1]] = []

        res = []
        visited = set()
        for account in accounts:
            name = account[0]

            # collect all emails belonging to the person
            src = account[1]

            # we have found the person before
            if src in visited:
                continue
            
            # breadth first search
            emails = []
            queue = [src]
            while queue:
                cur = queue.pop(0)
                emails.append(cur)
                visited.add(cur)

                neighbors = adjList[cur]
                for nb in neighbors:
                    if nb not in visited:
                        queue.append(nb)
                        visited.add(nb)
            emails.sort()
            emails = [name] + emails
            res.append(emails)

        return res