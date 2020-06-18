
class Solution:

    def do_eq(self, a_str):
        if "==" in a_str:
            num1, num2 = a_str.split("==")
            a_set = set([num1, num2])
            print(a_set)
            find = []
            for i in range(len(self.eq)):
                if len(a_set & self.eq[i]) > 0:
                    find.append(i)
            if not find:
                self.eq.append(a_set)
            else:
                he_set = set(a_set)
                for i in find:
                    he_set |= self.eq[i]
                for i in find:
                    self.eq[i] =set()
                self.eq.append(he_set)


    def do_not_eq(self, a_str):
        if "!=" in a_str:
            num1, num2 = a_str.split("!=")
            if num1 == num2:
                self.can = False
            a_set = set([num1, num2])
            for i in self.eq:
                if len(a_set & i) == len(a_set):
                    self.can =False
                    break

    def equationsPossible(self, equations: list) -> bool:
        self.eq=[]
        self.can = True
        [self.do_eq(i) for i in equations]
        print(self.eq)
        [self.do_not_eq(i) for i in equations]
        return self.can
print(Solution().equationsPossible(["a==b","b!=c","c==a"]))