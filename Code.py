class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        f = 'n'
        t = []
        c = [0, 0]
        obstacles = set(tuple(obstacle) for obstacle in obstacles)
        
        for i in commands:
            if i != -1 and i != -2:
                new_c = c[:]
                if f == 'n':
                    for j in range(i):
                        new_c[1] += 1
                        if tuple(new_c) in obstacles:
                            new_c[1] -= 1
                            break
                elif f == 'e':
                    for j in range(i):
                        new_c[0] += 1
                        if tuple(new_c) in obstacles:
                            new_c[0] -= 1
                            break
                elif f == 's':
                    for j in range(i):
                        new_c[1] -= 1
                        if tuple(new_c) in obstacles:
                            new_c[1] += 1
                            break
                elif f == 'w':
                    for j in range(i):
                        new_c[0] -= 1
                        if tuple(new_c) in obstacles:
                            new_c[0] += 1
                            break
                c = new_c
                t.append(c[0]**2 + c[1]**2)
            elif i == -1:
                if f == 'n':
                    f = 'e'
                elif f == 'e':
                    f = 's'
                elif f == 's':
                    f = 'w'
                elif f == 'w':
                    f = 'n'
            elif i == -2:
                if f == 'n':
                    f = 'w'
                elif f == 'w':
                    f = 's'
                elif f == 's':
                    f = 'e'
                elif f == 'e':
                    f = 'n'
        return max(t)
