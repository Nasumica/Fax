import math
from scipy.special import erfinv

class StatCalc:
    SQRT2 = 2 ** 0.5
    def __init__(self, *cat: str):
        '''
        ### Statistical calculator
        '''
        self.Cat = ""
        self.Reset(*cat)
    def Reset(self, *cat: str):
        '''
        ### Reset calculator
        '''
        if len(cat) > 0: self.Cat = cat[0]
        self.Cnt = 0
        self.Sum = 0
        self.Min = 0
        self.Max = 0
        self.Sqr = 0
        self.Nul = 0
        self.Val = 0
    def Add(self, *v):
        '''
        ### Add values to calculator
        '''
        for x in v:
            if self.Cnt == 0:
                self.Min = self.Max = x
            elif self.Min > x:
                self.Min = x
            elif self.Max < x:
                self.Max = x
            self.Cnt += 1
            self.Sum += x
            self.Sqr += x * x
            self.Val = x
            if x == 0: self.Nul += 1
    def Same(self):
        '''
        ### Is Min = Max?
        '''
        return self.Min == self.Max
    def Average(self):
        '''
        ### Average (μ)
        '''
        if self.Same(): return self.Min
        return self.Sum / self.Cnt
    def Var(self):
        '''
        ### Variance
        '''
        if self.Same(): return 0
        μ = self.Average()
        v = self.Sqr / self.Cnt - μ * μ
        if v < 0: return 0 # ensure if rounding error
        return v
    def StDev(self):
        '''
        ### Standard deviation (σ)
        '''
        return self.Var() ** 0.5
    def Error(self):
        '''
        ### Standard errpr
        '''
        if self.Same(): return 0
        return (self.Var() / self.Cnt) ** 0.5
    def Margin(self, level: float):
        '''
        ### Confidence interval margin
        level must be in range [0, 1]

        <code>
        CI(level) = Average() ± Margin(level)
        </code>
        '''
        if level <= 0 or self.Same(): return 0
        if level >= 1: return math.inf 
        return erfinv(level) * self.Error() * self.SQRT2
    def Zscore(self, x):
        '''
        ### Z-score
        '''
        μ = self.Average()
        if x == μ: return 0
        σ = self.StDev()
        if σ == 0: return math.nan
        return (x - μ) / σ
    def Report(self):
        '''
        ### Print report
        '''
        print()
        print(self.Cat)
        print("Cnt =", self.Cnt)
        if self.Cnt > 0:
            print("Sum =", self.Sum)
            print("Min =", self.Min)
            print("Max =", self.Max)
        if self.Min != self.Max:
            print("Avg =", self.Average())
            print("Dev =", self.StDev())
        if self.Nul > 0: print("Nul =", self.Nul)


def sctest():
    s = StatCalc("test")
    s.Add(2, 4, 4, 4, 5, 5, 7, 9)
    s.Report()
    x = 3
    print("Z-score (",x,") =",s.Zscore(x))
    level = 95
    print("Margin (",level,"% ) =",s.Margin(level/100))
